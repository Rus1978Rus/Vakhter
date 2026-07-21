ЧАСТНЫЙ АВТОРСКИЙ ПРОЕКТ / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_CYRILLIC_A_U0430_GEN3_v0_3_RU
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
CARD_UID: SIGN_CORE_CARD_CYRILLIC_A_U0430_GEN3_v0_3_RU
CODEPOINT: U+0430
VISIBLE_FORM: а
UNICODE_NAME: CYRILLIC SMALL LETTER A
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: кириллическая «а» (гомоглиф латинской a)
CATEGORY_ROADMAP: PH (phishing) · PHAGO: ● (сильный носитель — имитирует само имя бренда)

============================================================
3. REQUIRED_GENERAL_GUARDS
============================================================
REQUIRED_GENERAL_GUARDS:
  - SIGN_FALSE_EFFECT_MIMICRY_GUARD_v0_2A_RU
    GUARD_COMPATIBILITY: применим — знак не создаёт effect-полей; для гомоглифа гард дополняется проверкой смешения письменностей на уровне интегратора
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
VISIBLE_FORM: а
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_LETTER_HOMOGLYPH
BASE_MODE_FORMULA: CYRILLIC_A_FORM ≠ LATIN_A
SIGN_CATEGORY:
  - кириллическая буква (легитимна в русском/др. кириллических письменностях)
  - гомоглиф латинской строчной «a» (U+0061)
  - потенциальный носитель homoglyph/IDN-спуфинга при смешении письменностей

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_LATIN_A — кириллическая а (U+0430) это НЕ латинская a (U+0061); другой кодпоинт
  2. NOT_SAME_STRING_AS_LATIN — строка с кириллической а машинно не равна латинскому двойнику
  3. NOT_BRAND_NAME_PROOF — «аpple» не доказывает связь с брендом Apple
  4. NOT_DOMAIN_VALIDITY_PROOF — визуальное совпадение домена не подтверждает регистрируемый домен
  5. NOT_AUTHORITY — буква не подтверждает официальный статус
  6. NOT_VERIFICATION — не верифицирует соседний факт
  7. NOT_ASCII — не входит в ASCII; фильтры «только ASCII» её не увидят как a
  8. NOT_AUTOMATICALLY_SPOOF — в односкриптовом русском тексте это норма, не атака
  9. NOT_EXECUTION_TRIGGER — сама по себе ничего не запускает
  10. NOT_TRUST_SIGNAL — не повышает доверие к контенту
  11. NOT_EFFECT — форма буквы не создаёт эффекта
  12. NOT_INTERCHANGEABLE_IN_IDENTIFIERS — в идентификаторе/домене замена a→а меняет сущность

BASE_FORMULAS:
  CYRILLIC_A_FORM ≠ LATIN_A
  CYRILLIC_A_FORM ≠ SAME_CODEPOINT_AS_LATIN
  CYRILLIC_A_FORM ≠ BRAND_NAME_PROOF
  CYRILLIC_A_FORM ≠ DOMAIN_VALIDITY_PROOF
  CYRILLIC_A_FORM ≠ AUTHORITY
  CYRILLIC_A_FORM ≠ VERIFICATION
  CYRILLIC_A_FORM ≠ ASCII_LETTER
  CYRILLIC_A_FORM ≠ AUTOMATICALLY_SPOOF
  CYRILLIC_A_FORM ≠ TRUST_SIGNAL
  CYRILLIC_A_FORM ≠ EFFECT
  CYRILLIC_A_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: кириллическая «а» — стабильная буква без культурной прецессии функций. «Гомоглиф» это не эпоха, а свойство визуального совпадения с латинской a, существующее одновременно с легит-функцией буквы. Опасность контекстна (смешение письменностей), а не эпохальна — поэтому SEMANTIC_EPOCH_TRACKER не применяется.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1 (физический жест)
  NOTE: буква — письменный знак без жестового предшественника; кириллица восходит к греческому унциалу (письменная генеалогия).

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
    INPUT: "привет мир"
    CONTEXT: обычный русский текст (одна письменность)
    EXPECTED: INFO
    RISK: NONE
    GUARD: CYRILLIC_A_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_002:
    INPUT: "Анна Ахматова"
    CONTEXT: русское имя собственное
    EXPECTED: INFO
    RISK: NONE
    GUARD: CYRILLIC_A_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "касса магазина"
    CONTEXT: русские слова, где «а» — обычная буква
    EXPECTED: INFO
    RISK: NONE
    GUARD: CYRILLIC_A_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_004:
    INPUT: "1 апреля 2026"
    CONTEXT: дата с русским месяцем
    EXPECTED: INFO
    RISK: NONE
    GUARD: CYRILLIC_A_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "банк России"
    CONTEXT: односкриптовое кириллическое словосочетание
    EXPECTED: INFO
    RISK: NONE
    GUARD: CYRILLIC_A_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_006:
    INPUT: "мама"
    CONTEXT: слово только из потенциально-двойниковых букв, но всё кириллическое
    EXPECTED: INFO
    RISK: NONE
    GUARD: CYRILLIC_A_FORM ≠ AUTOMATICALLY_SPOOF

RISK_CASES:
  RISK_CASE_001:
    NAME: MIXED_SCRIPT_BRAND_SPOOF
    INPUT: "аpple.com" (кириллическая а + латинские pple)
    CONTEXT: IDN/бренд-спуф — токен выглядит как apple.com, но первый символ кириллический
    RISK: CRITICAL
    ATTACK: замена латинской a на кириллическую а даёт визуально идентичный домен, регистрируемый атакующим
    GUARD: CYRILLIC_A_FORM ≠ LATIN_A
  RISK_CASE_002:
    NAME: PAYPAL_HOMOGLYPH
    INPUT: "pаypal.com" (кириллическая а в середине)
    CONTEXT: срединная подмена в бренде
    RISK: CRITICAL
    ATTACK: строка машинно ≠ paypal.com, но человек не видит разницы
    GUARD: CYRILLIC_A_FORM ≠ DOMAIN_VALIDITY_PROOF
  RISK_CASE_003:
    NAME: HANDLE_IMPERSONATION
    INPUT: "@аdmin" (кириллическая а в хэндле)
    CONTEXT: имитация аккаунта admin в соцсети/чате
    RISK: HIGH
    ATTACK: двойник-хэндл выглядит как admin, но это другой аккаунт
    GUARD: CYRILLIC_A_FORM ≠ VERIFICATION
  RISK_CASE_004:
    NAME: FILTER_BYPASS_KEYWORD
    INPUT: "cаsino" (кириллическая а обходит blocklist по «casino»)
    CONTEXT: обход текстового фильтра, ищущего латинское слово
    RISK: HIGH
    ATTACK: подмена одной буквы уводит слово из-под blocklist
    GUARD: CYRILLIC_A_FORM ≠ ASCII_LETTER
  RISK_CASE_005:
    NAME: EMAIL_LOOKALIKE
    INPUT: "support@bаnk.example" (кириллическая а в домене письма)
    CONTEXT: фишинговое письмо от «того же» банка
    RISK: HIGH
    ATTACK: домен визуально совпадает, но ведёт к атакующему
    GUARD: CYRILLIC_A_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
  RISK_CASE_006:
    NAME: WHOLE_WORD_CYRILLIC_ON_TARGET
    INPUT: "раyраl" (несколько кириллических а/р, имитирующих paypal)
    CONTEXT: множественная подмена в одном токене
    RISK: HIGH
    ATTACK: цепочка двойников целиком имитирует латинское имя бренда
    GUARD: CYRILLIC_A_FORM ≠ BRAND_NAME_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: a
    CODEPOINT: U+0061
    NAME: LATIN SMALL LETTER A
    RISK: CRITICAL
    RULE: LATIN_A ≠ CYRILLIC_A (главная цель имитации; визуально идентичны во многих шрифтах)
  CONFUSABLE_002:
    VISIBLE_FORM: α
    CODEPOINT: U+03B1
    NAME: GREEK SMALL LETTER ALPHA
    RISK: MEDIUM
    RULE: GREEK_ALPHA ≠ CYRILLIC_A (в части шрифтов похожа)
  CONFUSABLE_003:
    VISIBLE_FORM: ɑ
    CODEPOINT: U+0251
    NAME: LATIN SMALL LETTER ALPHA
    RISK: MEDIUM
    RULE: LATIN_ALPHA ≠ CYRILLIC_A
  CONFUSABLE_004:
    VISIBLE_FORM: ª
    CODEPOINT: U+00AA
    NAME: FEMININE ORDINAL INDICATOR
    RISK: LOW
    RULE: FEMININE_ORDINAL ≠ CYRILLIC_A
  CONFUSABLE_005:
    VISIBLE_FORM: á
    CODEPOINT: U+00E1
    NAME: LATIN SMALL LETTER A WITH ACUTE
    RISK: LOW
    RULE: LATIN_A_ACUTE ≠ CYRILLIC_A (акцентированный латинский двойник)
  CONFUSABLE_006:
    VISIBLE_FORM: ạ
    CODEPOINT: U+1EA1
    NAME: LATIN SMALL LETTER A WITH DOT BELOW
    RISK: LOW
    RULE: LATIN_A_DOT_BELOW ≠ CYRILLIC_A

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: «домен `аpple.com` — это Apple»
    RESPONSE: CYRILLIC_A_FORM ≠ LATIN_A
    RULE: первый символ кириллический; регистрируемый домен иной, DNS решает, не глаз
  CG2:
    TRIGGER: «строка с кириллической а равна её латинскому написанию»
    RESPONSE: CYRILLIC_A_FORM ≠ SAME_CODEPOINT_AS_LATIN
    RULE: разные кодпоинты → машинно разные строки
  CG3:
    TRIGGER: «любая кириллическая а в тексте — это атака»
    RESPONSE: CYRILLIC_A_FORM ≠ AUTOMATICALLY_SPOOF
    RULE: в односкриптовом русском тексте буква легитимна; спуф — это СМЕШЕНИЕ письменностей в одном токене
  CG4:
    TRIGGER: «ASCII-фильтр поймает подменённое слово»
    RESPONSE: CYRILLIC_A_FORM ≠ ASCII_LETTER
    RULE: кириллическая а вне ASCII; фильтр по латинице её не сматчит
  CG5:
    TRIGGER: «хэндл `@аdmin` — тот же аккаунт, что @admin»
    RESPONSE: CYRILLIC_A_FORM ≠ VERIFICATION
    RULE: визуальное сходство не идентифицирует аккаунт
  CG6:
    TRIGGER: «замена a→а в идентификаторе безобидна»
    RESPONSE: CYRILLIC_A_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
    RULE: в домене/логине/токене замена меняет сущность, к которой ведёт строка

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "аpple" (кириллическая а + латиница в одном токене)
      NAME: MIXED_SCRIPT_TOKEN
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: IDN/бренд-спуф; ключевой сигнал — СМЕШЕНИЕ письменностей внутри одного токена
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "раyраl" (несколько кириллических среди латиницы)
      NAME: MULTI_HOMOGLYPH_TOKEN
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: множественная подмена под целевой бренд
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — опасность знака проявляется именно в последовательности (токене), не в изоляции.

PHAGO_ENTITY_MIMICRY:
  PE_001:
    INPUT: "аpple.com"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: CRITICAL
    NOTE: кириллическая а имитирует само ИМЯ проверенного бренда (не просто структуру) — прямая имитация существования сущности. Именно поэтому реестр помечает знак PHAGO ●; коммерческие защиты от подделок этот класс часто пропускают.
  PE_002:
    INPUT: "@аmazon_support"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: HIGH
    NOTE: имитация официального аккаунта бренда через двойник в имени.

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: подмена латинской a (U+0061) на кириллическую а (U+0430) в домене бренда
  A2: смешение кириллической а с греческой α/латинской ɑ для усложнения детекции
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: кириллическая а обходит blocklist по латинскому ключевому слову (cаsino)
  B2: кириллическая а в домене письма (support@bаnk.example) для фишинга
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: смешанный токен `аpple` (SC1) — письменность в одном слове
  C2: множественная подмена `раyраl` (SC2) под целевой бренд
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: хэндл `@аdmin` имитирует служебный аккаунт
  D2: «cаfe-official» — двойник в псевдо-официальном имени
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: `аpple.com` — имитация имени бренда (PE_001)
  E2: `@аmazon_support` — имитация официального аккаунта (PE_002)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у буквы нет дремлющих/активных эпох (см. раздел 5).
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: `аpple.com` с кириллической а — это домен Apple
  EXPECTED: FAIL_BRAND_NAME_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: строка с кириллической а машинно равна латинскому написанию
  EXPECTED: FAIL_CODEPOINT_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: любая кириллическая а в тексте — атака
  EXPECTED: FAIL_OVERBLOCK_MIMICRY (обратная ошибка: настоящий русский — не спуф)
  RESULT: FAIL
MUTATION_04:
  CLAIM: ASCII-фильтр по «casino» поймает «cаsino»
  EXPECTED: FAIL_ASCII_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: хэндл `@аdmin` — тот же аккаунт, что `@admin`
  EXPECTED: FAIL_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: замена a→а в идентификаторе безобидна
  EXPECTED: FAIL_IDENTIFIER_INTERCHANGE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как отличать легит односкриптовый русский текст от спуфа без ложных срабатываний?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (правило «смешение письменностей в одном токене» — уровень интегратора; см. прототип Vakhter confusable_cards.py)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует формулу LOOKS_SAME ≠ IS_SAME и правило «спуф = смешение, не присутствие».
OQ2:
  QUESTION: нужен ли полный UTS #39 confusables + корпус брендов для whole-script случая?
  STATUS: OPEN
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: делегируется рантайму/интегратору.
ALL_OPEN_QUESTIONS_CLOSED: NO (делегированы, не блокируют)

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
