# Author decisions — the log · Журнал авторских решений

AUTHOR / АВТОР: Руслан Малявский · STATUS / СТАТУС: `WORKING DOCUMENT` · 2026-07-22

🇬🇧 [English](#english) · 🇷🇺 [Русский](#русский)

---

Every non-obvious choice in this codebase, in one place, with its reason. The
rationale is not invented here — it is consolidated from the detectors' own
docstrings, the commit history, and the cross-review with the **NOTARIUS**
repository (a sibling project: strong provenance cryptography, naive detection —
the mirror image of this one). Where a decision rejects an approach, the reason
it was rejected is recorded so it is not silently re-tried.

Format: **Decision / Rationale / Status**. Status is one of `ADOPTED`,
`REJECTED`, `DEFERRED`.

---

<a name="english"></a>
## English

### Detection — the confusable / homoglyph front

**AD-1 · The core law is LOOKS_SAME ≠ IS_SAME.**
Decision: the confusable detector keys on the *identity* of a codepoint, not its
rendered shape. `paypal.com` and `pаypal.com` render alike; the second carries a
Cyrillic `а` (U+0430).
Rationale: rendering is the attack surface; identity is ground truth.
Status: `ADOPTED` (code/range/confusable_cards.py).

**AD-2 · The signal is script MIX within one token — not "a foreign letter exists".**
Decision: ALARM when a single token mixes Latin with Cyrillic/Greek lookalikes,
not merely because a non-Latin letter is present.
Rationale: "a non-Latin letter exists" would flag all Russian, all Greek — every
native word. The deception is the *mix inside one token*, or a wholly-foreign
token impersonating a known target.
Status: `ADOPTED`.

**AD-3 · A blanket "whole-script, no native anchor → WATCH" rule was rejected.**
Decision: whole-script confusion is gated on a target skeleton (DEMO_TARGETS),
not flagged on its own.
Rationale: simulated, the blanket rule fired on ~25% of common Russian words
(соус, орех, хор …) — legitimate words built from letters that happen to be
Latin lookalikes. Whole-script confusion is only meaningful *relative to a
target*.
Status: `REJECTED` (the blanket rule); target-gating `ADOPTED`.

**AD-4 · Roman-numeral forms are checked BEFORE the ≥2-letter gate.**
Decision: the Roman-numeral and non-ASCII-dash branches run before the
`len(letters) < 2: continue` gate.
Rationale: a Roman-numeral letter-form (e.g. `Ⅼ` U+216C) is Unicode category Nl,
so `_letters()` does not count it. A short token like `ⅬG` (one ASCII letter +
one Roman form) was therefore skipped and slipped through — a real false-negative
(fixed in commit 8deaf9a; pinned by test_confusable::
test_roman_numeral_short_token_regression).
Status: `ADOPTED`.

**AD-5 · A non-ASCII dash is a spoof only inside a domain-like token.**
Decision: a confusable dash (U+2010, U+2011, U+2013 …) ALARMs only when the token
contains a dot; in ordinary prose it stays OK.
Rationale: `pay‐pal.com` is a domain spoof; `a well‐known author` is legitimate
typography. The dot is the domain tell.
Status: `ADOPTED`.

### Detection — the invisible / bidi front

**AD-6 · Invisibles use a three-way verdict: ALARM / OK / WATCH.**
Decision: a proven smuggle ALARMs; provable legit glue is cleared to OK; an
invisible that is neither is WATCHed (non-conclusive).
Rationale: MSL alone flags an uncarded invisible as a witness but cannot tell a
smuggle from emoji glue — that is context, and context is this layer's job.
Status: `ADOPTED` (code/range/invisible_cards.py).

**AD-7 · Legit glue is vouched narrowly; ZWSP/ZWNJ/BOM/WJ/SHY are never auto-vouched.**
Decision: only ZWJ between emoji, one variation selector on a valid base, a tag
char after a flag base, and *balanced* bidi are cleared. The word-splitting
invisibles are never auto-cleared.
Rationale: those five have no legitimate role inside a word, so their presence
there is signal, not glue.
Status: `ADOPTED`.

**AD-8 · Variation selectors are a SEPARATE detector because they are Mn, not Cf.**
Decision: variation selectors get their own branch (vs_cards.py) rather than
riding the invisible detector.
Rationale: they are Unicode general category **Mn (Nonspacing_Mark), not Cf
(Format)**. The usual "strip all format chars" cleanup reflex misses every one of
them — exactly the gap the emoji-variation-selector smuggling technique exploits.
Status: `ADOPTED`.

### Trust core — provenance, quorum, transparency, integrity

**AD-9 · INTEGRITY ≠ PROVENANCE; SIGNED ≠ NATIVE.**
Decision: two distinct layers — a hash answers "did the container change since the
manifest?"; provenance answers "is this element of legitimate origin?".
Rationale: an attacker who swaps a component AND regenerates the manifest passes a
pure-hash check. A valid signature proves *who attested*, not that the text is
native.
Status: `ADOPTED` (provenance.py, integrity.py).

**AD-10 · A lowering change needs an M-of-N quorum.**
Decision: a change to a component that can LOWER a verdict (ERG / integrator)
requires ≥3 distinct authorised signatures; add-only cards need 1.
Rationale: one stolen or malicious key must not be enough to sign a backdoor that
passes the behavioral battery. Closing that is organizational, not cryptographic.
Status: `ADOPTED` (quorum.py).

**AD-11 · The transparency log is hash-chained and takes time from the caller.**
Decision: an append-only log where each entry commits to the previous one; the
timestamp is passed in by the caller.
Rationale: chaining makes silent removal/alteration detectable; caller-supplied
time keeps the log deterministic and reproducible, and chain integrity does not
depend on it.
Status: `ADOPTED` (transparency.py).

**AD-12 · Signing stays HMAC in-repo; Ed25519 is the sanctioned production upgrade — DEFERRED.**
Decision: provenance/quorum sign with HMAC in this repository; the asymmetric
(Ed25519) upgrade is documented but not vendored in.
Rationale: from the NOTARIUS review, its `envelope_v2.py`/`trace.py` show the
real asymmetric path (author signs with a private key; the gate verifies with the
public key), which closes the HMAC symmetry defect. It is **deferred here** for
two concrete reasons: (a) no Ed25519 provider is installed in this environment
(no PyNaCl, no `cryptography`), so vendoring it would add an unrunnable hard
dependency to a security project; (b) provenance and quorum are quorum-protected
lowering components — swapping their signing primitive is itself an M-of-N change
(AD-10), not a drive-by edit. The security property (you cannot mint NATIVE
provenance without the author's key) is identical under both; only key management
differs.
Status: `DEFERRED` (upgrade path recorded; adopt when a crypto provider is present
and under quorum).

### Method — how the project keeps itself honest

**AD-13 · coverage_lock keeps cards and detector tables in sync, both directions, with no generator.**
Decision: a regression lock asserts (A) every detector homoglyph codepoint has a
full EN+RU card and (B) every homoglyph-family card names a codepoint the detector
actually backs.
Rationale: the card spec and the detector tables are two independent sources of
truth; without a bidirectional lock the manual contract drifts silently. A
generator was avoided so neither side becomes derived/second-class.
Status: `ADOPTED` (code/tools/coverage_lock.py).

**AD-14 · A real assert-based test layer was added, adopted from the NOTARIUS review.**
Decision: a standalone test runner (code/tests/) with hard assertions on each
detector's contract — including a behavioral lock on every table codepoint and
the `ⅬG` false-negative regression.
Rationale: the NOTARIUS repo carried 109 real pytest asserts; this project drove
whole scenarios through range_*.py harnesses but pinned no individual contract,
and the `ⅬG` bug lived in exactly that gap. The runner needs no pytest (there is
none in this environment) yet stays pytest-collectable. 27 tests / 221 checks at
adoption.
Status: `ADOPTED` (code/tests/run_tests.py).

**AD-15 · NOTARIUS's custody / carrier / human-fingerprint machinery was reviewed and NOT taken.**
Decision: Shamir M-of-N custody, mortal TTL carriers, heartbeat/death-pulse, and
the PGP-wordlist human fingerprint stay in NOTARIUS.
Rationale: they solve *secret-splitting and key custody*. Vakhter holds no secret
to split and no key for a human to verify; importing them would be scope creep.
The scanner trichotomy NOTARIUS uses (HIGH/MEDIUM/LIKELY_LEGITIMATE) is already
superseded here by the ALARM/OK/WATCH layer (AD-6) plus the Mn insight (AD-8), so
that too was recorded rather than imported.
Status: `REJECTED` (import); recorded for provenance of the decision.

### Detection — prioritisation and the fullwidth carrier

**AD-16 · New confusable/carrier work is prioritised by real-world attack frequency; fullwidth folds in canonicalization.**
Decision: the confusable table is extended by how often a form is actually abused,
not alphabetically. Under that rule Cyrillic к (U+043A) → k was added (the last
common single-substitution Cyrillic look-alike; the mixed-script check already
fires when any foreign letter is a confusable, so the only real gap is a
single-swap token whose one letter is absent). The next-frequency vector,
fullwidth ASCII (U+FF01–FF5E, U+3000), is handled by FOLDING it to ASCII in the
canonicalization pre-pass — not by a new detector.
Rationale: fullwidth is a compatibility CARRIER, not a script mix, so its home is
the "double bottom" pre-pass beside overlong-UTF8: peel the carrier, let the
readers judge the real sign (fullwidth ＜script＞ / IP / ../ now surface). Scope is
kept to the fullwidth ASCII block only — halfwidth katakana (FF61–FF9F), the
fullwidth white brackets (FF5F–FF60) and real CJK are left untouched — so the fold
adds 0 false positives. `м`/`т`/`ь` were considered and REJECTED as confusables:
they are not in UTS #39 and their glyphs are not reliably ASCII-confusable, and a
security table must not assert a look-alike that isn't one.
Status: `ADOPTED` (code/canonicalization/canonicalize.py :: fold_fullwidth;
code/tests/test_fullwidth.py).

**AD-17 · Mathematical-alphanumeric styling is folded to ASCII in the pre-pass, from a curated source.**
Decision: math-alphanumeric letters/digits (𝐛𝐨𝐥𝐝, 𝘪𝘵𝘢𝘭𝘪𝘤, 𝔻𝕠𝕦𝕓𝕝𝕖-𝕤𝕥𝕣𝕦𝕔𝕜,
𝗌𝖺𝗇𝗌, monospace) fold to ASCII in canonicalization, next after fullwidth by
real-world frequency, with a `math_styled` witness flag.
Rationale: same carrier logic as AD-16 — pure styling, not a script mix. The map
is built once at import from a NARROW source: the Mathematical Alphanumeric
Symbols block (U+1D400–1D7FF) plus the ~29 math styles that live as holes in the
Letterlike Symbols block (ℂ ℬ ℑ ℝ …), taking the ASCII value from NFKC. Using
full NFKC was rejected as too broad (it also folds ½, ², ﬁ, ㎏ …); the curated
source keeps ordinary compatibility characters (², ½, №, ™, Ω, ℹ) untouched → 0
false positives. U+210E PLANCK CONSTANT is added by hand because it is the math
italic h but its Unicode name carries no style keyword, so the name filter misses
it (a unit test caught this).
Status: `ADOPTED` (code/canonicalization/canonicalize.py :: fold_math_alnum;
code/tests/test_math_alnum.py).

**AD-18 · The two brand-mimicry detectors share ONE frequency-ordered brand corpus.**
Decision: the digit-leet detector (digit_cards) and the whole-script branch
(confusable_cards) read a single `brand_corpus.py` instead of two private
hard-coded lists. The corpus is ordered by real-world impersonation frequency.
Rationale: the two lists had drifted (21 vs 10 brands) — the exact silent-drift
failure AD-13 exists to prevent, now removed by a shared source of truth. Two
consumers, two FP profiles, so the corpus exposes a length gate: the whole-script
branch uses only targets of length ≥5 (`WHOLE_SCRIPT_TARGETS`), because a short
all-foreign skeleton could collide with a real short word, while the digit-leet
branch is already gated by the digit-present requirement and safely uses the full
set (`PHISHING_BRANDS`). It stays a curated demo corpus; production swaps the list
in one place.
Status: `ADOPTED` (code/range/brand_corpus.py; code/tests/test_brand_corpus.py).

**AD-19 · Non-ASCII dot/slash separators are detected in the table, not as per-sign cards, gated between Latin letters.**
Decision: homoglyph separators — dots (U+2024 ․, U+3002 。, U+FF61 ｡, U+06D4 ۔) and
slashes (U+2044 ⁄, U+2215 ∕, U+29F8 ⧸) — join NASCII_DASH as detector tables with
a branch, and get NO SIGN_CORE_CARD.
Rationale: a separator is not a letter, so the letter-oriented card template does
not fit it, and coverage_lock only requires cards for the letter families
(GREEK_/CYRILLIC_/ROMAN_) — the same treatment the existing non-ASCII dash already
gets. Detection fires ONLY when the confusable sits BETWEEN two ASCII-Latin
letters (paypal․com), which is the domain-separator signature: it keeps a CJK or
Arabic sentence-final full stop (preceded by non-Latin) and a real fraction slash
(digits around it) clean → 0 false positives. Fullwidth full stop/solidus
(U+FF0E/FF0F) are intentionally absent here — they are already peeled by the
canonicalization fold (AD-16).
Status: `ADOPTED` (code/range/confusable_cards.py; code/tests/test_domain_separator.py).

**AD-20 · Visual-multigraph brand mimicry is adopted; raw edit-distance-1 is rejected.**
Decision: brand look-alikes that carry no digit — rn→m (arnazon), vv→w
(vvhatsapp), cl→d, and capital-I-for-lowercase-l (paypaI, googIe) — are detected
by de-confusing a label with those specific folds and matching the shared brand
corpus. General edit-distance-1 matching is NOT adopted.
Rationale: the fold-then-exact-match rule is FP-safe — it fires only when a fold
lands exactly on a brand AND the label is not already that brand, so legit brand
mentions and ordinary words with rn/vv/cl/I stay clean (0 FP across a 90-word
benign corpus). Raw edit-distance-1 was tested and rejected: short brands make it
unsafe (visas~visa, beta~meta, phase~chase, team/steal~steam would all fire), and
distinguishing a typo-squat from a real word needs a dictionary the tool does not
carry. A `len>=5` gate skips short labels. This is the fallback the 3-step plan
reserved for step 2.
Status: `ADOPTED` (fold subset) / `REJECTED` (raw ed-1); code/range/digit_cards.py
:: _visual_brand; code/tests/test_brand_visual.py.

**AD-21 · Non-ASCII whitespace is folded to an ASCII space; zero-width marks are not.**
Decision: NBSP (U+00A0), the en/em/thin/hair spaces (U+2000–200A), U+202F, U+205F
and the ogham space (U+1680) fold to a plain ASCII space in canonicalization, with
a `weird_space` witness flag — the last compatibility carrier after fullwidth and
math.
Rationale: honest scope — our readers are structure-based, so this is
normalization + a witness, not a new structural detector; its value is one
canonical spacing for anything downstream plus a recorded carrier. Zero-width
marks (U+200B/200C/200D/FEFF) are explicitly EXCLUDED — they are invisible
smuggles owned by the invisible detector, and folding them to a space would both
lose that signal and misrepresent them. U+3000 is already covered by the
fullwidth fold. Benign typography (NBSP/thin space in prose and number grouping)
folds to normal spacing → 0 false positives.
Status: `ADOPTED` (code/canonicalization/canonicalize.py :: fold_spaces;
code/tests/test_space_fold.py).

**AD-22 · The rich confusable detector is wired into the assembled guard.**
Decision: `confusable_cards_reader` joins `_READERS` in product.py, so `analyze()`
judges the full homoglyph surface (Greek, Roman-numeral forms, extended Cyrillic,
whole-script, non-ASCII dash/dot/slash — 76 locked forms) instead of only the
light dot-gated Cyrillic check that digit_cards carries.
Rationale: the rich detector was built and locked over this series but lived only
as a draft simulator (measured by range_confusable), NOT in the front door — so
the guard silently missed most homoglyph attacks. A reader can only raise
severity (findings combine by max), so wiring it can add detection or false
positives but never remove either; it was therefore gated on a full regression
sweep. Result: the guard now flags Greek/Cyrillic/Roman/whole-script/dot-separator
spoofs that were previously CLEAN through analyze(), with 0 new false positives
across every range_* benign corpus and the ERG safety gate still silencing 0
threats. self_defense bounces floods before the reader, so no DoS surface is
added.
Status: `ADOPTED` (code/range/product.py; code/tests/test_guard_confusable.py).

**AD-23 · Every built detector is audited against the guard's reader list; three more smuggle detectors wired.**
Decision: after AD-22, audit ALL `*_reader` functions against `product._READERS`
and wire the ones that catch a real attack the guard misses. This adds
whitespace_cards (U+2028/2029 line/paragraph separators), hangul_filler_cards
(U+3164 & jamo fillers) and prepended_format_cards (Arabic/Syriac number signs,
interlinear annotation). vs_cards / tag_cards / bidi_cards / canonical_view /
urlpunct were left OUT — the invisible detector and others already cover their
sampled attacks, so wiring them would be redundant.
Rationale: a detector that is built, locked and tested but not in `_READERS` gives
zero protection — the same "built but not connected" gap AD-22 fixed for
confusables. The three added are conclusive-smuggle detectors, FP-safe by design
(a filler flanked by Hangul jamo is OK; a number sign prefixing its own script's
digits is OK), and verified 0-FP on legit Korean/Arabic/CJK before wiring. The
whitespace space-lookalike branch is largely pre-empted by the AD-21 space fold
(NBSP etc. are already ASCII by the time the reader runs), leaving it the
line-separator class the fold deliberately does not touch.
Status: `ADOPTED` (code/range/product.py; code/tests/test_guard_smuggles.py).

**AD-24 · An adversarial sweep through the wired guard drove the next round of threat coverage.**
Decision: after wiring everything (AD-22/23), run a broad attack battery through
`analyze()` and close every conclusive attack that came back CLEAN. Six gaps were
found and fixed: UNC / Windows-backslash paths, LDAP injection, NoSQL injection,
PowerShell stealth/encoded execution (+ LOLBins, curl|sh), short-form IPv4
(http://127.1/) and IPv6-with-zone SSRF.
Rationale: a completeness critic — once the guard runs every detector, the honest
question is what it still MISSES, not what it flags. Each fix is contextual and
FP-calibrated to the attack's specific shape (LDAP only on wildcard-paren /
boolean-chaining / attr=* ; NoSQL only on a quoted "$op" key or [$op] param;
short-form IP only URL-gated; PowerShell only on -enc/stealth flags), and every
new regex is bounded + flat (ReDoS-safe, verified <26 ms on 60 k inputs). 0 new
false positives across all range_* benign corpora; range_meta and range_harden
stay at 100%.
Status: `ADOPTED` (code/range/harden_cards.py, code/range/metachar_cards.py;
code/tests/test_execution_windows.py, code/tests/test_injection_ssrf.py).

**AD-25 · A second adversarial round adds Armenian homoglyphs and round-2 injection/RCE; some classes are deliberately out of scope.**
Decision: re-sweep the guard (loop-until-dry). Added: Armenian look-alikes (a
conservative, verified set օ/ո/ս/ա/Օ → o/n/u/a/O, joining Cyrillic/Greek), SQL
stacked queries, Java/PHP deserialization magic, exotic SSRF schemes
(gopher/dict/…), and JS prototype pollution. Left OUT on purpose: raw
credential-format scanning (AWS AKIA…, GitHub ghp_…, JWT, Slack tokens) is
data-loss prevention, a different mission from attack-detection; Georgian is not a
genuine Latin-confusable script (Mkhedruli is distinctive); Cherokee IS a real
confusable script but needs a verified mapping table (a follow-up, not guessed);
pickle/XStream gadgets are niche/binary and hard to detect in text without FP.
Rationale: keep expanding by real attack shape, but a security table must assert
only verified look-alikes and the guard should not silently take on a DLP mission
it was not scoped for. All new patterns are contextual, FP-calibrated and
ReDoS-safe; 0 new false positives.
Status: `ADOPTED` (confusable_cards ARM_TO_LAT; metachar/harden round-2;
test_armenian.py, test_rce_round2.py) / `DEFERRED` (Cherokee cards, secret-format
DLP).

**AD-26 · Cherokee is detected by a hard-mix rule, not a guessed look-alike table.**
Decision: Cherokee (a documented IDN-spoof syllabary) is flagged when a single
token mixes Latin with Cherokee — the mix itself is conclusive — WITHOUT a
per-letter Cherokee→Latin table.
Rationale: AD-25 refused to guess Cherokee equivalences, and a security table must
not assert unverified look-alikes. But the equivalences aren't needed: the
detector's core law is that a script MIX within a token is the tell (AD-2), and —
unlike CJK, where "IDカード" / "iPhone12" are normal tokens — no language
interleaves Latin with Cherokee mid-token, so the mix alone is anomalous. This is
strictly script-specific: only "hard-mix" scripts (Cherokee) are treated this way,
so Japanese/CJK Latin-mixing and pure single-script Cherokee (ᏣᎳᎩ) stay clean
(verified 0 FP). The trade-off vs the Cyrillic/Greek/Armenian tables: no impersonated
skeleton is shown, only the anomaly — an honest reflection of what is verified.
Status: `ADOPTED` (code/range/confusable_cards.py hard-mix branch;
code/tests/test_cherokee.py).

**AD-27 · Armenian is promoted to a carded family; ERG-softening immunity is audited and pinned.**
Decision: (a) Armenian gets five first-class per-sign cards (օ/ո/ս/ա/Օ) tracked by
coverage_lock (ARM_TO_LAT + ARMENIAN_ family, LOCKED 81), while Cherokee stays
card-less by design (a method note, docs/CHEROKEE_HARD_MIX.md). (b) The ERG
context layer — the only component that can LOWER a verdict — is audited against
every detector added this cycle, and the audit is made a permanent regression
test.
Rationale: after expanding detection so broadly, the real risk is not a missed
attack but a *silenced* one — ERG wrongly clearing a new conclusive finding under
a benign frame. ERG's contract already makes drafted-card signatures immune (it
softens only MSL-core action signatures, and never clears a conclusive ALARM to
OK), but "immune by contract" is verified, not assumed: 14 new attack classes
wrapped in the softening trigger ("is it safe…?", "explain…", "for example…") all
stay blocked (0 silenced). test_erg_immunity.py pins this so a future ERG change
cannot silently start clearing them.
Status: `ADOPTED` (sign_cards ARMENIAN_*; coverage_lock ARM; docs/CHEROKEE_HARD_MIX.md;
code/tests/test_erg_immunity.py).

---

<a name="русский"></a>
## Русский

Каждый неочевидный выбор в этом коде — в одном месте, с обоснованием. Обоснование
здесь не выдумано: оно сведено из докстрингов самих детекторов, истории коммитов и
кросс-обзора с репозиторием **NOTARIUS** (родственный проект: сильная криптография
провенанса, наивная детекция — зеркало этого). Где решение что-то отвергает,
причина отказа записана, чтобы её не пробовали заново.

Формат: **Решение / Обоснование / Статус**. Статус — `ПРИНЯТО`, `ОТВЕРГНУТО`,
`ОТЛОЖЕНО`.

### Детекция — фронт конфузаблов / гомоглифов

**AD-1 · Основной закон: ВЫГЛЯДИТ_ОДИНАКОВО ≠ ЯВЛЯЕТСЯ_ТЕМ_ЖЕ.**
Решение: детектор смотрит на *идентичность* кодпоинта, а не на нарисованную
форму. `paypal.com` и `pаypal.com` выглядят одинаково; во втором — кириллическая
`а` (U+0430).
Обоснование: рендер — поверхность атаки; идентичность — истина.
Статус: `ПРИНЯТО`.

**AD-2 · Сигнал — СМЕШЕНИЕ письменностей внутри одного токена, а не «есть чужая буква».**
Решение: тревога, когда один токен смешивает латиницу с кирилло/греческими
двойниками, а не просто из-за наличия нелатинской буквы.
Обоснование: правило «есть нелатинская буква» пометило бы весь русский и весь
греческий — каждое родное слово. Обман — это *смесь внутри токена* или целиком
чужой токен, выдающий себя за известную цель.
Статус: `ПРИНЯТО`.

**AD-3 · Огульное «целиком чужой, без родного якоря → WATCH» отвергнуто.**
Решение: путаница целой письменностью срабатывает только по скелету-цели
(DEMO_TARGETS), сама по себе — нет.
Обоснование: в симуляции огульное правило било по ~25% обычных русских слов
(соус, орех, хор …) — законных слов из букв, случайно похожих на латиницу.
Путаница целой письменностью осмысленна лишь *относительно цели*.
Статус: `ОТВЕРГНУТО` (огульное правило); привязка к цели — `ПРИНЯТО`.

**AD-4 · Римские цифры проверяются ДО барьера «≥2 букв».**
Решение: ветки римских цифр и не-ASCII-дефиса идут до барьера
`len(letters) < 2: continue`.
Обоснование: форма римской цифры (напр. `Ⅼ` U+216C) — категория Unicode Nl, и
`_letters()` её не считает. Короткий токен `ⅬG` (одна ASCII-буква + одна римская
форма) поэтому пропускался — реальный ложноотрицательный (починен в 8deaf9a;
закреплён test_confusable::test_roman_numeral_short_token_regression).
Статус: `ПРИНЯТО`.

**AD-5 · Не-ASCII-дефис — подмена только внутри доменоподобного токена.**
Решение: конфузабл-дефис (U+2010, U+2011, U+2013 …) даёт тревогу лишь если в
токене есть точка; в обычной прозе — чисто.
Обоснование: `pay‐pal.com` — подмена домена; `a well‐known author` — законная
типографика. Точка — признак домена.
Статус: `ПРИНЯТО`.

### Детекция — фронт невидимок / bidi

**AD-6 · У невидимок трёхзначный вердикт: ALARM / OK / WATCH.**
Решение: доказанная контрабанда — тревога; доказуемый законный «клей» — чисто;
невидимка, которая ни то ни другое — WATCH (неокончательно).
Обоснование: сам MSL помечает некартированную невидимку как свидетеля, но не
отличает контрабанду от эмодзи-клея — это контекст, а контекст — работа этого
слоя.
Статус: `ПРИНЯТО`.

**AD-7 · Законный клей заверяется узко; ZWSP/ZWNJ/BOM/WJ/SHY не заверяются никогда.**
Решение: чисто только ZWJ между эмодзи, один селектор вариации на валидной базе,
tag-символ после флаг-базы и *сбалансированный* bidi. Невидимки, рвущие слово, не
заверяются автоматически.
Обоснование: у этих пяти нет законной роли внутри слова, поэтому их присутствие
там — сигнал, а не клей.
Статус: `ПРИНЯТО`.

**AD-8 · Селекторы вариаций — ОТДЕЛЬНЫЙ детектор, потому что они Mn, а не Cf.**
Решение: селекторам вариаций дана своя ветка (vs_cards.py), а не общая с
невидимками.
Обоснование: они — категория Unicode **Mn (Nonspacing_Mark), а не Cf (Format)**.
Привычный рефлекс «вырезать все format-символы» пропускает их все — именно ту
щель, что эксплуатирует контрабанда через эмодзи-селекторы.
Статус: `ПРИНЯТО`.

### Ядро доверия — провенанс, кворум, прозрачность, целостность

**AD-9 · ЦЕЛОСТНОСТЬ ≠ ПРОВЕНАНС; ПОДПИСАНО ≠ РОДНОЕ.**
Решение: два разных слоя — хеш отвечает «менялся ли контейнер с момента
манифеста?»; провенанс — «законного ли происхождения элемент?».
Обоснование: атакующий, подменивший компонент И перегенерировавший манифест,
проходит чистую хеш-проверку. Валидная подпись доказывает *кто заверил*, а не что
текст родной.
Статус: `ПРИНЯТО`.

**AD-10 · Понижающее изменение требует кворума M-из-N.**
Решение: изменение компонента, способного ПОНИЗИТЬ вердикт (ERG / интегратор),
требует ≥3 различных авторизованных подписей; add-only карточки — 1.
Обоснование: одного украденного или вредоносного ключа не должно хватать, чтобы
подписать бэкдор, проходящий поведенческую батарею. Это закрывается
организационно, не криптографически.
Статус: `ПРИНЯТО`.

**AD-11 · Лог прозрачности хеш-сцеплен и берёт время у вызывающего.**
Решение: append-only лог, где каждая запись коммитит предыдущую; отметка времени
передаётся вызывающим.
Обоснование: сцепление делает тихое удаление/подмену обнаружимыми; переданное
время держит лог детерминированным и воспроизводимым, а целостность цепи от него
не зависит.
Статус: `ПРИНЯТО`.

**AD-12 · Подпись остаётся HMAC в репозитории; Ed25519 — санкционированный боевой апгрейд — ОТЛОЖЕНО.**
Решение: провенанс/кворум подписывают HMAC в этом репозитории; асимметричный
(Ed25519) апгрейд задокументирован, но не внесён.
Обоснование: из обзора NOTARIUS его `envelope_v2.py`/`trace.py` показывают
реальный асимметричный путь (автор подписывает приватным ключом; шлюз проверяет
публичным), закрывающий дефект симметрии HMAC. Здесь **отложено** по двум
конкретным причинам: (а) в этой среде нет провайдера Ed25519 (ни PyNaCl, ни
`cryptography`), поэтому внесение добавило бы незапускаемую жёсткую зависимость в
security-проект; (б) провенанс и кворум — quorum-защищённые понижающие компоненты,
и смена их примитива подписи сама по себе есть изменение M-из-N (AD-10), а не
мимоходная правка. Свойство безопасности (нельзя выпустить РОДНОЙ провенанс без
ключа автора) идентично в обоих; различается лишь управление ключами.
Статус: `ОТЛОЖЕНО` (путь апгрейда зафиксирован; принять при наличии крипто-
провайдера и под кворумом).

### Метод — как проект держит себя честным

**AD-13 · coverage_lock держит карточки и таблицы детектора в синхроне, в обе стороны, без генератора.**
Решение: регрессионный замок утверждает (A) у каждого гомоглиф-кодпоинта детектора
есть полная пара карточек EN+RU и (B) каждая карточка гомоглиф-семейства называет
кодпоинт, который детектор реально поддерживает.
Обоснование: спецификация карточек и таблицы детектора — два независимых
источника истины; без двунаправленного замка ручной контракт тихо расходится.
Генератор намеренно не заведён, чтобы ни одна сторона не стала производной.
Статус: `ПРИНЯТО` (code/tools/coverage_lock.py).

**AD-14 · Добавлен настоящий тест-слой на ассертах, взятый из обзора NOTARIUS.**
Решение: автономный раннер (code/tests/) с жёсткими ассертами на контракт каждого
детектора — включая поведенческий замок на каждый кодпоинт таблиц и регрессию
ложноотрицательного `ⅬG`.
Обоснование: репозиторий NOTARIUS нёс 109 настоящих pytest-ассертов; этот проект
гонял целые сценарии через range_*.py, но не закреплял отдельный контракт, и баг
`ⅬG` жил ровно в этой щели. Раннер не требует pytest (его в среде нет), но
остаётся собираемым pytest'ом. На момент принятия — 27 тестов / 221 проверка.
Статус: `ПРИНЯТО` (code/tests/run_tests.py).

**AD-15 · Механика NOTARIUS (custody / carrier / человеческий отпечаток) рассмотрена и НЕ взята.**
Решение: Shamir M-из-N, смертные TTL-носители, heartbeat/death-pulse и
человеческий отпечаток по PGP-словарю остаются в NOTARIUS.
Обоснование: они решают *разделение секрета и хранение ключей*. У Вахтёра нет
секрета для разделения и ключа для сверки человеком; их импорт был бы расползанием
рамок. Трихотомию сканера NOTARIUS (HIGH/MEDIUM/LIKELY_LEGITIMATE) здесь уже
превосходит слой ALARM/OK/WATCH (AD-6) плюс инсайт про Mn (AD-8), поэтому и она
записана, а не импортирована.
Статус: `ОТВЕРГНУТО` (импорт); записано для провенанса решения.

### Детекция — приоритизация и полноширинный носитель

**AD-16 · Новая работа по двойникам/носителям приоритизируется по частоте атак в реальной жизни; fullwidth сворачивается в канонизации.**
Решение: таблица конфузаблов расширяется по тому, насколько часто форму реально
эксплуатируют, а не по алфавиту. По этому правилу добавлена кириллическая к
(U+043A) → k (последний ходовой односимвольный кириллический двойник; проверка
смешения письменностей уже срабатывает, если хоть одна чужая буква — конфузабл,
поэтому реальная дыра — только токен с единственной подменой, чья буква
отсутствует в таблице). Следующий по частоте вектор — полноширинный ASCII
(U+FF01–FF5E, U+3000) — закрыт СВОРАЧИВАНИЕМ в ASCII в пре-пассе канонизации, а не
новым детектором.
Обоснование: fullwidth — это компат-НОСИТЕЛЬ, а не смесь письменностей, поэтому
его место в «двойном дне» рядом с overlong-UTF8: снять носитель, дать детекторам
судить настоящий знак (fullwidth ＜script＞ / IP / ../ теперь всплывают). Область
ограничена только блоком fullwidth ASCII — halfwidth-катакана (FF61–FF9F),
полноширинные белые скобки (FF5F–FF60) и настоящий CJK не тронуты — поэтому fold
даёт 0 ложных срабатываний. `м`/`т`/`ь` рассмотрены и ОТВЕРГНУТЫ как конфузаблы:
их нет в UTS #39, а начертание не является надёжно ASCII-двойником; security-
таблица не должна утверждать сходство, которого нет.
Статус: `ПРИНЯТО` (code/canonicalization/canonicalize.py :: fold_fullwidth;
code/tests/test_fullwidth.py).

**AD-17 · Math-alphanumeric стилизация сворачивается в ASCII в пре-пассе, из курируемого источника.**
Решение: math-буквы/цифры (𝐛𝐨𝐥𝐝, 𝘪𝘵𝘢𝘭𝘪𝘤, 𝔻𝕠𝕦𝕓𝕝𝕖-𝕤𝕥𝕣𝕦𝕔𝕜, 𝗌𝖺𝗇𝗌, monospace)
сворачиваются в ASCII в канонизации — следующий за fullwidth по частоте — с флагом-
свидетелем `math_styled`.
Обоснование: та же логика носителя, что и AD-16 — чистая стилизация, не смесь
письменностей. Таблица строится один раз на импорте из УЗКОГО источника: блок
Mathematical Alphanumeric Symbols (U+1D400–1D7FF) плюс ~29 math-стилей, живущих
«дырами» в блоке Letterlike Symbols (ℂ ℬ ℑ ℝ …), значение ASCII берётся из NFKC.
Полный NFKC отвергнут как слишком широкий (свернул бы и ½, ², ﬁ, ㎏ …); курируемый
источник оставляет обычные компат-символы (², ½, №, ™, Ω, ℹ) нетронутыми → 0 ложных
срабатываний. U+210E PLANCK CONSTANT добавлена вручную: это math-курсивная h, но её
имя не несёт ключа стиля, и name-фильтр её пропускал (поймал юнит-тест).
Статус: `ПРИНЯТО` (code/canonicalization/canonicalize.py :: fold_math_alnum;
code/tests/test_math_alnum.py).

**AD-18 · Два детектора бренд-мимикрии делят ОДИН frequency-ранжированный корпус.**
Решение: leet-детектор (digit_cards) и whole-script ветка (confusable_cards)
читают единый `brand_corpus.py` вместо двух приватных хардкод-списков. Корпус
упорядочен по частоте имитации в реальной жизни.
Обоснование: списки разошлись (21 против 10 брендов) — ровно тот тихий дрейф,
против которого существует AD-13, теперь устранён единым источником правды. Два
потребителя — два профиля FP, поэтому корпус выставляет порог длины: whole-script
берёт только цели длиной ≥5 (`WHOLE_SCRIPT_TARGETS`), т.к. короткий целиком-чужой
скелет мог бы совпасть с реальным коротким словом, а leet-ветка уже отсечена
требованием наличия цифры и безопасно использует полный набор (`PHISHING_BRANDS`).
Остаётся курируемым демо-корпусом; прод меняет список в одном месте.
Статус: `ПРИНЯТО` (code/range/brand_corpus.py; code/tests/test_brand_corpus.py).

**AD-19 · Non-ASCII «точка»/«слэш»-разделители детектятся таблицей, без per-sign карточек, с гейтом «между латиницей».**
Решение: гомоглифы-разделители — точки (U+2024 ․, U+3002 。, U+FF61 ｡, U+06D4 ۔) и
слэши (U+2044 ⁄, U+2215 ∕, U+29F8 ⧸) — присоединяются к NASCII_DASH как таблицы
детектора с веткой, и карточки SIGN_CORE_CARD НЕ получают.
Обоснование: разделитель — не буква, letter-ориентированный шаблон ему не подходит,
а coverage_lock требует карточки только для буквенных семейств
(GREEK_/CYRILLIC_/ROMAN_) — ровно как уже сделано для non-ASCII дефиса. Детект
срабатывает ТОЛЬКО когда гомоглиф стоит МЕЖДУ двумя ASCII-латинскими буквами
(paypal․com) — это подпись доменного разделителя: японская/арабская концевая точка
(после не-латиницы) и настоящая дробь (цифры вокруг) остаются чистыми → 0 ложных
срабатываний. Полноширинные точка/слэш (U+FF0E/FF0F) здесь намеренно отсутствуют —
их уже снимает fold канонизации (AD-16).
Статус: `ПРИНЯТО` (code/range/confusable_cards.py; code/tests/test_domain_separator.py).

**AD-20 · Визуальные биграммы бренд-мимикрии приняты; сырой edit-distance-1 отвергнут.**
Решение: бренд-двойники без цифры — rn→m (arnazon), vv→w (vvhatsapp), cl→d и
заглавная-I-вместо-строчной-l (paypaI, googIe) — детектятся свёрткой метки этими
конкретными правилами и сверкой с общим бренд-корпусом. Общий edit-distance-1 НЕ
принят.
Обоснование: правило «свернуть → точное совпадение» FP-безопасно — срабатывает
только когда свёртка точно попадает в бренд И метка ещё не является этим брендом,
поэтому легит-упоминания брендов и обычные слова с rn/vv/cl/I остаются чистыми (0 FP
на 90-словном бенайн-корпусе). Сырой edit-distance-1 проверен и отвергнут: короткие
бренды делают его небезопасным (visas~visa, beta~meta, phase~chase, team/steal~steam
— все бы сработали), а отличить тайпосквот от настоящего слова без словаря нельзя.
Гейт `len>=5` пропускает короткие метки. Это запасной вариант, заложенный в план на
ступень 2.
Статус: `ПРИНЯТО` (подмножество свёрток) / `ОТВЕРГНУТО` (сырой ed-1);
code/range/digit_cards.py :: _visual_brand; code/tests/test_brand_visual.py.

**AD-21 · Non-ASCII пробелы сворачиваются в ASCII-пробел; zero-width — нет.**
Решение: NBSP (U+00A0), en/em/thin/hair пробелы (U+2000–200A), U+202F, U+205F и
ogham-пробел (U+1680) сворачиваются в обычный ASCII-пробел в канонизации, с флагом-
свидетелем `weird_space` — последний компат-носитель после fullwidth и math.
Обоснование: честная область — детекторы структурные, поэтому это нормализация +
свидетель, а не новый структурный детект; ценность — единое каноническое
расстановка пробелов для всего, что ниже по потоку, плюс зафиксированный носитель.
Zero-width метки (U+200B/200C/200D/FEFF) явно ИСКЛЮЧЕНЫ — это невидимые контрабанды
детектора невидимок, и сворачивание их в пробел и потеряло бы сигнал, и исказило бы
их. U+3000 уже покрыт fullwidth-fold. Обычная типографика (NBSP/тонкий пробел в
прозе и разрядке чисел) сворачивается в норму → 0 ложных срабатываний.
Статус: `ПРИНЯТО` (code/canonicalization/canonicalize.py :: fold_spaces;
code/tests/test_space_fold.py).

**AD-22 · Богатый confusable-детектор подключён в собранный гвард.**
Решение: `confusable_cards_reader` добавлен в `_READERS` в product.py, поэтому
`analyze()` судит всю гомоглиф-поверхность (греческий, римские формы, расширенная
кириллица, whole-script, non-ASCII дефис/точка/слэш — 76 запертых форм) вместо
только урезанной dot-gated кириллической проверки из digit_cards.
Обоснование: богатый детектор строился и запирался всю эту серию, но жил лишь как
draft-симулятор (мерялся range_confusable), а НЕ в парадной двери — поэтому гвард
тихо пропускал большинство гомоглиф-атак. Ридер может только повышать серьёзность
(находки сливаются по максимуму), поэтому подключение может добавить детект или
ложные срабатывания, но не убрать ни то ни другое; отсюда — полный регресс-прогон
перед принятием. Итог: гвард теперь ловит греческие/кириллические/римские/
whole-script/dot-разделитель спуфы, ранее CLEAN через analyze(), с 0 новых ложных
срабатываний по всем бенайн-корпусам range_* и safety-gate ERG по-прежнему глушит 0
угроз. self_defense гасит флуды до ридера, так что DoS-поверхность не добавляется.
Статус: `ПРИНЯТО` (code/range/product.py; code/tests/test_guard_confusable.py).

**AD-23 · Каждый построенный детектор сверен со списком ридеров гварда; подключены ещё три детектора контрабанды.**
Решение: после AD-22 — сверить ВСЕ `*_reader` функции с `product._READERS` и
подключить те, что ловят реальную атаку, пропускаемую гвардом. Добавлены
whitespace_cards (U+2028/2029 разделители строк/абзацев), hangul_filler_cards
(U+3164 и jamo-филлеры) и prepended_format_cards (арабские/сирийские number sign,
interlinear annotation). vs_cards / tag_cards / bidi_cards / canonical_view /
urlpunct НЕ подключены — детектор невидимок и другие уже покрывают их выборочные
атаки, подключение было бы избыточным.
Обоснование: детектор построенный, запертый и протестированный, но не в `_READERS`,
даёт ноль защиты — тот же разрыв «построено, но не подключено», что AD-22 закрыл
для конфузаблов. Три добавленных — детекторы окончательной контрабанды, FP-безопасны
по дизайну (филлер в окружении корейских jamo — OK; number sign перед своими цифрами
— OK), проверены на 0 FP на легит корейском/арабском/CJK до вайринга. Ветка
space-lookalike в whitespace во многом упреждена fold-ом пробелов из AD-21 (NBSP и
пр. уже ASCII к моменту ридера), оставляя ей класс разделителей строк, который fold
намеренно не трогает.
Статус: `ПРИНЯТО` (code/range/product.py; code/tests/test_guard_smuggles.py).

**AD-24 · Adversarial-прогон через подключённый гвард задал следующий раунд покрытия угроз.**
Решение: после подключения всего (AD-22/23) прогнать широкую батарею атак через
`analyze()` и закрыть каждую окончательную атаку, вернувшуюся CLEAN. Найдено и
исправлено шесть пробелов: UNC / Windows-backslash пути, LDAP-инъекция,
NoSQL-инъекция, PowerShell stealth/encoded исполнение (+ LOLBins, curl|sh),
short-form IPv4 (http://127.1/) и IPv6-with-zone SSRF.
Обоснование: критик полноты — раз гвард запускает все детекторы, честный вопрос не
что он флагует, а что ещё ПРОПУСКАЕТ. Каждое исправление контекстно и FP-калибровано
под конкретную форму атаки (LDAP только на wildcard-скобки / boolean-цепочки / attr=*;
NoSQL только на quoted-ключ "$op" или [$op] параметр; short-form IP только в
URL-контексте; PowerShell только на -enc/stealth-флагах), и каждый новый регекс
ограничен + плоский (ReDoS-безопасен, проверено <26 мс на 60k). 0 новых ложных
срабатываний по всем бенайн-корпусам range_*; range_meta и range_harden держат 100%.
Статус: `ПРИНЯТО` (code/range/harden_cards.py, code/range/metachar_cards.py;
code/tests/test_execution_windows.py, code/tests/test_injection_ssrf.py).

**AD-25 · Второй adversarial-раунд добавляет армянские гомоглифы и round-2 инъекции/RCE; часть классов намеренно вне рамок.**
Решение: перепрогон гварда (loop-until-dry). Добавлено: армянские двойники
(консервативный выверенный набор օ/ո/ս/ա/Օ → o/n/u/a/O, рядом с кириллицей/греческим),
SQL stacked-запросы, магия десериализации Java/PHP, экзотические SSRF-схемы
(gopher/dict/…), JS prototype pollution. Намеренно ИСКЛЮЧЕНО: сканирование форматов
секретов (AWS AKIA…, GitHub ghp_…, JWT, Slack-токены) — это DLP, иная миссия, чем
детекция атак; грузинский не является настоящим Latin-двойником (Мхедрули
самобытен); Cherokee — реальный confusable-скрипт, но нужна выверенная таблица
(follow-up, не угадывать); pickle/XStream-гаджеты нишевые/бинарные, трудно детектить
в тексте без FP. Обоснование: расширять по реальной форме атаки, но security-таблица
должна утверждать лишь выверенные двойники, а гвард не должен тихо брать DLP-миссию,
под которую не проектировался. Все новые паттерны контекстны, FP-калиброваны и
ReDoS-безопасны; 0 новых ложных срабатываний.
Статус: `ПРИНЯТО` (confusable_cards ARM_TO_LAT; metachar/harden round-2;
test_armenian.py, test_rce_round2.py) / `ОТЛОЖЕНО` (Cherokee-карточки, secret-format DLP).

**AD-26 · Cherokee детектится правилом hard-mix, а не угаданной таблицей двойников.**
Решение: Cherokee (задокументированный IDN-спуф-силлабарий) флагуется, когда один
токен смешивает латиницу с Cherokee — сама смесь окончательна — БЕЗ таблицы
Cherokee→Latin по буквам.
Обоснование: AD-25 отказался угадывать Cherokee-соответствия, и security-таблица не
должна утверждать невыверенные двойники. Но соответствия и не нужны: базовый закон
детектора — смесь письменностей внутри токена и есть признак (AD-2), и — в отличие от
CJK, где «IDカード» / «iPhone12» нормальные токены — ни один язык не переплетает
латиницу с Cherokee внутри токена, поэтому одна смесь уже аномальна. Это строго
скрипт-специфично: только «hard-mix» скрипты (Cherokee) обрабатываются так, поэтому
Latin-смешение японского/CJK и чистый односкриптовый Cherokee (ᏣᎳᎩ) остаются чистыми
(проверено 0 FP). Компромисс против таблиц Cyrillic/Greek/Armenian: не показывается
имитируемый скелет, только аномалия — честное отражение того, что выверено.
Статус: `ПРИНЯТО` (code/range/confusable_cards.py hard-mix branch;
code/tests/test_cherokee.py).

**AD-27 · Армянский повышен до карточного семейства; иммунитет к ERG-смягчению проверен и закреплён.**
Решение: (a) армянский получает пять first-class per-sign карточек (օ/ո/ս/ա/Օ),
отслеживаемых coverage_lock (ARM_TO_LAT + семейство ARMENIAN_, LOCKED 81), а чероки
остаётся без карточек по дизайну (method-заметка docs/CHEROKEE_HARD_MIX.md). (b)
Слой ERG-контекста — единственный компонент, способный ПОНИЗИТЬ вердикт — проверен
против каждого детектора, добавленного в этом цикле, и аудит превращён в постоянный
регрессионный тест.
Обоснование: после столь широкого расширения детекции реальный риск — не
пропущенная атака, а *заглушённая* — ERG ошибочно очищает новую окончательную
находку под benign-рамкой. Контракт ERG уже делает сигнатуры drafted-карточек
иммунными (смягчает только MSL-core action-сигнатуры и никогда не очищает
conclusive ALARM в OK), но «иммунно по контракту» — проверяется, а не
предполагается: 14 новых классов атак, обёрнутых в триггер смягчения («безопасно
ли…?», «объясни…», «например…»), остаются заблокированными (0 заглушено).
test_erg_immunity.py закрепляет это, чтобы будущая правка ERG не могла тихо начать
их очищать.
Статус: `ПРИНЯТО` (sign_cards ARMENIAN_*; coverage_lock ARM; docs/CHEROKEE_HARD_MIX.md;
code/tests/test_erg_immunity.py).
