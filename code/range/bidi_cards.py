# -*- coding: utf-8 -*-
"""
Bidi-axis detector card (SIMULATOR of a draft) — the DIRECTIONAL-CONTROL axis.

This is a SEPARATE axis from the invisible/zero-width card. A zero-width char is
invisible; a bidi control is (often) invisible too, but its danger is of a
different KIND: it makes the LOGICAL (byte) order diverge from the VISUAL
(rendered) order. That divergence is the Trojan-Source attack (CVE-2021-42574):
what a human reviewer SEES is not what the compiler / parser CONSUMES.

Two laws this card encodes:

  1. BIDI_DETECTED != SAFE_TO_DELETE.
     Bidi controls are MANDATORY to render Arabic / Hebrew / mixed text
     correctly. Blindly stripping them corrupts legitimate content. So the
     card NEVER recommends silent deletion — its verdicts are ALARM / WATCH,
     i.e. reject-or-review, never "just remove it".

  2. BIDI_PRESENT != BIDI_DANGEROUS.
     Balanced isolates/embeddings around genuine RTL script are legitimate
     layout. The danger is OVERRIDES and IMBALANCE, not presence.

  ALARM (conclusive):
    1. an OVERRIDE run (LRO/RLO) whose scope contains ASCII/Latin word or
       operator characters -> forced logical!=visual reorder of readable text
       (Trojan Source). Overrides are the hard signal.
    2. directional IMBALANCE: embeddings/isolates opened but never closed, or
       a pop underflow -> the control leaks past its intended scope / line.
    3. a bidi control splitting a LTR code/word token (foo<RLI>bar).
  OK (clean):
    only implicit marks (LRM/RLM/ALM) and/or BALANCED isolates/embeddings whose
    controlled content is predominantly RTL script -> legitimate layout.
  WATCH (non-conclusive):
    bidi present, balanced, but neither provably legit RTL layout nor a proven
    smuggle -> keep an eye, do not auto-clear, do not auto-delete.
"""
import unicodedata
from invariant_engine.core import Finding

# --- the directional-control alphabet (the whole axis, by role) ---
OVERRIDE   = {0x202D, 0x202E}                       # LRO RLO  (force a direction)
EMBED      = {0x202A, 0x202B}                       # LRE RLE  (push a direction)
ISOLATE    = {0x2066, 0x2067, 0x2068}               # LRI RLI FSI
POP_EMBED  = {0x202C}                               # PDF  (pop LRE/RLE/LRO/RLO)
POP_ISO    = {0x2069}                               # PDI  (pop isolate)
MARK       = {0x200E, 0x200F, 0x061C}               # LRM RLM ALM (implicit, no scope)

OPEN  = OVERRIDE | EMBED | ISOLATE
CLOSE = POP_EMBED | POP_ISO
ALL_BIDI = OPEN | CLOSE | MARK

NAME = {0x202A: "LRE", 0x202B: "RLE", 0x202C: "PDF", 0x202D: "LRO", 0x202E: "RLO",
        0x2066: "LRI", 0x2067: "RLI", 0x2068: "FSI", 0x2069: "PDI",
        0x200E: "LRM", 0x200F: "RLM", 0x061C: "ALM"}


def _is_bidi(ch):
    return ord(ch) in ALL_BIDI


def _rtl_script(ch):
    """True for a strong-RTL letter (Arabic / Hebrew / Syriac / Thaana ...)."""
    o = ord(ch)
    return (0x0590 <= o <= 0x08FF) or (0xFB1D <= o <= 0xFDFF) or (0xFE70 <= o <= 0xFEFF)


def _ltr_tokenish(ch):
    """ASCII/Latin letter, digit or a syntax operator — the stuff a reviewer reads."""
    o = ord(ch)
    if 0x30 <= o <= 0x39 or 0x41 <= o <= 0x5A or 0x61 <= o <= 0x7A:
        return True
    return ch in "/;=(){}[]<>|&$'\"`#-_.@:%?~+*!\\,"


# ---- conclusive checks -------------------------------------------------
def _override_over_ltr(text):
    """LRO/RLO whose scope carries LTR/ASCII content = Trojan-Source reorder."""
    depth = 0
    scope_ltr = 0
    open_name = None
    for ch in text:
        o = ord(ch)
        if o in OVERRIDE:
            depth += 1
            if open_name is None:
                open_name = NAME[o]
            scope_ltr = 0
        elif o in POP_EMBED and depth > 0:
            if scope_ltr > 0:
                return Finding("suspect", 0.92,
                    f"{open_name} override scope reorders {scope_ltr} readable "
                    f"LTR char(s) — logical!=visual (Trojan Source)",
                    conclusive=True, signature="bidi_override_reorder")
            depth -= 1
            open_name = None
        elif depth > 0 and _ltr_tokenish(ch):
            scope_ltr += 1
    if depth > 0 and scope_ltr > 0:      # override never popped, still carrying LTR
        return Finding("suspect", 0.92,
            f"{open_name} override left open over {scope_ltr} readable LTR "
            f"char(s) — logical!=visual (Trojan Source)",
            conclusive=True, signature="bidi_override_reorder")
    return None


def _imbalance(text):
    """Depth of embeddings/isolates must return to 0; no pop underflow."""
    emb = iso = 0
    underflow = False
    for ch in text:
        o = ord(ch)
        if o in EMBED or o in OVERRIDE:
            emb += 1
        elif o in ISOLATE:
            iso += 1
        elif o in POP_EMBED:
            if emb == 0:
                underflow = True
            else:
                emb -= 1
        elif o in POP_ISO:
            if iso == 0:
                underflow = True
            else:
                iso -= 1
    if emb or iso or underflow:
        return Finding("suspect", 0.88,
            f"unbalanced directional controls (embed={emb}, isolate={iso}, "
            f"underflow={underflow}) — scope leaks past its line",
            conclusive=True, signature="bidi_imbalance")
    return None


def _splits_ltr_token(text):
    """A scope-opening bidi control wedged inside a LTR word/code token."""
    for i, ch in enumerate(text):
        if ord(ch) in (OPEN | CLOSE):
            prev = text[i - 1] if i > 0 else ""
            nxt = text[i + 1] if i + 1 < len(text) else ""
            if prev and nxt and _ltr_tokenish(prev) and _ltr_tokenish(nxt) \
               and not _rtl_script(prev) and not _rtl_script(nxt):
                return Finding("suspect", 0.8,
                    f"{NAME.get(ord(ch),'bidi')} wedged inside a LTR token "
                    f"('{prev}<{NAME.get(ord(ch),'?')}>{nxt}')",
                    conclusive=True, signature="bidi_token_split")
    return None


def _first_smuggle(text):
    for chk in (_override_over_ltr, _imbalance, _splits_ltr_token):
        f = chk(text)
        if f:
            return f
    return None


# ---- legit-layout vouch ------------------------------------------------
def _legit_layout(text):
    """Balanced isolates/embeddings around genuine RTL script, or bare marks."""
    controls = [c for c in text if _is_bidi(c)]
    if not controls:
        return True
    if any(ord(c) in OVERRIDE for c in controls):
        return False                                  # overrides never auto-vouched
    if all(ord(c) in MARK for c in controls):         # bare implicit marks
        return any(_rtl_script(c) for c in text)      # only legit near RTL text
    # scope controls present: require balance AND real RTL content
    bal = _imbalance(text) is None
    has_rtl = any(_rtl_script(c) for c in text)
    return bal and has_rtl


def bidi_cards_reader(text):
    """Bidi authority: ALARM reorder/imbalance / OK legit RTL layout / WATCH.

    NEVER_BLIND_STRIP: no verdict here authorizes silent deletion of a control;
    remediation is reject-or-review, because deleting corrupts real RTL text.
    """
    smug = _first_smuggle(text)
    if smug:
        return smug
    controls = [c for c in text if _is_bidi(c)]
    if not controls:
        return Finding("clean", 0.0, "bidi-cards: no directional controls")
    if _legit_layout(text):
        return Finding("clean", 0.0,
                       "bidi-cards: balanced controls over genuine RTL layout")
    return Finding("suspect", 0.45,
                   f"{len(controls)} bidi control(s) present without provable "
                   f"RTL-layout context (do not strip — review)",
                   signature="bidi_watch")
