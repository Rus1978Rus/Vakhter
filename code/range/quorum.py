# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
m-of-n QUORUM — no single key can push a LOWERING component.

Check #5 left one residual: a malicious author (or a stolen key) can sign a
backdoor that passes the behavioral battery. Closing it is organizational, not
cryptographic: a change to a lowering component (ERG / integrator) requires at
least M distinct signatures out of N authorised signers. One compromised key is
not enough.

Signing is HMAC per signer here (demo); in production each signer has their own
asymmetric key. The property is the same: you need M different people/keys.
"""
import hmac
import hashlib

# how many signatures each role needs
POLICY = {"lowering": 3, "normal": 1}     # ERG/integrator need 3-of-N; cards need 1


def _sign(secret, msg):
    return hmac.new(secret, msg.encode("utf-8"), hashlib.sha256).hexdigest()


def _canon(*parts):
    """Unambiguous field encoding: LENGTH-PREFIX each field so a delimiter inside
    a field cannot shift boundaries. Without this, subject_of('a','b|c') and
    subject_of('a|b','c') both render 'a|b|c', so one signature is valid for two
    different (name,hash) pairs (audit finding, PoC in test_trust_core.py)."""
    return "\x1e".join(f"{len(p)}:{p}" for p in (str(x) for x in parts))


def subject_of(name, component_hash, epoch=0):
    """Bind a signature to (name, hash, EPOCH). The epoch is a monotonic version
    counter: an approval signed at epoch N does not validate at epoch M, so old
    signatures cannot be REPLAYED to re-accept a rolled-back component (audit
    finding). Callers thread the component's current epoch; default 0 keeps the
    single-version demo working."""
    return _canon(name, component_hash, epoch)


def sign_as(signer_id, secret, subject):
    """One signer signs the subject (component name + hash)."""
    return {"signer": signer_id, "sig": _sign(secret, subject)}


def verify_quorum(subject, signatures, authorised, threshold):
    """Count DISTINCT authorised signers with a valid signature over `subject`.
    Duplicates and unknown signers do not count. Return (ok, valid_signers)."""
    valid = set()
    for s in signatures:
        sid, sig = s.get("signer"), s.get("sig", "")
        if sid in authorised and sid not in valid:
            if hmac.compare_digest(_sign(authorised[sid], subject), sig):
                valid.add(sid)
    return (len(valid) >= threshold, sorted(valid))


def accept_change(name, component_hash, role, signatures, authorised, epoch=0):
    """Gate a component change under the role's quorum policy, bound to `epoch`
    (the component's current monotonic version — signatures for any other epoch
    do not count, blocking rollback replay)."""
    threshold = POLICY.get(role, POLICY["lowering"])   # unknown role -> strictest
    subject = subject_of(name, component_hash, epoch)
    ok, signers = verify_quorum(subject, signatures, authorised, threshold)
    return ok, threshold, signers
