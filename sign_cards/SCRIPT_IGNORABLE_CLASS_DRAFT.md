PRIVATE AUTHORIAL PROJECT / ЧАСТНЫЙ АВТОРСКИЙ ПРОЕКТ · COMMERCIAL USE PROHIBITED

# SIGN CORE CARD — SCRIPT-BOUND-IGNORABLE CLASS (class card, DRAFT)

DOCUMENT_ID: SIGN_CORE_CARD_SCRIPT_IGNORABLE_CLASS_GEN3_v0_1 · DOCUMENT_TYPE: SIGN_CORE_CARD · TEMPLATE_LINE: GEN3_v0_3
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
PRIORITY_TIER: P2 (contour completion) · RAW_PROTOTYPE: `code/range/script_ignorable_cards.py` · HARNESS: `code/range/range_contour_tail.py`
SCOPE: U+180B–U+180D, U+180F (Mongolian Free Variation Selectors) and U+17B4, U+17B5 (Khmer inherent vowels) — default-ignorable combining marks (category Mn) bound to one script. Part of the assigned non-Cf tail of the Default_Ignorable contour, alongside HANGUL_FILLER and RESERVED_IGNORABLE.

🇬🇧 [English](#english) · 🇷🇺 [Русский](#русский)

---

<a name="english"></a>
## English

DRAFT_NOTE (2026-07-20): the CLASS card for the script-bound default-ignorable marks — combining marks (category Mn) that mean something ONLY inside their own script. The Mongolian Free Variation Selectors (U+180B–U+180D, U+180F) pick a Mongolian glyph variant of the preceding Mongolian letter — the Mongolian analogue of the general variation-selector card, but bound to the Mongolian block. The Khmer inherent vowels (U+17B4 AQ, U+17B5 AA) are invisible inherent vowels used inside Khmer. Governing law: **SCRIPT_IGNORABLE ≠ UNIVERSAL** — legitimate on its own script, an orphan or a data carrier anywhere else, and (like all VS) invisible to a Cf-only filter because it is a mark. WORKING_DRAFT, NON-CONVEYOR.

**0. UNIVERSALITY.** BOUND_TO_SPECIFIC_SIGN: CLASS (script-bound default-ignorable marks, category Mn) · AFTER_USE_RESIDUE: FORBIDDEN · SIGN_DATA_IS_SESSION_ONLY: YES

**1. COMMON_CONVEYOR_DISCIPLINE.** v0_3 · RUN_CARD_REQUIRED_BEFORE_LOCK: YES · MODEL_FAMILY_DIVERSITY_REQUIRED: YES · ADVERSARIAL_EVIDENCE_REQUIRED: YES · MUTATION_CHECK_REQUIRED: YES · LIMITATION_STATEMENT_REQUIRED: YES. TRACKER: WORKING_DRAFT YES; PREFLIGHT PENDING; CONVEYOR_REVIEW PENDING; WORKINGLY_CLOSED NO.

**2. META.** ZONE: ZONE_1. WHY_THIS_SIGN_MATTERS: these marks share the variation-selector danger — one is meaningful per base, a chain is a carrier, and one on the wrong base is an orphan — but they live in different blocks than the FE00/E0100 selectors, so a VS card scoped to those ranges misses them entirely. The Mongolian FVS are Variation_Selector=Yes in the Mongolian block; the Khmer inherent vowels are default-ignorable Mn used in Khmer text (Unicode UAX #44; the Mongolian and Khmer blocks). INTERACTS_WITH: VARIATION_SELECTOR_CLASS (same Mn-carrier logic, different block — this card extends it to the script-bound selectors), CANONICALIZATION_PRE_PASS (decode entity/percent first), NOTARIUS (a mark run shifts the codepoint count).

**3. REQUIRED_GENERAL_GUARDS.** RAW_SIGN_INPUT_STATUS: DATA_ONLY · NO_EXECUTION_FROM_SIGN: YES · NO_TRUST_FROM_SIGN: YES · DECODE_BEFORE_TRUST: YES · JUDGE_IN_CONTEXT_NOT_ON_PRESENCE: YES · NEVER_BLIND_STRIP: YES (an in-script mark carries real shaping) · SEPARATE_BRANCH_FROM_Cf: YES (Mn, not Format).

**4. SIGN IDENTITY — LAYER_A (LOCK: PERMANENT).** BASE_MODE: DATA_ONLY_SCRIPT_MARK · BASE_MODE_FORMULA: MARK_FORM ≠ EFFECT ; IN_SCRIPT = LEGIT ; RUN_OR_OFF_SCRIPT = CARRIER.

| Codepoint(s) | Name | Cat | Priority | Attack mechanism | Legitimate use (do NOT blind-strip) |
|---|---|---|---|---|---|
| U+180B–U+180D | MONGOLIAN FREE VARIATION SELECTOR ONE..THREE | Mn | WITNESS/MED | chained as a data carrier; orphan off Mongolian | Mongolian glyph-variant selection |
| U+180F | MONGOLIAN FREE VARIATION SELECTOR FOUR | Mn | WITNESS/MED | same | Mongolian glyph-variant selection |
| U+17B4 | KHMER VOWEL INHERENT AQ | Mn | WITNESS/MED | invisible insertion off Khmer | Khmer inherent vowel |
| U+17B5 | KHMER VOWEL INHERENT AA | Mn | WITNESS/MED | invisible insertion off Khmer | Khmer inherent vowel |

WHAT_THIS_SIGN_IS_NOT: (1) NOT_A_FORMAT_CHAR — a combining MARK (Mn); a Cf filter never touches it; (2) NOT_UNIVERSAL — meaningful only on its own script; (3) NOT_STRIPPABLE — deleting an in-script mark corrupts Mongolian/Khmer shaping; (4) NOT_FINAL_SURFACE — may arrive entity/percent-encoded and must be decoded first.
BASE_FORMULAS: IN_SCRIPT_ON_BASE = OK ; RUN(≥2) = CARRIER ; OFF_SCRIPT = ORPHAN.

**5. SEMANTIC_EPOCH_TRACKER (LOCK: REVIEWABLE).** EPOCH_TRACKER: U+180F (FVS4) was added in a later Unicode version than FVS1–3, so a version-blind tool may not know it; the Khmer inherent vowels are stable. NOTE: LATER_ADDITION ≠ ABSENT_RISK (a tool that doesn't know FVS4 will silently pass it).

**6. EFFECT_FIELDS — LAYER_C (LOCK: SESSION).** authority / trust / verification / proof / execution / permission / status / role_assignment / runtime / existence effect: all NONE. EFFECT_FIELDS_ALL_NONE: YES · CLOSED_SCHEMA: YES.

**7. SAFE / RISK / GUARDS — LAYER_B (LOCK: REVIEWABLE).**
Keys on IN-SCRIPT vs. OFF-SCRIPT and ONE vs. MANY:
- ALARM (conclusive): a run of ≥2 of these marks (data carrier); a mark with no valid in-script base (a Mongolian FVS not after a Mongolian letter, a Khmer inherent vowel off Khmer) — orphan carrier.
- OK (clean, "in-script" vouch): every Mongolian FVS sits on a Mongolian base; every Khmer inherent vowel sits inside Khmer.
- (No standing WATCH tier in the prototype: off-script is treated as an orphan ALARM, since these marks have no cross-script role.)
SAFE_CASES (must stay OK): Mongolian text using an FVS after a Mongolian letter; Khmer text using an inherent vowel.
RISK_CASES: `data‹FVS1›x` (FVS off Mongolian) ALARM; `‹Mongolian letter›‹FVS1›‹FVS2›` (run) ALARM; a Khmer inherent vowel in Latin prose ALARM.
GUARD_PRINCIPLE: one mark per valid in-script base; a run or an off-script mark is a carrier; never strip an in-script mark; keep this on the Mn branch, distinct from Cf.

**8. ADVERSARIAL_COVERAGE — RUN_CARD SEED.** FVS runs after Mongolian and off Mongolian; Khmer inherent vowel off Khmer; FVS4 specifically (later addition); legit Mongolian and Khmer runs (must stay OK); every case ALSO delivered entity/percent-encoded (pre-pass path). MODEL_FAMILY_DIVERSITY_REQUIRED: YES.

**9. MUTATION_CHECK.** literal mark ↔ `&#N;` ↔ `%XX` byte form; in-script vs. off-script; single vs. run. INVARIANT: after canonicalization one verdict; an in-script case stays OK, a run/orphan stays ALARM across all forms.

**10. KNOWN_OPEN_QUESTIONS.** Q1: a proper Mongolian shaping model (an FVS is legit only after a letter that actually HAS the selected variant). Q2: whether a single off-script mark should be WATCH rather than ALARM in text that is otherwise plausibly multilingual. Q3: fold this and the general VS card into one selector engine keyed by block, so the Mn-carrier logic lives in one place.

**11. PATCH_HISTORY.** v0_1 (2026-07-20): first draft of the script-bound-ignorable CLASS card (Mongolian FVS + Khmer inherent vowels), paired with `script_ignorable_cards.py`. Not conveyor-run.

**12. LIMITATION_STATEMENT.** (1) WORKING_DRAFT / NOT_CONVEYOR_RUN. (2) In-script validity is checked by BLOCK adjacency, not real shaping (Q1). (3) Off-script is always ALARM — no WATCH middle tier for plausibly-multilingual text (Q2). (4) Entity/percent-delivered marks are caught only WITH the pre-pass in front. (5) The general VS card and this one are separate prototypes, not yet one engine (Q3).

**13. INTEGRATION_INTERFACE_STATUS.** INTEGRATION_STATUS: PROTOTYPED (raw). RAW_PROTOTYPE: `script_ignorable_cards.py::script_ignorable_cards_reader(text) -> Finding`. HARNESS: `range_contour_tail.py`. LIVE RESULT (real MSL + all 6 invisible axes as baseline, shared with the other two tail cards): **tail threats 0/6 → 6/6, legit in-script 4/4 kept, 0 new FP** — FVS orphan and FVS carrier move to ALARM while legit Mongolian FVS and Khmer inherent vowels stay OK. REQUIRES for closing: Mongolian shaping model (Q1); multilingual WATCH tier (Q2); pre-pass in front; conveyor review.

> HOW THE RAW PROTOTYPE WORKS: `MSL_MIP_HOME=/path/to/msl_mip python code/range/range_contour_tail.py` runs this card with the other two tail cards, scanning off-script/carrier cases and legit in-script runs BEFORE (MSL + all invisible axes) and AFTER (+ the tail), printing the before/after verdict per case plus totals.

---

<a name="русский"></a>
## Русский

DRAFT_NOTE (2026-07-20): КЛАССОВАЯ карточка привязанных-к-письменности default-ignorable марок — комбинирующих марок (категория Mn), осмысленных ТОЛЬКО внутри своей письменности. Монгольские свободные селекторы вариаций (U+180B–U+180D, U+180F) выбирают монгольский вариант глифа предыдущей монгольской буквы — монгольский аналог общей карточки селекторов вариаций, но привязанный к монгольскому блоку. Кхмерские присущие гласные (U+17B4 AQ, U+17B5 AA) — невидимые присущие гласные внутри кхмерского. Управляющий закон: **SCRIPT_IGNORABLE ≠ УНИВЕРСАЛЬНЫЙ** — легитимен на своей письменности, сирота или носитель данных где угодно ещё, и (как все VS) невидим для Cf-only фильтра, ведь это марка. WORKING_DRAFT, БЕЗКОНВЕЙЕРНО.

**0. UNIVERSALITY.** BOUND_TO_SPECIFIC_SIGN: CLASS (привязанные-к-письменности default-ignorable марки, категория Mn) · AFTER_USE_RESIDUE: FORBIDDEN · SIGN_DATA_IS_SESSION_ONLY: YES

**1. COMMON_CONVEYOR_DISCIPLINE.** v0_3 · RUN_CARD_REQUIRED_BEFORE_LOCK: YES · MODEL_FAMILY_DIVERSITY_REQUIRED: YES · ADVERSARIAL_EVIDENCE_REQUIRED: YES · MUTATION_CHECK_REQUIRED: YES · LIMITATION_STATEMENT_REQUIRED: YES. TRACKER: WORKING_DRAFT YES; PREFLIGHT PENDING; CONVEYOR_REVIEW PENDING; WORKINGLY_CLOSED NO.

**2. META.** ZONE: ZONE_1. WHY_THIS_SIGN_MATTERS: эти марки разделяют опасность селектора вариаций — одна осмыслена на базу, цепочка это носитель, одна на неправильной базе это сирота — но живут в других блоках, чем селекторы FE00/E0100, поэтому VS-карточка, скоупленная на те диапазоны, их полностью пропускает. Монгольские FVS это Variation_Selector=Yes в монгольском блоке; кхмерские присущие гласные это default-ignorable Mn в кхмерском тексте (Unicode UAX #44; монгольский и кхмерский блоки). INTERACTS_WITH: VARIATION_SELECTOR_CLASS (та же логика Mn-носителя, другой блок — эта карточка расширяет её на привязанные-к-письменности селекторы), CANONICALIZATION_PRE_PASS (сперва декод entity/percent), NOTARIUS (цепочка марок сдвигает счётчик кодпоинтов).

**3. REQUIRED_GENERAL_GUARDS.** RAW_SIGN_INPUT_STATUS: DATA_ONLY · NO_EXECUTION_FROM_SIGN: YES · NO_TRUST_FROM_SIGN: YES · DECODE_BEFORE_TRUST: YES · JUDGE_IN_CONTEXT_NOT_ON_PRESENCE: YES · NEVER_BLIND_STRIP: YES (в-скрипте марка несёт настоящее формообразование) · SEPARATE_BRANCH_FROM_Cf: YES (Mn, не Format).

**4. SIGN IDENTITY — LAYER_A (LOCK: PERMANENT).** BASE_MODE: DATA_ONLY_SCRIPT_MARK · BASE_MODE_FORMULA: MARK_FORM ≠ EFFECT ; IN_SCRIPT = LEGIT ; RUN_OR_OFF_SCRIPT = CARRIER.

| Кодпоинт(ы) | Имя | Кат | Приоритет | Механизм атаки | Легит-применение (НЕ вырезать слепо) |
|---|---|---|---|---|---|
| U+180B–U+180D | MONGOLIAN FREE VARIATION SELECTOR ONE..THREE | Mn | WITNESS/СРЕД | сцеплены как носитель данных; сирота вне монгольского | выбор монгольского варианта глифа |
| U+180F | MONGOLIAN FREE VARIATION SELECTOR FOUR | Mn | WITNESS/СРЕД | то же | выбор монгольского варианта глифа |
| U+17B4 | KHMER VOWEL INHERENT AQ | Mn | WITNESS/СРЕД | невидимая вставка вне кхмерского | кхмерская присущая гласная |
| U+17B5 | KHMER VOWEL INHERENT AA | Mn | WITNESS/СРЕД | невидимая вставка вне кхмерского | кхмерская присущая гласная |

WHAT_THIS_SIGN_IS_NOT: (1) NOT_A_FORMAT_CHAR — комбинирующая МАРКА (Mn); Cf-фильтр её не трогает; (2) NOT_UNIVERSAL — осмыслена лишь на своей письменности; (3) NOT_STRIPPABLE — удаление в-скрипте марки портит монгольское/кхмерское формообразование; (4) NOT_FINAL_SURFACE — может прийти entity/percent-кодированной, сперва декод.
BASE_FORMULAS: IN_SCRIPT_ON_BASE = OK ; RUN(≥2) = CARRIER ; OFF_SCRIPT = ORPHAN.

**5. SEMANTIC_EPOCH_TRACKER (LOCK: REVIEWABLE).** EPOCH_TRACKER: U+180F (FVS4) добавлен в более поздней версии Unicode, чем FVS1–3, поэтому версия-слепой инструмент может его не знать; кхмерские присущие гласные стабильны. NOTE: ПОЗДНЕЕ_ДОБАВЛЕНИЕ ≠ ОТСУТСТВИЕ_РИСКА (инструмент, не знающий FVS4, молча его пропустит).

**6. EFFECT_FIELDS — LAYER_C (LOCK: SESSION).** authority / trust / verification / proof / execution / permission / status / role_assignment / runtime / existence effect: всё NONE. EFFECT_FIELDS_ALL_NONE: YES · CLOSED_SCHEMA: YES.

**7. SAFE / RISK / GUARDS — LAYER_B (LOCK: REVIEWABLE).**
Ключ на IN-SCRIPT vs. OFF-SCRIPT и ОДИН vs. МНОГО:
- ALARM (conclusive): цепочка ≥2 этих марок (носитель данных); марка без валидной in-script базы (монгольский FVS не после монгольской буквы, кхмерская присущая гласная вне кхмерского) — сиротский носитель.
- OK (чистое, вауч «in-script»): каждый монгольский FVS на монгольской базе; каждая кхмерская присущая гласная внутри кхмерского.
- (В прототипе нет постоянного яруса WATCH: off-script трактуется как сиротский ALARM, ведь у этих марок нет межскриптовой роли.)
SAFE_CASES (должны остаться OK): монгольский текст с FVS после монгольской буквы; кхмерский текст с присущей гласной.
RISK_CASES: `data‹FVS1›x` (FVS вне монгольского) ALARM; `‹монгольская буква›‹FVS1›‹FVS2›` (цепочка) ALARM; кхмерская присущая гласная в латинской прозе ALARM.
GUARD_PRINCIPLE: одна марка на валидную in-script базу; цепочка или off-script марка это носитель; никогда не вырезать in-script марку; держать это на ветке Mn, отдельно от Cf.

**8. ADVERSARIAL_COVERAGE — RUN_CARD SEED.** цепочки FVS после монгольского и вне монгольского; кхмерская присущая гласная вне кхмерского; конкретно FVS4 (позднее добавление); легит монгольские и кхмерские прогоны (должны остаться OK); каждый кейс ТАКЖЕ доставлен entity/percent-кодированным (путь pre-pass). MODEL_FAMILY_DIVERSITY_REQUIRED: YES.

**9. MUTATION_CHECK.** литеральная марка ↔ `&#N;` ↔ байтовая форма `%XX`; in-script vs. off-script; одиночная vs. цепочка. INVARIANT: после канонизации один вердикт; in-script кейс остаётся OK, цепочка/сирота остаётся ALARM во всех формах.

**10. KNOWN_OPEN_QUESTIONS.** Q1: полноценная модель монгольского формообразования (FVS легитимен лишь после буквы, у которой реально ЕСТЬ выбранный вариант). Q2: должна ли одиночная off-script марка быть WATCH, а не ALARM в тексте, иначе правдоподобно многоязычном. Q3: свести эту и общую VS-карточку в один селектор-движок с ключом по блоку, чтобы логика Mn-носителя жила в одном месте.

**11. PATCH_HISTORY.** v0_1 (2026-07-20): первый черновик КЛАССОВОЙ карточки привязанных-к-письменности ignorable (монгольские FVS + кхмерские присущие гласные), в паре с `script_ignorable_cards.py`. Не прогонялся через конвейер.

**12. LIMITATION_STATEMENT.** (1) WORKING_DRAFT / NOT_CONVEYOR_RUN. (2) In-script валидность проверяется соседством по БЛОКУ, не настоящим формообразованием (Q1). (3) Off-script всегда ALARM — нет среднего яруса WATCH для правдоподобно-многоязычного текста (Q2). (4) Entity/percent-доставленные марки ловятся только С pre-pass впереди. (5) Общая VS-карточка и эта — отдельные прототипы, ещё не один движок (Q3).

**13. INTEGRATION_INTERFACE_STATUS.** INTEGRATION_STATUS: PROTOTYPED (сырой). RAW_PROTOTYPE: `script_ignorable_cards.py::script_ignorable_cards_reader(text) -> Finding`. HARNESS: `range_contour_tail.py`. ЖИВОЙ РЕЗУЛЬТАТ (настоящий MSL + все 6 невидимых осей как база, общая с двумя другими хвостовыми карточками): **хвостовые угрозы 0/6 → 6/6, легит в-скрипте 4/4, 0 новых FP** — FVS-сирота и FVS-носитель переходят в ALARM, а легит монгольские FVS и кхмерские присущие гласные остаются OK. ТРЕБУЕТСЯ для закрытия: модель монгольского формообразования (Q1); многоязычный ярус WATCH (Q2); pre-pass впереди; конвейер-ревью.

> КАК РАБОТАЕТ СЫРОЙ ПРОТОТИП: `MSL_MIP_HOME=/path/to/msl_mip python code/range/range_contour_tail.py` прогоняет эту карточку с двумя другими хвостовыми, сканируя off-script/носитель кейсы и легит in-script прогоны BEFORE (MSL + все невидимые оси) и AFTER (+ хвост), печатая вердикт до/после по кейсу и итоги.
