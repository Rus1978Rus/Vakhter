PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_PLUS_SIGN_U002B_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: Русский оригинал (authoritative). Английское зеркало — SIGN_CORE_CARD_PLUS_SIGN_U002B_GEN3_v0_3_EN. Кодпоинты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_PLUS_SIGN_U002B_GEN3_v0_3_RU
CODEPOINT: U+002B
VISIBLE_FORM: +
UNICODE_NAME: PLUS SIGN
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: плюс / пробел URL и конкатенация
CATEGORY_ROADMAP: INJ (декод пробела URL, конкатенация SQL, квантор регэкспа) · PHAGO: — (неоднозначность кодирования)

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
VISIBLE_FORM: +
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: PLUS_SIGN_FORM ≠ EFFECT
SIGN_CATEGORY:
  - арифметическое сложение / конкатенация строк (a + b)
  - кодирование пробела в application/x-www-form-urlencoded (+)
  - конкатенация строк SQL (в некоторых диалектах: 'a' + 'b')
  - квантор регэкспа «один или более» (a+)

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_ADDITION_ONLY — "+" не всегда арифметика (в form-encoded URL это пробел)
  2. NOT_SPACE_DECODE_SAFE — "+", декодируемый в пробел, может изменить разбор значения дальше по цепочке
  3. NOT_CONCAT_SAFE — конкатенация строк может вставить данные атакующего в запрос/команду
  4. NOT_ESCAPED_PROOF — наличие "+" не значит, что он закавычен/экранирован
  5. NOT_ENCODED_SAFE — "%2B" может быть раскодирован обратно в "+" позже (или "+" в пробел)
  6. NOT_AUTHORITY — "+" не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сам по себе ничего не исполняет; декод/конкатенацию делает контекст
  8. NOT_TRUST_SIGNAL — не повышает доверие
  9. NOT_REGEX_ONLY — "+" в регэкспе — квантор, который может вызвать ReDoS
  10. NOT_SANITIZED_PROOF — наличие "+" не значит, что ввод санитизирован
  11. NOT_OUTPUT_CONTEXT_PROOF — безопасность зависит от контекста декода/разбора

BASE_FORMULAS:
  PLUS_SIGN_FORM ≠ EFFECT
  PLUS_SIGN_FORM ≠ ADDITION_ONLY_PROOF
  PLUS_SIGN_FORM ≠ SPACE_DECODE_SAFETY_PROOF
  PLUS_SIGN_FORM ≠ CONCAT_SAFETY_PROOF
  PLUS_SIGN_FORM ≠ ESCAPED_PROOF
  PLUS_SIGN_FORM ≠ ENCODED_SAFETY_PROOF
  PLUS_SIGN_FORM ≠ AUTHORITY
  PLUS_SIGN_FORM ≠ EXECUTION_TRIGGER
  PLUS_SIGN_FORM ≠ REGEX_ONLY_PROOF
  PLUS_SIGN_FORM ≠ SANITIZED_PROOF
  PLUS_SIGN_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: "+" (ZONE_1) имеет параллельные функции (сложение, конкатенация, пробел URL, квантор регэкспа), сосуществующие без культурной прецессии. Полисемия стабильного знака.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1
  NOTE: математический знак без жестового предшественника; функции пробела URL/конкатенации/квантора надстроены цифровой эпохой параллельно.

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
    INPUT: "2 + 3 = 5"
    CONTEXT: арифметическое сложение в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: PLUS_SIGN_FORM ≠ ADDITION_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: "C++ programming"
    CONTEXT: "+" внутри названия языка
    EXPECTED: INFO
    RISK: NONE
    GUARD: PLUS_SIGN_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "+1 202 555 0100"
    CONTEXT: международный префикс телефонного номера
    EXPECTED: INFO
    RISK: NONE
    GUARD: PLUS_SIGN_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "a + b in code"
    CONTEXT: сложение/конкатенация, показанные как текст
    EXPECTED: INFO
    RISK: NONE
    GUARD: PLUS_SIGN_FORM ≠ CONCAT_SAFETY_PROOF
  SAFE_CASE_005:
    INPUT: "temperature +5 degrees"
    CONTEXT: знак «плюс» в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: PLUS_SIGN_FORM ≠ ADDITION_ONLY_PROOF
  SAFE_CASE_006:
    INPUT: "search?q=cats+dogs"
    CONTEXT: обычный form-encoded пробел между словами
    EXPECTED: INFO
    RISK: NONE
    GUARD: PLUS_SIGN_FORM ≠ SPACE_DECODE_SAFETY_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: URL_SPACE_DECODE_DESYNC
    INPUT: "id=1+OR+1=1"
    CONTEXT: "+" декодируется в пробелы, образуя предложение SQL после декода
    RISK: HIGH
    ATTACK: "+" декодируется в пробел, так что "1 OR 1=1" достигает построителя запросов
    GUARD: PLUS_SIGN_FORM ≠ SPACE_DECODE_SAFETY_PROOF
  RISK_CASE_002:
    NAME: SQL_STRING_CONCAT
    INPUT: "'a'+(SELECT password FROM users)"
    CONTEXT: "+" конкатенирует подзапрос в строку (MSSQL)
    RISK: HIGH
    ATTACK: "+" вставляет утёкшие данные в вывод через конкатенацию
    GUARD: PLUS_SIGN_FORM ≠ CONCAT_SAFETY_PROOF
  RISK_CASE_003:
    NAME: REGEX_QUANTIFIER_REDOS
    INPUT: "(a+)+$ на длинном вводе"
    CONTEXT: вложенный квантор "+", вызывающий катастрофический бэктрекинг
    RISK: HIGH
    ATTACK: "+" над группой запускает ReDoS (отказ в обслуживании)
    GUARD: PLUS_SIGN_FORM ≠ REGEX_ONLY_PROOF
  RISK_CASE_004:
    NAME: PLUS_VS_ENCODED_PLUS_AMBIGUITY
    INPUT: "token=a%2Bb (литеральный +) vs a+b (пробел)"
    CONTEXT: неоднозначность между литеральным "+" и form-encoded пробелом
    RISK: MEDIUM
    ATTACK: рассогласованные декодеры читают "+" как пробел или литерал, портя токен/подпись
    GUARD: PLUS_SIGN_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: EMAIL_SUBADDRESS_ABUSE
    INPUT: "victim+attacker@example.com"
    CONTEXT: "+"-субадресация для обхода проверки уникальности email
    RISK: MEDIUM
    ATTACK: "+tag" создаёт множество псевдонимов одного ящика, обходя лимиты на email
    GUARD: PLUS_SIGN_FORM ≠ EFFECT
  RISK_CASE_006:
    NAME: FULLWIDTH_PLUS_BYPASS
    INPUT: "1＋1 (полноширинный ＋ U+FF0B)"
    CONTEXT: похожий знак для обхода фильтра "+"
    RISK: LOW
    ATTACK: фильтр ищет ASCII "+", нормализатор может свернуть ＋ в "+"
    GUARD: PLUS_SIGN_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ＋
    CODEPOINT: U+FF0B
    NAME: FULLWIDTH PLUS SIGN
    RISK: HIGH
    RULE: FULLWIDTH_PLUS_SIGN ≠ PLUS_SIGN (обходит фильтр, ищущий ASCII "+")
  CONFUSABLE_002:
    VISIBLE_FORM: ﹢
    CODEPOINT: U+FE62
    NAME: SMALL PLUS SIGN
    RISK: MEDIUM
    RULE: SMALL_PLUS_SIGN ≠ PLUS_SIGN
  CONFUSABLE_003:
    VISIBLE_FORM: ⁺
    CODEPOINT: U+207A
    NAME: SUPERSCRIPT PLUS SIGN
    RISK: LOW
    RULE: SUPERSCRIPT_PLUS ≠ PLUS_SIGN
  CONFUSABLE_004:
    VISIBLE_FORM: ➕
    CODEPOINT: U+2795
    NAME: HEAVY PLUS SIGN
    RISK: LOW
    RULE: HEAVY_PLUS_SIGN ≠ PLUS_SIGN
  CONFUSABLE_005:
    VISIBLE_FORM: ﬩
    CODEPOINT: U+FB29
    NAME: HEBREW LETTER ALTERNATIVE PLUS SIGN
    RISK: LOW
    RULE: HEBREW_ALT_PLUS ≠ PLUS_SIGN

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "'+' — это всегда арифметическое сложение"
    RESPONSE: PLUS_SIGN_FORM ≠ ADDITION_ONLY_PROOF
    RULE: в form-encoded URL "+" значит пробел; в SQL он конкатенирует
  CG2:
    TRIGGER: "'+', декодируемый в пробел, безобиден"
    RESPONSE: PLUS_SIGN_FORM ≠ SPACE_DECODE_SAFETY_PROOF
    RULE: декодированный пробел может переформировать значение в инъектируемое предложение
  CG3:
    TRIGGER: "конкатенация строк не может быть опасной"
    RESPONSE: PLUS_SIGN_FORM ≠ CONCAT_SAFETY_PROOF
    RULE: "+" может вставить подзапрос/данные атакующего в вывод
  CG4:
    TRIGGER: "'%2B' / '+' кодирование безопасно навсегда"
    RESPONSE: PLUS_SIGN_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: декодеры расходятся во мнении "+" vs пробел; смысл может перевернуться дальше по цепочке
  CG5:
    TRIGGER: "фильтр по ASCII '+' ловит все знаки плюс"
    RESPONSE: PLUS_SIGN_FORM ≠ EFFECT
    RULE: полноширинный ＋ (U+FF0B) и малый ﹢ (U+FE62) — другие кодпоинты
  CG6:
    TRIGGER: "наличие '+' значит, что ввод санитизирован"
    RESPONSE: PLUS_SIGN_FORM ≠ SANITIZED_PROOF
    RULE: наличие знака ничего не говорит о санитизации

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "+OR+"
      NAME: URL_SPACE_SQL
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: "+" декодируется в пробелы, образуя предложение SQL
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: ")+"
      NAME: REGEX_NESTED_QUANTIFIER
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: квантор над группой, вызывающий катастрофический бэктрекинг
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "+@"
      NAME: EMAIL_SUBADDRESS
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: "+tag"-субадресация для порождения множества псевдонимов ящика
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — последовательности с "+" центральны для рассинхрона декода/конкатенации/злоупотребления регэкспом.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: "+" декодируется в пробел или конкатенирует значения, но не имитирует существование верифицированной сущности. Его риски — рассинхрон декода/конкатенация, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена ASCII "+" на полноширинный ＋ (U+FF0B) для обхода фильтра
  A2: замена на малый ﹢ (U+FE62)
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: рассинхрон декода пробела URL id=1+OR+1=1
  B2: конкатенация строк SQL 'a'+(SELECT password FROM users)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "+OR+" (SC1) — пробел URL в предложение SQL
  C2: ")+" (SC2) — вложенный квантор регэкспа (ReDoS)
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: "+" подан как безобидное сложение внутри значения запроса
  D2: неоднозначность "%2B vs +", трактуемая как «безопасная», пока декодер её не перевернёт
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: рассинхрон декода в построитель запросов
  E2: N/A — вектор: утечка через конкатенацию в строку MSSQL
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: "+" — всегда арифметическое сложение
  EXPECTED: FAIL_ADDITION_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: "+", декодируемый в пробел, безобиден
  EXPECTED: FAIL_SPACE_DECODE_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: конкатенация строк не может быть опасной
  EXPECTED: FAIL_CONCAT_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%2B" / "+" кодирование безопасно навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: фильтр по ASCII "+" ловит все похожие знаки плюс
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: наличие "+" доказывает санитизацию ввода
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как канонизировать "+" по контексту (form-декод/SQL/регэксп) без ложных срабатываний на арифметике/телефоне/C++/субадресе?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (согласованный однопроходный декод + параметризованные запросы + таймаут регэкспа — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «смысл '+' (пробел vs литерал vs конкатенация) решается контекстом декода/разбора».
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
