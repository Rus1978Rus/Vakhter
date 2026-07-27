# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
Metacharacter detector cards (SIMULATOR of drafts) — closes coverage point #7.

The pre-pass REVEALS the dangerous sign (%27->' , %60->` , %7c->| , %3c-><,
%00, %0d%0a); these cards are the missing DETECTORS. They are CONTEXTUAL
(pattern, not bare presence) so normal apostrophes / math a<b / markdown
`code` / tables a|b / multiline text stay clean.
"""
import re
from invariant_engine.core import Finding
from invariant_engine.supplement import combine

_SQL   = re.compile(r"'(\s*(or|and|union|select|drop|insert)\b|\s*--|\s*#|\s*;|\s*=\s*')"
                    r"|(\bor\b|\band\b)\s+'?\d+'?\s*=\s*'?\d+"
                    # stacked query: ; then an unambiguous DDL/DML verb+object
                    r"|;\s*(drop\s+(table|database)|delete\s+from|insert\s+into|"
                    r"update\s+\w+\s+set|truncate\s+table|alter\s+table|exec(ute)?\s*[\s(])", re.I)
# bounded wildcards ({0,N}) so a wall of the same char can't cause O(n^2)
# backtracking (ReDoS). Real payloads are short.
_BTICK = re.compile(r"`[^`]{0,200}\b(id|whoami|cat|ls|rm|curl|wget|nc|bash|sh|uname|env|ping|nslookup)\b[^`]{0,200}`"
                    r"|\$\(", re.I)
_SHELL = re.compile(r"[|;&][ \t]{0,8}\b(nc|bash|sh|curl|wget|rm|cat|python|perl|whoami|id|"
                    r"nslookup|powershell|cmd|telnet)\b", re.I)
_XSS   = re.compile(r"<[ \t]{0,8}(script|iframe|svg|img|body|object|embed|link)\b"
                    r"|javascript:|on(error|load|click|mouseover|focus)[ \t]{0,8}=", re.I)
_CRLF  = re.compile(r"[\r\n][ \t]{0,16}(set-cookie|location|content-length|content-type|host|"
                    r"x-forwarded-for)[ \t]{0,16}:", re.I)
# LDAP filter injection — only the LDAP-specific shapes, so ordinary ")(" in code
# / math never trips it: the wildcard-paren break "*)(", boolean chaining ")(&(" /
# ")(|(", or an LDAP attribute wildcarded "(uid=*".
_LDAP  = re.compile(r"\*\s*\)\s*\("
                    r"|\)\s*\(\s*[&|]\s*\("
                    r"|\(\s*(uid|cn|mail|sn|givenname|objectclass|memberof|samaccountname)"
                    r"\s*=\s*\*", re.I)
# NoSQL (Mongo) operator injection — only a QUOTED key "$op" (as in {"$gt":""}) or
# a bracketed param [$op] (as in user[$ne]=1); a bare "$where" in prose stays clean.
_NOSQL = re.compile(r'"\$(gt|gte|lt|lte|ne|eq|nin|in|or|and|nor|not|where|regex|expr|'
                    r'exists|elemmatch|mod|all|type)"'
                    r"|\[\s*\$(gt|gte|lt|lte|ne|eq|nin|in|where|regex|exists)\s*\]", re.I)

# Control codepoints that do not belong in text shown to a model: C0 (U+0000–1F)
# and C1 (U+0080–9F) plus DEL (U+007F). Excludes the ordinary whitespace controls
# tab/LF/CR/VT/FF (the whitespace card owns those) and NUL (flagged above with its
# own signature). NEL (U+0085) is a line break in some parsers (header/log
# injection), CSI (U+009B) a terminal escape, ESC (U+001B) a terminal control,
# DEL a parser disruptor — the digit-card R7-3/R8-2/R9-1 carrier class.
_CTRL = ((set(range(0x00, 0x20)) | {0x7F} | set(range(0x80, 0xA0)))
         - {0x00, 0x09, 0x0A, 0x0B, 0x0C, 0x0D})


def metachar_cards_reader(text):
    res = Finding("clean", 0.0, "metachar: nothing")

    def hit(sev, reason, sig, conclusive=True):
        return combine(res, Finding("suspect", sev, reason, conclusive=conclusive, signature=sig))

    if "\x00" in text:
        res = hit(0.9, "NULL byte in input (parser truncation / filter bypass)", "null_byte")
    ctrl = sorted({ord(c) for c in text if ord(c) in _CTRL})
    if ctrl:
        names = ", ".join(f"U+{c:04X}" for c in ctrl[:4]) + ("…" if len(ctrl) > 4 else "")
        res = hit(0.8, f"control character(s) invalid in text ({names}) — NEL/CSI/"
                  f"ESC/DEL class (line / terminal / parser injection)", "control_char")
    if _CRLF.search(text):
        res = hit(0.9, "CRLF followed by a header name (header/log injection)", "crlf")
    if _XSS.search(text):
        res = hit(0.9, "HTML script/handler pattern (XSS)", "xss")
    if _SQL.search(text):
        res = hit(0.85, "quote + SQL operator pattern (SQL injection)", "sqli")
    if _BTICK.search(text) or _SHELL.search(text):
        res = hit(0.9, "shell command-substitution / chaining pattern (command injection)", "cmdi")
    if _LDAP.search(text):
        res = hit(0.85, "LDAP filter metacharacter pattern (LDAP injection)", "ldapi")
    if _NOSQL.search(text):
        res = hit(0.85, "NoSQL operator in a query position (NoSQL injection)", "nosqli")
    return res
