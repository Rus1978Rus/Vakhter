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


def _severity(f: Finding):
    """Deterministic severity/specificity key. Order-INDEPENDENT: conclusive and
    signature-presence are in the key, so a conclusive or signatured finding wins
    a rank tie regardless of argument position (combine(x,y) == combine(y,x))."""
    return (_rank(f), f.conclusive, f.strength, bool(f.signature))


def combine(f1: Finding, f2: Finding) -> Finding:
    """Return the more severe of two findings; merge reasons if both fire.

    The integrator is MONOTONE — it must never LOWER a verdict:
      - `conclusive` is the OR of both inputs, in EVERY branch (a hard verdict on
        either side is never dropped — the earlier same-reason short-circuit
        could, order-dependently, drop a losing finding's conclusive flag);
      - tie-breaking is by severity/specificity, not argument order, so a
        conclusive / more-specific finding is not masked behind a generic one
        that merely came first among the readers.
    """
    hi, lo = (f1, f2) if _severity(f1) >= _severity(f2) else (f2, f1)
    conclusive = f1.conclusive or f2.conclusive          # never drop a hard verdict
    signature = hi.signature or (lo.signature if lo.label != "clean" else "")
    both = lo.label != "clean" and hi.label != "clean"
    reason = (f"{hi.reason} | + {lo.reason}"
              if both and lo.reason != hi.reason else hi.reason)
    if conclusive == hi.conclusive and signature == hi.signature and reason == hi.reason:
        return hi                                        # unchanged — keep the object
    return Finding(hi.label, hi.strength, reason,
                   conclusive=conclusive, signature=signature)
