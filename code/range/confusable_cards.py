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
    0x043A: "k",
    0x0410: "A", 0x0412: "B", 0x0415: "E", 0x041A: "K", 0x041C: "M", 0x041D: "H",
    0x041E: "O", 0x0420: "P", 0x0421: "C", 0x0422: "T", 0x0425: "X", 0x0423: "Y",
    0x0406: "I", 0x0408: "J", 0x0405: "S",
    0x051B: "q", 0x0501: "d", 0x051D: "w", 0x0475: "v",
    0x051A: "Q", 0x0500: "D", 0x051C: "W", 0x0474: "V",
}
# Greek letters that are Latin look-alikes
GRK_TO_LAT = {
    0x03BF: "o", 0x03B1: "a", 0x03C1: "p", 0x03BD: "v", 0x03B9: "i", 0x03BA: "k",
    0x03B7: "n", 0x03C5: "u", 0x03C7: "x", 0x03F2: "c",
    0x0391: "A", 0x0392: "B", 0x0395: "E", 0x0396: "Z", 0x0397: "H", 0x0399: "I",
    0x039A: "K", 0x039C: "M", 0x039D: "N", 0x039F: "O", 0x03A1: "P", 0x03A4: "T",
    0x03A5: "Y", 0x03A7: "X", 0x03F9: "C", 0x03F3: "j",
}
# Roman-numeral LETTER FORMS that look like Latin letters (Number Forms block).
# Mixed INTO an ASCII-Latin word they are a spoof (ⅼ in paypaⅼ); standalone
# Roman numerals (Ⅻ, "ⅰ ⅴ ⅹ ⅼ") are their own tokens and never trip this.
ROMAN_TO_LAT = {0x2170: "i", 0x2174: "v", 0x2179: "x", 0x217C: "l", 0x217D: "c",
                0x217E: "d", 0x217F: "m",
                0x2160: "I", 0x2164: "V", 0x2169: "X", 0x216C: "L", 0x216D: "C",
                0x216E: "D", 0x216F: "M"}
# Non-ASCII dashes that confuse with the ASCII hyphen. Legit in prose typography
# (well‐known) — flagged ONLY inside a domain-ish token (one containing a dot).
NASCII_DASH = {0x2010: "-", 0x2011: "-", 0x2012: "-", 0x2013: "-", 0x2014: "-",
               0x2015: "-", 0x2212: "-", 0xFF0D: "-"}
OTHER_CONF = {}
CONFUSABLE = {}
CONFUSABLE.update(CYR_TO_LAT)
CONFUSABLE.update(GRK_TO_LAT)
CONFUSABLE.update(ROMAN_TO_LAT)
CONFUSABLE.update(NASCII_DASH)
CONFUSABLE.update(OTHER_CONF)

# Target skeletons for the whole-script branch: fires ONLY when a foreign token's
# Latin skeleton equals one of these, so ordinary foreign words never trip it. The
# list is the shared brand corpus (frequency-ordered, len>=5 for FP-safety) — one
# source of truth with the digit-leet detector (see brand_corpus.py / AD-13).
from brand_corpus import WHOLE_SCRIPT_TARGETS as DEMO_TARGETS


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


def _tokish(ch):
    return (_script(ch) is not None or ch in ".-_"
            or ord(ch) in ROMAN_TO_LAT or ord(ch) in NASCII_DASH)


def _tokens(text):
    """Maximal runs of letters (+ intra-token '.' '-' '_', roman-numeral
    letter-forms and non-ASCII dashes — so paypaⅼ.com / pay‐pal.com are tokens)."""
    toks, cur = [], []
    for ch in text:
        if _tokish(ch):
            cur.append(ch)
        elif cur:
            toks.append("".join(cur)); cur = []
    if cur:
        toks.append("".join(cur))
    return toks


def _ascii_latin(ch):
    o = ord(ch)
    return (0x41 <= o <= 0x5A) or (0x61 <= o <= 0x7A)


def confusable_cards_reader(text):
    """Confusable authority: ALARM mixed-script or whole-script-on-target / OK."""
    for tok in _tokens(text):
        letters = _letters(tok)
        scripts = {_script(c) for c in letters}
        has_ascii_latin = any(_ascii_latin(c) for c in tok)

        # roman-numeral letter-form mixed INTO an ASCII-Latin word (paypaⅼ, ⅬG, iⅼlegal).
        # Evaluated BEFORE the >=2-letter gate below: a roman-numeral FORM is category Nl
        # and is NOT counted by _letters(), so a single ASCII letter + a roman form (e.g.
        # "ⅬG" for LG) would otherwise be skipped. A standalone numeral ("Ⅹ", "ⅩVⅠ") has
        # no ASCII letter, so has_ascii_latin is False there and this never fires on it.
        roman = [c for c in tok if ord(c) in ROMAN_TO_LAT]
        if has_ascii_latin and roman:
            skel = _skeleton(tok)
            return Finding("suspect", 0.85,
                f"confusable token '{tok}' impersonates '{skel}' "
                f"(Roman-numeral letter-form among Latin letters)",
                conclusive=True, signature="mixed_script_confusable")

        # non-ASCII dash in a DOMAIN-ish token (has a dot) — pay‐pal.com, not well‐known.
        # Also gate-independent for the same reason (a dash is not a letter).
        dash = [c for c in tok if ord(c) in NASCII_DASH]
        if has_ascii_latin and dash and "." in tok:
            skel = _skeleton(tok)
            return Finding("suspect", 0.85,
                f"confusable token '{tok}' impersonates '{skel}' "
                f"(non-ASCII dash in a domain-like token)",
                conclusive=True, signature="mixed_script_confusable")

        # the remaining checks compare script letters, so they need >=2 of them
        if len(letters) < 2:
            continue

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
