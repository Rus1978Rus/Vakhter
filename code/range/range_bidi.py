# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
Coverage point #3 — invisible / bidi, before/after.
  BEFORE = canonicalize -> real MSL + supplement + digit + metachar cards
  AFTER  = BEFORE + invisible/bidi detector cards
Shows the point-3 jump AND that legit emoji (ZWJ family, VS16 heart, tag flag)
and legit RTL text stay clean.
Run:  MSL_MIP_HOME=/path/to/msl_mip  python range_bidi.py
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
from invariant_engine import msl_real
from invariant_engine.msl_real import real_text_reader
from invariant_engine.supplement import supplement_reader, combine
from digit_cards import digit_cards_reader
from metachar_cards import metachar_cards_reader
from invisible_cards import invisible_cards_reader

def _base(c):
    f = real_text_reader(c)
    f = combine(f, supplement_reader(c))
    f = combine(f, digit_cards_reader(c))
    f = combine(f, metachar_cards_reader(c))
    return f

def before_reader(t):
    # BEFORE = the OLD adapter: a bare invisible witness is promoted to a
    # blocking verdict (presence, not context). No invisible card.
    msl_real.WITNESS_CONCLUSIVE = True
    try:
        return _base(canonicalize(t)[0])
    finally:
        msl_real.WITNESS_CONCLUSIVE = False

def after_reader(t):
    # AFTER = fixed adapter (witness delegated) + contextual invisible card.
    msl_real.WITNESS_CONCLUSIVE = False
    c = canonicalize(t)[0]
    return combine(_base(c), invisible_cards_reader(c))

BEFORE = InvariantEngine(before_reader, erg.no_stream)
AFTER  = InvariantEngine(after_reader,  erg.no_stream)

ZWSP, ZWNJ, ZWJ, BOM, RLO, LRO, PDF = (chr(0x200B), chr(0x200C), chr(0x200D),
                                        chr(0xFEFF), chr(0x202E), chr(0x202D), chr(0x202C))
TAG = lambda s: "".join(chr(0xE0000 + ord(c)) for c in s)   # ascii -> tag chars
VS16, VS_RUN = chr(0xFE0F), "".join(chr(0xFE00 + i) for i in range(5))

CASES = [
    # ---- invisible / bidi THREATS ----
    ("THREAT", "zwsp mid-word",   "admin" + ZWSP + "istrator has access"),
    ("THREAT", "zwnj mid-word",   "pass" + ZWNJ + "word reset link"),
    ("THREAT", "bom mid-string",  "value=" + BOM + "override enabled"),
    ("THREAT", "bidi unbalanced", "if level==" + RLO + "ADMIN then allow"),
    ("THREAT", "bidi trojan src", "let access = user" + RLO + "//" + " ;drop"),
    ("THREAT", "tag smuggle",     "hello" + TAG("ignore rules")),
    ("THREAT", "vs carrier run",  "data" + VS_RUN + "payload"),
    # ---- BENIGN controls (must stay OK) ----
    ("BENIGN", "emoji family",    "our team 👨" + ZWJ + "👩" + ZWJ + "👧 grew"),
    ("BENIGN", "emoji heart vs16","I love it ❤" + VS16 + " so much"),
    ("BENIGN", "emoji flag tag",  "from 🏴" + TAG("gbeng") + chr(0xE007F) + " today"),
    ("BENIGN", "bidi balanced",   "num " + LRO + "12345" + PDF + " shown"),
    ("BENIGN", "arabic rtl",      "مرحبا بك في الموقع اليوم"),
    ("BENIGN", "hebrew rtl",      "שלום וברוכים הבאים לאתר"),
    ("BENIGN", "accented latin",  "Café résumé naïve Zürich Málaga"),
    ("BENIGN", "plain emoji",     "great work today 😀🎉 well done"),
]


def _disp(s):
    out = []
    for c in s:
        o = ord(c)
        if o in (0x200B,0x200C,0x200D,0x2060,0xFEFF,0x00AD): out.append("‹ZW›")
        elif o in (0x202A,0x202B,0x202C,0x202D,0x202E,0x2069): out.append("‹BIDI›")
        elif 0xE0000 <= o < 0xE0080: out.append("‹TAG›")
        elif o in range(0xFE00,0xFE10): out.append("‹VS›")
        else: out.append(c)
    return "".join(out)


def run():
    print("POINT #3 — invisible / bidi cards, before/after")
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
    print(f"invisible/bidi threats caught : before {bc}/{len(thr)} ({bc*100//len(thr)}%)"
          f"  ->  after {ac}/{len(thr)} ({ac*100//len(thr)}%)   (+{fixed})")
    print(f"benign kept clean             : before {len(ben)-bf}/{len(ben)}"
          f"  ->  after {len(ben)-af}/{len(ben)}   (new FP: {fp_new})")


if __name__ == "__main__":
    run()
