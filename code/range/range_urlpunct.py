# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
URL-PUNCTUATION axis — visible structural-punctuation deception, before/after.
  BEFORE = canonicalize -> real MSL + supplement + digit + metachar + confusable
  AFTER  = BEFORE + url-punct card (look-alike delimiters + at-userinfo)
Test set built from the MSL/MIP legacy cards (DOT / SOLIDUS / AT) so the legit
exceptions those cards proved (email, federated handle, clean URL, CJK prose)
stay OK.
Run:  MSL_MIP_HOME=/path/to/msl_mip  python range_urlpunct.py
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
from urlpunct_cards import urlpunct_cards_reader

def _base(c):
    f = real_text_reader(c)
    f = combine(f, supplement_reader(c))
    f = combine(f, digit_cards_reader(c))
    f = combine(f, metachar_cards_reader(c))
    f = combine(f, confusable_cards_reader(c))
    return f

def before_reader(t):
    return _base(canonicalize(t)[0])

def after_reader(t):
    c = canonicalize(t)[0]
    return combine(_base(c), urlpunct_cards_reader(c))

BEFORE = InvariantEngine(before_reader, erg.no_stream)
AFTER  = InvariantEngine(after_reader,  erg.no_stream)

FW_DOT, IDEO_DOT, FW_SLASH, FW_AT = chr(0xFF0E), chr(0x3002), chr(0xFF0F), chr(0xFF20)

CASES = [
    # ---- look-alike delimiter THREATS ----
    ("THREAT", "fullwidth dot",  "go to google"+FW_DOT+"com now"),
    ("THREAT", "ideographic dot","visit google"+IDEO_DOT+"com today"),
    ("THREAT", "fullwidth slash","open evil.com"+FW_SLASH+FW_SLASH+"bank.com"),
    ("THREAT", "fullwidth at",   "mail admin"+FW_AT+"host.com now"),
    # ---- at-userinfo THREATS (scheme-aware) ----
    ("THREAT", "userinfo spoof", "click http://paypal.com@evil.ru/login"),
    ("THREAT", "userinfo nosch", "visit paypal.com@evil.ru now"),
    # ---- BENIGN (legit cases the legacy cards proved) ----
    ("BENIGN", "clean url",      "see http://example.com/page here"),
    ("BENIGN", "plain email",    "write to ivan@example.com please"),
    ("BENIGN", "federated",      "follow @user@mastodon.social today"),
    ("BENIGN", "cjk prose",      "これは文です。次の文もある。"),
    ("BENIGN", "normal dots",    "version 2.5.1 and file report.pdf ok"),
]


def run():
    print("URL-PUNCTUATION AXIS — structural-punct deception, before/after")
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
        print(f"{kind:6} | {name:15} | before={b:5} after={a:5}{tag}")

    thr = [c for c in CASES if c[0] == "THREAT"]; ben = [c for c in CASES if c[0] == "BENIGN"]
    bc = sum(1 for k,n,t in thr if BEFORE.analyze(t).risk != "OK")
    ac = sum(1 for k,n,t in thr if AFTER.analyze(t).risk != "OK")
    bf = sum(1 for k,n,t in ben if BEFORE.analyze(t).risk != "OK")
    af = sum(1 for k,n,t in ben if AFTER.analyze(t).risk != "OK")
    print("\n" + "=" * 74)
    print(f"url-punct spoofs caught : before {bc}/{len(thr)} ({bc*100//len(thr)}%)"
          f"  ->  after {ac}/{len(thr)} ({ac*100//len(thr)}%)   (+{fixed})")
    print(f"legit cases kept OK     : before {len(ben)-bf}/{len(ben)}"
          f"  ->  after {len(ben)-af}/{len(ben)}   (new FP: {fp_new})")
    print("Legacy-proven exceptions (email, federated handle, clean URL, CJK) stay OK.")


if __name__ == "__main__":
    run()
