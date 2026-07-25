# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
Reserved-ignorable detector card (SIMULATOR of a draft) — the SHOULD-NEVER-APPEAR
blanket that closes the default-ignorable contour.

Unicode reserves whole ranges as default-ignorable-by-DEFAULT: code points that
are UNASSIGNED (category Cn) yet, should they ever appear, must be rendered as
nothing. That combination — no assigned character AND invisible — is a gift to an
attacker: a future-proof, tooling-invisible channel that no legitimate text can
possibly need, because nothing is assigned there.

This card is the blanket rule that makes the contour complete: the individual
assigned families each have their own card; this one owns everything left — the
~3.7k reserved default-ignorable code points — with a single law.

Law: RESERVED + IGNORABLE = SHOULD_NEVER_APPEAR. There is no legitimate use of an
unassigned default-ignorable code point, so presence is conclusive.

Ranges (Unicode Other_Default_Ignorable reserved space):
  U+2065; U+FFF0..U+FFF8; U+E0000; U+E0002..U+E001F; U+E0080..U+E00FF;
  U+E01F0..U+E0FFF.
"""
import unicodedata
from invariant_engine.core import Finding

def _R(a, b):
    return range(a, b + 1)

RESERVED_DI = (set(_R(0xFFF0, 0xFFF8)) | {0x2065, 0xE0000}
               | set(_R(0xE0002, 0xE001F)) | set(_R(0xE0080, 0xE00FF))
               | set(_R(0xE01F0, 0xE0FFF)))


def _is_reserved_di(o):
    return o in RESERVED_DI


def reserved_ignorable_cards_reader(text):
    """Reserved-ignorable authority: any presence is a conclusive anomaly.

    Version note: 'reserved' is defined against the Unicode version this draft
    was written for; a code point assigned in a later version would move to its
    own family card. The prototype double-checks category Cn (unassigned) so a
    newly-assigned code point does not stay mis-flagged here.
    """
    hits = []
    for ch in text:
        o = ord(ch)
        if _is_reserved_di(o) and unicodedata.category(ch) == "Cn":
            hits.append(o)
    if not hits:
        return Finding("clean", 0.0, "reserved-ignorable-cards: none present")
    shown = ", ".join(f"U+{o:04X}" for o in hits[:4])
    return Finding("suspect", 0.88,
        f"{len(hits)} reserved default-ignorable code point(s) present "
        f"({shown}) — unassigned AND invisible: should never appear",
        conclusive=True, signature="reserved_ignorable")
