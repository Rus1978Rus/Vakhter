# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
Contract for the Unicode-whitespace fold in the canonicalization pre-pass
(code/canonicalization/canonicalize.py :: fold_spaces / canonicalize).

Non-ASCII spaces (NBSP U+00A0, en/em/thin/hair spaces U+2000–200A, U+202F,
U+205F, ogham U+1680) are a space-substitution carrier used to evade spacing-
sensitive filters. The fold peels them to a plain ASCII space and reports a
`weird_space` witness — the last of the compatibility carriers (after fullwidth
and math). Zero-width marks are deliberately NOT spaces: they belong to the
invisible detector. Benign typography (NBSP thin space in numbers) stays clean.
"""
import os
import sys

from _support import ok, eq, clean

_HERE = os.path.dirname(os.path.abspath(__file__))
for _p in (os.path.join(_HERE, "..", "canonicalization"),):
    _p = os.path.abspath(_p)
    if _p not in sys.path:
        sys.path.insert(0, _p)

from canonicalize import fold_spaces, canonicalize
from product import analyze

NBSP = chr(0x00A0)
THIN = chr(0x2009)
NNBSP = chr(0x202F)
EM = chr(0x2003)
OGHAM = chr(0x1680)
ZWSP = chr(0x200B)


def test_fold_common_spaces():
    eq(fold_spaces("rm" + NBSP + "-rf")[0], "rm -rf")
    eq(fold_spaces("click" + THIN + "here")[0], "click here")
    eq(fold_spaces("a" + EM + "b" + OGHAM + "c")[0], "a b c")
    eq(fold_spaces("x" + NNBSP + "y")[0], "x y")
    ok(fold_spaces("a" + NBSP + "b")[1], "present flag must be set")


def test_zero_width_is_not_a_space():
    # ZWSP is an invisible smuggle, not a space — it must pass through unfolded
    folded, present = fold_spaces("ad" + ZWSP + "min")
    eq(folded, "ad" + ZWSP + "min")
    ok(not present, "zero-width must not count as a weird space")


def test_canonicalize_sets_weird_space_flag():
    _, meta = canonicalize("rm" + NBSP + "-rf /")
    ok(meta["weird_space"], "canonicalize meta must record the weird space")
    _, meta2 = canonicalize("rm -rf /")
    ok(not meta2["weird_space"], "plain ASCII spacing must not set the flag")


def test_benign_typography_stays_clean():
    # NBSP / thin space in ordinary text and number grouping is legitimate
    for s in ("café" + NBSP + "résumé", "5" + NBSP + "000", "1" + THIN + "000 meters",
              "normal spacing here"):
        clean(analyze, s)
