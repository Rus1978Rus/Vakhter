# -*- coding: utf-8 -*-
"""
combine() monotonicity + order-independence lock (external conveyor, M4; AD-34).

The integrator must NEVER lower a verdict, and its output must not depend on the
order readers happen to run in. Two measured defects are pinned here:

  C1  same reason, the LOSING finding is conclusive -> the earlier short-circuit
      dropped conclusive True->False (a hard ALARM silently softened);
  C2  that drop was order-dependent: combine(a,b) != combine(b,a);
  C3  on a rank tie a specific/conclusive finding was masked behind a generic
      one that merely came first among the readers.
"""
from _support import ok

from invariant_engine.core import Finding
from invariant_engine.supplement import combine


def test_conclusive_is_never_dropped_same_reason():
    lo_conclusive = Finding("suspect", 0.85, "same reason", conclusive=True)
    hi_soft = Finding("suspect", 1.0, "same reason", conclusive=False)
    ok(combine(hi_soft, lo_conclusive).conclusive,
       "a conclusive verdict must survive combine even on a same-reason tie")


def test_combine_is_order_independent_for_conclusive():
    a = Finding("suspect", 1.0, "same reason", conclusive=False)
    b = Finding("suspect", 0.85, "same reason", conclusive=True)
    ok(combine(a, b).conclusive == combine(b, a).conclusive == True,
       "combine must be commutative in the hard-verdict flag (no reader-order dependence)")


def test_conclusive_or_across_any_reasons():
    # different reasons, loser conclusive: still must be conclusive both ways
    a = Finding("suspect", 1.0, "generic reason", conclusive=False)
    b = Finding("suspect", 0.85, "specific reason", conclusive=True)
    ok(combine(a, b).conclusive and combine(b, a).conclusive,
       "conclusive is the OR of both inputs in every branch")


def test_specific_signature_wins_a_tie():
    generic = Finding("suspect", 1.0, "generic", conclusive=False, signature="")
    specific = Finding("suspect", 0.85, "SPECIFIC rce", conclusive=True, signature="rce")
    ok(combine(generic, specific).signature == "rce",
       "a conclusive, signatured finding must be the headline on a tie, not the "
       "generic one that came first")
    ok(combine(specific, generic).signature == "rce",
       "and that is order-independent")


def test_clean_never_raises_a_verdict():
    clean = Finding("clean", 0.0, "nothing")
    real = Finding("suspect", 0.7, "real thing", conclusive=False, signature="x")
    r = combine(real, clean)
    ok(r.label == "suspect" and not r.conclusive and r.signature == "x",
       "combining with a clean finding must not invent conclusiveness or change the finding")
