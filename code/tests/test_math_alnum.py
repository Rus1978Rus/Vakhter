# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
Contract for the math-alphanumeric fold in the canonicalization pre-pass
(code/canonicalization/canonicalize.py :: fold_math_alnum / canonicalize).

Mathematical-alphanumeric letters (𝐛𝐨𝐥𝐝, 𝘪𝘵𝘢𝘭𝘪𝘤, 𝔻𝕠𝕦𝕓𝕝𝕖-𝕤𝕥𝕣𝕦𝕔𝕜, 𝗌𝖺𝗇𝗌, monospace)
plus their Letterlike-block 'holes' (ℂ ℎ ℬ ℑ ℝ …) are pure styling carriers: they
render like ASCII but dodge ASCII filters. The fold peels them to ASCII so the
readers judge the real sign. This pins the fold, the mapping of the irregular
holes, AND the no-false-positive boundary (², ½, №, ™, Ω are NOT math styling).
"""
import os
import sys

from _support import ok, eq, flags, clean

_HERE = os.path.dirname(os.path.abspath(__file__))
for _p in (os.path.join(_HERE, "..", "canonicalization"),):
    _p = os.path.abspath(_p)
    if _p not in sys.path:
        sys.path.insert(0, _p)

from canonicalize import fold_math_alnum, canonicalize
from product import analyze


def test_fold_styles():
    eq(fold_math_alnum("𝐩𝐚𝐲𝐩𝐚𝐥")[0], "paypal")     # bold
    eq(fold_math_alnum("𝘩𝘵𝘵𝘱𝘴")[0], "https")          # italic
    eq(fold_math_alnum("𝗌𝖼𝗋𝗂𝗉𝗍")[0], "script")        # sans-serif
    eq(fold_math_alnum("𝕏")[0], "X")                    # double-struck
    ok(fold_math_alnum("𝐩𝐚𝐲𝐩𝐚𝐥")[1], "present flag must be set")


def test_fold_digits():
    eq(fold_math_alnum("𝟏𝟐𝟕")[0], "127")               # bold digits
    eq(fold_math_alnum("𝟢𝟣𝟤")[0], "012")               # monospace digits


def test_fold_letterlike_holes():
    # the irregular holes that live in the Letterlike Symbols block
    eq(fold_math_alnum("ℝ")[0], "R")   # double-struck R
    eq(fold_math_alnum("ℎ")[0], "h")   # italic h (Planck)
    eq(fold_math_alnum("ℬ")[0], "B")   # script B
    eq(fold_math_alnum("ℑ")[0], "I")   # fraktur I


def test_no_fold_non_math_compat():
    # ordinary compatibility characters are NOT math styling and must not fold
    for s in ("½", "²", "№", "™", "Ω", "ℹ", "㎏"):
        folded, present = fold_math_alnum(s)
        eq(folded, s)
        ok(not present, f"must not fold {s!r}")


def test_canonicalize_sets_math_flag():
    _, meta = canonicalize("𝐩𝐚𝐲𝐩𝐚𝐥.𝐜𝐨𝐦")
    ok(meta["math_styled"], "canonicalize meta must record math styling")
    _, meta2 = canonicalize("paypal.com")
    ok(not meta2["math_styled"], "plain ASCII must not set the flag")


def test_pipeline_reveals_math_attacks():
    flags(analyze, "＜𝘴𝘤𝘳𝘪𝘱𝘵＞alert(1)＜/𝘴𝘤𝘳𝘪𝘱𝘵＞")   # math+fullwidth XSS
    flags(analyze, "𝗵𝘁𝘁𝗽://𝟭𝟮𝟳.𝟬.𝟬.𝟭/")               # math loopback IP URL
    flags(analyze, "𝐩а𝐲𝐩𝐚𝐥.com")   # math bold hiding a Cyrillic а -> mixed-script after fold


def test_pipeline_no_false_positive():
    for s in ("𝐱 + 𝐲 = 𝐳", "ℝ is the set of reals", "½ ² № ™ Ω", "plain text ok"):
        clean(analyze, s)
