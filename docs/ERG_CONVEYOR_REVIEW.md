# ERG conveyor review — 5 reviewers, adversarially verified
RUN: wf_19f3b960 · 2026-07-20 · SUBJECT: code/range/erg_context.py

A multi-agent conveyor (5 independent reviewers, distinct lenses; every finding
adversarially re-verified against the real code/run). 10 findings, **all 10
CONFIRMED**, 0 refuted. This found real bypasses that the earlier single-pass
component check #2 missed — the value of the conveyor discipline, demonstrated.

## Confirmed findings (ranked)

**CRITICAL — a real threat, MSL-flagged (WATCH), cleared to OK by phrasing:**
1. `data:` URI XSS — `What is data:text/html;base64,PHNjcmlwdD…?` (decodes to
   `<script>alert(document.cookie)</script>`) → was OK.
2. `data:` URI PE-dropper — `…for example data:application/x-msdownload;base64,TVqQAA…`
   (MZ header) → was OK.
3. Windows backslash traversal — `What is ..\..\..\windows\system32\config\sam ?`
   → was OK (forward-slash `../..` was protected; backslash and `%5c` were not).

**HIGH:**
4. The benign-frame gate was fully attacker-controlled — `for example` / `e.g.` /
   `such as` / a trailing `?` anywhere in the text self-authorised softening.
5. Home-dir credential files omitted from the operational veto —
   `~/.git-credentials`, `~/.pgpass`, `~/.bash_history`, `~/.ssh` (no slash) →
   recon cleared to OK.
6. Operational veto narrower than MSL — `chmod 777 /etc`, `chmod -R 777 /`,
   `echo pwned > ~/.bashrc`, bare `/etc` → cleared to OK.

**MEDIUM:**
7. `.ssh/` off-by-one (trailing slash required).
8. False positive: any 4-label dotted token (internal hostnames, Java packages,
   version quads) stuck at WATCH.
9. False positive: multipart TLDs (`.co.uk`, `.co.jp`, `.com.au`) stuck at WATCH.

**INFO — invariants that HELD:** never raises; no ReDoS (<0.07s on pathological
input); immune (non-MSL) signatures untouched; a *conclusive* finding was never
cleared to OK.

## Root cause (the synthesis)

Not a pile of regex gaps — one architectural flaw: `_OPERATIONAL` was a **denylist**
used to *veto* clearing, but MSL's `queue_for_review` coverage is strictly
**broader** than `_OPERATIONAL`. Every WATCH→OK bypass was a token MSL flags that
`_OPERATIONAL` did not re-derive. A denylist can never be complete → the
clear-to-OK path was inherently a bypass surface.

## Fix applied (structural, recommended by the review)

ERG now **never clears an MSL-flagged finding to OK**. The clear-to-OK path and the
`_OPERATIONAL` denylist were removed entirely. ERG may only soften a *conclusive*
ALARM → WATCH inside a benign frame (so a legit question is not BLOCKED). Nothing
MSL flags can reach OK through ERG.

Verified after fix: all 8 critical/high repros → WATCH (0 still-OK);
`range_erg_attack` THREATS SILENCED TO OK = 0; `range_context` 24/24 threats
flagged. The two precision false-positives (7-9) disappear as a class — there is
no longer a clear-to-OK decision to get wrong.

## Resolution — mask-and-rescan (author chose "restore safely")

Rather than accept the FP-clearing loss, ERG now restores clearing with a
POSITIVE proof bound to the flagged signal: **mask-and-rescan**. To clear a
non-conclusive WATCH to OK, ERG removes the benign structure (`git@host`,
`${VAR}`, `{{ident}}`) and re-scans the remainder with the readers-only pipeline
(MSL + cards, no ERG). It clears ONLY if what remains is clean — i.e. the benign
structure was the SOLE cause of the flag. A hidden payload survives the mask,
keeps the rescan dirty, and blocks the clear. This is not a denylist, so it
cannot be evaded by an unlisted carrier or an injected frame word.

Verified after mask-and-rescan:
- benign `git@github.com` clone and `{{ user.name }}` → OK again (proven sole cause);
- `${HOME}` stays WATCH — honestly, because masking it leaves `/` `:` that MSL
  also flags, so the structure was NOT the sole cause;
- all bypasses stay WATCH, including the two combos designed to beat it
  (`${X} data:…base64` and `git@a.co:b … ..\..\sam`): 0/7 reach OK;
- `range_erg_attack` THREATS SILENCED TO OK = 0; `range_context` 24/24 threats
  flagged, FPs cleared 1/5 → 2/5; detection and unit tests unchanged.

Net: false-positive clearing restored where it is provably safe, with zero bypass.
