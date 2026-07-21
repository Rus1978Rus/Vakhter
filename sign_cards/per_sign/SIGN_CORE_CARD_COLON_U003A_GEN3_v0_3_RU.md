ЧАСТНЫЙ АВТОРСКИЙ ПРОЕКТ / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_COLON_U003A_GEN3_v0_3_RU
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
CARD_UID: SIGN_CORE_CARD_COLON_U003A_GEN3_v0_3_RU
CODEPOINT: U+003A
VISIBLE_FORM: :
UNICODE_NAME: COLON
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: двоеточие
CATEGORY_ROADMAP: PH (путаница порт/схема) · PHAGO: ○ (частичный — схема-URI может внушать «официальный» ресурс)

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
VISIBLE_FORM: :
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_SEPARATOR
BASE_MODE_FORMULA: COLON_FORM ≠ EFFECT
SIGN_CATEGORY:
  - пунктуация (пояснение, перечисление)
  - разделитель времени (12:30) и отношения (3:1)
  - разделитель ключ-значение (key: value)
  - разделитель схемы URI (http:, javascript:, data:)
  - разделитель хост:порт и логин:пароль в URL
  - разделитель пространства имён (namespace::member)

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_SCHEME_SAFE — двоеточие в «scheme:» не делает саму схему безопасной (javascript:, data:)
  2. NOT_PORT_VALIDITY_PROOF — «host:port» не подтверждает корректность/безопасность порта
  3. NOT_TIME_PROOF — двоеточие не гарантирует, что «12:99» валидное время
  4. NOT_KEYVALUE_PROOF — «key:value» не подтверждает корректность пары
  5. NOT_CREDENTIAL_PROOF — «user:pass» не верифицирует учётные данные
  6. NOT_AUTHORITY — двоеточие не подтверждает официальность
  7. NOT_URL_STRUCTURE_PROOF — присутствие «:» не доказывает валидную структуру URL
  8. NOT_EXECUTION_TRIGGER — двоеточие само по себе не исполняет (исполняет схема javascript:)
  9. NOT_TRUST_SIGNAL — не повышает доверие
  10. NOT_ALWAYS_SEPARATOR — «::» может быть IPv6/пространством имён, не парой
  11. NOT_SCHEME_PRESENCE_PROOF — «:» без валидной схемы перед ним — не схема

BASE_FORMULAS:
  COLON_FORM ≠ EFFECT
  COLON_FORM ≠ SCHEME_SAFETY_PROOF
  COLON_FORM ≠ PORT_VALIDITY_PROOF
  COLON_FORM ≠ TIME_VALIDITY_PROOF
  COLON_FORM ≠ KEYVALUE_VALIDITY_PROOF
  COLON_FORM ≠ CREDENTIAL_PROOF
  COLON_FORM ≠ AUTHORITY
  COLON_FORM ≠ URL_STRUCTURE_PROOF
  COLON_FORM ≠ EXECUTION_TRIGGER
  COLON_FORM ≠ TRUST_SIGNAL
  COLON_FORM ≠ SCHEME_PRESENCE_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: «:» (ZONE_1) имеет параллельные функции (пунктуация, время, отношение, ключ-значение, схема, хост:порт), сосуществующие без культурной прецессии. Полисемия стабильного знака.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1
  NOTE: письменный знак пунктуации без жестового предшественника; URI-функция наложена цифровой эпохой параллельно.

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
    INPUT: "встреча в 12:30"
    CONTEXT: разделитель времени
    EXPECTED: INFO
    RISK: NONE
    GUARD: COLON_FORM ≠ TIME_VALIDITY_PROOF
  SAFE_CASE_002:
    INPUT: "соотношение 3:1"
    CONTEXT: отношение
    EXPECTED: INFO
    RISK: NONE
    GUARD: COLON_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "name: Ivan"
    CONTEXT: пара ключ-значение (YAML/JSON-подобное)
    EXPECTED: INFO
    RISK: NONE
    GUARD: COLON_FORM ≠ KEYVALUE_VALIDITY_PROOF
  SAFE_CASE_004:
    INPUT: "Важно: прочитать до конца"
    CONTEXT: пунктуационное пояснение
    EXPECTED: INFO
    RISK: NONE
    GUARD: COLON_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "https://example.com"
    CONTEXT: легитимная схема URL
    EXPECTED: INFO
    RISK: NONE
    GUARD: COLON_FORM ≠ SCHEME_SAFETY_PROOF
  SAFE_CASE_006:
    INPUT: "std::vector<int>"
    CONTEXT: разделитель пространства имён в C++
    EXPECTED: INFO
    RISK: NONE
    GUARD: COLON_FORM ≠ ALWAYS_SEPARATOR

RISK_CASES:
  RISK_CASE_001:
    NAME: JAVASCRIPT_SCHEME_INJECTION
    INPUT: "javascript:alert(document.cookie)"
    CONTEXT: опасная схема в href/ссылке
    RISK: CRITICAL
    ATTACK: схема javascript: исполняет код при переходе; двоеточие — разделитель схемы, но исполняет СХЕМА, не «:»
    GUARD: COLON_FORM ≠ SCHEME_SAFETY_PROOF
  RISK_CASE_002:
    NAME: DATA_URI_PAYLOAD
    INPUT: "data:text/html,<script>...</script>"
    CONTEXT: data-URI с активным содержимым
    RISK: HIGH
    ATTACK: data: встраивает исполняемый/HTML-контент в «ссылку»
    GUARD: COLON_FORM ≠ URL_STRUCTURE_PROOF
  RISK_CASE_003:
    NAME: PORT_REDIRECT_CONFUSION
    INPUT: "http://trusted.com:evil.com/"
    CONTEXT: путаница хост:порт для маскировки настоящего хоста
    RISK: HIGH
    ATTACK: нестандартная позиция «:» путает наивный парсер URL о реальном хосте/порте
    GUARD: COLON_FORM ≠ PORT_VALIDITY_PROOF
  RISK_CASE_004:
    NAME: CREDENTIALS_IN_URL
    INPUT: "http://user:pass@evil.com"
    CONTEXT: логин:пароль в userinfo (совместно с @)
    RISK: MEDIUM
    ATTACK: «:» разделяет учётные данные, всё до «@» — userinfo; реальный хост evil.com
    GUARD: COLON_FORM ≠ CREDENTIAL_PROOF
  RISK_CASE_005:
    NAME: FILE_SCHEME_LOCAL_READ
    INPUT: "file:///etc/passwd"
    CONTEXT: схема file: для чтения локального ресурса
    RISK: HIGH
    ATTACK: схема file: уводит запрос к локальной ФС
    GUARD: COLON_FORM ≠ SCHEME_SAFETY_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_COLON_BYPASS
    INPUT: "javascript：alert(1)" (полноширинное ： U+FF1A)
    CONTEXT: двойник-двоеточие для обхода фильтра схем
    RISK: MEDIUM
    ATTACK: фильтр ищет ASCII «:», а нормализатор/браузер может привести ： к «:»
    GUARD: COLON_FORM ≠ EFFECT (см. CONFUSABLES)

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ：
    CODEPOINT: U+FF1A
    NAME: FULLWIDTH COLON
    RISK: HIGH
    RULE: FULLWIDTH_COLON ≠ COLON (обход фильтра схем/портов, ищущего ASCII «:»)
  CONFUSABLE_002:
    VISIBLE_FORM: ∶
    CODEPOINT: U+2236
    NAME: RATIO
    RISK: MEDIUM
    RULE: RATIO ≠ COLON (математическое отношение, другой кодпоинт)
  CONFUSABLE_003:
    VISIBLE_FORM: ꞉
    CODEPOINT: U+A789
    NAME: MODIFIER LETTER COLON
    RISK: MEDIUM
    RULE: MODIFIER_COLON ≠ COLON
  CONFUSABLE_004:
    VISIBLE_FORM: ˸
    CODEPOINT: U+02F8
    NAME: MODIFIER LETTER RAISED COLON
    RISK: LOW
    RULE: RAISED_COLON ≠ COLON
  CONFUSABLE_005:
    VISIBLE_FORM: ։
    CODEPOINT: U+0589
    NAME: ARMENIAN FULL STOP
    RISK: LOW
    RULE: ARMENIAN_FULL_STOP ≠ COLON (визуально схож с двоеточием)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: «раз есть „scheme:“, ссылка безопасна»
    RESPONSE: COLON_FORM ≠ SCHEME_SAFETY_PROOF
    RULE: javascript:/data:/file: — опасные схемы; безопасность определяет схема, не «:»
  CG2:
    TRIGGER: «„host:port“ всегда корректный хост и порт»
    RESPONSE: COLON_FORM ≠ PORT_VALIDITY_PROOF
    RULE: позиция «:» может путать парсер о реальном хосте/порте
  CG3:
    TRIGGER: «„12:99“ — валидное время, раз есть двоеточие»
    RESPONSE: COLON_FORM ≠ TIME_VALIDITY_PROOF
    RULE: разделитель не проверяет диапазон компонентов
  CG4:
    TRIGGER: «„user:pass@host“ — доверенные учётные данные»
    RESPONSE: COLON_FORM ≠ CREDENTIAL_PROOF
    RULE: «:» лишь разделяет; всё до «@» это userinfo, реальный хост после «@»
  CG5:
    TRIGGER: «фильтр по ASCII „:“ ловит все схемы»
    RESPONSE: COLON_FORM ≠ EFFECT
    RULE: полноширинное ： (U+FF1A) — другой кодпоинт; нормализатор может привести его к «:»
  CG6:
    TRIGGER: «наличие „:“ доказывает валидный URL»
    RESPONSE: COLON_FORM ≠ URL_STRUCTURE_PROOF
    RULE: «:» есть во времени, отношении, ключ-значении; это не признак валидного URL

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "://"
      NAME: SCHEME_AUTHORITY_SEPARATOR
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: разделитель схемы и authority; сам по себе легит-связка (URL_CONTEXT), но включает более строгий анализ @ и точки далее (см. легаси SOLIDUS_SCHEME_PATCH)
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "::"
      NAME: DOUBLE_COLON
      RISK_LEVEL: LOW
      POSSIBLE_CONTEXTS: IPv6-сокращение, пространство имён C++, YAML — обычно легит
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "scheme:payload" (без //)
      NAME: OPAQUE_SCHEME
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: javascript:/data:/file: — непрозрачные схемы без authority, частый вектор
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — последовательности с «:» ключевы для URL-структуры.

PHAGO_ENTITY_MIMICRY:
  PE_001:
    INPUT: "http://microsoft.com:login@evil.com"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: MEDIUM
    NOTE: «:» совместно с «@» помогает выстроить строку, где бренд стоит в userinfo, внушая «официальный» ресурс. Частичный (○) PHAGO — усиливает entity-mimicry знака @, но сам по себе маскирует структуру.
  PE_002:
    INPUT: "javascript:/* официальный портал */alert(1)"
    TYPE: SEMANTIC_AMBIGUITY (not PHAGO)
    RISK: LOW
    NOTE: комментарий-приманка не есть имитация проверенной сущности; помечено как неоднозначность, не PHAGO.

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена ASCII «:» на полноширинное ： (U+FF1A) в схеме javascript：
  A2: смешение «:» с RATIO (U+2236) для обхода парсера
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: javascript:/data: схема в href/поле URL
  B2: userinfo user:pass@evil.com (совместно с @)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: opaque-схема scheme:payload без // (SC3)
  C2: путаница host:port (http://trusted.com:evil.com/)
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: file:///etc/passwd — локальное чтение под видом «ссылки»
  D2: «Важно:» как псевдо-авторитетное пояснение (инфляция значимости)
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: бренд в userinfo через «:»+«@» (PE_001)
  E2: схема-приманка с «официальным» комментарием (граничный случай, помечен как неоднозначность)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет дремлющих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: наличие «scheme:» делает ссылку безопасной
  EXPECTED: FAIL_SCHEME_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: «host:port» гарантирует корректный хост и порт
  EXPECTED: FAIL_PORT_VALIDITY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: «12:99» — валидное время, раз есть двоеточие
  EXPECTED: FAIL_TIME_VALIDITY_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: «user:pass@host» — доверенные учётные данные
  EXPECTED: FAIL_CREDENTIAL_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: ASCII-фильтр по «:» ловит все схемы
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: наличие «:» доказывает валидный URL
  EXPECTED: FAIL_URL_STRUCTURE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как различать opaque-схему (javascript:/data:) и легит scheme:// без ложных срабатываний на «12:30»/«key:value»?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (валидация схемы RFC 3986 §3.1 + allowlist безопасных схем — уровень интегратора; ср. легаси SOLIDUS_SCHEME_PATCH)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует формулы и правило «безопасность определяет схема, не двоеточие».
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
