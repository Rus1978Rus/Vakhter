# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
FAIL-CLOSED wrappers — a security guard must NEVER answer "OK" just because it
crashed. If it cannot examine the input, the safe answer is HOLD/BLOCK, not PASS.

Two levels of defense-in-depth:

  A) safe_reader(name, fn, text) — per-component isolation. One detector crashing
     yields a WATCH ("this detector could not vouch"), NOT silence — and the OTHER
     detectors still run. No single buggy card can blind the guard or clear a threat.

  B) safe_analyze(text, pipeline) — whole-guard backstop. Non-text input or any
     uncaught error becomes a conclusive blocking verdict (ALARM), never OK. Even a
     caller that does `try: v = guard(x) except: allow()` stays safe, because the
     guard returns a blocking Finding instead of throwing.
"""
from invariant_engine.core import Finding


def safe_reader(name, fn, text):
    """Run one detector; a crash becomes a WATCH, never silent clean."""
    try:
        return fn(text)
    except Exception as e:
        return Finding("suspect", 0.4,
            f"detector '{name}' could not evaluate ({type(e).__name__}) — "
            f"held, not cleared",
            conclusive=False, signature="component_error")


def safe_analyze(text, pipeline):
    """Whole-guard fail-CLOSED: bad input or any uncaught error -> block, never OK.
    `pipeline` is text -> Finding (or Verdict-like with .risk)."""
    if not isinstance(text, str):
        return Finding("suspect", 0.7,
            f"non-text input ({type(text).__name__}) — cannot analyze, blocked",
            conclusive=True, signature="invalid_input")
    try:
        return pipeline(text)
    except Exception as e:
        return Finding("suspect", 0.8,
            f"analysis failed ({type(e).__name__}) — blocked (fail-closed)",
            conclusive=True, signature="analysis_error")
