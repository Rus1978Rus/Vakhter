# -*- coding: utf-8 -*-
"""
Contract for the fullwidth fold in the canonicalization pre-pass
(code/canonicalization/canonicalize.py :: fold_fullwidth / canonicalize).

Fullwidth ASCII (U+FF01..U+FF5E) is a compatibility carrier: a fullwidth-encoded
attack (＜script＞, fullwidth IP, fullwidth ../) renders like its ASCII twin but
dodges an ASCII-only filter. The fold peels that carrier so the readers judge the
real sign underneath — the same "double bottom" as overlong-UTF8. This pins the
fold AND the no-false-positive boundary (real CJK / halfwidth katakana untouched).
"""
import os
import sys

from _support import ok, eq, flags, clean

_HERE = os.path.dirname(os.path.abspath(__file__))
for _p in (os.path.join(_HERE, "..", "canonicalization"),):
    _p = os.path.abspath(_p)
    if _p not in sys.path:
        sys.path.insert(0, _p)

from canonicalize import fold_fullwidth, canonicalize
from product import analyze


def test_fold_letters_digits_punct():
    folded, present = fold_fullwidth("ｐａｙｐａｌ.ｃｏｍ")
    eq(folded, "paypal.com")
    ok(present, "fullwidth present flag must be set")
    eq(fold_fullwidth("ＡＢＣ")[0], "ABC")
    eq(fold_fullwidth("１２７．０．０．１")[0], "127.0.0.1")
    eq(fold_fullwidth("＜script＞")[0], "<script>")


def test_fold_block_boundaries():
    # FF01 (first) and FF5E (last) fold; the ideographic space folds to ASCII space
    eq(fold_fullwidth("！")[0], "!")     # U+FF01 -> !
    eq(fold_fullwidth("～")[0], "~")     # U+FF5E -> ~
    eq(fold_fullwidth("　")[0], " ")     # ideographic space -> space


def test_no_fold_outside_block():
    # halfwidth katakana (FF61..FF9F) and real CJK are NOT ASCII carriers
    for s in ("ﾊﾛｰﾜｰﾙﾄﾞ", "日本語のテキスト", "正常な文章"):
        folded, present = fold_fullwidth(s)
        eq(folded, s)
        ok(not present, f"must not fold {s!r}")


def test_canonicalize_sets_fullwidth_flag():
    _, meta = canonicalize("ｐａｙｐａｌ.ｃｏｍ")
    ok(meta["fullwidth"], "canonicalize meta must record fullwidth carrier")
    _, meta2 = canonicalize("paypal.com")
    ok(not meta2["fullwidth"], "plain ASCII must not set the flag")


def test_pipeline_reveals_fullwidth_attacks():
    # each was clean before the fold; folding surfaces it to the readers
    flags(analyze, "＜script＞alert(1)＜/script＞")        # fullwidth XSS
    flags(analyze, "ｈｔｔｐ：／／１２７．０．０．１／")            # fullwidth loopback IP URL
    flags(analyze, "．．／．．／．．／etc／passwd")             # fullwidth path traversal


def test_pipeline_no_false_positive():
    for s in ("plain ascii text", "日本語のテキスト", "ﾊﾛｰﾜｰﾙﾄﾞ", "привет мир"):
        clean(analyze, s)
