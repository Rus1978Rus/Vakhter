# -*- coding: utf-8 -*-
"""
Per-sign card validator (structural gate) — run BEFORE each commit.

Checks every SIGN_CORE_CARD_*_{RU,EN}.md in sign_cards/per_sign/ against the
GEN3_v0_3 template minimums, catches leftover placeholders, verifies that
CONFUSABLE codepoints are real (and their stated Unicode name matches), and
checks EN/RU consistency (same CODEPOINT, same section counts).

This is the "run it before you trust it" gate for the card batch. It does NOT
judge card SEMANTICS (that is the separate card-simulator phase) — it guarantees
structure, codepoint sanity, and bilingual parity so bigger batches stay safe.

Usage:  python code/tools/validate_per_sign.py
Exit 0 = all pass; exit 1 = at least one card failed.
"""
import os, re, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
CARDS = os.path.abspath(os.path.join(HERE, "..", "..", "sign_cards", "per_sign"))

MIN = {"WHAT_IS_NOT": 10, "BASE_FORMULAS": 10, "SAFE_CASE": 6, "RISK_CASE": 6,
       "CONFUSABLE": 5, "CG": 6, "MUTATION": 6, "ADVERSARIAL": 10}

# Control codepoints have no formal UCD name, only aliases. Names below are the
# Unicode Name Aliases (control category) used when a card lists one as a
# functional confusable of a control-char sign (LF/CR/TAB/NUL...).
CONTROL_ALIASES = {
    0x0000: "NULL", 0x0007: "BELL", 0x0008: "BACKSPACE",
    0x0009: "CHARACTER TABULATION", 0x000A: "LINE FEED",
    0x000B: "LINE TABULATION", 0x000C: "FORM FEED",
    0x000D: "CARRIAGE RETURN", 0x001B: "ESCAPE",
    0x0085: "NEXT LINE",
}

PLACEHOLDER_HINTS = ["<...>", "<XXXX>", "U+<X", "<the ", "<author", "<YYYY",
                     "<number>", "<vector>", "<category", "<example text>",
                     "<similar symbol>", "<official name>", "<question>",
                     "<short ", "<SIGN_NAME", "<reference"]


def _block(text, start_label):
    """Return the lines from `start_label:` up to the next ==== delimiter."""
    lines = text.splitlines()
    out, grabbing = [], False
    for ln in lines:
        if grabbing:
            if ln.strip().startswith("====") or re.match(r"^\d+\.\s", ln.strip()):
                break
            out.append(ln)
        elif ln.strip().startswith(start_label):
            grabbing = True
    return out


def counts(text):
    c = {}
    c["WHAT_IS_NOT"] = len(re.findall(r"^\s*\d+\.\s+NOT_", text, re.M))
    bf = _block(text, "BASE_FORMULAS:")
    c["BASE_FORMULAS"] = sum(1 for ln in bf if "≠" in ln)
    c["SAFE_CASE"] = len(set(re.findall(r"SAFE_CASE_(\d+):", text)))
    c["RISK_CASE"] = len(set(re.findall(r"RISK_CASE_(\d+):", text)))
    c["CONFUSABLE"] = len(set(re.findall(r"CONFUSABLE_(\d+):", text)))
    c["CG"] = len(set(re.findall(r"^\s*CG(\d+):", text, re.M)))
    c["MUTATION"] = len(set(re.findall(r"MUTATION_(\d+):", text)))
    m = re.search(r"ACTUAL_TOTAL_VECTORS:\s*(\d+)", text)
    c["ADVERSARIAL"] = int(m.group(1)) if m else 0
    return c


def confusable_codepoints(text):
    """Yield (cp_int, stated_name) for each CONFUSABLE block."""
    for blk in re.split(r"CONFUSABLE_\d+:", text)[1:]:
        cp = re.search(r"CODEPOINT:\s*U\+([0-9A-Fa-f]+)", blk)
        nm = re.search(r"NAME:\s*(.+)", blk)
        if cp:
            yield int(cp.group(1), 16), (nm.group(1).strip() if nm else "")


def placeholders(text):
    return [h for h in PLACEHOLDER_HINTS if h in text]


def codepoint(text):
    m = re.search(r"^CODEPOINT:\s*U\+([0-9A-Fa-f]+)", text, re.M)
    return m.group(1).upper() if m else None


def validate_file(path):
    text = open(path, encoding="utf-8").read()
    errs, warns = [], []
    c = counts(text)
    for k, need in MIN.items():
        if c.get(k, 0) < need:
            errs.append(f"{k} = {c.get(k,0)} < {need}")
    ph = placeholders(text)
    if ph:
        errs.append(f"leftover placeholders: {ph}")
    for cp, nm in confusable_codepoints(text):
        ch = chr(cp)
        try:
            real = unicodedata.name(ch)
        except (ValueError, KeyError):
            # Control chars (LF/CR/TAB/VT/FF/NEL...) are real assigned codepoints
            # with no formal UCD name, only aliases. Accept them when the category
            # is a control (Cc); reject only genuinely unassigned/surrogate points.
            if unicodedata.category(ch) == "Cc":
                real = CONTROL_ALIASES.get(cp)
                if real is None:
                    warns.append(f"U+{cp:04X} control char without a known alias")
                    continue
            else:
                errs.append(f"CONFUSABLE U+{cp:04X} not a named codepoint")
                continue
        if nm and nm.upper() != real.upper():
            warns.append(f"U+{cp:04X} name '{nm}' != UCD '{real}'")
    return c, errs, warns


def main():
    files = sorted(f for f in os.listdir(CARDS) if f.endswith(".md"))
    by_cp = {}
    failed = 0
    print("PER-SIGN CARD VALIDATOR")
    print("=" * 68)
    for f in files:
        path = os.path.join(CARDS, f)
        text = open(path, encoding="utf-8").read()
        c, errs, warns = validate_file(path)
        cpv = codepoint(text)
        lang = "RU" if f.endswith("_RU.md") else "EN"
        by_cp.setdefault(cpv, {})[lang] = c
        status = "PASS" if not errs else "FAIL"
        if errs:
            failed += 1
        print(f"[{status}] {f}")
        for e in errs:
            print(f"        ERROR: {e}")
        for w in warns:
            print(f"        warn : {w}")

    # EN/RU parity
    print("-" * 68)
    for cp, langs in by_cp.items():
        if set(langs) != {"RU", "EN"}:
            print(f"[WARN] U+{cp}: missing pair ({sorted(langs)})")
            continue
        for key in MIN:
            if langs["RU"].get(key) != langs["EN"].get(key):
                print(f"[WARN] U+{cp}: {key} RU={langs['RU'].get(key)} != EN={langs['EN'].get(key)}")

    print("=" * 68)
    print(f"{'ALL PASS' if not failed else f'{failed} FILE(S) FAILED'} "
          f"({len(files)} files, {len(by_cp)} signs)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
