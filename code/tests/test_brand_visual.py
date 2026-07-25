# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
Contract for the visual-multigraph brand-mimicry check
(code/range/digit_cards.py :: _visual_brand).

Typosquatting look-alikes that need no digit: rn→m (arnazon), vv→w (vvhatsapp),
cl→d, and capital-I used as lowercase-l (paypaI, googIe). A label is flagged ONLY
when a fold lands EXACTLY on a brand AND the label is not already that brand — so
ordinary words carrying rn/vv/cl/I and legitimate brand mentions stay clean.
Raw edit-distance-1 was deliberately NOT adopted (short brands make it
FP-unsafe); this pins the FP-safe subset and its boundary.
"""
from _support import ok, flags, clean
from digit_cards import digit_cards_reader as D


def test_rn_to_m_spoof_flags():
    for s in ("arnazon-login.com", "rnicrosoft account", "rnetamask wallet"):
        flags(D, s, "brand_visual")


def test_vv_to_w_spoof_flags():
    for s in ("vvhatsapp verify", "vvellsfargo alert"):
        flags(D, s, "brand_visual")


def test_capital_i_for_l_spoof_flags():
    for s in ("paypaI security", "googIe drive"):
        flags(D, s, "brand_visual")


def test_legit_brand_mention_clean():
    # the real brand (no trick) must not fire — lower(label) is already the brand
    for s in ("Amazon", "amazon", "Microsoft", "Chase", "PayPal", "Instagram"):
        clean(D, s)


def test_benign_words_with_rn_vv_cl_i_clean():
    # ordinary words carrying the trigger multigraphs must never de-confuse onto a brand
    benign = ("modern govern return internet external eternal pattern concern "
              "learn intern stern tavern lantern savvy revving divvy clean close "
              "clock cloud click clarity class cluster include declare business "
              "address username filename database wireless fitness harness "
              "Instagram Islands Italy Iceland India Iris iPhone iCloud").split()
    for w in benign:
        clean(D, w)


def test_short_brandish_words_not_over_matched():
    # len<5 labels are skipped entirely, and 5-letter real words that are also
    # brands are treated as legit mentions
    for s in ("chase the ball", "steam engine", "visa application", "meta tags"):
        clean(D, s)
