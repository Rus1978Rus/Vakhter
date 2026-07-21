ЧАСТНЫЙ АВТОРСКИЙ ПРОЕКТ / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_SMALL_ROMAN_FIFTY_U217C_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
DRAFT_NOTE: черновик для нашей работы (Vakhter). Русская версия авторитетна; EN — зеркало. Знак-гомоглиф: ядро — LOOKS_SAME ≠ IS_SAME.

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
CARD_UID: SIGN_CORE_CARD_SMALL_ROMAN_FIFTY_U217C_GEN3_v0_3_RU
CODEPOINT: U+217C
VISIBLE_FORM: ⅼ
UNICODE_NAME: SMALL ROMAN NUMERAL FIFTY
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: малая римская 50 (гомоглиф латинской l)
CATEGORY_ROADMAP: PH (римская цифра-двойник 'l') · PHAGO: ○ (частичный — реже, но имитирует букву имени бренда)

============================================================
3. REQUIRED_GENERAL_GUARDS
============================================================
REQUIRED_GENERAL_GUARDS:
  - SIGN_FALSE_EFFECT_MIMICRY_GUARD_v0_2A_RU
    GUARD_COMPATIBILITY: применим — знак не создаёт effect-полей; для гомоглифа гард дополняется проверкой смешения на уровне интегратора
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
VISIBLE_FORM: ⅼ
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_NUMERAL_HOMOGLYPH
BASE_MODE_FORMULA: ROMAN_FIFTY_FORM ≠ LATIN_L
SIGN_CATEGORY:
  - римская цифра «50» (легитимна в римской нумерации)
  - гомоглиф латинской строчной «l» (U+006C)
  - потенциальный носитель homoglyph-спуфинга (буква имени бренда)

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_LATIN_L — ⅼ (U+217C) это НЕ латинская l (U+006C); другой кодпоинт
  2. NOT_SAME_STRING_AS_LATIN — строка с ⅼ машинно не равна латинскому двойнику
  3. NOT_BRAND_NAME_PROOF — «paypaⅼ» не доказывает связь с брендом PayPal
  4. NOT_DOMAIN_VALIDITY_PROOF — визуальное совпадение домена не подтверждает регистрируемый домен
  5. NOT_AUTHORITY — символ не подтверждает официальный статус
  6. NOT_VERIFICATION — не верифицирует соседний факт
  7. NOT_ASCII — вне ASCII; фильтры «только ASCII» её не увидят как l
  8. NOT_AUTOMATICALLY_SPOOF — в римской нумерации это норма, не атака
  9. NOT_EXECUTION_TRIGGER — сама по себе ничего не запускает
  10. NOT_TRUST_SIGNAL — не повышает доверие
  11. NOT_INTERCHANGEABLE_IN_IDENTIFIERS — в идентификаторе замена l→ⅼ меняет сущность

BASE_FORMULAS:
  ROMAN_FIFTY_FORM ≠ LATIN_L
  ROMAN_FIFTY_FORM ≠ SAME_CODEPOINT_AS_LATIN
  ROMAN_FIFTY_FORM ≠ BRAND_NAME_PROOF
  ROMAN_FIFTY_FORM ≠ DOMAIN_VALIDITY_PROOF
  ROMAN_FIFTY_FORM ≠ AUTHORITY
  ROMAN_FIFTY_FORM ≠ VERIFICATION
  ROMAN_FIFTY_FORM ≠ ASCII_LETTER
  ROMAN_FIFTY_FORM ≠ AUTOMATICALLY_SPOOF
  ROMAN_FIFTY_FORM ≠ TRUST_SIGNAL
  ROMAN_FIFTY_FORM ≠ EFFECT
  ROMAN_FIFTY_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: ⅼ (малая римская 50) — стабильный числовой знак. «Гомоглиф» это свойство визуального совпадения с латинской l, существующее одновременно с числовой функцией. Опасность контекстна (подмена буквы в токене), не эпохальна.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1
  NOTE: числовой письменный знак без жестового предшественника; форма-числоформа Unicode унаследована от латинской буквы L.

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
    INPUT: "Ⅼ = 50 (римская)"
    CONTEXT: римская цифра 50 в числовом контексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_FIFTY_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_002:
    INPUT: "нумерация: ⅰ ⅴ ⅹ ⅼ"
    CONTEXT: последовательность малых римских цифр
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_FIFTY_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "глава Ⅼ"
    CONTEXT: номер главы римской цифрой
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_FIFTY_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_004:
    INPUT: "циферблат: Ⅰ Ⅴ Ⅹ Ⅼ"
    CONTEXT: римские цифры (типографика)
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_FIFTY_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "том ⅼ, страница 3"
    CONTEXT: номер тома малой римской цифрой
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_FIFTY_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_006:
    INPUT: "пункт Ⅼ списка"
    CONTEXT: пункт нумерованного списка римской цифрой
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_FIFTY_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: BRAND_LETTER_SPOOF
    INPUT: "paypaⅼ.com" (римская ⅼ вместо l)
    CONTEXT: IDN/бренд-спуф — токен выглядит как paypal.com
    RISK: HIGH
    ATTACK: замена латинской l на римскую ⅼ даёт визуально идентичный домен, регистрируемый атакующим
    GUARD: ROMAN_FIFTY_FORM ≠ LATIN_L
  RISK_CASE_002:
    NAME: LOGIN_HOMOGLYPH
    INPUT: "ⅼogin.example" (римская ⅼ в начале)
    CONTEXT: подмена в служебном имени
    RISK: MEDIUM
    ATTACK: «ⅼogin» выглядит как «login», но это иной токен
    GUARD: ROMAN_FIFTY_FORM ≠ DOMAIN_VALIDITY_PROOF
  RISK_CASE_003:
    NAME: FILTER_BYPASS_KEYWORD
    INPUT: "iⅼlegal" (римская ⅼ обходит blocklist по «illegal»)
    CONTEXT: обход текстового фильтра
    RISK: MEDIUM
    ATTACK: подмена одной буквы уводит слово из-под blocklist
    GUARD: ROMAN_FIFTY_FORM ≠ ASCII_LETTER
  RISK_CASE_004:
    NAME: HANDLE_IMPERSONATION
    INPUT: "@nulⅼ_admin" (римская ⅼ в хэндле)
    CONTEXT: имитация служебного аккаунта
    RISK: MEDIUM
    ATTACK: двойник-хэндл выглядит как «null_admin», но это другой аккаунт
    GUARD: ROMAN_FIFTY_FORM ≠ VERIFICATION
  RISK_CASE_005:
    NAME: EMAIL_LOOKALIKE
    INPUT: "billing@gⅼobal-bank.example"
    CONTEXT: римская ⅼ в домене письма
    RISK: MEDIUM
    ATTACK: домен визуально совпадает, но ведёт к атакующему
    GUARD: ROMAN_FIFTY_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
  RISK_CASE_006:
    NAME: MULTI_HOMOGLYPH_MIX
    INPUT: "paypaⅼ" (римская ⅼ + латиница + возможна вертикальная черта)
    CONTEXT: смешение источников-двойников усложняет детекцию
    RISK: MEDIUM
    ATTACK: одна буква цели имитируется из разных наборов (цифра/буква/пунктуация)
    GUARD: ROMAN_FIFTY_FORM ≠ BRAND_NAME_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: l
    CODEPOINT: U+006C
    NAME: LATIN SMALL LETTER L
    RISK: HIGH
    RULE: LATIN_L ≠ ROMAN_FIFTY (главная цель имитации; визуально идентичны)
  CONFUSABLE_002:
    VISIBLE_FORM: 1
    CODEPOINT: U+0031
    NAME: DIGIT ONE
    RISK: MEDIUM
    RULE: DIGIT_ONE ≠ ROMAN_FIFTY (в части шрифтов близки к l/1)
  CONFUSABLE_003:
    VISIBLE_FORM: I
    CODEPOINT: U+0049
    NAME: LATIN CAPITAL LETTER I
    RISK: MEDIUM
    RULE: CAPITAL_I ≠ ROMAN_FIFTY
  CONFUSABLE_004:
    VISIBLE_FORM: |
    CODEPOINT: U+007C
    NAME: VERTICAL LINE
    RISK: LOW
    RULE: VERTICAL_LINE ≠ ROMAN_FIFTY
  CONFUSABLE_005:
    VISIBLE_FORM: ǀ
    CODEPOINT: U+01C0
    NAME: LATIN LETTER DENTAL CLICK
    RISK: LOW
    RULE: DENTAL_CLICK ≠ ROMAN_FIFTY

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: «домен `paypaⅼ.com` — это PayPal»
    RESPONSE: ROMAN_FIFTY_FORM ≠ LATIN_L
    RULE: символ — римская цифра; регистрируемый домен иной, DNS решает, не глаз
  CG2:
    TRIGGER: «строка с ⅼ равна её латинскому написанию»
    RESPONSE: ROMAN_FIFTY_FORM ≠ SAME_CODEPOINT_AS_LATIN
    RULE: разные кодпоинты → машинно разные строки
  CG3:
    TRIGGER: «любая ⅼ в тексте — атака»
    RESPONSE: ROMAN_FIFTY_FORM ≠ AUTOMATICALLY_SPOOF
    RULE: в римской нумерации знак легитимен; спуф — это подмена БУКВЫ в латинском токене
  CG4:
    TRIGGER: «ASCII-фильтр поймает подменённое слово»
    RESPONSE: ROMAN_FIFTY_FORM ≠ ASCII_LETTER
    RULE: ⅼ вне ASCII; фильтр по латинице её не сматчит
  CG5:
    TRIGGER: «хэндл `@nulⅼ_admin` — тот же аккаунт»
    RESPONSE: ROMAN_FIFTY_FORM ≠ VERIFICATION
    RULE: визуальное сходство не идентифицирует аккаунт
  CG6:
    TRIGGER: «замена l→ⅼ в идентификаторе безобидна»
    RESPONSE: ROMAN_FIFTY_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
    RULE: в домене/логине замена меняет сущность, к которой ведёт строка

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "paypaⅼ" (римская ⅼ + латиница в одном токене)
      NAME: MIXED_SCRIPT_TOKEN
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: бренд-спуф; ключевой сигнал — числоформа/иной набор внутри латинского токена
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "gⅼobaⅼ" (несколько ⅼ среди латиницы)
      NAME: MULTI_HOMOGLYPH_TOKEN
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: множественная подмена под целевое имя
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — опасность знака проявляется в последовательности (токене), не в изоляции.

PHAGO_ENTITY_MIMICRY:
  PE_001:
    INPUT: "paypaⅼ.com"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: MEDIUM
    NOTE: ⅼ имитирует букву ИМЕНИ проверенного бренда (paypal). Частичный (○) PHAGO — реже гомоглифов a/o, но тот же класс entity-mimicry по имени.
  PE_002:
    INPUT: "@gⅼobal_support"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: MEDIUM
    NOTE: имитация официального аккаунта через двойник-букву в имени.

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: подмена латинской l (U+006C) на римскую ⅼ (U+217C) в домене бренда
  A2: смешение ⅼ с вертикальной чертой | (U+007C) / цифрой 1 для усложнения детекции
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: римская ⅼ обходит blocklist по латинскому ключевому слову (iⅼlegal)
  B2: римская ⅼ в домене письма (billing@gⅼobal-bank.example)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: смешанный токен `paypaⅼ` (SC1)
  C2: множественная подмена `gⅼobaⅼ` (SC2)
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: хэндл `@nulⅼ_admin` имитирует служебный аккаунт
  D2: «ⅼogin-official» — двойник в псевдо-официальном имени
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: `paypaⅼ.com` — имитация имени бренда (PE_001)
  E2: `@gⅼobal_support` — имитация официального аккаунта (PE_002)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет дремлющих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: `paypaⅼ.com` с римской ⅼ — это домен PayPal
  EXPECTED: FAIL_BRAND_NAME_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: строка с ⅼ машинно равна латинскому написанию
  EXPECTED: FAIL_CODEPOINT_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: любая ⅼ в тексте — атака
  EXPECTED: FAIL_OVERBLOCK_MIMICRY (обратная ошибка: настоящая римская нумерация — не спуф)
  RESULT: FAIL
MUTATION_04:
  CLAIM: ASCII-фильтр по «illegal» поймает «iⅼlegal»
  EXPECTED: FAIL_ASCII_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: хэндл `@nulⅼ_admin` — тот же аккаунт, что `@null_admin`
  EXPECTED: FAIL_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: замена l→ⅼ в идентификаторе безобидна
  EXPECTED: FAIL_IDENTIFIER_INTERCHANGE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как отличать легит римскую нумерацию от подмены буквы без ложных срабатываний?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (правило «числоформа среди латинских БУКВ в одном токене» — уровень интегратора; ср. Vakhter confusable_cards.py)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует формулу LOOKS_SAME ≠ IS_SAME и правило «спуф = подмена в токене, не присутствие числоформы».
ALL_OPEN_QUESTIONS_CLOSED: NO (делегирован, не блокирует)

============================================================
11. PATCH_HISTORY
============================================================
PATCH_HISTORY:
  v0_1_PATCH_01: первичное создание (Ruslan Malyavsky, 2026-07-21) — черновик по шаблону GEN3_v0_3 (Vakhter), знак-гомоглиф; не прогонялся через конвейер.
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
