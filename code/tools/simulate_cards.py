# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
Card simulator (phase 2) — run each per-sign card's RISK/SAFE cases through the
live Vakhter detection prototypes and see which fire.

The structural validator (validate_per_sign.py) checks a card is well-FORMED.
This simulator checks a card's example cases against live CODE:
  - RISK_CASES  should be CAUGHT   (risk != OK) by some prototype
  - SAFE_CASES  should stay CLEAN  (risk == OK)

Not every sign has a dedicated prototype yet (many are delegated to the
integrator per the cards' own OPEN_QUESTIONS). The simulator is honest about
that: a card whose RISK cases are not caught by any current prototype is
reported as SPEC_ONLY (pending integrator) rather than silently "passing".

Detection stack used: canonicalize -> confusable + urlpunct + metachar +
invisible + digit cards (the visible/structural readers relevant to PH).

Usage:  MSL_MIP_HOME=/path/to/msl_mip  python code/tools/simulate_cards.py
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RANGE = os.path.abspath(os.path.join(HERE, "..", "range"))
CARDS = os.path.abspath(os.path.join(HERE, "..", "..", "sign_cards", "per_sign"))
for _cand in ("canon", "canonicalization"):
    _p = os.path.abspath(os.path.join(HERE, "..", _cand))
    if os.path.isdir(_p):
        sys.path.insert(0, _p); break
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "invariant_engine")))
sys.path.insert(0, RANGE)

from canonicalize import canonicalize
from invariant_engine.core import judge
from invariant_engine.supplement import combine
from confusable_cards import confusable_cards_reader
from urlpunct_cards import urlpunct_cards_reader
from metachar_cards import metachar_cards_reader
from invisible_cards import invisible_cards_reader
from digit_cards import digit_cards_reader

READERS = [confusable_cards_reader, urlpunct_cards_reader, metachar_cards_reader,
           invisible_cards_reader, digit_cards_reader]


def verdict(text):
    """Combined risk across the visible/structural stack."""
    c = canonicalize(text)[0]
    f = confusable_cards_reader(c)
    for r in READERS[1:]:
        f = combine(f, r(c))
    return judge(f, 0.0).risk


def _extract_input(line):
    """Pull the test payload from an `INPUT: ...` line."""
    m = re.search(r'INPUT:\s*"([^"]+)"', line)
    if m:
        return m.group(1)
    m = re.search(r"INPUT:\s*(.+)", line)
    if not m:
        return None
    val = m.group(1).strip()
    val = re.split(r"\s+\(", val)[0]          # drop trailing parenthetical
    return val.strip().strip('"')


def cases(text, kind):
    """Yield INPUT payloads under RISK_CASE_/SAFE_CASE_ blocks."""
    out = []
    cur = None
    for line in text.splitlines():
        if re.search(rf"{kind}_CASE_\d+:", line):
            cur = True
        elif cur and "INPUT:" in line:
            v = _extract_input(line)
            if v:
                out.append(v)
            cur = None
    return out


def codepoint(text):
    m = re.search(r"^CODEPOINT:\s*(U\+[0-9A-Fa-f]+)", text, re.M)
    return m.group(1) if m else "?"


def main():
    files = sorted(f for f in os.listdir(CARDS) if f.endswith("_RU.md"))
    print("CARD SIMULATOR — RISK caught / SAFE clean, against live prototypes")
    print("=" * 74)
    proto_backed = spec_only = 0
    for f in files:
        text = open(os.path.join(CARDS, f), encoding="utf-8").read()
        cp = codepoint(text)
        name = f.replace("SIGN_CORE_CARD_", "").replace("_GEN3_v0_3_RU.md", "")
        risk = cases(text, "RISK")
        safe = cases(text, "SAFE")
        caught = sum(1 for t in risk if verdict(t) != "OK")
        clean = sum(1 for t in safe if verdict(t) == "OK")
        backed = caught > 0
        if backed:
            proto_backed += 1
        else:
            spec_only += 1
        tag = "PROTO" if backed else "SPEC_ONLY (pending integrator)"
        print(f"{cp:>8} {name:24} RISK caught {caught}/{len(risk)} · "
              f"SAFE clean {clean}/{len(safe)}   [{tag}]")

    print("=" * 74)
    print(f"{proto_backed} prototype-backed · {spec_only} spec-only (delegated to integrator) "
          f"· {proto_backed+spec_only} signs")
    print("Note: SAFE clean should stay high; SPEC_ONLY = no live detector yet, "
          "not a card defect (see each card's OPEN_QUESTIONS).")


if __name__ == "__main__":
    main()
