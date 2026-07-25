# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
Self-integrity honest-report contract (external conveyor, option B; AD-32).

The guard must NEVER show a fake green integrity check. Two honest behaviours:
  - default mode: the guard serves normally, but self-report is 'unverified'
    (it does NOT claim proof it does not have);
  - strict mode without a real anchor: the guard REFUSES TO SERVE — every call
    returns a conclusive block — instead of pretending integrity is proven.
"""
import importlib
import os

from _support import ok

import self_integrity
import product


def test_status_never_fakes_verified():
    # No out-of-process anchor is shipped in this build -> honest 'unverified',
    # and never a fabricated 'verified', even if an anchor path is merely named.
    old = os.environ.pop("VAKHTER_INTEGRITY_ANCHOR", None)
    try:
        ok(self_integrity.integrity_status() == "unverified",
           "no anchor must report 'unverified'")
        os.environ["VAKHTER_INTEGRITY_ANCHOR"] = "/mnt/ro/manifest.json"
        ok(self_integrity.integrity_status() != "verified",
           "a merely-named anchor must NOT be reported as 'verified' (no real "
           "verifier in this build)")
    finally:
        os.environ.pop("VAKHTER_INTEGRITY_ANCHOR", None)
        if old is not None:
            os.environ["VAKHTER_INTEGRITY_ANCHOR"] = old


def test_default_mode_serves_normally():
    old = os.environ.pop("VAKHTER_REQUIRE_INTEGRITY", None)
    try:
        f = product.analyze("just a normal sentence")
        ok(f.label == "clean", f"default mode must serve; got {f.label} — {f.reason}")
    finally:
        if old is not None:
            os.environ["VAKHTER_REQUIRE_INTEGRITY"] = old


def test_strict_mode_refuses_to_serve():
    old = os.environ.get("VAKHTER_REQUIRE_INTEGRITY")
    os.environ["VAKHTER_REQUIRE_INTEGRITY"] = "1"
    os.environ.pop("VAKHTER_INTEGRITY_ANCHOR", None)
    try:
        # strict + no proven integrity -> refuse to serve, even benign input,
        # even input that would otherwise be perfectly clean.
        f = product.analyze("just a normal sentence")
        ok(f.label != "clean", "strict mode without anchor must NOT return clean")
        ok(f.signature == "integrity_unverified",
           f"expected integrity_unverified block, got {f.signature!r}")
        ok(f.conclusive, "the refusal must be conclusive (a hard block)")
    finally:
        if old is None:
            os.environ.pop("VAKHTER_REQUIRE_INTEGRITY", None)
        else:
            os.environ["VAKHTER_REQUIRE_INTEGRITY"] = old
