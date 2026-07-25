# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
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


def fold_fullwidth(s: str):
    """Fold the FULLWIDTH ASCII block (a compatibility carrier) to its ASCII form:
    U+FF01..U+FF5E -> U+0021..U+007E (offset 0xFEE0), and IDEOGRAPHIC SPACE
    U+3000 -> U+0020. This is the fullwidth slice of NFKC, done explicitly so a
    fullwidth-encoded attack (＜script＞, １２７．０．０．１, paypa1 as ｐａｙｐａ1) is
    revealed to the readers underneath — the same "double bottom" as overlong.

    SCOPE (deliberately narrow, to avoid false positives): ONLY the fullwidth
    ASCII variants FF01..FF5E and U+3000. Halfwidth katakana (FF61..FF9F) and the
    fullwidth white brackets (FF5F..FF60) are REAL characters, not ASCII carriers,
    and are left untouched. Returns (folded, present)."""
    out, present = [], False
    for ch in s:
        o = ord(ch)
        if 0xFF01 <= o <= 0xFF5E:
            out.append(chr(o - 0xFEE0)); present = True
        elif o == 0x3000:
            out.append(" "); present = True
        else:
            out.append(ch)
    return "".join(out), present


def _build_math_fold():
    """Map every MATHEMATICAL ALPHANUMERIC letter/digit to its ASCII base.

    Source is restricted on purpose: the Mathematical Alphanumeric Symbols block
    (U+1D400..U+1D7FF) PLUS the ~29 math styles that live as 'holes' in the
    Letterlike Symbols block (ℂ ℎ ℬ ℑ ℝ …, U+2100..U+214F). We take the ASCII
    value from NFKC but keep the SOURCE list narrow so ordinary compatibility
    characters (², ½, №, ™, Ω, ℹ) are NOT touched. Built once at import."""
    import unicodedata as _u
    fold = {}
    for o in range(0x1D400, 0x1D800):
        nf = _u.normalize("NFKC", chr(o))
        if len(nf) == 1 and nf.isascii() and nf.isalnum():
            fold[o] = nf
    _KEEP = ("SCRIPT", "FRAKTUR", "BLACK-LETTER", "DOUBLE-STRUCK", "ITALIC")
    for o in range(0x2100, 0x2150):
        ch = chr(o)
        try:
            name = _u.name(ch)
        except ValueError:
            continue
        nf = _u.normalize("NFKC", ch)
        if len(nf) == 1 and nf.isascii() and nf.isalpha() and any(k in name for k in _KEEP):
            fold[o] = nf
    # math letters whose Unicode NAME carries no style keyword: U+210E PLANCK
    # CONSTANT is the mathematical italic small h (its 1D-block slot is reserved).
    fold[0x210E] = "h"
    return fold


_MATH_FOLD = _build_math_fold()


def fold_math_alnum(s: str):
    """Fold mathematical-alphanumeric styling (a compatibility carrier) to ASCII:
    𝐩𝐚𝐲𝐩𝐚𝐥 → paypal, 𝕏 → X, ℝ → R. Same "double bottom" as fullwidth — a styled
    attack (𝗌𝖼𝗋𝗂𝗉𝗍, math-styled brand) is revealed to the readers underneath.
    Only the curated math source set folds (see _build_math_fold). Returns
    (folded, present)."""
    out, present = [], False
    for ch in s:
        r = _MATH_FOLD.get(ord(ch))
        if r is not None:
            out.append(r); present = True
        else:
            out.append(ch)
    return "".join(out), present


# Unicode spaces that a filter-evader uses in place of a normal space. Folded to
# a plain ASCII space so downstream sees one canonical spacing. ZERO-WIDTH marks
# (U+200B/200C/200D/FEFF) are NOT here — they are invisible smuggles, judged by
# the invisible detector, not spaces. U+3000 is already folded by fold_fullwidth.
_SPACE_FOLD = ({0x00A0, 0x1680, 0x202F, 0x205F} | set(range(0x2000, 0x200B)))


def fold_spaces(s: str):
    """Fold non-ASCII whitespace (NBSP, en/em/thin/hair spaces, U+202F, U+205F,
    ogham space) to a plain ASCII space, so a space-substitution evasion is peeled
    to one canonical form. Returns (folded, present)."""
    out, present = [], False
    for ch in s:
        if ord(ch) in _SPACE_FOLD:
            out.append(" "); present = True
        else:
            out.append(ch)
    return "".join(out), present


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
    folded, fullwidth = fold_fullwidth(decoded)   # peel the fullwidth carrier
    folded, math = fold_math_alnum(folded)        # peel math-alphanumeric styling
    folded, wspace = fold_spaces(folded)          # peel non-ASCII space carriers
    canon = normalize_ip_hosts(folded)            # after folds: styled IPs normalize too
    return canon, {"decode_passes": passes, "overlong_utf8": overlong,
                   "fullwidth": fullwidth, "math_styled": math,
                   "weird_space": wspace, "changed": canon != text}
