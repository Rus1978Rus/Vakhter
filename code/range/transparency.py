# -*- coding: utf-8 -*-
"""
APPEND-ONLY TRANSPARENCY LOG — every sign-off is public and tamper-evident.

A hash-chained log (like Certificate Transparency): each entry commits to the
previous one, so a past entry cannot be altered, removed, or reordered without
breaking the chain from that point on. Signing a component in secret becomes
impossible: the event is on the record, and any attempt to edit it is detectable.

Time is passed in by the caller (a stamped date string) so the log is
deterministic and reproducible; chain integrity does not depend on it.

HONEST LIMITS (audit AD-30) — a bare hash chain proves internal consistency, not
authenticity of the WHOLE log:
  * TRUNCATION / ROLLBACK: dropping entries from the END leaves a still-consistent
    prefix. Detected ONLY against an external anchor — pass the head you last saw
    as `expected_head` to verify_chain (that is what a CT auditor / gossip does).
  * FULL REWRITE: an adversary who controls the whole log can rebuild it from
    genesis with fresh hashes and it verifies. Same defence: an externally
    anchored `expected_head`, or (future) a SIGNED tree head. This module chains
    but does not sign — signing is provenance/quorum's job (and is HMAC there, see
    AD-12/AD-28).
verify_chain(log) alone answers "is this log internally consistent?"; with
`expected_head` it also answers "is it the same log I anchored, un-truncated?".
"""
import hashlib


def _h(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def _canon(*parts):
    """Length-prefixed field encoding so a '|' inside `when`/`event` cannot shift
    the committed boundaries — otherwise (when='a', event='b|c') and
    (when='a|b', event='c') would hash identically (audit AD-30, same class as the
    provenance/quorum delimiter fix in AD-28)."""
    return "\x1e".join(f"{len(p)}:{p}" for p in (str(x) for x in parts))


def _entry_hash(seq, when, event, prev):
    return _h(_canon(seq, when, event, prev))


GENESIS_PREV = "0" * 64


def new_log():
    g = {"seq": 0, "when": "genesis", "event": "GENESIS", "prev": GENESIS_PREV}
    g["hash"] = _entry_hash(0, "genesis", "GENESIS", GENESIS_PREV)
    return [g]


def append(log, event, when=""):
    prev = log[-1]
    seq = prev["seq"] + 1
    entry = {"seq": seq, "when": when, "event": event, "prev": prev["hash"]}
    entry["hash"] = _entry_hash(seq, when, event, entry["prev"])
    log.append(entry)
    return entry


def head(log):
    """The current head hash — the value a caller ANCHORS externally so a later
    verify_chain(log, expected_head=...) can detect truncation / full rewrite."""
    return log[-1]["hash"] if log else GENESIS_PREV


def verify_chain(log, expected_head=None):
    """Return (ok, first_bad_seq). Detects altered / removed / inserted / reordered
    entries. If `expected_head` is given, ALSO detects truncation and full rewrite
    by pinning the log to a previously-anchored head (returns the head entry's seq,
    or -1 if the log is unexpectedly empty, when the anchor does not match)."""
    if not log:
        return (expected_head in (None, GENESIS_PREV)), -1
    # genesis must be structurally a genesis (prev = all-zero, seq 0)
    if log[0]["seq"] != 0 or log[0]["prev"] != GENESIS_PREV:
        return False, log[0].get("seq", -1)
    for i, e in enumerate(log):
        recomputed = _entry_hash(e["seq"], e["when"], e["event"], e["prev"])
        if e["hash"] != recomputed:
            return False, e["seq"]
        if i > 0:
            if e["prev"] != log[i - 1]["hash"]:
                return False, e["seq"]
            if e["seq"] != log[i - 1]["seq"] + 1:          # seq must be contiguous
                return False, e["seq"]
    if expected_head is not None and log[-1]["hash"] != expected_head:
        return False, log[-1]["seq"]                       # truncated / rewritten
    return True, None
