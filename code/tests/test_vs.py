# -*- coding: utf-8 -*-
"""
Unit contract for the variation-selector detector (code/range/vs_cards.py).

Key invariant this pins: variation selectors are category Mn (Nonspacing_Mark),
NOT Cf (Format). A guard that "strips all format chars" misses them entirely,
which is why they get their own detector. One selector on a valid base is fine;
a RUN, or a selector with no base, is a carrier.
"""
from _support import ok, flags, clean
from vs_cards import vs_cards_reader as R

VS16 = chr(0xFE0F)
VS1 = chr(0xFE00)
VS2 = chr(0xFE01)


def test_vs_run_is_carrier():
    flags(R, "\U0001F600" + VS1 + VS2)                 # emoji + 2 selectors
    flags(R, "\U0001F600" + VS1 + VS2 + chr(0xFE02))   # emoji + 3 selectors


def test_leading_vs_flags():
    flags(R, VS1 + "abc")   # a selector with no base at all


def test_vs_after_nonbase_flags():
    flags(R, "a" + VS1)     # selector after a plain ASCII letter — nothing to select


def test_single_vs_on_emoji_clean():
    clean(R, "❤" + VS16)          # heart + VS16 (emoji presentation) — legit
    clean(R, "\U0001F600" + VS16)  # grinning face + VS16


def test_no_vs_clean():
    for s in ("plain text", "emoji \U0001F600 alone", "digits 123"):
        clean(R, s)
