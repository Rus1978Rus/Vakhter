# -*- coding: utf-8 -*-
"""
CONTOUR TAIL — the three cards that complete the default-ignorable contour beyond
the 138 format chars: Hangul fillers (Lo), script-bound ignorable marks (Mn:
Mongolian FVS + Khmer inherent), and the reserved should-never-appear blanket.
  BEFORE = canonicalize -> real MSL + supplement + digit + metachar + all 6 invisible axes
  AFTER  = BEFORE + the three tail cards
Run:  MSL_MIP_HOME=/path/to/msl_mip  python range_contour_tail.py
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
from hangul_filler_cards import hangul_filler_cards_reader
from script_ignorable_cards import script_ignorable_cards_reader
from reserved_ignorable_cards import reserved_ignorable_cards_reader

def _base(c):
    f = real_text_reader(c)
    for r in (supplement_reader, digit_cards_reader, metachar_cards_reader,
              invisible_cards_reader, bidi_cards_reader, tag_cards_reader,
              vs_cards_reader, whitespace_cards_reader, monitored_cards_reader):
        f = combine(f, r(c))
    return f

def before_reader(t):
    return _base(canonicalize(t)[0])

def after_reader(t):
    c = canonicalize(t)[0]
    f = _base(c)
    f = combine(f, hangul_filler_cards_reader(c))
    f = combine(f, script_ignorable_cards_reader(c))
    f = combine(f, reserved_ignorable_cards_reader(c))
    return f

BEFORE = InvariantEngine(before_reader, erg.no_stream)
AFTER  = InvariantEngine(after_reader,  erg.no_stream)

FILL, CHO, JUNG = chr(0x3164), chr(0x115F), chr(0x1160)     # Hangul fillers
KA, MO = chr(0xAC00), chr(0x1820)                            # Hangul syllable / Mongolian letter
FVS1, FVS2 = chr(0x180B), chr(0x180C)                        # Mongolian free variation selectors
KHM, KHV = chr(0x1780), chr(0x17B4)                          # Khmer letter / inherent vowel
RES1, RES2 = chr(0x2065), chr(0xE0080)                       # reserved default-ignorable

CASES = [
    # ---- Hangul filler ----
    ("THREAT", "blank username",  FILL + FILL + FILL),
    ("THREAT", "filler pads ascii","admin" + FILL + " login"),
    ("BENIGN", "hangul compose",  CHO + JUNG + KA + " 한글"),
    # ---- script-bound ignorable (Mn) ----
    ("THREAT", "fvs orphan",      "data" + FVS1 + "x payload"),
    ("THREAT", "fvs carrier",     "hi" + MO + FVS1 + FVS2 + " there"),
    ("BENIGN", "mongolian fvs",   "text " + MO + FVS1 + " word"),
    ("BENIGN", "khmer inherent",  "khmer " + KHM + KHV + " text"),
    # ---- reserved should-never-appear ----
    ("THREAT", "reserved 2065",   "value" + RES1 + "here"),
    ("THREAT", "reserved e0080",  "hello" + RES2 + "world"),
    ("BENIGN", "plain text",      "an ordinary sentence with nothing odd"),
]


def run():
    print("CONTOUR TAIL — Hangul fillers + script-ignorable + reserved, before/after")
    print("=" * 76)
    fixed = fp_new = 0
    for kind, name, text in CASES:
        b = BEFORE.analyze(text).risk
        av = AFTER.analyze(text); a = av.risk
        tag = ""
        if kind == "THREAT" and b == "OK" and a != "OK":
            tag = f"  <= CLOSED ({av.finding.signature})"; fixed += 1
        if kind == "BENIGN" and b == "OK" and a != "OK":
            tag = f"  <= NEW false alarm ({av.finding.signature})"; fp_new += 1
        print(f"{kind:6} | {name:15} | before={b:5} after={a:5}{tag}")

    thr = [c for c in CASES if c[0] == "THREAT"]; ben = [c for c in CASES if c[0] == "BENIGN"]
    bc = sum(1 for k,n,t in thr if BEFORE.analyze(t).risk != "OK")
    ac = sum(1 for k,n,t in thr if AFTER.analyze(t).risk != "OK")
    bf = sum(1 for k,n,t in ben if BEFORE.analyze(t).risk != "OK")
    af = sum(1 for k,n,t in ben if AFTER.analyze(t).risk != "OK")
    print("\n" + "=" * 76)
    print(f"tail threats caught   : before {bc}/{len(thr)} ({bc*100//len(thr)}%)"
          f"  ->  after {ac}/{len(thr)} ({ac*100//len(thr)}%)   (+{fixed})")
    print(f"legit in-script kept OK: before {len(ben)-bf}/{len(ben)}"
          f"  ->  after {len(ben)-af}/{len(ben)}   (new FP: {fp_new})")
    print("Contour complete: 138 format chars (existing) + this tail = full DI set.")


if __name__ == "__main__":
    run()
