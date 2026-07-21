PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_SEMICOLON_U003B_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: Русский оригинал (authoritative). Английское зеркало — SIGN_CORE_CARD_SEMICOLON_U003B_GEN3_v0_3_EN. Кодпоинты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_SEMICOLON_U003B_GEN3_v0_3_RU
CODEPOINT: U+003B
VISIBLE_FORM: ;
UNICODE_NAME: SEMICOLON
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: точка с запятой / разделитель инструкций
CATEGORY_ROADMAP: INJ (стекинг инструкций shell/SQL) · PHAGO: — (цепочка команд)

============================================================
3. REQUIRED_GENERAL_GUARDS
============================================================
REQUIRED_GENERAL_GUARDS:
  - SIGN_FALSE_EFFECT_MIMICRY_GUARD_v0_2A_RU
    GUARD_COMPATIBILITY: применим без изменений — знак не создаёт effect-полей
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
VISIBLE_FORM: ;
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: SEMICOLON_FORM ≠ EFFECT
SIGN_CATEGORY:
  - разделитель команд shell (cmd1; cmd2)
  - терминатор/стекер инструкций SQL (SELECT …; DROP …)
  - разделитель инструкций в коде (a=1; b=2)
  - пунктуация в тексте (разделение частей предложения)

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_PUNCTUATION_ONLY — ";" не всегда текстовая пунктуация (в shell это цепочка команд)
  2. NOT_SEPARATOR_SAFE — «разделение», которое он делает, может запустить вторую команду
  3. NOT_TERMINATOR_SAFE — завершение одной инструкции SQL позволяет выполнить вторую
  4. NOT_ESCAPED_PROOF — наличие ";" не значит, что он экранирован/закавычен
  5. NOT_ENCODED_SAFE — "%3B" может быть раскодирован обратно в ";" позже
  6. NOT_AUTHORITY — ";" не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сам по себе ничего не исполняет; цепочку делает контекст
  8. NOT_TRUST_SIGNAL — не повышает доверие
  9. NOT_COMMENT_SAFE — ";" — маркер комментария в некоторых диалектах (INI/asm), не нейтрален
  10. NOT_SANITIZED_PROOF — наличие ";" не значит, что ввод санитизирован
  11. NOT_OUTPUT_CONTEXT_PROOF — безопасность зависит от контекста исполнения/разбора

BASE_FORMULAS:
  SEMICOLON_FORM ≠ EFFECT
  SEMICOLON_FORM ≠ PUNCTUATION_ONLY_PROOF
  SEMICOLON_FORM ≠ SEPARATOR_SAFETY_PROOF
  SEMICOLON_FORM ≠ TERMINATOR_SAFETY_PROOF
  SEMICOLON_FORM ≠ ESCAPED_PROOF
  SEMICOLON_FORM ≠ ENCODED_SAFETY_PROOF
  SEMICOLON_FORM ≠ AUTHORITY
  SEMICOLON_FORM ≠ EXECUTION_TRIGGER
  SEMICOLON_FORM ≠ TRUST_SIGNAL
  SEMICOLON_FORM ≠ SANITIZED_PROOF
  SEMICOLON_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: ";" (ZONE_1) имеет параллельные функции (текстовая пунктуация, разделитель shell/SQL/кода), сосуществующие без культурной прецессии. Полисемия стабильного знака.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1
  NOTE: письменный знак пунктуации без жестового предшественника; функции разделителя команд/инструкций надстроены цифровой эпохой параллельно.

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
    INPUT: "I came; I saw; I left"
    CONTEXT: пунктуация между частями предложения
    EXPECTED: INFO
    RISK: NONE
    GUARD: SEMICOLON_FORM ≠ PUNCTUATION_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: "int a = 1; int b = 2;"
    CONTEXT: разделители инструкций в коде (как литеральный текст)
    EXPECTED: INFO
    RISK: NONE
    GUARD: SEMICOLON_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "color: red; font-size: 12px;"
    CONTEXT: объявления CSS
    EXPECTED: INFO
    RISK: NONE
    GUARD: SEMICOLON_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "a;b;c"
    CONTEXT: список данных с разделителем точка-с-запятой
    EXPECTED: INFO
    RISK: NONE
    GUARD: SEMICOLON_FORM ≠ SEPARATOR_SAFETY_PROOF
  SAFE_CASE_005:
    INPUT: "&amp; &lt; &gt;"
    CONTEXT: ";" завершает HTML-сущность
    EXPECTED: INFO
    RISK: NONE
    GUARD: SEMICOLON_FORM ≠ EFFECT
  SAFE_CASE_006:
    INPUT: "key=value; expires=..."
    CONTEXT: разделитель атрибутов cookie
    EXPECTED: INFO
    RISK: NONE
    GUARD: SEMICOLON_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: SHELL_COMMAND_CHAIN
    INPUT: "ping 8.8.8.8; rm -rf /"
    CONTEXT: вторая команда выполняется после первой в shell
    RISK: CRITICAL
    ATTACK: ";" завершает безобидную команду и запускает команду атакующего
    GUARD: SEMICOLON_FORM ≠ SEPARATOR_SAFETY_PROOF
  RISK_CASE_002:
    NAME: SQL_STATEMENT_STACKING
    INPUT: "1; DROP TABLE users; --"
    CONTEXT: стекинг второй инструкции SQL
    RISK: CRITICAL
    ATTACK: ";" завершает запрос и внедряет разрушающую инструкцию
    GUARD: SEMICOLON_FORM ≠ TERMINATOR_SAFETY_PROOF
  RISK_CASE_003:
    NAME: GREEK_QUESTION_MARK_HOMOGLYPH
    INPUT: "cmd; (где ; — греческий ; U+037E)"
    CONTEXT: идентичный по виду греческий вопросительный знак проходит фильтр ";"
    RISK: HIGH
    ATTACK: U+037E отображается как ";" и может свернуться в ";" после проверки фильтра
    GUARD: SEMICOLON_FORM ≠ EFFECT
  RISK_CASE_004:
    NAME: ENCODED_SEMICOLON_BYPASS
    INPUT: "cmd%3B rm -rf ~ (с поздним декодированием)"
    CONTEXT: кодированная ";" декодируется обратно перед исполнением
    RISK: HIGH
    ATTACK: %3B декодируется в ";" ПОСЛЕ проверки → цепочка команд
    GUARD: SEMICOLON_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: CRLF_HEADER_STACK
    INPUT: "value; injected=1 (в заголовке/cookie)"
    CONTEXT: добавление лишнего атрибута/директивы через ";"
    RISK: MEDIUM
    ATTACK: ";" дописывает подконтрольную атакующему директиву в заголовок/cookie
    GUARD: SEMICOLON_FORM ≠ OUTPUT_CONTEXT_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_SEMICOLON_BYPASS
    INPUT: "cmd；rm （полноширинная ； U+FF1B）"
    CONTEXT: похожий знак для обхода фильтра ";"
    RISK: MEDIUM
    ATTACK: фильтр ищет ASCII ";", нормализатор может свернуть ； в ";"
    GUARD: SEMICOLON_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ;
    CODEPOINT: U+037E
    NAME: GREEK QUESTION MARK
    RISK: HIGH
    RULE: GREEK_QUESTION_MARK ≠ SEMICOLON (визуально идентичен; обходит фильтр по ASCII ";")
  CONFUSABLE_002:
    VISIBLE_FORM: ；
    CODEPOINT: U+FF1B
    NAME: FULLWIDTH SEMICOLON
    RISK: HIGH
    RULE: FULLWIDTH_SEMICOLON ≠ SEMICOLON (обходит фильтр, ищущий ASCII ";")
  CONFUSABLE_003:
    VISIBLE_FORM: ؛
    CODEPOINT: U+061B
    NAME: ARABIC SEMICOLON
    RISK: MEDIUM
    RULE: ARABIC_SEMICOLON ≠ SEMICOLON
  CONFUSABLE_004:
    VISIBLE_FORM: ⁏
    CODEPOINT: U+204F
    NAME: REVERSED SEMICOLON
    RISK: LOW
    RULE: REVERSED_SEMICOLON ≠ SEMICOLON
  CONFUSABLE_005:
    VISIBLE_FORM: ﹔
    CODEPOINT: U+FE54
    NAME: SMALL SEMICOLON
    RISK: LOW
    RULE: SMALL_SEMICOLON ≠ SEMICOLON

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "';' — это всегда текстовая пунктуация"
    RESPONSE: SEMICOLON_FORM ≠ PUNCTUATION_ONLY_PROOF
    RULE: в shell/SQL ";" запускает вторую команду/инструкцию
  CG2:
    TRIGGER: "разделитель не может ничего исполнить"
    RESPONSE: SEMICOLON_FORM ≠ SEPARATOR_SAFETY_PROOF
    RULE: разделение начинает новую исполняемую единицу
  CG3:
    TRIGGER: "раз ввод дошёл до исполнения, ';' уже безопасен"
    RESPONSE: SEMICOLON_FORM ≠ OUTPUT_CONTEXT_PROOF
    RULE: безопасность зависит от контекста разбора/исполнения; параметризация/allow-list
  CG4:
    TRIGGER: "'%3B' безопасен навсегда"
    RESPONSE: SEMICOLON_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в ";" перед исполнением
  CG5:
    TRIGGER: "фильтр по ASCII ';' ловит все разделители"
    RESPONSE: SEMICOLON_FORM ≠ EFFECT
    RULE: греческий ; (U+037E) и полноширинный ； (U+FF1B) — другие кодпоинты
  CG6:
    TRIGGER: "наличие ';' значит, что ввод санитизирован"
    RESPONSE: SEMICOLON_FORM ≠ SANITIZED_PROOF
    RULE: наличие знака ничего не говорит о санитизации

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "; "
      NAME: SHELL_COMMAND_CHAIN
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: цепочка второй команды shell
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "; --"
      NAME: SQL_STACK_COMMENT
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: стекинг инструкции и комментирование остатка
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: ";&"
      NAME: CHAIN_BACKGROUND
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: цепочка с последующим уходом команды в фон
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — последовательности с ";" центральны для инъекции команд/инструкций.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: ";" делает цепочку команд/инструкций, но не имитирует существование верифицированной сущности. Его риски — инъекция/стекинг, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена ASCII ";" на греческий ; (U+037E) для обхода фильтра
  A2: замена на полноширинный ； (U+FF1B)
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: цепочка shell ping 8.8.8.8; rm -rf /
  B2: стекинг SQL 1; DROP TABLE users; --
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "; " (SC1) — цепочка команд shell
  C2: "; --" (SC2) — стекинг SQL + комментарий
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: ";" подан как безобидная пунктуация внутри поля команды
  D2: "%3B" как «безопасный» кодированный текст с поздним декодированием
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: цепочка в шаблон OS-команды
  E2: N/A — вектор: инъекция второй инструкции в построитель запросов
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: ";" — всегда текстовая пунктуация
  EXPECTED: FAIL_PUNCTUATION_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: разделитель не может ничего исполнить
  EXPECTED: FAIL_SEPARATOR_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: раз ввод дошёл до исполнения, ";" уже безопасен
  EXPECTED: FAIL_OUTPUT_CONTEXT_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%3B" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: фильтр по ASCII ";" ловит все похожие разделители
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: наличие ";" доказывает санитизацию ввода
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как нейтрализовать ";" по контексту (shell/SQL/заголовок) без ложных срабатываний на тексте/CSS/CSV?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (параметризованные запросы + exec через вектор аргументов + контекстное экранирование — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «безопасность ';' решается контекстом исполнения/разбора».
ALL_OPEN_QUESTIONS_CLOSED: NO (делегировано, не блокирует)

============================================================
11. PATCH_HISTORY
============================================================
PATCH_HISTORY:
  v0_1_PATCH_01: первичное создание (Ruslan Malyavsky, 2026-07-21) — черновик по шаблону GEN3_v0_3 (Vakhter); не прогнан по конвейеру.
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
  NOT_CONVEYOR_RUN (черновик для нашей работы; конвейер — отдельный проект)
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
