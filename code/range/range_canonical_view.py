# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
canonical_view axis — parser-DESYNC detection, before/after.
  BEFORE = the invisible/zero-width card alone (judges ONE string; alnum word-split)
  AFTER  = BEFORE + canonical_view (compares raw vs canonical readings)
The marginal value: an invisible adjacent to DOMAIN/TOKEN punctuation (. - _ @)
splits the token differently in raw vs canonical views, but the alnum-only
word-split heuristic only WATCHes it. canonical_view escalates that real
parser-desync to ALARM, while staying clean on emoji glue and trailing invisibles
(the invisible sits outside any token -> the two views agree).
Run:  MSL_MIP_HOME=/path/to/msl_mip  python range_canonical_view.py
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
for _cand in ("canon", "canonicalization"):
    _p = os.path.abspath(os.path.join(HERE, "..", _cand))
    if os.path.isdir(_p):
        sys.path.insert(0, _p); break
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "invariant_engine")))
sys.path.insert(0, HERE)

from invariant_engine.core import judge
from invariant_engine.supplement import combine
from invisible_cards import invisible_cards_reader
from canonical_view import canonical_view_reader, canonical_view

ZWSP, ZWJ, SHY, BOM = chr(0x200B), chr(0x200D), chr(0x00AD), chr(0xFEFF)

def before(text):
    return judge(invisible_cards_reader(text), 0.0).risk

def after(text):
    return judge(combine(invisible_cards_reader(text), canonical_view_reader(text)), 0.0).risk

def cv_only(text):
    return judge(canonical_view_reader(text), 0.0).risk

CASES = [
    # ---- NEWLY CLOSED: invisible against domain/token punctuation (. - @) ----
    ("THREAT", "zwsp before dot",  "visit pay" + ZWSP + ".pal.com now"),
    ("THREAT", "zwsp before at",   "mail user" + ZWSP + "@host.com today"),
    ("THREAT", "shy before hyphen","go sub" + SHY + "-domain.com now"),
    # ---- already caught by word-split; desync now explicit ----
    ("THREAT", "zwsp in word",     "admin" + ZWSP + "istrator granted"),
    ("THREAT", "zwsp in domain",   "visit pay" + ZWSP + "pal now"),
    # ---- BENIGN (invisible outside any token -> views agree) ----
    ("BENIGN", "emoji zwj glue",   "team 👨" + ZWJ + "👩 grew"),
    ("BENIGN", "no invisible",     "visit paypal.com now"),
    ("BENIGN", "trailing zwsp",    "hello world" + ZWSP),
]


def run():
    print("canonical_view — parser-DESYNC (B5), before/after")
    print("=" * 72)
    closed = fp = 0
    for kind, name, text in CASES:
        b, a, cv = before(text), after(text), cv_only(text)
        tag = ""
        if kind == "THREAT" and b != "ALARM" and a == "ALARM":
            tag = "  <= CLOSED (WATCH->ALARM, parser_desync)"; closed += 1
        elif kind == "THREAT" and b == "ALARM":
            tag = "  (already ALARM; desync confirmed)"
        if kind == "BENIGN" and cv != "OK":
            tag = "  <= canonical_view FALSE ALARM"; fp += 1
        raw, canon = text, canonical_view(text)[0]
        div = " raw!=canon" if raw != canon else ""
        print(f"{kind:6} | {name:15} | before={b:5} after={a:5} cv={cv:5}{tag}{div}")

    thr = [c for c in CASES if c[0] == "THREAT"]; ben = [c for c in CASES if c[0] == "BENIGN"]
    b_alarm = sum(1 for k,n,t in thr if before(t) == "ALARM")
    a_alarm = sum(1 for k,n,t in thr if after(t) == "ALARM")
    cv_fp = sum(1 for k,n,t in ben if cv_only(t) != "OK")
    print("\n" + "=" * 72)
    print(f"desync threats at ALARM : before {b_alarm}/{len(thr)}  ->  after {a_alarm}/{len(thr)}   (+{closed})")
    print(f"canonical_view own FP   : {cv_fp}/{len(ben)} benign")
    print("Marginal value: invisible against domain punctuation (. - @) WATCH->ALARM;")
    print("canonical_view itself is clean on emoji glue and trailing invisibles.")


if __name__ == "__main__":
    run()
