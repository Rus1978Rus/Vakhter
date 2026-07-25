# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
Whitespace / space-lookalike detector card (SIMULATOR of a draft).

This axis follows the priority guidance exactly: it is NOT "every non-ASCII
space is dangerous". The family splits by real vector:

  - LINE / PARAGRAPH SEPARATOR (U+2028 / U+2029) are the genuine HIGH members:
    they are line breaks that a human does not see as a newline but a JS/JSON
    parser, a log line or a CSV record DOES — record / statement injection.
    -> ALARM (conclusive).

  - A space-lookalike (NBSP, NNBSP, EM/EN/THIN spaces, IDEOGRAPHIC SPACE, ...)
    doing DELIMITER duty in an ASCII-structured string — sitting against a
    syntax metacharacter ("rm<NBSP>-rf", "cmd<NNBSP>| sh") — masquerades as the
    ASCII space a shell / parser / allowlist splits on. -> ALARM (conclusive).

  - Any OTHER space-lookalike is a WITNESS, not an alarm: NBSP/NNBSP/EM space
    between letters is ordinary typography (French thin space, CJK spacing).
    "SPACE_LOOKALIKE != ASCII_SPACE" but also "!= AUTOMATICALLY DANGEROUS".
    -> WATCH when flanked by ASCII (ambiguous), OK when flanked by non-ASCII
    letters (clear i18n typography).
"""
import unicodedata
from invariant_engine.core import Finding

LINE_PARA = {0x2028, 0x2029}                       # LINE SEP / PARAGRAPH SEP
SPACE_LOOKALIKE = ({0x00A0, 0x1680, 0x202F, 0x205F, 0x3000}
                   | set(range(0x2000, 0x200B)))    # NBSP, OGHAM, NNBSP, MMSP, IDEO, 2000..200A
METACHAR = set("-=/;|&<>()[]{}'\"`$#:@")

NAME = {0x00A0: "NBSP", 0x202F: "NNBSP", 0x205F: "MMSP", 0x3000: "IDEOGRAPHIC SPACE",
        0x1680: "OGHAM SPACE", 0x2028: "LINE SEP", 0x2029: "PARAGRAPH SEP"}


def _nm(o):
    return NAME.get(o, f"U+{o:04X} space")


def _ascii_wordish(ch):
    if not ch:
        return False
    o = ord(ch)
    return o < 128 and (ch.isalnum())


def _nonascii_letter(ch):
    return bool(ch) and ord(ch) > 127 and unicodedata.category(ch).startswith("L")


def _letter(ch):
    return bool(ch) and unicodedata.category(ch).startswith("L")


def whitespace_cards_reader(text):
    """Whitespace authority: ALARM sep/delimiter / WATCH witness / OK typography."""
    # 1. line / paragraph separators — conclusive injection
    for ch in text:
        if ord(ch) in LINE_PARA:
            return Finding("suspect", 0.9,
                f"{_nm(ord(ch))} U+{ord(ch):04X} — invisible line break "
                f"(record / statement injection)",
                conclusive=True, signature="line_para_sep")

    pos = [i for i, ch in enumerate(text) if ord(ch) in SPACE_LOOKALIKE]
    if not pos:
        return Finding("clean", 0.0, "whitespace-cards: no space-lookalikes")

    # 2. space-lookalike doing delimiter duty against a metacharacter
    for i in pos:
        prev = text[i - 1] if i > 0 else ""
        nxt = text[i + 1] if i + 1 < len(text) else ""
        if prev in METACHAR or nxt in METACHAR:
            return Finding("suspect", 0.82,
                f"{_nm(ord(text[i]))} as a delimiter next to a metacharacter "
                f"('{prev}<sp>{nxt}') — masquerades as an ASCII split point",
                conclusive=True, signature="space_delimiter")

    # 3. witness vs. typography. Genuine i18n prose (the text carries non-ASCII
    #    letters) where every lookalike is an ordinary letter-to-letter word gap
    #    is legitimate typography -> OK. Otherwise the lookalike sits in an
    #    ASCII / non-prose context and is a WITNESS (held, not stripped).
    has_i18n = any(_nonascii_letter(c) for c in text)
    all_letter_gaps = True
    for i in pos:
        prev = text[i - 1] if i > 0 else ""
        nxt = text[i + 1] if i + 1 < len(text) else ""
        if not (_letter(prev) and _letter(nxt)):
            all_letter_gaps = False
            break
    if has_i18n and all_letter_gaps:
        return Finding("clean", 0.0,
                       "whitespace-cards: space-lookalikes are i18n typography "
                       "(letter-to-letter word gaps in non-ASCII prose)")

    return Finding("suspect", 0.4,
                   f"{len(pos)} space-lookalike(s) in an ASCII context — witness "
                   f"(not auto-HIGH; held for review, not stripped)",
                   signature="space_witness")
