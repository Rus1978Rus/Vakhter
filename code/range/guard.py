# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
SELF-DEFENSE for the analyzer — so the guard itself cannot be drowned.

Two layers, cheap first then a hard guarantee:

  A) self_defense(text) — CHEAP, BOUNDED pre-checks that bounce obvious floods
     in well under a millisecond and label them as attacks:
       1. oversized input           -> WATCH  "held, chunk upstream"
       2. invisible-character flood  -> ALARM  (100+ hidden chars: not a message)
       3. single-character flood      -> ALARM  (one char >40%: a wall of '/' or '.'
                                        meant to drive per-sign analysis into O(n^2))

  B) guarded_analyze(text, pipeline, budget) — a wall-clock BUDGET around the
     analysis. IMPORTANT, measured honestly: this in-process (signal) budget
     reliably stops code WE control (our regex cards, loops) — but the real MSL
     core has broad exception handling that SWALLOWS the interrupt, so it does
     NOT stop a slow MSL call. That is why MSL's costliest sign ('/') is also
     capped in the cheap pre-check above (predict-and-hold). The production-grade
     guarantee against any slow third-party code is a WORKER/SUBPROCESS timeout
     that can be killed from outside; the signal budget here is the single-thread
     stand-in for it.

Every pre-check is O(1) or one bounded O(n) pass, so the gate cannot itself be
turned into the DoS.
"""
import signal
from invariant_engine.core import Finding

MAX_LEN     = 128_000     # deep analysis beyond this is refused (chunk upstream).
                          # Lowered from 200k after the full detector stack (incl. the
                          # wired confusable reader) was measured: worst-case clean
                          # input costs ~5us/char, so 128k keeps the whole pipeline at
                          # ~0.6s — a comfortable margin under BUDGET_S even on a slow
                          # host. A sign-in-context input is never this large anyway.
INVIS_CAP   = 128         # more hidden chars than this = a flood, not a message
DOM_RATIO   = 0.40        # one char making up >40% of a real message = flood
DOM_MIN_LEN = 500         # ...only judged once the input is long enough to matter
SLASH_CAP   = 1500        # '/' is MSL's costliest sign; hold clear bulk before MSL
BUDGET_S    = 1.5         # wall-clock ceiling (stops OUR code; MSL needs a worker)

_INVIS = (set(range(0x200B, 0x2010)) | {0x2060, 0xFEFF, 0x00AD} |
          set(range(0x202A, 0x202F)) | set(range(0x2066, 0x206A)) |
          set(range(0xFE00, 0xFE10)))
def _is_invis(o):
    return o in _INVIS or 0xE0000 <= o <= 0xE007F or 0xE0100 <= o <= 0xE01EF


def self_defense(text):
    """Cheap bounded pre-checks. Return an early Finding on abuse, else None."""
    n = len(text)                                    # O(1)
    if n > MAX_LEN:
        return Finding("suspect", 0.5,
            f"oversized input ({n} chars > {MAX_LEN}) — held, chunk upstream",
            conclusive=False, signature="oversize")
    invis = 0
    freq = {}
    for ch in text:                                  # bounded to MAX_LEN
        o = ord(ch)
        if _is_invis(o):
            invis += 1
            if invis > INVIS_CAP:
                return Finding("suspect", 0.9,
                    f"invisible-character flood (>{INVIS_CAP} hidden chars) — "
                    f"abnormal for any real message",
                    conclusive=True, signature="invis_flood")
        freq[ch] = freq.get(ch, 0) + 1
    if n >= DOM_MIN_LEN:
        ch, cnt = max(freq.items(), key=lambda kv: kv[1])
        if cnt / n > DOM_RATIO and not ch.isspace():
            return Finding("suspect", 0.85,
                f"single-character flood: {cnt}/{n} ({cnt*100//n}%) are {ch!r} — "
                f"parser-exhaustion attempt",
                conclusive=True, signature="char_flood")
    # predict-and-hold: '/' is MSL's costliest sign (~O(n^2)); a message with
    # thousands of them is bulk to chunk, and MSL swallows in-process interrupts,
    # so we hold BEFORE handing it to MSL rather than relying on the budget.
    if freq.get("/", 0) > SLASH_CAP:
        return Finding("suspect", 0.5,
            f"too many '/' ({freq['/']}) — held, chunk upstream (bulk, not deep-analyzed)",
            conclusive=False, signature="too_complex")
    return None


class _Budget(Exception):
    pass


def guarded_analyze(text, pipeline, budget_s=BUDGET_S):
    """Full guard: cheap pre-checks, then the pipeline under a hard time budget.
    `pipeline` is a callable text -> Finding. Boot/warm-up must happen before
    calling this (in production, at startup)."""
    early = self_defense(text)
    if early is not None:
        return early

    def _h(_s, _f):
        raise _Budget()
    old = signal.signal(signal.SIGALRM, _h)
    signal.setitimer(signal.ITIMER_REAL, budget_s)
    try:
        return pipeline(text)
    except _Budget:
        return Finding("suspect", 0.5,
            f"analysis budget ({budget_s}s) exceeded — held for review",
            conclusive=False, signature="budget_exceeded")
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, old)
