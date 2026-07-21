ЧАСТНЫЙ АВТОРСКИЙ ПРОЕКТ / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_QUESTION_MARK_U003F_GEN3_v0_3_RU
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
CARD_UID: SIGN_CORE_CARD_QUESTION_MARK_U003F_GEN3_v0_3_RU
CODEPOINT: U+003F
VISIBLE_FORM: ?
UNICODE_NAME: QUESTION MARK
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: вопросительный знак
CATEGORY_ROADMAP: PH (граница query, контрабанда параметров) · PHAGO: — (маскировка структуры)

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
VISIBLE_FORM: ?
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_SEPARATOR
BASE_MODE_FORMULA: QUESTION_MARK_FORM ≠ EFFECT
SIGN_CATEGORY:
  - пунктуация (вопрос)
  - разделитель начала query-строки в URL (?a=1&b=2)
  - тернарный оператор (a ? b : c)
  - квантификатор «0 или 1» в regex (colou?r)
  - glob-wildcard одного символа в shell (file?.txt)

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_QUERY_SAFE — начало query «?» не делает параметры безопасными
  2. NOT_PARAM_VALIDITY_PROOF — наличие «?» не подтверждает корректность параметров
  3. NOT_SINGLE_QUERY_BOUNDARY — второй «?» может путать парсер о границе query
  4. NOT_REDIRECT_SAFE — «?next=…» не гарантирует безопасный редирект
  5. NOT_AUTHORITY — «?» не подтверждает официальность
  6. NOT_EXECUTION_TRIGGER — сам по себе ничего не исполняет
  7. NOT_TRUST_SIGNAL — не повышает доверие
  8. NOT_GLOB_SAFE — «?» как wildcard может расширять доступ к файлам
  9. NOT_REGEX_SAFE — «?» в regex меняет семантику паттерна
  10. NOT_PARAM_UNIQUENESS_PROOF — повтор параметра (?id=1&id=2) не однозначен
  11. NOT_URL_END_MARKER — «?» не отмечает конец URL/пути надёжно

BASE_FORMULAS:
  QUESTION_MARK_FORM ≠ EFFECT
  QUESTION_MARK_FORM ≠ QUERY_SAFETY_PROOF
  QUESTION_MARK_FORM ≠ PARAM_VALIDITY_PROOF
  QUESTION_MARK_FORM ≠ SINGLE_QUERY_BOUNDARY_PROOF
  QUESTION_MARK_FORM ≠ REDIRECT_SAFETY_PROOF
  QUESTION_MARK_FORM ≠ AUTHORITY
  QUESTION_MARK_FORM ≠ TRUST_SIGNAL
  QUESTION_MARK_FORM ≠ GLOB_SAFETY_PROOF
  QUESTION_MARK_FORM ≠ REGEX_SAFETY_PROOF
  QUESTION_MARK_FORM ≠ PARAM_UNIQUENESS_PROOF
  QUESTION_MARK_FORM ≠ URL_END_MARKER_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: «?» (ZONE_1) имеет параллельные функции (вопрос, query, тернар, regex, glob), сосуществующие без культурной прецессии. Полисемия стабильного знака.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1
  NOTE: письменный знак пунктуации без жестового предшественника; функции query/regex наложены цифровой эпохой параллельно.

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
    INPUT: "Вы уверены?"
    CONTEXT: вопросительное предложение
    EXPECTED: INFO
    RISK: NONE
    GUARD: QUESTION_MARK_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "https://site.com/search?q=коты"
    CONTEXT: обычная query-строка
    EXPECTED: INFO
    RISK: NONE
    GUARD: QUESTION_MARK_FORM ≠ QUERY_SAFETY_PROOF
  SAFE_CASE_003:
    INPUT: "x = a ? b : c"
    CONTEXT: тернарный оператор
    EXPECTED: INFO
    RISK: NONE
    GUARD: QUESTION_MARK_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "regex: colou?r"
    CONTEXT: квантификатор «0 или 1»
    EXPECTED: INFO
    RISK: NONE
    GUARD: QUESTION_MARK_FORM ≠ REGEX_SAFETY_PROOF
  SAFE_CASE_005:
    INPUT: "ls file?.txt"
    CONTEXT: glob одного символа
    EXPECTED: INFO
    RISK: NONE
    GUARD: QUESTION_MARK_FORM ≠ GLOB_SAFETY_PROOF
  SAFE_CASE_006:
    INPUT: "issue #? open"
    CONTEXT: вопрос в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: QUESTION_MARK_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: OPEN_REDIRECT_PARAM
    INPUT: "https://site.com/login?next=//evil.com"
    CONTEXT: параметр редиректа ведёт на внешний хост
    RISK: HIGH
    ATTACK: «?next=» с внешним URL/protocol-relative — open redirect после логина
    GUARD: QUESTION_MARK_FORM ≠ REDIRECT_SAFETY_PROOF
  RISK_CASE_002:
    NAME: PARAMETER_POLLUTION
    INPUT: "?id=1&id=2&id=admin"
    CONTEXT: повтор параметра (HTTP Parameter Pollution)
    RISK: HIGH
    ATTACK: разные слои читают разное значение id — рассинхрон авторизации/логики
    GUARD: QUESTION_MARK_FORM ≠ PARAM_UNIQUENESS_PROOF
  RISK_CASE_003:
    NAME: SECOND_QUESTION_MARK_SMUGGLE
    INPUT: "/path?a=1?b=2"
    CONTEXT: второй «?» путает парсер о границе query
    RISK: MEDIUM
    ATTACK: неоднозначная граница query протаскивает параметр мимо валидации
    GUARD: QUESTION_MARK_FORM ≠ SINGLE_QUERY_BOUNDARY_PROOF
  RISK_CASE_004:
    NAME: JS_SCHEME_IN_PARAM
    INPUT: "?url=javascript:alert(1)"
    CONTEXT: опасная схема как значение параметра-редиректа
    RISK: HIGH
    ATTACK: значение параметра подставляется в href → XSS
    GUARD: QUESTION_MARK_FORM ≠ QUERY_SAFETY_PROOF
  RISK_CASE_005:
    NAME: SSRF_VIA_PARAM
    INPUT: "?image=http://169.254.169.254/latest/meta-data/"
    CONTEXT: параметр с внутренним URL (SSRF)
    RISK: HIGH
    ATTACK: сервер запрашивает URL из параметра — доступ к метаданным/внутренней сети
    GUARD: QUESTION_MARK_FORM ≠ PARAM_VALIDITY_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_QM_BYPASS
    INPUT: "search？q=x" (полноширинный ？ U+FF1F)
    CONTEXT: двойник-знак для обхода парсера query
    RISK: MEDIUM
    ATTACK: фильтр ищет ASCII «?», нормализатор может привести ？ к «?»
    GUARD: QUESTION_MARK_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ？
    CODEPOINT: U+FF1F
    NAME: FULLWIDTH QUESTION MARK
    RISK: HIGH
    RULE: FULLWIDTH_QUESTION_MARK ≠ QUESTION_MARK (обход фильтра query, ищущего ASCII «?»)
  CONFUSABLE_002:
    VISIBLE_FORM: ⁇
    CODEPOINT: U+2047
    NAME: DOUBLE QUESTION MARK
    RISK: LOW
    RULE: DOUBLE_QUESTION_MARK ≠ QUESTION_MARK
  CONFUSABLE_003:
    VISIBLE_FORM: ¿
    CODEPOINT: U+00BF
    NAME: INVERTED QUESTION MARK
    RISK: LOW
    RULE: INVERTED_QUESTION_MARK ≠ QUESTION_MARK
  CONFUSABLE_004:
    VISIBLE_FORM: ‽
    CODEPOINT: U+203D
    NAME: INTERROBANG
    RISK: LOW
    RULE: INTERROBANG ≠ QUESTION_MARK
  CONFUSABLE_005:
    VISIBLE_FORM: ﹖
    CODEPOINT: U+FE56
    NAME: SMALL QUESTION MARK
    RISK: LOW
    RULE: SMALL_QUESTION_MARK ≠ QUESTION_MARK

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: «раз есть „?“, query безопасен»
    RESPONSE: QUESTION_MARK_FORM ≠ QUERY_SAFETY_PROOF
    RULE: значения параметров могут нести редирект/XSS/SSRF; проверять значения
  CG2:
    TRIGGER: «параметр в URL уникален»
    RESPONSE: QUESTION_MARK_FORM ≠ PARAM_UNIQUENESS_PROOF
    RULE: возможен повтор (HPP); разные слои читают разное
  CG3:
    TRIGGER: «в URL только один „?“, значит граница query однозначна»
    RESPONSE: QUESTION_MARK_FORM ≠ SINGLE_QUERY_BOUNDARY_PROOF
    RULE: второй «?» может путать парсер
  CG4:
    TRIGGER: «„?next=URL“ ведёт только внутрь сайта»
    RESPONSE: QUESTION_MARK_FORM ≠ REDIRECT_SAFETY_PROOF
    RULE: значение редиректа надо валидировать по allowlist хостов
  CG5:
    TRIGGER: «фильтр по ASCII „?“ ловит все query»
    RESPONSE: QUESTION_MARK_FORM ≠ EFFECT
    RULE: полноширинный ？ (U+FF1F) — другой кодпоинт
  CG6:
    TRIGGER: «„?“ отмечает конец URL»
    RESPONSE: QUESTION_MARK_FORM ≠ URL_END_MARKER_PROOF
    RULE: после «?» идёт query, а затем возможен «#» fragment; «?» не конец

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "?a=1&b=2"
      NAME: QUERY_STRING
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: параметры запроса; опасность в значениях (редирект/SSRF/XSS)
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "?a=1?b=2"
      NAME: DOUBLE_QUERY_DELIMITER
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: неоднозначная граница query, контрабанда параметра
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "id=1&id=2"
      NAME: PARAM_POLLUTION
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: HTTP Parameter Pollution, рассинхрон слоёв
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — query-последовательности ключевы для знака.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: «?» маскирует СТРУКТУРУ URL (границы query, контрабанда параметров), но не имитирует существование проверенной сущности. Риски — обфускация/логика, не entity-mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена ASCII «?» на полноширинный ？ (U+FF1F) для обхода парсера query
  A2: смешение «?» с двойником ⁇ (U+2047) в фильтре
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: open redirect «?next=//evil.com»
  B2: SSRF «?image=http://169.254.169.254/…»
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: двойной «?» «/path?a=1?b=2» (SC2)
  C2: parameter pollution «id=1&id=2&id=admin» (SC3)
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: «?url=javascript:…» — опасная схема в параметре
  D2: cache-buster «?v=12345» как псевдо-легит для сокрытия трекинга
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не носитель PHAGO; вектор: параметр-редирект на двойник бренда
  E2: N/A — вектор: параметр с внутренним URL (SSRF)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет дремлющих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: наличие «?» делает query-параметры безопасными
  EXPECTED: FAIL_QUERY_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: параметр в URL всегда уникален
  EXPECTED: FAIL_PARAM_UNIQUENESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: один «?» означает однозначную границу query
  EXPECTED: FAIL_QUERY_BOUNDARY_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: «?next=URL» ведёт только внутрь сайта
  EXPECTED: FAIL_REDIRECT_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: ASCII-фильтр по «?» ловит все варианты знака
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: «?» отмечает конец URL
  EXPECTED: FAIL_URL_END_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как валидировать значения параметров (редирект/SSRF/XSS) без ложных срабатываний на легит-query?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (allowlist хостов/схем + контекст вывода — уровень интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «проверять значения параметров, а не факт „?“».
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
