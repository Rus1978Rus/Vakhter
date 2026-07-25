# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
Gate self-test — proves the two quality gates are REAL, not false greens.

Discipline adopted from msl_mip's acceptance-gate / shadow-oracle work
(D-GUARD-DESIGN P3 mutation-adequacy + guard_shadow_oracle properties):
a gate you cannot fail is not a gate. So we inject known breakage and assert
each gate CATCHES it, plus we assert the gates stay clean / pure / crash-free
on good and hostile input.

Part A — VALIDATOR mutation-adequacy (validate_per_sign):
  take a real committed card, inject one defect at a time, assert validate_file
  reports an error for each. A negative control (unmutated card) must pass.

Part B — SIMULATOR robustness (simulate_cards.verdict):
  purity (same input -> same verdict), identity-on-clean (benign -> OK),
  exception-containment (hostile/degenerate input never raises).

Run:  python3 code/tools/gate_selftest.py
Exit 0 = both gates proven real & robust; exit 1 = a gate is a false green
or crashes (a finding to fix in OUR tooling — msl_mip is read-only).
"""
import os, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import validate_per_sign as V
import simulate_cards as S

CARDS = V.CARDS
GOOD = os.path.join(CARDS, "SIGN_CORE_CARD_QUOTATION_MARK_U0022_GEN3_v0_3_EN.md")


def _validate_text(text):
    """Write text to a temp *_EN.md and run validate_file; return (errs, warns)."""
    fd, path = tempfile.mkstemp(suffix="_EN.md", dir=os.environ.get(
        "TMPDIR", tempfile.gettempdir()))
    os.close(fd)
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        _c, errs, warns = V.validate_file(path)
        return errs, warns
    finally:
        os.remove(path)


# ---- injected validator defects: (name, mutation) -> each MUST produce an error ----
def _mut_drop_what_is_not(t):
    # remove items 3..12 -> WHAT_IS_NOT count drops to 2, well below the min of 10
    # (robust regardless of how many items the source card happens to carry)
    import re
    return re.sub(r"^\s*(?:[3-9]|1[0-2])\.\s+NOT_.*\n", "", t, flags=re.M)

def _mut_break_two_confusables(t):
    # break two CONFUSABLE_00N: labels -> CONFUSABLE set drops below the min of 5
    return t.replace("CONFUSABLE_005:", "CONFUSABLE_ZZ5:").replace(
        "CONFUSABLE_004:", "CONFUSABLE_ZZ4:")

def _mut_placeholder(t):
    # leftover template placeholder must be caught
    return t.replace("DISPLAY_NAME:", "DISPLAY_NAME: <official name>", 1)

def _mut_fake_confusable_codepoint(t):
    # point a confusable at an unassigned codepoint (no UCD name, not a control)
    import re
    return re.sub(r"(CONFUSABLE_001:\n\s*VISIBLE_FORM:.*\n\s*CODEPOINT:\s*)U\+[0-9A-Fa-f]+",
                  r"\1U+FFFFF", t, count=1)

def _mut_adversarial_undercount(t):
    return t.replace("ACTUAL_TOTAL_VECTORS: 10", "ACTUAL_TOTAL_VECTORS: 5")


VALIDATOR_MUTATIONS = [
    ("MUT-V1 drop WHAT_IS_NOT below min", _mut_drop_what_is_not),
    ("MUT-V2 break CONFUSABLE below min", _mut_break_two_confusables),
    ("MUT-V3 leftover placeholder", _mut_placeholder),
    ("MUT-V4 fake confusable codepoint", _mut_fake_confusable_codepoint),
    ("MUT-V5 adversarial undercount", _mut_adversarial_undercount),
]


def test_validator_negative_control():
    """The unmutated good card must pass (gate is not always-red)."""
    good = open(GOOD, encoding="utf-8").read()
    errs, _warns = _validate_text(good)
    assert not errs, "negative control failed: good card produced %r" % errs


def test_validator_mutation_adequacy():
    """Every injected defect must be caught by the validator."""
    good = open(GOOD, encoding="utf-8").read()
    for name, mut in VALIDATOR_MUTATIONS:
        mutated = mut(good)
        assert mutated != good, "%s did not change the card" % name
        errs, _warns = _validate_text(mutated)
        assert errs, "%s NOT caught (false green)" % name


def test_simulator_verdict_purity():
    """verdict() is a pure function: same input -> same output, order-independent."""
    a, b = 'attr="value"', "cn=*)(uid=*"
    assert S.verdict(a) == S.verdict(a)
    va1, vb1 = S.verdict(a), S.verdict(b)
    vb2, va2 = S.verdict(b), S.verdict(a)          # reversed order, no shared state
    assert va1 == va2 and vb1 == vb2


def test_simulator_identity_on_clean():
    """Genuinely benign strings must stay OK (no false alarms on plain text)."""
    for t in ("hello world", "cafe resume naive", "", "3 + 4 = 7",
              "Procter & Gamble", "a b c 123", "voila"):
        assert S.verdict(t) == "OK", "false alarm on %r" % t


def test_simulator_exception_containment():
    """Hostile / degenerate input must never raise — the gate must fail visible,
    not crash (msl_mip P2ii)."""
    for t in ("\ud800", "\udfff", "\x00\x01\x02", "\U000e0065" * 50,
              "‮" * 30, "​" * 200, "%00" * 100):
        try:
            v = S.verdict(t)
        except Exception as e:                     # noqa: BLE001
            raise AssertionError("verdict raised on %r: %s" % (t, e))
        assert v in ("OK", "WATCH", "ALARM"), "bad verdict %r on %r" % (v, t)


def main():
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    failed = 0
    print("GATE SELF-TEST (validator mutation-adequacy + simulator robustness)")
    print("=" * 68)
    for t in tests:
        try:
            t()
            print("OK  ", t.__name__)
        except AssertionError as e:
            failed += 1
            print("FAIL", t.__name__, "->", e)
    print("-" * 68)
    print("%d/%d passed" % (len(tests) - failed, len(tests)))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
