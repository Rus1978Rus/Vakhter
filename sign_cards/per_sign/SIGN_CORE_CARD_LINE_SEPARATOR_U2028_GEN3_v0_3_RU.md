PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_LINE_SEPARATOR_U2028_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
TRANSLATION_NOTE: Русский оригинал (авторитетный). Английское зеркало — SIGN_CORE_CARD_LINE_SEPARATOR_U2028_GEN3_v0_3_EN. Кодпойнты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_LINE_SEPARATOR_U2028_GEN3_v0_3_RU
CODEPOINT: U+2028
VISIBLE_FORM: ⟨LSEP⟩
UNICODE_NAME: LINE SEPARATOR
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: разделитель строк / перенос строки, который не LF и не CR (расхождение парсеров, разрыв JS-литерала)
CATEGORY_ROADMAP: LLM (invisible line-break injection) · PHAGO: — (маскировка строковой структуры)
GLYPH_NOTE: VISIBLE_FORM использует маркер ⟨LSEP⟩; сам знак (U+2028) — Line Separator (Zl) и НИКОГДА не пишется буквально — буквальный U+2028 был бы трактован как новая строка Unicode-осведомлёнными инструментами и мог бы испортить блочный разбор этого документа. Примеры используют ⟨LSEP⟩/%E2%80%A8, но не байт.

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
VISIBLE_FORM: ⟨LSEP⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: LSEP_FORM ≠ EFFECT
SIGN_CATEGORY:
  - Unicode-терминатор строки (категория Zl), начинающий новую строку для Unicode-осведомлённого кода
  - легитимный перенос строки в Unicode-тексте (альтернатива LF)
  - это НЕ U+000A (LF) и не U+000D (CR); парсер только-LF/CR не трактует его как перенос
  - (при злоупотреблении) почти-невидимый перенос, который парсер только-\n упускает → десинхрон счёта строк / логов / записей, и исторически разрыв строкового литерала JavaScript

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_NEWLINE_LF — это перенос строки, но ДРУГОЙ кодпойнт, чем LF (U+000A)
  2. NOT_SEEN_BY_EVERY_PARSER — сплиттер только-LF/CR не разбивает по U+2028; Unicode splitlines() разбивает → расхождение
  3. NOT_VISIBLE — обычно отрисовывается как ничто или маленький зазор, так что человек может не заметить новой строки
  4. NOT_PSEP — U+2028 это разделитель СТРОК (Zl); U+2029 — разделитель АБЗАЦЕВ (Zp); обработка одного не есть обработка другого
  5. NOT_ENCODED_SAFE — «%E2%80%A8» может быть декодирован обратно в U+2028 позже
  6. NOT_AUTHORITY — он не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сам по себе он ничего не исполняет; он обманывает строковую логику
  8. NOT_TRUST_SIGNAL — он не повышает доверие
  9. NOT_JS_STRING_SAFE — исторически (до ES2019) сырой U+2028 был недопустим в строковом литерале JavaScript, ломая JSON, встроенный в <script>
  10. NOT_SANITIZED_PROOF — присутствие символа не означает, что ввод санирован
  11. NOT_SINGLE_LINE_PROOF — значение, которое «выглядит как одна строка», может содержать U+2028, разбивающий его далее

BASE_FORMULAS:
  LSEP_FORM ≠ EFFECT
  LSEP_FORM ≠ NEWLINE_LF_PROOF
  LSEP_FORM ≠ SEEN_BY_EVERY_PARSER_PROOF
  LSEP_FORM ≠ VISIBLE_PROOF
  LSEP_FORM ≠ PSEP_EQUIVALENCE_PROOF
  LSEP_FORM ≠ ENCODED_SAFETY_PROOF
  LSEP_FORM ≠ AUTHORITY
  LSEP_FORM ≠ EXECUTION_TRIGGER
  LSEP_FORM ≠ JS_STRING_SAFE_PROOF
  LSEP_FORM ≠ SANITIZED_PROOF
  LSEP_FORM ≠ SINGLE_LINE_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: LSEP (ZONE_1) имеет параллельные функции (легитимный Unicode-перенос строки vs. инъекция через расхождение парсеров), сосуществующие без культурной прецессии. Полисемия стабильного разделителя.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: терминатор строки эпохи Unicode без жестового предшественника; злоупотребление через десинхрон парсеров и инъекцию в логи надстроено цифровой эпохой параллельно с легитимным использованием переноса строки.

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
    INPUT: "LSEP is U+2028 in Unicode"
    CONTEXT: именование символа в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: LSEP_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "a line separator starts a new line in Unicode text"
    CONTEXT: описание легитимной функции в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: LSEP_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <LSEP> here"
    CONTEXT: документационный маркер, не байт
    EXPECTED: INFO
    RISK: NONE
    GUARD: LSEP_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "it is a different codepoint from LF"
    CONTEXT: отличие от U+000A в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: LSEP_FORM ≠ NEWLINE_LF_PROOF
  SAFE_CASE_005:
    INPUT: "a line separator differs from a paragraph separator"
    CONTEXT: отличие от U+2029 в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: LSEP_FORM ≠ PSEP_EQUIVALENCE_PROOF
  SAFE_CASE_006:
    INPUT: "a Unicode-aware splitlines can normalize it"
    CONTEXT: описание аккуратной обработки в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: LSEP_FORM ≠ SEEN_BY_EVERY_PARSER_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: LOG_INJECTION
    INPUT: "a field value containing a U+2028 written into a log"
    CONTEXT: Unicode-осведомлённый просмотрщик логов показывает поддельную лишнюю строку, которую \n-писатель не задумывал
    RISK: HIGH
    ATTACK: U+2028 инъецирует фальшивую строку лога (поддельная запись), невидимую для LF-only обзора
    GUARD: LSEP_FORM ≠ SINGLE_LINE_PROOF
  RISK_CASE_002:
    NAME: PARSER_LINE_DESYNC
    INPUT: "record<LSEP>second half processed as one line by an LF-only parser"
    CONTEXT: сплиттер только-LF держит одну строку там, где Unicode-сплиттер видит две (или наоборот)
    RISK: HIGH
    ATTACK: проверка и исполнитель расходятся в границах строк → протащенная вторая строка
    GUARD: LSEP_FORM ≠ SEEN_BY_EVERY_PARSER_PROOF
  RISK_CASE_003:
    NAME: JS_STRING_LITERAL_BREAK
    INPUT: "JSON containing a raw U+2028 embedded in a <script> block"
    CONTEXT: движок JS до ES2019 трактует сырой U+2028 как терминатор строки внутри строкового литерала
    RISK: MEDIUM
    ATTACK: сырой разделитель ломает строковый литерал, превращая данные в код (XSS/разрыв разбора)
    GUARD: LSEP_FORM ≠ JS_STRING_SAFE_PROOF
  RISK_CASE_004:
    NAME: ENCODED_LSEP_BYPASS
    INPUT: "value%E2%80%A8tail (with a later decode)"
    CONTEXT: percent-кодированный U+2028, декодируемый обратно перед использованием
    RISK: HIGH
    ATTACK: «%E2%80%A8» декодируется в U+2028 ПОСЛЕ проверки → скрытый перенос строки возвращается
    GUARD: LSEP_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: SEPARATOR_FAMILY_GAP
    INPUT: "input using U+2029 (PSEP) or U+0085 (NEL) where only U+2028 is filtered"
    CONTEXT: другие Unicode-терминаторы строк/абзацев проскакивают мимо фильтра только-LSEP
    RISK: MEDIUM
    ATTACK: фильтрация только U+2028 упускает U+2029/U+0085 и другие кодпойнты переноса
    GUARD: LSEP_FORM ≠ PSEP_EQUIVALENCE_PROOF
  RISK_CASE_006:
    NAME: INVISIBLE_BREAK_REVIEW_BYPASS
    INPUT: "a value that looks like one line but splits when rendered"
    CONTEXT: U+2028, проходящий однострочный визуальный обзор и разбивающийся далее
    RISK: MEDIUM
    ATTACK: почти-невидимый перенос заставляет многострочную нагрузку читаться как одна безобидная строка
    GUARD: LSEP_FORM ≠ VISIBLE_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨PSEP⟩
    CODEPOINT: U+2029
    NAME: PARAGRAPH SEPARATOR
    RISK: HIGH
    RULE: PARAGRAPH_SEPARATOR ≠ LINE_SEPARATOR (разрыв абзаца (Zp) vs разрыв строки (Zl); фильтр, обрабатывающий один, может упустить другой)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨LF⟩
    CODEPOINT: U+000A
    NAME: LINE FEED
    RISK: HIGH
    RULE: LINE_FEED ≠ LINE_SEPARATOR (ASCII-новая-строка; мир только-LF/CR не трактует U+2028 как перенос)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨NEL⟩
    CODEPOINT: U+0085
    NAME: NEXT LINE
    RISK: MEDIUM
    RULE: NEXT_LINE ≠ LINE_SEPARATOR (ещё один Unicode-терминатор строки, из C1-контролов; другой кодпойнт, похожий эффект)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨CR⟩
    CODEPOINT: U+000D
    NAME: CARRIAGE RETURN
    RISK: MEDIUM
    RULE: CARRIAGE_RETURN ≠ LINE_SEPARATOR (классический CR-конец строки; не U+2028)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨VT⟩
    CODEPOINT: U+000B
    NAME: LINE TABULATION
    RISK: LOW
    RULE: LINE_TABULATION ≠ LINE_SEPARATOR (вертикальная табуляция, которую некоторые парсеры трактуют как перенос; отдельный control)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "it is a newline, so it is LF"
    RESPONSE: LSEP_FORM ≠ NEWLINE_LF_PROOF
    RULE: это перенос строки, но другой кодпойнт, чем U+000A
  CG2:
    TRIGGER: "our parser handles newlines, so it sees this"
    RESPONSE: LSEP_FORM ≠ SEEN_BY_EVERY_PARSER_PROOF
    RULE: сплиттер только-LF/CR не разбивает по U+2028; Unicode-сплиттер разбивает — они расходятся
  CG3:
    TRIGGER: "a human would see the new line"
    RESPONSE: LSEP_FORM ≠ VISIBLE_PROOF
    RULE: обычно отрисовывается как ничто/зазор; обозреватель может пропустить перенос
  CG4:
    TRIGGER: "'%E2%80%A8' is safe forever"
    RESPONSE: LSEP_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в U+2028 перед использованием
  CG5:
    TRIGGER: "we filter U+2028, so all Unicode breaks are handled"
    RESPONSE: LSEP_FORM ≠ PSEP_EQUIVALENCE_PROOF
    RULE: U+2029 (PSEP), U+0085 (NEL) и другие — отдельные кодпойнты переноса
  CG6:
    TRIGGER: "the string looks like one line, so it is one line"
    RESPONSE: LSEP_FORM ≠ SINGLE_LINE_PROOF
    RULE: почти-невидимый U+2028 может разбить его на две строки далее

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "field value with an interior U+2028"
      NAME: LINE_SPLIT_INJECTION
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: внутренний разделитель строк, подделывающий лишнюю строку лога/записи
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "raw U+2028 inside a JS/JSON string"
      NAME: STRING_LITERAL_BREAK
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: сырой разделитель, ломающий строковый литерал до ES2019
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "mixed U+2028 + U+2029 + U+0085"
      NAME: BREAK_FAMILY_MIX
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: несколько кодпойнтов переноса вместе для обхода фильтра только-LSEP
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: не применимо — риск LSEP именно о том, где перенос падает в последовательности.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: U+2028 подделывает строковую/записевую структуру (маскировка строковой структуры), но не имитирует существование верифицированной сущности. Его риски — десинхрон парсера/лога, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена U+2028 на U+2029 (PSEP) / U+0085 (NEL) для смены кодпойнта переноса / обхода фильтра только-LSEP
  A2: percent-кодирование "%E2%80%A8" для проскока мимо сканера сырых байтов
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: инъекция в лог (U+2028 подделывает лишнюю строку лога)
  B2: десинхрон строк парсера (только-LF vs Unicode-сплиттер расходятся)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "raw U+2028 inside a JS/JSON string" (SC2) — разрыв строкового литерала
  C2: "mixed U+2028 + U+2029 + U+0085" (SC3) — смесь семейства переносов
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: U+2028 подан как «просто новая строка», чтобы его трактовали как LF и нормализовали неверно (или не нормализовали)
  D2: "%E2%80%A8" как «безопасный» кодированный текст с последующим декодом
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: подделанная структура записи/строки через невидимый перенос
  E2: N/A — вектор: фильтр только-LSEP, упускающий более широкое семейство переносов строк/абзацев
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: разделитель строк то же самое, что LF
  EXPECTED: FAIL_NEWLINE_LF_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: каждый newline-осведомлённый парсер видит U+2028
  EXPECTED: FAIL_SEEN_BY_EVERY_PARSER_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: обозреватель всегда видит новую строку
  EXPECTED: FAIL_VISIBLE_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%E2%80%A8" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: фильтрация U+2028 обрабатывает все Unicode-переносы
  EXPECTED: FAIL_PSEP_EQUIVALENCE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: сырой U+2028 безопасен внутри строкового литерала JS
  EXPECTED: FAIL_JS_STRING_SAFE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как нормализовать всё Unicode-семейство переносов строк/абзацев (U+2028, U+2029, U+0085, U+000B, U+000C …) согласованно до разбиения строк, логирования, встраивания JSON/JS и разбора записей, не ломая легитимные Unicode-переносы строк?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (Unicode-осведомлённый нормализатор строк, применяемый один раз до split, записи в лог, встраивания и разбора; экранировать или отклонять сырые разделители в контекстах JS/JSON — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «U+2028 — перенос строки, но не LF; парсеры только-LF и Unicode-осведомлённые расходятся, и это лишь один из более широкого семейства переносов».
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
