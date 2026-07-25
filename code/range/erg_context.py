# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
ERG / context layer (SIMULATOR) — the "does the threat survive coarse-graining?"
pass. MSL says what a SIGN is; ERG-context asks whether the FRAME around it
corroborates operational intent, or whether the sign dissolves into a mention /
explanation when you zoom out.

SAFETY CONTRACT (hardened after a 5-reviewer conveyor review, wf_19f3b960):
  1. It acts only on a `suspect` finding whose signature is an MSL-core ACTION.
     The operational drafted cards (sqli, jndi, homoglyph, ip_metadata,
     zw_wordsplit, cloud_cred, …) carry their own signatures and are IMMUNE.
  2. A conclusive ALARM may be softened at most ONE notch (ALARM -> WATCH) inside
     a benign frame — never cleared to OK.
  3. A non-conclusive WATCH is cleared to OK ONLY by MASK-AND-RESCAN proof: the
     benign STRUCTURE (git@host, ${VAR}, {{ident}}) is removed and the rest is
     re-scanned; it clears ONLY if what remains is clean — i.e. the benign
     structure was the SOLE cause of the flag. Any hidden payload survives the
     mask, keeps the rescan dirty, and blocks the clear.
  4. It never raises severity.

WHY (3) replaces the old denylist: the previous version cleared a WATCH to OK
whenever an allowlist (`_OPERATIONAL`) failed to recognise the content as
operational. That denylist was strictly narrower than what MSL flags, so crafted
MSL-flagged threats reached OK inside an attacker-chosen frame — data: URIs (live
XSS / PE dropper), backslash `..\\..` traversal, `~/.git-credentials` recon,
`chmod 777 /etc`. Mask-and-rescan is a POSITIVE proof bound to the flagged signal,
not a denylist, so it cannot be evaded by an unlisted carrier or an injected frame
word: removing `git@host` from "git@x:y ..\\..\\sam" leaves the traversal, which
MSL still flags, so it stays WATCH.
"""
import re
from invariant_engine.core import Finding

# broad presence verdicts from MSL core (msl_real maps action -> signature)
MSL_ACTION_SIGS = {"pass", "log_only", "queue_for_review",
                   "hold_pending_review", "escalate_to_human"}

_INTERROG = re.compile(
    r"\b(how|what|why|when|which|who|where|is|are|does|do|can|could|should|"
    r"would|explain|describe|difference between)\b", re.I)
_DEFINE = re.compile(
    r"(is the code for|is the escape|stands for|shorthand for|refers to|"
    r"is called|represents the|for example|e\.g\.|such as|"
    r"means (a|the|that)|is a (code|character|token|symbol|placeholder|convention))",
    re.I)
_SSH = re.compile(r"\b(git|hg|svn)@[\w.-]+\.[a-z]{2,}:[\w~./-]+", re.I)   # git@host:path
_SHELLVAR = re.compile(r"\$\{[A-Za-z_][A-Za-z0-9_]*\}")                   # ${HOME}
_TEMPLATE_VAR = re.compile(r"\{\{\s*[\w.]+\s*\}\}")                       # {{ title }}


def _benign_frame(text):
    t = text.strip()
    if t.endswith("?") and _INTERROG.search(t):
        return "interrogative"
    if _DEFINE.search(text):
        return "definitional"
    if _SSH.search(text) or _SHELLVAR.search(text) or _TEMPLATE_VAR.search(text):
        return "legit-structure"
    return None


def _mask_benign(text):
    """Remove the benign structural tokens so we can test whether they were the
    SOLE cause of the flag."""
    masked = _SSH.sub(" ", text)
    masked = _SHELLVAR.sub(" ", masked)
    masked = _TEMPLATE_VAR.sub(" ", masked)
    return masked


_RESCAN = None
def _default_rescan():
    """Lazy readers-only pipeline (MSL + cards, NO erg) for the mask-and-rescan
    proof. Cached. Never recurses into erg_context."""
    global _RESCAN
    if _RESCAN is None:
        from canonicalize import canonicalize
        from invariant_engine.msl_real import real_text_reader
        from invariant_engine.supplement import supplement_reader, combine
        from digit_cards import digit_cards_reader
        from metachar_cards import metachar_cards_reader
        from invisible_cards import invisible_cards_reader
        from harden_cards import harden_cards_reader
        from fail_closed import safe_reader
        readers = [("msl", real_text_reader), ("supplement", supplement_reader),
                   ("digit", digit_cards_reader), ("metachar", metachar_cards_reader),
                   ("invisible", invisible_cards_reader), ("harden", harden_cards_reader)]

        def rescan(t):
            c = canonicalize(t)[0]
            f = None
            for n, r in readers:
                g = safe_reader(n, r, c)
                f = g if f is None else combine(f, g)
            return f
        _RESCAN = rescan
    return _RESCAN


def erg_context(text, finding, rescan=None):
    """Return a possibly-softened finding. Never escalates. Clears an MSL-flagged
    WATCH to OK only when mask-and-rescan proves the benign structure was the sole
    cause; softens a conclusive ALARM to WATCH at most."""
    if finding.label != "suspect":
        return finding
    if finding.signature not in MSL_ACTION_SIGS:
        return finding                       # operational detector — immune
    frame = _benign_frame(text)
    if not frame:
        return finding
    if finding.conclusive:                    # ALARM -> WATCH at most, never OK
        return Finding("suspect", 0.4,
            f"context-softened ALARM->WATCH ({frame} frame; MSL-flagged, never cleared to OK)",
            conclusive=False, signature="ctx_soft")
    # non-conclusive WATCH: clear to OK ONLY if a legit STRUCTURE is the sole cause
    if frame == "legit-structure":
        masked = _mask_benign(text)
        if masked != text:
            scan = (rescan or _default_rescan())(masked)
            if scan.label == "clean":
                return Finding("clean", 0.0,
                    "context-cleared: benign structure is the sole cause "
                    "(mask-and-rescan of the remainder is clean)",
                    signature="ctx_clear")
    return finding                            # otherwise keep the WATCH
