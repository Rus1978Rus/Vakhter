# -*- coding: utf-8 -*-
"""
Contract for the shared brand corpus (code/range/brand_corpus.py) and its two
consumers: the digit-leet detector (digit_cards) and the whole-script branch of
the confusable detector (confusable_cards).

Pins: (1) both detectors read ONE corpus (no drift, cf. AD-13); (2) the corpus
covers the high-frequency phishing brands; (3) the whole-script length gate keeps
it FP-safe; (4) benign digit+letter tokens and ordinary Russian stay clean.
"""
from _support import ok, eq, flags, clean
from brand_corpus import PHISHING_BRANDS, WHOLE_SCRIPT_TARGETS, WHOLE_SCRIPT_MIN_LEN
from digit_cards import digit_cards_reader as D, BRANDS as DIGIT_BRANDS
from confusable_cards import confusable_cards_reader as C, DEMO_TARGETS


def test_single_source_of_truth():
    # both consumers must read the shared corpus, not private copies
    ok(DIGIT_BRANDS is PHISHING_BRANDS, "digit_cards must use the shared corpus")
    ok(set(DEMO_TARGETS) == set(WHOLE_SCRIPT_TARGETS),
       "confusable whole-script must use the shared corpus")


def test_corpus_covers_high_frequency_brands():
    for b in ("microsoft", "paypal", "chase", "wellsfargo", "coinbase",
              "docusign", "netflix", "amazon", "sberbank", "dhl"):
        ok(b in PHISHING_BRANDS, f"{b} missing from corpus")


def test_whole_script_gate_is_length_safe():
    # every whole-script target is >= the min length (short brands excluded there)
    for b in WHOLE_SCRIPT_TARGETS:
        ok(len(b) >= WHOLE_SCRIPT_MIN_LEN, f"{b} too short for whole-script")
    ok("visa" not in WHOLE_SCRIPT_TARGETS, "4-letter visa must be gated out")
    ok("visa" in PHISHING_BRANDS, "visa still covered by the leet branch")


def test_leet_flags_new_brands():
    for s in ("wellsfarg0-login", "d0cusign.com", "ch4se-alert",
              "r0blox-free", "sp0tify-premium", "tr3zor-wallet", "v1sa-secure"):
        flags(D, s, "homoglyph_digit")


def test_whole_script_flags_all_cyrillic_brand():
    # whole-script fires on a PURE all-Cyrillic brand token (name/handle spoof);
    # cisco=сіѕсо  skype=ѕкуре  chase=сһаѕе  yahoo=уаһоо (every letter a look-alike)
    for s in ("сіѕсо", "ѕкуре", "сһаѕе", "уаһоо"):
        flags(C, s, "whole_script_confusable")


def test_cyrillic_brand_domain_still_flags_as_mixed():
    # append a Latin TLD and the SAME spoof is caught by the mixed-script branch
    # (com is Latin, so the token is mixed) — still suspect, different signature
    flags(C, "сіѕсо.com", "mixed_script_confusable")
    flags(C, "сһаѕе-login.com", "mixed_script_confusable")


def test_leet_no_false_positive():
    # benign digit+letter tokens must not de-leet onto a brand
    for s in ("mp3 file", "utf8 encoding", "sha256 hash", "win10 update",
              "ec2 instance", "covid19 data", "base64 blob", "h264 video"):
        clean(D, s)


def test_whole_script_no_false_positive_on_russian():
    for s in ("россия", "сосна", "посёлок", "красота", "каскад"):
        clean(C, s)
