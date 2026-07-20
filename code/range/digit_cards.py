# -*- coding: utf-8 -*-
"""
Digit-card SIMULATOR — runs the drafted digit-card SURFACE logic as code.
(The real cards are WORKING_DRAFT, not loaded into msl_mip; this exercises
their detection so we can measure before/after empirically.)

Three checks, matching the drafts:
  A) digit-as-letter homoglyph brand mimicry   (paypa1, g00gle, micr0s0ft)
  B) numeric IP host classification            (metadata / private / loopback)
  C) mixed-script confusable                   (Cyrillic look-alike, раypal)
Returns an engine Finding; combine() picks the most severe.
"""
import re
import ipaddress
from invariant_engine.core import Finding
from invariant_engine.supplement import combine  # severity-max merge

# ---- A) digit-as-letter homoglyph ----
LEET = {"0": ["o"], "1": ["l", "i"], "3": ["e"], "4": ["a"],
        "5": ["s"], "6": ["g", "b"], "7": ["t"], "8": ["b"], "9": ["g"]}
BRANDS = {"paypal", "google", "microsoft", "apple", "amazon", "netflix",
          "facebook", "twitter", "instagram", "sberbank", "binance",
          "telegram", "whatsapp", "linkedin", "gmail", "outlook", "yahoo",
          "youtube", "coinbase", "metamask", "steam"}

def _deleet_variants(tok):
    outs = [""]
    for c in tok.lower():
        subs = LEET.get(c, [c])
        outs = [o + s for o in outs for s in subs]
        if len(outs) > 32:                      # keep bounded
            outs = outs[:32]
    return set(outs)

def _homoglyph_digit(text):
    for label in re.findall(r"[a-z0-9]+", text.lower()):
        if any(ch.isdigit() for ch in label) and any(ch.isalpha() for ch in label):
            if _deleet_variants(label) & BRANDS:
                return Finding("suspect", 0.85,
                    f"digit-as-letter brand mimicry: '{label}' de-leets to a known brand",
                    conclusive=True, signature="homoglyph_digit")
    return None

# ---- B) numeric IP host ----
def _ip_host(text):
    for m in re.finditer(r"https?://([^/\s:?#]+)", text, re.I):
        host = m.group(1)
        try:
            ip = ipaddress.ip_address(host)
        except ValueError:
            continue
        if ip.is_link_local:
            return Finding("suspect", 0.95, f"link-local/metadata IP host {host} (SSRF)",
                           conclusive=True, signature="ip_metadata")
        if ip.is_loopback or ip.is_private:
            return Finding("suspect", 0.9, f"internal/loopback IP host {host} (SSRF)",
                           conclusive=True, signature="ip_internal")
        if ip.is_unspecified or ip.is_reserved:
            return Finding("suspect", 0.85, f"wildcard/reserved IP host {host}",
                           conclusive=True, signature="ip_wildcard")
        return Finding("suspect", 0.5, f"raw public IP as host {host}",
                       signature="ip_public")
    return None

# ---- C) mixed-script confusable (Cyrillic look-alike) ----
CYR_LOOKALIKE = set("аеорсхукіѕј")  # cyrillic letters that look Latin

def _confusable(text):
    if "." not in text:                                      # cheap guard: no dot, no domain
        return None
    for tok in re.findall(r"[^\s/.]{0,80}\.[^\s/]{1,80}", text):  # bounded domain-ish token
        low = tok.lower()
        has_latin = any("a" <= c <= "z" for c in low)
        has_cyr = any(c in CYR_LOOKALIKE for c in low)
        if has_latin and has_cyr:
            return Finding("suspect", 0.85,
                f"mixed-script confusable in '{tok}' (Latin + Cyrillic look-alike)",
                conclusive=True, signature="confusable_cyrillic")
    return None

def digit_cards_reader(text):
    """Max-severity of the three simulated digit-card checks; clean if none."""
    result = Finding("clean", 0.0, "digit-cards: nothing")
    for check in (_homoglyph_digit, _ip_host, _confusable):
        f = check(text)
        if f:
            result = combine(result, f)
    return result
