# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
DoS / self-defense recheck for the readers wired this cycle.

Wiring the rich confusable reader plus whitespace/hangul/prepended raised the
per-char cost of the full pipeline, so this pins two things:
  1. self_defense still BOUNCES floods (oversize / invisible / dominant-char)
     before the readers run — cheaply.
  2. a worst-case input at exactly MAX_LEN (all-foreign, no early return, no
     dominant char — the slowest legal input) completes comfortably under the
     wall-clock budget, and every new reader stays linear on it.

Timing thresholds are deliberately generous (real measured worst-case is ~0.57s
vs the 1.5s budget) so the test is not flaky on a slow host.
"""
import os
import sys
import time

from _support import ok

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "range")))
from product import analyze, _core
from guard import MAX_LEN, BUDGET_S
from confusable_cards import confusable_cards_reader
from whitespace_cards import whitespace_cards_reader
from hangul_filler_cards import hangul_filler_cards_reader
from prepended_format_cards import prepended_format_cards_reader

# worst-case legal input: 5 distinct Cyrillic look-alikes, so no char exceeds the
# dominant-char ratio, length == MAX_LEN, and it returns clean (no early exit).
_UNIT = "сіѕсо"
_WORST = _UNIT * (MAX_LEN // len(_UNIT))

analyze("warmup")   # compile regexes / load cards before timing


def test_oversize_input_is_bounced_cheaply():
    big = "a" * (MAX_LEN + 5000)
    t = time.time()
    f = analyze(big)
    dt = time.time() - t
    ok(f.label != "clean", "oversized input must be held")
    ok(dt < 0.2, f"oversize bounce must be cheap, took {dt*1000:.0f}ms")


def test_invisible_and_dominant_floods_bounce():
    ok(analyze("a" + "​" * 500).label != "clean", "invisible flood must bounce")
    ok(analyze("/" * 3000).label != "clean", "slash flood must be held")
    ok(analyze("x" * 2000).label != "clean", "single-char flood must bounce")


def test_worst_case_full_pipeline_under_budget():
    t = time.time()
    _core(_WORST)                    # bypasses the oversize check to time the readers
    dt = time.time() - t
    ok(dt < BUDGET_S, f"worst-case pipeline {dt:.2f}s must be under budget {BUDGET_S}s")
    ok(dt < 1.2, f"worst-case pipeline {dt:.2f}s should keep a healthy margin")


def test_each_new_reader_linear_on_max_input():
    for name, r in (("confusable", confusable_cards_reader),
                    ("whitespace", whitespace_cards_reader),
                    ("hangul", hangul_filler_cards_reader),
                    ("prepended", prepended_format_cards_reader)):
        t = time.time()
        r(_WORST)
        dt = time.time() - t
        ok(dt < 0.6, f"{name} reader took {dt*1000:.0f}ms on MAX_LEN input")
