# -*- coding: utf-8 -*-
"""
THE GUARD, assembled with every defense on — the canonical front door.

Order of defense:
  1. self_defense    — bounce DoS floods (invisible/char/oversize) in <1 ms
  2. canonicalize    — peel encoding carriers, judge the real sign underneath
  3. safe_reader x N — MSL + every card, each ISOLATED (one crash -> WATCH, not
                       silence; the others still run)
  4. erg_context     — context softening (only ever softens; wrapped so it can't
                       throw the whole thing)
  5. safe_analyze    — fail-CLOSED envelope: non-text input or any uncaught error
                       -> a blocking verdict, never OK. analyze() never throws.

Usage:  from product import analyze;  finding = analyze(text)
        block = (finding.label != "clean")
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
for _c in ("canon", "canonicalization"):
    _p = os.path.abspath(os.path.join(_HERE, "..", _c))
    if os.path.isdir(_p):
        sys.path.insert(0, _p); break
sys.path.insert(0, os.path.abspath(os.path.join(_HERE, "..", "invariant_engine")))
sys.path.insert(0, _HERE)

from canonicalize import canonicalize
from invariant_engine.msl_real import real_text_reader
from invariant_engine.supplement import supplement_reader, combine
from digit_cards import digit_cards_reader
from metachar_cards import metachar_cards_reader
from invisible_cards import invisible_cards_reader
from harden_cards import harden_cards_reader
from confusable_cards import confusable_cards_reader
from whitespace_cards import whitespace_cards_reader
from hangul_filler_cards import hangul_filler_cards_reader
from prepended_format_cards import prepended_format_cards_reader
from erg_context import erg_context
from guard import self_defense
from fail_closed import safe_reader, safe_analyze

_READERS = [("msl", real_text_reader), ("supplement", supplement_reader),
            ("digit", digit_cards_reader), ("metachar", metachar_cards_reader),
            ("invisible", invisible_cards_reader), ("harden", harden_cards_reader),
            ("confusable", confusable_cards_reader),
            ("whitespace", whitespace_cards_reader),
            ("hangul_filler", hangul_filler_cards_reader),
            ("prepended_format", prepended_format_cards_reader)]


def _core(text):
    early = self_defense(text)
    if early is not None:
        return early
    c = canonicalize(text)[0]
    f = None
    for name, r in _READERS:
        g = safe_reader(name, r, c)
        f = g if f is None else combine(f, g)
    try:
        return erg_context(c, f)
    except Exception:
        return f                       # ERG only softens; ignore its failure


def analyze(text):
    """The guard. Fail-closed, DoS-guarded, per-component isolated. Never throws.
    Returns a Finding; block when finding.label != 'clean'."""
    return safe_analyze(text, _core)
