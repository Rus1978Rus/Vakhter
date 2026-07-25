# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
Hardening cards (SIMULATOR of drafts) — the "tomorrow's threats" round.

Closes the highest-severity items left on the coverage map's "missing to raise":
  #7-ext  template / expression injection: ${jndi:} (Log4Shell CVE-2021-44228),
          {{7*7}} SSTI, SpEL/OGNL, ERB with system calls
  #8      cloud-credential resource paths + private-key headers; DNS exfiltration
  #5-ext  IPv6 (bracketed) private/loopback/link-local + octal-dotted IP hosts (SSRF)

CONTEXTUAL by design so normal shell vars ${HOME}, legit templates {{ user.name }},
prose mentions of "aws", and short domains a.example.com stay clean.
"""
import re
import socket
import ipaddress
from invariant_engine.core import Finding
from invariant_engine.supplement import combine

# ---- #7-ext: template / expression injection ----
# bounded wildcards ({0,N}) so a wall of the same char can't cause O(n^2)
# backtracking (ReDoS). Real payloads are short.
_JNDI = re.compile(r"\$\{jndi:(ldap|ldaps|rmi|dns|iiop|nis|corba)\b", re.I)
_LOOKUP_URL = re.compile(r"\$\{[^}]{0,200}://")                       # lookup w/ a URL scheme
_SSTI = re.compile(
    r"\{\{[^}]{0,200}("
    r"[*/+%\-]\s*\d"                                                  # {{7*7}}
    r"|\b(config|self|request|__class__|__globals__|__mro__|application|cycler|"
    r"joiner|namespace|lipsum|subprocess|popen|os\.|system|import)\b"
    r")", re.I)
_SPEL = re.compile(r"[#$]\{[^}]{0,200}\b(T\(|getRuntime|Runtime|ProcessBuilder|exec)\b", re.I)
_ERB = re.compile(r"<%=?[^%]{0,200}\b(system|exec|eval|IO\.|File\.|open|`)\b", re.I)

# ---- #8: cloud credentials / private keys / DNS exfil ----
_CLOUD_CRED = re.compile(
    r"(\.aws/credentials|\.config/gcloud|(^|/)\.azure/|\.kube/config|"
    r"\.docker/config\.json|service[_-]?account[^\s]{0,120}\.json|"
    r"-----BEGIN [A-Z0-9 ]{0,40}PRIVATE KEY-----|(^|/)\.npmrc\b|(^|/)\.pypirc\b|(^|/)\.netrc\b)",
    re.I)
_DNS_TOOL = re.compile(r"\b(nslookup|dig|host)\s+[\w.-]+\.\w", re.I)
# NOTE: written to be LINEAR (no nested quantifier) so a wall of dots cannot
# trigger catastrophic backtracking (ReDoS). A long hex/base label, then a
# flat domain tail.
_DNS_LABEL = re.compile(r"\b([a-f0-9]{24,}|[A-Za-z0-9+/=_-]{28,})\.[a-z0-9][a-z0-9.-]{1,}\b")


def _templates(text):
    if _JNDI.search(text) or _LOOKUP_URL.search(text):
        return Finding("suspect", 0.95, "JNDI/URL lookup expression (Log4Shell-class RCE)",
                       conclusive=True, signature="jndi")
    if _SSTI.search(text) or _SPEL.search(text) or _ERB.search(text):
        return Finding("suspect", 0.9, "template/expression injection (SSTI/SpEL/ERB)",
                       conclusive=True, signature="ssti")
    return None


def _cloud(text):
    m = _CLOUD_CRED.search(text)
    if m:
        return Finding("suspect", 0.85, f"cloud-credential / private-key artifact '{m.group(0)[:40]}'",
                       conclusive=True, signature="cloud_cred")
    return None


def _dns_exfil(text):
    if _DNS_TOOL.search(text) and _DNS_LABEL.search(text):
        return Finding("suspect", 0.7, "DNS lookup of a long-label host (possible DNS exfiltration)",
                       signature="dns_exfil")
    if _DNS_LABEL.search(text):
        return Finding("suspect", 0.55, "suspiciously long DNS label (possible data-in-hostname)",
                       signature="dns_label")
    return None


# ---- execution: PowerShell encoded / LOLBins / pipe-to-shell ----
# All bounded ([^\n]{0,N}) and flat (no nested quantifier) -> linear, ReDoS-safe.
_POWERSHELL = re.compile(
    r"\b(powershell|pwsh)\b[^\n]{0,80}?("
    r"-e(nc|ncodedcommand|c)?\s+[A-Za-z0-9+/=]{8,}"           # -enc <base64> (>=8 = UTF-16LE floor)
    r"|-nop\b|-noni\b|-w\s+hidden|-windowstyle\s+hidden"      # stealth flags
    r"|iex\b|invoke-expression|frombase64string|downloadstring)", re.I)
_LOLBIN = re.compile(
    r"\b(certutil\b[^\n]{0,80}?(-urlcache|-decode|-f\s+https?:)"  # certutil download/decode
    r"|bitsadmin\b[^\n]{0,40}?/transfer"                          # bitsadmin transfer
    r"|mshta\b\s+(https?:|javascript:|vbscript:)"                 # mshta remote
    r"|regsvr32\b[^\n]{0,40}?/i:https?:"                          # regsvr32 scriptlet
    r"|rundll32\b[^\n]{0,40}?(javascript:|,\s*DllRegisterServer))", re.I)
_PIPE_SHELL = re.compile(r"\b(curl|wget)\b[^\n|]{0,200}\|\s*(sudo\s+)?(ba|z|d)?sh\b", re.I)


# ---- deserialization / SSRF schemes / prototype pollution ----
# Java serialized stream base64 starts rO0AB (magic AC ED 00 05); PHP serialized
# object is O:<len>:"Class":<n>:{ . Both are unambiguous data-format magic.
_DESERIAL = re.compile(r"\brO0AB[A-Za-z0-9+/]"          # rO0AB = base64 of the Java magic AC ED 00 05
                       r'|(?:^|[^A-Za-z0-9])O:\d{1,4}:"[^"\n]{1,80}":\d{1,4}:\{')
# Exotic URL schemes used for SSRF / protocol smuggling (gopher to Redis, dict to
# memcached, tftp/netdoc/jar). Everyday http/https/ftp/mailto are NOT here.
_SSRF_SCHEME = re.compile(r"\b(gopher|dict|tftp|netdoc|jar|ldap|ldaps)://", re.I)
# JS prototype pollution: a "__proto__" JSON key, __proto__ used as an accessor, or
# constructor[...]prototype. A bare mention "the __proto__ property" (no [ or .) is clean.
_PROTO = re.compile(r'"__proto__"|\b__proto__\s*[\[.]'
                    r"|constructor\s*\[?\s*[\"']?\s*prototype", re.I)


def _rce_misc(text):
    if _DESERIAL.search(text):
        return Finding("suspect", 0.85, "serialized-object magic (Java/PHP deserialization)",
                       conclusive=True, signature="deserialize")
    if _SSRF_SCHEME.search(text):
        return Finding("suspect", 0.85, "exotic URL scheme (SSRF / protocol smuggling)",
                       conclusive=True, signature="ssrf_scheme")
    if _PROTO.search(text):
        return Finding("suspect", 0.8, "prototype-pollution accessor (__proto__ / constructor.prototype)",
                       conclusive=True, signature="proto_pollution")
    return None


def _execution(text):
    if _POWERSHELL.search(text):
        return Finding("suspect", 0.9, "PowerShell stealth/encoded execution",
                       conclusive=True, signature="powershell_exec")
    if _LOLBIN.search(text):
        return Finding("suspect", 0.9, "living-off-the-land binary download/exec (LOLBin)",
                       conclusive=True, signature="lolbin")
    if _PIPE_SHELL.search(text):
        return Finding("suspect", 0.9, "download piped straight to a shell (curl|sh)",
                       conclusive=True, signature="pipe_to_shell")
    return None


# ---- Windows / UNC paths ----
_WIN_TRAVERSAL = re.compile(r"(?:\.\.[\\/]){2,}[\w.\\/-]*\\")   # ..\..\  (Windows backslash)
_UNC = re.compile(r"(?:^|[\s\"'(=,>])\\\\[A-Za-z0-9._-]+\\[A-Za-z0-9$._-]+")  # \\host\share


def _windows_path(text):
    if _WIN_TRAVERSAL.search(text):
        return Finding("suspect", 0.85, "Windows backslash path traversal (..\\..\\)",
                       conclusive=True, signature="win_traversal")
    if _UNC.search(text):
        # a remote SMB/UNC reference: credential-leak / lateral vector — WATCH, not
        # conclusive, since legit intranet shares exist.
        return Finding("suspect", 0.5, "UNC / SMB network path (\\\\host\\share) reference",
                       signature="unc_path")
    return None


# ---- #5-ext: IPv6 + octal IP hosts ----
def _classify_ip(ip, host):
    if ip.is_link_local:
        return Finding("suspect", 0.95, f"link-local/metadata IP host {host} (SSRF)",
                       conclusive=True, signature="ip_metadata")
    if ip.is_loopback or ip.is_private:
        return Finding("suspect", 0.9, f"internal/loopback IP host {host} (SSRF)",
                       conclusive=True, signature="ip_internal")
    if ip.is_unspecified or ip.is_reserved:
        return Finding("suspect", 0.85, f"wildcard/reserved IP host {host}",
                       conclusive=True, signature="ip_wildcard")
    return None


def _ip_advanced(text):
    # bracketed IPv6 in a URL, with an OPTIONAL zone id:  http://[::1]/  http://[fd00::1]/
    # http://[::ffff:169.254.169.254]/  http://[fe80::1%25eth0]/  (%25 = url-encoded %)
    for m in re.finditer(r"https?://\[([0-9a-fA-F:.]+)(?:(?:%25|%)[^\]]{0,40})?\]", text):
        try:
            ip = ipaddress.ip_address(m.group(1))
        except ValueError:
            continue
        # an IPv4-mapped v6 (::ffff:a.b.c.d) should be judged on the embedded v4
        mapped = getattr(ip, "ipv4_mapped", None)
        f = _classify_ip(mapped or ip, m.group(0))
        if f:
            return f
    # short-form dotted IPv4 host (inet_aton):  http://127.1/  http://10.0.1/  http://0x7f.1/
    # Gated on URL context so "version 5.1" in prose is never read as an IP.
    for m in re.finditer(r"https?://([0-9xa-fA-F]{1,10}(?:\.[0-9xa-fA-F]{1,10}){1,2})(?=[/:?#\s]|$)", text):
        host = m.group(1)
        try:
            ip = ipaddress.ip_address(socket.inet_aton(host))
        except (OSError, ValueError):
            continue
        f = _classify_ip(ip, m.group(0))
        if f:
            return f
    # octal-dotted IPv4 host:  http://0177.0.0.1/   http://0300.0250.0.1/
    for m in re.finditer(r"https?://(0[0-7]{1,}(?:\.0?[0-7]+){1,3})\b", text):
        parts = m.group(1).split(".")
        try:
            octets = [int(p, 8) for p in parts]
            if any(o > 255 for o in octets) or not (2 <= len(octets) <= 4):
                continue
            while len(octets) < 4:
                octets.insert(-1, 0)
            ip = ipaddress.ip_address(".".join(map(str, octets)))
        except ValueError:
            continue
        f = _classify_ip(ip, m.group(0))
        if f:
            return f
    return None


def harden_cards_reader(text):
    result = Finding("clean", 0.0, "harden-cards: nothing")
    for check in (_templates, _cloud, _dns_exfil, _rce_misc, _execution, _windows_path, _ip_advanced):
        f = check(text)
        if f:
            result = combine(result, f)
    return result
