# -*- coding: utf-8 -*-
"""
PROVENANCE layer for the integrity gate — the Notarius idea, applied.

Check #4 built the INTEGRITY gate (hash of each component vs a manifest). But a
hash only answers "did the file change since the manifest was written?" — it does
NOT answer "is this component of legitimate origin?". An attacker who swaps in a
malicious component AND regenerates the manifest passes a pure-hash check.

  INTEGRITY  = "container unchanged"     (hash)
  PROVENANCE = "element is NATIVE"       (origin + signed lineage + length witness)
  SIGNED != NATIVE.

Each component carries a provenance record:
  - hash    : sha256 of the bytes            (integrity)
  - cp_len  : Unicode codepoint count        (crypto-free insertion witness —
              any inserted char, incl. invisibles ZWSP/ZWJ/BOM, shifts it)
  - lineage : a chain of conveyor steps, EACH signed by the author's key. An
              attacker without that key cannot forge a lineage for a new hash.

Signing here is HMAC with a secret the author holds; in production this is an
asymmetric signature (author signs with a private key; the gate verifies with
the public key). The security property demonstrated is identical: you cannot
mint NATIVE provenance without the author's key.
"""
import hashlib
import hmac
import os

CONVEYOR_STEPS = ("created", "reviewed", "closed")


def file_hash(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def cp_len(path):
    """Unicode codepoint length — the crypto-free length witness."""
    with open(path, "r", encoding="utf-8", errors="surrogatepass") as f:
        return len(f.read())


def _sign(secret, msg):
    return hmac.new(secret, msg.encode("utf-8"), hashlib.sha256).hexdigest()


def stamp(name, path, author_secret, steps=CONVEYOR_STEPS):
    """AUTHOR side (needs the key): produce a provenance record after the
    conveyor closes a component."""
    h = file_hash(path)
    lineage = []
    prev = "ROOT"
    for step in steps:
        sig = _sign(author_secret, f"{name}|{h}|{step}|{prev}")
        lineage.append({"step": step, "prev": prev, "sig": sig})
        prev = sig
    return {"name": name, "origin": "author-conveyor",
            "hash": h, "cp_len": cp_len(path), "lineage": lineage}


def verify_native(record, path, verifier_key):
    """GATE side: return one of
       NATIVE | MISSING | TAMPERED | INVISIBLE_INSERT | NO_PROVENANCE | FORGED_LINEAGE."""
    if not path or not os.path.exists(path):
        return "MISSING"
    if file_hash(path) != record.get("hash"):
        return "TAMPERED"                       # integrity: bytes changed
    if cp_len(path) != record.get("cp_len"):
        return "INVISIBLE_INSERT"               # length witness: char count shifted
    lineage = record.get("lineage")
    if not lineage:
        return "NO_PROVENANCE"                   # signed maybe, but no origin trace
    prev = "ROOT"
    for s in lineage:                            # every step must be author-signed
        expect = _sign(verifier_key, f"{record['name']}|{record['hash']}|{s['step']}|{prev}")
        if s.get("prev") != prev or not hmac.compare_digest(expect, s.get("sig", "")):
            return "FORGED_LINEAGE"              # SIGNED != NATIVE — no author key
        prev = s["sig"]
    return "NATIVE"


# --- the two gates, for A/B comparison ---
def gate_hash_only(manifest_hashes, files):
    """OLD gate: pass iff every file's hash is in the manifest (and nothing extra)."""
    for name, expected in manifest_hashes.items():
        p = files.get(name)
        if not p or not os.path.exists(p) or file_hash(p) != expected:
            return False, name
    for name in files:
        if name not in manifest_hashes:
            return False, name
    return True, None


def gate_native(records, files, verifier_key):
    """NEW gate: every component must verify NATIVE, and nothing extra may load."""
    report = []
    ok = True
    for name, rec in records.items():
        status = verify_native(rec, files.get(name), verifier_key)
        report.append((name, status))
        if status != "NATIVE":
            ok = False
    for name in files:
        if name not in records:
            report.append((name, "UNKNOWN (no provenance record)")); ok = False
    return ok, report
