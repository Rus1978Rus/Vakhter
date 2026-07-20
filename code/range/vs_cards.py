# -*- coding: utf-8 -*-
"""
Variation-selector detector card (SIMULATOR of a draft) — the Mn CARRIER axis.

Variation selectors are a SEPARATE axis for a category reason that matters:
they are Unicode general category **Mn (Nonspacing_Mark), NOT Cf (Format)**.
A guard that "strips all format (Cf) characters" — the usual invisible-cleanup
reflex — MISSES every variation selector, because they are combining marks, not
format chars. That is exactly why they get their own branch here.

Legit role: ONE selector immediately after an appropriate base — VS16 (U+FE0F)
for emoji presentation, VS15 (U+FE0E) for text presentation, VS1..14 and the
VS supplement (U+E0100..U+E01EF) for CJK ideograph variants. One base, one
selector.

Attack role: a RUN of selectors after a single base is a data CARRIER — each
selector encodes several bits, so a chain smuggles arbitrary bytes (the "emoji
variation-selector smuggling" technique). A selector with NO valid base (leading,
or after a space / plain letter) is equally anomalous.

  ALARM (conclusive):
    1. a RUN of >= 2 consecutive selectors (one base cannot meaningfully take
       two) -> data carrier.
    2. a leading selector (no base at all).
    3. a selector after a non-base character (space, ASCII letter) -> no
       variation to select -> anomalous carrier.
  OK (clean):
    every selector is a SINGLE selector sitting on a valid base
    (emoji base for VS15/VS16; CJK ideograph for the rest).
"""
import unicodedata
from invariant_engine.core import Finding

VS_BMP  = set(range(0xFE00, 0xFE10))          # VS1..VS16
VS_SUPP = set(range(0xE0100, 0xE01F0))        # VS17..VS256 (CJK)
VS_ALL  = VS_BMP | VS_SUPP
VS16, VS15 = 0xFE0F, 0xFE0E


def _is_vs(o):
    return o in VS_ALL


def _emoji_base(ch):
    if not ch:
        return False
    o = ord(ch)
    if o >= 0x1F000:                         # emoji planes
        return True
    if unicodedata.category(ch).startswith("S"):   # symbols (❤ ☺ ✂ …)
        return True
    return ch in "#*0123456789"              # keycap bases
                                             # (approximation for the draft)


def _cjk_base(ch):
    if not ch:
        return False
    o = ord(ch)
    return (0x3400 <= o <= 0x9FFF) or (0x20000 <= o <= 0x2FFFF) or (0xF900 <= o <= 0xFAFF)


def _valid_single(text, i):
    """Selector at index i is a lone selector on an appropriate base."""
    o = ord(text[i])
    prev = text[i - 1] if i > 0 else ""
    nxt_is_vs = i + 1 < len(text) and _is_vs(ord(text[i + 1]))
    prev_is_vs = i > 0 and _is_vs(ord(text[i - 1]))
    if nxt_is_vs or prev_is_vs:              # part of a run -> not a lone selector
        return False
    if o in (VS16, VS15):
        return _emoji_base(prev)
    return _cjk_base(prev)                    # VS1..14 / supplement -> CJK base


def vs_cards_reader(text):
    """VS authority: ALARM carrier/orphan / OK single-selector-on-base.

    NOTE: these are Mn marks; a Cf-only invisible filter never sees them.
    """
    idx = [i for i, ch in enumerate(text) if _is_vs(ord(ch))]
    if not idx:
        return Finding("clean", 0.0, "vs-cards: no variation selectors")

    # 1. run of >= 2 consecutive selectors -> data carrier
    run = best = 0
    for ch in text:
        if _is_vs(ord(ch)):
            run += 1; best = max(best, run)
        else:
            run = 0
    if best >= 2:
        return Finding("suspect", 0.85,
            f"variation-selector run (len {best}) after one base — data carrier "
            f"(Mn marks; a Cf-only filter misses these)",
            conclusive=True, signature="vs_carrier")

    # 2. leading selector (no base)
    if _is_vs(ord(text[0])):
        return Finding("suspect", 0.8,
            "leading variation selector with no base character",
            conclusive=True, signature="vs_orphan")

    # 3. any single selector on a non-base char
    for i in idx:
        if not _valid_single(text, i):
            prev = text[i - 1] if i > 0 else ""
            return Finding("suspect", 0.75,
                f"variation selector U+{ord(text[i]):04X} after non-base "
                f"'{prev}' — nothing to select (anomalous carrier)",
                conclusive=True, signature="vs_orphan")

    return Finding("clean", 0.0,
                   "vs-cards: every selector is a lone selector on a valid base")
