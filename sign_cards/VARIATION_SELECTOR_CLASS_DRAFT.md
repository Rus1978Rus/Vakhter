PRIVATE AUTHORIAL PROJECT / ЧАСТНЫЙ АВТОРСКИЙ ПРОЕКТ · COMMERCIAL USE PROHIBITED

# SIGN CORE CARD — VARIATION-SELECTOR / Mn-CARRIER CLASS (class card, DRAFT)

DOCUMENT_ID: SIGN_CORE_CARD_VARIATION_SELECTOR_CLASS_GEN3_v0_1 · DOCUMENT_TYPE: SIGN_CORE_CARD · TEMPLATE_LINE: GEN3_v0_3
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
PRIORITY_TIER: P1 (core) · RAW_PROTOTYPE: `code/range/vs_cards.py` · HARNESS: `code/range/range_vs.py`
SCOPE: variation selectors U+FE00–U+FE0F (VS1–VS16) and the supplement U+E0100–U+E01EF (VS17–VS256). Zero-width signs, bidi controls and TAG characters are SEPARATE axes (see INVISIBLE_CLASS, BIDI_CLASS, TAG_CLASS).

🇬🇧 [English](#english) · 🇷🇺 [Русский](#русский)

---

<a name="english"></a>
## English

DRAFT_NOTE (2026-07-20): the CLASS card for variation selectors — a fourth invisible axis that is separate for a **category reason that matters operationally**: variation selectors are Unicode general category **Mn (Nonspacing_Mark), NOT Cf (Format)**. The reflex cleanup "strip all format (Cf) characters" — which handles most invisibles — MISSES every variation selector, because they are combining marks. A defender who only knows the Cf invisibles has a blind spot exactly the size of this class. Legit role: ONE selector on an appropriate base (VS16 emoji presentation, VS15 text presentation, VS1–14 / supplement for CJK variants). Attack role: a RUN of selectors on one base is a data CARRIER (each carries several bits → arbitrary bytes smuggled) and a selector with NO valid base is an orphan carrier. The governing law: **VS_PRESENT ≠ Cf ≠ IN "CLASS 138"** — this is its own branch; and **ONE selector on a base = OK, a run or an orphan = carrier.** WORKING_DRAFT, NON-CONVEYOR.

**0. UNIVERSALITY.** BOUND_TO_SPECIFIC_SIGN: CLASS (variation selectors, category Mn) · AFTER_USE_RESIDUE: FORBIDDEN · SIGN_DATA_IS_SESSION_ONLY: YES

**1. COMMON_CONVEYOR_DISCIPLINE.** v0_3 · RUN_CARD_REQUIRED_BEFORE_LOCK: YES · MODEL_FAMILY_DIVERSITY_REQUIRED: YES · ADVERSARIAL_EVIDENCE_REQUIRED: YES · MUTATION_CHECK_REQUIRED: YES · LIMITATION_STATEMENT_REQUIRED: YES. TRACKER: WORKING_DRAFT YES; PREFLIGHT PENDING; CONVEYOR_REVIEW PENDING; WORKINGLY_CLOSED NO.

**2. META.** ZONE: ZONE_1. WHY_THIS_SIGN_MATTERS: variation selectors were designed to pick a glyph variant of the PRECEDING base (emoji vs. text presentation; CJK ideograph variants — Unicode UAX #44 category Mn, Unicode Variation Sequences / Ideographic Variation Database). Because exactly one selector is meaningful per base, a chain of them carries no legitimate typographic meaning — it carries data. In 2025 this became a public smuggling/watermark technique (arbitrary bytes hidden after an emoji). The **Mn-not-Cf** fact is the reason this MUST be a separate guard branch, not folded into the format-character (Cf) invisibles of the general 138-sign contour. INTERACTS_WITH: INVISIBLE_CLASS (adjacent invisible axis — but Cf vs. Mn: the invisible card is scoped to zero-width Cf and delegates VS here), CANONICALIZATION_PRE_PASS (a selector can arrive as `&#65039;` for VS16 and must be decoded first), NOTARIUS (a selector run shifts the codepoint count).

**3. REQUIRED_GENERAL_GUARDS.** RAW_SIGN_INPUT_STATUS: DATA_ONLY · NO_EXECUTION_FROM_SIGN: YES · NO_TRUST_FROM_SIGN: YES · DECODE_BEFORE_TRUST: YES · JUDGE_IN_CONTEXT_NOT_ON_PRESENCE: YES · NEVER_BLIND_STRIP: YES (a lone VS16 IS the emoji/text presentation and must be preserved) · SEPARATE_BRANCH_FROM_Cf: YES (Mn, not Format).

**4. SIGN IDENTITY — LAYER_A (LOCK: PERMANENT).** BASE_MODE: DATA_ONLY_COMBINING_MARK · BASE_MODE_FORMULA: VS_FORM ≠ EFFECT ; ONE_ON_BASE = LEGIT ; RUN_OR_ORPHAN = CARRIER.

| Codepoint(s) | Name | Category | Priority | Attack mechanism | Legitimate use (do NOT blind-strip) |
|---|---|---|---|---|---|
| U+FE0F | VARIATION SELECTOR-16 (VS16) | Mn | HIGH | as a run head / on a non-base — carrier | emoji presentation of the preceding base (❤ → ❤️) |
| U+FE0E | VARIATION SELECTOR-15 (VS15) | Mn | HIGH | as a run head / on a non-base — carrier | text presentation of the preceding base |
| U+FE00–U+FE0D | VARIATION SELECTOR-1..14 | Mn | MED | chained as a data carrier | CJK / symbol glyph variants (one per base) |
| U+E0100–U+E01EF | VARIATION SELECTOR-17..256 (supplement) | Mn | MED | chained as a data carrier | CJK Ideographic Variation Sequences (IVD) |

WHAT_THIS_SIGN_IS_NOT: (1) NOT_A_FORMAT_CHAR — it is a combining MARK (Mn); a Cf filter never touches it; (2) NOT_SMUGGLE_BY_PRESENCE — one selector on a base is legitimate presentation; (3) NOT_STRIPPABLE — deleting VS16 changes ❤️ back to ❤ (text) and can corrupt CJK variants; (4) NOT_FINAL_SURFACE — may arrive as `&#65039;` / `%EF%B8%8F` and must be decoded first.
BASE_FORMULAS: VS_FORM ≠ EFFECT ; ONE_SELECTOR_ON_VALID_BASE = LEGIT ; RUN(≥2) = CARRIER ; ORPHAN(no base / on non-base) = CARRIER.

**5. SEMANTIC_EPOCH_TRACKER (LOCK: REVIEWABLE).** EPOCH_TRACKER: VS16 gained enormous reach when emoji presentation was standardized (a once-obscure typographic control became ubiquitous), which is exactly what makes a VS run a good hiding place today. NOTE: UBIQUITOUS_LEGIT_USE ≠ SAFE_IN_RUNS (the legitimacy of the single case is the camouflage for the run case).

**6. EFFECT_FIELDS — LAYER_C (LOCK: SESSION).** authority / trust / verification / proof / execution / permission / status / role_assignment / runtime / existence effect: all NONE. EFFECT_FIELDS_ALL_NONE: YES · CLOSED_SCHEMA: YES.

**7. SAFE / RISK / GUARDS — LAYER_B (LOCK: REVIEWABLE).**
The decision keys on ONE-vs-MANY and BASE-vs-NO-BASE: **OK** for a single selector on a valid base, **ALARM** for a run or an orphan.
- ALARM (conclusive): a run of ≥2 consecutive selectors (one base cannot meaningfully take two) — data carrier; a leading selector (no base); a selector after a non-base char (space, plain ASCII letter) — nothing to select.
- OK (clean, "single-on-base" vouch): one VS16/VS15 on an emoji-capable base (`❤️`, `✂︎`); one VS1–14 / supplement selector on a CJK ideograph.
SAFE_CASES (must stay OK): "I love it ❤️ a lot" (single VS16 on ❤); "cut here ✂︎ please" (single VS15); a CJK ideograph + one supplement selector; plain text/emoji with no selectors.
RISK_CASES: `❤️︎` head of a 2-selector run ALARM (`vs_carrier`); a 5-selector run after "data" ALARM; a leading VS16 ALARM (`vs_orphan`); `pass‹VS16›word` (selector on a plain letter) ALARM; `hello ‹VS15›world` (selector on a space) ALARM.
GUARD_PRINCIPLE: allow exactly one selector per valid base; a second consecutive selector, a leading selector, or a selector on a non-base is a carrier → ALARM; never strip the legitimate single selector; keep this branch DISTINCT from the Cf invisible branch (Mn ≠ Cf).

**8. ADVERSARIAL_COVERAGE — RUN_CARD SEED.** 2-, 5-, and long selector runs after emoji and after CJK; leading selector; selector on space / ASCII letter / punctuation; a legit single VS16 immediately adjacent to a carrier run (must ALARM); every case ALSO delivered via numeric-entity and percent (pre-pass path). MODEL_FAMILY_DIVERSITY_REQUIRED: YES.

**9. MUTATION_CHECK.** literal selector ↔ `&#N;` ↔ `%XX` byte form; BMP selector vs. supplement selector carrying the same run; run split into two adjacent bases. INVARIANT: after canonicalization one verdict; a single-on-base case stays OK, a run/orphan stays ALARM across all forms.

**10. KNOWN_OPEN_QUESTIONS.** Q1: a proper base-validity model — the draft approximates "emoji base" (symbol category / emoji planes) and "CJK base" (ideograph ranges); a real emoji-VS / IVD table would remove the residual approximation. Q2: whether a *single* selector on a wrong-but-plausible base should be WATCH rather than ALARM (currently ALARM). Q3: decode the carrier run's bits and surface the smuggled bytes, the way the TAG card surfaces its ASCII.

**11. PATCH_HISTORY.** v0_1 (2026-07-20): first draft of the variation-selector CLASS card as a separate Mn branch (distinct from the Cf invisibles), paired with `vs_cards.py`. Not conveyor-run.

**12. LIMITATION_STATEMENT.** (1) WORKING_DRAFT / NOT_CONVEYOR_RUN. (2) Base validity is APPROXIMATED (emoji-planes/symbol category, CJK ranges), not the exact emoji-VS / Ideographic-Variation-Database tables (Q1). (3) The harness models the taxonomy split by making the invisible-card baseline VS-blind (VS delegated here); in the current shared prototype the invisible card still references VS until refactored. (4) The carrier's hidden bytes are detected but not decoded (Q3). (5) Entity/percent-delivered selectors are caught only WITH the pre-pass in front.

**13. INTEGRATION_INTERFACE_STATUS.** INTEGRATION_STATUS: PROTOTYPED (raw). RAW_PROTOTYPE: `vs_cards.py::vs_cards_reader(text) -> Finding`. HARNESS: `range_vs.py` (baseline VS-blind per the taxonomy split). LIVE RESULT (real MSL + invisible[zero-width only] + bidi + tag as baseline): **VS carrier/orphan 0/5 (0%) → 5/5 (100%), legit selectors 5/5 → 5/5, 0 new FP** — every carrier run and orphan selector moves to ALARM while single-selector-on-base (emoji VS16/VS15 and CJK supplement) stays OK. This is the axis a Cf-only filter cannot see. REQUIRES for closing: emoji-VS / IVD base tables (Q1); carrier-byte decode (Q3); pre-pass in front; conveyor review.

> HOW THE RAW PROTOTYPE WORKS: `MSL_MIP_HOME=/path/to/msl_mip python code/range/range_vs.py` scans carrier/orphan threats and legit single selectors BEFORE (MSL + zero-width invisible + bidi + tag) and AFTER (+ this Mn axis) and prints the before/after verdict per case plus totals, with the Mn-not-Cf reminder.

---

<a name="русский"></a>
## Русский

DRAFT_NOTE (2026-07-20): КЛАССОВАЯ карточка селекторов вариаций — четвёртая невидимая ось, отдельная по **категорийной причине, важной операционно**: селекторы вариаций это общая категория Unicode **Mn (Nonspacing_Mark), НЕ Cf (Format)**. Рефлекс-очистка «вырезать все форматные (Cf) символы» — которая закрывает большинство невидимок — ПРОПУСКАЕТ каждый селектор вариации, потому что это комбинирующие марки. У защитника, знающего лишь Cf-невидимки, слепое пятно ровно размером с этот класс. Легит-роль: ОДИН селектор на подходящей базе (VS16 emoji-презентация, VS15 текстовая презентация, VS1–14 / supplement для вариантов CJK). Атака-роль: ЦЕПОЧКА селекторов на одной базе это НОСИТЕЛЬ данных (каждый несёт несколько бит → произвольные байты контрабандой), а селектор БЕЗ валидной базы — сиротский носитель. Управляющий закон: **VS_ПРИСУТСТВУЕТ ≠ Cf ≠ В «КЛАССЕ 138»** — это своя ветка; и **один селектор на базе = OK, цепочка или сирота = носитель.** WORKING_DRAFT, БЕЗКОНВЕЙЕРНО.

**0. UNIVERSALITY.** BOUND_TO_SPECIFIC_SIGN: CLASS (селекторы вариаций, категория Mn) · AFTER_USE_RESIDUE: FORBIDDEN · SIGN_DATA_IS_SESSION_ONLY: YES

**1. COMMON_CONVEYOR_DISCIPLINE.** v0_3 · RUN_CARD_REQUIRED_BEFORE_LOCK: YES · MODEL_FAMILY_DIVERSITY_REQUIRED: YES · ADVERSARIAL_EVIDENCE_REQUIRED: YES · MUTATION_CHECK_REQUIRED: YES · LIMITATION_STATEMENT_REQUIRED: YES. TRACKER: WORKING_DRAFT YES; PREFLIGHT PENDING; CONVEYOR_REVIEW PENDING; WORKINGLY_CLOSED NO.

**2. META.** ZONE: ZONE_1. WHY_THIS_SIGN_MATTERS: селекторы вариаций созданы, чтобы выбирать вариант глифа ПРЕДЫДУЩЕЙ базы (emoji vs. текстовая презентация; варианты идеографов CJK — Unicode UAX #44 категория Mn, Unicode Variation Sequences / Ideographic Variation Database). Поскольку осмыслен ровно один селектор на базу, их цепочка не несёт легит-типографического смысла — она несёт данные. В 2025 это стало публичной техникой контрабанды/водяных знаков (произвольные байты, спрятанные после emoji). Факт **Mn-не-Cf** и есть причина, почему это ДОЛЖНО быть отдельной веткой охраны, а не сложено в форматные (Cf) невидимки общего контура 138 знаков. INTERACTS_WITH: INVISIBLE_CLASS (смежная невидимая ось — но Cf vs. Mn: карточка невидимок скоупится на zero-width Cf и делегирует VS сюда), CANONICALIZATION_PRE_PASS (селектор может прийти как `&#65039;` для VS16, сперва декод), NOTARIUS (цепочка селекторов сдвигает счётчик кодпоинтов).

**3. REQUIRED_GENERAL_GUARDS.** RAW_SIGN_INPUT_STATUS: DATA_ONLY · NO_EXECUTION_FROM_SIGN: YES · NO_TRUST_FROM_SIGN: YES · DECODE_BEFORE_TRUST: YES · JUDGE_IN_CONTEXT_NOT_ON_PRESENCE: YES · NEVER_BLIND_STRIP: YES (одиночный VS16 ЕСТЬ emoji/текстовая презентация, его надо сохранить) · SEPARATE_BRANCH_FROM_Cf: YES (Mn, не Format).

**4. SIGN IDENTITY — LAYER_A (LOCK: PERMANENT).** BASE_MODE: DATA_ONLY_COMBINING_MARK · BASE_MODE_FORMULA: VS_FORM ≠ EFFECT ; ONE_ON_BASE = LEGIT ; RUN_OR_ORPHAN = CARRIER.

| Кодпоинт(ы) | Имя | Категория | Приоритет | Механизм атаки | Легит-применение (НЕ вырезать слепо) |
|---|---|---|---|---|---|
| U+FE0F | VARIATION SELECTOR-16 (VS16) | Mn | ВЫСОКИЙ | как голова цепочки / на не-базе — носитель | emoji-презентация предыдущей базы (❤ → ❤️) |
| U+FE0E | VARIATION SELECTOR-15 (VS15) | Mn | ВЫСОКИЙ | как голова цепочки / на не-базе — носитель | текстовая презентация предыдущей базы |
| U+FE00–U+FE0D | VARIATION SELECTOR-1..14 | Mn | СРЕД. | сцеплены как носитель данных | варианты глифов CJK / символов (один на базу) |
| U+E0100–U+E01EF | VARIATION SELECTOR-17..256 (supplement) | Mn | СРЕД. | сцеплены как носитель данных | последовательности идеографических вариаций CJK (IVD) |

WHAT_THIS_SIGN_IS_NOT: (1) NOT_A_FORMAT_CHAR — это комбинирующая МАРКА (Mn); Cf-фильтр её не трогает; (2) NOT_SMUGGLE_BY_PRESENCE — один селектор на базе это легит-презентация; (3) NOT_STRIPPABLE — удаление VS16 возвращает ❤️ к ❤ (текст) и может испортить варианты CJK; (4) NOT_FINAL_SURFACE — может прийти как `&#65039;` / `%EF%B8%8F`, сперва декод.
BASE_FORMULAS: VS_FORM ≠ EFFECT ; ONE_SELECTOR_ON_VALID_BASE = LEGIT ; RUN(≥2) = CARRIER ; ORPHAN(нет базы / на не-базе) = CARRIER.

**5. SEMANTIC_EPOCH_TRACKER (LOCK: REVIEWABLE).** EPOCH_TRACKER: VS16 получил огромный охват, когда стандартизировали emoji-презентацию (некогда малозаметный типографический контроль стал вездесущим) — именно это делает цепочку VS хорошим тайником сегодня. NOTE: ВЕЗДЕСУЩЕЕ_ЛЕГИТ_ПРИМЕНЕНИЕ ≠ БЕЗОПАСНО_В_ЦЕПОЧКАХ (легитимность одиночного случая — камуфляж для случая цепочки).

**6. EFFECT_FIELDS — LAYER_C (LOCK: SESSION).** authority / trust / verification / proof / execution / permission / status / role_assignment / runtime / existence effect: всё NONE. EFFECT_FIELDS_ALL_NONE: YES · CLOSED_SCHEMA: YES.

**7. SAFE / RISK / GUARDS — LAYER_B (LOCK: REVIEWABLE).**
Решение опирается на ОДИН-vs-МНОГО и БАЗА-vs-НЕТ-БАЗЫ: **OK** для одиночного селектора на валидной базе, **ALARM** для цепочки или сироты.
- ALARM (conclusive): цепочка ≥2 подряд селекторов (одна база не может осмысленно принять два) — носитель данных; ведущий селектор (нет базы); селектор после не-базового символа (пробел, обычная ASCII-буква) — нечего выбирать.
- OK (чистое, вауч «одиночный-на-базе»): один VS16/VS15 на emoji-способной базе (`❤️`, `✂︎`); один селектор VS1–14 / supplement на идеографе CJK.
SAFE_CASES (должны остаться OK): "I love it ❤️ a lot" (одиночный VS16 на ❤); "cut here ✂︎ please" (одиночный VS15); идеограф CJK + один supplement-селектор; обычный текст/emoji без селекторов.
RISK_CASES: `❤️︎` голова цепочки из 2 селекторов ALARM (`vs_carrier`); цепочка из 5 селекторов после "data" ALARM; ведущий VS16 ALARM (`vs_orphan`); `pass‹VS16›word` (селектор на обычной букве) ALARM; `hello ‹VS15›world` (селектор на пробеле) ALARM.
GUARD_PRINCIPLE: разрешать ровно один селектор на валидную базу; второй подряд, ведущий, или на не-базе — носитель → ALARM; никогда не вырезать легит-одиночный селектор; держать эту ветку ОТДЕЛЬНОЙ от Cf-ветки невидимок (Mn ≠ Cf).

**8. ADVERSARIAL_COVERAGE — RUN_CARD SEED.** цепочки из 2, 5 и много селекторов после emoji и после CJK; ведущий селектор; селектор на пробеле / ASCII-букве / пунктуации; легит-одиночный VS16 вплотную к цепочке-носителю (должно быть ALARM); каждый кейс ТАКЖЕ доставлен numeric-entity и percent (путь pre-pass). MODEL_FAMILY_DIVERSITY_REQUIRED: YES.

**9. MUTATION_CHECK.** литеральный селектор ↔ `&#N;` ↔ байтовая форма `%XX`; BMP-селектор vs. supplement-селектор с одной цепочкой; цепочка, разбитая на две смежные базы. INVARIANT: после канонизации один вердикт; кейс одиночный-на-базе остаётся OK, цепочка/сирота остаётся ALARM во всех формах.

**10. KNOWN_OPEN_QUESTIONS.** Q1: полноценная модель валидности базы — черновик приближает «emoji-база» (категория символов / emoji-плоскости) и «CJK-база» (диапазоны идеографов); настоящая таблица emoji-VS / IVD убрала бы остаточное приближение. Q2: должен ли *одиночный* селектор на неправильной-но-правдоподобной базе быть WATCH, а не ALARM (сейчас ALARM). Q3: декодировать биты цепочки-носителя и показать контрабандные байты, как TAG-карточка показывает свой ASCII.

**11. PATCH_HISTORY.** v0_1 (2026-07-20): первый черновик КЛАССОВОЙ карточки селекторов вариаций как отдельной Mn-ветки (отличной от Cf-невидимок), в паре с `vs_cards.py`. Не прогонялся через конвейер.

**12. LIMITATION_STATEMENT.** (1) WORKING_DRAFT / NOT_CONVEYOR_RUN. (2) Валидность базы ПРИБЛИЖЕНА (emoji-плоскости/категория символов, диапазоны CJK), не точные таблицы emoji-VS / Ideographic-Variation-Database (Q1). (3) Harness моделирует таксономическое разделение, делая базу карточки невидимок VS-слепой (VS делегирован сюда); в текущем общем прототипе карточка невидимок всё ещё ссылается на VS, пока не отрефакторена. (4) Скрытые байты носителя детектируются, но не декодируются (Q3). (5) Entity/percent-доставленные селекторы ловятся только С pre-pass впереди.

**13. INTEGRATION_INTERFACE_STATUS.** INTEGRATION_STATUS: PROTOTYPED (сырой). RAW_PROTOTYPE: `vs_cards.py::vs_cards_reader(text) -> Finding`. HARNESS: `range_vs.py` (база VS-слепая по таксономическому разделению). ЖИВОЙ РЕЗУЛЬТАТ (настоящий MSL + invisible[только zero-width] + bidi + tag как база): **VS носитель/сирота 0/5 (0%) → 5/5 (100%), легит-селекторы 5/5 → 5/5, 0 новых FP** — каждая цепочка-носитель и сиротский селектор переходят в ALARM, а одиночный-селектор-на-базе (emoji VS16/VS15 и CJK supplement) остаётся OK. Это ось, которую Cf-фильтр не видит. ТРЕБУЕТСЯ для закрытия: таблицы баз emoji-VS / IVD (Q1); декод байтов носителя (Q3); pre-pass впереди; конвейер-ревью.

> КАК РАБОТАЕТ СЫРОЙ ПРОТОТИП: `MSL_MIP_HOME=/path/to/msl_mip python code/range/range_vs.py` сканирует угрозы-носители/сироты и легит-одиночные селекторы BEFORE (MSL + zero-width невидимки + bidi + tag) и AFTER (+ эта Mn-ось) и печатает вердикт до/после по кейсу и итоги, с напоминанием Mn-не-Cf.
