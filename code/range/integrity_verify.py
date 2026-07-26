# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
Real integrity — the offline-signature engine (AD-36, option A).

The self-hash tautology (AD-32) is unbreakable from inside a writable code dir: an
attacker who can rewrite the code rewrites the checker too. This module does NOT
pretend otherwise. It provides the ASYMMETRIC half of the real fix: the author
signs a manifest of runtime file hashes OFFLINE (private key never ships), and the
runtime verifies that signature with a PUBLIC key before re-hashing the files.

The load-bearing security property is NOT this Python — it is the anchor (manifest
+ signature) and the code living on a READ-ONLY MOUNT so the attacker cannot
rewrite the verifier or re-sign the manifest. The signature proves AUTHORSHIP
(only the offline key could have made it); the read-only mount proves the checker
itself was not swapped. Both are required; neither alone suffices. Without a
read-only mount this raises the bar (a tamper now needs the private key) but does
not close the tautology — which is exactly why AD-32's honest self-report remains
the default and this is opt-in.

Shared by the offline signer (tools/sign_integrity.py) and the runtime verifier
(self_integrity.integrity_status) so the two can never disagree on the file set or
the manifest serialization.
"""
import hashlib
import json
import os

_HERE = os.path.dirname(os.path.abspath(__file__))     # …/code/range
_ROOT = os.path.dirname(_HERE)                          # …/code
# the three dirs that make up the autonomous runtime (see the 22-file surface)
_RUNTIME_DIRS = ("range", "canonicalization",
                 os.path.join("invariant_engine", "invariant_engine"))


def runtime_files(root=_ROOT):
    """Deterministic, sorted list of every runtime .py, relative to `root`."""
    out = []
    for d in _RUNTIME_DIRS:
        base = os.path.join(root, d)
        for dp, _dns, fns in os.walk(base):
            if "__pycache__" in dp.split(os.sep):
                continue
            for fn in fns:
                if fn.endswith(".py"):
                    out.append(os.path.relpath(os.path.join(dp, fn), root))
    return sorted(out)


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def build_manifest(version, root=_ROOT):
    """{'version':…, 'files':{relpath: sha256hex}} over the runtime file set."""
    files = {rel: _sha256(os.path.join(root, rel)) for rel in runtime_files(root)}
    return {"version": version, "files": files}


def manifest_bytes(manifest):
    """The EXACT bytes that get signed AND written to manifest.json — one source of
    truth so the signature always covers the on-disk file byte-for-byte."""
    return json.dumps(manifest, sort_keys=True,
                      separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def verify_anchor(anchor_dir, pubkey_hex, root=_ROOT):
    """Return 'verified' or 'failed'.

    'verified' requires ALL of: the anchor's manifest.sig is a valid Ed25519
    signature over the exact manifest.json bytes under the pinned public key
    (authorship); every manifested file is present and its hash matches
    (integrity); and no runtime file exists that the manifest omits (no smuggled
    addition). Any failure, missing file, or malformed anchor -> 'failed'. Never
    raises."""
    import _ed25519 as ed
    try:
        with open(os.path.join(anchor_dir, "manifest.json"), "rb") as f:
            mbytes = f.read()
        with open(os.path.join(anchor_dir, "manifest.sig"), "rb") as f:
            sig = f.read()
        pub = bytes.fromhex(pubkey_hex.strip())
    except Exception:
        return "failed"

    if not ed.verify(sig, mbytes, pub):
        return "failed"                       # not signed by the pinned author key

    try:
        manifest = json.loads(mbytes.decode("utf-8"))
        files = manifest["files"]
    except Exception:
        return "failed"
    if not files:
        return "failed"

    for rel, want in files.items():
        p = os.path.join(root, rel)
        if not os.path.exists(p) or _sha256(p) != want:
            return "failed"                   # missing or changed runtime file
    if set(runtime_files(root)) != set(files.keys()):
        return "failed"                       # a runtime file the manifest omits
    return "verified"
