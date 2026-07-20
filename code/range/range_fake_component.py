# -*- coding: utf-8 -*-
"""
COMPONENT CHECK #4 — a POISONED component (supply-chain). What if an attacker
slips in a fake sign card, a fake integrator (combine), or a fake ERG?

Key structural question: which components can only RAISE suspicion, and which can
LOWER a verdict? Anything that can lower a verdict is the trusted core and must be
integrity-protected; anything add-only is safe even if forged.

We inject each kind of fake while sending a REAL SQL-injection and watch the verdict.
Run:  MSL_MIP_HOME=/path/to/msl_mip  python range_fake_component.py
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
from invariant_engine.core import Finding
from invariant_engine.msl_real import real_text_reader
from invariant_engine.supplement import supplement_reader, combine
from metachar_cards import metachar_cards_reader
from erg_context import erg_context
from fail_closed import safe_reader

THREAT = "id=1%27 OR %271%27=%271"          # a real SQL-injection

def verdict(f):
    return "OK" if f.label == "clean" else ("ALARM" if f.conclusive else "WATCH")

# a genuine (minimal) pipeline
def pipeline(readers, combiner, erg):
    c = canonicalize(THREAT)[0]
    f = None
    for n, r in readers:
        g = safe_reader(n, r, c)
        f = g if f is None else combiner(f, g)
    return verdict(erg(c, f))

REAL_READERS = [("msl", real_text_reader), ("supplement", supplement_reader),
                ("metachar", metachar_cards_reader)]

# --- the fakes ---
def fake_clean_card(_):                      # a card that lies "all clear"
    return Finding("clean", 0.0, "FAKE: nothing to see here")
def fake_alarm_card(_):                      # a card that screams on everything
    return Finding("suspect", 0.9, "FAKE alarm", conclusive=True, signature="fake")
def evil_combine(a, b):                      # integrator that keeps the LOWER severity
    def rank(f): return 0 if f.label == "clean" else (2 if f.conclusive else 1)
    return a if rank(a) <= rank(b) else b
def evil_erg(_c, _f):                         # ERG that clears everything
    return Finding("clean", 0.0, "FAKE ERG: cleared")

def run():
    print("COMPONENT CHECK #4 — poisoned component (supply-chain)")
    print("=" * 70)
    rows = [
        ("baseline (all real)",           REAL_READERS, combine, erg_context),
        ("+ fake card lies 'clean'",      REAL_READERS + [("fakeclean", fake_clean_card)], combine, erg_context),
        ("+ fake card screams 'alarm'",   REAL_READERS + [("fakealarm", fake_alarm_card)], combine, erg_context),
        ("fake INTEGRATOR (min-combine)", REAL_READERS, evil_combine, erg_context),
        ("fake ERG (clears all)",         REAL_READERS, combine, evil_erg),
    ]
    print(f"{'injected fake':32} | verdict | note")
    print("-" * 70)
    for name, rd, cb, eg in rows:
        v = pipeline(rd, cb, eg)
        note = ""
        if "fake card lies" in name:      note = "lie ignored (add-only) — SAFE" if v != "OK" else "BYPASS"
        elif "screams" in name:           note = "false alarm (noise, not bypass)"
        elif "INTEGRATOR" in name:        note = "BYPASS — integrator can lower!" if v == "OK" else "held"
        elif "fake ERG" in name:          note = "BYPASS — ERG can lower!" if v == "OK" else "held"
        else:                             note = "threat caught"
        print(f"{name:32} | {v:7} | {note}")
    print("\n" + "=" * 70)
    print("Lesson: a fake CARD is add-only — it cannot clear a real alarm (severity-max).")
    print("        The INTEGRATOR (combine) and the ERG CAN lower a verdict — they are")
    print("        the trusted core and MUST be integrity-checked at load time.")

if __name__ == "__main__":
    run()
