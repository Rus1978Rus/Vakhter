"""
Structural supplement — engine-layer checks that COMPLEMENT the real MSL.

These are NOT edits to the msl_mip sign cards (that core stays untouched and
conveyor-governed). They live in the engine, which is the right home for a new
detection until it is properly carded through the conveyor.

Three GENERAL checks (written before the held-out test items, to avoid
teach-to-the-test):
  A) leading-position invisible smuggling (BOM / zero-width at the very start)
  B) sensitive ABSOLUTE resource paths (protected-asset list, not a threat DB)
  C) exfiltration intent = an external destination (email / URL) + an exfil verb
"""
import re
from .core import Finding

INVIS = {0x200B, 0x200C, 0x200D, 0x2060, 0xFEFF,
         0x202A, 0x202B, 0x202C, 0x202D, 0x202E, 0x2066, 0x2067, 0x2068, 0x2069}

# protected ASSETS (what must not leak) — not a list of attackers
# bounded wildcards ({0,N}) so a wall of the same char can't cause O(n^2)
# regex backtracking (ReDoS). Real paths / addresses are short.
SENSITIVE_PATH = re.compile(
    r"(/etc/(passwd|shadow|sudoers)|/root/|(^|/)\.ssh/|id_rsa|id_ed25519|"
    r"(^|/)\.env(\b|$)|/proc/self/environ|/var/www/[^\s]{0,200}\.env)", re.I)

EMAIL = re.compile(r"\b[\w.+-]{1,64}@[\w-]{1,63}\.[\w.-]{1,64}\b")
URL = re.compile(r"https?://[^\s]{1,2000}", re.I)
# exfil ACTIONS only — 'email' the noun is too common ("here's my email"), so it
# is deliberately excluded to protect precision.
EXFIL_VERB = re.compile(
    r"\b(send|upload|exfiltrat\w*|post|forward|leak|transmit|deliver|drop)\b", re.I)


def supplement_reader(text: str) -> Finding:
    # A) leading invisible (first 3 code points)
    for ch in text[:3]:
        if ord(ch) in INVIS:
            return Finding("suspect", 0.6,
                           f"leading invisible control char U+{ord(ch):04X} "
                           f"(smuggling position)", signature="lead_invisible")

    # B) sensitive absolute resource path
    m = SENSITIVE_PATH.search(text)
    if m:
        return Finding("suspect", 0.85,
                       f"sensitive resource path '{m.group(0)}'",
                       conclusive=True, signature="sensitive_path")

    # C) exfiltration intent: external destination + exfil verb.
    # Cheap literal guards first so the address regexes never run on input that
    # cannot contain an address (avoids ReDoS on long non-address strings).
    dest = (EMAIL.search(text) if "@" in text else None) or \
           (URL.search(text) if "://" in text else None)
    if dest and EXFIL_VERB.search(text):
        return Finding("suspect", 0.8,
                       f"exfiltration intent: verb + external destination "
                       f"'{dest.group(0)}'", conclusive=True,
                       signature="exfil_intent")

    return Finding("clean", 0.0, "supplement: nothing")


def _rank(f: Finding) -> float:
    if f.label == "clean":
        return 0.0
    return 2.0 if f.conclusive else 1.0 + f.strength


def combine(f1: Finding, f2: Finding) -> Finding:
    """Return the more severe of two findings; merge reasons if both fire."""
    hi, lo = (f1, f2) if _rank(f1) >= _rank(f2) else (f2, f1)
    if lo.label != "clean" and hi.label != "clean" and lo.reason != hi.reason:
        return Finding(hi.label, hi.strength,
                       f"{hi.reason} | + {lo.reason}",
                       conclusive=hi.conclusive or lo.conclusive,
                       signature=hi.signature)
    return hi
