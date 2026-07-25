# -*- coding: utf-8 -*-
"""
urlpunct deliberate-exclusion lock (external conveyor, M2; AD-33).

urlpunct_cards is a built detector that is DELIBERATELY not in the production
guard: its at-userinfo branch cannot tell a spoof (paypal.com@evil.ru) from an
ordinary dotted-local-part email (john.smith@company.com). Wiring it would flag
every first.last@ corporate address. These tests pin BOTH halves of that fact so
the decision is measured, not asserted, and so a future "helpful" wiring goes red.
"""
from _support import ok, clean

import product
from urlpunct_cards import urlpunct_cards_reader
from canonicalize import canonicalize


# Normal corporate emails a production guard must never flag. If someone wires
# urlpunct into product._READERS, these go red — that is the lock.
_NORMAL = [
    "email john.smith@company.com please",
    "contact maria.garcia@acme.co today",
    "follow @user@mastodon.social",
]


def test_production_guard_keeps_dotted_emails_clean():
    for t in _NORMAL:
        f = product.analyze(t)
        ok(f.label == "clean",
           f"production guard must not flag normal email {t!r} — got "
           f"{f.label}/{f.signature}; is urlpunct wired into _READERS?")


def test_urlpunct_would_false_positive_documents_why_excluded():
    # The measured reason for exclusion: urlpunct itself CANNOT separate a real
    # userinfo spoof from a dotted-local-part email — both come back 'suspect'.
    spoof = urlpunct_cards_reader(canonicalize("http://paypal.com@evil.ru/login")[0])
    ok(spoof.label == "suspect", "urlpunct should catch the actual spoof")
    normal = urlpunct_cards_reader(canonicalize("john.smith@company.com")[0])
    ok(normal.label == "suspect",
       "the exclusion rationale: urlpunct also (wrongly) flags a normal dotted "
       "email — this FP is exactly why it stays out of the always-on guard")
