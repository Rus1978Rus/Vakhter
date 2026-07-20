"""
Invariant Engine — the general core.

One idea, taken twice:
    REAL / MEANINGFUL = the structure that is INVARIANT under a transform,
    not the local surface token.

Two axes (both pluggable):
  - MSL role  (nature)  : read STRUCTURE of one subject  -> is it doing
                          something out of place, and how blatantly.
                          Invariance across SUBSTRATE.
  - ERG role  (reality) : does that structure SURVIVE a transform
                          (zoom-out across scale, or recurrence across a
                          stream over time). Invariance across SCALE/TIME.

Any input (signal grid, text, prompt, code, ...) becomes a Subject via an
adapter. The core never knows or cares what the substrate is.
"""

from dataclasses import dataclass


@dataclass
class Finding:
    """What the MSL role returns about ONE subject (its nature)."""
    label: str          # "clean" | "activation" | "suspect"
    strength: float     # 0..1  — how strong / how blatant
    reason: str         # human explanation
    conclusive: bool = False   # damning on its own; no persistence needed
    signature: str = ""        # stable key for recurrence matching


@dataclass
class Verdict:
    risk: str           # "OK" | "NOISE" | "WATCH" | "ALARM"
    reality: float      # 0..1 survival
    finding: Finding
    explanation: str


def judge(finding: Finding, reality: float,
          strength_hi: float = 0.6, reality_hi: float = 0.5) -> Verdict:
    """Combine nature (MSL) x reality (ERG) into one honest verdict.

    - clean                              -> OK
    - conclusive structural attack       -> ALARM  (ERG not needed)
    - 'activation' (pure magnitude, e.g. a signal spike):
        did NOT survive                  -> NOISE   (strong but transient)
        survived + strong                -> ALARM
        survived + mild                  -> WATCH
    - 'suspect' (named structural anomaly, e.g. URL mimicry):
        survived (recurs)                -> ALARM
        did not survive (one-off)        -> WATCH   (flagged, unconfirmed)
    """
    f = finding
    if f.label == "clean":
        return Verdict("OK", round(reality, 4), f, "No structural anomaly.")

    if f.conclusive:
        return Verdict("ALARM", round(reality, 4), f,
                       f"{f.reason}; conclusive on its own.")

    if f.label == "activation":
        if reality < reality_hi:
            risk, exp = "NOISE", f"{f.reason} but collapsed under the transform (transient)."
        elif f.strength >= strength_hi:
            risk, exp = "ALARM", f"{f.reason} and survived the transform at high amplitude."
        else:
            risk, exp = "WATCH", f"{f.reason}, survived but only at moderate amplitude."
        return Verdict(risk, round(reality, 4), f, exp)

    # label == "suspect"
    if reality >= reality_hi:
        risk, exp = "ALARM", f"{f.reason}; and it persists across the stream."
    else:
        risk, exp = "WATCH", f"{f.reason}; but it did not recur (single / transient)."
    return Verdict(risk, round(reality, 4), f, exp)


class InvariantEngine:
    """Wires a structure-reader (MSL) and a survival-tester (ERG)."""

    def __init__(self, reader, survival, strength_hi=0.6, reality_hi=0.5):
        self.reader = reader        # subject -> Finding
        self.survival = survival    # (subject, finding) -> float 0..1
        self.strength_hi = strength_hi
        self.reality_hi = reality_hi

    def analyze(self, subject) -> Verdict:
        finding = self.reader(subject)
        reality = 0.0 if finding.label == "clean" else self.survival(subject, finding)
        return judge(finding, reality, self.strength_hi, self.reality_hi)

    @staticmethod
    def mask(verdict: Verdict) -> dict:
        """Client-safe view — no raw scores / internals."""
        band = ("high" if verdict.reality >= 0.66 else
                "medium" if verdict.reality >= 0.33 else "low")
        action = {"OK": "No action.",
                  "NOISE": "Log as transient; no action.",
                  "WATCH": "Monitor; re-evaluate on recurrence.",
                  "ALARM": "Escalate for human review."}[verdict.risk]
        return {"risk_level": verdict.risk,
                "explanation": verdict.explanation,
                "confidence_band": band,
                "recommended_action": action}
