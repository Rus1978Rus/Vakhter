# COVERAGE MAP — what the product catches, by category

Empirical, measured (not claimed). Two columns:

- **BASELINE** = `canonicalize → real MSL → verdict` — the product with *only*
  the real msl_mip cards loaded (the ~"half a percent" of the planned card base).
- **+DRAFTS** = same pipeline **plus the drafted card simulators**
  (supplement checks, digit/IP/confusable cards, metacharacter cards,
  invisible/bidi cards, hardening cards: jndi/ssti, cloud-creds, IPv6/octal IP).
  These are WORKING_DRAFT cards run as code so we can measure them before the
  author's conveyor closes them into msl_mip proper.

Numbers come from six harnesses in `code/range/`:
`range_test.py` (broad), `range_digits.py` (digit/IP/confusable),
`range_meta.py` (metacharacters), `range_bidi.py` (invisible/bidi),
`range_harden.py` (tomorrow's high-severity classes),
`range_context.py` (ERG context layer + threat-regression safety battery).
Re-runnable with `MSL_MIP_HOME` set.

---

## Summary line

| | BASELINE | +DRAFTS |
|---|---|---|
| broad structural threats | 9/20 (45%) | — |
| digit / IP / confusable threats | 3/14 (21%) | **14/14 (100%)** |
| metacharacter threats | 2/11 (18%) | **11/11 (100%)** |
| invisible / bidi threats | 6/7 (85%) | **7/7 (100%)** |
| benign kept clean (digit set) | 11/11 | 11/11 (0 new FP) |
| benign kept clean (metachar set) | 9/9 | 9/9 (0 new FP) |
| benign kept clean (invisible set) | **5/8** | **8/8 (0 new FP)** |
| hardening classes (jndi/ssti/cloud/ipv6/octal) | 3/15 (20%) | **15/15 (100%)** |
| benign kept clean (hardening set) | 7/10 | 7/10 (0 new FP) |
| residual MSL-core FPs (context layer) | 5 flagged | **5 → OK, 0 threats silenced** |
| natural-language prompt injection | 0/1 | 0/1 — **blind by design** |

> The hardening set's 7/10 benign "clean" is because 3 controls (`${HOME}`,
> `{{ title }}`, `git@github.com`) sit at WATCH — but that WATCH comes from
> **MSL core** (`queue_for_review` on its `{` / `:` / `@` cards), *not* from the
> new cards (new FP: 0). They are the same meaning-gap WATCHes noted at the end.

---

## By category

### 1. Encoding: percent / double-percent / overlong UTF-8 — **100%**
BASELINE already 100%. The canonicalization pre-pass decodes `%2e`, `%252e`,
`%c0%af` back to the real sign, then MSL reads it. This is the "double bottom"
working: the carrier is peeled, the sign underneath is judged.
*Missing to raise: nothing critical; add UTF-7, base64-in-URL, and mixed
double+overlong layering to the battery as regression guards.*

### 2. Path traversal (`../`, encoded, overlong) — **100%**
BASELINE 100% (plain, percent, double-enc, overlong all → ALARM).
*Missing: Windows `..\`, UNC `\\host\share`, and `....//` collapse variants.*

### 3. Invisible / zero-width / bidi — **precision fix: benign 5/8 → 8/8, threats 6/7 → 7/7**
Not a *catch* gap (MSL already witnesses invisibles) but a **precision** gap —
and fixing it exposed an adapter bug.

**The bug (fixed):** on an uncarded invisible, MSL says `pass` +
`WITNESS_PRESENT` — an honest "look at this," not a verdict. The engine adapter
(`msl_real.py`) promoted **every** witness to a conclusive ALARM
(`conclusive = sev>=3 or witness`). That judges on *presence, not context*, so it
could not tell a Trojan-Source RLO from a legit ❤️ emoji — and blocked both.
Three false ALARMs on benign input (`❤️` VS16, tag-flag `🏴…`, balanced bidi).

**The fix:** the adapter DELEGATES invisible judgment to a contextual
`invisible_cards` layer (a witness is never itself conclusive). That card is the
invisible authority:
- **ALARM:** zero-width splitting a *word* (`admin‹zw›istrator`); bidi
  **imbalance** (unterminated RLO/LRO — CVE-2021-42574); tag chars U+E00xx with
  no flag base; variation-selector carrier run (>=3 / leading).
- **OK:** every invisible present is provable glue — ZWJ *between emoji*, VS
  *after* an emoji base, tag chars *after* a flag base, *balanced* bidi.
- **WATCH:** an invisible present that is neither proven smuggle nor provable glue.

Now the RLO ALARMs *because the bidi is unbalanced* (context), and `❤️` /
family-emoji / tag-flag / Arabic-Hebrew RTL stay **OK**. `range_bidi.py`:
benign 5/8 → **8/8**, threats 6/7 → **7/7**, 0 new FP.

Honest side effect: pure-MSL BASELINE broad moved 10/20 → **9/20** — the RLO's
old ALARM was a *fake* from the buggy witness rule (MSL-alone only witnesses it);
the +DRAFTS layer earns that catch back correctly.
*Missing to raise: script-specific legit-ZWNJ allowlist (Persian/Indic) so those
reach OK instead of WATCH.*

### 4. Homoglyph digit-as-letter brand mimicry (`paypa1`, `g00gle`) — **0% → 100%**
BASELINE 0% (MSL sees valid ASCII letters/digits, nothing structurally wrong).
Digit cards de-leet each label and match against a brand set → ALARM, **0 FP**
on `version 1.0.3`, `pi 3.14159`, `iPhone 15`, `H2O`.
*Missing to raise: expand the brand set (currently ~21), add edit-distance-1
fuzzy match, and per-brand ‑TLD expectations.*

### 5. Numeric IP hosts (metadata / private / loopback / decimal / hex / wildcard) — **~20% → 100%**
BASELINE catches only dotted-private (`192.168.x`). Digit cards + canon
normalize decimal `2130706433` and hex `0x7f000001` to dotted, then classify:
link-local `169.254.169.254` → metadata/SSRF (ALARM), `0` → wildcard, etc.
**Hardening round added** (`harden_cards`): bracketed IPv6 in URLs —
`[::1]` loopback, `[fd00::1]` ULA-private, `[::ffff:169.254.169.254]`
IPv4-mapped-metadata — and octal-dotted `0177.0.0.1` all → ALARM. `range_harden`
IP cases 0/4 → 4/4, 0 FP (`::1`-as-prose-mention stays OK).
*Missing to raise: mixed dotted-decimal short forms (`127.1`), IPv6 zone-ids.*

### 6. Mixed-script confusable (Cyrillic look-alike `раypal.com`) — **0% → 100%**
BASELINE 0%. Confusable card flags Latin+Cyrillic-lookalike in one domain token.
*Missing to raise: Greek/Armenian look-alikes, full Unicode confusables table,
and whole-script-confusable (all-Cyrillic domain mimicking all-Latin brand).*

### 7. Metacharacters (SQLi `'`, cmdi `` ` `` `|` `;` `$()`, XSS `<>`, null `\x00`, CRLF `\r\n`) — **18% → 100%**
The point we just raised. Contextual detectors (quote+SQL-operator,
backtick+command-word, CRLF+header-name) → all 11 → ALARM, **0 new FP** on
`don't`, `'hello'`, `a<b`, `` `print()` ``, `a|b`, `true|false`, `<b>` tag,
"bash scripting".
**Hardening round added** (`harden_cards`): template/expression injection —
`${jndi:ldap://…}` (Log4Shell CVE-2021-44228), `{{7*7}}` and
`{{config.__class__}}` SSTI, SpEL `T(Runtime).exec`, ERB `<%= system(…) %>` —
all → ALARM, **0 FP** on shell `${HOME}`, legit `{{ user.name }}`, `<%= @post.title %>`.
Contextual: `{{…}}` fires only with an operator or a dangerous keyword.
*Missing to raise: LDAP/NoSQL/XPath operator families; PowerShell cmdlets.*

### 8. Sensitive-path & exfiltration intent — **supplement + hardening**
Supplement flags `/etc/passwd`, `id_rsa`, `.env`, and EMAIL/URL + exfil-verb.
The "email"-as-noun false positive was removed.
**Hardening round added** (`harden_cards`): cloud-credential artifacts —
`~/.aws/credentials`, `~/.config/gcloud/…`, `~/.kube/config`, `.docker/config.json`,
`.npmrc`/`.pypirc`/`.netrc`, and `-----BEGIN … PRIVATE KEY-----` headers → ALARM;
DNS-exfil (`nslookup <long-hex-label>.evil.tld`) → WATCH (conservative). **0 FP**
on `aws` in prose, "config in your settings file", `git@github.com`.
*Missing to raise: Azure/OCI credential paths; base32 DNS-exfil label variants.*

### 9. Natural-language / semantic prompt injection — **0%, BLIND BY DESIGN**
"Ignore all previous instructions…" is structurally clean text. MSL judges what
a *sign* does, not what a *sentence means*. This is not a gap to patch in MSL —
it is the boundary of the tool. It belongs to a semantic layer sitting *beside*
MSL, not inside it.
*Missing to raise: out of scope for MSL; documented as the honest limit.*

### 10. ERG / context layer — **precision, not detection** (`erg_context`, `range_context`)
The largest remaining lever, now built as a first-cut. MSL says what a *sign* is;
this layer asks whether the FRAME corroborates operational intent — the ERG
"does the threat survive coarse-graining?" test. It **only softens**, under a
strict safety contract:
- acts only on a broad **MSL-core presence verdict** (signature ∈ MSL actions);
  the operational drafted cards (sqli, jndi, ip_metadata, homoglyph, …) carry
  their own signatures and are **immune** — never downgraded;
- softens only inside a benign **frame** — a question *about* the sign, a
  *definition* of it, or a legit *structural* use (`git@host:`, `${VAR}`, `{{ x }}`);
- if a real **operational token** is also present (sensitive path, live URL host,
  command chain, double traversal) it softens by **at most one notch**
  (ALARM→WATCH), never to OK.

`range_context.py` (24-threat regression battery): residual MSL-core FPs cleared;
threats still flagged **24/24**; **threats silenced to OK: 0** (safety gate held);
`"how do I read ../../etc/passwd?"` correctly softened ALARM→WATCH (still flagged);
`"fetch http://169.254.169.254/"` stays ALARM (metadata card immune).

**Adversarially hardened** (component check #2, `range_erg_attack.py`): a red-team
found a real bypass — a phishing domain (`paypal.com.evil.ru/verify`) wrapped in
*"is this safe?"* was cleared to OK (5 silenced). Fixed with two rules: a
**conclusive** MSL verdict is now **never cleared** (softened one notch at most),
and `_OPERATIONAL` recognizes phishing domain shape (TLD-in-the-middle, deep
multi-label). Re-run: **0 silenced**, phishing-in-a-question → WATCH, one benign
FP (`"how do I use ../?"`) traded OK→WATCH for the safety.
*Missing to raise: this is rule-based framing, not the full multi-scale ERG
engine; and it reduces FALSE POSITIVES only — it adds no semantic THREAT
detection (point 9 stays blind by design).*

### 11. Self-defense — the guard's own robustness (`guard.py`, `range_stress.py`)
A guard you can drown is not a guard. We attacked the analyzer *itself* and found
a real DoS: **10k invisible characters hung it** (my invisible card recomputed a
whole-string fact per invisible → O(n²)); **25k `/` took ~15 s** (MSL's slash
sign is ~O(n²)). Both are now closed.

- **Fixed the O(n²)** in the invisible card (compute shared facts once).
- **Self-defense front gate** (`self_defense`) — cheap, bounded pre-checks that
  bounce floods in **<1 ms** before any heavy work: oversized input → hold;
  invisible flood (>128 hidden chars) → ALARM; single-character flood (>40% one
  char — a wall of `/` or `.`) → ALARM; too many `/` → hold-and-chunk.
- **Time budget** (`guarded_analyze`) — wall-clock ceiling around analysis. Honest
  limitation, measured: it stops *our* code but the MSL core **swallows the
  in-process interrupt**, so MSL's slow signs are handled by the predict-and-hold
  `/` cap instead, and the production-grade backstop is a worker/subprocess timeout.

`range_stress.py`: 13 attack inputs (up to 10M chars, invisible/bidi/tag floods,
percent-bombs, ReDoS probes) — **all bounce in <10 ms, none hang, none crash**;
real threats still classified; legit prose (150k) analyzes in ~0.3 s.
Also fixed a **ReDoS** in the DNS-label regex (nested quantifier → linear).

**Component check #1 — fail-open vs fail-closed (`fail_closed.py`, `range_failopen.py`).**
Per-component threat review, part by part. The scariest finding first: the guard
was **fail-OPEN**. With no error handling, crashing *any single component* (MSL,
or any card — even one unrelated to the attack) or passing a non-string made the
whole guard throw; the near-universal caller pattern `try: v=guard(x) except:
allow()` then let the threat straight through. `range_failopen.py`: a real
SQL-injection **leaked 9 different ways** through the naive guard.
Fixed with defense-in-depth: **per-component isolation** (`safe_reader` — a
crashed card yields WATCH, not silence; the others still run) + a **fail-closed
envelope** (`safe_analyze` — non-text input or any uncaught error → a blocking
verdict, never OK). Same battery: **0 leaks**. The whole assembly is now the
canonical front door `product.py` — `analyze()` is DoS-guarded, per-component
isolated, fail-closed, and **never throws** on any input (verified on objects,
lists, surrogates, oversized).
**Component check #3 — per-card stress (`range_cards_stress.py`).** Each card hit
on its own with inputs shaped to its regex (ReDoS probes, heavy repetition, nasty
unicode). Found **4 cards with ReDoS** (metachar CRLF, harden JNDI/SSTI/SpEL, digit
confusable, supplement EMAIL) — each hung on a crafted 100k input. The assembled
guard's DoS gate bounces these, but the cards were landmines on their own. Fixed
at the source: **bounded every greedy wildcard** (`[^}]*`→`[^}]{0,200}`,
`\s*`→`[ \t]{0,16}`) + cheap literal guards. Re-run: all 7 components healthy,
<65 ms, no hangs, no throws — and detection unchanged (metachar 11/11, harden
15/15, digit 14/14, 0 new FP).

**Component check #4 — poisoned component / supply-chain (`range_fake_component.py`,
`integrity.py`, `range_integrity.py`).** What if an attacker slips in a fake
component? Empirical result: a fake **card** is harmless — it is *add-only*, it
cannot clear a real alarm (severity-max combine); its worst is noise or a crash
(contained by isolation). But a fake **integrator** or fake **ERG** *can lower* a
verdict → silent bypass. Those are the trusted core. Defense: an **integrity
gate** — every component checked at load against an author-signed manifest of
hashes; anything MISSING / TAMPERED / UNKNOWN → the guard **refuses to start**
(fail-closed). This is the conveyor discipline enforced in code: a component the
author did not close and sign never runs.
**Component check #4c — provenance gate (`provenance.py`, `range_provenance.py`),
applying the Notarius idea (`docs/NOTARIUS.md`).** The hash gate answers "did it
change?" but not "is it NATIVE?" — `SIGNED ≠ NATIVE`. Demonstrated the attack the
hash gate MISSES: an attacker swaps in a backdoored ERG **and regenerates the
manifest** with the correct hash → **hash-only gate accepts it (BYPASS)**. The
provenance gate refuses it (`FORGED_LINEAGE`) because each component carries an
author-**signed lineage** the attacker cannot mint without the author's key, plus
a crypto-free **codepoint-length witness** (catches invisible insertions: ZWSP
shifted 3898→3899). Provenance record = `{hash (integrity) + cp_len (insertion
witness) + signed lineage (native origin)}`. This is the author's conveyor
discipline enforced in code.
**Component check #5 — the malicious author / SIGNED ≠ SAFE (`behavioral.py`,
`range_malicious_author.py`).** The hard limit of any signature: if the attacker
IS the author (or stole the key), they sign a backdoor and provenance accepts it
as NATIVE. Signature proves ORIGIN, not safety. What still holds:
- a signed malicious **card** cannot bypass — add-only (check #4), so the easy
  attack fails structurally (verified: threat stays ALARM);
- a signed backdoored **ERG** passes provenance (NATIVE) but is caught by a
  **behavioral acceptance gate** — every lowering component must pass a fixed
  adversarial battery at load; a backdoor that silences known threats is rejected
  no matter who signed it (verified: silences 8/8 → REJECT). No signature waives it.
Residual (a subtle backdoor that passes the battery) is closed organizationally:
**m-of-n sign-off** on lowering components + an **append-only transparency log**
(malice is signed = visible + accountable). Defense in depth, not a silver bullet.
**Component check #6 — m-of-n quorum + transparency log (`quorum.py`,
`transparency.py`, `range_quorum.py`).** The residual from #5, closed
organizationally. A change to a **lowering** component (ERG / integrator) needs
**M-of-N distinct signatures** (demo: 3-of-5) — one compromised key is not enough.
Verified: 1 valid signature → REJECT; the same signer replayed 3× → REJECT
(counts once); an unauthorised key → not counted; 3 distinct board members →
ACCEPT; a normal add-only card still needs only 1. Every sign-off is written to an
**append-only, hash-chained transparency log** — erasing or altering a past entry
breaks the chain and is detected (verified: tampering entry #3 → chain invalid at
seq 3). No lone key pushes a lowering component; no sign-off happens in secret.
*Missing to raise: process-isolation timeout for the MSL call; wire
integrity+provenance+behavioral+quorum into `product.py` startup; real asymmetric
signatures; a real signer-identity/PKI and log-witness gossip for the log.*

---

## Security posture — the six component checks at a glance

| # | check | finding | status |
|---|---|---|---|
| 1 | integrators fail-open/closed | SQLi leaked 9 ways when a part crashed | ✅ fail-closed, 0 leaks |
| 2 | ERG adversarial bypass | phishing-in-a-question silenced 5 threats | ✅ 0 silenced |
| 3 | per-card stress | 4 cards had ReDoS (hung) | ✅ all healthy <65 ms |
| 4 | poisoned component | fake integrator/ERG could lower a verdict | ✅ integrity gate + core isolation |
| 5 | malicious author (SIGNED≠SAFE) | valid signature can make a backdoor NATIVE | ✅ behavioral battery rejects it |
| 6 | one key / secret sign-off | a lone author could push a lowering change | ✅ m-of-n + transparency log |
| 7 | query-time injection via output | a card echoed raw ANSI into the admin-facing reason | ✅ safe_view sanitizes, 1/5→0/5 |
| 8 | 5-reviewer conveyor on ERG | 3 CRITICAL + 3 HIGH bypasses (data:URI XSS/dropper, `..\\..` traversal, credential recon, chmod) cleared to OK by phrasing — missed by check #2 | ✅ denylist removed; mask-and-rescan; 0/7 bypass, FPs restored where provable |

The guard defends the input (detection + DoS), defends itself (fail-closed,
per-component isolation), and defends its own supply chain (integrity →
provenance → behavior → quorum → transparency). Each layer is measured, not
claimed; every number reproduces from `code/range/`.

---

## Honest false positives still present at BASELINE

Two benign inputs the **real MSL** flags on its own (not our drafts):

- `"How do I use ../ in a relative import?"` → ALARM (traversal token in a
  question about traversal).
- `"In URLs, %2f is the code for a slash"` → WATCH (canon reveals `/`).

Plus WATCH-level ones from MSL's own `queue_for_review` cards: `${HOME}`,
`{{ title }}`, `git@github.com`, `the / character is the code for…`.

**These are now cleared by the ERG/context layer (point 10) — with a proven
0-threats-silenced safety gate.** See below.

---

## Reading the map

The shape is consistent: **MSL baseline is strong exactly where a sign's
danger is structural and encoding-carried** (traversal, encoding, bidi), and
**blind exactly where danger needs a lookup or a meaning** (which brand does
this mimic? is this IP internal? does this sentence intend harm?).

The drafted cards close the *lookup* gaps (brand set, IP classes, confusable
tables, metachar grammars) — deterministically, with no heavy database — and
leave the *meaning* gap to a semantic layer by design.
