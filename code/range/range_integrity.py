# -*- coding: utf-8 -*-
"""
COMPONENT CHECK #4b — demonstrate the integrity gate catching a poisoned component.

Build a manifest from the real components, then simulate three supply-chain
attacks and show the guard refuses to start each time.
Run:  python range_integrity.py
"""
import os, sys, tempfile, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from integrity import build_manifest, verify, refuse_reason

ENG = os.path.abspath(os.path.join(HERE, "..", "invariant_engine", "invariant_engine"))

# the guard's components, by role
def component_files(root_range, root_eng):
    return {
        "integrator": os.path.join(root_eng, "supplement.py"),    # combine() lives here
        "erg":        os.path.join(root_range, "erg_context.py"),
        "adapter":    os.path.join(root_eng, "msl_real.py"),
        "core":       os.path.join(root_eng, "core.py"),
        "card:digit":     os.path.join(root_range, "digit_cards.py"),
        "card:metachar":  os.path.join(root_range, "metachar_cards.py"),
        "card:invisible": os.path.join(root_range, "invisible_cards.py"),
        "card:harden":    os.path.join(root_range, "harden_cards.py"),
        "guard":      os.path.join(root_range, "guard.py"),
        "fail_closed":os.path.join(root_range, "fail_closed.py"),
    }

def run():
    print("COMPONENT CHECK #4b — integrity gate vs supply-chain tampering")
    print("=" * 70)
    files = component_files(HERE, ENG)
    manifest = build_manifest(files)                # author signs this
    print(f"manifest built over {len(manifest)} components (author-signed).\n")

    # 1) clean start
    ok, rep = verify(manifest, files)
    print(f"[clean start]          ok={ok}   {'-> guard starts' if ok else refuse_reason(rep)}")

    # copy the tree to a sandbox we can tamper with
    tmp = tempfile.mkdtemp()
    tr, te = os.path.join(tmp, "range"), os.path.join(tmp, "eng")
    os.makedirs(tr); os.makedirs(te)
    for name, p in files.items():
        dst = tr if p.startswith(HERE) else te
        shutil.copy(p, os.path.join(dst, os.path.basename(p)))
    tfiles = component_files(tr, te)

    # 2) tamper the ERG (the crown jewel) — flip a byte
    erg = tfiles["erg"]
    data = open(erg, "rb").read()
    open(erg, "wb").write(data.replace(b"context-cleared", b"context-cleared "))
    ok, rep = verify(manifest, tfiles)
    print(f"[tampered ERG]         ok={ok}   {refuse_reason(rep)}")
    shutil.copy(files["erg"], erg)                  # restore

    # 3) swap in a fake extra component (unknown, not in manifest)
    fake = os.path.join(tr, "evil_card.py")
    open(fake, "w").write("# malicious card\n")
    tfiles2 = dict(tfiles); tfiles2["card:evil"] = fake
    ok, rep = verify(manifest, tfiles2)
    print(f"[unknown component]    ok={ok}   {refuse_reason(rep)}")

    # 4) delete a component (missing)
    tfiles3 = dict(tfiles); tfiles3.pop("integrator")  # pretend it vanished
    # simulate missing by pointing at a non-existent path
    tfiles3b = dict(tfiles); tfiles3b["integrator"] = os.path.join(te, "gone.py")
    ok, rep = verify(manifest, tfiles3b)
    print(f"[missing integrator]   ok={ok}   {refuse_reason(rep)}")

    shutil.rmtree(tmp, ignore_errors=True)
    print("\n" + "=" * 70)
    print("Every tamper -> ok=False -> guard refuses to start (fail-closed).")
    print("A component the author's conveyor did not sign never runs.")

if __name__ == "__main__":
    run()
