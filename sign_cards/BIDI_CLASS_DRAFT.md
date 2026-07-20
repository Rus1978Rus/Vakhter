PRIVATE AUTHORIAL PROJECT / ЧАСТНЫЙ АВТОРСКИЙ ПРОЕКТ · COMMERCIAL USE PROHIBITED

# SIGN CORE CARD — BIDI / DIRECTIONAL-CONTROL CLASS (class card, DRAFT)

DOCUMENT_ID: SIGN_CORE_CARD_BIDI_CLASS_GEN3_v0_1 · DOCUMENT_TYPE: SIGN_CORE_CARD · TEMPLATE_LINE: GEN3_v0_3
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
PRIORITY_TIER: P0 (core) · RAW_PROTOTYPE: `code/range/bidi_cards.py` · HARNESS: `code/range/range_bidi_axis.py`
SCOPE: bidirectional format controls — embeddings, overrides, isolates, pops, implicit marks. Zero-width signs, TAG characters and variation selectors are SEPARATE axes (see INVISIBLE_CLASS, TAG_CLASS, VARIATION_SELECTOR_CLASS).

🇬🇧 [English](#english) · 🇷🇺 [Русский](#русский)

---

<a name="english"></a>
## English

DRAFT_NOTE (2026-07-20): the CLASS card for the bidi / directional-control family — a SEPARATE axis from the invisible card. A zero-width sign hides a byte; a bidi control does something categorically different: it makes the **LOGICAL (byte) order diverge from the VISUAL (rendered) order**. That divergence is the Trojan-Source attack (CVE-2021-42574) — a reviewer sees one thing, the compiler/parser consumes another. The governing law of the class is **BIDI_DETECTED ≠ SAFE_TO_DELETE**: these controls are mandatory to render Arabic/Hebrew correctly, so stripping them corrupts real text; the verdict is reject-or-review, never silent deletion. WORKING_DRAFT, NON-CONVEYOR: the raw prototype runs; conveyor closing is a separate project.

**0. UNIVERSALITY.** BOUND_TO_SPECIFIC_SIGN: CLASS (bidirectional format controls) · AFTER_USE_RESIDUE: FORBIDDEN · SIGN_DATA_IS_SESSION_ONLY: YES

**1. COMMON_CONVEYOR_DISCIPLINE.** v0_3 · RUN_CARD_REQUIRED_BEFORE_LOCK: YES · MODEL_FAMILY_DIVERSITY_REQUIRED: YES · ADVERSARIAL_EVIDENCE_REQUIRED: YES · MUTATION_CHECK_REQUIRED: YES · LIMITATION_STATEMENT_REQUIRED: YES. TRACKER: WORKING_DRAFT YES; PREFLIGHT PENDING; CONVEYOR_REVIEW PENDING; WORKINGLY_CLOSED NO.

**2. META.** ZONE: ZONE_1. WHY_THIS_SIGN_MATTERS: bidi controls reorder how text renders without changing the bytes. An override (LRO/RLO) or an unbalanced isolate/embedding lets an attacker place code, comments or identifiers so the eye reads one order and the machine another — the Trojan-Source class (Boucher & Anderson, 2021; Unicode UAX #9, UTS #55). This is why the axis is judged separately from zero-width: the danger is *reordering*, not *hiding*. INTERACTS_WITH: INVISIBLE_CLASS (adjacent invisible axis — gross open/close imbalance overlaps; this card adds override-reorder and pop-underflow), CANONICALIZATION_PRE_PASS (decode entities/percent first — a control can arrive as `&#8238;` → RLO), NOTARIUS (length/codepoint witness — a bidi insertion also shifts the count).

**3. REQUIRED_GENERAL_GUARDS.** RAW_SIGN_INPUT_STATUS: DATA_ONLY · NO_EXECUTION_FROM_SIGN: YES · NO_TRUST_FROM_SIGN: YES · DECODE_BEFORE_TRUST: YES · JUDGE_IN_CONTEXT_NOT_ON_PRESENCE: YES · NEVER_BLIND_STRIP: YES (bidi controls carry real RTL layout).

**4. SIGN IDENTITY — LAYER_A (LOCK: PERMANENT).** BASE_MODE: DATA_ONLY_DIRECTIONAL · BASE_MODE_FORMULA: BIDI_FORM ≠ EFFECT ; PRESENCE ≠ REORDER_ATTACK ; BIDI_DETECTED ≠ SAFE_TO_DELETE.

| Codepoint | Name | Role | Priority | Attack mechanism | Legitimate use (do NOT blind-strip) |
|---|---|---|---|---|---|
| U+202E | RIGHT-TO-LEFT OVERRIDE (RLO) | override | CRITICAL | forces RTL on LTR text — the classic Trojan Source / filename spoof | almost never in plain text (deprecated for content) |
| U+202D | LEFT-TO-RIGHT OVERRIDE (LRO) | override | CRITICAL | forces LTR — reorders readable tokens | almost never in plain text |
| U+202A / U+202B | LRE / RLE (embedding) | embed | HIGH | unbalanced embedding leaks direction past its line | legacy layout of mixed-direction runs |
| U+202C | POP DIRECTIONAL FORMATTING (PDF) | pop | HIGH | underflow / mismatched pop desyncs scope | closes an LRE/RLE/LRO/RLO |
| U+2066 / U+2067 / U+2068 | LRI / RLI / FSI (isolate) | isolate | HIGH | unbalanced isolate leaks; nesting depth spill | modern, PREFERRED way to wrap a mixed run |
| U+2069 | POP DIRECTIONAL ISOLATE (PDI) | pop | HIGH | pop underflow desyncs isolate scope | closes an LRI/RLI/FSI |
| U+200E / U+200F | LRM / RLM (implicit mark) | mark | MED | subtle digit/punctuation reordering near boundaries | mandatory to fix weak-char direction in RTL text |
| U+061C | ARABIC LETTER MARK (ALM) | mark | MED | same as LRM/RLM for Arabic-script context | mandatory in Arabic numeric/punctuation layout |

WHAT_THIS_SIGN_IS_NOT: (1) NOT_ATTACK_BY_PRESENCE — a balanced isolate around Arabic text is legitimate layout, not a smuggle; (2) NOT_STRIPPABLE — deleting RLM/RLI from real RTL text corrupts it; (3) NOT_FINAL_SURFACE — may arrive as `&#8238;` or `%E2%80%AE` and must be decoded first.
BASE_FORMULAS: BIDI_FORM ≠ EFFECT ; PRESENCE ≠ REORDER_ATTACK ; BIDI_DETECTED ≠ SAFE_TO_DELETE ; REORDER_ATTACK = OVERRIDE/IMBALANCE + READABLE_LTR_CONTENT.

**5. SEMANTIC_EPOCH_TRACKER (LOCK: REVIEWABLE).** EPOCH_TRACKER: the axis shifted with Unicode 6.3 — isolates (LRI/RLI/FSI/PDI) were added and are now the PREFERRED mechanism, while embeddings/overrides for content are deprecated. So an override in modern content is a stronger anomaly than it was pre-2013. NOTE: DEPRECATED_MECHANISM ≠ HARMLESS (renderers still honour it).

**6. EFFECT_FIELDS — LAYER_C (LOCK: SESSION).** authority / trust / verification / proof / execution / permission / status / role_assignment / runtime / existence effect: all NONE. EFFECT_FIELDS_ALL_NONE: YES · CLOSED_SCHEMA: YES.

**7. SAFE / RISK / GUARDS — LAYER_B (LOCK: REVIEWABLE).**
The decision is three-way (the bidi authority): **ALARM** on a proven reorder/imbalance, **OK** on balanced controls over genuine RTL layout, **WATCH** on bidi present without provable legit context.
- ALARM (conclusive): an OVERRIDE run (LRO/RLO) whose scope carries readable LTR/ASCII (`level‹RLO›NIMDA‹PDF›` reorders to "ADMIN"); directional IMBALANCE (embedding/isolate opened, never closed; pop underflow); a bidi control wedged inside a LTR code token (`user‹RLI›name`).
- OK (clean, "legit layout" vouch): balanced isolates/embeddings around real RTL script (`name: ‹FSI›مرحبا‹PDI›`); bare implicit marks (RLM/LRM/ALM) adjacent to RTL text.
- WATCH: bidi present, balanced, but not provably RTL-legit and not a proven smuggle — held, reviewed, NOT deleted.
SAFE_CASES (must stay OK): plain Arabic/Hebrew text; `name: ‹FSI›مرحبا‹PDI› (verified)` (isolated RTL run); `‹RLE›שלום‹PDF›` (balanced embedding); `مرحبا‹RLM› 2026` (mark fixing digit direction).
RISK_CASES: `access = level‹RLO›NIMDA‹PDF› ok` (override reorder → "ADMIN") ALARM; `return 1;‹RLO›// ‹PDF›safe` (Trojan comment) ALARM; `if isAdmin‹LRO› return true` (override left open) ALARM; `value‹PDI› = 42` (pop underflow) ALARM; a lone balanced isolate around non-RTL content WATCH.
GUARD_PRINCIPLE: fire on override-over-LTR or imbalance, not on presence; a control near genuine RTL script vouches to OK; when neither, WATCH; NEVER auto-delete a control (that corrupts real RTL text) — flag for reject-or-review.

**8. ADVERSARIAL_COVERAGE — RUN_CARD SEED.** RLO/LRO reorder over identifiers, over `//` comments, over string literals; unbalanced LRE/RLE/LRI/RLI; PDF/PDI underflow; override vs. balanced-isolate-around-RTL (must diverge); every case ALSO delivered via numeric-entity and percent (pre-pass path). MODEL_FAMILY_DIVERSITY_REQUIRED: YES.

**9. MUTATION_CHECK.** literal control ↔ `&#N;` ↔ `%XX` byte form; override vs. embedding vs. isolate carrying the same payload; balanced vs. off-by-one nesting. INVARIANT: after canonicalization one verdict; a balanced-RTL-layout case must stay OK across all forms; an override-over-LTR must stay ALARM.

**10. KNOWN_OPEN_QUESTIONS.** Q1: a real UBA (Unicode Bidi Algorithm) mini-model to compute the actual visual order and compare against logical order, instead of the override/imbalance heuristics used here. Q2: line-scoped analysis (bidi scope resets at paragraph/line boundaries — a per-line depth check would catch cross-line leaks that a whole-string check blurs). Q3: script-run awareness so a mark inside a genuinely mixed LTR/RTL sentence reaches OK instead of WATCH.

**11. PATCH_HISTORY.** v0_1 (2026-07-20): first draft of the bidi/directional-control CLASS card, separating the reorder axis from the invisible axis, paired with `bidi_cards.py`. Not conveyor-run.

**12. LIMITATION_STATEMENT.** (1) WORKING_DRAFT / NOT_CONVEYOR_RUN. (2) The prototype uses override/imbalance/token-split heuristics, NOT a full Unicode Bidi Algorithm — it will miss reorderings that need real UBA resolution and may WATCH some legit mixed runs (Q1/Q3). (3) Balance is checked over the whole string, not per line/paragraph — a control that is "balanced" globally but leaks across a line boundary can be missed (Q2). (4) Entity/percent-delivered controls are caught only WITH the pre-pass in front. (5) Not a language-intent detector.

**13. INTEGRATION_INTERFACE_STATUS.** INTEGRATION_STATUS: PROTOTYPED (raw). RAW_PROTOTYPE: `bidi_cards.py::bidi_cards_reader(text) -> Finding`. HARNESS: `range_bidi_axis.py`. LIVE RESULT (real MSL + invisible card as baseline): **bidi-axis threats 5/6 (83%) → 6/6 (100%), legit RTL 6/6 → 6/6, 0 new FP** — the added catch is the BALANCED override that reorders LTR content (`level‹RLO›NIMDA‹PDF›`), which the invisible card passes as "balanced"; the separate axis flags it because an override over readable LTR is logical≠visual. All legit RTL layout stays OK and is never deleted. REQUIRES for closing: UBA mini-model (Q1); per-line scope (Q2); pre-pass in front; conveyor review.

> HOW THE RAW PROTOTYPE WORKS: `MSL_MIP_HOME=/path/to/msl_mip python code/range/range_bidi_axis.py` scans reorder threats and legit RTL layout BEFORE (MSL + invisible card) and AFTER (+ this bidi axis) and prints the before/after verdict per case plus totals; it also prints the NEVER_BLIND_STRIP reminder.

---

<a name="русский"></a>
## Русский

DRAFT_NOTE (2026-07-20): КЛАССОВАЯ карточка семейства bidi / направляющих контролей — ОТДЕЛЬНАЯ ось от карточки невидимок. Zero-width прячет байт; bidi-контроль делает категорически иное: заставляет **ЛОГИЧЕСКИЙ (байтовый) порядок разойтись с ВИЗУАЛЬНЫМ (отрисованным)**. Это расхождение и есть атака Trojan Source (CVE-2021-42574) — ревьюер видит одно, компилятор/парсер потребляет другое. Управляющий закон класса — **BIDI_DETECTED ≠ БЕЗОПАСНО_УДАЛИТЬ**: эти контроли обязательны для корректной отрисовки арабского/иврита, поэтому их вырезание портит настоящий текст; вердикт — отклонить-или-проверить, никогда не тихое удаление. WORKING_DRAFT, БЕЗКОНВЕЙЕРНО: сырой прототип бежит; закрытие конвейером — отдельный проект.

**0. UNIVERSALITY.** BOUND_TO_SPECIFIC_SIGN: CLASS (bidi-направляющие форматные контроли) · AFTER_USE_RESIDUE: FORBIDDEN · SIGN_DATA_IS_SESSION_ONLY: YES

**1. COMMON_CONVEYOR_DISCIPLINE.** v0_3 · RUN_CARD_REQUIRED_BEFORE_LOCK: YES · MODEL_FAMILY_DIVERSITY_REQUIRED: YES · ADVERSARIAL_EVIDENCE_REQUIRED: YES · MUTATION_CHECK_REQUIRED: YES · LIMITATION_STATEMENT_REQUIRED: YES. TRACKER: WORKING_DRAFT YES; PREFLIGHT PENDING; CONVEYOR_REVIEW PENDING; WORKINGLY_CLOSED NO.

**2. META.** ZONE: ZONE_1. WHY_THIS_SIGN_MATTERS: bidi-контроли переставляют то, КАК текст рисуется, не меняя байтов. Override (LRO/RLO) или несбалансированный isolate/embedding позволяет разместить код, комментарии или идентификаторы так, что глаз читает один порядок, а машина — другой (класс Trojan Source; Boucher & Anderson, 2021; Unicode UAX #9, UTS #55). Поэтому ось судится отдельно от zero-width: опасность в *перестановке*, а не в *сокрытии*. INTERACTS_WITH: INVISIBLE_CLASS (смежная невидимая ось — грубый дисбаланс open/close пересекается; эта карточка добавляет override-reorder и pop-underflow), CANONICALIZATION_PRE_PASS (сперва декодировать entity/percent — контроль может прийти как `&#8238;` → RLO), NOTARIUS (улика длины/кодпоинтов — bidi-вставка тоже сдвигает счётчик).

**3. REQUIRED_GENERAL_GUARDS.** RAW_SIGN_INPUT_STATUS: DATA_ONLY · NO_EXECUTION_FROM_SIGN: YES · NO_TRUST_FROM_SIGN: YES · DECODE_BEFORE_TRUST: YES · JUDGE_IN_CONTEXT_NOT_ON_PRESENCE: YES · NEVER_BLIND_STRIP: YES (bidi-контроли несут настоящую RTL-раскладку).

**4. SIGN IDENTITY — LAYER_A (LOCK: PERMANENT).** BASE_MODE: DATA_ONLY_DIRECTIONAL · BASE_MODE_FORMULA: BIDI_FORM ≠ EFFECT ; PRESENCE ≠ REORDER_ATTACK ; BIDI_DETECTED ≠ SAFE_TO_DELETE.

| Кодпоинт | Имя | Роль | Приоритет | Механизм атаки | Легит-применение (НЕ вырезать слепо) |
|---|---|---|---|---|---|
| U+202E | RIGHT-TO-LEFT OVERRIDE (RLO) | override | КРИТИЧ. | форсирует RTL на LTR-тексте — классический Trojan Source / спуф имени файла | почти никогда в обычном тексте (для контента устарел) |
| U+202D | LEFT-TO-RIGHT OVERRIDE (LRO) | override | КРИТИЧ. | форсирует LTR — переставляет читаемые токены | почти никогда в обычном тексте |
| U+202A / U+202B | LRE / RLE (embedding) | embed | ВЫСОКИЙ | несбалансированный embedding утекает направлением за свою строку | legacy-раскладка смешанных прогонов |
| U+202C | POP DIRECTIONAL FORMATTING (PDF) | pop | ВЫСОКИЙ | underflow / несогласованный pop десинхронизирует область | закрывает LRE/RLE/LRO/RLO |
| U+2066 / U+2067 / U+2068 | LRI / RLI / FSI (isolate) | isolate | ВЫСОКИЙ | несбалансированный isolate утекает; переполнение глубины вложения | современный, ПРЕДПОЧТИТЕЛЬНЫЙ способ обернуть смешанный прогон |
| U+2069 | POP DIRECTIONAL ISOLATE (PDI) | pop | ВЫСОКИЙ | pop-underflow десинхронизирует область isolate | закрывает LRI/RLI/FSI |
| U+200E / U+200F | LRM / RLM (implicit mark) | mark | СРЕД. | тонкая перестановка цифр/пунктуации у границ | обязателен для фиксации направления слабых символов в RTL-тексте |
| U+061C | ARABIC LETTER MARK (ALM) | mark | СРЕД. | то же, что LRM/RLM, для арабского контекста | обязателен в арабской числовой/пунктуационной раскладке |

WHAT_THIS_SIGN_IS_NOT: (1) NOT_ATTACK_BY_PRESENCE — сбалансированный isolate вокруг арабского текста это легит-раскладка, не контрабанда; (2) NOT_STRIPPABLE — удаление RLM/RLI из настоящего RTL-текста портит его; (3) NOT_FINAL_SURFACE — может прийти как `&#8238;` или `%E2%80%AE`, сперва раскрыть.
BASE_FORMULAS: BIDI_FORM ≠ EFFECT ; PRESENCE ≠ REORDER_ATTACK ; BIDI_DETECTED ≠ SAFE_TO_DELETE ; REORDER_ATTACK = OVERRIDE/IMBALANCE + ЧИТАЕМЫЙ_LTR_КОНТЕНТ.

**5. SEMANTIC_EPOCH_TRACKER (LOCK: REVIEWABLE).** EPOCH_TRACKER: ось сместилась с Unicode 6.3 — добавлены isolates (LRI/RLI/FSI/PDI), теперь они ПРЕДПОЧТИТЕЛЬНЫЙ механизм, а embedding/override для контента устарели. Поэтому override в современном контенте — более сильная аномалия, чем до 2013. NOTE: DEPRECATED_MECHANISM ≠ БЕЗВРЕДНО (отрисовщики его всё ещё исполняют).

**6. EFFECT_FIELDS — LAYER_C (LOCK: SESSION).** authority / trust / verification / proof / execution / permission / status / role_assignment / runtime / existence effect: всё NONE. EFFECT_FIELDS_ALL_NONE: YES · CLOSED_SCHEMA: YES.

**7. SAFE / RISK / GUARDS — LAYER_B (LOCK: REVIEWABLE).**
Решение трёхстороннее (авторитет по bidi): **ALARM** на доказанной перестановке/дисбалансе, **OK** на сбалансированных контролях над настоящей RTL-раскладкой, **WATCH** на bidi без доказуемого легит-контекста.
- ALARM (conclusive): OVERRIDE-прогон (LRO/RLO), чья область несёт читаемый LTR/ASCII (`level‹RLO›NIMDA‹PDF›` переставляется в "ADMIN"); направляющий ДИСБАЛАНС (embedding/isolate открыт, не закрыт; pop-underflow); bidi-контроль, вклиненный в LTR-код-токен (`user‹RLI›name`).
- OK (чистое, вауч «легит-раскладка»): сбалансированные isolate/embedding вокруг настоящей RTL-письменности (`name: ‹FSI›مرحبا‹PDI›`); голые implicit-марки (RLM/LRM/ALM) рядом с RTL-текстом.
- WATCH: bidi присутствует, сбалансирован, но не доказуемо RTL-легит и не доказанная контрабанда — держим, проверяем, НЕ удаляем.
SAFE_CASES (должны остаться OK): обычный арабский/иврит; `name: ‹FSI›مرحبا‹PDI› (verified)` (изолированный RTL-прогон); `‹RLE›שלום‹PDF›` (сбалансированный embedding); `مرحبا‹RLM› 2026` (марка, фиксирующая направление цифры).
RISK_CASES: `access = level‹RLO›NIMDA‹PDF› ok` (override-перестановка → "ADMIN") ALARM; `return 1;‹RLO›// ‹PDF›safe` (Trojan-комментарий) ALARM; `if isAdmin‹LRO› return true` (override оставлен открытым) ALARM; `value‹PDI› = 42` (pop-underflow) ALARM; одиночный сбалансированный isolate вокруг не-RTL контента WATCH.
GUARD_PRINCIPLE: срабатывать на override-над-LTR или дисбаланс, не на присутствие; контроль рядом с настоящей RTL-письменностью вауч в OK; когда ни то ни другое — WATCH; НИКОГДА автоматически не удалять контроль (это портит настоящий RTL-текст) — флагать на отклонить-или-проверить.

**8. ADVERSARIAL_COVERAGE — RUN_CARD SEED.** RLO/LRO-перестановка над идентификаторами, над `//`-комментариями, над строковыми литералами; несбалансированные LRE/RLE/LRI/RLI; PDF/PDI-underflow; override против сбалансированного-isolate-вокруг-RTL (должны расходиться); каждый кейс ТАКЖЕ доставлен numeric-entity и percent (путь pre-pass). MODEL_FAMILY_DIVERSITY_REQUIRED: YES.

**9. MUTATION_CHECK.** литеральный контроль ↔ `&#N;` ↔ байтовая форма `%XX`; override vs. embedding vs. isolate с одним payload; сбалансированное vs. вложение с ошибкой на единицу. INVARIANT: после канонизации один вердикт; кейс сбалансированной RTL-раскладки должен оставаться OK во всех формах; override-над-LTR должен оставаться ALARM.

**10. KNOWN_OPEN_QUESTIONS.** Q1: настоящая мини-модель UBA (Unicode Bidi Algorithm) для вычисления фактического визуального порядка и сравнения с логическим — вместо использованных здесь эвристик override/дисбаланс. Q2: анализ с областью по строкам (область bidi сбрасывается на границе абзаца/строки — проверка глубины по строкам поймала бы межстрочные утечки, которые размывает проверка по всей строке). Q3: осознание script-run, чтобы марка внутри реально смешанного LTR/RTL-предложения достигала OK вместо WATCH.

**11. PATCH_HISTORY.** v0_1 (2026-07-20): первый черновик bidi/направляющей КЛАССОВОЙ карточки, отделяющий ось перестановки от оси невидимок, в паре с `bidi_cards.py`. Не прогонялся через конвейер.

**12. LIMITATION_STATEMENT.** (1) WORKING_DRAFT / NOT_CONVEYOR_RUN. (2) Прототип использует эвристики override/дисбаланс/token-split, НЕ полный Unicode Bidi Algorithm — он пропустит перестановки, требующие настоящего разрешения UBA, и может держать на WATCH часть легит смешанных прогонов (Q1/Q3). (3) Баланс проверяется по всей строке, не по строке/абзацу — контроль, «сбалансированный» глобально, но утекающий через границу строки, может быть пропущен (Q2). (4) Entity/percent-доставленные контроли ловятся только С pre-pass впереди. (5) Не детектор языкового смысла.

**13. INTEGRATION_INTERFACE_STATUS.** INTEGRATION_STATUS: PROTOTYPED (сырой). RAW_PROTOTYPE: `bidi_cards.py::bidi_cards_reader(text) -> Finding`. HARNESS: `range_bidi_axis.py`. ЖИВОЙ РЕЗУЛЬТАТ (настоящий MSL + карточка невидимок как база): **bidi-ось угрозы 5/6 (83%) → 6/6 (100%), легит RTL 6/6 → 6/6, 0 новых FP** — добавленный улов это СБАЛАНСИРОВАННЫЙ override, переставляющий LTR-контент (`level‹RLO›NIMDA‹PDF›`), который карточка невидимок пропускает как «сбалансированный»; отдельная ось флагает его, потому что override над читаемым LTR это логический≠визуальный. Вся легит RTL-раскладка остаётся OK и никогда не удаляется. ТРЕБУЕТСЯ для закрытия: мини-модель UBA (Q1); область по строкам (Q2); pre-pass впереди; конвейер-ревью.

> КАК РАБОТАЕТ СЫРОЙ ПРОТОТИП: `MSL_MIP_HOME=/path/to/msl_mip python code/range/range_bidi_axis.py` сканирует угрозы-перестановки и легит RTL-раскладку BEFORE (MSL + карточка невидимок) и AFTER (+ эта bidi-ось) и печатает вердикт до/после по кейсу и итоги; также печатает напоминание NEVER_BLIND_STRIP.
