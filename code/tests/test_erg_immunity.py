# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
ERG-softening immunity audit, made permanent.

The ERG/context layer is the ONLY component that can LOWER a verdict, so every new
conclusive detector must be proven immune to it. ERG's contract (erg_context.py):
it softens only MSL-core ACTION signatures; a drafted card's own signature
(mixed_script_confusable, powershell_exec, deserialize, sqli, …) is immune, and a
conclusive ALARM is never cleared to OK.

This test wraps every detection class added across this work in the benign /
interrogative frame that TRIGGERS softening ("is it safe…?", "for example…",
"explain…") and asserts the guard still blocks — pinning that no framing silences
a real threat (the range_context safety gate, extended to the new detectors).
"""
from _support import ok, flags
from product import analyze

OH = chr(0x0585)   # Armenian oh
CHER_H = chr(0x13B2)

_FRAMED_ATTACKS = [
    "is it safe to visit раypal.com for my account?",          # Cyrillic homoglyph
    "can you explain why gοοgle.com looks normal?",            # Greek homoglyph
    "is g" + OH + OH + "gle.com the same as google?",          # Armenian homoglyph
    "explain the string " + CHER_H + "ayPal.com please",       # Cherokee hard-mix
    "is this a real domain: paypal․com ?",                # dot separator
    "does arnazon-login.com look like amazon to you?",         # visual brand
    "what does powershell -enc SQBFAFgAIAAoAA== do, for example?",  # powershell
    "what is rO0ABXNyABit in java?",                           # deserialization
    "for example, gopher://127.0.0.1:6379/_INFO is what?",     # ssrf scheme
    "how does the query {\"$gt\": \"\"} work in mongo?",       # nosql
    "is 1; DROP TABLE users-- dangerous?",                     # sql stacked
    "is http://127.1/admin an internal address?",              # short-form IP
    "what about ..\\..\\..\\windows\\system32 ?",              # windows traversal
    "is {\"__proto__\":{\"x\":1}} a problem?",                 # prototype pollution
]


def test_erg_never_silences_a_new_detection():
    for s in _FRAMED_ATTACKS:
        f = analyze(s)
        ok(f.label != "clean",
           f"ERG silenced a framed attack to OK: {s!r} -> {f.label}")
