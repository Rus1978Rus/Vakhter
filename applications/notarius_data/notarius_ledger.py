# -*- coding: utf-8 -*-
"""
NOTARIUS-DATA — a lightweight provenance ledger for DATA RECORDS (MVP sketch).

Spun out of the guard session's Notarius/provenance primitives, applied to a new
field: data pipelines / ledgers / documents. The pitch, same as the guard's:
PRIMITIVE = RELIABLE = AUDITABLE — no heavy database, no black box.

What it answers that a plain checksum does NOT:
  - element-level, not just "the whole file changed" — each RECORD is tracked;
  - NATIVE vs inserted — a foreign row with a valid hash is still rejected
    (SIGNED != NATIVE): its lineage was never signed by the author's key;
  - a crypto-free LENGTH WITNESS catches inserted characters incl. invisibles
    (ZWSP/ZWNJ/BOM) with three lines and zero dependencies;
  - an append-only TRANSPARENCY LOG makes every entry's history tamper-evident.

Four independent barriers, each catches a different attack:
  hash (content) · cp_len (length/insertion) · signed lineage (native origin) · log (history)
  LENGTH_INTACT != CONTENT_INTACT != NATIVE — you want all of them.
"""
import hashlib
import hmac
import json

CONVEYOR = ("created", "checked", "closed")   # each record's provenance chain


# ---------- primitives ----------
def _canon(record):
    """Stable serialization; ensure_ascii=False keeps invisibles in the string."""
    return json.dumps(record, sort_keys=True, ensure_ascii=False, separators=(",", ":"))

def _hash(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def _cplen(s):
    return len(s)                              # Unicode codepoint count = length witness

def _sign(secret, msg):
    return hmac.new(secret, msg.encode("utf-8"), hashlib.sha256).hexdigest()

def _fields(*parts):
    """Length-prefixed field join so a '|' inside an id/event cannot shift the
    signed/hashed boundaries (the delimiter-injection class the core modules fixed
    in AD-28/AD-30; applied here too so the MVP does not repeat the lesson)."""
    return "\x1e".join(f"{len(p)}:{p}" for p in (str(x) for x in parts))


# ---------- author side (holds the key) ----------
def notarize(rec_id, record, author_key):
    s = _canon(record)
    h = _hash(s)
    lineage, prev = [], "ROOT"
    for step in CONVEYOR:
        sig = _sign(author_key, _fields(rec_id, h, step, prev))
        lineage.append({"step": step, "prev": prev, "sig": sig})
        prev = sig
    return {"id": rec_id, "record": record, "hash": h, "cp_len": _cplen(s), "lineage": lineage}


# ---------- verifier side ----------
def verify(entry, author_key, manifest_ids):
    """Full verify: NATIVE | FOREIGN | TAMPERED | INVISIBLE_INSERT | FORGED_LINEAGE."""
    if entry["id"] not in manifest_ids:
        return "FOREIGN"                       # id was never notarised by the author
    s = _canon(entry["record"])
    if _hash(s) != entry["hash"]:
        # content changed. length witness tells us HOW (insertion vs equal-length edit)
        return "INVISIBLE_INSERT" if _cplen(s) != entry["cp_len"] else "TAMPERED"
    if _cplen(s) != entry["cp_len"]:
        return "INVISIBLE_INSERT"
    prev = "ROOT"
    for st in entry["lineage"]:
        good = _sign(author_key, _fields(entry["id"], entry["hash"], st["step"], prev))
        if st.get("prev") != prev or not hmac.compare_digest(good, st.get("sig", "")):
            return "FORGED_LINEAGE"
        prev = st["sig"]
    return "NATIVE"

def light_witness(entry):
    """Crypto-free barrier only: does the codepoint length still match? (3 lines.)"""
    return _cplen(_canon(entry["record"])) == entry["cp_len"]


# ---------- append-only transparency log (hash-chained) ----------
def log_new():
    g = {"seq": 0, "event": "GENESIS", "prev": "0" * 64}
    g["hash"] = _hash(_fields(0, "GENESIS", g["prev"]))
    return [g]

def log_append(log, event):
    prev = log[-1]
    e = {"seq": prev["seq"] + 1, "event": event, "prev": prev["hash"]}
    e["hash"] = _hash(_fields(e["seq"], event, e["prev"]))
    log.append(e)
    return e

def log_ok(log):
    for i, e in enumerate(log):
        if e["hash"] != _hash(_fields(e["seq"], e["event"], e["prev"])):
            return False, e["seq"]
        if i and e["prev"] != log[i - 1]["hash"]:
            return False, e["seq"]
    return True, None


# ---------- demo ----------
def run():
    KEY = b"finance-team-author-key"
    ATTACKER = b"attacker-has-no-key"
    ZWNJ = chr(0x200C)

    ledger = [
        {"id": "INV-1", "amount": "1000000", "account": "ACME-Corp",  "date": "2026-06-01"},
        {"id": "INV-2", "amount": "250000",  "account": "Beta-LLC",   "date": "2026-06-02"},
        {"id": "INV-3", "amount": "3140000", "account": "Gamma-Trust", "date": "2026-06-03"},
    ]
    signed = {r["id"]: notarize(r["id"], r, KEY) for r in ledger}
    manifest = set(signed.keys())
    tlog = log_new()
    for rid in signed:
        log_append(tlog, f"NOTARISE {rid}")

    print("NOTARIUS-DATA — provenance ledger (MVP)")
    print("=" * 66)
    print(f"author notarised {len(signed)} records + logged them\n")

    import copy
    def attack(name, mutate=None, key=KEY, foreign=None):
        e = foreign if foreign else copy.deepcopy(signed["INV-1"])
        if mutate:
            mutate(e)
        v = verify(e, key, manifest)
        light = "len-ok" if light_witness(e) else "LEN-SHIFT"
        print(f"{name:34} -> {v:16} (crypto-free witness: {light})")

    attack("clean record")
    attack("edit amount 1000000->2000000",
           lambda e: e["record"].__setitem__("amount", "2000000"))     # same length
    attack("edit amount 1000000->500",
           lambda e: e["record"].__setitem__("amount", "500"))         # different length
    attack("inject invisible char (ZWNJ)",
           lambda e: e["record"].__setitem__("account", "ACME" + ZWNJ + "-Corp"))
    attack("attacker re-signs with own key",
           lambda e: e.__setitem__("lineage", notarize("INV-1", e["record"], ATTACKER)["lineage"]))
    attack("FOREIGN row inserted (valid hash)",
           foreign=notarize("INV-99", {"id": "INV-99", "amount": "9000000",
                                       "account": "Ghost", "date": "2026-06-09"}, ATTACKER))

    ok, _ = log_ok(tlog)
    print(f"\ntransparency log: {len(tlog)} entries, chain valid = {ok}")
    tlog[1]["event"] = "NOTARISE INV-1 (secretly altered)"
    ok2, bad = log_ok(tlog)
    print(f"after tampering a past log entry: chain valid = {ok2} (break at seq {bad})")

    print("\n" + "=" * 66)
    print("Four barriers, four different catches: content (hash), length (cp_len,")
    print("crypto-free), origin (signed lineage: SIGNED != NATIVE), history (log).")

if __name__ == "__main__":
    run()
