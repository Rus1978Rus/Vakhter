# -*- coding: utf-8 -*-
"""
MONITORED-FORMAT axis card, before/after — the WITNESS tier.
  BEFORE = canonicalize -> real MSL + supplement + digit + metachar + invisible + bidi + tag + vs + whitespace
  AFTER  = BEFORE + dedicated monitored-format card
Demonstrates "observe all, prioritize the real vectors": monitored controls are
WATCH by default, ALARM only in a hostile context (word-split / metachar), OK
inside their legit substrate (music / shorthand).
Run:  MSL_MIP_HOME=/path/to/msl_mip  python range_monitored.py
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
from invariant_engine import InvariantEngine, erg
from invariant_engine.msl_real import real_text_reader
from invariant_engine.supplement import supplement_reader, combine
from digit_cards import digit_cards_reader
from metachar_cards import metachar_cards_reader
from invisible_cards import invisible_cards_reader
from bidi_cards import bidi_cards_reader
from tag_cards import tag_cards_reader
from vs_cards import vs_cards_reader
from whitespace_cards import whitespace_cards_reader
from monitored_cards import monitored_cards_reader

def _base(c):
    f = real_text_reader(c)
    f = combine(f, supplement_reader(c))
    f = combine(f, digit_cards_reader(c))
    f = combine(f, metachar_cards_reader(c))
    f = combine(f, invisible_cards_reader(c))
    f = combine(f, bidi_cards_reader(c))
    f = combine(f, tag_cards_reader(c))
    f = combine(f, vs_cards_reader(c))
    f = combine(f, whitespace_cards_reader(c))
    return f

def before_reader(t):
    return _base(canonicalize(t)[0])

def after_reader(t):
    c = canonicalize(t)[0]
    return combine(_base(c), monitored_cards_reader(c))

BEFORE = InvariantEngine(before_reader, erg.no_stream)
AFTER  = InvariantEngine(after_reader,  erg.no_stream)

MVS = chr(0x180E)                       # MONGOLIAN VOWEL SEPARATOR
NDS = chr(0x206E)                       # NATIONAL DIGIT SHAPES (deprecated)
ISS = chr(0x206A)                       # INHIBIT SYMMETRIC SWAPPING (deprecated)
MUS_BEAM = chr(0x1D173)                 # MUSICAL SYMBOL BEGIN BEAM
MUS_NOTE = chr(0x1D15F)                 # a musical symbol (substrate)
SHORT = chr(0x1BCA0)                    # SHORTHAND FORMAT LETTER OVERLAP
DUP = chr(0x1BC02)                      # a Duployan letter (substrate)

CASES = [
    # ---- ALARM: monitored control in a hostile context ----
    ("THREAT", "mvs word split",  "admin" + MVS + "istrator role"),
    ("THREAT", "nds in token",    "user" + NDS + "name = root"),
    ("THREAT", "iss on metachar", "value" + ISS + "= admin"),
    # ---- WITNESS: present, held at WATCH (not auto-HIGH) ----
    ("WITNESS", "lone mvs",        "greeting " + MVS + " text"),
    ("WITNESS", "lone deprecated", "digits " + NDS + " here"),
    # ---- OK: inside legit substrate / none ----
    ("BENIGN", "music control",   MUS_NOTE + MUS_BEAM + MUS_NOTE + " score"),
    ("BENIGN", "shorthand ctrl",  DUP + SHORT + DUP + " duployan"),
    ("BENIGN", "plain text",      "an ordinary sentence with nothing odd"),
]


def run():
    print("MONITORED-FORMAT AXIS (witness tier) — before/after")
    print("=" * 74)
    fixed = fp_new = 0
    for kind, name, text in CASES:
        b = BEFORE.analyze(text).risk
        av = AFTER.analyze(text); a = av.risk
        tag = ""
        if kind == "THREAT" and b == "OK" and a != "OK":
            tag = f"  <= CLOSED ({av.finding.signature})"; fixed += 1
        if kind == "WITNESS":
            tag = f"  <= WITNESS ({av.finding.signature})" if a != "OK" else ""
        if kind == "BENIGN" and b == "OK" and a != "OK":
            tag = f"  <= NEW false alarm ({av.finding.signature})"; fp_new += 1
        print(f"{kind:7} | {name:15} | before={b:5} after={a:5}{tag}")

    thr = [c for c in CASES if c[0] == "THREAT"]; ben = [c for c in CASES if c[0] == "BENIGN"]
    bc = sum(1 for k,n,t in thr if BEFORE.analyze(t).risk != "OK")
    ac = sum(1 for k,n,t in thr if AFTER.analyze(t).risk != "OK")
    bf = sum(1 for k,n,t in ben if BEFORE.analyze(t).risk != "OK")
    af = sum(1 for k,n,t in ben if AFTER.analyze(t).risk != "OK")
    print("\n" + "=" * 74)
    print(f"hostile-context caught : before {bc}/{len(thr)} ({bc*100//len(thr)}%)"
          f"  ->  after {ac}/{len(thr)} ({ac*100//len(thr)}%)   (+{fixed})")
    print(f"legit substrate kept OK: before {len(ben)-bf}/{len(ben)}"
          f"  ->  after {len(ben)-af}/{len(ben)}   (new FP: {fp_new})")
    print("WITNESS tier held at WATCH — 'observe all, prioritize the real vectors'.")


if __name__ == "__main__":
    run()
