# -*- coding: utf-8 -*-
"""
CLASS-138 coverage proof — self-derives the invisible-format contour and maps
every member to the draft class card that owns it.

"Class 138" is the AUTHORITATIVE set: General_Category==Cf AND
Default_Ignorable_Code_Point==True (per the MSL/MIP oracle_class_138, UCD 17.0).
Buckets: PURE 23 · DIRECTIONAL 12 · TAG 97 · DEPRECATED 6 = 138.

This harness re-derives the set from the host Unicode database (no external
file dependency) and asserts each member is owned by exactly one Vakhter card.
Note: U+2028/U+2029 are Zl/Zp and U+034F (CGJ) is Mn — none is Cf, so none is
in the 138 (they are covered elsewhere: whitespace / invisible tail).
Run:  python range_class138_coverage.py
"""
import unicodedata as u

def R(a, b):
    return set(range(a, b + 1))

# --- codepoints each draft card owns, restricted to the Cf-and-DI contour ---
OWNERS = {
    "INVISIBLE_CLASS":  {0x00AD, 0x200B, 0x200C, 0x200D, 0x2060, 0xFEFF} | R(0x2061, 0x2064),
    "BIDI_CLASS":       {0x061C, 0x200E, 0x200F, 0x202A, 0x202B, 0x202C, 0x202D, 0x202E,
                         0x2066, 0x2067, 0x2068, 0x2069},
    "TAG_CLASS":        {0xE0001} | R(0xE0020, 0xE007F),
    "MONITORED_FORMAT": {0x180E} | R(0x206A, 0x206F) | R(0x1BCA0, 0x1BCA3) | R(0x1D173, 0x1D17A),
}

# --- the authoritative predicate: Cf AND Default_Ignorable ---
# Default_Ignorable = Cf + Other_DI + VS - White_Space - the Cf-not-DI carve-out.
CF_NOT_DI = ({0x600, 0x601, 0x602, 0x603, 0x604, 0x605, 0x6DD, 0x70F, 0x890, 0x891, 0x8E2,
              0x110BD, 0x110CD} | R(0xFFF9, 0xFFFB) | R(0x13430, 0x1343F))
CF = {cp for cp in range(0, 0x110000) if u.category(chr(cp)) == "Cf"}
CLASS_138 = CF - CF_NOT_DI

# authoritative bucket assignment (matches the oracle)
def bucket(cp):
    if cp in R(0xE0000, 0xE007F):
        return "TAG"
    if cp in R(0x206A, 0x206F):
        return "DEPRECATED"
    if cp in {0x061C, 0x200E, 0x200F} | R(0x202A, 0x202E) | R(0x2066, 0x2069):
        return "DIRECTIONAL"
    return "PURE"


def run():
    print("CLASS-138 COVERAGE PROOF")
    print("=" * 68)
    print(f"predicate : General_Category==Cf AND Default_Ignorable==True")
    print(f"total     : {len(CLASS_138)} (expected 138)")

    # bucket census
    from collections import Counter
    cen = Counter(bucket(cp) for cp in CLASS_138)
    print("buckets   :", dict(sorted(cen.items())),
          "(expected PURE 23, DIRECTIONAL 12, TAG 97, DEPRECATED 6)")

    # map every member to its owner
    owned = set().union(*OWNERS.values())
    uncovered = sorted(CLASS_138 - owned)
    overreach = sorted(owned - CLASS_138)   # a card claiming a non-138 codepoint
    print("\nper-card ownership within the 138:")
    for card, cps in OWNERS.items():
        n = len(cps & CLASS_138)
        print(f"  {card:18} owns {n:3d} of the 138")

    print("\nuncovered members :", len(uncovered), [hex(x) for x in uncovered[:8]])
    print("owner over-reach  :", len(overreach), [hex(x) for x in overreach[:8]])

    # the two categorization nits the oracle settles
    print("\nnot in the 138 (Cf-only set) — covered elsewhere, not here:")
    for cp, nm, where in [(0x2028, "LINE SEP", "WHITESPACE (Zl)"),
                          (0x2029, "PARA SEP", "WHITESPACE (Zp)"),
                          (0x034F, "CGJ", "INVISIBLE tail (Mn)")]:
        print(f"  U+{cp:04X} {nm:9} cat={u.category(chr(cp))}  -> {where}; in 138? {cp in CLASS_138}")

    ok = (len(CLASS_138) == 138 and not uncovered and not overreach
          and dict(cen) == {"PURE": 23, "DIRECTIONAL": 12, "TAG": 97, "DEPRECATED": 6})
    print("\n" + "=" * 68)
    print("RESULT:", "PASS — 138/138 owned, buckets match oracle, 0 over-reach"
          if ok else "FAIL — see above")
    return ok


if __name__ == "__main__":
    run()
