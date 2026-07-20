# -*- coding: utf-8 -*-
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
    # bracketed IPv6 in a URL:  http://[::1]/  http://[fd00::1]/  http://[::ffff:169.254.169.254]/
    for m in re.finditer(r"https?://\[([0-9a-fA-F:.]+)\]", text):
        try:
            ip = ipaddress.ip_address(m.group(1))
        except ValueError:
            continue
        # an IPv4-mapped v6 (::ffff:a.b.c.d) should be judged on the embedded v4
        mapped = getattr(ip, "ipv4_mapped", None)
        f = _classify_ip(mapped or ip, m.group(0))
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
    for check in (_templates, _cloud, _dns_exfil, _ip_advanced):
        f = check(text)
        if f:
            result = combine(result, f)
    return result
