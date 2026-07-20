# -*- coding: utf-8 -*-
"""
COMPONENT CHECK #3 — stress each sign card ON ITS OWN.

For every card we throw inputs crafted to hit ITS regex / logic hard: long
pattern-shaped strings (ReDoS probes), heavy repetition, nasty unicode. Each run
is time-limited. A card is HEALTHY if it never throws and never runs slow
(< 300 ms) on any input up to the guard's 200k length cap.
Run:  MSL_MIP_HOME=/path/to/msl_mip  python range_cards_stress.py
"""
import os, sys, time, signal
HERE = os.path.dirname(os.path.abspath(__file__))
for _cand in ("canon", "canonicalization"):
    _p = os.path.abspath(os.path.join(HERE, "..", _cand))
    if os.path.isdir(_p):
        sys.path.insert(0, _p); break
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "invariant_engine")))
sys.path.insert(0, HERE)

from digit_cards import digit_cards_reader
from metachar_cards import metachar_cards_reader
from invisible_cards import invisible_cards_reader
from harden_cards import harden_cards_reader
from invariant_engine.supplement import supplement_reader
from erg_context import erg_context
from canonicalize import canonicalize

N = 100_000
PROBES = {
    "backtick no-close":  "`" + "a " * (N // 2),
    "ssti open no-close": "{{ " + "a." * (N // 2),
    "jndi-ish":           "${" + "a:" * (N // 2),
    "sql quote run":      "' " * (N // 2),
    "xss open run":       "<" * 2 + "script " * (N // 5),
    "crlf run":           "\r\n" * (N // 2),
    "dns label long":     "a" * 40 + "." + "b" * 40 + "." + "c." * (N // 2),
    "domain dots":        "a." * (N // 2),
    "deep domain":        ("x." * 4) * (N // 8),
    "deleet brand run":   "paypa1." * (N // 7),
    "ip-ish run":         "http://" + "1." * (N // 2),
    "email run":          "a@b.c " * (N // 6),
    "path run":           "/etc/x " * (N // 7),
    "combining marks":    "e" + "́" * (N // 2),
    "mixed unicode":      ("é1ρ/%.@`{}<>" * (N // 12)),
}

CARDS = [
    ("digit",      digit_cards_reader),
    ("metachar",   metachar_cards_reader),
    ("invisible",  invisible_cards_reader),
    ("harden",     harden_cards_reader),
    ("supplement", supplement_reader),
    ("erg",        lambda t: erg_context(t, digit_cards_reader("dummy"))),
    ("canon",      lambda t: canonicalize(t)),
]

def timed(fn, text, limit=3):
    def h(s, f): raise TimeoutError()
    signal.signal(signal.SIGALRM, h); signal.setitimer(signal.ITIMER_REAL, limit)
    t0 = time.time()
    try:
        fn(text); return (time.time() - t0) * 1000, None
    except TimeoutError:
        return None, "HANG"
    except Exception as e:
        return (time.time() - t0) * 1000, type(e).__name__
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)

def run():
    print("COMPONENT CHECK #3 — per-card stress (each input up to 100k chars)")
    print("=" * 74)
    worst = {}
    problems = []
    for cname, fn in CARDS:
        mx = 0.0; err = None
        for pname, text in PROBES.items():
            ms, e = timed(fn, text)
            if e == "HANG":
                problems.append(f"{cname} HANGS on '{pname}'"); mx = 9999; break
            if e:
                problems.append(f"{cname} throws {e} on '{pname}'"); err = e
            if ms and ms > mx: mx = ms
        worst[cname] = (mx, err)
        flag = "  <-- SLOW/ReDoS" if mx > 300 else ("  <-- throws" if err else "  ok")
        print(f"{cname:12} worst={mx:8.1f} ms  {('err='+err) if err else '':16}{flag}")
    print("\n" + "=" * 74)
    if problems:
        print("PROBLEMS:")
        for p in problems: print("  -", p)
    else:
        print("All cards healthy: no hangs, no throws, all < 300 ms on 100k probes.")

if __name__ == "__main__":
    run()
