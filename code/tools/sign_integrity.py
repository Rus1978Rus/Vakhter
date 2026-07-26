# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
Offline integrity signer (AUTHOR-ONLY tool; AD-36).

Run this on a TRUSTED, OFFLINE machine — the one place the private signing seed
ever exists. It builds a manifest of the runtime file hashes and signs it with
Ed25519. The private seed NEVER ships; only the public key + manifest + signature
do, onto a read-only mount at deploy.

    # 1) once: make a keypair. Keep the seed OFFLINE and SECRET.
    python code/tools/sign_integrity.py --keygen  secret.seed

    # 2) each release: sign the current runtime into an anchor directory.
    python code/tools/sign_integrity.py --sign  secret.seed  dist/anchor  0.1.0

Then deploy dist/anchor (manifest.json + manifest.sig) on a READ-ONLY mount and set:
    VAKHTER_INTEGRITY_ANCHOR=/ro/anchor
    VAKHTER_INTEGRITY_PUBKEY=<the printed public key hex>

The pubkey is printed and also written to <anchor>/pubkey.hex for convenience — but
PIN it in your deploy config / immutable image, do not trust a copy that travels in
a writable place. The read-only mount is the load-bearing control (AD-36).
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, "..", "range"))

import _ed25519 as ed                 # noqa: E402
import integrity_verify as iv         # noqa: E402


def keygen(seed_path):
    if os.path.exists(seed_path):
        sys.stderr.write(f"refusing to overwrite existing {seed_path}\n")
        return 2
    seed = os.urandom(32)
    # write 0600 so the secret is not world-readable
    fd = os.open(seed_path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, "wb") as f:
        f.write(seed)
    pub = ed.publickey(seed)
    print(f"wrote secret seed -> {seed_path}  (KEEP OFFLINE, chmod 600, back up)")
    print(f"public key (hex): {pub.hex()}")
    return 0


def sign(seed_path, anchor_dir, version):
    with open(seed_path, "rb") as f:
        seed = f.read()
    if len(seed) != 32:
        sys.stderr.write("seed must be exactly 32 bytes (use --keygen)\n")
        return 2
    pub = ed.publickey(seed)
    manifest = iv.build_manifest(version)
    mbytes = iv.manifest_bytes(manifest)
    sig = ed.sign(mbytes, seed, pub)

    os.makedirs(anchor_dir, exist_ok=True)
    with open(os.path.join(anchor_dir, "manifest.json"), "wb") as f:
        f.write(mbytes)
    with open(os.path.join(anchor_dir, "manifest.sig"), "wb") as f:
        f.write(sig)
    with open(os.path.join(anchor_dir, "pubkey.hex"), "w") as f:
        f.write(pub.hex() + "\n")

    print(f"signed {len(manifest['files'])} runtime files -> {anchor_dir}")
    print(f"version: {version}")
    print(f"public key (hex): {pub.hex()}")
    print("deploy the anchor on a READ-ONLY mount; set VAKHTER_INTEGRITY_ANCHOR "
          "and VAKHTER_INTEGRITY_PUBKEY.")
    return 0


def main(argv):
    if len(argv) >= 2 and argv[0] == "--keygen":
        return keygen(argv[1])
    if len(argv) >= 3 and argv[0] == "--sign":
        version = argv[3] if len(argv) >= 4 else "0.0.0"
        return sign(argv[1], argv[2], version)
    sys.stderr.write(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
