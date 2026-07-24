# -*- coding: utf-8 -*-
"""
Smoke test for the applications/ demos — catches the "built but not connected"
class of defect automatically (external audit H1: ai_gateway's import paths
pointed at applications/range instead of code/range, so the flagship demo raised
ModuleNotFoundError while the docs told users to run it).

Each app is run as a subprocess; a clean exit (no import error / no crash) is the
contract. The guard is fail-closed, so these complete with or without an external
MSL present.
"""
import os
import subprocess
import sys

from _support import ok

_REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
_APPS = [
    "applications/ai_gateway/ai_gateway.py",
    "applications/notarius_data/notarius_ledger.py",
    "applications/erg_fraud/erg_fraud.py",
]


def _run(rel):
    p = subprocess.run([sys.executable, os.path.join(_REPO, rel)],
                       capture_output=True, text=True, timeout=120)
    return p.returncode, (p.stderr or "")


def test_apps_run_without_import_error():
    for rel in _APPS:
        rc, err = _run(rel)
        ok("ModuleNotFoundError" not in err and "ImportError" not in err,
           f"{rel}: import error\n{err[-400:]}")
        ok(rc == 0, f"{rel}: non-zero exit {rc}\n{err[-400:]}")
