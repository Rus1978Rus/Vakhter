PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_EQUALS_SIGN_U003D_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: Русский оригинал (authoritative). Английское зеркало — SIGN_CORE_CARD_EQUALS_SIGN_U003D_GEN3_v0_3_EN. Кодпоинты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_EQUALS_SIGN_U003D_GEN3_v0_3_RU
CODEPOINT: U+003D
VISIBLE_FORM: =
UNICODE_NAME: EQUALS SIGN
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: равно / присваивание и фильтр
CATEGORY_ROADMAP: INJ (LDAP-фильтр, присваивание параметра/env) · PHAGO: — (подделка ключ-значение)

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
VISIBLE_FORM: =
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: EQUALS_SIGN_FORM ≠ EFFECT
SIGN_CATEGORY:
  - оператор присваивания (x = 1) / сравнение (a == b)
  - разделитель ключ-значение (URL-запрос, cookie, env, конфиг)
  - равенство в LDAP-фильтре (cn=value)
  - паддинг Base64 / математическое равенство в тексте

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_EQUALITY_ONLY — "=" не всегда математическое равенство (он присваивает/фильтрует/связывает)
  2. NOT_ASSIGN_SAFE — присваивание может перезаписать доверенный ключ (параметр/env/конфиг)
  3. NOT_KV_SCOPED — лишний "=" может расщепить значение в неожиданную пару ключ-значение
  4. NOT_ESCAPED_PROOF — наличие "=" не значит, что он закавычен/экранирован
  5. NOT_ENCODED_SAFE — "%3D" может быть раскодирован обратно в "=" позже
  6. NOT_AUTHORITY — "=" не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сам по себе ничего не исполняет; связывание делает контекст
  8. NOT_TRUST_SIGNAL — не повышает доверие
  9. NOT_LDAP_FILTER_SAFE — "=" строит равенство LDAP, которое можно расширить/внедрить
  10. NOT_SANITIZED_PROOF — наличие "=" не значит, что ввод санитизирован
  11. NOT_OUTPUT_CONTEXT_PROOF — безопасность зависит от контекста разбора/связывания

BASE_FORMULAS:
  EQUALS_SIGN_FORM ≠ EFFECT
  EQUALS_SIGN_FORM ≠ EQUALITY_ONLY_PROOF
  EQUALS_SIGN_FORM ≠ ASSIGN_SAFETY_PROOF
  EQUALS_SIGN_FORM ≠ KV_SCOPE_PROOF
  EQUALS_SIGN_FORM ≠ ESCAPED_PROOF
  EQUALS_SIGN_FORM ≠ ENCODED_SAFETY_PROOF
  EQUALS_SIGN_FORM ≠ AUTHORITY
  EQUALS_SIGN_FORM ≠ EXECUTION_TRIGGER
  EQUALS_SIGN_FORM ≠ LDAP_FILTER_SAFETY_PROOF
  EQUALS_SIGN_FORM ≠ SANITIZED_PROOF
  EQUALS_SIGN_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: "=" (ZONE_1) имеет параллельные функции (математическое равенство, присваивание, разделитель ключ-значение, равенство LDAP, паддинг Base64), сосуществующие без культурной прецессии. Полисемия стабильного знака.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1
  NOTE: математический знак без жестового предшественника; функции присваивания/связывания/фильтра надстроены цифровой эпохой параллельно.

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
    INPUT: "2 + 2 = 4"
    CONTEXT: математическое равенство в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: EQUALS_SIGN_FORM ≠ EQUALITY_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: "let x = 10"
    CONTEXT: присваивание в примере кода (как литеральный текст)
    EXPECTED: INFO
    RISK: NONE
    GUARD: EQUALS_SIGN_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "?page=1"
    CONTEXT: обычная пара ключ-значение URL
    EXPECTED: INFO
    RISK: NONE
    GUARD: EQUALS_SIGN_FORM ≠ KV_SCOPE_PROOF
  SAFE_CASE_004:
    INPUT: "if (a == b)"
    CONTEXT: сравнение в коде
    EXPECTED: INFO
    RISK: NONE
    GUARD: EQUALS_SIGN_FORM ≠ EQUALITY_ONLY_PROOF
  SAFE_CASE_005:
    INPUT: "dGVzdA== (паддинг Base64)"
    CONTEXT: "=" как паддинг Base64
    EXPECTED: INFO
    RISK: NONE
    GUARD: EQUALS_SIGN_FORM ≠ EFFECT
  SAFE_CASE_006:
    INPUT: "color=red in a config line"
    CONTEXT: безобидная запись конфига ключ-значение
    EXPECTED: INFO
    RISK: NONE
    GUARD: EQUALS_SIGN_FORM ≠ ASSIGN_SAFETY_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: LDAP_EQUALITY_INJECTION
    INPUT: "cn=admin)(|(password=*"
    CONTEXT: "=", строящий внедрённое равенство/фильтр LDAP
    RISK: CRITICAL
    ATTACK: "=" плюс синтаксис фильтра внедряет логику LDAP (обход аутентификации / раскрытие данных)
    GUARD: EQUALS_SIGN_FORM ≠ LDAP_FILTER_SAFETY_PROOF
  RISK_CASE_002:
    NAME: PARAMETER_KEY_INJECTION
    INPUT: "name=x&isAdmin=true"
    CONTEXT: внедрённый "=", подделывающий лишний параметр ключ-значение
    RISK: HIGH
    ATTACK: "=" определяет новый ключ (isAdmin), который бэкенд может соблюсти (смена привилегий)
    GUARD: EQUALS_SIGN_FORM ≠ KV_SCOPE_PROOF
  RISK_CASE_003:
    NAME: ENV_VAR_INJECTION
    INPUT: "value\\nLD_PRELOAD=/tmp/evil.so"
    CONTEXT: внедрённый "=", определяющий опасную переменную окружения
    RISK: HIGH
    ATTACK: "=" связывает подконтрольную атакующему env-переменную, меняющую поведение рантайма
    GUARD: EQUALS_SIGN_FORM ≠ ASSIGN_SAFETY_PROOF
  RISK_CASE_004:
    NAME: SQL_ALWAYS_TRUE
    INPUT: "' OR 1=1 -- "
    CONTEXT: "=", строящий всегда-истинное условие SQL
    RISK: HIGH
    ATTACK: "1=1" делает условие WHERE всегда совпадающим (обход аутентификации)
    GUARD: EQUALS_SIGN_FORM ≠ EFFECT
  RISK_CASE_005:
    NAME: ENCODED_EQUALS_BYPASS
    INPUT: "cn%3Dadmin (с поздним декодированием)"
    CONTEXT: кодированный "=" декодируется обратно перед фильтром/парсером
    RISK: MEDIUM
    ATTACK: %3D декодируется в "=" ПОСЛЕ проверки → связывание ключ-значение/фильтр
    GUARD: EQUALS_SIGN_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_EQUALS_BYPASS
    INPUT: "cn＝admin (полноширинный ＝ U+FF1D)"
    CONTEXT: похожий знак для обхода фильтра "="
    RISK: MEDIUM
    ATTACK: фильтр ищет ASCII "=", нормализатор может свернуть ＝ в "="
    GUARD: EQUALS_SIGN_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ＝
    CODEPOINT: U+FF1D
    NAME: FULLWIDTH EQUALS SIGN
    RISK: HIGH
    RULE: FULLWIDTH_EQUALS_SIGN ≠ EQUALS_SIGN (обходит фильтр, ищущий ASCII "=")
  CONFUSABLE_002:
    VISIBLE_FORM: ﹦
    CODEPOINT: U+FE66
    NAME: SMALL EQUALS SIGN
    RISK: MEDIUM
    RULE: SMALL_EQUALS_SIGN ≠ EQUALS_SIGN
  CONFUSABLE_003:
    VISIBLE_FORM: ꞊
    CODEPOINT: U+A78A
    NAME: MODIFIER LETTER SHORT EQUALS SIGN
    RISK: MEDIUM
    RULE: MODIFIER_SHORT_EQUALS ≠ EQUALS_SIGN
  CONFUSABLE_004:
    VISIBLE_FORM: ⩵
    CODEPOINT: U+2A75
    NAME: TWO CONSECUTIVE EQUALS SIGNS
    RISK: LOW
    RULE: TWO_CONSECUTIVE_EQUALS ≠ EQUALS_SIGN (единый глиф, похожий на "==")
  CONFUSABLE_005:
    VISIBLE_FORM: ═
    CODEPOINT: U+2550
    NAME: BOX DRAWINGS DOUBLE HORIZONTAL
    RISK: LOW
    RULE: BOX_DOUBLE_HORIZONTAL ≠ EQUALS_SIGN (только визуальное перекрытие)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "'=' — это всегда математическое равенство"
    RESPONSE: EQUALS_SIGN_FORM ≠ EQUALITY_ONLY_PROOF
    RULE: "=" присваивает, связывает ключ-значения и строит фильтры LDAP/SQL
  CG2:
    TRIGGER: "присваивание не может быть опасным"
    RESPONSE: EQUALS_SIGN_FORM ≠ ASSIGN_SAFETY_PROOF
    RULE: "=" может перезаписать доверенный ключ или связать опасную env-переменную
  CG3:
    TRIGGER: "'=' в LDAP просто проверяет равенство"
    RESPONSE: EQUALS_SIGN_FORM ≠ LDAP_FILTER_SAFETY_PROOF
    RULE: "=" плюс синтаксис фильтра внедряет логику (обход аутентификации)
  CG4:
    TRIGGER: "'%3D' безопасен навсегда"
    RESPONSE: EQUALS_SIGN_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в "=" перед парсером
  CG5:
    TRIGGER: "фильтр по ASCII '=' ловит все знаки равно"
    RESPONSE: EQUALS_SIGN_FORM ≠ EFFECT
    RULE: полноширинный ＝ (U+FF1D) и малый ﹦ (U+FE66) — другие кодпоинты
  CG6:
    TRIGGER: "наличие '=' значит, что ввод санитизирован"
    RESPONSE: EQUALS_SIGN_FORM ≠ SANITIZED_PROOF
    RULE: наличие знака ничего не говорит о санитизации

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "=*"
      NAME: LDAP_PRESENCE_WILDCARD
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: равенство, превращённое в присутствие/любое совпадение
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "&key="
      NAME: PARAM_KEY_INJECTION
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: внедрение лишнего параметра ключ-значение
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "1=1"
      NAME: ALWAYS_TRUE
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: всегда-истинное условие в SQL/фильтрах
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — последовательности с "=" центральны для инъекции фильтра/ключ-значение.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: "=" связывает ключ-значения или строит фильтры, но не имитирует существование верифицированной сущности. Его риски — инъекция присваивания/фильтра, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена ASCII "=" на полноширинный ＝ (U+FF1D) для обхода фильтра
  A2: замена на малый ﹦ (U+FE66)
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: инъекция равенства LDAP cn=admin)(|(password=*
  B2: инъекция ключа HTTP-параметра name=x&isAdmin=true
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "=*" (SC1) — присутствие/wildcard LDAP
  C2: "1=1" (SC3) — всегда-истинное условие
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: "=" подан как безобидное математическое равенство внутри поля фильтра
  D2: "%3D" как «безопасный» кодированный текст с поздним декодированием
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: связывание env-переменной в запуск процесса
  E2: N/A — вектор: инъекция поддельного ключ-значение в парсер параметров
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: "=" — всегда математическое равенство
  EXPECTED: FAIL_EQUALITY_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: присваивание не может быть опасным
  EXPECTED: FAIL_ASSIGN_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: "=" в LDAP просто проверяет равенство
  EXPECTED: FAIL_LDAP_FILTER_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%3D" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: фильтр по ASCII "=" ловит все похожие знаки равно
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: наличие "=" доказывает санитизацию ввода
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как экранировать "=" по контексту (LDAP/запрос/env/SQL) без ложных срабатываний на математике/присваивании/Base64?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (экранирование LDAP-фильтра + строгий разбор параметров + allow-list env + параметризованные запросы — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «безопасность '=' решается контекстом разбора/связывания».
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
