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
# Non-ASCII dots that confuse with the ASCII full stop '.' — used to spoof a
# domain separator (paypal․com). Legit as a CJK/Arabic full stop in native text,
# so flagged ONLY between two ASCII-Latin letters (the domain-separator tell).
# (Fullwidth full stop U+FF0E is peeled upstream by the canonicalization fold.)
NASCII_DOT = {0x2024: ".", 0x3002: ".", 0xFF61: ".", 0x06D4: ".", 0x0701: "."}
# Non-ASCII slashes that confuse with '/'. (Fullwidth solidus U+FF0F is folded
# upstream.) Same domain-separator gate as the dots.
NASCII_SLASH = {0x2044: "/", 0x2215: "/", 0x29F8: "/"}
# Armenian letters that are Latin look-alikes (UTS #39). Conservative set — only
# the well-established confusables — so single-script Armenian text stays clean and
# only a Latin+Armenian MIX (or a whole-Armenian brand skeleton) is flagged.
ARM_TO_LAT = {0x0585: "o", 0x0578: "n", 0x057D: "u", 0x0561: "a", 0x0555: "O"}
OTHER_CONF = {}
CONFUSABLE = {}
CONFUSABLE.update(CYR_TO_LAT)
CONFUSABLE.update(GRK_TO_LAT)
CONFUSABLE.update(ROMAN_TO_LAT)
CONFUSABLE.update(NASCII_DASH)
CONFUSABLE.update(NASCII_DOT)
CONFUSABLE.update(NASCII_SLASH)
CONFUSABLE.update(ARM_TO_LAT)
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
    if 0x0531 <= o <= 0x058F:
        return "Armenian"
    if 0x13A0 <= o <= 0x13FF or 0xAB70 <= o <= 0xABBF:
        return "Cherokee"
    if u.category(ch).startswith("L"):
        return "Other"
    return None


def _letters(tok):
    return [c for c in tok if _script(c) is not None]


def _skeleton(tok):
    return "".join(CONFUSABLE.get(ord(c), c) for c in tok)


def _tokish(ch):
    return (_script(ch) is not None or ch in ".-_"
            or ord(ch) in ROMAN_TO_LAT or ord(ch) in NASCII_DASH
            or ord(ch) in NASCII_DOT or ord(ch) in NASCII_SLASH)


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

        # non-ASCII dot/slash used as a DOMAIN SEPARATOR (paypal․com, micro∕soft).
        # Flagged ONLY when the confusable sits BETWEEN two ASCII-Latin letters —
        # so a CJK sentence-final 。 (preceded by CJK, not by an ASCII letter) never
        # trips it. Gate-independent for the same reason as dash (not a letter).
        for i, c in enumerate(tok):
            if ord(c) in NASCII_DOT or ord(c) in NASCII_SLASH:
                prev = tok[i - 1] if i > 0 else ""
                nxt = tok[i + 1] if i + 1 < len(tok) else ""
                if prev and nxt and _ascii_latin(prev) and _ascii_latin(nxt):
                    skel = _skeleton(tok)
                    kind = "dot" if ord(c) in NASCII_DOT else "slash"
                    return Finding("suspect", 0.85,
                        f"confusable token '{tok}' impersonates '{skel}' "
                        f"(non-ASCII {kind} as a domain separator)",
                        conclusive=True, signature="mixed_script_confusable")

        # the remaining checks compare script letters, so they need >=2 of them
        if len(letters) < 2:
            continue

        # hard-mix anomaly: Latin + a script that NEVER legitimately mixes with Latin
        # mid-token (Cherokee — a documented IDN-spoof syllabary). Unlike CJK, where
        # "IDカード" is a normal token, no language interleaves Latin with Cherokee, so
        # the mix itself is the tell — flagged WITHOUT asserting per-letter equivalences
        # (those are not carried, to avoid claiming an unverified look-alike).
        if "Latin" in scripts and ("Cherokee" in scripts):
            return Finding("suspect", 0.85,
                f"anomalous script mix in '{tok}' (Latin + Cherokee — homoglyph spoof)",
                conclusive=True, signature="mixed_script_confusable")

        # mixed-script confusable: Latin + (Cyrillic/Greek/Armenian) lookalikes in one token
        _FOREIGN = {"Cyrillic", "Greek", "Armenian"}
        if "Latin" in scripts and (scripts & _FOREIGN):
            foreign = [c for c in letters if _script(c) in _FOREIGN]
            if any(ord(c) in CONFUSABLE for c in foreign):
                skel = _skeleton(tok)
                return Finding("suspect", 0.9,
                    f"mixed-script confusable token '{tok}' impersonates '{skel}' "
                    f"(Latin + {'/'.join(sorted(scripts & _FOREIGN))} "
                    f"look-alikes)", conclusive=True, signature="mixed_script_confusable")

        # whole-script spoof: all-foreign token whose skeleton equals a TARGET
        if (scripts <= {"Cyrillic"} or scripts <= {"Greek"} or scripts <= {"Armenian"}) and letters:
            if all(ord(c) in CONFUSABLE for c in letters):
                skel = _skeleton(tok).strip(".-_").lower()
                if skel in DEMO_TARGETS:
                    return Finding("suspect", 0.85,
                        f"whole-script confusable token '{tok}' impersonates target "
                        f"'{skel}'", conclusive=True, signature="whole_script_confusable")

    return Finding("clean", 0.0, "confusable-cards: no mixed/whole-script confusables")
