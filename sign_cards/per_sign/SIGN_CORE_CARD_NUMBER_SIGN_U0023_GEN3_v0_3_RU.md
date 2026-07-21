ЧАСТНЫЙ АВТОРСКИЙ ПРОЕКТ / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_NUMBER_SIGN_U0023_GEN3_v0_3_RU
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
CARD_UID: SIGN_CORE_CARD_NUMBER_SIGN_U0023_GEN3_v0_3_RU
CODEPOINT: U+0023
VISIBLE_FORM: #
UNICODE_NAME: NUMBER SIGN
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: решётка / номер (hash)
CATEGORY_ROADMAP: PH (скрытие фрагмента, обрезка URL) · PHAGO: — (маскировка структуры)

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
VISIBLE_FORM: #
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_SEPARATOR
BASE_MODE_FORMULA: NUMBER_SIGN_FORM ≠ EFFECT
SIGN_CATEGORY:
  - разделитель фрагмента URL (#section, #/route)
  - хэштег в соцсетях (#news)
  - идентификатор CSS (#id) / номер (#5)
  - комментарий (shell/python/yaml: # ...)
  - директива препроцессора (#include) / заголовок Markdown (# Title)

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_FRAGMENT_SAFE — «#» фрагмент не делает то, что после него, безопасным
  2. NOT_SERVER_VISIBLE — часть после «#» не отправляется на сервер (только клиент)
  3. NOT_URL_END — «#» не отмечает конец URL; после него идёт фрагмент
  4. NOT_COMMENT_SAFE — «#» как комментарий не гарантирует безопасность строки
  5. NOT_AUTHORITY — «#» не подтверждает официальность
  6. NOT_EXECUTION_TRIGGER — сам по себе ничего не исполняет
  7. NOT_TRUST_SIGNAL — не повышает доверие
  8. NOT_HASHTAG_VALIDITY — «#tag» не подтверждает существование/официальность темы
  9. NOT_ID_UNIQUENESS — «#id» не гарантирует уникальность на странице
  10. NOT_ROUTE_SAFE — «#/admin» (SPA-роут) не безопасен по факту наличия «#»
  11. NOT_TRUNCATION_SAFE — «#» может визуально обрезать восприятие URL

BASE_FORMULAS:
  NUMBER_SIGN_FORM ≠ EFFECT
  NUMBER_SIGN_FORM ≠ FRAGMENT_SAFETY_PROOF
  NUMBER_SIGN_FORM ≠ SERVER_VISIBILITY_PROOF
  NUMBER_SIGN_FORM ≠ URL_END_MARKER_PROOF
  NUMBER_SIGN_FORM ≠ COMMENT_SAFETY_PROOF
  NUMBER_SIGN_FORM ≠ AUTHORITY
  NUMBER_SIGN_FORM ≠ TRUST_SIGNAL
  NUMBER_SIGN_FORM ≠ HASHTAG_VALIDITY_PROOF
  NUMBER_SIGN_FORM ≠ ID_UNIQUENESS_PROOF
  NUMBER_SIGN_FORM ≠ ROUTE_SAFETY_PROOF
  NUMBER_SIGN_FORM ≠ TRUNCATION_SAFETY_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: «#» (ZONE_1) имеет параллельные функции (фрагмент, хэштег, id, номер, комментарий, заголовок), сосуществующие без культурной прецессии. Полисемия стабильного знака.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1
  NOTE: письменный знак без жестового предшественника; функции URL/хэштег наложены цифровой эпохой параллельно.

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
    INPUT: "#новости"
    CONTEXT: хэштег
    EXPECTED: INFO
    RISK: NONE
    GUARD: NUMBER_SIGN_FORM ≠ HASHTAG_VALIDITY_PROOF
  SAFE_CASE_002:
    INPUT: "задача #42"
    CONTEXT: номер элемента
    EXPECTED: INFO
    RISK: NONE
    GUARD: NUMBER_SIGN_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "#include <stdio.h>"
    CONTEXT: директива препроцессора C
    EXPECTED: INFO
    RISK: NONE
    GUARD: NUMBER_SIGN_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "# Заголовок"
    CONTEXT: заголовок Markdown
    EXPECTED: INFO
    RISK: NONE
    GUARD: NUMBER_SIGN_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "count = 5  # комментарий"
    CONTEXT: комментарий в Python/shell
    EXPECTED: INFO
    RISK: NONE
    GUARD: NUMBER_SIGN_FORM ≠ COMMENT_SAFETY_PROOF
  SAFE_CASE_006:
    INPUT: "https://site.com/doc#section-3"
    CONTEXT: легитимный якорь-фрагмент
    EXPECTED: INFO
    RISK: NONE
    GUARD: NUMBER_SIGN_FORM ≠ FRAGMENT_SAFETY_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: FRAGMENT_HIDES_REAL_TARGET
    INPUT: "https://good.com/login#@evil.com"
    CONTEXT: фрагмент маскирует восприятие настоящего хоста
    RISK: HIGH
    ATTACK: всё после «#» — фрагмент (клиентский); «@evil.com» в нём создаёт иллюзию/путаницу о цели
    GUARD: NUMBER_SIGN_FORM ≠ SERVER_VISIBILITY_PROOF
  RISK_CASE_002:
    NAME: URL_TRUNCATION_TRICK
    INPUT: "https://evil.com#good.com/verify"
    CONTEXT: реальный хост evil.com, «good.com» лишь во фрагменте
    RISK: HIGH
    ATTACK: глаз читает «good.com», но запрос идёт на evil.com; фрагмент не отправляется
    GUARD: NUMBER_SIGN_FORM ≠ TRUNCATION_SAFETY_PROOF
  RISK_CASE_003:
    NAME: COMMENT_INJECTION
    INPUT: "value # rm -rf /"
    CONTEXT: «#» уводит остаток строки в комментарий (или наоборот раскрывает)
    RISK: MEDIUM
    ATTACK: инъекция «#» меняет то, что интерпретатор считает кодом vs комментарием
    GUARD: NUMBER_SIGN_FORM ≠ COMMENT_SAFETY_PROOF
  RISK_CASE_004:
    NAME: SPA_ROUTE_BYPASS
    INPUT: "https://app.com/#/admin/users"
    CONTEXT: клиентский роут после «#» в обход серверной проверки
    RISK: MEDIUM
    ATTACK: «#/admin» — клиентская навигация; авторизация должна быть на сервере, не по «#»
    GUARD: NUMBER_SIGN_FORM ≠ ROUTE_SAFETY_PROOF
  RISK_CASE_005:
    NAME: HASHBANG_UPLOAD
    INPUT: "#!/bin/sh" (в начале загруженного файла)
    CONTEXT: shebang делает загруженный файл исполняемым скриптом
    RISK: HIGH
    ATTACK: «#!» в начале файла + исполняемый бит → выполнение произвольного скрипта
    GUARD: NUMBER_SIGN_FORM ≠ EXECUTION_TRIGGER
  RISK_CASE_006:
    NAME: FULLWIDTH_HASH_BYPASS
    INPUT: "＃/admin" (полноширинный ＃ U+FF03)
    CONTEXT: двойник-решётка для обхода фильтра фрагмента/роута
    RISK: LOW
    ATTACK: фильтр ищет ASCII «#», нормализатор может привести ＃ к «#»
    GUARD: NUMBER_SIGN_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ＃
    CODEPOINT: U+FF03
    NAME: FULLWIDTH NUMBER SIGN
    RISK: MEDIUM
    RULE: FULLWIDTH_NUMBER_SIGN ≠ NUMBER_SIGN (обход фильтра, ищущего ASCII «#»)
  CONFUSABLE_002:
    VISIBLE_FORM: ♯
    CODEPOINT: U+266F
    NAME: MUSIC SHARP SIGN
    RISK: LOW
    RULE: MUSIC_SHARP_SIGN ≠ NUMBER_SIGN
  CONFUSABLE_003:
    VISIBLE_FORM: ﹟
    CODEPOINT: U+FE5F
    NAME: SMALL NUMBER SIGN
    RISK: LOW
    RULE: SMALL_NUMBER_SIGN ≠ NUMBER_SIGN
  CONFUSABLE_004:
    VISIBLE_FORM: ⌗
    CODEPOINT: U+2317
    NAME: VIEWDATA SQUARE
    RISK: LOW
    RULE: VIEWDATA_SQUARE ≠ NUMBER_SIGN
  CONFUSABLE_005:
    VISIBLE_FORM: №
    CODEPOINT: U+2116
    NAME: NUMERO SIGN
    RISK: LOW
    RULE: NUMERO_SIGN ≠ NUMBER_SIGN (иной знак «номер», не ASCII «#»)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: «то, что после „#“, безопасно, ведь это лишь фрагмент»
    RESPONSE: NUMBER_SIGN_FORM ≠ FRAGMENT_SAFETY_PROOF
    RULE: фрагмент управляет клиентом (роут/скролл/DOM); не автоматически безопасен
  CG2:
    TRIGGER: «„good.com“ в URL значит запрос идёт на good.com»
    RESPONSE: NUMBER_SIGN_FORM ≠ SERVER_VISIBILITY_PROOF
    RULE: часть после «#» не отправляется; реальный хост — до «#»
  CG3:
    TRIGGER: «„#“ отмечает конец URL»
    RESPONSE: NUMBER_SIGN_FORM ≠ URL_END_MARKER_PROOF
    RULE: после «#» идёт фрагмент — это часть URL, не конец
  CG4:
    TRIGGER: «„#/admin“ безопасен, раз это клиентский роут»
    RESPONSE: NUMBER_SIGN_FORM ≠ ROUTE_SAFETY_PROOF
    RULE: авторизация должна быть серверной; клиентский роут её не заменяет
  CG5:
    TRIGGER: «„#“ в начале файла — просто комментарий»
    RESPONSE: NUMBER_SIGN_FORM ≠ EXECUTION_TRIGGER
    RULE: «#!» (shebang) + исполняемый бит делает файл скриптом
  CG6:
    TRIGGER: «фильтр по ASCII „#“ ловит все решётки»
    RESPONSE: NUMBER_SIGN_FORM ≠ EFFECT
    RULE: полноширинный ＃ (U+FF03) — другой кодпоинт

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "#@host" (фрагмент с @)
      NAME: FRAGMENT_USERINFO_CONFUSION
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: путаница о цели URL (совместно с @); фрагмент маскирует восприятие
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "#!"
      NAME: SHEBANG_OR_HASHBANG
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: shebang исполняемого файла; hashbang-роут в старых SPA
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "#/route"
      NAME: CLIENT_ROUTE
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: SPA-навигация; обход при доверии клиентскому роуту
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — последовательности с «#» ключевы для URL/исполнения.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: «#» маскирует СТРУКТУРУ URL/кода (фрагмент, комментарий, роут), но не имитирует существование проверенной сущности. Риски — обфускация/логика, не entity-mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена ASCII «#» на полноширинный ＃ (U+FF03) для обхода фильтра фрагмента
  A2: смешение «#» с ♯ (U+266F) в фильтре
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: комментарий-инъекция «value # rm -rf /»
  B2: shebang «#!/bin/sh» в начале загруженного файла
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: фрагмент «#@evil.com» (SC1) — путаница о цели URL
  C2: клиентский роут «#/admin» (SC3) в обход серверной проверки
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: URL-truncation «evil.com#good.com» — глаз читает good.com
  D2: «#verified» как псевдо-статус (инфляция доверия хэштегом)
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не носитель PHAGO; вектор: фрагмент маскирует настоящий хост
  E2: N/A — вектор: комментарий-инъекция в конфиге/скрипте
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет дремлющих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: то, что после «#», безопасно (лишь фрагмент)
  EXPECTED: FAIL_FRAGMENT_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: «good.com» в URL значит запрос идёт на good.com
  EXPECTED: FAIL_SERVER_VISIBILITY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: «#» отмечает конец URL
  EXPECTED: FAIL_URL_END_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: клиентский роут «#/admin» безопасен сам по себе
  EXPECTED: FAIL_ROUTE_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: «#» в начале файла — всегда безобидный комментарий
  EXPECTED: FAIL_SHEBANG_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: ASCII-фильтр по «#» ловит все варианты знака
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как трактовать фрагмент в контексте безопасности URL (клиент vs сервер)?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (разбор реального хоста до «#» + политика клиентских роутов — уровень интегратора)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «реальный хост — до „#“; фрагмент не отправляется на сервер».
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
