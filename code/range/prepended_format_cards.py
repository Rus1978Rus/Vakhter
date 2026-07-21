# -*- coding: utf-8 -*-
"""
Prepended / enclosing-format detector card (SIMULATOR of a draft).

These are the format (Cf) characters that are NOT default-ignorable — the ones
that ACT on their scope instead of hiding. They fall outside "class 138" for
exactly that reason: they change how the surrounding characters are read or laid
out. Two mechanism branches:

  1. PREPENDED CONCATENATION MARKS (Arabic / Syriac / Kaithi number & abbreviation
     signs). Each prepends to and visually encloses the characters that FOLLOW it
     — an Arabic number sign takes the following Arabic-Indic digits as its scope.
     Attack: point the mark at foreign-script digits / a security token, so the
     enclosing/annotating effect lands on content it was never meant to scope
     (amount spoofing, number-meaning confusion).

  2. BRACKETING / ANNOTATION CONTROLS (interlinear annotation FFF9..FFFB;
     Egyptian segment/join 13430..13438). They come in ANCHOR..SEPARATOR..
     TERMINATOR triples or BEGIN..END pairs that structure a run. Attack:
     unbalanced or orphaned brackets desync a parser, or hide "annotation" text
     that display and logic treat differently. Unicode marks interlinear
     annotation as NOT for open interchange, so its mere presence is a witness.

  ALARM (conclusive):
    - a prepended mark not prefixing its own script's digits/letters (scope abuse
      / orphan), OR
    - unbalanced interlinear annotation, an orphan separator, OR
    - unbalanced Egyptian segment brackets.
  WATCH:
    balanced interlinear annotation present (Unicode: not for interchange).
  OK:
    a prepended mark on its own script's digits/letters; balanced Egyptian
    segment; nothing present.
"""
from invariant_engine.core import Finding

ARABIC_PCM = {0x0600, 0x0601, 0x0602, 0x0603, 0x0604, 0x0605, 0x06DD, 0x08E2, 0x0890, 0x0891}
KAITHI_PCM = {0x110BD, 0x110CD}
SYRIAC_ABBR = {0x070F}
PCM = ARABIC_PCM | KAITHI_PCM | SYRIAC_ABBR

ANN_ANCHOR, ANN_SEP, ANN_TERM = 0xFFF9, 0xFFFA, 0xFFFB
EGY_JOIN = set(range(0x13430, 0x13437))     # 13430..13436 joiners / inserts / overlay
EGY_BEGIN, EGY_END = 0x13437, 0x13438
ALL = PCM | {ANN_ANCHOR, ANN_SEP, ANN_TERM} | EGY_JOIN | {EGY_BEGIN, EGY_END}


def _is_prepended_format(o):
    return o in ALL


def _arabic_digit(ch):
    o = ord(ch) if ch else -1
    return 0x0660 <= o <= 0x0669 or 0x06F0 <= o <= 0x06F9


def _kaithi_digit(ch):
    o = ord(ch) if ch else -1
    return 0x11066 <= o <= 0x1106F


def _syriac_letter(ch):
    o = ord(ch) if ch else -1
    return 0x0710 <= o <= 0x074F


def _pcm_scope_ok(o, nxt):
    if o in ARABIC_PCM:
        return _arabic_digit(nxt)
    if o in KAITHI_PCM:
        return _kaithi_digit(nxt)
    return _syriac_letter(nxt)              # syriac abbreviation mark -> letters


def prepended_format_cards_reader(text):
    """Prepended/enclosing-format authority: ALARM scope abuse / imbalance."""
    if not any(_is_prepended_format(ord(c)) for c in text):
        return Finding("clean", 0.0, "prepended-format-cards: none present")

    # 1. prepended concatenation mark not scoping its own script
    for i, ch in enumerate(text):
        o = ord(ch)
        if o in PCM:
            nxt = text[i + 1] if i + 1 < len(text) else ""
            if not _pcm_scope_ok(o, nxt):
                return Finding("suspect", 0.85,
                    f"prepended mark U+{o:04X} not scoping its own-script "
                    f"number/word (follows '{nxt or '<end>'}') — scope abuse",
                    conclusive=True, signature="pcm_scope_abuse")

    # 2. interlinear annotation balance / orphan separator
    anchors = sum(1 for c in text if ord(c) == ANN_ANCHOR)
    terms = sum(1 for c in text if ord(c) == ANN_TERM)
    seps = sum(1 for c in text if ord(c) == ANN_SEP)
    if anchors != terms:
        return Finding("suspect", 0.88,
            f"unbalanced interlinear annotation (anchor={anchors}, term={terms}) "
            f"— annotation desync / hidden text", conclusive=True,
            signature="annotation_imbalance")
    if seps and anchors == 0:
        return Finding("suspect", 0.85,
            "interlinear annotation SEPARATOR with no annotation open — orphan",
            conclusive=True, signature="annotation_orphan")

    # 3. Egyptian segment balance
    begins = sum(1 for c in text if ord(c) == EGY_BEGIN)
    ends = sum(1 for c in text if ord(c) == EGY_END)
    if begins != ends:
        return Finding("suspect", 0.8,
            f"unbalanced Egyptian segment brackets (begin={begins}, end={ends})",
            conclusive=True, signature="segment_imbalance")

    # 4. balanced interlinear annotation present -> witness (not for interchange)
    if anchors:
        return Finding("suspect", 0.4,
            "interlinear annotation present (balanced) — Unicode: not for open "
            "interchange; witness (held, not stripped)",
            signature="annotation_witness")

    # 5. everything present is a legit in-script prepend / balanced segment
    return Finding("clean", 0.0,
                   "prepended-format-cards: marks scope their own script / balanced")
