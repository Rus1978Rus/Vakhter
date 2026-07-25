# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
Contract that the guard (product.analyze) wires three invisible/format smuggle
detectors that were previously absent from _READERS and that the guard therefore
missed: whitespace (line/paragraph separators), Hangul fillers, and prepended
format marks. Pins the coverage AND the 0-FP boundary on legit Korean/Arabic/CJK.
"""
from _support import ok, flags, clean
from product import analyze

LSEP = chr(0x2028)       # LINE SEPARATOR
PSEP = chr(0x2029)       # PARAGRAPH SEPARATOR
HFILL = chr(0x3164)      # HANGUL FILLER
ARABIC_NUM = chr(0x0600)  # ARABIC NUMBER SIGN (prepended format)


def test_guard_catches_line_separator():
    flags(analyze, "pay" + LSEP + "pal")      # record/statement-injection separator
    flags(analyze, "line1" + PSEP + "line2")


def test_guard_catches_hangul_filler_in_ascii():
    flags(analyze, "ad" + HFILL + "min")       # blank-looking filler splitting a word


def test_guard_catches_prepended_format_scope_abuse():
    flags(analyze, "abc" + ARABIC_NUM + "123")  # Arabic sign scoping ASCII digits


def test_guard_clean_on_legit_scripts():
    for s in ("안녕하세요 세계", "한국어 텍스트입니다",           # Korean
              "مرحبا بالعالم", "الرقم " + ARABIC_NUM + "١٢٣",   # Arabic (sign + Arabic digits)
              "日本語のテキスト", "中文文本测试",                  # CJK
              "plain english", "россия москва"):
        clean(analyze, s)
