# -*- coding: utf-8 -*-
"""
Transparency-log audit, made permanent (transparency.py).

Two weaknesses found and fixed, plus the honest hash-chain limits pinned:
  Finding 1 (FIXED)  delimiter injection in the committed (when|event) fields.
  Finding 2 (FIXED)  truncation / full-rewrite invisible to verify_chain — now
                     caught when the caller pins a previously-anchored head.
  Limit (DOCUMENTED) without an anchor a bare chain proves only internal
                     consistency; a truncated prefix or a from-genesis rewrite is
                     self-consistent. Pinned so the boundary is explicit.
"""
import os
import sys

from _support import ok, eq

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "range")))
import transparency as T


def _log(*events):
    log = T.new_log()
    for e in events:
        T.append(log, e, "2026")
    return log


# ---- Finding 1 (FIXED): delimiter injection ----
def test_no_delimiter_collision():
    a = T.append(T.new_log(), event="b|c", when="a")
    b = T.append(T.new_log(), event="c", when="a|b")
    ok(a["hash"] != b["hash"],
       "(when,event) boundaries must be unambiguous in the commitment")


# ---- Finding 2 (FIXED): truncation / rewrite caught by an anchor ----
def test_truncation_caught_with_anchor():
    log = _log("created", "reviewed", "APPROVED", "SIGNED erg")
    anchor = T.head(log)
    ok(T.verify_chain(log, expected_head=anchor)[0], "full log must verify against its head")
    truncated = log[:-1]
    ok(not T.verify_chain(truncated, expected_head=anchor)[0],
       "dropping the last entry must be caught against the anchor")


def test_full_rewrite_caught_with_anchor():
    log = _log("created", "SIGNED erg")
    anchor = T.head(log)
    forged = _log("created", "SIGNED backdoor")   # attacker rebuilds a clean chain
    ok(not T.verify_chain(forged, expected_head=anchor)[0],
       "a from-genesis rewrite must not match the original anchor")


# ---- honest limit: without an anchor, a bare chain is only internally consistent ----
def test_truncation_without_anchor_is_consistent():
    log = _log("created", "reviewed", "SIGNED erg")
    ok(T.verify_chain(log[:-1])[0],
       "documents the limit: a truncated prefix is self-consistent without an anchor")


# ---- internal tamper still caught with no anchor ----
def test_internal_tamper_caught():
    log = _log("created", "reviewed", "SIGNED erg")
    ok(T.verify_chain(log)[0], "clean log verifies")
    log[2]["event"] = "TAMPERED"
    okc, bad = T.verify_chain(log)
    ok(not okc, "altered entry must break the chain")
    eq(bad, 2)


def test_reorder_and_seq_gap_caught():
    log = _log("a", "b", "c")
    log[1], log[2] = log[2], log[1]        # reorder
    ok(not T.verify_chain(log)[0], "reordering must break the chain")
    log2 = _log("a", "b", "c")
    del log2[2]                             # remove an interior entry -> seq gap / prev break
    ok(not T.verify_chain(log2)[0], "interior removal must be caught")
