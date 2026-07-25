# -*- coding: utf-8 -*-
"""
SELF-INTEGRITY REPORT — honest, never a fake green check (external conveyor,
option B; recorded in AUTHOR_DECISIONS AD-32).

A guard made of pure in-process Python CANNOT cryptographically prove that its
own code is intact: an attacker who can rewrite the code directory rewrites the
checker AND any manifest sitting beside it too (the "self-hash tautology" the
external conveyor named as security theatre). integrity.py holds the hash
machinery, but a manifest co-located with the code it checks proves nothing on
its own. So this module refuses to pretend. It reports the TRUTH about what
self-protection is actually deployed:

  'unverified' : no OUT-OF-PROCESS anchor is present (the default). The guard
                 still runs, but makes NO claim that its integrity is proven.
  'verified'   : a real external anchor (read-only mount + offline signature,
                 AD-32) was configured AND matched. NOT shipped in this build.
  'failed'     : an anchor was configured but did NOT match -> possible tamper.

Because a genuine anchor is not part of this build, honest status here is
'unverified' — never a green 'ok'. When AD-32 (read-only mount + Ed25519) is
deployed, integrity_status() gains a real body; until then it does not lie.

Strict mode (opt-in): set VAKHTER_REQUIRE_INTEGRITY=1 and the guard REFUSES TO
SERVE unless status is 'verified' — the fail-closed posture ("I cannot prove
myself, so I will not pretend to guard"). Off by default so the guard stays
usable; on for deployments that have provisioned the anchor.
"""
import os


def integrity_status():
    """'verified' | 'failed' | 'unverified'. Truthful by construction: with no
    out-of-process anchor deployed this returns 'unverified', never a
    fabricated 'verified'. A co-located manifest is NOT accepted as proof."""
    if not os.environ.get("VAKHTER_INTEGRITY_ANCHOR"):
        return "unverified"
    # A path was named, but this build ships no real out-of-process verifier
    # (Ed25519 + read-only mount, AD-32). Refuse to fake a pass; tell the truth.
    return "unverified"


def strict_mode():
    """True when the operator demands PROVEN integrity before the guard serves."""
    return os.environ.get("VAKHTER_REQUIRE_INTEGRITY") == "1"


def integrity_gate():
    """Honest fail-closed gate. Returns a BLOCKING Finding when the guard must
    refuse to serve (integrity demanded via strict mode but not proven), else
    None. This is the whole point of option B: refuse, rather than serve behind
    a fake green check."""
    if strict_mode() and integrity_status() != "verified":
        from invariant_engine.core import Finding
        return Finding(
            "suspect", 0.9,
            "integrity unproven and strict mode on — guard refuses to serve "
            "rather than present a fake green check; deploy the read-only+"
            "signature anchor (AD-32) to enable proven integrity",
            conclusive=True, signature="integrity_unverified")
    return None
