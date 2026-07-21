PRIVATE AUTHORIAL PROJECT / ЧАСТНЫЙ АВТОРСКИЙ ПРОЕКТ · COMMERCIAL USE PROHIBITED

# SIGN CORE CARD — INVISIBLE / ZERO-WIDTH CLASS (class card, DRAFT)

DOCUMENT_ID: SIGN_CORE_CARD_INVISIBLE_CLASS_GEN3_v0_1 · DOCUMENT_TYPE: SIGN_CORE_CARD · TEMPLATE_LINE: GEN3_v0_3
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
PRIORITY_TIER: P0 (core) · RAW_PROTOTYPE: `code/range/invisible_cards.py` · HARNESS: `code/range/range_bidi.py`
SCOPE: zero-width / default-ignorable format signs. Bidi controls, TAG characters and variation selectors are SEPARATE axes (see BIDI_CLASS, TAG_CLASS, VARIATION_SELECTOR_CLASS).

🇬🇧 [English](#english) · 🇷🇺 [Русский](#русский)

---

<a name="english"></a>
## English

DRAFT_NOTE (2026-07-20): the CLASS card for the zero-width / invisible format family — signs that render to nothing yet change the machine string. The governing law is the hardest part of the class: **INVISIBLE ≠ DANGEROUS.** ZWNJ and ZWJ have legitimate language uses (Persian, Indic, emoji), so they cannot be blindly stripped; the danger is *context* — an invisible splitting a word/domain/token, or a de-sync where one parser removes it and another keeps it. WORKING_DRAFT, NON-CONVEYOR: the raw prototype runs; conveyor closing is a separate project.

**0. UNIVERSALITY.** BOUND_TO_SPECIFIC_SIGN: CLASS (zero-width / default-ignorable) · AFTER_USE_RESIDUE: FORBIDDEN · SIGN_DATA_IS_SESSION_ONLY: YES

**1. COMMON_CONVEYOR_DISCIPLINE.** v0_3 · RUN_CARD_REQUIRED_BEFORE_LOCK: YES · MODEL_FAMILY_DIVERSITY_REQUIRED: YES · ADVERSARIAL_EVIDENCE_REQUIRED: YES · MUTATION_CHECK_REQUIRED: YES · LIMITATION_STATEMENT_REQUIRED: YES. TRACKER: WORKING_DRAFT YES; PREFLIGHT PENDING; CONVEYOR_REVIEW PENDING; WORKINGLY_CLOSED NO.

**2. META.** ZONE: ZONE_1. WHY_THIS_SIGN_MATTERS: these signs are visually absent but present in the byte/codepoint stream. They split words, domains, tokens and blacklist entries; they prefix files; they desync parsers. Unicode (UAX #31) warns that default-ignorable signs can create visually identical but machine-different identifiers. INTERACTS_WITH: DIGIT_CLASS (each is reconstructable via numeric HTML-entity, e.g. `&#8203;` → ZWSP), CANONICALIZATION_PRE_PASS (decode entities/percent first), BIDI_CLASS / TAG_CLASS / VARIATION_SELECTOR_CLASS (adjacent invisible axes, judged separately).

**3. REQUIRED_GENERAL_GUARDS.** RAW_SIGN_INPUT_STATUS: DATA_ONLY · NO_EXECUTION_FROM_SIGN: YES · NO_TRUST_FROM_SIGN: YES · DECODE_BEFORE_TRUST: YES · JUDGE_IN_CONTEXT_NOT_ON_PRESENCE: YES · NEVER_BLIND_STRIP: YES (ZWNJ/ZWJ have legit uses).

**4. SIGN IDENTITY — LAYER_A (LOCK: PERMANENT).** BASE_MODE: DATA_ONLY_INVISIBLE · BASE_MODE_FORMULA: INVISIBLE_FORM ≠ EFFECT ; PRESENCE ≠ SMUGGLE ; INVISIBLE_DETECTED ≠ SAFE_TO_DELETE.

| Codepoint | Name | Priority | Attack mechanism | Legitimate use (do NOT blind-strip) |
|---|---|---|---|---|
| U+200B | ZERO WIDTH SPACE (ZWSP) | CRITICAL | splits words / prompts / domains / tokens / blacklist entries | line-break opportunity in some layouts |
| U+200C | ZERO WIDTH NON-JOINER (ZWNJ) | HIGH | identifier/domain difference, comparison bypass | Persian, Indic scripts (mandatory) |
| U+200D | ZERO WIDTH JOINER (ZWJ) | CRITICAL | hidden insertion, emoji-sequence masking, token split | emoji ZWJ sequences, Arabic/Indic shaping |
| U+2060 | WORD JOINER (WJ) | HIGH | invisible joining, tokenization/search break | no-break binding without BOM semantics |
| U+FEFF | ZERO WIDTH NO-BREAK SPACE / BOM | HIGH | invisible prefix, parser desync, file marker | legacy BOM at file start |
| U+00AD | SOFT HYPHEN (SHY) | HIGH | keyword/domain break, moderation/search bypass | conditional hyphenation |
| U+034F | COMBINING GRAPHEME JOINER (CGJ) | HIGH (P1) | normalization/comparison difference, invisible string diff | collation/normalization control |
| U+2061..U+2064 | FUNCTION APPLICATION / INVISIBLE TIMES / SEPARATOR / PLUS | MED (Level B) | payload separation, tokenization change, filter bypass (only known zero-width removed) | math notation, machine expressions |

WHAT_THIS_SIGN_IS_NOT: (1) NOT_SMUGGLE_BY_PRESENCE — an invisible present is a WITNESS, not a verdict; (2) NOT_ALWAYS_STRIPPABLE — ZWNJ/ZWJ carry meaning in real scripts; (3) NOT_FINAL_SURFACE — may arrive as `&#8203;` or `%E2%80%8B` and must be decoded first.
BASE_FORMULAS: INVISIBLE_FORM ≠ EFFECT ; PRESENCE ≠ SMUGGLE ; INVISIBLE_DETECTED ≠ SAFE_TO_DELETE ; SMUGGLE = INVISIBLE + HOSTILE_CONTEXT.

**5. SEMANTIC_EPOCH_TRACKER (LOCK: REVIEWABLE).** EPOCH_TRACKER: NOT_APPLICABLE for the class, but per-sign the legit/attack balance shifts by substrate (ZWJ went from shaping-only to emoji-carrier). NOTE: DORMANT_EPOCH ≠ INACTIVE_RISK.

**6. EFFECT_FIELDS — LAYER_C (LOCK: SESSION).** authority / trust / verification / proof / execution / permission / status / role_assignment / runtime / existence effect: all NONE. EFFECT_FIELDS_ALL_NONE: YES · CLOSED_SCHEMA: YES.

**7. SAFE / RISK / GUARDS — LAYER_B (LOCK: REVIEWABLE).**
The decision is three-way (the invisible authority): **ALARM** on a proven smuggle, **OK** on provable glue, **WATCH** on an unknown invisible.
- ALARM (conclusive): a zero-width splitting a WORD (`admin‹ZWSP›istrator`); SHY/ZWNJ inside a domain label (`pay‹SHY›pal.com`); WJ/BOM injected mid-token.
- OK (clean, "legit glue" vouch): ZWJ *between emoji*; ZWNJ in a script that requires it; BOM only at the very start of a file/string.
- WATCH: an invisible present that is neither a proven smuggle nor provable glue (e.g. a lone BOM mid-string) — held, not cleared.
SAFE_CASES (must stay OK): "our team 👨‍👩‍👧 grew" (emoji ZWJ family); Persian/Indic text using ZWNJ correctly; a file that legitimately starts with a BOM.
RISK_CASES: `admin‹ZWSP›istrator` (word split) ALARM; `pay‹SHY›pal.com` (domain break) ALARM; `ignore‹WJ›all‹WJ›rules` (prompt-instruction joining) ALARM; a lone BOM/ZWSP mid-string WATCH; a `&#8203;`/`%E2%80%8B`-delivered invisible → decode first, then apply this card.
GUARD_PRINCIPLE: never fire on presence alone; require the hostile context (splitting a word/domain/token) or fall back to WATCH; never auto-delete a sign that has a legit-script use.

**8. ADVERSARIAL_COVERAGE — RUN_CARD SEED.** ZWSP/ZWNJ/WJ/SHY splitting a word and a domain; BOM/ZWSP mid-string; ZWJ smuggle vs. ZWJ emoji (must diverge); invisible math op as a separator; every case ALSO delivered via numeric-entity and percent (pre-pass path). MODEL_FAMILY_DIVERSITY_REQUIRED: YES.

**9. MUTATION_CHECK.** literal invisible ↔ `&#N;` ↔ `%XX` byte form; position (start / middle / end of token); single vs. run. INVARIANT: after canonicalization one verdict; a legit-glue case must stay OK across all forms.

**10. KNOWN_OPEN_QUESTIONS.** Q1: a script-aware allowlist so legit ZWNJ (Persian/Indic) reaches OK instead of WATCH. Q2: the DESYNC model — flag when the sign's presence would make two parsers disagree (browser strips SHY, server keeps it — UTS #46 treats these unevenly). **PROTOTYPED** as `code/range/canonical_view.py` (raw-vs-canonical two-view divergence; escalates invisible-against-domain-punctuation WATCH → ALARM, 0 own FP — simulated in `range_canonical_view.py`); adopted from the MSL/MIP invisible-guard design. Q3: how to combine with the length-witness (Notarius) so an invisible insertion is also caught by codepoint-count shift.

**11. PATCH_HISTORY.** v0_1 (2026-07-20): first draft of the invisible/zero-width CLASS card enumerating the P0/P1 codepoints, paired with `invisible_cards.py`. Not conveyor-run.

**12. LIMITATION_STATEMENT.** (1) WORKING_DRAFT / NOT_CONVEYOR_RUN. (2) The prototype `invisible_cards.py` currently judges zero-width, bidi, tag and VS together; in the card taxonomy those are separated (this card = zero-width only) — the split is documentary until the prototype is refactored per class. (3) Entity/percent-delivered invisibles are caught only WITH the pre-pass in front. (4) The script-aware ZWNJ allowlist (Q1) is not yet built, so some legit ZWNJ sits at WATCH, not OK. (5) Not a language-intent detector.

**13. INTEGRATION_INTERFACE_STATUS.** INTEGRATION_STATUS: PROTOTYPED (raw). RAW_PROTOTYPE: `invisible_cards.py::invisible_cards_reader(text) -> Finding`. HARNESS: `range_bidi.py`. LIVE RESULT (real MSL): **invisible/bidi threats 6/7 (85%) → 7/7 (100%), benign 5/8 → 8/8, 0 new FP** — legit `❤️`(VS16), flag-tag and balanced bidi moved from false-ALARM to OK; smuggles stay ALARM. REQUIRES for closing: pre-pass in front; the script-aware ZWNJ allowlist; conveyor review.

> HOW THE RAW PROTOTYPE WORKS: `MSL_MIP_HOME=/path/to/msl_mip python code/range/range_bidi.py` scans threats and benign controls BEFORE (MSL alone) and AFTER (MSL + this card) and prints the before/after verdict per case plus totals.

---

<a name="русский"></a>
## Русский

DRAFT_NOTE (2026-07-20): КЛАССОВАЯ карточка семейства zero-width / невидимых форматных знаков — знаков, которые рисуются в ничто, но меняют машинную строку. Управляющий закон — самое трудное в классе: **НЕВИДИМЫЙ ≠ ОПАСНЫЙ.** ZWNJ и ZWJ имеют законные языковые применения (персидский, индийские письменности, emoji), поэтому их нельзя слепо вырезать; опасность — в *контексте*: невидимый, рвущий слово/домен/токен, или де-синхрон, когда один парсер удаляет, другой оставляет. WORKING_DRAFT, БЕЗКОНВЕЙЕРНО: сырой прототип бежит; закрытие конвейером — отдельный проект.

**0. UNIVERSALITY.** BOUND_TO_SPECIFIC_SIGN: CLASS (zero-width / default-ignorable) · AFTER_USE_RESIDUE: FORBIDDEN · SIGN_DATA_IS_SESSION_ONLY: YES

**1. COMMON_CONVEYOR_DISCIPLINE.** v0_3 · RUN_CARD_REQUIRED_BEFORE_LOCK: YES · MODEL_FAMILY_DIVERSITY_REQUIRED: YES · ADVERSARIAL_EVIDENCE_REQUIRED: YES · MUTATION_CHECK_REQUIRED: YES · LIMITATION_STATEMENT_REQUIRED: YES. TRACKER: WORKING_DRAFT YES; PREFLIGHT PENDING; CONVEYOR_REVIEW PENDING; WORKINGLY_CLOSED NO.

**2. META.** ZONE: ZONE_1. WHY_THIS_SIGN_MATTERS: эти знаки визуально отсутствуют, но присутствуют в потоке байтов/кодпоинтов. Они рвут слова, домены, токены и записи blacklist; префиксуют файлы; десинхронизируют парсеры. Unicode (UAX #31) предупреждает, что default-ignorable-знаки создают визуально одинаковые, но машинно различные идентификаторы. INTERACTS_WITH: DIGIT_CLASS (каждый воссоздаётся числовой HTML-entity, напр. `&#8203;` → ZWSP), CANONICALIZATION_PRE_PASS (сперва декодировать entity/percent), BIDI_CLASS / TAG_CLASS / VARIATION_SELECTOR_CLASS (смежные невидимые оси, судятся отдельно).

**3. REQUIRED_GENERAL_GUARDS.** RAW_SIGN_INPUT_STATUS: DATA_ONLY · NO_EXECUTION_FROM_SIGN: YES · NO_TRUST_FROM_SIGN: YES · DECODE_BEFORE_TRUST: YES · JUDGE_IN_CONTEXT_NOT_ON_PRESENCE: YES · NEVER_BLIND_STRIP: YES (у ZWNJ/ZWJ есть легит-применения).

**4. SIGN IDENTITY — LAYER_A (LOCK: PERMANENT).** BASE_MODE: DATA_ONLY_INVISIBLE · BASE_MODE_FORMULA: INVISIBLE_FORM ≠ EFFECT ; PRESENCE ≠ SMUGGLE ; INVISIBLE_DETECTED ≠ SAFE_TO_DELETE.

| Кодпоинт | Имя | Приоритет | Механизм атаки | Легит-применение (НЕ вырезать слепо) |
|---|---|---|---|---|
| U+200B | ZERO WIDTH SPACE (ZWSP) | КРИТИЧ. | рвёт слова / промпты / домены / токены / записи blacklist | точка переноса в части раскладок |
| U+200C | ZERO WIDTH NON-JOINER (ZWNJ) | ВЫСОКИЙ | различие идентиф./домена, обход сравнения | персидский, индийские письменности (обязателен) |
| U+200D | ZERO WIDTH JOINER (ZWJ) | КРИТИЧ. | скрытая вставка, маскировка emoji-sequence, разрыв токена | emoji-ZWJ, арабское/индийское формообразование |
| U+2060 | WORD JOINER (WJ) | ВЫСОКИЙ | невидимое соединение, разрыв токенизации/поиска | неразрывная связка без семантики BOM |
| U+FEFF | ZERO WIDTH NO-BREAK SPACE / BOM | ВЫСОКИЙ | невидимый префикс, десинхрон парсеров, маркер файла | legacy BOM в начале файла |
| U+00AD | SOFT HYPHEN (SHY) | ВЫСОКИЙ | разрыв ключевого слова/домена, обход модерации/поиска | условный перенос |
| U+034F | COMBINING GRAPHEME JOINER (CGJ) | ВЫСОКИЙ (P1) | различие нормализации/сравнения, невидимое различие строк | контроль collation/нормализации |
| U+2061..U+2064 | FUNCTION APPLICATION / INVISIBLE TIMES / SEPARATOR / PLUS | СРЕД. (Level B) | разделение payload, изменение токенизации, обход фильтров (удаляют лишь известные zero-width) | матнотация, машинные выражения |

WHAT_THIS_SIGN_IS_NOT: (1) NOT_SMUGGLE_BY_PRESENCE — присутствующий невидимый это СВИДЕТЕЛЬ, не вердикт; (2) NOT_ALWAYS_STRIPPABLE — у ZWNJ/ZWJ есть смысл в реальных письменностях; (3) NOT_FINAL_SURFACE — может прийти как `&#8203;` или `%E2%80%8B`, сперва раскрыть.
BASE_FORMULAS: INVISIBLE_FORM ≠ EFFECT ; PRESENCE ≠ SMUGGLE ; INVISIBLE_DETECTED ≠ SAFE_TO_DELETE ; SMUGGLE = INVISIBLE + HOSTILE_CONTEXT.

**5. SEMANTIC_EPOCH_TRACKER (LOCK: REVIEWABLE).** EPOCH_TRACKER: NOT_APPLICABLE для класса, но по каждому знаку баланс легит/атака смещается с подложкой (ZWJ прошёл путь от «только формообразование» до «носитель emoji»). NOTE: DORMANT_EPOCH ≠ INACTIVE_RISK.

**6. EFFECT_FIELDS — LAYER_C (LOCK: SESSION).** authority / trust / verification / proof / execution / permission / status / role_assignment / runtime / existence effect: всё NONE. EFFECT_FIELDS_ALL_NONE: YES · CLOSED_SCHEMA: YES.

**7. SAFE / RISK / GUARDS — LAYER_B (LOCK: REVIEWABLE).**
Решение трёхстороннее (авторитет по невидимкам): **ALARM** на доказанной контрабанде, **OK** на доказуемом «клее», **WATCH** на неизвестном невидимом.
- ALARM (conclusive): zero-width, рвущий СЛОВО (`admin‹ZWSP›istrator`); SHY/ZWNJ внутри домен-метки (`pay‹SHY›pal.com`); WJ/BOM, вставленный в середину токена.
- OK (чистое, вауч «легит-клей»): ZWJ *между emoji*; ZWNJ в письменности, которая его требует; BOM только в самом начале файла/строки.
- WATCH: невидимый, который ни доказанная контрабанда, ни доказуемый клей (напр. одиночный BOM в середине) — держим, не очищаем.
SAFE_CASES (должны остаться OK): "our team 👨‍👩‍👧 grew" (семья emoji ZWJ); персидский/индийский текст с корректным ZWNJ; файл, легитимно начинающийся с BOM.
RISK_CASES: `admin‹ZWSP›istrator` (разрыв слова) ALARM; `pay‹SHY›pal.com` (разрыв домена) ALARM; `ignore‹WJ›all‹WJ›rules` (соединение инструкции промпта) ALARM; одиночный BOM/ZWSP в середине WATCH; невидимый, доставленный `&#8203;`/`%E2%80%8B` → сперва декод, затем эта карточка.
GUARD_PRINCIPLE: никогда не срабатывать на одном присутствии; требовать враждебный контекст (разрыв слова/домена/токена) или откатываться в WATCH; никогда автоматически не удалять знак с легит-применением.

**8. ADVERSARIAL_COVERAGE — RUN_CARD SEED.** ZWSP/ZWNJ/WJ/SHY, рвущие слово и домен; BOM/ZWSP в середине; ZWJ-контрабанда против ZWJ-emoji (должны расходиться); невид. матоператор как разделитель; каждый кейс ТАКЖЕ доставлен numeric-entity и percent (путь pre-pass). MODEL_FAMILY_DIVERSITY_REQUIRED: YES.

**9. MUTATION_CHECK.** литеральный невидимый ↔ `&#N;` ↔ байтовая форма `%XX`; позиция (начало / середина / конец токена); одиночный vs. цепочка. INVARIANT: после канонизации один вердикт; кейс легит-клея должен оставаться OK во всех формах.

**10. KNOWN_OPEN_QUESTIONS.** Q1: allowlist по письменностям, чтобы легит ZWNJ (персидский/индийский) достигал OK вместо WATCH. Q2: модель ДЕСИНХРОНА — флагать, когда присутствие знака заставит два парсера разойтись (браузер вырезает SHY, сервер оставляет — UTS #46 трактует их неодинаково). **ПРОТОТИПИРОВАНО** как `code/range/canonical_view.py` (расхождение двух прочтений raw-vs-canonical; повышает невидимый-рядом-с-доменной-пунктуацией WATCH → ALARM, 0 собственных FP — симуляция в `range_canonical_view.py`); взято из MSL/MIP invisible-guard дизайна. Q3: как совместить с уликой-длины (Notarius), чтобы невидимая вставка ловилась ещё и сдвигом счётчика кодпоинтов.

**11. PATCH_HISTORY.** v0_1 (2026-07-20): первый черновик невидимой/zero-width КЛАССОВОЙ карточки с перечислением кодпоинтов P0/P1, в паре с `invisible_cards.py`. Не прогонялся через конвейер.

**12. LIMITATION_STATEMENT.** (1) WORKING_DRAFT / NOT_CONVEYOR_RUN. (2) Прототип `invisible_cards.py` сейчас судит zero-width, bidi, tag и VS вместе; в таксономии карточек они разделены (эта карточка = только zero-width) — разделение документарное, пока прототип не отрефакторен по классам. (3) Entity/percent-доставленные невидимки ловятся только С pre-pass впереди. (4) Allowlist ZWNJ по письменностям (Q1) ещё не построен, поэтому часть легит ZWNJ стоит на WATCH, а не OK. (5) Не детектор языкового смысла.

**13. INTEGRATION_INTERFACE_STATUS.** INTEGRATION_STATUS: PROTOTYPED (сырой). RAW_PROTOTYPE: `invisible_cards.py::invisible_cards_reader(text) -> Finding`. HARNESS: `range_bidi.py`. ЖИВОЙ РЕЗУЛЬТАТ (настоящий MSL): **невидимые/bidi угрозы 6/7 (85%) → 7/7 (100%), безобидное 5/8 → 8/8, 0 новых FP** — легит `❤️`(VS16), флаг-tag и сбалансированный bidi перешли из ложного ALARM в OK; контрабанда осталась ALARM. ТРЕБУЕТСЯ для закрытия: pre-pass впереди; allowlist ZWNJ по письменностям; конвейер-ревью.

> КАК РАБОТАЕТ СЫРОЙ ПРОТОТИП: `MSL_MIP_HOME=/path/to/msl_mip python code/range/range_bidi.py` сканирует угрозы и безобидные контроли BEFORE (MSL один) и AFTER (MSL + эта карточка) и печатает вердикт до/после по кейсу и итоги.
