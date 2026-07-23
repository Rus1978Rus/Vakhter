# -*- coding: utf-8 -*-
"""
Trust-core audit, made permanent (provenance.py / quorum.py).

Two real weaknesses found in the HMAC demo and FIXED here; one is the documented
HMAC-symmetry limitation that only Ed25519 closes (AD-12) — pinned as a known
property so a future reader knows it is deliberate, not an oversight.
"""
import os
import sys

from _support import ok, eq

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(_HERE, "..", "range")))
sys.path.insert(0, os.path.abspath(os.path.join(_HERE, "..", "invariant_engine")))

import quorum
import provenance

BOARD = {"a": b"ka", "b": b"kb", "c": b"kc"}


# ---- Finding 1 (FIXED): field-delimiter injection ----
def test_no_delimiter_collision_quorum():
    # ('a','b|c') and ('a|b','c') must NOT map to the same subject anymore
    ok(quorum.subject_of("a", "b|c") != quorum.subject_of("a|b", "c"),
       "delimiter injection: two (name,hash) pairs share a subject")
    # a signature over one must not validate the other
    subj1 = quorum.subject_of("a", "b|c")
    sig = quorum.sign_as("a", BOARD["a"], subj1)
    good, _ = quorum.verify_quorum(subj1, [sig], BOARD, 1)
    bad, _ = quorum.verify_quorum(quorum.subject_of("a|b", "c"), [sig], BOARD, 1)
    ok(good and not bad, "signature must bind to exactly one (name,hash)")


def test_no_delimiter_collision_provenance():
    a = provenance._canon("erg", "H", "created", "ROOT")
    b = provenance._canon("erg|H", "created", "ROOT", "x")
    ok(a != b, "provenance signed-message boundaries must be unambiguous")


# ---- Finding 2 (FIXED): rollback / replay without an epoch ----
def test_epoch_blocks_rollback_replay():
    subj_e1 = quorum.subject_of("erg", "H_OLD", 1)
    sigs_e1 = [quorum.sign_as(s, BOARD[s], subj_e1) for s in ("a", "b", "c")]
    # replaying epoch-1 signatures at the current epoch 5 must fail
    replayed, _, _ = quorum.accept_change("erg", "H_OLD", "lowering", sigs_e1, BOARD, epoch=5)
    ok(not replayed, "old-epoch signatures must not be replayable after a rollback")
    # a fresh epoch-5 quorum passes
    subj_e5 = quorum.subject_of("erg", "H_NEW", 5)
    sigs_e5 = [quorum.sign_as(s, BOARD[s], subj_e5) for s in ("a", "b", "c")]
    fresh, _, _ = quorum.accept_change("erg", "H_NEW", "lowering", sigs_e5, BOARD, epoch=5)
    ok(fresh, "a fresh current-epoch quorum must pass")


# ---- normal behaviour still holds ----
def test_quorum_threshold_and_distinct_signers():
    subj = quorum.subject_of("erg", "H")
    one = [quorum.sign_as("a", BOARD["a"], subj)]
    ok(not quorum.accept_change("erg", "H", "lowering", one, BOARD)[0], "1 sig < 3 must fail")
    dup = [quorum.sign_as("a", BOARD["a"], subj)] * 3
    ok(not quorum.accept_change("erg", "H", "lowering", dup, BOARD)[0], "duplicate signer must not count 3x")
    three = [quorum.sign_as(s, BOARD[s], subj) for s in ("a", "b", "c")]
    ok(quorum.accept_change("erg", "H", "lowering", three, BOARD)[0], "3 distinct sigs must pass")
    outsider = [quorum.sign_as("x", b"xkey", subj)]
    ok(not quorum.accept_change("erg", "H", "lowering", one + outsider, BOARD)[0],
       "unauthorised signer must not count")


def test_unknown_role_is_strictest():
    # an unknown role must default to the lowering (3) threshold, not a weak one
    subj = quorum.subject_of("erg", "H")
    one = [quorum.sign_as("a", BOARD["a"], subj)]
    _, thr, _ = quorum.accept_change("erg", "H", "mystery-role", one, BOARD)
    eq(thr, quorum.POLICY["lowering"])


# ---- Finding 3 (KNOWN, Ed25519-deferred): HMAC symmetry ----
def test_hmac_symmetry_is_a_known_limitation():
    # The verifier holds the signing secrets, so it CAN mint any signer's signature.
    # This is inherent to HMAC and is why AD-12 defers to asymmetric Ed25519. We pin
    # the current (symmetric) behaviour so the limitation is explicit, not silent.
    subj = quorum.subject_of("erg", "H")
    forged = quorum.sign_as("a", BOARD["a"], subj)   # a party holding BOARD forges 'a'
    accepted, _ = quorum.verify_quorum(subj, [forged], BOARD, 1)
    ok(accepted, "documents HMAC symmetry: holder of secrets can forge (needs Ed25519)")
