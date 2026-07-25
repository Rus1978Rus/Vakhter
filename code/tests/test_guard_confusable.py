# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
Contract that the assembled guard (code/range/product.py :: analyze) actually
WIRES the rich confusable detector — not just the light dot-gated Cyrillic check
that digit_cards carries.

Before wiring, analyze() missed Greek/Roman/whole-script/dot-separator homoglyphs
entirely (they live in confusable_cards, which was absent from _READERS). This
pins that the front door now judges them, and that the wiring adds 0 false
positives on ordinary multilingual text.
"""
from _support import ok, flags, clean
from product import analyze


def test_guard_catches_greek_homoglyph():
    flags(analyze, "faϲebook-login.com")   # Greek lunate sigma
    flags(analyze, "gοοgle.com")           # Greek omicron


def test_guard_catches_cyrillic_homoglyph():
    flags(analyze, "раypal.com")           # Cyrillic р, а
    flags(analyze, "microsοft.com")        # (Greek ο) — cross-script


def test_guard_catches_roman_and_separator():
    flags(analyze, "ⅬG-support")            # Roman-numeral form in a short token
    flags(analyze, "paypal․com")           # non-ASCII dot separator


def test_guard_catches_whole_script():
    flags(analyze, "сіѕсо")                 # bare all-Cyrillic brand token


def test_guard_no_false_positive_multilingual():
    for s in ("россия москва", "привет мир", "日本語のテキスト", "καλημέρα κόσμε",
              "visit paypal.com now", "user@example.com", "café résumé",
              "Ⅻ chapter twelve", "the quick brown fox"):
        clean(analyze, s)
