# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
WHITESPACE axis card, before/after — space-lookalikes by real vector.
  BEFORE = canonicalize -> real MSL + supplement + digit + metachar + invisible + bidi + tag + vs
  AFTER  = BEFORE + dedicated whitespace card
Three tiers, per the priority guidance:
  ALARM   = line/paragraph separator (U+2028/9) OR a lookalike doing delimiter
            duty against a metacharacter.
  WITNESS = a lookalike in an ASCII context (WATCH; "not auto-HIGH").
  OK      = lookalike as genuine i18n typography (flanked by non-ASCII letters),
            or no lookalikes.
Run:  MSL_MIP_HOME=/path/to/msl_mip  python range_whitespace.py
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

def _base(c):
    f = real_text_reader(c)
    f = combine(f, supplement_reader(c))
    f = combine(f, digit_cards_reader(c))
    f = combine(f, metachar_cards_reader(c))
    f = combine(f, invisible_cards_reader(c))
    f = combine(f, bidi_cards_reader(c))
    f = combine(f, tag_cards_reader(c))
    f = combine(f, vs_cards_reader(c))
    return f

def before_reader(t):
    return _base(canonicalize(t)[0])

def after_reader(t):
    c = canonicalize(t)[0]
    return combine(_base(c), whitespace_cards_reader(c))

BEFORE = InvariantEngine(before_reader, erg.no_stream)
AFTER  = InvariantEngine(after_reader,  erg.no_stream)

NBSP, NNBSP, EMSP, IDEO = chr(0x00A0), chr(0x202F), chr(0x2003), chr(0x3000)
FIGSP = chr(0x2007)
LINESEP, PARASEP = chr(0x2028), chr(0x2029)

CASES = [
    # ---- ALARM: separators + delimiter masquerade ----
    ("THREAT", "line sep inject", "user=admin" + LINESEP + "role=root"),
    ("THREAT", "para sep inject", "row1" + PARASEP + "; DROP TABLE t"),
    ("THREAT", "nbsp command",    "rm" + NBSP + "-rf /tmp/data"),
    ("THREAT", "nnbsp pipe",      "cat f" + NNBSP + "| sh"),
    ("THREAT", "emsp equals",     "role" + EMSP + "=" + EMSP + "admin"),
    # ---- WITNESS: lookalike in ASCII context (WATCH, not auto-HIGH) ----
    ("WITNESS", "nbsp two words",  "hello" + NBSP + "world today"),
    ("WITNESS", "figure number",   "total 1" + FIGSP + "000 units"),
    # ---- OK: genuine i18n typography / none ----
    ("BENIGN", "cjk ideo space",  "日本" + IDEO + "語 の 文"),
    ("BENIGN", "accented nbsp",   "Café" + NBSP + "résumé served"),
    ("BENIGN", "plain ascii",     "just a normal sentence here"),
]


def run():
    print("WHITESPACE AXIS — space-lookalikes by real vector, before/after")
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
    print(f"sep/delimiter caught   : before {bc}/{len(thr)} ({bc*100//len(thr)}%)"
          f"  ->  after {ac}/{len(thr)} ({ac*100//len(thr)}%)   (+{fixed})")
    print(f"legit typography kept OK: before {len(ben)-bf}/{len(ben)}"
          f"  ->  after {len(ben)-af}/{len(ben)}   (new FP: {fp_new})")
    print("WITNESS tier held at WATCH — 'space-lookalike != automatically dangerous'.")


if __name__ == "__main__":
    run()
