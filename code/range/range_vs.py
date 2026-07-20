# -*- coding: utf-8 -*-
"""
VARIATION-SELECTOR axis card, before/after — the Mn carrier axis.
  BEFORE = canonicalize -> real MSL + supplement + digit + metachar + invisible + bidi + tag
  AFTER  = BEFORE + dedicated VS card
The invisible card catches a gross VS run (>=3 or leading); this harness shows
what the dedicated Mn axis ADDS: a 2-length carrier run, and a single selector
sitting on a NON-base char (space / plain letter) — anomalies a Cf-only
invisible filter never sees — while keeping legit single-selector-on-base OK.
Run:  MSL_MIP_HOME=/path/to/msl_mip  python range_vs.py
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
import invisible_cards
from invisible_cards import invisible_cards_reader
from bidi_cards import bidi_cards_reader
from tag_cards import tag_cards_reader
from vs_cards import vs_cards_reader

# Card taxonomy: variation selectors are being SPLIT OUT to their own axis.
# So the honest baseline is the invisible card scoped to zero-width only —
# VS-blind — with the VS axis (this card) taking that responsibility.
invisible_cards.VS = set()

def _base(c):
    f = real_text_reader(c)
    f = combine(f, supplement_reader(c))
    f = combine(f, digit_cards_reader(c))
    f = combine(f, metachar_cards_reader(c))
    f = combine(f, invisible_cards_reader(c))
    f = combine(f, bidi_cards_reader(c))
    f = combine(f, tag_cards_reader(c))
    return f

def before_reader(t):
    return _base(canonicalize(t)[0])

def after_reader(t):
    c = canonicalize(t)[0]
    return combine(_base(c), vs_cards_reader(c))

BEFORE = InvariantEngine(before_reader, erg.no_stream)
AFTER  = InvariantEngine(after_reader,  erg.no_stream)

def VS(n):     # VS1..VS16 -> U+FE00..FE0F
    return chr(0xFE00 + n - 1)
VS16, VS15 = VS(16), VS(15)
VSSUP = chr(0xE0100)                 # first CJK variation selector supplement
HEART, SCISSORS = "❤", "✂"  # emoji-capable bases
CJK = "亜"                       # 亜 — a CJK ideograph base

CASES = [
    # ---- VS carrier / orphan THREATS ----
    ("THREAT", "carrier len2",  "hi" + HEART + VS16 + VS15 + " there"),     # run of 2 on one base
    ("THREAT", "carrier len5",  "data" + "".join(VS(i) for i in range(1,6)) + "x"),
    ("THREAT", "leading vs",    VS16 + "starts here"),
    ("THREAT", "vs on letter",  "pas" + "s" + VS16 + "word"),              # selector after plain ASCII
    ("THREAT", "vs on space",   "hello " + VS15 + "world"),                 # selector after a space
    # ---- BENIGN legit single-selector-on-base (must stay OK) ----
    ("BENIGN", "emoji heart",   "I love it " + HEART + VS16 + " a lot"),
    ("BENIGN", "text scissors", "cut here " + SCISSORS + VS15 + " please"),
    ("BENIGN", "cjk variant",   "kanji " + CJK + VSSUP + " form"),
    ("BENIGN", "plain text",    "an ordinary sentence with no selectors"),
    ("BENIGN", "plain emoji",   "nice work " + "\U0001F600" + " today"),
]


def run():
    print("VARIATION-SELECTOR AXIS (Mn carrier) — before/after")
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
        print(f"{kind:6} | {name:14} | before={b:5} after={a:5}{tag}")

    thr = [c for c in CASES if c[0] == "THREAT"]; ben = [c for c in CASES if c[0] == "BENIGN"]
    bc = sum(1 for k,n,t in thr if BEFORE.analyze(t).risk != "OK")
    ac = sum(1 for k,n,t in thr if AFTER.analyze(t).risk != "OK")
    bf = sum(1 for k,n,t in ben if BEFORE.analyze(t).risk != "OK")
    af = sum(1 for k,n,t in ben if AFTER.analyze(t).risk != "OK")
    print("\n" + "=" * 74)
    print(f"VS carrier/orphan caught : before {bc}/{len(thr)} ({bc*100//len(thr)}%)"
          f"  ->  after {ac}/{len(thr)} ({ac*100//len(thr)}%)   (+{fixed})")
    print(f"legit selectors kept OK  : before {len(ben)-bf}/{len(ben)}"
          f"  ->  after {len(ben)-af}/{len(ben)}   (new FP: {fp_new})")
    print("NOTE: VS are Mn (marks), not Cf (format) — a Cf-only filter never sees them.")


if __name__ == "__main__":
    run()
