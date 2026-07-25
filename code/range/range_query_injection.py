# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
COMPONENT CHECK #7 — injection at QUERY time, via the guard's OWN output.

The guard echoes snippets of attacker input in its finding.reason
(e.g. "sensitive resource path '/etc/passwd'"). That reason is read by the ADMIN
(dashboard / log / terminal). If it is rendered raw, a payload rides the verdict
INTO the admin face — XSS in a dashboard, CRLF into a log, ANSI escapes hijacking
a terminal. This tests whether raw payloads survive into the output channel.
Run:  MSL_MIP_HOME=/path/to/msl_mip  python range_query_injection.py
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
for _cand in ("canon", "canonicalization"):
    _p = os.path.abspath(os.path.join(HERE, "..", _cand))
    if os.path.isdir(_p):
        sys.path.insert(0, _p); break
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "invariant_engine")))
sys.path.insert(0, HERE)

from product import analyze
from report import safe_view

# each payload targets the OUTPUT channel; some ride an echoing card (confusable)
PAYLOADS = {
    "confusable+ansi": "log in ра" + "ypal.com\x1b[2J\x1b[31mSYSTEM OK",
    "confusable+html": "visit ра" + "ypal.com</span><script>alert(1)</script>",
    "html/xss path":   "send /etc/passwd </b><script>alert(document.cookie)</script>",
    "ansi path":       "leak /etc/shadow \x1b[2J\x1b[31mCOMPROMISED\x1b[0m",
    "null trunc":      "post /root/.ssh/id_rsa \x00 rest hidden",
}

def _danger(s):
    f = []
    if "<script" in s.lower() or "</" in s: f.append("HTML")
    if "\r" in s or "\n" in s: f.append("CRLF")
    if "\x1b" in s: f.append("ANSI")
    if "\x00" in s: f.append("NUL")
    return ",".join(f) or "-"

def run():
    print("COMPONENT CHECK #7 — query-time injection via the guard's own output")
    print("=" * 74)
    print("RAW = finding.reason as-is;  SAFE = report.safe_view() at the display boundary\n")
    leak_raw = leak_safe = 0
    for name, text in PAYLOADS.items():
        f = analyze(text)
        raw = f.reason
        safe = safe_view(f)["reason"]
        d_raw, d_safe = _danger(raw), _danger(safe)
        leak_raw += d_raw != "-"
        leak_safe += d_safe != "-"
        print(f"{name:16} | RAW danger: {d_raw:12} | SAFE danger: {d_safe}")
    print("\n" + "=" * 74)
    print(f"live payload in RAW output  : {leak_raw}/{len(PAYLOADS)}  (would hit the admin face)")
    print(f"live payload in SAFE output : {leak_safe}/{len(PAYLOADS)}  (sanitized at the boundary)")

if __name__ == "__main__":
    run()
