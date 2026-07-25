# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
BRAND_CORPUS — one source of truth for "which brands do we protect", shared by
the two brand-mimicry detectors so they cannot drift apart (cf. AD-13):

  - digit_cards.py      uses PHISHING_BRANDS for de-leet matching (paypa1, g00gle)
  - confusable_cards.py uses WHOLE_SCRIPT_TARGETS for the whole-script branch
                        (a wholly-Cyrillic/Greek token whose skeleton == a brand)

The list is ordered by real-world impersonation frequency (the brands most seen
in public phishing / brand-abuse telemetry: big tech, the major banks and card
networks, shipping/mail, crypto, and the large RU services), lowercased and
letters-only — both consumers strip non-alpha before matching.

This replaces the two hard-coded DEMO lists. It is still a curated demo corpus,
not the full brand universe; a production deployment swaps in its own list here
and nothing else changes.
"""

# frequency-ordered; grouped only for readability
PHISHING_BRANDS = {
    # big tech / accounts
    "microsoft", "google", "apple", "icloud", "amazon", "meta", "facebook",
    "instagram", "whatsapp", "linkedin", "netflix", "youtube", "gmail",
    "outlook", "yahoo", "adobe", "docusign", "dropbox", "spotify", "discord",
    "roblox", "steam", "tiktok", "twitter", "cisco", "skype", "ebay", "walmart",
    "aliexpress",
    # finance / cards / pay
    "paypal", "chase", "wellsfargo", "bankofamerica", "americanexpress",
    "mastercard", "visa", "cashapp", "venmo", "revolut",
    # crypto
    "coinbase", "binance", "metamask", "kraken", "trezor", "ledger",
    # shipping / mail
    "dhl", "fedex", "usps",
    # large RU services
    "sberbank", "tinkoff", "yandex", "wildberries", "ozon", "gosuslugi",
    "telegram",
}

# The whole-script branch fires on an all-foreign token, so a very short target
# skeleton (<=4) could collide with a real short word; gate it on length >= 5.
# (Short brands like "visa"/"ebay" are still covered by the leet and single-
#  substitution mixed-script branches, just not by whole-script.)
WHOLE_SCRIPT_MIN_LEN = 5
WHOLE_SCRIPT_TARGETS = frozenset(b for b in PHISHING_BRANDS
                                 if len(b) >= WHOLE_SCRIPT_MIN_LEN)
