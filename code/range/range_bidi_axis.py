# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
Bidi AXIS card, before/after — the directional-control (logical!=visual) axis.
  BEFORE = canonicalize -> real MSL + supplement + digit + metachar + invisible
  AFTER  = BEFORE + dedicated bidi-axis card
The invisible card already catches gross open/close imbalance; this harness
shows what the SEPARATE bidi axis adds: override reorder (Trojan Source),
token-split, pop underflow — while keeping legit RTL layout OK and NOT deleting
controls out of real Arabic/Hebrew text.
Run:  MSL_MIP_HOME=/path/to/msl_mip  python range_bidi_axis.py
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

def _base(c):
    f = real_text_reader(c)
    f = combine(f, supplement_reader(c))
    f = combine(f, digit_cards_reader(c))
    f = combine(f, metachar_cards_reader(c))
    f = combine(f, invisible_cards_reader(c))
    return f

def before_reader(t):
    return _base(canonicalize(t)[0])

def after_reader(t):
    c = canonicalize(t)[0]
    return combine(_base(c), bidi_cards_reader(c))

BEFORE = InvariantEngine(before_reader, erg.no_stream)
AFTER  = InvariantEngine(after_reader,  erg.no_stream)

LRE, RLE, PDF, LRO, RLO = (chr(0x202A), chr(0x202B), chr(0x202C),
                           chr(0x202D), chr(0x202E))
LRI, RLI, FSI, PDI = chr(0x2066), chr(0x2067), chr(0x2068), chr(0x2069)
LRM, RLM, ALM = chr(0x200E), chr(0x200F), chr(0x061C)
AR = "مرحبا"      # arabic
HE = "שלום"       # hebrew

CASES = [
    # ---- bidi-axis THREATS (logical != visual) ----
    ("THREAT", "override reorder", "access = level" + RLO + "NIMDA" + PDF + " ok"),
    ("THREAT", "trojan comment",   "return 1;" + RLO + "// " + PDF + "safe"),
    ("THREAT", "override open",    "if isAdmin" + LRO + " return true"),
    ("THREAT", "token split",      "user" + RLI + "name = root"),
    ("THREAT", "pop underflow",    "value" + PDI + " = 42 shown"),
    ("THREAT", "embed unclosed",   "amount " + RLE + "1000 credited"),
    # ---- BENIGN legit RTL layout (must stay OK, must NOT be deleted) ----
    ("BENIGN", "arabic plain",     "اهلا وسهلا بكم في الموقع"),
    ("BENIGN", "isolate rtl",      "name: " + FSI + AR + PDI + " (verified)"),
    ("BENIGN", "embed rtl",        "label " + RLE + HE + PDF + " ok"),
    ("BENIGN", "rlm after rtl",    AR + RLM + " 2026"),
    ("BENIGN", "mixed balanced",   "total " + LRI + "123" + PDI + " " + AR),
    ("BENIGN", "no bidi",          "plain ascii sentence here"),
]


def run():
    print("BIDI AXIS — directional-control card, before/after")
    print("=" * 74)
    fixed = fp_new = 0
    for kind, name, text in CASES:
        b = BEFORE.analyze(text).risk
        av = AFTER.analyze(text); a = av.risk
        tag = ""
        if kind == "THREAT" and b == "OK" and a != "OK":
            tag = f"  <= CLOSED ({av.finding.signature})"; fixed += 1
        if kind == "BENIGN" and b == "OK" and a != "OK":
            tag = f"  <= NEW false alarm ({av.finding.signature})"; fp_new += 1
        print(f"{kind:6} | {name:16} | before={b:5} after={a:5}{tag}")

    thr = [c for c in CASES if c[0] == "THREAT"]; ben = [c for c in CASES if c[0] == "BENIGN"]
    bc = sum(1 for k,n,t in thr if BEFORE.analyze(t).risk != "OK")
    ac = sum(1 for k,n,t in thr if AFTER.analyze(t).risk != "OK")
    bf = sum(1 for k,n,t in ben if BEFORE.analyze(t).risk != "OK")
    af = sum(1 for k,n,t in ben if AFTER.analyze(t).risk != "OK")
    print("\n" + "=" * 74)
    print(f"bidi-axis threats caught : before {bc}/{len(thr)} ({bc*100//len(thr)}%)"
          f"  ->  after {ac}/{len(thr)} ({ac*100//len(thr)}%)   (+{fixed})")
    print(f"legit RTL kept clean     : before {len(ben)-bf}/{len(ben)}"
          f"  ->  after {len(ben)-af}/{len(ben)}   (new FP: {fp_new})")
    print("NEVER_BLIND_STRIP: controls are flagged for review, never auto-deleted.")


if __name__ == "__main__":
    run()
