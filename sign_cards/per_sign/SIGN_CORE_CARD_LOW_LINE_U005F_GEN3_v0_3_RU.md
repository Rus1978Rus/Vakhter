ЧАСТНЫЙ АВТОРСКИЙ ПРОЕКТ / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_LOW_LINE_U005F_GEN3_v0_3_RU
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
CARD_UID: SIGN_CORE_CARD_LOW_LINE_U005F_GEN3_v0_3_RU
CODEPOINT: U+005F
VISIBLE_FORM: _
UNICODE_NAME: LOW LINE
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: подчёркивание (underscore)
CATEGORY_ROADMAP: PH (фейковые поддомены, двойники-разделители) · PHAGO: ○ (частичный — фейк-поддомен может внушать официальную субсущность)

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
VISIBLE_FORM: _
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_CONNECTOR
BASE_MODE_FORMULA: LOW_LINE_FORM ≠ EFFECT
SIGN_CATEGORY:
  - соединитель идентификаторов (snake_case, user_name)
  - выделение курсивом в Markdown (_курсив_)
  - wildcard одного символа в SQL LIKE (a_c)
  - служебные DNS-метки (_dmarc, _acme-challenge)
  - псевдо-разделитель в домене/хосте (визуальный, не DNS-иерархия)

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_SUBDOMAIN — «_» не создаёт поддомен и не меняет регистрируемый домен
  2. NOT_BRAND_AFFILIATION — «paypal_secure» не делает строку частью бренда
  3. NOT_HOSTNAME_VALIDITY — «_» формально не валиден в hostname (RFC 1123), но встречается
  4. NOT_WILDCARD_SAFE — «_» в SQL LIKE совпадает с любым одним символом
  5. NOT_EMPHASIS_SAFE — «_текст_» (Markdown) не гарантирует безопасность содержимого
  6. NOT_AUTHORITY — «_» не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сам по себе ничего не исполняет
  8. NOT_TRUST_SIGNAL — не повышает доверие
  9. NOT_WORD_BOUNDARY_GUARANTEE — «_» не всегда граница слова (часто внутри токена)
  10. NOT_SEPARATOR_UNIQUENESS — «user_id» и «user__id» — разные идентификаторы
  11. NOT_IDENTIFIER_VALIDITY_PROOF — «_» не подтверждает существование/права идентификатора

BASE_FORMULAS:
  LOW_LINE_FORM ≠ EFFECT
  LOW_LINE_FORM ≠ SUBDOMAIN_PROOF
  LOW_LINE_FORM ≠ BRAND_AFFILIATION
  LOW_LINE_FORM ≠ HOSTNAME_VALIDITY_PROOF
  LOW_LINE_FORM ≠ WILDCARD_SAFETY_PROOF
  LOW_LINE_FORM ≠ EMPHASIS_SAFETY_PROOF
  LOW_LINE_FORM ≠ AUTHORITY
  LOW_LINE_FORM ≠ TRUST_SIGNAL
  LOW_LINE_FORM ≠ WORD_BOUNDARY_PROOF
  LOW_LINE_FORM ≠ SEPARATOR_UNIQUENESS_PROOF
  LOW_LINE_FORM ≠ IDENTIFIER_VALIDITY_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: «_» (ZONE_1) имеет параллельные функции (соединитель, курсив, wildcard, DNS-метка), сосуществующие без культурной прецессии. Полисемия стабильного знака.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1
  NOTE: письменный знак (низкая линия/подчёркивание) без жестового предшественника; функции идентификаторов/DNS наложены цифровой эпохой параллельно.

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
    INPUT: "user_name"
    CONTEXT: snake_case идентификатор
    EXPECTED: INFO
    RISK: NONE
    GUARD: LOW_LINE_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "MAX_BUFFER_SIZE"
    CONTEXT: константа UPPER_SNAKE
    EXPECTED: INFO
    RISK: NONE
    GUARD: LOW_LINE_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "_курсив_"
    CONTEXT: выделение Markdown
    EXPECTED: INFO
    RISK: NONE
    GUARD: LOW_LINE_FORM ≠ EMPHASIS_SAFETY_PROOF
  SAFE_CASE_004:
    INPUT: "def __init__(self)"
    CONTEXT: dunder-метод Python
    EXPECTED: INFO
    RISK: NONE
    GUARD: LOW_LINE_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "SELECT * WHERE code LIKE 'a_c'"
    CONTEXT: намеренный wildcard одного символа
    EXPECTED: INFO
    RISK: NONE
    GUARD: LOW_LINE_FORM ≠ WILDCARD_SAFETY_PROOF
  SAFE_CASE_006:
    INPUT: "_dmarc.example.com"
    CONTEXT: легитимная служебная DNS-метка
    EXPECTED: INFO
    RISK: NONE
    GUARD: LOW_LINE_FORM ≠ HOSTNAME_VALIDITY_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: FAKE_SUBDOMAIN_SEPARATOR
    INPUT: "paypal_com.evil.ru"
    CONTEXT: «_» имитирует точку-разделитель, внушая поддомен бренда
    RISK: HIGH
    ATTACK: «paypal_com» выглядит как поддомен PayPal; регистрируемый домен — evil.ru
    GUARD: LOW_LINE_FORM ≠ SUBDOMAIN_PROOF
  RISK_CASE_002:
    NAME: SQL_LIKE_WILDCARD_BYPASS
    INPUT: "username LIKE 'admin_'"
    CONTEXT: «_» как wildcard совпадает с admin1/adminX
    RISK: HIGH
    ATTACK: неэкранированный «_» в LIKE расширяет совпадение за пределы ожидаемого
    GUARD: LOW_LINE_FORM ≠ WILDCARD_SAFETY_PROOF
  RISK_CASE_003:
    NAME: FAKE_AFFILIATED_LABEL
    INPUT: "login_secure_bank.example"
    CONTEXT: цепочка «_» внушает официальную субсущность
    RISK: MEDIUM
    ATTACK: «_»-разделители собирают «служебное» имя, имитирующее аффилиацию
    GUARD: LOW_LINE_FORM ≠ BRAND_AFFILIATION
  RISK_CASE_004:
    NAME: DNS_LABEL_SPOOF
    INPUT: "_dmarc.paypal.com.evil.ru"
    CONTEXT: служебная метка в спуф-домене для доверия
    RISK: MEDIUM
    ATTACK: «_dmarc/_acme» перед доменом-двойником имитирует легит-инфраструктуру
    GUARD: LOW_LINE_FORM ≠ IDENTIFIER_VALIDITY_PROOF
  RISK_CASE_005:
    NAME: IDENTIFIER_COLLISION
    INPUT: "user__id vs user_id"
    CONTEXT: двойной «_» создаёт похожий, но иной идентификатор
    RISK: LOW
    ATTACK: визуально близкие имена ведут к разным сущностям/полям
    GUARD: LOW_LINE_FORM ≠ SEPARATOR_UNIQUENESS_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_UNDERSCORE_BYPASS
    INPUT: "paypal＿com" (полноширинное ＿ U+FF3F)
    CONTEXT: двойник-подчёркивание для обхода фильтра
    RISK: LOW
    ATTACK: фильтр ищет ASCII «_», нормализатор может привести ＿ к «_»
    GUARD: LOW_LINE_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ＿
    CODEPOINT: U+FF3F
    NAME: FULLWIDTH LOW LINE
    RISK: MEDIUM
    RULE: FULLWIDTH_LOW_LINE ≠ LOW_LINE (обход фильтра, ищущего ASCII «_»)
  CONFUSABLE_002:
    VISIBLE_FORM: ﹍
    CODEPOINT: U+FE4D
    NAME: DASHED LOW LINE
    RISK: LOW
    RULE: DASHED_LOW_LINE ≠ LOW_LINE
  CONFUSABLE_003:
    VISIBLE_FORM: ﹎
    CODEPOINT: U+FE4E
    NAME: CENTRELINE LOW LINE
    RISK: LOW
    RULE: CENTRELINE_LOW_LINE ≠ LOW_LINE
  CONFUSABLE_004:
    VISIBLE_FORM: ﹏
    CODEPOINT: U+FE4F
    NAME: WAVY LOW LINE
    RISK: LOW
    RULE: WAVY_LOW_LINE ≠ LOW_LINE
  CONFUSABLE_005:
    VISIBLE_FORM: ‿
    CODEPOINT: U+203F
    NAME: UNDERTIE
    RISK: LOW
    RULE: UNDERTIE ≠ LOW_LINE

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: «„paypal_com“ — поддомен PayPal»
    RESPONSE: LOW_LINE_FORM ≠ SUBDOMAIN_PROOF
    RULE: «_» не разделитель DNS-иерархии; регистрируемый домен решает DNS
  CG2:
    TRIGGER: «„_“ в LIKE — просто символ подчёркивания»
    RESPONSE: LOW_LINE_FORM ≠ WILDCARD_SAFETY_PROOF
    RULE: в SQL LIKE «_» совпадает с любым одним символом; экранировать при литеральном смысле
  CG3:
    TRIGGER: «составное имя через „_“ подтверждает организацию»
    RESPONSE: LOW_LINE_FORM ≠ BRAND_AFFILIATION
    RULE: соединение через «_» — орфография идентификатора, не верификация сущности
  CG4:
    TRIGGER: «„user_id“ и „user__id“ — одно и то же»
    RESPONSE: LOW_LINE_FORM ≠ SEPARATOR_UNIQUENESS_PROOF
    RULE: разное число «_» → разные идентификаторы
  CG5:
    TRIGGER: «„_dmarc“ доказывает легит-инфраструктуру домена»
    RESPONSE: LOW_LINE_FORM ≠ IDENTIFIER_VALIDITY_PROOF
    RULE: служебная метка не подтверждает подлинность родительского домена
  CG6:
    TRIGGER: «фильтр по ASCII „_“ ловит все подчёркивания»
    RESPONSE: LOW_LINE_FORM ≠ EFFECT
    RULE: полноширинное ＿ (U+FF3F) — другой кодпоинт

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "brand_word.tld"
      NAME: FAKE_SUBDOMAIN_LABEL
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: «_» имитирует точку-разделитель поддомена (фишинг)
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "__dunder__"
      NAME: DOUBLE_UNDERSCORE
      RISK_LEVEL: LOW
      POSSIBLE_CONTEXTS: dunder-имена Python; обычно легит, но возможна коллизия имён
      REQUIRES_SEQUENCE_INTEGRATOR: NO
    SC3:
      SEQUENCE: "a_c (в LIKE)"
      NAME: LIKE_WILDCARD
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: неэкранированный wildcard в SQL LIKE
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — последовательности с «_» значимы (домен/SQL).

PHAGO_ENTITY_MIMICRY:
  PE_001:
    INPUT: "paypal_com.evil.ru"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: MEDIUM
    NOTE: «_» имитирует разделитель поддомена, внушая официальную субсущность бренда (напр. «paypal_com»). Частичный (○) PHAGO — маскировка структуры с элементом entity-mimicry.
  PE_002:
    INPUT: "support_official_paypal.example"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: MEDIUM
    NOTE: цепочка «_» собирает «официальную» служебную сущность бренда.

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена ASCII «_» на полноширинное ＿ (U+FF3F) для обхода фильтра
  A2: смешение «_» с ﹍ (U+FE4D) в фильтре
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: неэкранированный «_» как wildcard в SQL LIKE (admin_)
  B2: служебная DNS-метка «_dmarc» перед доменом-двойником
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: фейк-поддомен «brand_word.tld» (SC1)
  C2: коллизия «user__id» vs «user_id»
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: «login_secure_bank» — псевдо-служебное имя
  D2: «__verified__» как псевдо-статус (инфляция доверия)
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: «paypal_com.evil.ru» — имитация субсущности бренда (PE_001)
  E2: «support_official_paypal» — имитация служебной сущности (PE_002)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет дремлющих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: «paypal_com» — поддомен PayPal
  EXPECTED: FAIL_SUBDOMAIN_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: «_» в SQL LIKE — просто литеральное подчёркивание
  EXPECTED: FAIL_WILDCARD_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: составное имя через «_» подтверждает организацию
  EXPECTED: FAIL_ENTITY_EXISTENCE_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: «user_id» и «user__id» — один идентификатор
  EXPECTED: FAIL_SEPARATOR_UNIQUENESS_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: «_dmarc» доказывает легит-инфраструктуру домена
  EXPECTED: FAIL_IDENTIFIER_VALIDITY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: ASCII-фильтр по «_» ловит все варианты знака
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как отличать фейк-поддомен с «_» от легит-DNS-метки (_dmarc) без ложных срабатываний?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (разбор регистрируемого домена + allowlist служебных меток — уровень интегратора)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «„_“ не разделитель DNS-иерархии».
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
