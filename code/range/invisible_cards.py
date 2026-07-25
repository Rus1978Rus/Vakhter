# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
Invisible / bidi detector cards (SIMULATOR of drafts) — raises coverage point #3.

MSL flags an uncarded invisible as a WITNESS ("look at this") but cannot tell a
smuggle from legit emoji glue — that is CONTEXT, and context is this card's job.
This layer is the invisible authority: it ALARMs on a proven smuggle, clears
legit emoji/bidi glue, and WATCHes a genuinely unknown invisible.

  ALARM (conclusive):
    1. zero-width char splitting a WORD (admin<ZWSP>istrator)
    2. bidi control IMBALANCE (unterminated RLO/LRO = Trojan Source, CVE-2021-42574)
    3. tag characters U+E0000..U+E007F with no flag base (invisible ASCII smuggle)
    4. variation-selector CARRIER run (>=3, or leading)
  OK (clean):
    every invisible present is legit glue — ZWJ between emoji, VS after an emoji
    base, tag chars after a flag base, balanced bidi.
  WATCH (non-conclusive):
    an invisible is present that is neither a proven smuggle nor provable glue.
"""
import unicodedata
from invariant_engine.core import Finding

ZERO_WIDTH = {0x200B, 0x200C, 0x200D, 0x2060, 0xFEFF, 0x00AD}   # zwsp zwnj zwj wj bom shy
BIDI_OPEN  = {0x202A, 0x202B, 0x202D, 0x202E, 0x2066, 0x2067, 0x2068}  # LRE RLE LRO RLO LRI RLI FSI
BIDI_CLOSE = {0x202C, 0x2069}                                    # PDF PDI
TAG        = range(0xE0000, 0xE0080)                             # tag chars
VS         = set(range(0xFE00, 0xFE10)) | set(range(0xE0100, 0xE01F0))  # variation selectors
FLAG_BASE  = 0x1F3F4                                             # black flag (legit tag-seq base)


def _wordish(ch):
    return bool(ch) and ch.isalnum()


def _emoji_ish(ch):
    if not ch:
        return False
    return ord(ch) >= 0x1F000 or unicodedata.category(ch).startswith("S")


def _is_invisible(ch):
    o = ord(ch)
    return o in ZERO_WIDTH or o in BIDI_OPEN or o in BIDI_CLOSE or o in TAG or o in VS


# ---- conclusive smuggle checks ----
def _zw_wordsplit(text):
    for i, ch in enumerate(text):
        if ord(ch) in ZERO_WIDTH:
            prev = text[i - 1] if i > 0 else ""
            nxt = text[i + 1] if i + 1 < len(text) else ""
            if _emoji_ish(prev) or _emoji_ish(nxt):
                continue
            if _wordish(prev) and _wordish(nxt):
                return Finding("suspect", 0.85,
                    f"zero-width U+{ord(ch):04X} splitting a word "
                    f"('{prev}‹zw›{nxt}') — invisible smuggle",
                    conclusive=True, signature="zw_wordsplit")
    return None


def _bidi_imbalance(text):
    opens = sum(1 for c in text if ord(c) in BIDI_OPEN)
    closes = sum(1 for c in text if ord(c) in BIDI_CLOSE)
    if opens and opens != closes:
        return Finding("suspect", 0.9,
            f"unbalanced bidi controls (open={opens}, close={closes}) — "
            f"Trojan-Source style reordering", conclusive=True,
            signature="bidi_imbalance")
    return None


def _tag_smuggle(text):
    tags = [c for c in text if ord(c) in TAG]
    if tags and FLAG_BASE not in (ord(c) for c in text):
        return Finding("suspect", 0.9,
            f"{len(tags)} tag char(s) U+E00xx with no flag base — "
            f"invisible ASCII smuggling", conclusive=True, signature="tag_smuggle")
    return None


def _vs_carrier(text):
    run = best = 0
    for c in text:
        if ord(c) in VS:
            run += 1; best = max(best, run)
        else:
            run = 0
    if best >= 3 or (text and ord(text[0]) in VS):
        return Finding("suspect", 0.8,
            f"variation-selector run (max {best}) used as data carrier",
            conclusive=True, signature="vs_carrier")
    return None


def _first_smuggle(text):
    for chk in (_zw_wordsplit, _bidi_imbalance, _tag_smuggle, _vs_carrier):
        f = chk(text)
        if f:
            return f
    return None


# ---- legit-glue vouch ----
def _legit_glue(text, i):
    o = ord(text[i])
    prev = text[i - 1] if i > 0 else ""
    nxt = text[i + 1] if i + 1 < len(text) else ""
    if o == 0x200D:                       # ZWJ — emoji join
        return _emoji_ish(prev) or _emoji_ish(nxt)
    if o in VS:                           # variation selector — after an emoji base
        return _emoji_ish(prev)
    if o in TAG:                          # tag char — after a flag base earlier
        return FLAG_BASE in (ord(x) for x in text[:i])
    if o in BIDI_OPEN or o in BIDI_CLOSE:  # bidi — only if the whole string is balanced
        opens = sum(1 for x in text if ord(x) in BIDI_OPEN)
        closes = sum(1 for x in text if ord(x) in BIDI_CLOSE)
        return opens == closes
    return False                          # ZWSP/ZWNJ/BOM/WJ/SHY never auto-vouched


def invisible_cards_reader(text):
    """The invisible authority: ALARM smuggle / OK legit-glue / WATCH unknown."""
    smug = _first_smuggle(text)
    if smug:
        return smug
    pos = [i for i, c in enumerate(text) if _is_invisible(c)]
    if not pos:
        return Finding("clean", 0.0, "invisible-cards: no invisibles")
    if all(_legit_glue(text, i) for i in pos):
        return Finding("clean", 0.0,
                       "invisible-cards: all invisibles are legit emoji/bidi glue")
    return Finding("suspect", 0.45,
                   "uncarded invisible codepoint present without legit context",
                   signature="invisible_watch")
