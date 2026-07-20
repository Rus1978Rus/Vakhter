# ARCHITECTURE — the card library and its two faces
AUTHOR: Руслан Малявский · STATUS: WORKING FRAME · 2026-07-20

## The framing (fixed)

Sign cards are **records in a library**, queried like SQL.

| SQL world | here |
|---|---|
| table / rows | the sign-card library |
| `SELECT` | MSL reads a sign → fetches its card → "what does this sign do here" |
| query engine | the MSL engine |
| **admin plane** (INSERT/UPDATE, permissions, audit, constraints) | the governance layer: signing, m-of-n quorum, transparency log, integrity + provenance gates |

A database has **two faces**:
- **User face** — read-only queries. The user sends text and asks "is this sign
  dangerous?". They READ the library; they never change it.
- **Admin face** — add / change / close a card, permissions, change log. Rare,
  privileged, locked down. Everything built in component checks #1–#6 is this face.

The admin face is deliberately heavy: changing the library is more dangerous than
reading it. The ordinary user never sees it.

---

## SECURITY NOTE — injection at query time (to think about / not yet built)

Concern (Руслан): at the moment of a QUERY, can a threat be injected? This is the
SAME injection family the tool itself detects — now aimed at our OWN lookup path.
The attacker controls the input (the signs being looked up).

Principle: **at the boundary where attacker input meets the library, keep DATA as
DATA.** Never let input choose or alter the query STRUCTURE.

Vectors to watch:

1. **Lookup key built from input (classic injection).** If the card is fetched by
   building a query string from the input sign, an attacker crafts input that
   changes the query — SQL injection against our own card store.
   - Defense: parameterize. Key cards by **exact codepoint** (a number, not a
     string). A codepoint cannot carry query structure.
   - Status: the current runtime looks cards up by codepoint in a dict → naturally
     safe. The risk appears only if the library becomes a real SQL store and
     queries are string-built. Keep it parameterized then.

2. **File/path lookup (traversal).** If a card were a file named after the sign,
   `../` or NUL in the key → traversal / wrong-card fetch.
   - Defense: never use raw input as a filename; key by codepoint-hex; validate charset.

3. **Output echo (present — TESTED & MITIGATED, check #7).** The guard's own
   finding reason echoes snippets of attacker input. Confirmed empirically: the
   confusable card echoed **raw ANSI escapes** into the reason (would hijack an
   admin terminal). Fixed: `report.safe_view()` sanitizes at the display boundary
   — control chars (incl. ANSI ESC) → visible inert escapes, HTML metacharacters →
   entities, length capped. `range_query_injection.py`: live payload in RAW output
   1/5 → in SAFE output **0/5**. Rule: never show or log `finding.reason` raw;
   always pass it through `safe_view()` first.

4. **Second-order.** Input stored (transparency log, cache) then re-read and
   processed unsafely later.
   - Defense: stored input is DATA on write AND on read; never executed.

What already protects the query path:
- cards are **author-signed** (provenance) → an attacker cannot inject a card at
  query time;
- **fail-closed** → a lookup error blocks, never passes;
- **DoS gate** → a flood at query time is bounced before lookup.

One-liner: don't let the input pick or shape the query, and treat the guard's own
answer as untrusted too.
