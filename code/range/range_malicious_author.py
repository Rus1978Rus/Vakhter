# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
COMPONENT CHECK #5 — the malicious author (a legit signer embeds a threat).

Scenario: the attacker HAS the tool and the author key. They author a backdoored
ERG "by author decision" and sign it. Provenance says NATIVE (the signature is
real). Question: does anything still stop it?

We show:
  - a fake CARD, even signed, cannot bypass (add-only) — the easy attack fails.
  - a signed backdoored ERG passes PROVENANCE (NATIVE) ...
  - ... but FAILS the behavioral battery -> rejected. SIGNED != SAFE.
Run:  MSL_MIP_HOME=/path/to/msl_mip  python range_malicious_author.py
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
for _cand in ("canon", "canonicalization"):
    _p = os.path.abspath(os.path.join(HERE, "..", _cand))
    if os.path.isdir(_p):
        sys.path.insert(0, _p); break
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "invariant_engine")))
sys.path.insert(0, HERE)

from invariant_engine.core import Finding
from erg_context import erg_context
from behavioral import accept_lowering_component

# the good ERG (real one) and a backdoored ERG the malicious author writes + signs
def good_erg(c, f):
    return erg_context(c, f)
def backdoored_erg(c, f):
    return Finding("clean", 0.0, "BACKDOOR: cleared by malicious author")
def backdoored_card(_):                       # malicious author adds a lying card too
    return Finding("clean", 0.0, "FAKE clean")

def run():
    print("COMPONENT CHECK #5 — malicious author (SIGNED != SAFE)")
    print("=" * 70)
    print("Assume the signature on every component below is VALID (attacker = author).\n")

    # 1) signed malicious CARD — add-only, cannot silence
    from canonicalize import canonicalize
    from behavioral import _base, _verdict, combine
    c = canonicalize("id=1%27 OR %271%27=%271")[0]
    with_fake_card = _verdict(combine(_base(c, combine), backdoored_card(c)))
    print(f"signed malicious CARD    -> threat verdict: {with_fake_card}   "
          f"({'harmless (add-only)' if with_fake_card != 'OK' else 'BYPASS'})")

    # 2) signed backdoored ERG — passes provenance, fails behavior
    ok_good, _ = accept_lowering_component(candidate_erg=good_erg)
    ok_evil, silenced = accept_lowering_component(candidate_erg=backdoored_erg)
    print(f"\nsigned GOOD ERG          -> behavioral gate: {'ACCEPT' if ok_good else 'REJECT'}")
    print(f"signed BACKDOORED ERG    -> provenance: NATIVE (valid signature)")
    print(f"                            behavioral gate: {'ACCEPT' if ok_evil else 'REJECT'}"
          f"   (silences {len(silenced)}/{len(silenced) or ''} known threats)" if not ok_evil
          else "")
    print("\n" + "=" * 70)
    print("A valid signature made the backdoor NATIVE — but the behavioral battery")
    print("rejected it because it silences known threats. Signature proves ORIGIN;")
    print("the battery proves it still honors the guard's invariants. Need BOTH.")
    print("Residual (subtle backdoor passing the battery) -> m-of-n sign-off on")
    print("lowering components + append-only transparency log.")

if __name__ == "__main__":
    run()
