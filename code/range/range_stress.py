# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
STRESS TEST — attacks on the guard ITSELF (denial-of-service / exhaustion).
Runs each abusive input through: self_defense front gate -> (if it passes) the
full pipeline. Every case must finish FAST (bounded work) and never hang/crash.
Run:  MSL_MIP_HOME=/path/to/msl_mip  python range_stress.py
"""
import os, sys, time, signal
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
from guard import guarded_analyze

def _pipeline(text):
    c = canonicalize(text)[0]
    f = real_text_reader(c)
    for r in (supplement_reader, digit_cards_reader, metachar_cards_reader,
              invisible_cards_reader, harden_cards_reader):
        f = combine(f, r(c))
    return erg_context(c, f)

def guarded(text):
    """Cheap pre-checks + the pipeline under a hard time budget."""
    return guarded_analyze(text, _pipeline)

_pipeline("warmup so MSL boot is not billed to the first budgeted call")

def timed(name, text, limit=10):
    # No signal here — the time budget lives INSIDE guarded_analyze (single timer
    # owner). The outer `timeout` shell command is the last-resort backstop.
    t0 = time.time()
    try:
        r = guarded(text); dt = (time.time() - t0) * 1000
        verdict = getattr(r, "signature", "") or r.label
        flag = "  <-- slow" if dt > 1800 else ""
        print(f"{name:30} len={len(text):>9}  {dt:8.1f} ms   -> {verdict}{flag}")
    except Exception as e:
        print(f"{name:30} len={len(text):>9}  CRASH: {type(e).__name__}: {str(e)[:36]}")

CASES = [
    ("normal short",        "hello paypal.com login"),
    ("10k invisible zwsp",  "a" + chr(0x200B) * 10_000),
    ("100k invisible zwsp", "a" + chr(0x200B) * 100_000),
    ("1M invisible zwsp",   "a" + chr(0x200B) * 1_000_000),
    ("100k bidi controls",  chr(0x202E) * 100_000),
    ("1M plain chars",      "x" * 1_000_000),
    ("10M plain chars",     "x" * 10_000_000),
    ("nested percent bomb", "%25" * 100_000),
    ("100k tag chars",      "".join(chr(0xE0041) for _ in range(100_000))),
    ("dns redos probe",     "a" * 50 + "." * 50_000),
    ("500k digit run",      "1" * 500_000),
    ("real threat (short)", "id=1%27 OR %271%27=%271"),
    ("64 invisibles (ok)",  "hi" + chr(0x200B) * 64),
]

def run():
    print("STRESS TEST — attacks on the guard itself (with self-defense gate)")
    print("=" * 74)
    for name, text in CASES:
        timed(name, text)

if __name__ == "__main__":
    run()
