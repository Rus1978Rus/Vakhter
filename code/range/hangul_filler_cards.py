# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
Hangul-filler detector card (SIMULATOR of a draft) — invisible LETTER fillers.

These are the four default-ignorable Hangul fillers. Their trap is category:
they are category **Lo (Letter, other)** — they ARE letters — yet they render to
nothing. A "strip format / strip marks" filter never touches them because they
are neither Cf nor Mn. U+3164 HANGUL FILLER is the classic blank-username /
blank-nickname spoof (looks like an empty string but is a real character); the
choseong / jungseong fillers pad incomplete Korean syllable blocks.

Law: HANGUL_FILLER != EMPTY. A filler inside genuine Hangul composition (flanked
by jamo / syllables) is legitimate; a filler standing as a blank identifier, or
padding / splitting a non-Korean token, is a spoof.

  ALARM (conclusive):
    - the whole (trimmed) string is nothing but fillers -> blank identifier, OR
    - a filler splits / pads an ASCII word (admin<FILLER>).
  OK (clean):
    every filler is flanked by Hangul jamo / syllables (real composition).
  WATCH:
    a filler present but neither a proven spoof nor provable composition.
"""
from invariant_engine.core import Finding

FILLERS = {0x115F, 0x1160, 0x3164, 0xFFA0}
NAME = {0x115F: "HANGUL CHOSEONG FILLER", 0x1160: "HANGUL JUNGSEONG FILLER",
        0x3164: "HANGUL FILLER", 0xFFA0: "HALFWIDTH HANGUL FILLER"}


def _is_filler(o):
    return o in FILLERS


def _hangul(ch):
    if not ch:
        return False
    o = ord(ch)
    return (0x1100 <= o <= 0x11FF or 0x3130 <= o <= 0x318F
            or 0xA960 <= o <= 0xA97F or 0xAC00 <= o <= 0xD7A3)


def _ascii_wordish(ch):
    return bool(ch) and ord(ch) < 128 and ch.isalnum()


def hangul_filler_cards_reader(text):
    """Filler authority: ALARM blank/pad spoof / OK composition / WATCH."""
    idx = [i for i, ch in enumerate(text) if _is_filler(ord(ch))]
    if not idx:
        return Finding("clean", 0.0, "hangul-filler-cards: no fillers")

    # blank-identifier spoof: nothing but fillers (and spaces) in the string
    if all(_is_filler(ord(c)) or c.isspace() for c in text):
        return Finding("suspect", 0.85,
            "string is only Hangul filler(s) — invisible / blank identifier spoof",
            conclusive=True, signature="filler_blank")

    # padding / splitting a non-Korean (ASCII) token
    for i in idx:
        prev = text[i - 1] if i > 0 else ""
        nxt = text[i + 1] if i + 1 < len(text) else ""
        if _ascii_wordish(prev) or _ascii_wordish(nxt):
            return Finding("suspect", 0.82,
                f"{NAME[ord(text[i])]} padding/splitting a non-Korean token "
                f"('{prev}<filler>{nxt}')", conclusive=True, signature="filler_pad")

    # legit composition: every filler flanked by Hangul
    if all(_hangul(text[i-1] if i > 0 else "") or _hangul(text[i+1] if i+1 < len(text) else "")
           for i in idx):
        return Finding("clean", 0.0,
                       "hangul-filler-cards: fillers within Hangul composition")

    return Finding("suspect", 0.4,
                   f"{len(idx)} Hangul filler(s) present without composition "
                   f"context — witness (held, not stripped)",
                   signature="filler_witness")
