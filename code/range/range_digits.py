# -*- coding: utf-8 -*-
"""
Digit-focused empirical run WITH before/after.
  BEFORE = canonicalize -> real MSL only
  AFTER  = canonicalize -> real MSL + supplement + simulated digit cards
Shows: which misses the drafted digit cards close, and whether benign
numbers start false-alarming.
Run:  MSL_MIP_HOME=/path/to/msl_mip  python range_digits.py
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

def before_reader(t):
    return real_text_reader(canonicalize(t)[0])

def after_reader(t):
    c = canonicalize(t)[0]
    f = real_text_reader(c)
    f = combine(f, supplement_reader(c))
    f = combine(f, digit_cards_reader(c))
    return f

BEFORE = InvariantEngine(before_reader, erg.no_stream)
AFTER  = InvariantEngine(after_reader,  erg.no_stream)

CYR = "раypal.com"  # раypal.com (Cyrillic р,а)

CASES = [
    # ---- digit / IP / confusable THREATS ----
    ("THREAT", "homoglyph 1->l",  "login at paypa1.com now"),
    ("THREAT", "homoglyph 1 netflix","watch netf1ix.com/free"),
    ("THREAT", "homoglyph 0->o",  "visit g00gle.com"),
    ("THREAT", "homoglyph 0 msft", "update micr0s0ft.com"),
    ("THREAT", "homoglyph 3->e",  "search googl3.com"),
    ("THREAT", "homoglyph 5->s",  "buy from micro5oft.com"),
    ("THREAT", "cyrillic confuse", "log in " + CYR),
    ("THREAT", "ip metadata",     "http://169.254.169.254/latest/meta-data/"),
    ("THREAT", "ip private",      "http://192.168.0.1/admin"),
    ("THREAT", "ip loopback:port","http://127.0.0.1:8080/debug"),
    ("THREAT", "ip decimal",      "http://2130706433/login"),
    ("THREAT", "ip hex",          "http://0x7f000001/x"),
    ("THREAT", "ip wildcard 0",   "http://0/admin"),
    ("THREAT", "overlong /",      "..%c0%af..%c0%afetc%c0%afpasswd"),
    # ---- BENIGN digit controls (must stay OK) ----
    ("BENIGN", "version",         "we shipped version 1.0.3 today"),
    ("BENIGN", "pi",              "pi is about 3.14159"),
    ("BENIGN", "phone",           "call +7 900 123 45 67"),
    ("BENIGN", "year",            "founded in 2026, 5 people"),
    ("BENIGN", "chem",            "H2O and CO2 and COVID-2019"),
    ("BENIGN", "math",            "2 + 2 = 4 and 5*5=25"),
    ("BENIGN", "price",           "only $5.99 for 3 items"),
    ("BENIGN", "product",         "the new iPhone 15 and iOS 18"),
    ("BENIGN", "public-dns talk", "8.8.8.8 is Google DNS (as text)"),
    ("BENIGN", "brand no-leet",   "the real paypal.com is fine"),
    ("BENIGN", "cyrillic legit",  "Привет, заходи на сайт"),
]


def run():
    print("DIGIT-FOCUSED RUN — before (real MSL) vs after (+ digit cards)")
    print("=" * 76)
    fixed = fp_new = 0
    for kind, name, text in CASES:
        b = BEFORE.analyze(text).risk
        av = AFTER.analyze(text)
        a = av.risk
        tag = ""
        if kind == "THREAT" and b == "OK" and a != "OK":
            tag = "  <= CLOSED by digit cards"; fixed += 1
        if kind == "BENIGN" and b == "OK" and a != "OK":
            tag = "  <= NEW false alarm"; fp_new += 1
        disp = text.replace("​", "‹ZWSP›")
        print(f"{kind:6} | {name:16} | before={b:5} after={a:5}{tag}")
        if tag.startswith("  <= CLOSED"):
            print(f"         └ {av.finding.reason[:70]}")

    print("\n" + "=" * 76)
    thr = [c for c in CASES if c[0] == "THREAT"]
    ben = [c for c in CASES if c[0] == "BENIGN"]
    b_caught = sum(1 for k,n,t in thr if BEFORE.analyze(t).risk != "OK")
    a_caught = sum(1 for k,n,t in thr if AFTER.analyze(t).risk != "OK")
    b_fp = sum(1 for k,n,t in ben if BEFORE.analyze(t).risk != "OK")
    a_fp = sum(1 for k,n,t in ben if AFTER.analyze(t).risk != "OK")
    print(f"threats caught : before {b_caught}/{len(thr)}   ->   after {a_caught}/{len(thr)}   (+{fixed})")
    print(f"benign clean   : before {len(ben)-b_fp}/{len(ben)}   ->   after {len(ben)-a_fp}/{len(ben)}   (new FP: {fp_new})")


if __name__ == "__main__":
    run()
