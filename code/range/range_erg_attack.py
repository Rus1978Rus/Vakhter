# -*- coding: utf-8 -*-
"""
COMPONENT CHECK #2 — adversarial red-team of the ERG / context layer.

The ERG layer's job is to SOFTEN false alarms. That makes it the highest-stakes
component: if an attacker can wrap a REAL threat in a benign FRAME (a question
about it, a definition of it, a legit-looking structure) and trick ERG into
clearing it, that is a SILENT bypass of the whole guard.

We compare, for each input:
    RAW  = full pipeline WITHOUT the ERG layer
    ERG  = full pipeline WITH ERG softening
A threat is SILENCED if RAW != OK but ERG == OK. Silenced threats MUST be 0.
We also keep the intended false-positive cleanups to prove the fix still helps.

Run:  MSL_MIP_HOME=/path/to/msl_mip  python range_erg_attack.py
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
from invariant_engine.msl_real import real_text_reader
from invariant_engine.supplement import supplement_reader, combine
from digit_cards import digit_cards_reader
from metachar_cards import metachar_cards_reader
from invisible_cards import invisible_cards_reader
from harden_cards import harden_cards_reader
from erg_context import erg_context
from fail_closed import safe_reader

READERS = [("msl", real_text_reader), ("supplement", supplement_reader),
           ("digit", digit_cards_reader), ("metachar", metachar_cards_reader),
           ("invisible", invisible_cards_reader), ("harden", harden_cards_reader)]

def _raw(text):
    c = canonicalize(text)[0]
    f = None
    for n, r in READERS:
        g = safe_reader(n, r, c)
        f = g if f is None else combine(f, g)
    return c, f

def verdict(f):
    return "OK" if f.label == "clean" else ("ALARM" if f.conclusive else "WATCH")

def raw_verdict(text):
    return verdict(_raw(text)[1])

def erg_verdict(text):
    c, f = _raw(text)
    return verdict(erg_context(c, f))

# threat wrapped in a benign frame — each MUST NOT be silenced to OK
ATTACKS = [
    ("phish in question",   "is paypal.com.evil.ru/verify a safe site to use?"),
    ("phish definitional",  "for example, paypal.com.evil.ru/login is the address"),
    ("userinfo in question","what does admin@paypal.com.evil.ru mean here?"),
    ("subdomain phish Q",   "how do I log in to secure-login.paypal.com.evil.ru?"),
    ("homoglyph in Q",      "is paypa1.com the real one?"),
    ("cyrillic in Q",       "what is ра" + "ypal.com exactly?"),
    ("metadata ip in Q",    "can you explain http://169.254.169.254/ to me?"),
    ("traversal-ish Q",     "how do I open the file at etc/passwd/config?"),
    ("templated phish",     "render {{ paypal.com.evil.ru }} here"),
    ("shellvar phish",      "set URL=${paypal.com.evil.ru} please"),
]
# intended FP cleanups — should STILL reach OK (proves the fix keeps precision)
BENIGN = [
    ("shell var",     "export PATH=${HOME}/bin:$PATH"),
    ("template var",  "Hello {{ user.name }}, welcome"),
    ("git ssh",       "clone git@github.com:openai/whisper.git"),
    ("slash define",  "the / character is the code for a path separator"),
    ("dotdot Q",      "How do I use ../ in a relative import?"),
]

def run():
    print("COMPONENT CHECK #2 — adversarial ERG red-team")
    print("=" * 74)
    print(f"{'attack (threat in benign frame)':32} | {'RAW':6} | {'ERG':6}")
    print("-" * 74)
    silenced = 0
    for name, text in ATTACKS:
        rv, ev = raw_verdict(text), erg_verdict(text)
        tag = ""
        if rv != "OK" and ev == "OK":
            tag = "  <- !!! SILENCED (bypass) !!!"; silenced += 1
        elif rv == "ALARM" and ev == "WATCH":
            tag = "  (softened, still flagged)"
        print(f"{name:32} | {rv:6} | {ev:6}{tag}")
    print("-" * 74)
    cleared = 0
    for name, text in BENIGN:
        rv, ev = raw_verdict(text), erg_verdict(text)
        if ev == "OK":
            cleared += 1
        print(f"{'FP: '+name:32} | {rv:6} | {ev:6}{'  (cleared OK)' if ev=='OK' else ''}")
    print("\n" + "=" * 74)
    print(f"THREATS SILENCED TO OK : {silenced}   (safety gate — MUST be 0)")
    print(f"intended FPs cleared    : {cleared}/{len(BENIGN)}")

if __name__ == "__main__":
    run()
