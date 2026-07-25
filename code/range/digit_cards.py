# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
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
from brand_corpus import PHISHING_BRANDS as BRANDS   # one shared brand corpus

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

# ---- A2) visual multigraph / I-l brand mimicry (no digit needed) ----
# Typosquatting look-alikes that need no digit: rn->m (arnazon), vv->w (vvhatsapp),
# cl->d, and capital-I used as lowercase-l (paypaI, googIe). We de-confuse a label
# and flag ONLY when a fold lands exactly on a brand AND the label itself is not
# already that brand — so a legit "amazon"/"Chase" mention (no trick) never fires.
def _visual_variants(label):
    forms = {label}
    for f in list(forms):
        forms.add(f.replace("rn", "m"))
        forms.add(f.replace("vv", "w"))
        forms.add(f.replace("cl", "d"))
    forms |= {f.replace("rn", "m").replace("vv", "w") for f in list(forms)}
    forms |= {f.replace("I", "l") for f in list(forms)}   # capital I as lowercase l
    return {f.lower() for f in forms}

def _visual_brand(text):
    for label in re.findall(r"[A-Za-z]{5,}", text):     # len>=5: no short-brand FP
        if label.lower() in BRANDS:                     # legit brand mention, no trick
            continue
        if _visual_variants(label) & BRANDS:
            return Finding("suspect", 0.8,
                f"visual brand mimicry: '{label}' resolves to a known brand via a "
                f"look-alike multigraph (rn->m / vv->w / cl->d) or capital-I-for-l",
                conclusive=True, signature="brand_visual")
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
    for check in (_homoglyph_digit, _visual_brand, _ip_host, _confusable):
        f = check(text)
        if f:
            result = combine(result, f)
    return result
