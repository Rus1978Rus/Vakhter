# -*- coding: utf-8 -*-
"""
Contract for the non-ASCII dot/slash domain-separator branch in the confusable
detector (code/range/confusable_cards.py :: NASCII_DOT / NASCII_SLASH).

A homoglyph separator (paypal․com with U+2024, gmail。com with U+3002, micro∕soft
with U+2215) renders like a domain but is a different string. It is flagged ONLY
when the confusable sits BETWEEN two ASCII-Latin letters — the domain-separator
signature — so a CJK/Arabic sentence-final full stop and a real fraction slash
stay clean. This pins the branch and that no-false-positive boundary.
"""
from _support import ok, flags, clean
from confusable_cards import confusable_cards_reader as C


def test_dot_homoglyph_domain_flags():
    for s in ("paypal․com",     # U+2024 one dot leader
              "gmail。com",       # U+3002 ideographic full stop
              "coinbase｡com",    # U+FF61 halfwidth ideographic full stop
              "bank۔com"):        # U+06D4 Arabic full stop
        flags(C, s, "mixed_script_confusable")


def test_slash_homoglyph_domain_flags():
    for s in ("micro∕soft.com",   # U+2215 division slash
              "amazon⁄account",   # U+2044 fraction slash
              "drop⧸box.com"):    # U+29F8 big solidus
        flags(C, s, "mixed_script_confusable")


def test_cjk_sentence_final_stop_clean():
    # a 。 preceded by CJK (not by an ASCII letter) is legitimate punctuation
    for s in ("これはテストです。", "日本語。そうです", "Windowsをインストール。"):
        clean(C, s)


def test_arabic_full_stop_clean():
    clean(C, "مرحبا۔ كيف حالك")


def test_fraction_slash_clean():
    # a real fraction (digits around the slash, not ASCII letters) must not flag
    clean(C, "the ratio is 3⁄4 today")


def test_plain_domain_and_prose_clean():
    for s in ("example.com/path", "normal english text", "привет мир",
              "visit paypal.com now"):
        clean(C, s)
