# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
PREPENDED / ENCLOSING-FORMAT axis card, before/after — the Cf-but-NOT-default-
ignorable tail (outside 'class 138'): format chars that ACT on their scope.
  BEFORE = canonicalize -> real MSL + supplement + digit + metachar + all invisible axes + tail
  AFTER  = BEFORE + dedicated prepended-format card
Three tiers: ALARM (scope abuse / bracket imbalance), WATCH (balanced interlinear
annotation — Unicode: not for interchange), OK (in-script prepend / balanced
segment).
Run:  MSL_MIP_HOME=/path/to/msl_mip  python range_prepended.py
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
from prepended_format_cards import prepended_format_cards_reader

READERS = [supplement_reader, digit_cards_reader, metachar_cards_reader,
           invisible_cards_reader, bidi_cards_reader, tag_cards_reader,
           vs_cards_reader, whitespace_cards_reader, monitored_cards_reader,
           hangul_filler_cards_reader, script_ignorable_cards_reader,
           reserved_ignorable_cards_reader]

def _base(c):
    f = real_text_reader(c)
    for r in READERS:
        f = combine(f, r(c))
    return f

def before_reader(t):
    return _base(canonicalize(t)[0])

def after_reader(t):
    c = canonicalize(t)[0]
    return combine(_base(c), prepended_format_cards_reader(c))

BEFORE = InvariantEngine(before_reader, erg.no_stream)
AFTER  = InvariantEngine(after_reader,  erg.no_stream)

ANS = chr(0x0600)                          # ARABIC NUMBER SIGN (prepended concat mark)
AYAH = chr(0x06DD)                         # ARABIC END OF AYAH
AR_DIG = "١٢٣"              # arabic-indic digits ١٢٣
ANCHOR, SEP, TERM = chr(0xFFF9), chr(0xFFFA), chr(0xFFFB)   # interlinear annotation
EGY_B, EGY_E = chr(0x13437), chr(0x13438)  # egyptian begin/end segment
GLYPH = chr(0x13000)                       # an egyptian hieroglyph (segment content)

CASES = [
    # ---- ALARM: scope abuse + bracket imbalance ----
    ("THREAT", "sign on ascii",   "amount " + ANS + "1000 USD"),          # arabic sign over ASCII digits
    ("THREAT", "ayah orphan",     "verse " + AYAH + " ok"),               # end-of-ayah not on arabic digit
    ("THREAT", "ann unbalanced",  "base" + ANCHOR + "hidden ruby text"),  # anchor, no terminator
    ("THREAT", "sep orphan",      "a" + SEP + "b annotation"),            # separator, no annotation
    ("THREAT", "seg unbalanced",  "glyph " + EGY_B + GLYPH + " more"),    # begin, no end
    # ---- WATCH: balanced annotation (not for interchange) ----
    ("WITNESS","ann balanced",    "kanji" + ANCHOR + "kana" + TERM + " ruby"),
    # ---- OK: in-script prepend / balanced segment ----
    ("BENIGN", "arabic number",   "raqm " + ANS + AR_DIG + " tamam"),     # sign + arabic digits
    ("BENIGN", "egypt segment",   "text " + EGY_B + GLYPH + EGY_E + " end"),
    ("BENIGN", "plain text",      "an ordinary sentence with nothing odd"),
]


def run():
    print("PREPENDED / ENCLOSING-FORMAT AXIS (Cf-not-DI tail) — before/after")
    print("=" * 76)
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
        print(f"{kind:7} | {name:14} | before={b:5} after={a:5}{tag}")

    thr = [c for c in CASES if c[0] == "THREAT"]; ben = [c for c in CASES if c[0] == "BENIGN"]
    bc = sum(1 for k,n,t in thr if BEFORE.analyze(t).risk != "OK")
    ac = sum(1 for k,n,t in thr if AFTER.analyze(t).risk != "OK")
    bf = sum(1 for k,n,t in ben if BEFORE.analyze(t).risk != "OK")
    af = sum(1 for k,n,t in ben if AFTER.analyze(t).risk != "OK")
    print("\n" + "=" * 76)
    print(f"scope-abuse/imbalance caught : before {bc}/{len(thr)} ({bc*100//len(thr)}%)"
          f"  ->  after {ac}/{len(thr)} ({ac*100//len(thr)}%)   (+{fixed})")
    print(f"legit in-script kept OK      : before {len(ben)-bf}/{len(ben)}"
          f"  ->  after {len(ben)-af}/{len(ben)}   (new FP: {fp_new})")
    print("This tail is Cf-but-NOT-default-ignorable: format that ACTS, not hides.")


if __name__ == "__main__":
    run()
