#!/usr/bin/env python3
"""
coverage_lock.py — regression lock for the homoglyph front.

Keeps the two independent sources of truth in sync WITHOUT a generator:

  1. the live detector's confusable tables in code/range/confusable_cards.py
     (CYR_TO_LAT / GRK_TO_LAT / ROMAN_TO_LAT) — the codepoints it actually flags;
  2. the per-sign draft cards in sign_cards/per_sign/*.md — the authored spec.

It asserts both directions so the manual "card <-> detector" contract cannot
drift silently:

  A. COMPLETENESS   — every detector homoglyph codepoint has a full EN+RU card.
  B. BACKING        — every homoglyph-family card (GREEK_/CYRILLIC_/ROMAN_ in its
                      filename) names a codepoint the detector actually backs, so
                      no such card can claim PROTO the detector cannot deliver.

Exit code 0 = locked/in sync; 1 = drift (prints exactly what diverged).

Usage:  python code/tools/coverage_lock.py
"""
import os
import re
import glob
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DETECTOR = os.path.abspath(os.path.join(HERE, "..", "range", "confusable_cards.py"))
CARDS = os.path.abspath(os.path.join(HERE, "..", "..", "sign_cards", "per_sign"))

# families whose cards MUST be backed by the detector (i.e. must be PROTO-capable)
HOMOGLYPH_FAMILIES = ("GREEK_", "CYRILLIC_", "ROMAN_", "ARMENIAN_")


def detector_codepoints():
    """Union of the per-letter homoglyph lookup tables in the live detector.
    (Cherokee is intentionally excluded — it is detected by a script-mix rule with
    NO per-letter table, so it has no per-sign cards; see AD-26.)"""
    src = open(DETECTOR, encoding="utf-8").read()
    cps = set()
    for name in ("CYR_TO_LAT", "GRK_TO_LAT", "ROMAN_TO_LAT", "ARM_TO_LAT"):
        m = re.search(name + r"\s*=\s*\{(.*?)\}", src, re.S)
        if not m:
            raise SystemExit(f"coverage_lock: table {name} not found in detector")
        cps |= {int(x, 16) for x in re.findall(r"0x([0-9A-Fa-f]+)\s*:", m.group(1))}
    return cps


def card_index():
    """codepoint -> {'EN','RU'} langs present, and codepoint -> a homoglyph filename stem."""
    langs = {}
    homoglyph_files = {}   # cp -> filename (for a homoglyph-family card)
    for path in glob.glob(os.path.join(CARDS, "*.md")):
        text = open(path, encoding="utf-8").read()
        m = re.search(r"^CODEPOINT:\s*U\+([0-9A-Fa-f]+)", text, re.M)
        if not m:
            continue
        cp = int(m.group(1), 16)
        base = os.path.basename(path)
        lang = "RU" if base.endswith("_RU.md") else "EN"
        langs.setdefault(cp, set()).add(lang)
        if any(fam in base for fam in HOMOGLYPH_FAMILIES):
            homoglyph_files[cp] = base
    return langs, homoglyph_files


def main():
    det = detector_codepoints()
    langs, homoglyph_files = card_index()
    full_pairs = {cp for cp, ls in langs.items() if ls == {"EN", "RU"}}

    # A. completeness: detector codepoint must have a full EN+RU card
    missing = sorted(det - full_pairs)
    # B. backing: homoglyph-family card codepoint must be in the detector table
    unbacked = sorted(cp for cp in homoglyph_files if cp not in det)

    print("COVERAGE LOCK — homoglyph front (card <-> detector)")
    print("-" * 60)
    print(f"detector homoglyph codepoints : {len(det)}")
    print(f"full EN+RU card pairs         : {len(full_pairs)}")
    print(f"homoglyph-family cards        : {len(homoglyph_files)}")
    print("-" * 60)

    ok = True
    if missing:
        ok = False
        print("A. FAIL — detector codepoints with no full EN+RU card:")
        for cp in missing:
            langs_have = "".join(sorted(langs.get(cp, set()))) or "none"
            print(f"     U+{cp:04X}  (have: {langs_have})")
    else:
        print("A. PASS — every detector codepoint has a full EN+RU card.")

    if unbacked:
        ok = False
        print("B. FAIL — homoglyph-family cards not backed by the detector "
              "(cannot be PROTO):")
        for cp in unbacked:
            print(f"     U+{cp:04X}  {homoglyph_files[cp]}")
    else:
        print("B. PASS — every homoglyph-family card is backed by the detector.")

    print("-" * 60)
    if ok:
        print(f"LOCKED — {len(det)} homoglyph forms in sync (card <-> detector).")
        return 0
    print("DRIFT — card/detector contract broken (see above).")
    return 1


if __name__ == "__main__":
    sys.exit(main())
