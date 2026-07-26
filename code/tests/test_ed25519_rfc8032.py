# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
Ed25519 correctness — pinned against the official RFC 8032 test vectors (AD-36).

The integrity scheme's security rests on this pure-Python Ed25519 being byte-exact
Ed25519. These are two authoritative RFC 8032 §7.1 vectors: for each, the derived
public key AND the produced signature must match the RFC exactly, the signature
must verify, and any tamper (to message or key) must be rejected. A hand-rolled
crypto routine that reproduces the standard's own vectors is the correctness proof.
"""
from _support import ok

import _ed25519 as ed


def _hx(s):
    return bytes.fromhex(s)


# (secret seed, public key, message, signature) — RFC 8032 §7.1 TEST 2 and TEST 3
_VECTORS = [
    ("4ccd089b28ff96da9db6c346ec114e0f5b8a319f35aba624da8cf6ed4fb8a6fb",
     "3d4017c3e843895a92b70aa74d1b7ebc9c982ccf2ec4968cc0cd55f12af4660c",
     "72",
     "92a009a9f0d4cab8720e820b5f642540a2b27b5416503f8fb3762223ebdb69da"
     "085ac1e43e15996e458f3613d0f11d8c387b2eaeb4302aeeb00d291612bb0c00"),
    ("c5aa8df43f9f837bedb7442f31dcb7b166d38535076f094b85ce3a2e0b4458f7",
     "fc51cd8e6218a1a38da47ed00230f0580816ed13ba3303ac5deb911548908025",
     "af82",
     "6291d657deec24024827e69c3abe01a30ce548a284743a445e3680d7db5ac3ac"
     "18ff9b538d16f290ae67f760984dc6594a7c15e9716ed28dc027beceea1ec40a"),
]


def test_rfc8032_vectors_match_exactly():
    for skh, pkh, mh, sigh in _VECTORS:
        sk, m = _hx(skh), _hx(mh)
        pub = ed.publickey(sk)
        ok(pub.hex() == pkh, f"pubkey mismatch for {mh}: {pub.hex()} != {pkh}")
        sig = ed.sign(m, sk, pub)
        ok(sig.hex() == sigh, f"signature mismatch for {mh}")
        ok(ed.verify(sig, m, pub), f"valid signature failed to verify for {mh}")


def test_tamper_is_rejected():
    for skh, pkh, mh, sigh in _VECTORS:
        sk, m = _hx(skh), _hx(mh)
        pub, sig = ed.publickey(sk), _hx(sigh)
        ok(not ed.verify(sig, m + b"!", pub), "altered message must be rejected")
        ok(not ed.verify(sig, m, bytes(32)), "wrong public key must be rejected")
        bad = bytearray(sig); bad[0] ^= 1
        ok(not ed.verify(bytes(bad), m, pub), "altered signature must be rejected")


def test_verify_never_raises_on_garbage():
    ok(ed.verify(b"", b"msg", bytes(32)) is False, "empty sig -> False, no raise")
    ok(ed.verify(b"\x00" * 64, b"msg", b"short") is False, "short key -> False, no raise")
