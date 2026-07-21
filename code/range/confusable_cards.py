# -*- coding: utf-8 -*-
"""
Confusable / homoglyph detector card (SIMULATOR of a draft) — the VISIBLE-deception
axis. First card that is NOT about invisibles: the danger here is a character you
CAN see, that looks like a different character.

Law: LOOKS_SAME != IS_SAME. `paypal.com` and `pаypal.com` render alike, but the
second has a Cyrillic `а` (U+0430) among Latin letters — a mixed-script confusable
(the classic IDN / brand spoof). The structural signal is not "a non-Latin letter
exists" (that would flag all Russian) — it is a SINGLE TOKEN that mixes a base
script with lookalike letters of another, OR a wholly-foreign token whose every
letter is a cross-script lookalike (no native anchor).

  ALARM (conclusive):
    - a token mixes Latin with Cyrillic/Greek letters that are Latin CONFUSABLES
      — the foreign letters impersonate Latin (the mix itself is the tell), OR
    - a wholly-foreign token whose Latin SKELETON equals a known TARGET (a
      whole-script brand spoof).
  OK:
    a single-script token, or a genuine native word.

  NOTE (simulated): a blanket "whole-script, no native anchor -> WATCH" rule was
  tested and REJECTED — it fired on ~25% of common Russian words (соус, орех,
  хор ...), which are legitimately built from letters that happen to be Latin
  look-alikes. Whole-script confusion is only meaningful RELATIVE TO A TARGET, so
  it is gated on a target skeleton instead. A real deployment swaps DEMO_TARGETS
  for the Unicode confusables + brand/domain corpus.
"""
import unicodedata as u
from invariant_engine.core import Finding

# lowercase + uppercase Cyrillic letters that are Latin look-alikes
CYR_TO_LAT = {
    0x0430: "a", 0x0435: "e", 0x043E: "o", 0x0440: "p", 0x0441: "c", 0x0443: "y",
    0x0445: "x", 0x0456: "i", 0x0455: "s", 0x0458: "j", 0x04BB: "h", 0x0461: "w",
    0x0410: "A", 0x0412: "B", 0x0415: "E", 0x041A: "K", 0x041C: "M", 0x041D: "H",
    0x041E: "O", 0x0420: "P", 0x0421: "C", 0x0422: "T", 0x0425: "X", 0x0423: "Y",
    0x0406: "I", 0x0408: "J", 0x0405: "S",
}
# Greek letters that are Latin look-alikes
GRK_TO_LAT = {
    0x03BF: "o", 0x03B1: "a", 0x03C1: "p", 0x03BD: "v", 0x03B9: "i", 0x03BA: "k",
    0x03B7: "n", 0x03C5: "u", 0x03C7: "x",
    0x0391: "A", 0x0392: "B", 0x0395: "E", 0x0396: "Z", 0x0397: "H", 0x0399: "I",
    0x039A: "K", 0x039C: "M", 0x039D: "N", 0x039F: "O", 0x03A1: "P", 0x03A4: "T",
    0x03A5: "Y", 0x03A7: "X",
}
OTHER_CONF = {0x2010: "-"}                    # HYPHEN U+2010 confuses with ASCII '-'
CONFUSABLE = {}
CONFUSABLE.update(CYR_TO_LAT)
CONFUSABLE.update(GRK_TO_LAT)
CONFUSABLE.update(OTHER_CONF)

# DEMO target skeletons for the whole-script branch (a real deployment swaps this
# for the Unicode confusables data + a brand/domain corpus). Whole-script fires
# ONLY when a foreign token's Latin skeleton equals one of these — so ordinary
# foreign words never trip it.
DEMO_TARGETS = {"paypal", "google", "apple", "amazon", "microsoft", "yahoo",
                "coinbase", "binance", "outlook", "netflix"}


def _script(ch):
    o = ord(ch)
    if 0x41 <= o <= 0x5A or 0x61 <= o <= 0x7A or 0x00C0 <= o <= 0x024F:
        return "Latin"
    if 0x0400 <= o <= 0x052F:
        return "Cyrillic"
    if 0x0370 <= o <= 0x03FF:
        return "Greek"
    if u.category(ch).startswith("L"):
        return "Other"
    return None


def _letters(tok):
    return [c for c in tok if _script(c) is not None]


def _skeleton(tok):
    return "".join(CONFUSABLE.get(ord(c), c) for c in tok)


def _tokens(text):
    """Maximal runs of letters (+ intra-token '.' '-' '_' for domains)."""
    toks, cur = [], []
    for ch in text:
        if _script(ch) is not None or ch in ".-_":
            cur.append(ch)
        elif cur:
            toks.append("".join(cur)); cur = []
    if cur:
        toks.append("".join(cur))
    return toks


def confusable_cards_reader(text):
    """Confusable authority: ALARM mixed-script or whole-script-on-target / OK."""
    for tok in _tokens(text):
        letters = _letters(tok)
        if len(letters) < 2:
            continue
        scripts = {_script(c) for c in letters}

        # mixed-script confusable: Latin + (Cyrillic/Greek) lookalikes in one token
        if "Latin" in scripts and (scripts & {"Cyrillic", "Greek"}):
            foreign = [c for c in letters if _script(c) in ("Cyrillic", "Greek")]
            if any(ord(c) in CONFUSABLE for c in foreign):
                skel = _skeleton(tok)
                return Finding("suspect", 0.9,
                    f"mixed-script confusable token '{tok}' impersonates '{skel}' "
                    f"(Latin + {'/'.join(sorted(scripts & {'Cyrillic','Greek'}))} "
                    f"look-alikes)", conclusive=True, signature="mixed_script_confusable")

        # whole-script spoof: all-foreign token whose skeleton equals a TARGET
        if (scripts <= {"Cyrillic"} or scripts <= {"Greek"}) and letters:
            if all(ord(c) in CONFUSABLE for c in letters):
                skel = _skeleton(tok).strip(".-_").lower()
                if skel in DEMO_TARGETS:
                    return Finding("suspect", 0.85,
                        f"whole-script confusable token '{tok}' impersonates target "
                        f"'{skel}'", conclusive=True, signature="whole_script_confusable")

    return Finding("clean", 0.0, "confusable-cards: no mixed/whole-script confusables")
