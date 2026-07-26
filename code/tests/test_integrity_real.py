# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
Real integrity end-to-end (offline signature engine; AD-36).

An operator signs a manifest of the runtime files OFFLINE, deploys it, and the
guard verifies signature + hashes at runtime. These tests exercise the whole path
with an ephemeral key: a valid anchor -> 'verified'; every tamper class ->
'failed'; no config -> honest 'unverified'; and strict mode SERVES once integrity
is genuinely verified (it no longer refuses).
"""
import os
import tempfile

from _support import ok

import _ed25519 as ed
import integrity_verify as iv
import self_integrity
import product


def _fresh_anchor(mutate_manifest=None, sign_seed=None):
    """Build a signed anchor over the real runtime in a temp dir. Returns
    (anchor_dir, pubkey_hex). Optionally mutate the manifest before signing."""
    seed = os.urandom(32)
    pub = ed.publickey(seed)
    manifest = iv.build_manifest("test")
    if mutate_manifest:
        mutate_manifest(manifest)
    mbytes = iv.manifest_bytes(manifest)
    sig = ed.sign(mbytes, (sign_seed or seed), pub if sign_seed is None else ed.publickey(sign_seed))
    d = tempfile.mkdtemp()
    with open(os.path.join(d, "manifest.json"), "wb") as f:
        f.write(mbytes)
    with open(os.path.join(d, "manifest.sig"), "wb") as f:
        f.write(sig)
    return d, pub.hex()


def test_valid_anchor_verifies():
    d, pub = _fresh_anchor()
    ok(iv.verify_anchor(d, pub) == "verified", "a correctly signed anchor must verify")


def test_wrong_pubkey_fails():
    d, _pub = _fresh_anchor()
    other = ed.publickey(os.urandom(32)).hex()
    ok(iv.verify_anchor(d, other) == "failed", "a different pinned key must fail")


def test_tampered_manifest_fails():
    d, pub = _fresh_anchor()
    with open(os.path.join(d, "manifest.json"), "r+b") as f:
        b = f.read().replace(b'"version":"test"', b'"version":"evil"')
        f.seek(0); f.write(b); f.truncate()
    ok(iv.verify_anchor(d, pub) == "failed", "editing the signed manifest must fail")


def test_file_hash_mismatch_fails():
    # valid signature, but a manifest hash that will not match the real file
    def bad_hash(m):
        m["files"][sorted(m["files"])[0]] = "0" * 64
    d, pub = _fresh_anchor(mutate_manifest=bad_hash)
    ok(iv.verify_anchor(d, pub) == "failed", "a runtime file that does not match must fail")


def test_manifest_omitting_a_runtime_file_fails():
    def drop_one(m):
        del m["files"][sorted(m["files"])[0]]
    d, pub = _fresh_anchor(mutate_manifest=drop_one)
    ok(iv.verify_anchor(d, pub) == "failed",
       "a runtime file missing from the manifest (smuggled addition) must fail")


def test_no_config_is_unverified():
    old_a = os.environ.pop("VAKHTER_INTEGRITY_ANCHOR", None)
    old_p = os.environ.pop("VAKHTER_INTEGRITY_PUBKEY", None)
    try:
        ok(self_integrity.integrity_status() == "unverified",
           "no anchor/pubkey -> honest 'unverified', never 'verified'")
    finally:
        if old_a is not None:
            os.environ["VAKHTER_INTEGRITY_ANCHOR"] = old_a
        if old_p is not None:
            os.environ["VAKHTER_INTEGRITY_PUBKEY"] = old_p


def test_strict_mode_serves_once_verified():
    d, pub = _fresh_anchor()
    saved = {k: os.environ.get(k) for k in
             ("VAKHTER_INTEGRITY_ANCHOR", "VAKHTER_INTEGRITY_PUBKEY",
              "VAKHTER_REQUIRE_INTEGRITY")}
    os.environ["VAKHTER_INTEGRITY_ANCHOR"] = d
    os.environ["VAKHTER_INTEGRITY_PUBKEY"] = pub
    os.environ["VAKHTER_REQUIRE_INTEGRITY"] = "1"
    try:
        ok(self_integrity.integrity_status() == "verified", "anchor must verify")
        f = product.analyze("a perfectly clean sentence")
        ok(f.label == "clean",
           f"strict mode must SERVE once integrity is verified — got {f.label}/{f.signature}")
    finally:
        for k, v in saved.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
