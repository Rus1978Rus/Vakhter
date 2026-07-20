PRIVATE AUTHORIAL PROJECT / ЧАСТНЫЙ АВТОРСКИЙ ПРОЕКТ · COMMERCIAL USE PROHIBITED

# SIGN CORE CARD — MONITORED-FORMAT / WITNESS CLASS (class card, DRAFT)

DOCUMENT_ID: SIGN_CORE_CARD_MONITORED_FORMAT_CLASS_GEN3_v0_1 · DOCUMENT_TYPE: SIGN_CORE_CARD · TEMPLATE_LINE: GEN3_v0_3
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
PRIORITY_TIER: P2 (witness/monitor — NOT auto-HIGH) · RAW_PROTOTYPE: `code/range/monitored_cards.py` · HARNESS: `code/range/range_monitored.py`
SCOPE: rare / deprecated / substrate-bound format controls — U+180E, U+206A–U+206F, U+1BCA0–U+1BCA3 (shorthand), U+1D173–U+1D17A (musical). The high-vector invisibles are their own cards (INVISIBLE / BIDI / TAG / VARIATION_SELECTOR / WHITESPACE).

🇬🇧 [English](#english) · 🇷🇺 [Русский](#русский)

---

<a name="english"></a>
## English

DRAFT_NOTE (2026-07-20): the CLASS card for the monitored-format tier — the operational form of the doctrine **OBSERVE ALL, PRIORITIZE THE REAL VECTORS.** Its members are rare, low-vector, mostly deprecated or substrate-bound format controls. The whole point of the card is restraint: these are **NOT auto-HIGH**. The default posture is WITNESS (WATCH) — seen, logged, held, never auto-stripped — and it escalates to ALARM only when a monitored control appears in a genuinely hostile context (splitting a word/token, or against a syntax metacharacter). A control sitting inside its ONE legitimate substrate (a musical control among musical symbols; a shorthand control among Duployan letters) is vouched OK. This is the card that keeps the contour honest: the full set is observed, but severity is spent only on real vectors. WORKING_DRAFT, NON-CONVEYOR.

**0. UNIVERSALITY.** BOUND_TO_SPECIFIC_SIGN: CLASS (rare / deprecated / substrate-bound format controls) · AFTER_USE_RESIDUE: FORBIDDEN · SIGN_DATA_IS_SESSION_ONLY: YES

**1. COMMON_CONVEYOR_DISCIPLINE.** v0_3 · RUN_CARD_REQUIRED_BEFORE_LOCK: YES · MODEL_FAMILY_DIVERSITY_REQUIRED: YES · ADVERSARIAL_EVIDENCE_REQUIRED: YES · MUTATION_CHECK_REQUIRED: YES · LIMITATION_STATEMENT_REQUIRED: YES. TRACKER: WORKING_DRAFT YES; PREFLIGHT PENDING; CONVEYOR_REVIEW PENDING; WORKINGLY_CLOSED NO.

**2. META.** ZONE: ZONE_1. WHY_THIS_SIGN_MATTERS: a defender who marks every format/default-ignorable codepoint HIGH drowns in false alarms and loses the signal on the codepoints that actually carry attacks. These members are the test of that discipline: U+180E (MONGOLIAN VOWEL SEPARATOR) drifted in and out of the default-ignorable set across Unicode versions and is a classic gray-zone; U+206A–U+206F are DEPRECATED format controls (symmetric-swap, Arabic-shaping, digit-shape) with no modern text use; U+1BCA0–U+1BCA3 are meaningful only inside Duployan shorthand; U+1D173–U+1D17A only inside musical notation (Unicode UAX #44; the deprecated 206x block; the Duployan and Musical Symbols blocks). So the class is watched, not alarmed, until context makes it a vector. INTERACTS_WITH: INVISIBLE_CLASS / METACHAR_CLASS (escalation borrows their hostile-context tests), CANONICALIZATION_PRE_PASS (a control can arrive entity/percent-encoded and must be decoded first), the ERG axis (recurrence can promote a witness).

**3. REQUIRED_GENERAL_GUARDS.** RAW_SIGN_INPUT_STATUS: DATA_ONLY · NO_EXECUTION_FROM_SIGN: YES · NO_TRUST_FROM_SIGN: YES · DECODE_BEFORE_TRUST: YES · JUDGE_IN_CONTEXT_NOT_ON_PRESENCE: YES · NEVER_BLIND_STRIP: YES · DEFAULT_POSTURE_IS_WITNESS: YES (severity spent only on real vectors).

**4. SIGN IDENTITY — LAYER_A (LOCK: PERMANENT).** BASE_MODE: DATA_ONLY_MONITORED · BASE_MODE_FORMULA: PRESENT_IN_SET ≠ IN_HIGH_CLASS ; OFTEN_ABUSED ≠ AUTO_HIGH ; SEVERITY = SIGN + REAL_VECTOR.

| Codepoint(s) | Name | Priority | Attack mechanism (only in hostile context) | Legitimate substrate (do NOT blind-strip) |
|---|---|---|---|---|
| U+180E | MONGOLIAN VOWEL SEPARATOR (MVS) | WITNESS | word/token split when abused as a zero-width | Mongolian text (historical / gray-zone) |
| U+206A–U+206F | INHIBIT/ACTIVATE SYMMETRIC SWAPPING, ARABIC FORM SHAPING, NATIONAL/NOMINAL DIGIT SHAPES | WITNESS | deprecated controls repurposed as hidden markers | none current (deprecated) |
| U+1BCA0–U+1BCA3 | SHORTHAND FORMAT (Duployan) | WITNESS | out-of-substrate insertion | Duployan shorthand rendering |
| U+1D173–U+1D17A | MUSICAL SYMBOL BEGIN/END BEAM/TIE/SLUR/PHRASE | WITNESS | out-of-substrate insertion | musical notation rendering |

WHAT_THIS_SIGN_IS_NOT: (1) NOT_HIGH_BY_MEMBERSHIP — being in this set is not being in the HIGH class; (2) NOT_AUTO_STRIPPABLE — a music/shorthand control carries real structure in its substrate; (3) NOT_FINAL_SURFACE — may arrive entity/percent-encoded and must be decoded first.
BASE_FORMULAS: PRESENT ≠ HIGH ; IN_LEGIT_SUBSTRATE = OK ; SUBSTRATE_LESS + HOSTILE_CONTEXT = ALARM ; OTHERWISE = WITNESS.

**5. SEMANTIC_EPOCH_TRACKER (LOCK: REVIEWABLE).** EPOCH_TRACKER: U+180E is the textbook case — its default-ignorable status was added, removed, and revisited across Unicode versions, so its risk read is version-dependent; the deprecated 206x controls are "dormant" but still ingested by many stacks. NOTE: DORMANT_OR_DEPRECATED ≠ INACTIVE_RISK (a deprecated control is a perfect hidden marker precisely because tooling ignores it).

**6. EFFECT_FIELDS — LAYER_C (LOCK: SESSION).** authority / trust / verification / proof / execution / permission / status / role_assignment / runtime / existence effect: all NONE. EFFECT_FIELDS_ALL_NONE: YES · CLOSED_SCHEMA: YES.

**7. SAFE / RISK / GUARDS — LAYER_B (LOCK: REVIEWABLE).**
Three tiers, restraint-first:
- ALARM (conclusive): a SUBSTRATE-LESS monitored control (MVS, deprecated 206x) in a hostile context — splitting a word/token (`admin‹MVS›istrator`, `user‹NDS›name`), or directly against a metacharacter (`value‹ISS›= admin`).
- OK (clean, "in-substrate" vouch): every monitored control sits inside its own legitimate substrate — a musical control among Musical Symbols, a shorthand control among Duployan letters.
- WATCH (witness — the DEFAULT for this class): a substrate-less monitored control is present but not in a hostile context (`greeting ‹MVS› text`, `digits ‹NDS› here`) — observed, logged, held; never auto-stripped, never auto-HIGH.
SAFE_CASES (must stay OK): a musical score using begin/end-beam controls; Duployan shorthand using its format letters; plain text with none of these.
RISK_CASES: `admin‹MVS›istrator` ALARM; `user‹NDS›name = root` ALARM; `value‹ISS›= admin` ALARM; a lone MVS/deprecated control in prose WATCH.
GUARD_PRINCIPLE: observe the whole set, but escalate ONLY on a real vector; in-substrate use vouches OK; the substrate-less members default to WITNESS at WATCH; the doctrine "often used in attacks ≠ belongs in the HIGH class" lives here.

**8. ADVERSARIAL_COVERAGE — RUN_CARD SEED.** MVS / deprecated 206x splitting a word, a domain, a token; the same control against `-`, `=`, `/`, `|`; a musical/shorthand control OUT of its substrate (should leave OK and become WATCH/ALARM); legit music and Duployan runs (must stay OK); every case ALSO delivered entity/percent-encoded (pre-pass path). MODEL_FAMILY_DIVERSITY_REQUIRED: YES.

**9. MUTATION_CHECK.** literal control ↔ `&#N;` ↔ `%XX` byte form; in-substrate vs. out-of-substrate placement; single vs. recurring. INVARIANT: after canonicalization one verdict; an in-substrate case stays OK, a hostile substrate-less case stays ALARM, a lone one stays WITNESS across all forms.

**10. KNOWN_OPEN_QUESTIONS.** Q1: version-aware default-ignorable handling for U+180E (its status changed across Unicode releases). Q2: recurrence promotion — a witness that repeats across a stream (ERG axis) should rise above WATCH, separating a one-off artifact from a deliberate marker. Q3: a fuller substrate model (e.g. a musical control must be inside a well-formed musical run, not merely near one musical symbol) to resist substrate-wrapping evasion.

**11. PATCH_HISTORY.** v0_1 (2026-07-20): first draft of the monitored-format WITNESS-tier CLASS card — restraint-first, escalate-on-vector — paired with `monitored_cards.py`. Not conveyor-run.

**12. LIMITATION_STATEMENT.** (1) WORKING_DRAFT / NOT_CONVEYOR_RUN. (2) The substrate vouch checks for the PRESENCE of substrate characters, not a well-formed substrate run, so a control wrapped in a couple of substrate characters could be vouched (Q3). (3) No recurrence promotion yet — a witness stays WATCH however often it repeats (Q2). (4) U+180E is handled version-agnostically (Q1). (5) Entity/percent-delivered controls are caught only WITH the pre-pass in front.

**13. INTEGRATION_INTERFACE_STATUS.** INTEGRATION_STATUS: PROTOTYPED (raw). RAW_PROTOTYPE: `monitored_cards.py::monitored_cards_reader(text) -> Finding`. HARNESS: `range_monitored.py`. LIVE RESULT (real MSL + invisible + bidi + tag + vs + whitespace as baseline): **hostile-context 0/3 (0%) → 3/3 (100%), legit substrate 3/3 → 3/3, 0 new FP**; the WITNESS tier (`greeting ‹MVS› text`, `digits ‹NDS› here`) is held at WATCH — a live demonstration of "observe all, prioritize the real vectors". REQUIRES for closing: version-aware U+180E (Q1); recurrence promotion (Q2); well-formed substrate model (Q3); pre-pass in front; conveyor review.

> HOW THE RAW PROTOTYPE WORKS: `MSL_MIP_HOME=/path/to/msl_mip python code/range/range_monitored.py` scans hostile-context cases, witness cases and legit substrate runs BEFORE (MSL + all prior invisible axes) and AFTER (+ this monitored axis), printing the before/after verdict per case, the WITNESS tier, and totals.

---

<a name="русский"></a>
## Русский

DRAFT_NOTE (2026-07-20): КЛАССОВАЯ карточка яруса наблюдаемого формата — операционная форма доктрины **НАБЛЮДАТЬ ВСЁ, ПРИОРИТИЗИРОВАТЬ ПО РЕАЛЬНЫМ ВЕКТОРАМ.** Её члены редкие, низковекторные, в основном устаревшие или привязанные-к-подложке форматные контроли. Весь смысл карточки — сдержанность: это **НЕ авто-HIGH**. Поза по умолчанию — WITNESS (WATCH) — увиден, залогирован, удержан, никогда не авто-вырезан — и эскалирует в ALARM только когда наблюдаемый контроль появляется в реально враждебном контексте (разрыв слова/токена или рядом с синтаксическим метасимволом). Контроль внутри своей ЕДИНСТВЕННОЙ легитимной подложки (музыкальный контроль среди музыкальных символов; стенографический контроль среди букв дюплойе) получает вауч OK. Это карточка, что держит контур честным: весь набор наблюдается, но серьёзность тратится только на реальные векторы. WORKING_DRAFT, БЕЗКОНВЕЙЕРНО.

**0. UNIVERSALITY.** BOUND_TO_SPECIFIC_SIGN: CLASS (редкие / устаревшие / привязанные-к-подложке форматные контроли) · AFTER_USE_RESIDUE: FORBIDDEN · SIGN_DATA_IS_SESSION_ONLY: YES

**1. COMMON_CONVEYOR_DISCIPLINE.** v0_3 · RUN_CARD_REQUIRED_BEFORE_LOCK: YES · MODEL_FAMILY_DIVERSITY_REQUIRED: YES · ADVERSARIAL_EVIDENCE_REQUIRED: YES · MUTATION_CHECK_REQUIRED: YES · LIMITATION_STATEMENT_REQUIRED: YES. TRACKER: WORKING_DRAFT YES; PREFLIGHT PENDING; CONVEYOR_REVIEW PENDING; WORKINGLY_CLOSED NO.

**2. META.** ZONE: ZONE_1. WHY_THIS_SIGN_MATTERS: защитник, помечающий каждый форматный/default-ignorable кодпоинт как HIGH, тонет в ложных тревогах и теряет сигнал на кодпоинтах, реально несущих атаки. Эти члены — проверка этой дисциплины: U+180E (MONGOLIAN VOWEL SEPARATOR) входил и выходил из набора default-ignorable между версиями Unicode, классическая серая зона; U+206A–U+206F — УСТАРЕВШИЕ форматные контроли (симметричный своп, арабское формообразование, формы цифр) без современного применения; U+1BCA0–U+1BCA3 осмыслены лишь внутри стенографии дюплойе; U+1D173–U+1D17A лишь внутри музыкальной нотации (Unicode UAX #44; устаревший блок 206x; блоки Duployan и Musical Symbols). Поэтому класс наблюдается, не алармится, пока контекст не сделает его вектором. INTERACTS_WITH: INVISIBLE_CLASS / METACHAR_CLASS (эскалация берёт их тесты враждебного контекста), CANONICALIZATION_PRE_PASS (контроль может прийти entity/percent-кодированным, сперва декод), ось ERG (повтор может повысить свидетеля).

**3. REQUIRED_GENERAL_GUARDS.** RAW_SIGN_INPUT_STATUS: DATA_ONLY · NO_EXECUTION_FROM_SIGN: YES · NO_TRUST_FROM_SIGN: YES · DECODE_BEFORE_TRUST: YES · JUDGE_IN_CONTEXT_NOT_ON_PRESENCE: YES · NEVER_BLIND_STRIP: YES · DEFAULT_POSTURE_IS_WITNESS: YES (серьёзность тратится только на реальные векторы).

**4. SIGN IDENTITY — LAYER_A (LOCK: PERMANENT).** BASE_MODE: DATA_ONLY_MONITORED · BASE_MODE_FORMULA: PRESENT_IN_SET ≠ IN_HIGH_CLASS ; OFTEN_ABUSED ≠ AUTO_HIGH ; SEVERITY = SIGN + REAL_VECTOR.

| Кодпоинт(ы) | Имя | Приоритет | Механизм атаки (лишь во враждебном контексте) | Легит-подложка (НЕ вырезать слепо) |
|---|---|---|---|---|
| U+180E | MONGOLIAN VOWEL SEPARATOR (MVS) | WITNESS | разрыв слова/токена при злоупотреблении как zero-width | монгольский текст (историч. / серая зона) |
| U+206A–U+206F | INHIBIT/ACTIVATE SYMMETRIC SWAPPING, ARABIC FORM SHAPING, NATIONAL/NOMINAL DIGIT SHAPES | WITNESS | устаревшие контроли, перепрофилированные в скрытые маркеры | нет актуального (устарели) |
| U+1BCA0–U+1BCA3 | SHORTHAND FORMAT (дюплойе) | WITNESS | вставка вне подложки | отрисовка стенографии дюплойе |
| U+1D173–U+1D17A | MUSICAL SYMBOL BEGIN/END BEAM/TIE/SLUR/PHRASE | WITNESS | вставка вне подложки | отрисовка музыкальной нотации |

WHAT_THIS_SIGN_IS_NOT: (1) NOT_HIGH_BY_MEMBERSHIP — быть в этом наборе не значит быть в классе HIGH; (2) NOT_AUTO_STRIPPABLE — музыкальный/стенографический контроль несёт настоящую структуру в своей подложке; (3) NOT_FINAL_SURFACE — может прийти entity/percent-кодированным, сперва декод.
BASE_FORMULAS: PRESENT ≠ HIGH ; IN_LEGIT_SUBSTRATE = OK ; SUBSTRATE_LESS + HOSTILE_CONTEXT = ALARM ; ИНАЧЕ = WITNESS.

**5. SEMANTIC_EPOCH_TRACKER (LOCK: REVIEWABLE).** EPOCH_TRACKER: U+180E — учебный случай: его статус default-ignorable добавляли, убирали и пересматривали между версиями Unicode, поэтому его прочтение риска зависит от версии; устаревшие контроли 206x «дремлют», но всё ещё потребляются многими стеками. NOTE: ДРЕМЛЮЩЕЕ_ИЛИ_УСТАРЕВШЕЕ ≠ НЕАКТИВНЫЙ_РИСК (устаревший контроль — идеальный скрытый маркер именно потому, что инструментарий его игнорирует).

**6. EFFECT_FIELDS — LAYER_C (LOCK: SESSION).** authority / trust / verification / proof / execution / permission / status / role_assignment / runtime / existence effect: всё NONE. EFFECT_FIELDS_ALL_NONE: YES · CLOSED_SCHEMA: YES.

**7. SAFE / RISK / GUARDS — LAYER_B (LOCK: REVIEWABLE).**
Три яруса, сдержанность-в-первую-очередь:
- ALARM (conclusive): БЕЗ-ПОДЛОЖНЫЙ наблюдаемый контроль (MVS, устаревшие 206x) во враждебном контексте — разрыв слова/токена (`admin‹MVS›istrator`, `user‹NDS›name`), или вплотную к метасимволу (`value‹ISS›= admin`).
- OK (чистое, вауч «в-подложке»): каждый наблюдаемый контроль сидит внутри своей легит-подложки — музыкальный среди Musical Symbols, стенографический среди букв дюплойе.
- WATCH (свидетель — ПО УМОЛЧАНИЮ для этого класса): без-подложный наблюдаемый контроль присутствует, но не во враждебном контексте (`greeting ‹MVS› text`, `digits ‹NDS› here`) — увиден, залогирован, удержан; никогда не авто-strip, никогда не авто-HIGH.
SAFE_CASES (должны остаться OK): музыкальная партитура с контролями begin/end-beam; стенография дюплойе с её форматными буквами; обычный текст без этих знаков.
RISK_CASES: `admin‹MVS›istrator` ALARM; `user‹NDS›name = root` ALARM; `value‹ISS›= admin` ALARM; одиночный MVS/устаревший контроль в прозе WATCH.
GUARD_PRINCIPLE: наблюдать весь набор, но эскалировать ТОЛЬКО на реальный вектор; использование в подложке вауч OK; без-подложные члены по умолчанию WITNESS на WATCH; доктрина «часто используется в атаках ≠ входит в класс HIGH» живёт здесь.

**8. ADVERSARIAL_COVERAGE — RUN_CARD SEED.** MVS / устаревшие 206x, рвущие слово, домен, токен; тот же контроль против `-`, `=`, `/`, `|`; музыкальный/стенографический контроль ВНЕ подложки (должен покинуть OK и стать WATCH/ALARM); легит музыкальные и дюплойе-прогоны (должны остаться OK); каждый кейс ТАКЖЕ доставлен entity/percent-кодированным (путь pre-pass). MODEL_FAMILY_DIVERSITY_REQUIRED: YES.

**9. MUTATION_CHECK.** литеральный контроль ↔ `&#N;` ↔ байтовая форма `%XX`; размещение в-подложке vs. вне-подложки; одиночный vs. повторяющийся. INVARIANT: после канонизации один вердикт; кейс в-подложке остаётся OK, враждебный без-подложный остаётся ALARM, одиночный остаётся WITNESS во всех формах.

**10. KNOWN_OPEN_QUESTIONS.** Q1: обработка default-ignorable с учётом версии для U+180E (его статус менялся между релизами Unicode). Q2: повышение по повтору — свидетель, повторяющийся по потоку (ось ERG), должен подняться выше WATCH, отделяя одноразовый артефакт от намеренного маркера. Q3: более полная модель подложки (напр. музыкальный контроль должен быть внутри корректного музыкального прогона, а не просто рядом с одним музыкальным символом), чтобы сопротивляться уклонению через обёртывание подложкой.

**11. PATCH_HISTORY.** v0_1 (2026-07-20): первый черновик КЛАССОВОЙ карточки яруса наблюдаемого формата — сдержанность-в-первую-очередь, эскалация-по-вектору — в паре с `monitored_cards.py`. Не прогонялся через конвейер.

**12. LIMITATION_STATEMENT.** (1) WORKING_DRAFT / NOT_CONVEYOR_RUN. (2) Вауч подложки проверяет ПРИСУТСТВИЕ символов подложки, не корректный прогон подложки, поэтому контроль, обёрнутый парой символов подложки, мог бы получить вауч (Q3). (3) Повышения по повтору пока нет — свидетель остаётся WATCH, сколько бы ни повторялся (Q2). (4) U+180E обрабатывается без учёта версии (Q1). (5) Entity/percent-доставленные контроли ловятся только С pre-pass впереди.

**13. INTEGRATION_INTERFACE_STATUS.** INTEGRATION_STATUS: PROTOTYPED (сырой). RAW_PROTOTYPE: `monitored_cards.py::monitored_cards_reader(text) -> Finding`. HARNESS: `range_monitored.py`. ЖИВОЙ РЕЗУЛЬТАТ (настоящий MSL + invisible + bidi + tag + vs + whitespace как база): **враждебный контекст 0/3 (0%) → 3/3 (100%), легит-подложка 3/3 → 3/3, 0 новых FP**; ярус WITNESS (`greeting ‹MVS› text`, `digits ‹NDS› here`) держится на WATCH — живая демонстрация «наблюдать всё, приоритизировать по реальным векторам». ТРЕБУЕТСЯ для закрытия: U+180E с учётом версии (Q1); повышение по повтору (Q2); модель корректной подложки (Q3); pre-pass впереди; конвейер-ревью.

> КАК РАБОТАЕТ СЫРОЙ ПРОТОТИП: `MSL_MIP_HOME=/path/to/msl_mip python code/range/range_monitored.py` сканирует кейсы враждебного контекста, кейсы-свидетели и легит-прогоны подложки BEFORE (MSL + все прежние невидимые оси) и AFTER (+ эта наблюдаемая ось), печатая вердикт до/после по кейсу, ярус WITNESS и итоги.
