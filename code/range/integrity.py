# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
COMPONENT INTEGRITY — the conveyor discipline, enforced in code.

Check #4 proved a fake CARD is harmless (add-only) but a fake INTEGRATOR or a
fake ERG can silently lower a verdict. Those are the trusted core. This module
is the load-time gate: every component is checked against a manifest of
author-approved hashes. Anything MISSING, TAMPERED, or UNKNOWN -> the guard
refuses to run (fail-closed). No component enters the guard that the author's
conveyor did not close and sign.

Flow:
  - author, after closing components through the conveyor, runs build_manifest()
    and SIGNS the result (signing key out of scope here; store the manifest with
    a detached signature).
  - at startup the guard runs verify(); it serves ONLY if ok is True.
"""
import hashlib
import os

CRITICAL = {"integrator", "erg"}   # components that can LOWER a verdict


def file_hash(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def build_manifest(files):
    """files: {name: path} -> {name: sha256}. Author runs this, then signs it."""
    return {name: file_hash(p) for name, p in files.items()}


def verify(manifest, files):
    """Return (ok, report). ok is True only if every manifested component is
    present and unchanged AND nothing outside the manifest is being loaded.
    A single failure in a CRITICAL component is enough to refuse service."""
    report = []
    ok = True
    for name, expected in manifest.items():
        p = files.get(name)
        if not p or not os.path.exists(p):
            report.append((name, "MISSING")); ok = False; continue
        actual = file_hash(p)
        if actual != expected:
            report.append((name, "TAMPERED")); ok = False
        else:
            report.append((name, "ok"))
    for name in files:
        if name not in manifest:
            report.append((name, "UNKNOWN (not in manifest)")); ok = False
    return ok, report


def refuse_reason(report):
    """Human summary of why the guard refuses to start (empty if all ok)."""
    bad = [(n, s) for n, s in report if s != "ok"]
    if not bad:
        return ""
    crit = [n for n, s in bad if n in CRITICAL]
    head = "REFUSE TO START (fail-closed): "
    head += "trusted-core failure — " if crit else "component integrity failure — "
    return head + ", ".join(f"{n}:{s}" for n, s in bad)
