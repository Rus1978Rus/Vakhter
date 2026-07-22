# -*- coding: utf-8 -*-
"""
Unit contract for the confusable / homoglyph detector (code/range/confusable_cards.py).

Flagship of the test layer: the FALSE-NEGATIVE this suite exists to prevent lived
here. Roman-numeral letter-FORMS are Unicode category Nl and are NOT counted by
the detector's _letters(); a short token like "ⅬG" (one ASCII letter + one Roman
form) was therefore skipped by the ">= 2 letters" gate and slipped through. The
fix (commit 8deaf9a) moved the Roman/dash checks BEFORE that gate. The regression
test below pins that fix so it cannot silently come back.

Contract under test:
  ALARM  — a single token that MIXES Latin with Cyrillic/Greek lookalikes, or a
           Roman-numeral form beside a Latin letter, or a non-ASCII dash inside a
           domain-like token, or a whole-foreign token whose skeleton == a target.
  OK     — single-script native text, and standalone Roman numerals.
"""
from _support import ok, flags, clean
from confusable_cards import (
    confusable_cards_reader as R,
    CYR_TO_LAT, GRK_TO_LAT, ROMAN_TO_LAT,
)


def test_mixed_script_cyrillic():
    # one Cyrillic lookalike among Latin letters — the classic IDN / brand spoof
    flags(R, "pаypal.com", "mixed_script_confusable")   # а U+0430
    flags(R, "аpple.com", "mixed_script_confusable")    # а U+0430
    flags(R, "gооgle", "mixed_script_confusable")  # о о U+043E
    flags(R, "micrоsoft", "mixed_script_confusable")    # о U+043E
    flags(R, "Сitibank", "mixed_script_confusable")     # С U+0421 (capital)


def test_mixed_script_greek():
    flags(R, "gοοgle", "mixed_script_confusable")  # ο ο U+03BF
    flags(R, "Αpple", "mixed_script_confusable")        # Α U+0391
    flags(R, "νisa.com", "mixed_script_confusable")     # ν U+03BD -> v
    flags(R, "Χase", "mixed_script_confusable")         # Χ U+03A7 -> X


def test_roman_numeral_short_token_regression():
    # REGRESSION for the false-negative fixed in 8deaf9a. A Roman-numeral form is
    # category Nl (not a letter to _letters()), so a single ASCII letter beside one
    # used to be dropped by the >=2-letter gate. Each of these MUST now ALARM.
    for s in ("ⅬG", "ⅩL", "ⅯB", "ⅠD", "ⅮC"):  # ⅬG ⅩL ⅯB ⅠD ⅮC
        flags(R, s, "mixed_script_confusable")
    # and the lowercase forms mixed into an ASCII word
    flags(R, "paypaⅼ", "mixed_script_confusable")   # paypaⅼ  (ⅼ U+217C)
    flags(R, "iⅼlegal", "mixed_script_confusable")  # iⅼlegal


def test_pure_roman_numerals_stay_clean():
    # a standalone Roman numeral has NO ASCII letter, so has_ascii_latin is False
    # and the Roman branch never fires — this is the guard against over-flagging.
    for s in ("Ⅹ", "ⅩⅤⅠ", "Ⅻ", "ⅰ ⅴ ⅹ", "Ⅳ"):
        clean(R, s)  # Ⅹ / ⅩⅤⅠ / Ⅻ / "ⅰ ⅴ ⅹ" / Ⅳ


def test_native_single_script_clean():
    # single-script native text must NEVER flag. A blanket "non-Latin letter =>
    # suspect" rule would flag ~25% of ordinary Russian (соус, орех, хор ...),
    # which is exactly why the detector keys on script MIX, not foreign presence.
    for s in ("соус", "орех", "хор",
              "привет мир",       # привет мир
              "καλημέρα",              # καλημέρα
              "σοφία"):                              # σοφία
        clean(R, s)


def test_nonascii_dash_domain_vs_prose():
    # a non-ASCII dash is a spoof ONLY inside a domain-ish token (one with a dot);
    # in ordinary prose typography (well‐known) it is legitimate and must stay OK.
    flags(R, "pay‐pal.com", "mixed_script_confusable")   # hyphen U+2010 in a domain
    flags(R, "e‑bay.com", "mixed_script_confusable")     # non-breaking hyphen U+2011
    clean(R, "a well‐known author")
    clean(R, "state–of–the–art design")        # en-dashes in prose


def test_whole_script_on_target():
    # a wholly-Cyrillic token whose Latin skeleton equals a DEMO target -> spoof.
    # уаһоо  =  у0443 а0430 һ04BB о043E о043E  ->  skeleton "yahoo"
    flags(R, "уаһоо", "whole_script_confusable")


def test_whole_script_off_target_clean():
    # a wholly-Cyrillic token whose skeleton is NOT a known target must stay OK,
    # or the rule would fire on ordinary foreign words.
    clean(R, "соус")   # соус -> skeleton "coyc", not a target


def test_ascii_and_native_together_clean():
    # mixing scripts ACROSS tokens (English word + Russian word) is not a spoof;
    # only a MIX WITHIN one token is. Each token is single-script here.
    clean(R, "hello мир")           # hello мир
    clean(R, "the σοφία of it")  # the σοφία of it


def test_every_cyrillic_table_form_flags():
    # behavioral lock on the CYR_TO_LAT table: every listed codepoint, embedded in
    # an ASCII-Latin word, must produce a mixed-script ALARM. Complements the
    # structural coverage_lock (card<->table) with a live detector check.
    for cp in CYR_TO_LAT:
        flags(R, "test" + chr(cp) + "ing", "mixed_script_confusable")


def test_every_greek_table_form_flags():
    for cp in GRK_TO_LAT:
        flags(R, "test" + chr(cp) + "ing", "mixed_script_confusable")


def test_every_roman_table_form_flags():
    # a Roman form beside a single ASCII letter must ALARM (the 8deaf9a path)
    for cp in ROMAN_TO_LAT:
        flags(R, "A" + chr(cp), "mixed_script_confusable")


def test_plain_ascii_clean():
    for s in ("plain ascii text", "paypal.com", "https://example.org/login",
              "The quick brown fox.", "user@example.com"):
        clean(R, s)
