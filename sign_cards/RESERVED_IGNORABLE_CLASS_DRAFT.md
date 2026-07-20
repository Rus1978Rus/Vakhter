PRIVATE AUTHORIAL PROJECT / ЧАСТНЫЙ АВТОРСКИЙ ПРОЕКТ · COMMERCIAL USE PROHIBITED

# SIGN CORE CARD — RESERVED-IGNORABLE / SHOULD-NEVER-APPEAR CLASS (class card, DRAFT)

DOCUMENT_ID: SIGN_CORE_CARD_RESERVED_IGNORABLE_CLASS_GEN3_v0_1 · DOCUMENT_TYPE: SIGN_CORE_CARD · TEMPLATE_LINE: GEN3_v0_3
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
PRIORITY_TIER: P2 (contour closure — blanket rule) · RAW_PROTOTYPE: `code/range/reserved_ignorable_cards.py` · HARNESS: `code/range/range_contour_tail.py`
SCOPE: the reserved (UNASSIGNED, category Cn) but default-ignorable code points — U+2065; U+FFF0–U+FFF8; U+E0000; U+E0002–U+E001F; U+E0080–U+E00FF; U+E01F0–U+E0FFF. This is the blanket that closes the Default_Ignorable contour after the enumerated family cards.

🇬🇧 [English](#english) · 🇷🇺 [Русский](#русский)

---

<a name="english"></a>
## English

DRAFT_NOTE (2026-07-20): the CLASS card that COMPLETES the contour. Unicode reserves whole ranges as default-ignorable-by-DEFAULT: code points that are UNASSIGNED (category Cn) yet, should they ever appear, must render as nothing. That combination — no assigned character AND invisible — is the perfect hostile channel: future-proof, tooling-invisible, and impossible for legitimate text to need, because nothing is assigned there. Every enumerated family has its own card; this one owns everything left — ~3.7k reserved code points — under a single law: **RESERVED + IGNORABLE = SHOULD_NEVER_APPEAR.** Presence is conclusive. WORKING_DRAFT, NON-CONVEYOR.

**0. UNIVERSALITY.** BOUND_TO_SPECIFIC_SIGN: CLASS (reserved default-ignorable code points, category Cn) · AFTER_USE_RESIDUE: FORBIDDEN · SIGN_DATA_IS_SESSION_ONLY: YES

**1. COMMON_CONVEYOR_DISCIPLINE.** v0_3 · RUN_CARD_REQUIRED_BEFORE_LOCK: YES · MODEL_FAMILY_DIVERSITY_REQUIRED: YES · ADVERSARIAL_EVIDENCE_REQUIRED: YES · MUTATION_CHECK_REQUIRED: YES · LIMITATION_STATEMENT_REQUIRED: YES. TRACKER: WORKING_DRAFT YES; PREFLIGHT PENDING; CONVEYOR_REVIEW PENDING; WORKINGLY_CLOSED NO.

**2. META.** ZONE: ZONE_1. WHY_THIS_SIGN_MATTERS: the default-ignorable property was designed so that a code point assigned in a FUTURE Unicode version degrades gracefully on OLD software (renders invisibly instead of as a tofu box). The side effect: a reserved code point in that space is already invisible today, everywhere, with no assigned meaning. An attacker gets a hidden channel that no allowlist can justify and no renderer will show. This card is the reason the contour can be called "complete": the 138 format chars plus the assigned non-Cf families cover what EXISTS; this card covers what is RESERVED-and-hidden, so nothing in the whole default-ignorable space is left uncarded (Unicode UAX #44; PropList Other_Default_Ignorable_Code_Point). INTERACTS_WITH: every enumerated invisible card (this is their complement), CANONICALIZATION_PRE_PASS (a reserved code point can arrive entity/percent-encoded and must be decoded first), the version tracker (a later-assigned code point migrates OUT of this card into its own family).

**3. REQUIRED_GENERAL_GUARDS.** RAW_SIGN_INPUT_STATUS: DATA_ONLY · NO_EXECUTION_FROM_SIGN: YES · NO_TRUST_FROM_SIGN: YES · DECODE_BEFORE_TRUST: YES · JUDGE_IN_CONTEXT_NOT_ON_PRESENCE: N/A (presence IS the anomaly) · NEVER_BLIND_STRIP: YES (reject/flag, do not silently delete — deletion hides evidence).

**4. SIGN IDENTITY — LAYER_A (LOCK: PERMANENT).** BASE_MODE: DATA_ONLY_RESERVED_INVISIBLE · BASE_MODE_FORMULA: UNASSIGNED + IGNORABLE = SHOULD_NEVER_APPEAR ; PRESENCE = ANOMALY.

| Range | Description | Priority | Attack mechanism | Legitimate use |
|---|---|---|---|---|
| U+2065 | reserved default-ignorable (BMP gap) | HIGH | future-proof invisible channel | NONE (unassigned) |
| U+FFF0–U+FFF8 | reserved default-ignorable (specials block) | HIGH | invisible marker / channel | NONE (unassigned) |
| U+E0000 | reserved in the Tags block | HIGH | invisible channel adjacent to TAG smuggling | NONE (unassigned) |
| U+E0002–U+E001F | reserved in the Tags block | HIGH | invisible channel adjacent to TAG smuggling | NONE (unassigned) |
| U+E0080–U+E00FF | reserved in the Tags block | HIGH | invisible channel | NONE (unassigned) |
| U+E01F0–U+E0FFF | reserved after the Variation Selectors Supplement | HIGH | invisible channel | NONE (unassigned) |

WHAT_THIS_SIGN_IS_NOT: (1) NOT_LEGIT_ANYWHERE — nothing is assigned, so there is no legitimate use to protect; (2) NOT_A_RENDERING_ARTIFACT — default-ignorable means it is deliberately hidden, not accidentally so; (3) NOT_FINAL_SURFACE — may arrive entity/percent-encoded and must be decoded first; (4) NOT_PERMANENT_TRUTH — the reserved set is version-dependent (see LIMITATION / EPOCH).
BASE_FORMULAS: RESERVED ∧ IGNORABLE ⇒ ANOMALY ; PRESENCE ⇒ ALARM ; NO_CONTEXT_EXCUSE.

**5. SEMANTIC_EPOCH_TRACKER (LOCK: REVIEWABLE).** EPOCH_TRACKER: this card is INTRINSICALLY version-bound — its whole set is "not yet assigned". When a future Unicode version assigns one of these code points, that code point graduates to its own family card and must be REMOVED here. So the card carries an explicit Unicode-version stamp and a re-check obligation. NOTE: RESERVED_TODAY ≠ RESERVED_FOREVER.

**6. EFFECT_FIELDS — LAYER_C (LOCK: SESSION).** authority / trust / verification / proof / execution / permission / status / role_assignment / runtime / existence effect: all NONE. EFFECT_FIELDS_ALL_NONE: YES · CLOSED_SCHEMA: YES.

**7. SAFE / RISK / GUARDS — LAYER_B (LOCK: REVIEWABLE).**
Essentially one-way — there is no OK-with-presence and no legit context, because the code points are unassigned:
- ALARM (conclusive): any code point in the reserved default-ignorable set is present AND still category Cn (the prototype double-checks Cn so a newly-assigned code point is not mis-flagged here).
- OK (clean): none present.
SAFE_CASES (must stay OK): any text with no reserved default-ignorable code points — ordinary content, including every legitimate invisible from the other cards.
RISK_CASES: `value‹U+2065›here` ALARM; `hello‹U+E0080›world` ALARM; a reserved code point anywhere ALARM.
GUARD_PRINCIPLE: presence alone is conclusive because there is no assigned character to be legitimate; verify category Cn to stay correct across Unicode versions; reject/flag for review, never silently delete (deletion destroys the evidence of a hidden channel).

**8. ADVERSARIAL_COVERAGE — RUN_CARD SEED.** a reserved code point from each range; a reserved code point adjacent to a real TAG smuggle (both must fire); a reserved code point delivered entity/percent-encoded (pre-pass path); a control that a LATER Unicode assigns (must NOT stay flagged here once assigned — the Cn check). MODEL_FAMILY_DIVERSITY_REQUIRED: YES.

**9. MUTATION_CHECK.** literal reserved code point ↔ `&#N;` ↔ `%XX` byte form; one range vs. another; single vs. run. INVARIANT: after canonicalization one verdict; presence stays ALARM across all forms; a since-assigned code point drops OUT (Cn check).

**10. KNOWN_OPEN_QUESTIONS.** Q1: automatic sync with the current Unicode version's assignment table so a newly-assigned code point migrates to its family card without manual edits. Q2: whether the noncharacter code points (e.g. U+FFFE/U+FFFF and the plane-end noncharacters) belong here or in a sibling NONCHARACTER card. Q3: telemetry — a reserved-ignorable hit is a strong indicator of a deliberate hidden channel and could be weighted heavily in an aggregate risk score.

**11. PATCH_HISTORY.** v0_1 (2026-07-20): first draft of the reserved-ignorable CLASS card — the blanket that closes the Default_Ignorable contour — paired with `reserved_ignorable_cards.py`. Not conveyor-run.

**12. LIMITATION_STATEMENT.** (1) WORKING_DRAFT / NOT_CONVEYOR_RUN. (2) The reserved set is stamped to the Unicode version this draft was written for; it MUST be re-derived per Unicode release (Q1). (3) Noncharacters are out of scope here (Q2). (4) Entity/percent-delivered reserved code points are caught only WITH the pre-pass in front. (5) The prototype's Cn double-check depends on the host Python's Unicode database version, which may lag the current standard.

**13. INTEGRATION_INTERFACE_STATUS.** INTEGRATION_STATUS: PROTOTYPED (raw). RAW_PROTOTYPE: `reserved_ignorable_cards.py::reserved_ignorable_cards_reader(text) -> Finding`. HARNESS: `range_contour_tail.py`. LIVE RESULT (real MSL + all 6 invisible axes as baseline, shared with the other two tail cards): **tail threats 0/6 → 6/6, legit in-script 4/4 kept, 0 new FP** — reserved U+2065 and U+E0080 move to ALARM while ordinary content stays OK. REQUIRES for closing: version auto-sync (Q1); noncharacter sibling decision (Q2); pre-pass in front; conveyor review.

> HOW THE RAW PROTOTYPE WORKS: `MSL_MIP_HOME=/path/to/msl_mip python code/range/range_contour_tail.py` runs this card with the other two tail cards, scanning reserved-code-point cases and ordinary content BEFORE (MSL + all invisible axes) and AFTER (+ the tail), printing the before/after verdict per case plus totals; the closing line confirms 138 format chars + this tail = the full DI set.

---

<a name="русский"></a>
## Русский

DRAFT_NOTE (2026-07-20): КЛАССОВАЯ карточка, что ЗАВЕРШАЕТ контур. Unicode резервирует целые диапазоны как default-ignorable-по-УМОЛЧАНИЮ: кодпоинты, которые НЕ НАЗНАЧЕНЫ (категория Cn), но, появись они, должны рисоваться в ничто. Эта комбинация — нет назначенного знака И невидим — идеальный враждебный канал: защищённый-на-будущее, невидимый для инструментов и невозможный для легит-текста, ведь там ничего не назначено. У каждого перечислимого семейства своя карточка; эта владеет всем остальным — ~3.7k зарезервированных кодпоинтов — под единым законом: **RESERVED + IGNORABLE = НИКОГДА_НЕ_ДОЛЖЕН_ПОЯВЛЯТЬСЯ.** Присутствие conclusive. WORKING_DRAFT, БЕЗКОНВЕЙЕРНО.

**0. UNIVERSALITY.** BOUND_TO_SPECIFIC_SIGN: CLASS (зарезервированные default-ignorable кодпоинты, категория Cn) · AFTER_USE_RESIDUE: FORBIDDEN · SIGN_DATA_IS_SESSION_ONLY: YES

**1. COMMON_CONVEYOR_DISCIPLINE.** v0_3 · RUN_CARD_REQUIRED_BEFORE_LOCK: YES · MODEL_FAMILY_DIVERSITY_REQUIRED: YES · ADVERSARIAL_EVIDENCE_REQUIRED: YES · MUTATION_CHECK_REQUIRED: YES · LIMITATION_STATEMENT_REQUIRED: YES. TRACKER: WORKING_DRAFT YES; PREFLIGHT PENDING; CONVEYOR_REVIEW PENDING; WORKINGLY_CLOSED NO.

**2. META.** ZONE: ZONE_1. WHY_THIS_SIGN_MATTERS: свойство default-ignorable создали, чтобы кодпоинт, назначенный в БУДУЩЕЙ версии Unicode, деградировал изящно на СТАРОМ софте (рисовался невидимо, а не как «тофу»-квадрат). Побочный эффект: зарезервированный кодпоинт в этом пространстве уже сегодня невидим, везде, без назначенного смысла. Атакующий получает скрытый канал, который ни один allowlist не оправдает и ни один отрисовщик не покажет. Эта карточка — причина, почему контур можно назвать «полным»: 138 форматных знаков плюс назначенные не-Cf семейства покрывают то, что СУЩЕСТВУЕТ; эта карточка покрывает то, что ЗАРЕЗЕРВИРОВАНО-и-скрыто, так что ничего во всём default-ignorable пространстве не остаётся без карточки (Unicode UAX #44; PropList Other_Default_Ignorable_Code_Point). INTERACTS_WITH: каждая перечислимая невидимая карточка (это их дополнение), CANONICALIZATION_PRE_PASS (зарезервированный кодпоинт может прийти entity/percent-кодированным, сперва декод), трекер версий (позднее-назначенный кодпоинт мигрирует ИЗ этой карточки в своё семейство).

**3. REQUIRED_GENERAL_GUARDS.** RAW_SIGN_INPUT_STATUS: DATA_ONLY · NO_EXECUTION_FROM_SIGN: YES · NO_TRUST_FROM_SIGN: YES · DECODE_BEFORE_TRUST: YES · JUDGE_IN_CONTEXT_NOT_ON_PRESENCE: N/A (присутствие И ЕСТЬ аномалия) · NEVER_BLIND_STRIP: YES (отклонить/флагать, не удалять тихо — удаление прячет улику).

**4. SIGN IDENTITY — LAYER_A (LOCK: PERMANENT).** BASE_MODE: DATA_ONLY_RESERVED_INVISIBLE · BASE_MODE_FORMULA: UNASSIGNED + IGNORABLE = НИКОГДА_НЕ_ДОЛЖЕН_ПОЯВЛЯТЬСЯ ; PRESENCE = ANOMALY.

| Диапазон | Описание | Приоритет | Механизм атаки | Легит-применение |
|---|---|---|---|---|
| U+2065 | зарезервирован default-ignorable (пробел BMP) | ВЫСОКИЙ | защищённый-на-будущее невидимый канал | НЕТ (не назначен) |
| U+FFF0–U+FFF8 | зарезервированы default-ignorable (блок Specials) | ВЫСОКИЙ | невидимый маркер / канал | НЕТ (не назначены) |
| U+E0000 | зарезервирован в блоке Tags | ВЫСОКИЙ | невидимый канал рядом с TAG-контрабандой | НЕТ (не назначен) |
| U+E0002–U+E001F | зарезервированы в блоке Tags | ВЫСОКИЙ | невидимый канал рядом с TAG-контрабандой | НЕТ (не назначены) |
| U+E0080–U+E00FF | зарезервированы в блоке Tags | ВЫСОКИЙ | невидимый канал | НЕТ (не назначены) |
| U+E01F0–U+E0FFF | зарезервированы после Variation Selectors Supplement | ВЫСОКИЙ | невидимый канал | НЕТ (не назначены) |

WHAT_THIS_SIGN_IS_NOT: (1) NOT_LEGIT_ANYWHERE — ничего не назначено, значит нет легит-применения для защиты; (2) NOT_A_RENDERING_ARTIFACT — default-ignorable значит намеренно скрыт, не случайно; (3) NOT_FINAL_SURFACE — может прийти entity/percent-кодированным, сперва декод; (4) NOT_PERMANENT_TRUTH — зарезервированный набор зависит от версии (см. LIMITATION / EPOCH).
BASE_FORMULAS: RESERVED ∧ IGNORABLE ⇒ ANOMALY ; PRESENCE ⇒ ALARM ; НЕТ_КОНТЕКСТНОГО_ОПРАВДАНИЯ.

**5. SEMANTIC_EPOCH_TRACKER (LOCK: REVIEWABLE).** EPOCH_TRACKER: эта карточка ВНУТРЕННЕ привязана к версии — весь её набор это «ещё не назначено». Когда будущая версия Unicode назначит один из этих кодпоинтов, тот выпускается в свою семейную карточку и должен быть УБРАН отсюда. Поэтому карточка несёт явный штамп версии Unicode и обязанность перепроверки. NOTE: RESERVED_СЕГОДНЯ ≠ RESERVED_НАВСЕГДА.

**6. EFFECT_FIELDS — LAYER_C (LOCK: SESSION).** authority / trust / verification / proof / execution / permission / status / role_assignment / runtime / existence effect: всё NONE. EFFECT_FIELDS_ALL_NONE: YES · CLOSED_SCHEMA: YES.

**7. SAFE / RISK / GUARDS — LAYER_B (LOCK: REVIEWABLE).**
По сути односторонне — нет OK-с-присутствием и нет легит-контекста, ведь кодпоинты не назначены:
- ALARM (conclusive): любой кодпоинт из зарезервированного default-ignorable набора присутствует И всё ещё категории Cn (прототип перепроверяет Cn, чтобы новоназначенный кодпоинт не был ложно флагнут здесь).
- OK (чистое): ничего не присутствует.
SAFE_CASES (должны остаться OK): любой текст без зарезервированных default-ignorable кодпоинтов — обычный контент, включая каждую легит-невидимку из других карточек.
RISK_CASES: `value‹U+2065›here` ALARM; `hello‹U+E0080›world` ALARM; зарезервированный кодпоинт где угодно ALARM.
GUARD_PRINCIPLE: одно присутствие conclusive, ведь нет назначенного знака, чтобы быть легитимным; проверять категорию Cn для корректности между версиями Unicode; отклонить/флагать на ревью, никогда не удалять тихо (удаление уничтожает улику скрытого канала).

**8. ADVERSARIAL_COVERAGE — RUN_CARD SEED.** зарезервированный кодпоинт из каждого диапазона; зарезервированный кодпоинт рядом с настоящей TAG-контрабандой (оба должны сработать); зарезервированный кодпоинт, доставленный entity/percent-кодированным (путь pre-pass); контроль, который ПОЗЖЕ назначит Unicode (не должен оставаться флагнутым здесь после назначения — проверка Cn). MODEL_FAMILY_DIVERSITY_REQUIRED: YES.

**9. MUTATION_CHECK.** литеральный зарезервированный кодпоинт ↔ `&#N;` ↔ байтовая форма `%XX`; один диапазон vs. другой; одиночный vs. цепочка. INVARIANT: после канонизации один вердикт; присутствие остаётся ALARM во всех формах; с-тех-пор-назначенный кодпоинт выпадает (проверка Cn).

**10. KNOWN_OPEN_QUESTIONS.** Q1: автосинхронизация с таблицей назначений текущей версии Unicode, чтобы новоназначенный кодпоинт мигрировал в семейную карточку без ручных правок. Q2: относятся ли noncharacter-кодпоинты (напр. U+FFFE/U+FFFF и noncharacter в концах плоскостей) сюда или в родственную карточку NONCHARACTER. Q3: телеметрия — попадание reserved-ignorable это сильный индикатор намеренного скрытого канала и может получать большой вес в агрегатной оценке риска.

**11. PATCH_HISTORY.** v0_1 (2026-07-20): первый черновик reserved-ignorable КЛАССОВОЙ карточки — бланкет, что закрывает Default_Ignorable контур — в паре с `reserved_ignorable_cards.py`. Не прогонялся через конвейер.

**12. LIMITATION_STATEMENT.** (1) WORKING_DRAFT / NOT_CONVEYOR_RUN. (2) Зарезервированный набор проштампован версией Unicode, под которую написан черновик; он ДОЛЖЕН пере-выводиться на каждый релиз Unicode (Q1). (3) Noncharacters вне области здесь (Q2). (4) Entity/percent-доставленные зарезервированные кодпоинты ловятся только С pre-pass впереди. (5) Проверка Cn прототипа зависит от версии базы Unicode в хост-Python, которая может отставать от текущего стандарта.

**13. INTEGRATION_INTERFACE_STATUS.** INTEGRATION_STATUS: PROTOTYPED (сырой). RAW_PROTOTYPE: `reserved_ignorable_cards.py::reserved_ignorable_cards_reader(text) -> Finding`. HARNESS: `range_contour_tail.py`. ЖИВОЙ РЕЗУЛЬТАТ (настоящий MSL + все 6 невидимых осей как база, общая с двумя другими хвостовыми карточками): **хвостовые угрозы 0/6 → 6/6, легит в-скрипте 4/4, 0 новых FP** — зарезервированные U+2065 и U+E0080 переходят в ALARM, а обычный контент остаётся OK. ТРЕБУЕТСЯ для закрытия: автосинк версии (Q1); решение по родственной noncharacter (Q2); pre-pass впереди; конвейер-ревью.

> КАК РАБОТАЕТ СЫРОЙ ПРОТОТИП: `MSL_MIP_HOME=/path/to/msl_mip python code/range/range_contour_tail.py` прогоняет эту карточку с двумя другими хвостовыми, сканируя кейсы зарезервированных кодпоинтов и обычный контент BEFORE (MSL + все невидимые оси) и AFTER (+ хвост), печатая вердикт до/после по кейсу и итоги; закрывающая строка подтверждает 138 форматных знаков + этот хвост = полный DI-набор.
