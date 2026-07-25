# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
Contract for Armenian homoglyph detection (confusable_cards :: ARM_TO_LAT), via
the reader and the assembled guard.

Armenian joins Cyrillic/Greek as a recognised script in the mixed-script and
whole-script branches, with a CONSERVATIVE confusable set (only well-established
Latin look-alikes: օ→o, ո→n, ս→u, ա→a, Օ→O). Single-script Armenian text stays
clean; only a Latin+Armenian mix (or a whole-Armenian brand skeleton) flags.
"""
from _support import ok, flags, clean
from confusable_cards import confusable_cards_reader as C
from product import analyze

OH = chr(0x0585)    # Armenian small oh  -> o
VO = chr(0x0578)    # Armenian small vo  -> n
SE = chr(0x057D)    # Armenian small se  -> u
AYB = chr(0x0561)   # Armenian small ayb -> a


def test_armenian_mixed_script_flags():
    for s in ("g" + OH + OH + "gle.com",        # gօօgle
              "micr" + OH + "soft.com",          # micrօsoft
              "amaz" + OH + "n.com",             # amazօn
              AYB + "mazon.com",                 # աmazon
              "n" + OH + "rton.com"):            # nօrton
        flags(C, s, "mixed_script_confusable")
        flags(analyze, s)                        # and through the guard


def test_single_script_armenian_clean():
    # real Armenian words must never flag (only script MIX is the signal)
    for s in ("Հայաստան", "բարեւ ձեզ", "շնորհակալություն",
              "ես սիրում եմ", "մայրը եւ որդին"):
        clean(C, s)
        clean(analyze, s)


def test_armenian_letters_not_in_ascii_domain_are_fine():
    # a plain Latin domain is untouched by the Armenian branch
    clean(C, "google.com")
    clean(C, "amazon.com")
