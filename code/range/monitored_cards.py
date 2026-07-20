# -*- coding: utf-8 -*-
"""
Monitored-format detector card (SIMULATOR of a draft) — the WITNESS tier.

This card is the operational form of the doctrine "OBSERVE ALL, PRIORITIZE THE
REAL VECTORS". Its members are rare, low-vector, mostly deprecated format
controls: they are NOT auto-HIGH. The default posture is WITNESS (WATCH) — seen,
logged, held — and it escalates to ALARM only when a monitored control appears
in a genuinely hostile context (splitting a word/token, or next to a syntax
metacharacter). A monitored control inside its ONE legitimate substrate
(a musical control among musical symbols; a shorthand control among Duployan)
is vouched OK.

  ALARM (conclusive):
    a monitored control in a hostile context — splitting a word/token, or
    directly against a metacharacter.
  OK (clean):
    the control sits inside its legitimate substrate (music / shorthand run),
    or no monitored controls at all.
  WATCH (witness — the default for this class):
    a monitored control is present but neither hostile nor provably in-substrate.
"""
from invariant_engine.core import Finding

MONGOLIAN_VS = {0x180E}                              # MONGOLIAN VOWEL SEPARATOR
DEPRECATED_FMT = set(range(0x206A, 0x2070))          # 206A..206F symmetric-swap / shaping / digit
SHORTHAND_FMT = set(range(0x1BCA0, 0x1BCA4))         # Duployan shorthand format controls
MUSICAL_FMT = set(range(0x1D173, 0x1D17B))           # musical beam/tie/slur/phrase controls
MONITORED = MONGOLIAN_VS | DEPRECATED_FMT | SHORTHAND_FMT | MUSICAL_FMT

MUSIC_BLOCK = set(range(0x1D100, 0x1D200))           # legit substrate for musical controls
DUPLOYAN_BLOCK = set(range(0x1BC00, 0x1BCA0))        # legit substrate for shorthand controls
METACHAR = set("-=/;|&<>()[]{}'\"`$#:@")

NAME = {0x180E: "MONGOLIAN VOWEL SEPARATOR"}


def _nm(o):
    return NAME.get(o, f"U+{o:04X} format control")


def _wordish(ch):
    return bool(ch) and ch.isalnum()


def _in_substrate(o, text):
    """A monitored control legit only among its own substrate characters."""
    if o in MUSICAL_FMT:
        return any(ord(c) in MUSIC_BLOCK for c in text)
    if o in SHORTHAND_FMT:
        return any(ord(c) in DUPLOYAN_BLOCK for c in text)
    return False                                     # MVS / deprecated: no modern substrate


def monitored_cards_reader(text):
    """Monitored-format authority: ALARM hostile / OK in-substrate / WATCH witness."""
    idx = [i for i, ch in enumerate(text) if ord(ch) in MONITORED]
    if not idx:
        return Finding("clean", 0.0, "monitored-cards: no monitored format controls")

    # A control inside its own substrate (music among music, shorthand among
    # Duployan) is legit — that vouch takes precedence over the hostile checks,
    # which are meant for the substrate-less controls (MVS / deprecated 206A-F).
    off_substrate = [i for i in idx if not _in_substrate(ord(text[i]), text)]
    if not off_substrate:
        return Finding("clean", 0.0,
                       "monitored-cards: controls inside their legit substrate "
                       "(music / shorthand)")

    # ALARM: a substrate-less monitored control in a hostile context
    for i in off_substrate:
        o = ord(text[i])
        prev = text[i - 1] if i > 0 else ""
        nxt = text[i + 1] if i + 1 < len(text) else ""
        if prev in METACHAR or nxt in METACHAR:
            return Finding("suspect", 0.8,
                f"{_nm(o)} next to a metacharacter ('{prev}<fmt>{nxt}') — "
                f"hostile use of a deprecated/monitored control",
                conclusive=True, signature="monitored_hostile")
        if _wordish(prev) and _wordish(nxt):
            return Finding("suspect", 0.8,
                f"{_nm(o)} splitting a word ('{prev}<fmt>{nxt}') — "
                f"hostile use of a deprecated/monitored control",
                conclusive=True, signature="monitored_hostile")

    # WATCH: present, witnessed, held — NOT auto-HIGH
    return Finding("suspect", 0.35,
                   f"{len(off_substrate)} monitored format control(s) present — "
                   f"WITNESS (observed and held; not auto-HIGH, not stripped)",
                   signature="monitored_witness")
