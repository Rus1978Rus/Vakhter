# -*- coding: utf-8 -*-
"""
CONFUSABLE / HOMOGLYPH axis — visible-deception, before/after.
  BEFORE = canonicalize -> real MSL + supplement + digit + metachar (no cross-script sense)
  AFTER  = BEFORE + confusable card (mixed/whole-script confusable)
Shows the homoglyph jump AND that genuine single-script text stays clean:
real Latin brands, real Russian words (native anchor), accented Latin, CJK.
Run:  MSL_MIP_HOME=/path/to/msl_mip  python range_confusable.py
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
from confusable_cards import confusable_cards_reader

def _base(c):
    f = real_text_reader(c)
    f = combine(f, supplement_reader(c))
    f = combine(f, digit_cards_reader(c))
    f = combine(f, metachar_cards_reader(c))
    return f

def before_reader(t):
    return _base(canonicalize(t)[0])

def after_reader(t):
    c = canonicalize(t)[0]
    return combine(_base(c), confusable_cards_reader(c))

BEFORE = InvariantEngine(before_reader, erg.no_stream)
AFTER  = InvariantEngine(after_reader,  erg.no_stream)

# Cyrillic look-alikes: а=0430 е=0435 о=043E р=0440 с=0441 у=0443 х=0445
a, e, o, p, c, y = chr(0x0430), chr(0x0435), chr(0x043E), chr(0x0440), chr(0x0441), chr(0x0443)
GRK_o = chr(0x03BF)   # greek omicron

CASES = [
    # ---- mixed-script confusable THREATS ----
    ("THREAT", "cyr paypal",   "login at pay"+a+"pal.com now"),        # cyrillic а
    ("THREAT", "cyr apple",    "update "+a+"pple.com account"),         # leading cyrillic а
    ("THREAT", "cyr google",   "go to g"+o+o+"gle.com search"),         # two cyrillic о
    ("THREAT", "cyr microsoft","open micr"+o+"s"+o+"ft.com portal"),    # cyrillic о
    ("THREAT", "grk omicron",  "visit g"+GRK_o+"ogle.com today"),       # greek omicron
    ("THREAT", "whole-script", "sign in "+y+a+chr(0x04BB)+o+o+".com"),  # уаһоо -> yahoo (all Cyrillic)
    # ---- BENIGN single-script (must stay OK) ----
    ("BENIGN", "real paypal",  "login at paypal.com now"),             # all latin
    ("BENIGN", "russian word", "привет мир как дела"),                 # genuine russian (anchors)
    ("BENIGN", "accented",     "Zürich café résumé naïve"),            # latin-1 accents
    ("BENIGN", "cjk text",     "日本語 の 文書 です"),                    # single-script CJK
]


def run():
    print("CONFUSABLE / HOMOGLYPH AXIS — visible-deception, before/after")
    print("=" * 72)
    fixed = fp_new = 0
    for kind, name, text in CASES:
        b = BEFORE.analyze(text).risk
        av = AFTER.analyze(text); a_ = av.risk
        tag = ""
        if kind == "THREAT" and b == "OK" and a_ != "OK":
            tag = f"  <= CLOSED ({av.finding.signature})"; fixed += 1
        if kind == "WITNESS":
            tag = f"  <= WITNESS ({av.finding.signature})" if a_ != "OK" else ""
        if kind == "BENIGN" and b == "OK" and a_ != "OK":
            tag = f"  <= NEW false alarm ({av.finding.signature})"; fp_new += 1
        print(f"{kind:7} | {name:12} | before={b:5} after={a_:5}{tag}")

    thr = [x for x in CASES if x[0] == "THREAT"]; ben = [x for x in CASES if x[0] == "BENIGN"]
    bc = sum(1 for k,n,t in thr if BEFORE.analyze(t).risk != "OK")
    ac = sum(1 for k,n,t in thr if AFTER.analyze(t).risk != "OK")
    bf = sum(1 for k,n,t in ben if BEFORE.analyze(t).risk != "OK")
    af = sum(1 for k,n,t in ben if AFTER.analyze(t).risk != "OK")
    print("\n" + "=" * 72)
    print(f"homoglyph spoofs caught : before {bc}/{len(thr)} ({bc*100//len(thr)}%)"
          f"  ->  after {ac}/{len(thr)} ({ac*100//len(thr)}%)   (+{fixed})")
    print(f"genuine text kept OK    : before {len(ben)-bf}/{len(ben)}"
          f"  ->  after {len(ben)-af}/{len(ben)}   (new FP: {fp_new})")
    print("Law: LOOKS_SAME != IS_SAME. Real Russian (native anchor) stays OK.")


if __name__ == "__main__":
    run()
