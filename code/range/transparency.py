# -*- coding: utf-8 -*-
"""
APPEND-ONLY TRANSPARENCY LOG — every sign-off is public and tamper-evident.

A hash-chained log (like Certificate Transparency): each entry commits to the
previous one, so a past entry cannot be altered or removed without breaking the
chain from that point on. Signing a component in secret becomes impossible: the
event is on the record, and any attempt to erase it is detectable.

Time is passed in by the caller (a stamped date string) so the log is
deterministic and reproducible; the chain integrity does not depend on it.
"""
import hashlib


def _h(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def new_log():
    g = {"seq": 0, "when": "genesis", "event": "GENESIS", "prev": "0" * 64}
    g["hash"] = _h(f"0|genesis|GENESIS|{g['prev']}")
    return [g]


def append(log, event, when=""):
    prev = log[-1]
    seq = prev["seq"] + 1
    entry = {"seq": seq, "when": when, "event": event, "prev": prev["hash"]}
    entry["hash"] = _h(f"{seq}|{when}|{event}|{entry['prev']}")
    log.append(entry)
    return entry


def verify_chain(log):
    """Return (ok, first_bad_seq). Detects altered / removed / inserted entries."""
    for i, e in enumerate(log):
        recomputed = _h(f"{e['seq']}|{e['when']}|{e['event']}|{e['prev']}")
        if e["hash"] != recomputed:
            return False, e["seq"]
        if i > 0 and e["prev"] != log[i - 1]["hash"]:
            return False, e["seq"]
    return True, None
