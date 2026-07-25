# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
Script-bound-ignorable detector card (SIMULATOR of a draft).

Two small families of default-ignorable combining marks (category Mn) that are
meaningful ONLY inside their own script:
  - Mongolian Free Variation Selectors: U+180B..U+180D, U+180F — pick a Mongolian
    glyph variant of the preceding Mongolian letter (the Mongolian analogue of
    the VS card, but script-bound to the Mongolian block).
  - Khmer inherent vowels: U+17B4 (AQ), U+17B5 (AA) — invisible inherent vowels
    used inside Khmer text.

Law: SCRIPT_IGNORABLE != UNIVERSAL. In-script (an FVS after a Mongolian letter, a
Khmer inherent vowel inside Khmer) is legitimate; anywhere else it is an orphan /
carrier — an invisible mark riding on the wrong substrate.

  ALARM (conclusive):
    - a run of >= 2 of these marks (data carrier), OR
    - a mark with no valid in-script base (orphan on Latin/ASCII/space).
  OK (clean):
    every mark sits on its own script (Mongolian FVS after Mongolian; Khmer
    inherent vowel among Khmer).
  WATCH:
    present but neither a proven orphan/carrier nor provably in-script.
"""
from invariant_engine.core import Finding

MONGOLIAN_FVS = {0x180B, 0x180C, 0x180D, 0x180F}
KHMER_INHERENT = {0x17B4, 0x17B5}
MARKS = MONGOLIAN_FVS | KHMER_INHERENT


def _is_mark(o):
    return o in MARKS


def _mongolian(ch):
    return bool(ch) and 0x1800 <= ord(ch) <= 0x18AF


def _khmer(ch):
    return bool(ch) and 0x1780 <= ord(ch) <= 0x17FF


def _in_script(o, prev):
    if o in MONGOLIAN_FVS:
        return _mongolian(prev)
    return _khmer(prev)                     # Khmer inherent vowel after Khmer


def script_ignorable_cards_reader(text):
    """Script-ignorable authority: ALARM carrier/orphan / OK in-script / WATCH."""
    idx = [i for i, ch in enumerate(text) if _is_mark(ord(ch))]
    if not idx:
        return Finding("clean", 0.0, "script-ignorable-cards: none present")

    # run of >= 2 consecutive marks -> data carrier
    run = best = 0
    for ch in text:
        if _is_mark(ord(ch)):
            run += 1; best = max(best, run)
        else:
            run = 0
    if best >= 2:
        return Finding("suspect", 0.82,
            f"script-ignorable mark run (len {best}) — data carrier "
            f"(Mn marks; a Cf-only filter misses these)",
            conclusive=True, signature="script_ig_carrier")

    # orphan: a mark with no valid in-script base
    for i in idx:
        prev = text[i - 1] if i > 0 else ""
        if not _in_script(ord(text[i]), prev):
            return Finding("suspect", 0.78,
                f"U+{ord(text[i]):04X} default-ignorable mark off its script "
                f"(base '{prev}') — orphan carrier",
                conclusive=True, signature="script_ig_orphan")

    return Finding("clean", 0.0,
                   "script-ignorable-cards: every mark is in-script (Mongolian / Khmer)")
