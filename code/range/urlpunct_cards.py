# -*- coding: utf-8 -*-
"""
URL-punctuation detector card (SIMULATOR of a draft) — visible structural
punctuation used to deceive: the dot / slash / at / colon family.

Design follows the proven MSL/MIP legacy cards (DOT U+002E ARTIFACT_CONFIRMED,
SOLIDUS U+002F scheme-patch, AT U+0040 userinfo model): the danger is not the
ASCII punctuation itself (it is everywhere in prose) but (a) LOOK-ALIKE
punctuation that renders like a URL delimiter yet is a different codepoint, and
(b) real ASCII punctuation used in a deceptive URL structure.

Two mechanism branches:
  1. PUNCT-LOOKALIKE — a dot/slash/at/colon look-alike (fullwidth, ideographic,
     ...) glued into a Latin/ASCII host-ish token. IDN resolvers normalize these
     to the ASCII delimiter, so `google。com` becomes `google.com` — a spoof.
     -> ALARM, with the ASCII skeleton shown.
  2. AT USERINFO (scheme-aware) — `LEFT@RIGHT` where LEFT already looks like a
     full domain (has a dot) and the context is URL-ish. Everything before `@`
     is userinfo, so `paypal.com@evil.ru` dials evil.ru. Ordinary email
     (`ivan@example.com`, no dot in the local part) and federated handles
     (`@user@server`) are NOT this. -> ALARM.

The ASCII dot is the shared pivot with the (future) numeric/IP card — this card
owns the dot FAMILY (ASCII + look-alikes); the numeric card will reuse the ASCII
dot for IPv4-like segmentation.
"""
from invariant_engine.core import Finding

DOT_LOOKALIKE   = {0x3002: ".", 0xFF0E: ".", 0xFF61: ".", 0x2024: ".", 0x2027: "."}
SLASH_LOOKALIKE = {0xFF0F: "/", 0x2215: "/", 0x2044: "/", 0x29F8: "/"}
AT_LOOKALIKE    = {0xFF20: "@", 0xFE6B: "@"}
COLON_LOOKALIKE = {0xFF1A: ":", 0x2236: ":", 0xA789: ":"}
PUNCT_LOOKALIKE = {}
for _m in (DOT_LOOKALIKE, SLASH_LOOKALIKE, AT_LOOKALIKE, COLON_LOOKALIKE):
    PUNCT_LOOKALIKE.update(_m)

NAME = {".": "dot", "/": "slash", "@": "at", ":": "colon"}


def _latin_alnum(ch):
    if not ch:
        return False
    o = ord(ch)
    return (0x30 <= o <= 0x39 or 0x41 <= o <= 0x5A or 0x61 <= o <= 0x7A
            or 0x00C0 <= o <= 0x024F)


def _hosttok(ch):
    """Characters that make up a host / URL token."""
    return _latin_alnum(ch) or ch in ".-_@:/"


def _skeleton(tok):
    return "".join(PUNCT_LOOKALIKE.get(ord(c), c) for c in tok)


def _tokens(text):
    toks, cur = [], []
    for ch in text:
        if _hosttok(ch) or ord(ch) in PUNCT_LOOKALIKE:
            cur.append(ch)
        elif cur:
            toks.append("".join(cur)); cur = []
    if cur:
        toks.append("".join(cur))
    return toks


def urlpunct_cards_reader(text):
    """URL-punct authority: ALARM lookalike-delimiter / at-userinfo / OK."""
    # 1. punctuation look-alike glued between Latin/ASCII host chars
    for i, ch in enumerate(text):
        o = ord(ch)
        if o in PUNCT_LOOKALIKE:
            prev = text[i - 1] if i > 0 else ""
            nxt = text[i + 1] if i + 1 < len(text) else ""
            if _latin_alnum(prev) and _latin_alnum(nxt):
                asc = PUNCT_LOOKALIKE[o]
                return Finding("suspect", 0.9,
                    f"URL {NAME[asc]} look-alike U+{o:04X} between host chars "
                    f"('{prev}<{NAME[asc]}>{nxt}') — normalizes to '{asc}' (spoof)",
                    conclusive=True, signature="urlpunct_lookalike")

    # 2. AT userinfo trick (scheme-aware): LEFT@RIGHT, LEFT already a dotted host
    url_context = "://" in text
    for tok in _tokens(text):
        if "@" not in tok:
            continue
        left, right = tok.split("@", 1)
        if right.startswith("@"):          # federated handle @user@server -> not userinfo
            continue
        left_is_domain = "." in left.strip(".") and _latin_alnum(left[:1] or "")
        right_is_host = "." in right
        if left_is_domain and right_is_host and (url_context or left.count(".") >= 1):
            return Finding("suspect", 0.88,
                f"userinfo spoof '{tok}' — everything before '@' ('{left}') is "
                f"userinfo; the real host is '{right}'",
                conclusive=True, signature="at_userinfo")

    return Finding("clean", 0.0, "urlpunct-cards: no look-alike delimiter / userinfo spoof")
