# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
data: URI detector card (SIMULATOR of a draft) — an embedded resource carrier.

A `data:` URI inlines a whole resource (data:<mediatype>[;base64],<payload>). It
is a legitimate way to embed a small image, but it is also a classic way to smuggle
an EXECUTABLE / MARKUP payload past a text filter: `data:text/html;base64,<script
…>` renders and runs in any HTML sink downstream. This is a STRUCTURAL signal —
the danger is the carrier + the payload's TYPE, not any natural-language meaning.

Autonomy note (AD-35): before this card the ONLY thing catching a data:text/html
payload was the external MSL engine; the demo's "data: URI in an upload" case
passed once MSL was made optional. This card closes that gap so the guard catches
it on its own.

Design — deliberately NOT "decode everything and re-scan" (the conveyor's M3
warning: a blind rescan escalates a benign inline image AND still misses a binary
dropper). Two narrow branches instead:

  1. EXECUTABLE MEDIATYPE (no decode) — the mediatype itself is a code/markup sink
     (text/html, image/svg+xml, application/javascript, application/x-*, …). A
     document/upload carrying such a data: URI is a smuggle regardless of payload.
     -> ALARM.
  2. BASE64 MAGIC SNIFF (bounded) — for a base64 payload under ANY mediatype,
     decode only the first few bytes and match a small set of unambiguous
     dangerous magics (<script / <!doctype html / <svg / <iframe markup; MZ / ELF
     native executables; #! shebang). This catches a MISLABELED dropper
     (data:image/png;base64,<a PE file>) without a full rescan.
     -> ALARM.

Benign and left CLEAN: data:image/{png,jpeg,gif,webp,bmp}, data:text/plain,
data:font/*, audio/*, video/* whose decoded head is inert (real PNG \x89PNG,
JPEG \xFF\xD8 … are not in the magic set).
"""
import base64
import re

from invariant_engine.core import Finding

# data:[<mediatype>][;param]*[;base64],   (payload follows the comma)
_DATA_URI = re.compile(
    r"data:([a-zA-Z0-9!#$&^_.+\-/*]*)((?:;[a-zA-Z0-9=\-.+]+)*)\s*,", re.I)

# mediatypes that are themselves an execution / markup sink
EXEC_MIME = {
    "text/html", "application/xhtml+xml", "image/svg+xml",
    "application/javascript", "text/javascript", "application/ecmascript",
    "text/ecmascript", "application/x-javascript",
}
EXEC_MIME_PREFIX = ("application/x-",)   # x-msdownload, x-sh, x-executable, x-msdos…

# unambiguous dangerous magics, matched on the decoded HEAD only
_MAGICS = [
    (b"<script", "html/script markup"),
    (b"<!doctype html", "html document"),
    (b"<html", "html markup"),
    (b"<svg", "svg markup (scriptable)"),
    (b"<iframe", "iframe markup"),
    (b"MZ", "PE/DOS executable"),
    (b"\x7fELF", "ELF executable"),
    (b"#!", "script shebang"),
]

_HEAD_B64 = 96          # decode at most this many base64 chars (bounded, ~72 bytes)


def _mime(mediatype):
    return (mediatype or "text/plain").split(";")[0].strip().lower()


def _is_exec_mime(mime):
    return mime in EXEC_MIME or mime.startswith(EXEC_MIME_PREFIX)


def _sniff_base64(payload):
    """Decode only the bounded head of a base64 payload and return a dangerous
    magic description, or None. Never raises; bounded work (no full decode)."""
    head = re.sub(r"\s", "", payload)[:_HEAD_B64]
    head += "=" * (-len(head) % 4)               # pad to a valid base64 length
    try:
        raw = base64.b64decode(head, validate=False)
    except Exception:
        return None
    low = raw[:32].lower()
    for magic, desc in _MAGICS:
        m = magic.lower() if magic.isascii() else magic
        if raw[:32].startswith(magic) or low.startswith(m):
            return desc
    return None


def data_uri_cards_reader(text):
    """data: URI authority: ALARM on an executable-mediatype or magic-sniffed
    dropper carrier; OK on inert inline resources / none present."""
    if "data:" not in text.lower():
        return Finding("clean", 0.0, "data-uri-cards: none present")

    for m in _DATA_URI.finditer(text):
        mediatype, params = m.group(1), m.group(2) or ""
        mime = _mime(mediatype)
        is_b64 = ";base64" in params.lower()

        # 1. executable / markup mediatype — carrier is a smuggle regardless of payload
        if _is_exec_mime(mime):
            return Finding("suspect", 0.9,
                f"data: URI carrying executable/markup type '{mime}' — a code sink "
                f"payload smuggled as an inline resource", conclusive=True,
                signature="data_uri_exec")

        # 2. bounded magic sniff of a base64 payload (mislabeled dropper)
        if is_b64:
            payload = text[m.end():m.end() + _HEAD_B64 + 8]
            desc = _sniff_base64(payload)
            if desc:
                return Finding("suspect", 0.9,
                    f"data: URI (declared '{mime}') base64 payload begins with "
                    f"{desc} — mislabeled executable/markup dropper", conclusive=True,
                    signature="data_uri_dropper")

    return Finding("clean", 0.0,
                   "data-uri-cards: inert inline resource(s) / no dangerous type")
