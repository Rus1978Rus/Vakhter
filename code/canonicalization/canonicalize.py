# -*- coding: utf-8 -*-
"""
CANONICALIZATION_PRE_PASS v0.2 — closes the whole %XX space.

v0.1 handled the ASCII bands %0X..%7X (percent / HTML-entity / escapes).
v0.2 closes the HIGH bands %8X..%FX: percent-decode to RAW BYTES, then run a
LENIENT UTF-8 decoder that ALSO reveals OVERLONG forms — the classic evasion
where "/" is smuggled as %c0%af (2-byte) or %e0%80%af (3-byte). A strict
decoder rejects these; a vulnerable downstream accepts them and sees "/".
We reveal what that downstream would see AND flag overlong_present.

So the digit/hex bands 0-9 + A-F together cover all of %00..%FF; but the
ENFORCEMENT is here (decode + reject overlong), not 16 separate band cards.

Pure standard library. HONEST LIMITS unchanged (over-decode of explanatory
text; depth capped).
"""
import re
import html
import socket
import struct
import urllib.parse

_ESC = re.compile(r"\\u([0-9a-fA-F]{4})|\\x([0-9a-fA-F]{2})")
_PCT_RUN = re.compile(r"(?:%[0-9a-fA-F]{2})+")


def _decode_escapes(s: str) -> str:
    return _ESC.sub(lambda m: chr(int(m.group(1) or m.group(2), 16)), s)


def decode_utf8_lenient(bs: bytes):
    """Decode bytes as UTF-8 but ACCEPT overlong forms; flag if any seen.
    Reveals what a permissive downstream would render (the attack's target)."""
    out, over, i, n = [], False, 0, len(bs)
    while i < n:
        b = bs[i]
        if b < 0x80:
            out.append(chr(b)); i += 1
        elif 0xC0 <= b <= 0xDF and i + 1 < n:
            cp = ((b & 0x1F) << 6) | (bs[i+1] & 0x3F)
            if cp < 0x80:        over = True          # overlong 2-byte
            out.append(chr(cp)); i += 2
        elif 0xE0 <= b <= 0xEF and i + 2 < n:
            cp = ((b & 0x0F) << 12) | ((bs[i+1] & 0x3F) << 6) | (bs[i+2] & 0x3F)
            if cp < 0x800:       over = True          # overlong 3-byte
            out.append(chr(cp)); i += 3
        elif 0xF0 <= b <= 0xF4 and i + 3 < n:
            cp = ((b & 0x07) << 18) | ((bs[i+1] & 0x3F) << 12) | \
                 ((bs[i+2] & 0x3F) << 6) | (bs[i+3] & 0x3F)
            if cp < 0x10000:     over = True          # overlong 4-byte
            out.append(chr(cp) if cp <= 0x10FFFF else "�"); i += 4
        else:
            out.append(chr(b) if b < 0x100 else "�"); i += 1   # lone byte
    return "".join(out), over


def _decode_pct_runs(s: str):
    """Replace each %XX-run with its LENIENT-UTF8 decoding. Returns (s, overlong)."""
    seen = {"over": False}
    def repl(m):
        txt, over = decode_utf8_lenient(urllib.parse.unquote_to_bytes(m.group(0)))
        if over:
            seen["over"] = True
        return txt
    return _PCT_RUN.sub(repl, s), seen["over"]


def _one_pass(s: str):
    s = _decode_escapes(s)             # . \x2f
    s, over = _decode_pct_runs(s)      # %2e %2f  AND overlong %c0%af
    s = html.unescape(s)               # &#46; &#x2f; &#8203;
    return s, over


def decode_layers(text: str, max_depth: int = 3):
    cur, passes, overlong = text, 0, False
    for _ in range(max_depth):
        nxt, over = _one_pass(cur)
        overlong = overlong or over
        if nxt == cur:
            break
        cur, passes = nxt, passes + 1
    return cur, passes, overlong


def _int_to_ip(n):
    return socket.inet_ntoa(struct.pack("!I", n)) if 0 <= n <= 0xFFFFFFFF else None


def normalize_ip_hosts(text: str) -> str:
    def repl(m):
        scheme, host = m.group(1), m.group(2)
        try:
            n = int(host, 16) if host.lower().startswith("0x") else \
                int(host) if host.isdigit() else None
        except ValueError:
            n = None
        ip = _int_to_ip(n) if n is not None else None
        return f"{scheme}{ip}" if ip else m.group(0)
    return re.sub(r"(https?://)([^/\s:?#]+)", repl, text, flags=re.I)


def canonicalize(text: str, max_depth: int = 3):
    decoded, passes, overlong = decode_layers(text, max_depth)
    canon = normalize_ip_hosts(decoded)
    return canon, {"decode_passes": passes, "overlong_utf8": overlong,
                   "changed": canon != text}
