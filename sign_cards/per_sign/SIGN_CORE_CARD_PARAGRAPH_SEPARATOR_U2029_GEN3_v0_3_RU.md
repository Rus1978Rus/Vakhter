PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_PARAGRAPH_SEPARATOR_U2029_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
TRANSLATION_NOTE: Русский оригинал (авторитетный). Английское зеркало — SIGN_CORE_CARD_PARAGRAPH_SEPARATOR_U2029_GEN3_v0_3_EN. Кодпойнты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

============================================================
0. UNIVERSALITY
============================================================
BOUND_TO_SPECIFIC_SIGN: YES
AFTER_USE_RESIDUE: FORBIDDEN
SIGN_DATA_IS_SESSION_ONLY: YES

============================================================
1. COMMON_CONVEYOR_DISCIPLINE
============================================================
CONVEYOR_DISCIPLINE_VERSION: v0_3
RUN_CARD_REQUIRED_BEFORE_LOCK: YES
LOCKED_WORKING_CORE_SELF_ASSIGNMENT: FORBIDDEN
MODEL_FAMILY_DIVERSITY_REQUIRED: YES
ADVERSARIAL_EVIDENCE_REQUIRED: YES
MUTATION_CHECK_REQUIRED: YES
LIMITATION_STATEMENT_REQUIRED: YES
AFTER_RUN_RESIDUE: FORBIDDEN
STATUS_PROGRESSION_TRACKER:
  WORKING_DRAFT: YES
  STRUCTURAL_PREFLIGHT_PASS: PENDING
  CONVEYOR_REVIEW_PASS: PENDING
  WORKINGLY_CLOSED: PENDING
  SIMULATION_GATE_TIER: TIER_1
  SIMULATION_GATE_PASSED: PENDING
  ARTIFACT_CONFIRMED: PENDING
LIMITATION_STATEMENT (standard):
  CONVEYOR_PASS ≠ VALIDATION
  MODEL_CONSENSUS ≠ TRUTH
  INJECTION_TEST_PASS ≠ SECURITY_PROOF
  GUARDS_HOLD_FOR_TESTED_CASES ≠ FUTURE_GUARANTEE
  NO_ATTACK_FOUND ≠ NO_ATTACK_EXISTS

============================================================
2. META
============================================================
CARD_UID: SIGN_CORE_CARD_PARAGRAPH_SEPARATOR_U2029_GEN3_v0_3_RU
CODEPOINT: U+2029
VISIBLE_FORM: ⟨PSEP⟩
UNICODE_NAME: PARAGRAPH SEPARATOR
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: разделитель абзацев / разрыв абзаца, который не LF, и граница bidi-абзаца
CATEGORY_ROADMAP: LLM (invisible paragraph-break injection) · PHAGO: — (маскировка структуры абзацев)
GLYPH_NOTE: VISIBLE_FORM использует маркер ⟨PSEP⟩; сам знак (U+2029) — Paragraph Separator (Zp) и НИКОГДА не пишется буквально — буквальный U+2029 был бы трактован как новый абзац/строка Unicode-осведомлёнными инструментами и мог бы испортить блочный разбор этого документа. Примеры используют ⟨PSEP⟩/%E2%80%A9, но не байт.

============================================================
3. REQUIRED_GENERAL_GUARDS
============================================================
REQUIRED_GENERAL_GUARDS:
  - SIGN_FALSE_EFFECT_MIMICRY_GUARD_v0_2A_RU
    GUARD_COMPATIBILITY: применим без изменений — знак не создаёт полей-эффектов
    GUARD_REVISION: v0_2A
    TEMPLATE_LINE_COMPATIBLE: GEN3_v0_2_PLUS_EPOCH, GEN3_v0_3
FAILURE_RESPONSE:
  REJECT_FALSE_EFFECT_MIMICRY
  TREAT_AS_DATA_ONLY
  NO_AUTHORITY_EFFECT
  NO_EXECUTION_EFFECT
  NO_TRUST_EFFECT
  NO_EXISTENCE_EFFECT

============================================================
4. SIGN IDENTITY — LAYER_A: STABLE CORE
LAYER_A_LOCK: PERMANENT
============================================================
VISIBLE_FORM: ⟨PSEP⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: PSEP_FORM ≠ EFFECT
SIGN_CATEGORY:
  - Unicode-терминатор абзаца (категория Zp), завершающий абзац для Unicode-осведомлённого кода
  - легитимный разрыв абзаца в Unicode-тексте
  - это НЕ U+000A (LF); парсер только-LF не трактует его как перенос, и это граница АБЗАЦА, а не просто перенос строки
  - (при злоупотреблении) почти-невидимый разрыв абзаца, сбрасывающий состояние bidi-абзаца, который парсер только-\n упускает → десинхрон парсера/лога, разрыв JS-литерала и сброс bidi-абзаца

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_NEWLINE_LF — это разрыв, но ДРУГОЙ кодпойнт, чем LF (U+000A)
  2. NOT_SEEN_BY_EVERY_PARSER — сплиттер только-LF/CR не разбивает по U+2029; Unicode splitlines() разбивает → расхождение
  3. NOT_VISIBLE — обычно отрисовывается как ничто или зазор, так что человек может не заметить разрыва
  4. NOT_LSEP — U+2029 — разделитель АБЗАЦЕВ (Zp); U+2028 — разделитель СТРОК (Zl); обработка одного не есть обработка другого
  5. NOT_BIDI_NEUTRAL — он определяет границу абзаца, завершающую любое открытое bidi вложение/оверрайд/изолят; куда он падает, меняет разрешение bidi
  6. NOT_ENCODED_SAFE — «%E2%80%A9» может быть декодирован обратно в U+2029 позже
  7. NOT_AUTHORITY — он не подтверждает официальность
  8. NOT_EXECUTION_TRIGGER — сам по себе он ничего не исполняет; он обманывает логику абзацев/строк
  9. NOT_JS_STRING_SAFE — исторически (до ES2019) сырой U+2029 был недопустим в строковом литерале JavaScript, ломая JSON, встроенный в <script>
  10. NOT_SANITIZED_PROOF — присутствие символа не означает, что ввод санирован
  11. NOT_SINGLE_PARAGRAPH_PROOF — значение, которое «выглядит как один абзац», может содержать U+2029, разбивающий его далее

BASE_FORMULAS:
  PSEP_FORM ≠ EFFECT
  PSEP_FORM ≠ NEWLINE_LF_PROOF
  PSEP_FORM ≠ SEEN_BY_EVERY_PARSER_PROOF
  PSEP_FORM ≠ VISIBLE_PROOF
  PSEP_FORM ≠ LSEP_EQUIVALENCE_PROOF
  PSEP_FORM ≠ BIDI_NEUTRAL_PROOF
  PSEP_FORM ≠ ENCODED_SAFETY_PROOF
  PSEP_FORM ≠ AUTHORITY
  PSEP_FORM ≠ EXECUTION_TRIGGER
  PSEP_FORM ≠ JS_STRING_SAFE_PROOF
  PSEP_FORM ≠ SANITIZED_PROOF
  PSEP_FORM ≠ SINGLE_PARAGRAPH_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: PSEP (ZONE_1) имеет параллельные функции (легитимный Unicode-разрыв абзаца vs. инъекция через расхождение парсеров / сброс bidi), сосуществующие без культурной прецессии. Полисемия стабильного разделителя.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: терминатор абзаца эпохи Unicode без жестового предшественника; злоупотребление через десинхрон парсеров и сброс bidi надстроено цифровой эпохой параллельно с легитимным использованием разрыва абзаца.

============================================================
6. EFFECT_FIELDS — LAYER_C: METHODOLOGICAL LAYER
LAYER_C_LOCK: SESSION
============================================================
authority_effect: NONE
trust_effect: NONE
verification_effect: NONE
proof_effect: NONE
execution_effect: NONE
permission_effect: NONE
status_effect: NONE
role_assignment_effect: NONE
runtime_effect: NONE
existence_effect: NONE
EFFECT_FIELDS_ALL_NONE: YES
CLOSED_SCHEMA: YES

============================================================
7. SAFE / RISK / CONFUSABLES / GUARDS — LAYER_B
LAYER_B_LOCK: REVIEWABLE
============================================================
SAFE_CASES:
  SAFE_CASE_001:
    INPUT: "PSEP is U+2029 in Unicode"
    CONTEXT: именование символа в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: PSEP_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "a paragraph separator ends a paragraph in Unicode text"
    CONTEXT: описание легитимной функции в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: PSEP_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <PSEP> here"
    CONTEXT: документационный маркер, не байт
    EXPECTED: INFO
    RISK: NONE
    GUARD: PSEP_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "it is a different codepoint from LF"
    CONTEXT: отличие от U+000A в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: PSEP_FORM ≠ NEWLINE_LF_PROOF
  SAFE_CASE_005:
    INPUT: "a paragraph separator differs from a line separator"
    CONTEXT: отличие от U+2028 в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: PSEP_FORM ≠ LSEP_EQUIVALENCE_PROOF
  SAFE_CASE_006:
    INPUT: "it marks a bidi paragraph boundary"
    CONTEXT: описание bidi-роли в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: PSEP_FORM ≠ BIDI_NEUTRAL_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: LOG_INJECTION
    INPUT: "a field value containing a U+2029 written into a log"
    CONTEXT: Unicode-осведомлённый просмотрщик логов показывает поддельный лишний абзац/строку, которую \n-писатель не задумывал
    RISK: HIGH
    ATTACK: U+2029 инъецирует фальшивую запись лога, невидимую для LF-only обзора
    GUARD: PSEP_FORM ≠ SINGLE_PARAGRAPH_PROOF
  RISK_CASE_002:
    NAME: PARSER_BREAK_DESYNC
    INPUT: "record<PSEP>second half processed as one unit by an LF-only parser"
    CONTEXT: сплиттер только-LF держит одну запись там, где Unicode-сплиттер видит две
    RISK: HIGH
    ATTACK: проверка и исполнитель расходятся в границах → протащенная вторая запись
    GUARD: PSEP_FORM ≠ SEEN_BY_EVERY_PARSER_PROOF
  RISK_CASE_003:
    NAME: BIDI_PARAGRAPH_RESET
    INPUT: "an open bidi override followed by a U+2029"
    CONTEXT: разделитель абзаца, завершающий bidi-абзац, меняя, где кончается оверрайд/изолят
    RISK: MEDIUM
    ATTACK: атакующий использует границу абзаца для контроля протяжённости bidi-разворота (см. карточки оверрайда/изолята)
    GUARD: PSEP_FORM ≠ BIDI_NEUTRAL_PROOF
  RISK_CASE_004:
    NAME: ENCODED_PSEP_BYPASS
    INPUT: "value%E2%80%A9tail (with a later decode)"
    CONTEXT: percent-кодированный U+2029, декодируемый обратно перед использованием
    RISK: HIGH
    ATTACK: «%E2%80%A9» декодируется в U+2029 ПОСЛЕ проверки → скрытый разрыв возвращается
    GUARD: PSEP_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: SEPARATOR_FAMILY_GAP
    INPUT: "input using U+2028 (LSEP) or U+0085 (NEL) where only U+2029 is filtered"
    CONTEXT: другие Unicode-терминаторы строк/абзацев проскакивают мимо фильтра только-PSEP
    RISK: MEDIUM
    ATTACK: фильтрация только U+2029 упускает U+2028/U+0085 и другие кодпойнты переноса
    GUARD: PSEP_FORM ≠ LSEP_EQUIVALENCE_PROOF
  RISK_CASE_006:
    NAME: JS_STRING_LITERAL_BREAK
    INPUT: "JSON containing a raw U+2029 embedded in a <script> block"
    CONTEXT: движок JS до ES2019 трактует сырой U+2029 как терминатор строки внутри строкового литерала
    RISK: MEDIUM
    ATTACK: сырой разделитель ломает строковый литерал, превращая данные в код (XSS/разрыв разбора)
    GUARD: PSEP_FORM ≠ JS_STRING_SAFE_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨LSEP⟩
    CODEPOINT: U+2028
    NAME: LINE SEPARATOR
    RISK: HIGH
    RULE: LINE_SEPARATOR ≠ PARAGRAPH_SEPARATOR (разрыв строки (Zl) vs разрыв абзаца (Zp); фильтр, обрабатывающий один, может упустить другой)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨LF⟩
    CODEPOINT: U+000A
    NAME: LINE FEED
    RISK: HIGH
    RULE: LINE_FEED ≠ PARAGRAPH_SEPARATOR (ASCII-новая-строка; мир только-LF/CR не трактует U+2029 как перенос)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨NEL⟩
    CODEPOINT: U+0085
    NAME: NEXT LINE
    RISK: MEDIUM
    RULE: NEXT_LINE ≠ PARAGRAPH_SEPARATOR (ещё один Unicode-терминатор строки, из C1-контролов; другой кодпойнт, похожий эффект)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨CR⟩
    CODEPOINT: U+000D
    NAME: CARRIAGE RETURN
    RISK: MEDIUM
    RULE: CARRIAGE_RETURN ≠ PARAGRAPH_SEPARATOR (классический CR-конец строки; не U+2029)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨FF⟩
    CODEPOINT: U+000C
    NAME: FORM FEED
    RISK: LOW
    RULE: FORM_FEED ≠ PARAGRAPH_SEPARATOR (control разрыва страницы/секции, который некоторые парсеры трактуют как перенос; отдельный control)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "it is a newline, so it is LF"
    RESPONSE: PSEP_FORM ≠ NEWLINE_LF_PROOF
    RULE: это разрыв, но другой кодпойнт, чем U+000A
  CG2:
    TRIGGER: "our parser handles newlines, so it sees this"
    RESPONSE: PSEP_FORM ≠ SEEN_BY_EVERY_PARSER_PROOF
    RULE: сплиттер только-LF/CR не разбивает по U+2029; Unicode-сплиттер разбивает — они расходятся
  CG3:
    TRIGGER: "a human would see the break"
    RESPONSE: PSEP_FORM ≠ VISIBLE_PROOF
    RULE: обычно отрисовывается как ничто/зазор; обозреватель может пропустить разрыв
  CG4:
    TRIGGER: "line and paragraph separators are the same"
    RESPONSE: PSEP_FORM ≠ LSEP_EQUIVALENCE_PROOF
    RULE: U+2029 (Zp) — граница абзаца; U+2028 (Zl) — граница строки; они различаются
  CG5:
    TRIGGER: "a paragraph break has nothing to do with bidi"
    RESPONSE: PSEP_FORM ≠ BIDI_NEUTRAL_PROOF
    RULE: он завершает bidi-абзац, ограничивая любой открытый оверрайд/вложение/изолят
  CG6:
    TRIGGER: "'%E2%80%A9' is safe forever"
    RESPONSE: PSEP_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в U+2029 перед использованием
  CG7:
    TRIGGER: "the string looks like one paragraph, so it is one"
    RESPONSE: PSEP_FORM ≠ SINGLE_PARAGRAPH_PROOF
    RULE: почти-невидимый U+2029 может разбить его далее

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "field value with an interior U+2029"
      NAME: PARAGRAPH_SPLIT_INJECTION
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: внутренний разделитель абзаца, подделывающий лишний лог/запись
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "open bidi control then U+2029"
      NAME: BIDI_PARAGRAPH_BOUND
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: разделитель абзаца, ограничивающий открытый оверрайд/изолят для контроля протяжённости разворота
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "mixed U+2029 + U+2028 + U+0085"
      NAME: BREAK_FAMILY_MIX
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: несколько кодпойнтов переноса вместе для обхода фильтра только-PSEP
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: не применимо — риск PSEP именно о том, где граница абзаца падает в последовательности.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: U+2029 подделывает абзацную/записевую структуру (маскировка структуры абзацев), но не имитирует существование верифицированной сущности. Его риски — десинхрон парсера/лога и контроль протяжённости bidi, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена U+2029 на U+2028 (LSEP) / U+0085 (NEL) для смены кодпойнта переноса / обхода фильтра только-PSEP
  A2: percent-кодирование "%E2%80%A9" для проскока мимо сканера сырых байтов
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: инъекция в лог (U+2029 подделывает лишнюю запись лога)
  B2: десинхрон разрывов парсера (только-LF vs Unicode-сплиттер расходятся)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "open bidi control then U+2029" (SC2) — граница bidi-абзаца
  C2: "mixed U+2029 + U+2028 + U+0085" (SC3) — смесь семейства переносов
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: U+2029 подан как «просто новая строка», чтобы его трактовали как LF и нормализовали неверно (или не нормализовали)
  D2: "%E2%80%A9" как «безопасный» кодированный текст с последующим декодом
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: подделанная структура записи/абзаца через невидимый разрыв
  E2: N/A — вектор: фильтр только-PSEP, упускающий более широкое семейство переносов строк/абзацев
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: разделитель абзаца то же самое, что LF
  EXPECTED: FAIL_NEWLINE_LF_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: каждый newline-осведомлённый парсер видит U+2029
  EXPECTED: FAIL_SEEN_BY_EVERY_PARSER_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: разделители строк и абзацев взаимозаменяемы
  EXPECTED: FAIL_LSEP_EQUIVALENCE_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%E2%80%A9" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: разрыв абзаца bidi-нейтрален
  EXPECTED: FAIL_BIDI_NEUTRAL_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: сырой U+2029 безопасен внутри строкового литерала JS
  EXPECTED: FAIL_JS_STRING_SAFE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как нормализовать всё Unicode-семейство переносов строк/абзацев (U+2028, U+2029, U+0085, U+000B, U+000C …) согласованно до разбиения, логирования, встраивания JSON/JS и разбора записей, учитывая сброс bidi-абзаца, вызываемый U+2029, не ломая легитимные разрывы абзацев?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (Unicode-осведомлённый нормализатор переносов, применяемый один раз до split, записи в лог, встраивания и разбора; экранировать/отклонять сырые разделители в JS/JSON; учитывать границы bidi-абзацев — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «U+2029 — разрыв абзаца (не LF, не U+2028), который также сбрасывает bidi-абзац; парсеры только-LF и Unicode-осведомлённые расходятся».
ALL_OPEN_QUESTIONS_CLOSED: NO (delegated, non-blocking)

============================================================
11. PATCH_HISTORY
============================================================
PATCH_HISTORY:
  v0_1_PATCH_01: первичное создание (Ruslan Malyavsky, 2026-07-22) — черновик из шаблона GEN3_v0_3 (Vakhter); не конвейер-ран.
PATCHES_APPLIED: 1
PATCHES_VERIFIED: 0/1

============================================================
12. LIMITATION_STATEMENT
============================================================
LIMITATION_STATEMENT:
  THIS_CARD IS A WORKING_DRAFT ARTIFACT (until ARTIFACT_CONFIRMED)
  NOT A FINAL_STANDARD
  NOT A PARSER
  NOT A RUNTIME
  NOT A SECURITY_CERTIFICATE
  NOT_CONVEYOR_RUN (draft for our work; conveyor is a separate project)
  CONVEYOR_PASS ≠ VALIDATION
  RUN_CARD_RESULT ≠ FINAL_STATUS
  WORKINGLY_CLOSED ≠ ARTIFACT_CONFIRMED

============================================================
13. INTEGRATION_INTERFACE_STATUS
============================================================
INTEGRATION_INTERFACE_STATUS:
  STATUS: READY_PENDING_CONCRETE_INTEGRATOR
  ATTACHED_INTEGRATOR_UID: NONE_CURRENTLY_ATTACHED
  ACTIVE_MODULES_COUNT: 0
  RUNTIME_ATTACHMENT: NONE
  PERMANENT_BINDING: NO
  SESSION_ONLY_BINDING: YES
  AFTER_RUN_RESIDUE: FORBIDDEN

============================================================
END_OF_DOCUMENT
