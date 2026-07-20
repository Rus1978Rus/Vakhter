# -*- coding: utf-8 -*-
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


def subject_of(name, component_hash):
    return f"{name}|{component_hash}"


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


def accept_change(name, component_hash, role, signatures, authorised):
    """Gate a component change under the role's quorum policy."""
    threshold = POLICY.get(role, POLICY["lowering"])   # unknown role -> strictest
    subject = subject_of(name, component_hash)
    ok, signers = verify_quorum(subject, signatures, authorised, threshold)
    return ok, threshold, signers
