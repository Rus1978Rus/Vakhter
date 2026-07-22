# -*- coding: utf-8 -*-
"""
Unit contract for the invisible / bidi detector (code/range/invisible_cards.py).

Pins the ALARM/OK/WATCH trichotomy: a proven smuggle must ALARM, legitimate
emoji/bidi glue must stay OK. (Reviewed against the NOTARIUS scanner's
HIGH/MEDIUM/LIKELY_LEGITIMATE scale — Vakhter's layer already supersedes it, so
this locks the existing behaviour rather than changing it; see AD-13.)
"""
from _support import ok, flags, clean
from invisible_cards import invisible_cards_reader as R

Z = chr(0x200B)    # ZERO WIDTH SPACE
BOM = chr(0xFEFF)  # ZERO WIDTH NO-BREAK SPACE / BOM
ZWJ = chr(0x200D)  # ZERO WIDTH JOINER
RLO = chr(0x202E)  # RIGHT-TO-LEFT OVERRIDE
PDF = chr(0x202C)  # POP DIRECTIONAL FORMATTING


def test_zero_width_wordsplit_flags():
    # an invisible splitting a real word is a smuggle (CVE-class token confusion)
    flags(R, "admin" + Z + "istrator", "zw_wordsplit")
    flags(R, "pass" + BOM + "word", "zw_wordsplit")
    flags(R, "verify" + chr(0x2060) + "account", "zw_wordsplit")  # word-joiner


def test_bidi_imbalance_flags():
    # unterminated RLO/LRO — Trojan Source (CVE-2021-42574)
    flags(R, "int x = 1;" + RLO + " // reversed", "bidi_imbalance")
    flags(R, RLO + "abc", "bidi_imbalance")


def test_bidi_balanced_clean():
    # a fully balanced open/close pair is legitimate bidi and must stay OK
    clean(R, RLO + "abc" + PDF)


def test_tag_smuggle_flags():
    # tag chars U+E00xx with no flag base = invisible ASCII smuggling
    flags(R, "hi" + chr(0xE0041) + chr(0xE0042), "tag_smuggle")


def test_vs_carrier_flags():
    # a RUN of variation selectors is a data carrier
    flags(R, "\U0001F600" + chr(0xFE00) + chr(0xFE01) + chr(0xFE02), "vs_carrier")


def test_emoji_zwj_glue_clean():
    # ZWJ between two emoji is a legitimate join (family / profession sequences)
    clean(R, "\U0001F468" + ZWJ + "\U0001F469")  # man + ZWJ + woman


def test_single_vs_on_emoji_clean():
    # ONE variation selector on an emoji base is legitimate presentation glue
    clean(R, "❤️")  # heart + VS16 (emoji presentation)


def test_no_invisible_clean():
    for s in ("just plain text", "no invisibles here", "42 + 8 = 50"):
        clean(R, s)


def test_zwj_not_between_emoji_is_not_auto_cleared():
    # ZWJ between two letters is NOT vouched as glue; the reader must not clear it.
    f = R("a" + ZWJ + "b")
    ok(f.label != "clean",
       f"ZWJ between letters should not be auto-cleared, got {f.label}")
