# -*- coding: utf-8 -*-
"""
canonical_view — a parser-DESYNC detector (SIMULATOR of a draft).

Every per-string card in this library judges ONE reading of the input. But a
whole class of attack lives in the GAP BETWEEN TWO readings: one component
strips a default-ignorable (a lenient canonicalizer, UTS #46, a browser), a
second keeps it (a raw byte consumer, a server). The SAME input is then two
different strings to two components — an allowlist clears `paypal.com` while a
fetcher dials `pay<ZWSP>pal.com`, or vice versa. A single-string reader is blind
to this by construction (this is the MSL/MIP "B5 parser-desync" blind spot).

The fix (per the invisible-guard design): carry TWO artifacts —
  raw_view       : the input, bit-for-bit
  canonical_view : the input with default-ignorables removed
with a bijective offset map between them, and FLAG when the two views resolve a
security-relevant TOKEN differently.

  DESYNC (conclusive): a default-ignorable was removed from BETWEEN two
    token characters, so raw_token != canonical_token — the string means two
    different things to two parsers.
  NO DESYNC: the invisible sits outside any token (e.g. between emoji), so both
    views resolve the same token — legit glue, no divergence.
"""
import unicodedata as u
from invariant_engine.core import Finding


def _default_ignorable(ch):
    """Approx Default_Ignorable: Cf + variation selectors + the Other_DI signs."""
    o = ord(ch)
    if u.category(ch) == "Cf":
        return o not in _CF_NOT_DI
    if 0xFE00 <= o <= 0xFE0F or 0xE0100 <= o <= 0xE01EF:   # variation selectors
        return True
    return o in _OTHER_DI


_CF_NOT_DI = ({0x600, 0x601, 0x602, 0x603, 0x604, 0x605, 0x6DD, 0x70F, 0x890, 0x891, 0x8E2,
               0x110BD, 0x110CD} | set(range(0xFFF9, 0xFFFC)) | set(range(0x13430, 0x13440)))
_OTHER_DI = ({0x034F, 0x115F, 0x1160, 0x17B4, 0x17B5, 0x180B, 0x180C, 0x180D, 0x180F,
              0x2065, 0x3164, 0xFFA0})


def canonical_view(text):
    """The canonical reading: default-ignorables removed. Returns (canon, offmap)
    where offmap[i] is the raw index of canon[i] (the bijective back-pointer)."""
    canon, offmap = [], []
    for i, ch in enumerate(text):
        if not _default_ignorable(ch):
            canon.append(ch); offmap.append(i)
    return "".join(canon), offmap


def _tokenish(ch):
    return bool(ch) and (ch.isalnum() or ch in ".-_@")   # domain / identifier chars


def canonical_view_reader(text):
    """Flag parser-desync: an invisible removed from inside a token."""
    canon, _ = canonical_view(text)
    if canon == text:
        return Finding("clean", 0.0, "canonical_view: raw == canonical (no divergence)")

    # find each removed invisible and ask whether it split a token
    for i, ch in enumerate(text):
        if _default_ignorable(ch):
            prev = text[i - 1] if i > 0 else ""
            nxt = text[i + 1] if i + 1 < len(text) else ""
            if _tokenish(prev) and _tokenish(nxt):
                return Finding("suspect", 0.9,
                    f"parser-desync: U+{ord(ch):04X} removed from inside a token "
                    f"('{prev}<di>{nxt}') — raw and canonical views disagree",
                    conclusive=True, signature="parser_desync")

    # invisibles present but none split a token (e.g. emoji glue) -> no desync
    return Finding("clean", 0.0,
                   "canonical_view: invisibles present but outside any token "
                   "(views agree on all tokens)")
