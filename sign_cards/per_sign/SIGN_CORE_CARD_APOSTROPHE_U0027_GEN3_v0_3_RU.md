ЧАСТНЫЙ АВТОРСКИЙ ПРОЕКТ / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_APOSTROPHE_U0027_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
DRAFT_NOTE: черновик для нашей работы (Vakhter). Русская версия авторитетна; EN — зеркало.

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
LIMITATION_STATEMENT (стандарт):
  CONVEYOR_PASS ≠ VALIDATION
  MODEL_CONSENSUS ≠ TRUTH
  INJECTION_TEST_PASS ≠ SECURITY_PROOF
  GUARDS_HOLD_FOR_TESTED_CASES ≠ FUTURE_GUARANTEE
  NO_ATTACK_FOUND ≠ NO_ATTACK_EXISTS

============================================================
2. META
============================================================
CARD_UID: SIGN_CORE_CARD_APOSTROPHE_U0027_GEN3_v0_3_RU
CODEPOINT: U+0027
VISIBLE_FORM: '
UNICODE_NAME: APOSTROPHE
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: апостроф / одинарная кавычка
CATEGORY_ROADMAP: INJ (разрыв строки SQL-инъекции) · PHAGO: — (маскировка структуры)

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
VISIBLE_FORM: '
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: APOSTROPHE_FORM ≠ EFFECT
SIGN_CATEGORY:
  - разделитель строкового литерала (SQL/JS/shell: '...')
  - апостроф/сокращение в тексте (don't, O'Brien)
  - одинарная кавычка/цитирование

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_STRING_SAFE — «'» не делает строковый литерал безопасным (разрывает контекст)
  2. NOT_ESCAPED_PROOF — присутствие «'» не значит, что он экранирован
  3. NOT_APOSTROPHE_ONLY — «'» не всегда апостроф (в SQL это разделитель строки)
  4. NOT_PARAMETERIZED_PROOF — «'» не значит, что запрос параметризован
  5. NOT_AUTHORITY — «'» не подтверждает официальность
  6. NOT_EXECUTION_TRIGGER — сам по себе ничего не исполняет
  7. NOT_TRUST_SIGNAL — не повышает доверие
  8. NOT_SANITIZED_PROOF — наличие «'» не значит, что вход санитизирован
  9. NOT_QUOTE_BALANCE_PROOF — «'» не гарантирует сбалансированность кавычек
  10. NOT_ENCODED_SAFE — «%27»/«&#39;» может декодироваться обратно в «'»
  11. NOT_LITERAL_TEXT — «'» не всегда литеральный текст (может закрывать строку в запросе)

BASE_FORMULAS:
  APOSTROPHE_FORM ≠ EFFECT
  APOSTROPHE_FORM ≠ STRING_SAFETY_PROOF
  APOSTROPHE_FORM ≠ ESCAPED_PROOF
  APOSTROPHE_FORM ≠ APOSTROPHE_ONLY_PROOF
  APOSTROPHE_FORM ≠ PARAMETERIZED_PROOF
  APOSTROPHE_FORM ≠ AUTHORITY
  APOSTROPHE_FORM ≠ EXECUTION_TRIGGER
  APOSTROPHE_FORM ≠ TRUST_SIGNAL
  APOSTROPHE_FORM ≠ SANITIZED_PROOF
  APOSTROPHE_FORM ≠ QUOTE_BALANCE_PROOF
  APOSTROPHE_FORM ≠ ENCODED_SAFETY_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: «'» (ZONE_1) имеет параллельные функции (апостроф в тексте, разделитель строки в коде/SQL, цитирование), сосуществующие без культурной прецессии. Полисемия стабильного знака.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1
  NOTE: письменный знак пунктуации без жестового предшественника; функция разделителя строк наложена цифровой эпохой параллельно.

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
    INPUT: "don't worry"
    CONTEXT: апостроф в сокращении
    EXPECTED: INFO
    RISK: NONE
    GUARD: APOSTROPHE_FORM ≠ APOSTROPHE_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: "O'Brien"
    CONTEXT: апостроф в фамилии
    EXPECTED: INFO
    RISK: NONE
    GUARD: APOSTROPHE_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "it's fine"
    CONTEXT: апостроф в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: APOSTROPHE_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "name = 'value' (параметризованный запрос)"
    CONTEXT: строковый литерал через prepared statement (значение — параметр)
    EXPECTED: INFO
    RISK: NONE
    GUARD: APOSTROPHE_FORM ≠ PARAMETERIZED_PROOF
  SAFE_CASE_005:
    INPUT: "l'école"
    CONTEXT: апостроф во французском слове
    EXPECTED: INFO
    RISK: NONE
    GUARD: APOSTROPHE_FORM ≠ APOSTROPHE_ONLY_PROOF
  SAFE_CASE_006:
    INPUT: "'строка в одинарных кавычках'"
    CONTEXT: корректно закрытый строковый литерал
    EXPECTED: INFO
    RISK: NONE
    GUARD: APOSTROPHE_FORM ≠ QUOTE_BALANCE_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: SQLI_AUTH_BYPASS
    INPUT: "' OR '1'='1"
    CONTEXT: ввод в неэкранированный SQL-запрос
    RISK: CRITICAL
    ATTACK: «'» закрывает строку, «OR '1'='1» делает условие всегда истинным — обход авторизации
    GUARD: APOSTROPHE_FORM ≠ STRING_SAFETY_PROOF
  RISK_CASE_002:
    NAME: SQLI_STACKED_QUERY
    INPUT: "'; DROP TABLE users --"
    CONTEXT: разрыв строки и добавление второго запроса
    RISK: CRITICAL
    ATTACK: «'» закрывает литерал, «;» начинает новый запрос, «--» комментирует хвост
    GUARD: APOSTROPHE_FORM ≠ SANITIZED_PROOF
  RISK_CASE_003:
    NAME: SQLI_UNION
    INPUT: "' UNION SELECT username,password FROM users --"
    CONTEXT: извлечение данных через UNION
    RISK: CRITICAL
    ATTACK: «'» разрывает строку, UNION присоединяет чужую выборку
    GUARD: APOSTROPHE_FORM ≠ PARAMETERIZED_PROOF
  RISK_CASE_004:
    NAME: COMMENT_TERMINATION
    INPUT: "admin'--"
    CONTEXT: закрытие строки и комментирование остатка запроса
    RISK: HIGH
    ATTACK: «'--» отсекает проверку пароля в условии WHERE
    GUARD: APOSTROPHE_FORM ≠ QUOTE_BALANCE_PROOF
  RISK_CASE_005:
    NAME: ESCAPED_QUOTE_CONFUSION
    INPUT: "\\' (обратный слэш перед кавычкой)"
    CONTEXT: путаница экранирования между слоями
    RISK: HIGH
    ATTACK: «\\'» в одном слое экранирован, в другом — разрывает строку (рассинхрон экранирования)
    GUARD: APOSTROPHE_FORM ≠ ESCAPED_PROOF
  RISK_CASE_006:
    NAME: SMART_QUOTE_BYPASS
    INPUT: "’ OR ’1’=’1 (правая одинарная кавычка ’ U+2019)"
    CONTEXT: двойник-кавычка, нормализуемый бэкендом к «'»
    RISK: MEDIUM
    ATTACK: фильтр ищет ASCII «'», а нормализатор/БД приводит ’ к «'» → инъекция оживает
    GUARD: APOSTROPHE_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ’
    CODEPOINT: U+2019
    NAME: RIGHT SINGLE QUOTATION MARK
    RISK: HIGH
    RULE: RIGHT_SINGLE_QUOTE ≠ APOSTROPHE (умная кавычка, нормализуется к «'»)
  CONFUSABLE_002:
    VISIBLE_FORM: ＇
    CODEPOINT: U+FF07
    NAME: FULLWIDTH APOSTROPHE
    RISK: HIGH
    RULE: FULLWIDTH_APOSTROPHE ≠ APOSTROPHE (обход ASCII-фильтра)
  CONFUSABLE_003:
    VISIBLE_FORM: ‘
    CODEPOINT: U+2018
    NAME: LEFT SINGLE QUOTATION MARK
    RISK: MEDIUM
    RULE: LEFT_SINGLE_QUOTE ≠ APOSTROPHE
  CONFUSABLE_004:
    VISIBLE_FORM: ´
    CODEPOINT: U+00B4
    NAME: ACUTE ACCENT
    RISK: LOW
    RULE: ACUTE_ACCENT ≠ APOSTROPHE
  CONFUSABLE_005:
    VISIBLE_FORM: ʼ
    CODEPOINT: U+02BC
    NAME: MODIFIER LETTER APOSTROPHE
    RISK: MEDIUM
    RULE: MODIFIER_APOSTROPHE ≠ APOSTROPHE

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: «раз ввод экранирован один раз, „'“ безопасен в SQL»
    RESPONSE: APOSTROPHE_FORM ≠ ESCAPED_PROOF
    RULE: рассинхрон экранирования между слоями; использовать параметризованные запросы
  CG2:
    TRIGGER: «„'“ — это всегда апостроф»
    RESPONSE: APOSTROPHE_FORM ≠ APOSTROPHE_ONLY_PROOF
    RULE: в SQL/JS «'» разделяет строку, а не пишет апостроф
  CG3:
    TRIGGER: «наличие „'“ значит, что запрос параметризован»
    RESPONSE: APOSTROPHE_FORM ≠ PARAMETERIZED_PROOF
    RULE: единственная защита — prepared statements, не присутствие/отсутствие кавычки
  CG4:
    TRIGGER: «фильтр по ASCII „'“ ловит все кавычки»
    RESPONSE: APOSTROPHE_FORM ≠ EFFECT
    RULE: ’ (U+2019), ＇ (U+FF07) — другие кодпоинты, нормализуемые к «'»
  CG5:
    TRIGGER: «„admin'--“ — просто текст с апострофом»
    RESPONSE: APOSTROPHE_FORM ≠ SANITIZED_PROOF
    RULE: «'--» закрывает строку и комментирует условие; санитизация обязательна
  CG6:
    TRIGGER: «сбалансированные кавычки = безопасно»
    RESPONSE: APOSTROPHE_FORM ≠ QUOTE_BALANCE_PROOF
    RULE: баланс кавычек не мешает инъекции (' OR '1'='1 сбалансирован)

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "'--"
      NAME: QUOTE_COMMENT_TERMINATION
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: закрытие строки + комментирование остатка SQL
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "' OR '"
      NAME: SQLI_TAUTOLOGY
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: тавтология для обхода авторизации (' OR '1'='1)
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "''"
      NAME: DOUBLED_QUOTE
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: экранированная кавычка в SQL ИЛИ пустая строка — контекст-зависимо
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — последовательности с «'» ключевы для SQL-инъекций.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: «'» маскирует/разрывает СТРУКТУРУ строкового литерала (SQL/код), но не имитирует существование проверенной сущности. Риски — инъекция, не entity-mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена ASCII «'» на ’ (U+2019) / ＇ (U+FF07), нормализуемые бэкендом к «'»
  A2: %27 / &#39; (кодированная кавычка) с последующим декодом
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: «' OR '1'='1» — обход авторизации
  B2: «'; DROP TABLE users --» — stacked query
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: «'--» (SC1) — закрытие строки + комментарий
  C2: «' UNION SELECT …» — извлечение данных
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: «admin'--» под видом обычного логина
  D2: «\\'» — путаница экранирования между слоями
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не носитель PHAGO; вектор: инъекция в WHERE-условие
  E2: N/A — вектор: multibyte-обход экранирования (напр. GBK)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет дремлющих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: однократное экранирование «'» делает SQL безопасным
  EXPECTED: FAIL_ESCAPE_DESYNC_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: «'» — это всегда апостроф
  EXPECTED: FAIL_APOSTROPHE_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: наличие «'» доказывает параметризацию запроса
  EXPECTED: FAIL_PARAMETERIZED_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: ASCII-фильтр по «'» ловит все кавычки-двойники
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: «admin'--» — безобидный текст с апострофом
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: сбалансированные кавычки означают безопасность
  EXPECTED: FAIL_QUOTE_BALANCE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как нейтрализовать «'» без ложных срабатываний на легит-апострофы (don't, O'Brien)?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (параметризованные запросы + нормализация кавычек-двойников — уровень интегратора/рантайма; апостроф в данных остаётся легит)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «безопасность — от prepared statements, не от присутствия „'“».
ALL_OPEN_QUESTIONS_CLOSED: NO (делегирован, не блокирует)

============================================================
11. PATCH_HISTORY
============================================================
PATCH_HISTORY:
  v0_1_PATCH_01: первичное создание (Ruslan Malyavsky, 2026-07-21) — черновик по шаблону GEN3_v0_3 (Vakhter); не прогонялся через конвейер.
PATCHES_APPLIED: 1
PATCHES_VERIFIED: 0/1

============================================================
12. LIMITATION_STATEMENT
============================================================
LIMITATION_STATEMENT:
  THIS_CARD IS A WORKING_DRAFT ARTIFACT (до ARTIFACT_CONFIRMED)
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
