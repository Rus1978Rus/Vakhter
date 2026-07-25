# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
Prompt-injection eval: MSL (real) vs keyword baseline vs combined.

Usage:
  MSL_MIP_HOME=/path/to/msl_mip  python eval.py [dataset.jsonl]

Positive (=flag as injection):
  keyword  : any known injection phrase appears (substring, case-insensitive)
  msl      : invariant engine (real MSL) verdict != OK   (WATCH or ALARM)
  combined : keyword OR msl
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ENGINE_DIR = os.path.join(HERE, "..", "invariant_engine")
sys.path.insert(0, os.path.abspath(ENGINE_DIR))

from invariant_engine import InvariantEngine, erg
from invariant_engine.msl_real import real_text_reader, real_plus_reader

msl_engine = InvariantEngine(real_text_reader, erg.no_stream)   # single-item, no feed
msl_plus_engine = InvariantEngine(real_plus_reader, erg.no_stream)  # + structural supplement

KEYWORDS = [
    "ignore previous", "ignore all previous", "disregard", "system prompt",
    "you are now", "developer mode", "no restrictions", "unfiltered",
    "forget your", "jailbreak", "dan can do anything", "hidden password",
    "override", "safety policy", "safety filter", "no content restrictions",
    "obey me", "reveal", "grant full access",
]

def kw_flag(text):
    low = text.lower()
    return any(k in low for k in KEYWORDS)

def msl_flag(text):
    return msl_engine.analyze(text).risk != "OK"

def msl_plus_flag(text):
    return msl_plus_engine.analyze(text).risk != "OK"

def metrics(rows, predict):
    tp = fp = fn = tn = 0
    for r in rows:
        p = predict(r["text"]); y = r["label"] == 1
        if p and y: tp += 1
        elif p and not y: fp += 1
        elif not p and y: fn += 1
        else: tn += 1
    prec = tp / (tp + fp) if tp + fp else 0.0
    rec = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * prec * rec / (prec + rec) if prec + rec else 0.0
    fpr = fp / (fp + tn) if fp + tn else 0.0
    acc = (tp + tn) / len(rows)
    return dict(tp=tp, fp=fp, fn=fn, tn=tn, precision=prec, recall=rec,
                f1=f1, fpr=fpr, accuracy=acc)

def recall_by_tag(rows, predict, tag):
    sub = [r for r in rows if r["tag"] == tag]
    hit = sum(1 for r in sub if predict(r["text"]))
    return hit, len(sub)

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "dataset.jsonl")
    rows = [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]
    real_text_reader("warmup")   # boot MSL once

    dets = {"keyword": kw_flag,
            "MSL (real)": msl_flag,
            "MSL + supplement": msl_plus_flag,
            "combined (kw OR MSL+supp)": lambda t: kw_flag(t) or msl_plus_flag(t)}

    def table(subset, title):
        if not subset:
            return
        print(f"\n### {title}  ({len(subset)} items)")
        hdr = (f"{'detector':26} {'prec':>6} {'recall':>7} {'F1':>6} "
               f"{'FPR':>6} {'acc':>6}   (TP/FP/FN/TN)")
        print(hdr); print("-" * len(hdr))
        for name, fn in dets.items():
            m = metrics(subset, fn)
            print(f"{name:26} {m['precision']:6.2f} {m['recall']:7.2f} {m['f1']:6.2f} "
                  f"{m['fpr']:6.2f} {m['accuracy']:6.2f}   "
                  f"({m['tp']}/{m['fp']}/{m['fn']}/{m['tn']})")

    print(f"dataset: {path}  ({len(rows)} items)")
    table(rows, "ALL")
    table([r for r in rows if r.get("split") == "seed"], "SEED (tuned-against)")
    table([r for r in rows if r.get("split") == "held"], "HELD-OUT (generalization)")

    print("\nrecall by injection sub-class (ALL):")
    for name, fn in dets.items():
        parts = []
        for tag in ("nl", "structural"):
            hit, tot = recall_by_tag(rows, fn, tag)
            parts.append(f"{tag}={hit}/{tot} ({hit/tot:.0%})")
        print(f"  {name:26} " + "  ".join(parts))

if __name__ == "__main__":
    main()
