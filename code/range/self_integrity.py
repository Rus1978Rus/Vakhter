# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
SELF-INTEGRITY REPORT — honest, never a fake green check (external conveyor,
option B AD-32; real signature engine AD-36).

A guard made of pure in-process Python CANNOT cryptographically prove that its
own code is intact from INSIDE a writable code directory: an attacker who can
rewrite the code rewrites the checker AND any manifest sitting beside it too (the
"self-hash tautology" the external conveyor named as security theatre). So this
module never pretends. It reports the TRUTH about what self-protection is actually
deployed:

  'unverified' : no out-of-process anchor + pinned public key are configured (the
                 default). The guard still runs, but makes NO claim of proof.
  'verified'   : an offline-signed manifest (Ed25519) verified under the pinned
                 public key AND every runtime file re-hashed to its manifest value
                 (AD-36). The load-bearing property is that the anchor + code sit
                 on a READ-ONLY MOUNT so the verifier could not be swapped.
  'failed'     : an anchor was configured but the signature or a file hash did NOT
                 match -> possible tamper.

The signature proves AUTHORSHIP (only the offline private key could have made it);
the read-only mount proves the checker was not replaced. Both are required. With
neither configured the honest status is 'unverified' — never a green 'ok'.

Strict mode (opt-in): set VAKHTER_REQUIRE_INTEGRITY=1 and the guard REFUSES TO
SERVE unless status is 'verified' — the fail-closed posture ("I cannot prove
myself, so I will not pretend to guard"). Off by default so the guard stays
usable; on for deployments that have provisioned the anchor.

Config (both required to reach 'verified'):
  VAKHTER_INTEGRITY_ANCHOR = dir holding manifest.json + manifest.sig (read-only)
  VAKHTER_INTEGRITY_PUBKEY = the author's Ed25519 public key, hex (the pin)
"""
import os

_STATUS_CACHE = {}          # (anchor, pubkey) -> status; verify once per process


def integrity_status():
    """'verified' | 'failed' | 'unverified'. Truthful by construction: with no
    out-of-process anchor + pinned key this returns 'unverified', never a
    fabricated 'verified'. A co-located manifest alone is NOT accepted as proof —
    only an Ed25519 signature under the pinned public key (AD-36)."""
    anchor = os.environ.get("VAKHTER_INTEGRITY_ANCHOR")
    pubkey = os.environ.get("VAKHTER_INTEGRITY_PUBKEY")
    if not anchor or not pubkey:
        return "unverified"
    key = (anchor, pubkey)
    if key not in _STATUS_CACHE:
        try:
            from integrity_verify import verify_anchor
            _STATUS_CACHE[key] = verify_anchor(anchor, pubkey)
        except Exception:
            _STATUS_CACHE[key] = "failed"      # fail-closed: any verifier error
    return _STATUS_CACHE[key]


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
            "rather than present a fake green check; deploy the read-only mount + "
            "offline-signed anchor (AD-36) to enable proven integrity",
            conclusive=True, signature="integrity_unverified")
    return None
