# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LicenseRef-Proprietary
"""
COMPONENT CHECK #6 — m-of-n quorum + append-only transparency log.

Closes the residual from check #5: one malicious/compromised author key must not
be able to push a lowering component, and no sign-off can happen in secret.
Run:  python range_quorum.py
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from quorum import sign_as, subject_of, accept_change, POLICY
import transparency as tlog

# five authorised signers (a review board); each has their own key
BOARD = {f"signer{i}": (f"key-of-signer{i}").encode() for i in range(1, 6)}
ERG_HASH = "abc123deadbeef"          # hash of the ERG change being proposed

def show(title, role, signatures):
    ok, thr, signers = accept_change("erg", ERG_HASH, role, signatures, BOARD)
    print(f"{title:44} -> {'ACCEPT' if ok else 'REJECT':6} "
          f"(need {thr}, got {len(signers)}: {signers})")
    return ok

def run():
    print("COMPONENT CHECK #6 — m-of-n quorum + transparency log")
    print("=" * 74)
    print(f"policy: lowering component (ERG/integrator) needs "
          f"{POLICY['lowering']}-of-{len(BOARD)} signatures\n")
    subj = subject_of("erg", ERG_HASH)

    # 1) a single (even valid) signature — the malicious-author move
    one = [sign_as("signer1", BOARD["signer1"], subj)]
    show("1 valid signature (lone author)", "lowering", one)

    # 2) the same signer three times (replay) — still one distinct signer
    replay = one * 3
    show("same signer x3 (replay)", "lowering", replay)

    # 3) an outsider key
    outsider = one + [sign_as("attacker", b"attacker-key", subj)]
    show("1 real + 1 unauthorised", "lowering", outsider)

    # 4) genuine quorum: three different board members
    three = [sign_as(f"signer{i}", BOARD[f"signer{i}"], subj) for i in (1, 2, 3)]
    ok = show("3 distinct board members", "lowering", three)

    # 5) a normal card needs only one
    show("normal card, 1 signature", "normal", one)

    # --- transparency log ---
    print("\n" + "-" * 74)
    log = tlog.new_log()
    tlog.append(log, "PROPOSE erg@abc123 by signer1", "2026-07-20T10:00")
    tlog.append(log, "SIGN erg@abc123 signer1", "2026-07-20T10:01")
    tlog.append(log, "SIGN erg@abc123 signer2", "2026-07-20T10:05")
    tlog.append(log, "SIGN erg@abc123 signer3 -> QUORUM MET, ACCEPTED", "2026-07-20T10:09")
    ok_chain, bad = tlog.verify_chain(log)
    print(f"transparency log: {len(log)} entries, chain valid = {ok_chain}")

    # attacker tries to erase the fact that signer3 signed (rewrite an entry)
    log[3]["event"] = "SIGN erg@abc123 signer3 (secretly removed)"
    ok_chain2, bad2 = tlog.verify_chain(log)
    print(f"after tampering entry #3: chain valid = {ok_chain2}  (break at seq {bad2})")

    print("\n" + "=" * 74)
    print("One key can't push a lowering component (needs m-of-n). Every sign-off")
    print("is on an append-only record — erasing it breaks the chain and is caught.")

if __name__ == "__main__":
    run()
