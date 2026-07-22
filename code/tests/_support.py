# -*- coding: utf-8 -*-
"""
Shared support for the standalone test layer.

Adopted from the NOTARIUS cross-review (its 109-assert pytest discipline): the
range_*.py harnesses drive whole scenarios and PRINT, but nothing pins an
individual detector's contract with a hard assertion. A single false-negative
(the Roman-numeral short-token bug fixed in 8deaf9a — "ⅬG" slipping past the
detector) lived precisely in that gap. These tests close it.

No pytest in this environment, so this module provides:
  - sys.path wiring to import the range detectors and invariant_engine;
  - a tiny assert helper set that ALSO counts checks (so the runner can report
    an honest "N checks" total, NOTARIUS-style);
  - flags()/clean() shorthands for "this reader must ALARM / must stay OK".

Every helper raises AssertionError on failure, so the same test_*() functions
are collectable by real pytest unchanged if it is ever installed.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.abspath(os.path.join(HERE, ".."))
RANGE = os.path.join(CODE, "range")
IE = os.path.join(CODE, "invariant_engine")
for _p in (CODE, IE, RANGE):
    if _p not in sys.path:
        sys.path.insert(0, _p)


class _Counter:
    n = 0


def ok(cond, msg=""):
    _Counter.n += 1
    assert cond, msg or "check failed"


def eq(got, want, msg=""):
    _Counter.n += 1
    assert got == want, msg or f"expected {want!r}, got {got!r}"


def flags(reader, s, signature=None):
    """Assert `reader` ALARMs on `s` (label 'suspect'); optionally pin the signature."""
    f = reader(s)
    _Counter.n += 1
    assert f.label == "suspect", (
        f"expected SUSPECT for {s!r}, got {f.label!r} — {f.reason}")
    if signature is not None:
        _Counter.n += 1
        assert f.signature == signature, (
            f"expected signature {signature!r} for {s!r}, got {f.signature!r}")
    return f


def clean(reader, s):
    """Assert `reader` stays OK on `s` (label 'clean') — the no-false-positive contract."""
    f = reader(s)
    _Counter.n += 1
    assert f.label == "clean", (
        f"expected CLEAN for {s!r}, got {f.label!r} — {f.reason}")
    return f
