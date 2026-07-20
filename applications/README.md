# APPLICATIONS — the same mechanisms, other fields

The guard (`code/`) was one product. Its parts are general primitives, so the
same machinery spins out into other fields. These are runnable MVP sketches
(one file each, zero dependencies) built from the session's own components —
same honest style: measured, reproducible, primitive = reliable = auditable.

All three sit on one idea the whole session turned on:
> **real / meaningful = the structure that is INVARIANT under a transform —
> native vs inserted, signal vs noise — not the surface value.**

| product | guards | the transform it is invariant to | reused from |
|---|---|---|---|
| **the guard** (`code/`) | an incoming message/prompt | substrate / encoding | MSL + cards + ERG |
| **notarius_data** | a data record / ledger row | tampering / insertion / foreign origin | provenance + transparency |
| **erg_fraud** | a stream of numbers | scale (coarse-graining) | ERG (intensity ≠ objectivity) |

## notarius_data — provenance ledger (`notarius_data/notarius_ledger.py`)
A lightweight, no-heavy-DB provenance layer for DATA RECORDS (invoices,
transactions, document fields). Four independent barriers, each catches a
different attack: **hash** (content), **codepoint-length witness** (insertion,
incl. invisibles — crypto-free), **signed lineage** (native origin: SIGNED ≠
NATIVE), **append-only log** (tamper-evident history). Demo catches: equal-length
edit (hash), length-changing edit + invisible-char injection (length witness),
attacker re-sign (forged lineage), a FOREIGN row with a valid hash (no signed
origin), and a rewritten log entry (chain break).
Fields: finance/audit ledgers, ETL data lineage (element-level), document
notarisation / chain of custody.

## erg_fraud — anomaly detection by survival across scale (`erg_fraud/erg_fraud.py`)
A real anomaly SURVIVES zoom-out. Coarse-grain the stream at several scales; a
one-off spike (a legit big purchase) is intense at the finest scale but
DISSOLVES when averaged → NOISE; a distributed pattern (structuring / card-testing
/ slow drain — many small events clustered in time) SURVIVES → REAL, even though
no single event trips a per-transaction threshold. Verified across 5 seeds:
naive threshold false-alarms on the spike AND misses the distributed fraud; ERG
does the opposite. No model, no training, no database.
Fields: fraud / AML, IoT & sensor validation, trading anomalies (its origin,
ERG-CAD), any signal-vs-noise stream.

## Honest status
MVP sketches, not products: learning HMAC (→ real asymmetric signatures in prod),
hand-tuned thresholds, small demo batteries. Mature incumbents exist in data
lineage (DataHub) and anomaly detection — the edge here is the same as the
guard's: lightweight, reasons instead of looks-up, fully auditable, fails safe.
Run: `python applications/notarius_data/notarius_ledger.py` /
`python applications/erg_fraud/erg_fraud.py`.
