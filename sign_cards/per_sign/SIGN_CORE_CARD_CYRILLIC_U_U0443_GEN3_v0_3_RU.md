PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_CYRILLIC_U_U0443_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
TRANSLATION_NOTE: Русский оригинал (авторитетный). Английское зеркало — SIGN_CORE_CARD_CYRILLIC_U_U0443_GEN3_v0_3_EN. Кодпойнты, имена полей и формулы идентичны. Знак-гомоглиф: базовый закон LOOKS_SAME ≠ IS_SAME. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_CYRILLIC_U_U0443_GEN3_v0_3_RU
CODEPOINT: U+0443
VISIBLE_FORM: у
UNICODE_NAME: CYRILLIC SMALL LETTER U
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: кириллическая «у» (гомоглиф латинской y)
CATEGORY_ROADMAP: PH (phishing) · PHAGO: ● (сильный носитель — имитирует само имя бренда)

============================================================
3. REQUIRED_GENERAL_GUARDS
============================================================
REQUIRED_GENERAL_GUARDS:
  - SIGN_FALSE_EFFECT_MIMICRY_GUARD_v0_2A_RU
    GUARD_COMPATIBILITY: применим — знак не создаёт полей-эффектов; для гомоглифа guard расширяется проверкой смешения письменностей на уровне интегратора
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
VISIBLE_FORM: у
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_LETTER_HOMOGLYPH
BASE_MODE_FORMULA: CYRILLIC_U_FORM ≠ LATIN_Y
SIGN_CATEGORY:
  - кириллическая буква (легитимна в русском / других кириллических письменностях)
  - гомоглиф латинской малой «y» (U+0079)
  - потенциальный носитель гомоглиф / IDN подделки при смешении письменностей

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_LATIN_Y — кириллическая у (U+0443) НЕ есть латинская y (U+0079); другой кодпойнт
  2. NOT_SAME_STRING_AS_LATIN — строка с кириллической у не машинно-равна своему латинскому двойнику
  3. NOT_BRAND_NAME_PROOF — «уoutube.com» не доказывает связь с брендом YouTube
  4. NOT_DOMAIN_VALIDITY_PROOF — визуальное совпадение домена не подтверждает регистрируемый домен
  5. NOT_AUTHORITY — буква не подтверждает официальный статус
  6. NOT_VERIFICATION — она не верифицирует соседний факт
  7. NOT_ASCII — не в ASCII; фильтры «только ASCII» не видят её как y
  8. NOT_AUTOMATICALLY_SPOOF — в односкриптовом русском тексте она нормальна, не атака
  9. NOT_EXECUTION_TRIGGER — сама по себе она ничего не запускает
  10. NOT_TRUST_SIGNAL — она не повышает доверие к контенту
  11. NOT_EFFECT — форма буквы не создаёт эффекта
  12. NOT_INTERCHANGEABLE_IN_IDENTIFIERS — в идентификаторе/домене y→у меняет сущность

BASE_FORMULAS:
  CYRILLIC_U_FORM ≠ LATIN_Y
  CYRILLIC_U_FORM ≠ SAME_CODEPOINT_AS_LATIN
  CYRILLIC_U_FORM ≠ BRAND_NAME_PROOF
  CYRILLIC_U_FORM ≠ DOMAIN_VALIDITY_PROOF
  CYRILLIC_U_FORM ≠ AUTHORITY
  CYRILLIC_U_FORM ≠ VERIFICATION
  CYRILLIC_U_FORM ≠ ASCII_LETTER
  CYRILLIC_U_FORM ≠ AUTOMATICALLY_SPOOF
  CYRILLIC_U_FORM ≠ TRUST_SIGNAL
  CYRILLIC_U_FORM ≠ EFFECT
  CYRILLIC_U_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: кириллическая «у» — стабильная буква без культурной прецессии функций. «Гомоглиф» — не эпоха, а свойство визуального совпадения с латинской y, сосуществующее с легитимной функцией буквы. Опасность контекстна (смешение письменностей), не эпохальна — поэтому SEMANTIC_EPOCH_TRACKER не применяется.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1 (физический жест)
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
    INPUT: "утро туманное" (a misty morning, Russian)
    CONTEXT: обычный русский текст (одна письменность)
    EXPECTED: INFO
    RISK: NONE
    GUARD: CYRILLIC_U_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_002:
    INPUT: "Ульяна Кузнецова" (a Russian name)
    CONTEXT: русское имя собственное
    EXPECTED: INFO
    RISK: NONE
    GUARD: CYRILLIC_U_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "улица и двор" (a street and a yard)
    CONTEXT: русские слова, где «у» — обычная буква
    EXPECTED: INFO
    RISK: NONE
    GUARD: CYRILLIC_U_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_004:
    INPUT: "уроки музыки" (music lessons)
    CONTEXT: русская фраза
    EXPECTED: INFO
    RISK: NONE
    GUARD: CYRILLIC_U_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "путь к успеху" (the path to success)
    CONTEXT: односкриптовая кириллическая фраза
    EXPECTED: INFO
    RISK: NONE
    GUARD: CYRILLIC_U_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_006:
    INPUT: "уху из щуки" (fish soup from pike)
    CONTEXT: фраза, богатая на «у», но вся кириллическая
    EXPECTED: INFO
    RISK: NONE
    GUARD: CYRILLIC_U_FORM ≠ AUTOMATICALLY_SPOOF

RISK_CASES:
  RISK_CASE_001:
    NAME: YOUTUBE_HOMOGLYPH
    INPUT: "уoutube.com" (Cyrillic у at the start of a brand)
    CONTEXT: IDN/бренд-подделка — токен выглядит как youtube.com, но первый символ кириллический
    RISK: CRITICAL
    ATTACK: замена латинской y на кириллическую у даёт визуально идентичный домен, который регистрирует атакующий
    GUARD: CYRILLIC_U_FORM ≠ LATIN_Y
  RISK_CASE_002:
    NAME: MEDIAL_BRAND_SUBSTITUTION
    INPUT: "paуpal.com" (Cyrillic у in the middle of a brand)
    CONTEXT: срединная замена в бренд-домене
    RISK: CRITICAL
    ATTACK: строка машинно-≠ paypal.com, но человек не видит разницы
    GUARD: CYRILLIC_U_FORM ≠ DOMAIN_VALIDITY_PROOF
  RISK_CASE_003:
    NAME: HANDLE_IMPERSONATION
    INPUT: "@securitу" (Cyrillic у in a handle)
    CONTEXT: выдача себя за аккаунт безопасности в чате/соцплатформе
    RISK: HIGH
    ATTACK: похожий хэндл выглядит как security, но это другой аккаунт
    GUARD: CYRILLIC_U_FORM ≠ VERIFICATION
  RISK_CASE_004:
    NAME: FILTER_BYPASS_KEYWORD
    INPUT: "buу-now" (Cyrillic у bypasses a "buy" blocklist)
    CONTEXT: обход текстового фильтра, ищущего латинское слово
    RISK: HIGH
    ATTACK: одна заменённая буква выводит слово из-под блоклиста
    GUARD: CYRILLIC_U_FORM ≠ ASCII_LETTER
  RISK_CASE_005:
    NAME: EMAIL_LOOKALIKE
    INPUT: "alerts@paу-verify.example" (Cyrillic у in the mail domain)
    CONTEXT: фишинговое письмо от «того же» платёжного сервиса
    RISK: HIGH
    ATTACK: домен выглядит идентично, но ведёт к атакующему
    GUARD: CYRILLIC_U_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
  RISK_CASE_006:
    NAME: MULTI_HOMOGLYPH_ON_TARGET
    INPUT: "moneу-paу" (several Cyrillic у imitating a brand phrase)
    CONTEXT: несколько замен в одном токене
    RISK: HIGH
    ATTACK: цепочка двойников имитирует всё латинское имя бренда
    GUARD: CYRILLIC_U_FORM ≠ BRAND_NAME_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: y
    CODEPOINT: U+0079
    NAME: LATIN SMALL LETTER Y
    RISK: CRITICAL
    RULE: LATIN_Y ≠ CYRILLIC_U (первичная цель имитации; визуально идентична во многих шрифтах)
  CONFUSABLE_002:
    VISIBLE_FORM: ү
    CODEPOINT: U+04AF
    NAME: CYRILLIC SMALL LETTER STRAIGHT U
    RISK: MEDIUM
    RULE: CYRILLIC_STRAIGHT_U ≠ CYRILLIC_U (та же письменность, родственная буква; отдельный кодпойнт)
  CONFUSABLE_003:
    VISIBLE_FORM: 𝗒
    CODEPOINT: U+1D5D2
    NAME: MATHEMATICAL SANS-SERIF SMALL Y
    RISK: MEDIUM
    RULE: MATH_SANS_Y ≠ CYRILLIC_U (математико-алфавитно-стилизованная латинская y для обхода простых фильтров)
  CONFUSABLE_004:
    VISIBLE_FORM: ý
    CODEPOINT: U+00FD
    NAME: LATIN SMALL LETTER Y WITH ACUTE
    RISK: LOW
    RULE: LATIN_Y_ACUTE ≠ CYRILLIC_U (латинский двойник с диакритикой)
  CONFUSABLE_005:
    VISIBLE_FORM: ｙ
    CODEPOINT: U+FF59
    NAME: FULLWIDTH LATIN SMALL LETTER Y
    RISK: LOW
    RULE: FULLWIDTH_Y ≠ CYRILLIC_U (полноширинная латинская y; другая совместимостная форма)
  CONFUSABLE_006:
    VISIBLE_FORM: ÿ
    CODEPOINT: U+00FF
    NAME: LATIN SMALL LETTER Y WITH DIAERESIS
    RISK: LOW
    RULE: LATIN_Y_DIAERESIS ≠ CYRILLIC_U (декорированный латинский двойник)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "the domain `уoutube.com` is YouTube"
    RESPONSE: CYRILLIC_U_FORM ≠ LATIN_Y
    RULE: первый символ кириллический; регистрируемый домен другой — решает DNS, не глаз
  CG2:
    TRIGGER: "a string with Cyrillic у equals its Latin spelling"
    RESPONSE: CYRILLIC_U_FORM ≠ SAME_CODEPOINT_AS_LATIN
    RULE: разные кодпойнты → машинно-разные строки
  CG3:
    TRIGGER: "any Cyrillic у in text is an attack"
    RESPONSE: CYRILLIC_U_FORM ≠ AUTOMATICALLY_SPOOF
    RULE: в односкриптовом русском тексте буква легитимна; подделка — это СМЕШЕНИЕ письменностей в одном токене
  CG4:
    TRIGGER: "an ASCII filter will catch the substituted word"
    RESPONSE: CYRILLIC_U_FORM ≠ ASCII_LETTER
    RULE: кириллическая у вне ASCII; латинский фильтр её не совпадёт
  CG5:
    TRIGGER: "the handle `@securitу` is the same account as @security"
    RESPONSE: CYRILLIC_U_FORM ≠ VERIFICATION
    RULE: визуальное сходство не идентифицирует аккаунт
  CG6:
    TRIGGER: "swapping y→у in an identifier is harmless"
    RESPONSE: CYRILLIC_U_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
    RULE: в домене/логине/токене замена меняет сущность, в которую строка разрешается

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "уoutube" (Cyrillic у + Latin in one token)
      NAME: MIXED_SCRIPT_TOKEN
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: IDN/бренд-подделка; ключевой сигнал — СМЕШЕНИЕ письменностей внутри одного токена
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "moneу-paу" (several Cyrillic among Latin)
      NAME: MULTI_HOMOGLYPH_TOKEN
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: множественная замена на целевой бренд
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: не применимо — опасность знака появляется именно в последовательности (в токене), не в изоляции.

PHAGO_ENTITY_MIMICRY:
  PE_001:
    INPUT: "уoutube.com"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: CRITICAL
    NOTE: кириллическая у имитирует само ИМЯ верифицированного бренда (не просто структуру) — прямая мимикрия существования сущности. Поэтому реестр помечает знак PHAGO ●; коммерческие защиты от двойников часто упускают этот класс.
  PE_002:
    INPUT: "@paуpal_support"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: HIGH
    NOTE: выдача себя за официальный бренд-аккаунт через двойника в имени.

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена латинской y (U+0079) на кириллическую у (U+0443) в бренд-домене
  A2: смешение кириллической у с математической sans-serif y / акцентированной латинской ý для усложнения детекции
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: кириллическая у обходит латинский блоклист ключевых слов (buу-now)
  B2: кириллическая у в почтовом домене (alerts@paу-verify.example) для фишинга
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: смешанный токен `уoutube` (SC1) — письменности внутри одного слова
  C2: множественная замена `moneу-paу` (SC2) на целевой бренд
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: хэндл `@securitу` имитирует сервисный аккаунт
  D2: "paу-official" — двойник в псевдо-официальном имени
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: `уoutube.com` — мимикрия имени бренда (PE_001)
  E2: `@paуpal_support` — мимикрия официального аккаунта (PE_002)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у буквы нет спящих/активных эпох (см. раздел 5).
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: `уoutube.com` with Cyrillic у is YouTube's domain
  EXPECTED: FAIL_BRAND_NAME_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: a string with Cyrillic у is machine-equal to its Latin spelling
  EXPECTED: FAIL_CODEPOINT_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: any Cyrillic у in text is an attack
  EXPECTED: FAIL_OVERBLOCK_MIMICRY (обратная ошибка: настоящий русский — не подделка)
  RESULT: FAIL
MUTATION_04:
  CLAIM: an ASCII filter on "buy" will catch "buу"
  EXPECTED: FAIL_ASCII_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: the handle `@securitу` is the same account as `@security`
  EXPECTED: FAIL_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: swapping y→у in an identifier is harmless
  EXPECTED: FAIL_IDENTIFIER_INTERCHANGE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как отличить легитимный односкриптовый русский текст от подделки без ложных срабатываний?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (правило «смешение письменностей внутри одного токена» — забота интегратора; см. прототип Vakhter confusable_cards.py)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует формулу LOOKS_SAME ≠ IS_SAME и правило «подделка = смешение, не присутствие».
OQ2:
  QUESTION: нужна ли полная таблица UTS #39 confusables + корпус брендов для случая целой письменности?
  STATUS: OPEN
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: делегировано рантайму/интегратору.
ALL_OPEN_QUESTIONS_CLOSED: NO (delegated, non-blocking)

============================================================
11. PATCH_HISTORY
============================================================
PATCH_HISTORY:
  v0_1_PATCH_01: первичное создание (Ruslan Malyavsky, 2026-07-22) — черновик из шаблона GEN3_v0_3 (Vakhter), знак-гомоглиф; не конвейер-ран.
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
  NOT_CONVEYOR_RUN (draft for our work; conveyor is a separate project)
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
