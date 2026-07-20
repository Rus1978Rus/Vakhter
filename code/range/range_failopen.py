# -*- coding: utf-8 -*-
"""
COMPONENT CHECK #1 — fail-open vs fail-closed.

Threat model: an attacker finds an input that CRASHES one component (simulated
by forcing that component to raise), or an integration passes a non-string. The
common real caller is:  try: v = guard(x)  except: allow()   (fail-OPEN).

We show, sending a REAL SQL-injection through while each component is crashed:
  NAIVE guard (no isolation)  -> the crash throws; the caller lets the THREAT in.
  SAFE  guard (fail-closed)   -> a crash becomes a BLOCK; the threat is stopped.

Run:  MSL_MIP_HOME=/path/to/msl_mip  python range_failopen.py
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
for _cand in ("canon", "canonicalization"):
    _p = os.path.abspath(os.path.join(HERE, "..", _cand))
    if os.path.isdir(_p):
        sys.path.insert(0, _p); break
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "invariant_engine")))
sys.path.insert(0, HERE)

from canonicalize import canonicalize
from invariant_engine.msl_real import real_text_reader
from invariant_engine.supplement import supplement_reader, combine
from digit_cards import digit_cards_reader
from metachar_cards import metachar_cards_reader
from invisible_cards import invisible_cards_reader
from harden_cards import harden_cards_reader
from erg_context import erg_context
from guard import self_defense
from fail_closed import safe_reader, safe_analyze

def _boom(_):
    raise ValueError("crafted input crashed this component")

# name -> real reader; `crash` picks one to replace with _boom
BASE = [("msl", real_text_reader), ("supplement", supplement_reader),
        ("digit", digit_cards_reader), ("metachar", metachar_cards_reader),
        ("invisible", invisible_cards_reader), ("harden", harden_cards_reader)]

def _readers(crash):
    return [(n, _boom if n == crash else f) for n, f in BASE]

# NAIVE: no isolation, no fail-closed — one reader throwing sinks the guard
def naive_guard(text, crash=None):
    early = self_defense(text)
    if early is not None:
        return early
    c = canonicalize(text)[0]
    f = None
    for _n, r in _readers(crash):
        f = r(c) if f is None else combine(f, r(c))
    return erg_context(c, f)

# SAFE: per-component isolation + whole-guard fail-closed
def safe_guard(text, crash=None):
    def pipeline(t):
        early = self_defense(t)
        if early is not None:
            return early
        c = canonicalize(t)[0]
        f = None
        for n, r in _readers(crash):
            g = safe_reader(n, r, c)
            f = g if f is None else combine(f, g)
        try:
            return erg_context(c, f)
        except Exception:
            return f
    return safe_analyze(text, pipeline)

def decide(guard, text, crash=None):
    """Map to ALLOWED/BLOCKED the way a typical integration would (allow on error)."""
    try:
        r = guard(text, crash)
        risk = "OK" if r.label == "clean" else ("ALARM" if r.conclusive else "WATCH")
        return "ALLOWED" if risk == "OK" else "BLOCKED"
    except Exception:
        return "ALLOWED"                       # fail-OPEN

THREAT = "id=1%27 OR %271%27=%271"             # a real SQL-injection attempt

def run():
    print("COMPONENT CHECK #1 — fail-open vs fail-closed")
    print("=" * 70)
    print("Sending a real SQL-injection while ONE component is crashed.\n")
    print(f"{'crashed component':18} | {'NAIVE guard':12} | {'SAFE guard':12}")
    print("-" * 70)
    leaks_naive = leaks_safe = 0
    for crash in [None, "msl", "supplement", "digit", "metachar", "invisible", "harden"]:
        n = decide(naive_guard, THREAT, crash)
        s = decide(safe_guard, THREAT, crash)
        leaks_naive += (n == "ALLOWED"); leaks_safe += (s == "ALLOWED")
        tag = "  <- THREAT LEAKED" if n == "ALLOWED" else ""
        print(f"{str(crash):18} | {n:12} | {s:12}{tag}")

    print("-" * 70)
    for label, val in [("non-str int", 12345), ("non-str None", None), ("bytes", b"x")]:
        n = decide(naive_guard, val); s = decide(safe_guard, val)
        leaks_naive += (n == "ALLOWED"); leaks_safe += (s == "ALLOWED")
        tag = "  <- LEAKED" if n == "ALLOWED" else ""
        print(f"{label:18} | {n:12} | {s:12}{tag}")

    print("\n" + "=" * 70)
    print(f"threat LEAKED through NAIVE guard : {leaks_naive}   (fail-open — BAD)")
    print(f"threat LEAKED through SAFE  guard : {leaks_safe}   (fail-closed — target 0)")

if __name__ == "__main__":
    run()
