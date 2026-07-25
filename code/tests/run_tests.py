#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
Standalone test runner — no pytest needed (there is none in this environment).

Discovers every test_*.py beside it, runs every test_* function, and reports an
honest count of tests / checks / failures (NOTARIUS-style). Exit code 1 on any
failure so it can gate CI or a pre-commit hook.

  Usage:  python code/tests/run_tests.py

The same test_*() functions are ordinary asserting functions, so if pytest is
ever installed it collects and runs this directory unchanged.
"""
import importlib
import os
import sys
import traceback

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import _support  # noqa: E402  (also wires sys.path for the detectors)


def main():
    files = sorted(f for f in os.listdir(HERE)
                   if f.startswith("test_") and f.endswith(".py"))
    total = failed = 0
    print("VAKHTER TEST LAYER")
    print("-" * 60)
    for fn in files:
        mod = importlib.import_module(fn[:-3])
        tests = sorted(n for n in dir(mod)
                       if n.startswith("test_") and callable(getattr(mod, n)))
        for name in tests:
            total += 1
            try:
                getattr(mod, name)()
                print(f"  PASS  {fn}::{name}")
            except Exception as exc:  # noqa: BLE001 — a runner reports every failure
                failed += 1
                print(f"  FAIL  {fn}::{name}  — {exc}")
                traceback.print_exc()
    print("-" * 60)
    print(f"{total} tests, {_support._Counter.n} checks, {failed} failed")
    if failed:
        print("TESTS FAILED")
        return 1
    print("ALL GREEN")
    return 0


if __name__ == "__main__":
    sys.exit(main())
