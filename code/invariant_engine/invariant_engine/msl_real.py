# SPDX-License-Identifier: LicenseRef-Proprietary
"""
REAL MSL adapter — bridges the invariant engine to the actual msl_mip runtime.

This is NOT a stub. It imports the user's real `msl_mip_runtime.py` (with its
core/single_sign/sequence modules and sign cards) and maps its verdict into the
engine's Finding contract.

The real MSL is a whole project, not one file, so this adapter *locates* the
installed msl_mip repo rather than copying it. Point it at the repo via:
  - env  MSL_MIP_HOME=/path/to/msl_mip     (preferred), or
  - run from inside the repo, or
  - it searches a few sensible candidates.

MSL action severity (from the runtime): pass < log_only < queue_for_review
< hold_pending_review < escalate_to_human.
"""
import os
import sys
import io
import contextlib

_rt = None
_CARDS = None
_SEV = None

# When MSL says "pass" but flags an uncarded invisible (attention=WITNESS_PRESENT),
# that is a POINTER to review, not a conclusion of malice — MSL cannot tell a
# Trojan-Source RLO from a legit ❤️ emoji, because a witness is presence, not
# context. So the adapter DELEGATES invisible judgment to the contextual
# invisible-cards layer and does not itself block on a bare witness.
# Set True only to reproduce the old (over-blocking) behaviour for A/B demos.
WITNESS_CONCLUSIVE = False


def _locate_repo():
    cands = []
    if os.environ.get("MSL_MIP_HOME"):
        cands.append(os.environ["MSL_MIP_HOME"])
    # walk up from cwd looking for the runtime
    d = os.getcwd()
    for _ in range(6):
        cands.append(d)
        d = os.path.dirname(d)
    cands.append("/home/user/msl_mip")
    for c in cands:
        if c and os.path.exists(os.path.join(c, "msl_mip_runtime.py")):
            return c
    raise ImportError(
        "msl_mip_runtime.py not found. Set MSL_MIP_HOME to the msl_mip repo path.")


def _boot():
    """Import the real runtime once, load cards once, silence load-time chatter."""
    global _rt, _CARDS, _SEV
    if _rt is not None:
        return
    repo = _locate_repo()
    for p in (repo, os.path.join(repo, "core"),
              os.path.join(repo, "single_sign"), os.path.join(repo, "sequence")):
        if p not in sys.path:
            sys.path.insert(0, p)
    with contextlib.redirect_stdout(io.StringIO()):   # hush PSL/TLD/load warnings
        import msl_mip_runtime as rt
        cards = rt.load_all_cards()
    _rt, _CARDS, _SEV = rt, cards, rt._SEVERITY


def real_text_reader(subject: str):
    """subject (text / prompt / code) -> engine Finding, via the REAL MSL."""
    from .core import Finding
    _boot()
    with contextlib.redirect_stdout(io.StringIO()):    # analyze() is quiet, but be safe
        report = _rt.analyze(subject, _CARDS)

    action = report.get("effective_action", "pass")
    sev = _SEV.get(action, 0)
    witness = report.get("attention_status") == "WITNESS_PRESENT"
    integ = report.get("integrity_status", "OK")

    # A bare witness (MSL action == pass, an uncarded invisible present) is a
    # pointer, not a verdict. Unless we are reproducing the legacy behaviour,
    # return clean here and let the contextual invisible-cards layer decide —
    # it can distinguish a word-splitting smuggle from legit emoji/bidi glue.
    if sev == 0 and integ == "OK":
        if witness and WITNESS_CONCLUSIVE:
            inv = report.get("uncarded_invisibles") or []
            cps = ", ".join(sorted({f"U+{ord(w.get('char','')):04X}"
                                    for w in inv if w.get('char')})) or "invisible"
            return Finding("suspect", 0.5,
                           f"MSL verdict: {action}; invisible/uncarded char present ({cps})",
                           conclusive=True, signature=action)
        return Finding("clean", 0.0, "MSL: pass (no structural risk)")

    bits = [f"MSL verdict: {action}"]
    if witness:
        inv = report.get("uncarded_invisibles") or []
        cps = ", ".join(sorted({f"U+{ord(w.get('char','')):04X}"
                                for w in inv if w.get('char')})) or "invisible"
        bits.append(f"invisible/uncarded char present ({cps})")
    if integ != "OK":
        bits.append(f"integrity {integ}")
    reason = "; ".join(bits)

    # conclusive on its own only when MSL itself escalates hard (hold/escalate)
    # or reports a broken integrity state — never on a bare invisible witness.
    conclusive = sev >= 3 or integ != "OK"
    return Finding("suspect", round(sev / 4.0, 3) or 0.4, reason,
                   conclusive=conclusive, signature=action)


def real_plus_reader(subject: str):
    """Real MSL  +  engine structural supplement (severity-max). Core untouched."""
    from .supplement import supplement_reader, combine
    return combine(real_text_reader(subject), supplement_reader(subject))


def probe(strings):
    """Utility: print the real MSL verdict for each string (for calibration)."""
    _boot()
    out = []
    for s in strings:
        with contextlib.redirect_stdout(io.StringIO()):
            r = _rt.analyze(s, _CARDS)
        out.append((s, r.get("effective_action"), r.get("attention_status"),
                    r.get("integrity_status")))
    return out
