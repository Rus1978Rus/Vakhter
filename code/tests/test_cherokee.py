# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
Contract for Cherokee homoglyph detection (confusable_cards, hard-mix branch).

Cherokee is a documented IDN-spoof syllabary, but its exact Latin equivalences are
not carried (to avoid asserting unverified look-alikes). Instead the detector uses
the structural fact that no language interleaves Latin with Cherokee mid-token, so
a Latin+Cherokee MIX in one token is itself the tell. Crucially this must NOT flag
scripts that DO legitimately mix with Latin mid-token — Japanese/CJK ("IDカード",
"iPhone12") — nor pure single-script Cherokee.
"""
from _support import ok, flags, clean
from confusable_cards import confusable_cards_reader as C
from product import analyze

CHER_A = chr(0x13A0)   # Cherokee letter A (looks like Latin D/A)
CHER_B = chr(0x13F4)   # Cherokee letter YV (looks like Latin B)
CHER_H = chr(0x13B2)   # Cherokee letter looks like Latin H/P


def test_cherokee_latin_mix_flags():
    for s in (CHER_H + "ayPal.com", "g" + CHER_A + "ogle.com",
              "amaz" + CHER_A + "n.com", CHER_B + "ank-login.com"):
        flags(C, s, "mixed_script_confusable")
        flags(analyze, s)


def test_pure_cherokee_clean():
    # ᏣᎳᎩ = "Tsalagi" (Cherokee) — single-script, must stay clean
    for s in ("ᏣᎳᎩ", CHER_A + CHER_B):
        clean(C, s)
        clean(analyze, s)


def test_latin_cjk_mix_stays_clean():
    # Japanese/CJK legitimately interleaves Latin mid-token — must NOT be flagged
    for s in ("IDカード", "iPhone12", "Windows10", "日本語ID", "USB端子"):
        clean(C, s)
        clean(analyze, s)
