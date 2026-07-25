# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
SAFE REPORT — the guard's own output is untrusted too.

Findings echo snippets of attacker input in their reason text. Check #7 showed a
card echoing raw ANSI escapes into the reason — which would hijack an admin
terminal / log / dashboard. The verdict is correct; only the DISPLAY text is the
hazard. So the boundary where a verdict is shown or logged must sanitize it.

sanitize(): control characters (incl. ANSI ESC) become visible inert escapes;
HTML metacharacters become entities; length is capped. safe_view() returns the
admin-facing view with reason and signature already sanitized.
"""
import html

_KEEP = ("\t",)


def sanitize(s, limit=300):
    if not isinstance(s, str):
        s = str(s)
    out = []
    for ch in s:
        o = ord(ch)
        if (o < 32 and ch not in _KEEP) or o == 127:
            out.append(f"\\x{o:02x}")          # control char -> visible & inert
        else:
            out.append(ch)
    cleaned = html.escape("".join(out), quote=True)   # < > & " ' -> entities
    if len(cleaned) > limit:
        cleaned = cleaned[:limit] + "…"
    return cleaned


def safe_view(finding):
    """Admin-facing, display-safe view of a verdict — safe for terminal/log/HTML."""
    risk = ("OK" if finding.label == "clean"
            else "ALARM" if finding.conclusive else "WATCH")
    return {"risk": risk,
            "reason": sanitize(finding.reason),
            "signature": sanitize(finding.signature or "")}
