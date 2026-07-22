PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_CYRILLIC_JE_U0458_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
TRANSLATION_NOTE: Русский оригинал (авторитетный). Английское зеркало — SIGN_CORE_CARD_CYRILLIC_JE_U0458_GEN3_v0_3_EN. Кодпойнты, имена полей и формулы идентичны. Знак-гомоглиф: базовый закон LOOKS_SAME ≠ IS_SAME. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_CYRILLIC_JE_U0458_GEN3_v0_3_RU
CODEPOINT: U+0458
VISIBLE_FORM: ј
UNICODE_NAME: CYRILLIC SMALL LETTER JE
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: кириллическая «ј» (гомоглиф латинской j)
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
VISIBLE_FORM: ј
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_LETTER_HOMOGLYPH
BASE_MODE_FORMULA: CYRILLIC_JE_FORM ≠ LATIN_J
SIGN_CATEGORY:
  - кириллическая буква (легитимна в сербском / македонском и других кириллических письменностях)
  - гомоглиф латинской малой «j» (U+006A)
  - потенциальный носитель гомоглиф / IDN подделки при смешении письменностей

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_LATIN_J — кириллическая ј (U+0458) НЕ есть латинская j (U+006A); другой кодпойнт
  2. NOT_SAME_STRING_AS_LATIN — строка с кириллической ј не машинно-равна своему латинскому двойнику
  3. NOT_BRAND_NAME_PROOF — «јquery.com» не доказывает связь с проектом jQuery
  4. NOT_DOMAIN_VALIDITY_PROOF — визуальное совпадение домена не подтверждает регистрируемый домен
  5. NOT_AUTHORITY — буква не подтверждает официальный статус
  6. NOT_VERIFICATION — она не верифицирует соседний факт
  7. NOT_ASCII — не в ASCII; фильтры «только ASCII» не видят её как j
  8. NOT_AUTOMATICALLY_SPOOF — в односкриптовом сербском/македонском тексте она нормальна, не атака
  9. NOT_EXECUTION_TRIGGER — сама по себе она ничего не запускает
  10. NOT_TRUST_SIGNAL — она не повышает доверие к контенту
  11. NOT_EFFECT — форма буквы не создаёт эффекта
  12. NOT_INTERCHANGEABLE_IN_IDENTIFIERS — в идентификаторе/домене j→ј меняет сущность

BASE_FORMULAS:
  CYRILLIC_JE_FORM ≠ LATIN_J
  CYRILLIC_JE_FORM ≠ SAME_CODEPOINT_AS_LATIN
  CYRILLIC_JE_FORM ≠ BRAND_NAME_PROOF
  CYRILLIC_JE_FORM ≠ DOMAIN_VALIDITY_PROOF
  CYRILLIC_JE_FORM ≠ AUTHORITY
  CYRILLIC_JE_FORM ≠ VERIFICATION
  CYRILLIC_JE_FORM ≠ ASCII_LETTER
  CYRILLIC_JE_FORM ≠ AUTOMATICALLY_SPOOF
  CYRILLIC_JE_FORM ≠ TRUST_SIGNAL
  CYRILLIC_JE_FORM ≠ EFFECT
  CYRILLIC_JE_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: кириллическая «ј» — стабильная буква без культурной прецессии функций. «Гомоглиф» — не эпоха, а свойство визуального совпадения с латинской j, сосуществующее с легитимной функцией буквы. Опасность контекстна (смешение письменностей), не эпохальна — поэтому SEMANTIC_EPOCH_TRACKER не применяется.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1 (физический жест)
  NOTE: буква — письменный знак без жестового предшественника; кириллическая ј заимствована в сербский из латинской j (письменная генеалогия).

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
    INPUT: "један дан" (one day, Serbian)
    CONTEXT: обычный сербский текст (одна письменность)
    EXPECTED: INFO
    RISK: NONE
    GUARD: CYRILLIC_JE_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_002:
    INPUT: "Јован Јовановић" (a Serbian name)
    CONTEXT: сербское имя собственное
    EXPECTED: INFO
    RISK: NONE
    GUARD: CYRILLIC_JE_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "српски језик" (the Serbian language)
    CONTEXT: сербские слова, где «ј» — обычная буква
    EXPECTED: INFO
    RISK: NONE
    GUARD: CYRILLIC_JE_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_004:
    INPUT: "ново јутро" (a new morning)
    CONTEXT: сербская фраза
    EXPECTED: INFO
    RISK: NONE
    GUARD: CYRILLIC_JE_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "чај и кафа" (tea and coffee)
    CONTEXT: односкриптовая кириллическая фраза
    EXPECTED: INFO
    RISK: NONE
    GUARD: CYRILLIC_JE_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_006:
    INPUT: "мојој мајци" (to my mother)
    CONTEXT: фраза, богатая на «ј», но вся кириллическая
    EXPECTED: INFO
    RISK: NONE
    GUARD: CYRILLIC_JE_FORM ≠ AUTOMATICALLY_SPOOF

RISK_CASES:
  RISK_CASE_001:
    NAME: JQUERY_HOMOGLYPH
    INPUT: "јquery.com" (Cyrillic ј at the start of a name)
    CONTEXT: IDN/бренд-подделка — токен выглядит как jquery.com, но первый символ кириллический
    RISK: CRITICAL
    ATTACK: замена латинской j на кириллическую ј даёт визуально идентичный домен, который регистрирует атакующий
    GUARD: CYRILLIC_JE_FORM ≠ LATIN_J
  RISK_CASE_002:
    NAME: PACKAGE_TYPOSQUAT
    INPUT: "јsonwebtoken" (Cyrillic ј in a package name)
    CONTEXT: имя-двойник пакета в реестре
    RISK: CRITICAL
    ATTACK: строка машинно-≠ jsonwebtoken, но человек не видит разницы
    GUARD: CYRILLIC_JE_FORM ≠ DOMAIN_VALIDITY_PROOF
  RISK_CASE_003:
    NAME: HANDLE_IMPERSONATION
    INPUT: "@јenkins_ci" (Cyrillic ј in a handle)
    CONTEXT: выдача себя за аккаунт проекта в чате/соцплатформе
    RISK: HIGH
    ATTACK: похожий хэндл выглядит как jenkins_ci, но это другой аккаунт
    GUARD: CYRILLIC_JE_FORM ≠ VERIFICATION
  RISK_CASE_004:
    NAME: FILTER_BYPASS_KEYWORD
    INPUT: "јackpot" (Cyrillic ј bypasses a "jackpot" blocklist)
    CONTEXT: обход текстового фильтра, ищущего латинское слово
    RISK: HIGH
    ATTACK: одна заменённая буква выводит слово из-под блоклиста
    GUARD: CYRILLIC_JE_FORM ≠ ASCII_LETTER
  RISK_CASE_005:
    NAME: EMAIL_LOOKALIKE
    INPUT: "team@projeсt-јoin.example" (Cyrillic ј in the mail domain)
    CONTEXT: фишинговое письмо от «того же» проекта
    RISK: HIGH
    ATTACK: домен выглядит идентично, но ведёт к атакующему
    GUARD: CYRILLIC_JE_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
  RISK_CASE_006:
    NAME: MULTI_HOMOGLYPH_ON_TARGET
    INPUT: "јаvascript" (Cyrillic ј + а imitating a keyword)
    CONTEXT: несколько замен в одном токене
    RISK: HIGH
    ATTACK: цепочка двойников имитирует всё латинское ключевое слово/имя
    GUARD: CYRILLIC_JE_FORM ≠ BRAND_NAME_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: j
    CODEPOINT: U+006A
    NAME: LATIN SMALL LETTER J
    RISK: CRITICAL
    RULE: LATIN_J ≠ CYRILLIC_JE (первичная цель имитации; визуально идентична во многих шрифтах)
  CONFUSABLE_002:
    VISIBLE_FORM: ϳ
    CODEPOINT: U+03F3
    NAME: GREEK LETTER YOT
    RISK: MEDIUM
    RULE: GREEK_YOT ≠ CYRILLIC_JE (греческая j-подобная буква; двойник из третьей письменности)
  CONFUSABLE_003:
    VISIBLE_FORM: ј
    CODEPOINT: U+0575
    NAME: ARMENIAN SMALL LETTER YIWN
    RISK: MEDIUM
    RULE: ARMENIAN_YIWN ≠ CYRILLIC_JE (армянская j-подобная буква; другая письменность)
  CONFUSABLE_004:
    VISIBLE_FORM: 𝗃
    CODEPOINT: U+1D5C3
    NAME: MATHEMATICAL SANS-SERIF SMALL J
    RISK: MEDIUM
    RULE: MATH_SANS_J ≠ CYRILLIC_JE (математико-алфавитно-стилизованная латинская j для обхода простых фильтров)
  CONFUSABLE_005:
    VISIBLE_FORM: ｊ
    CODEPOINT: U+FF4A
    NAME: FULLWIDTH LATIN SMALL LETTER J
    RISK: LOW
    RULE: FULLWIDTH_J ≠ CYRILLIC_JE (полноширинная латинская j; другая совместимостная форма)
  CONFUSABLE_006:
    VISIBLE_FORM: ĵ
    CODEPOINT: U+0135
    NAME: LATIN SMALL LETTER J WITH CIRCUMFLEX
    RISK: LOW
    RULE: LATIN_J_CIRCUMFLEX ≠ CYRILLIC_JE (латинский двойник с диакритикой)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "the domain `јquery.com` is jQuery"
    RESPONSE: CYRILLIC_JE_FORM ≠ LATIN_J
    RULE: первый символ кириллический; регистрируемый домен другой — решает DNS, не глаз
  CG2:
    TRIGGER: "a string with Cyrillic ј equals its Latin spelling"
    RESPONSE: CYRILLIC_JE_FORM ≠ SAME_CODEPOINT_AS_LATIN
    RULE: разные кодпойнты → машинно-разные строки
  CG3:
    TRIGGER: "any Cyrillic ј in text is an attack"
    RESPONSE: CYRILLIC_JE_FORM ≠ AUTOMATICALLY_SPOOF
    RULE: в односкриптовом сербском/македонском тексте буква легитимна; подделка — это СМЕШЕНИЕ письменностей в одном токене
  CG4:
    TRIGGER: "an ASCII filter will catch the substituted word"
    RESPONSE: CYRILLIC_JE_FORM ≠ ASCII_LETTER
    RULE: кириллическая ј вне ASCII; латинский фильтр её не совпадёт
  CG5:
    TRIGGER: "the handle `@јenkins_ci` is the same account as @jenkins_ci"
    RESPONSE: CYRILLIC_JE_FORM ≠ VERIFICATION
    RULE: визуальное сходство не идентифицирует аккаунт
  CG6:
    TRIGGER: "swapping j→ј in an identifier is harmless"
    RESPONSE: CYRILLIC_JE_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
    RULE: в домене/логине/токене/пакете замена меняет сущность, в которую строка разрешается

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "јquery" (Cyrillic ј + Latin in one token)
      NAME: MIXED_SCRIPT_TOKEN
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: IDN/бренд/пакет-подделка; ключевой сигнал — СМЕШЕНИЕ письменностей внутри одного токена
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "јаvascript" (several Cyrillic among Latin)
      NAME: MULTI_HOMOGLYPH_TOKEN
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: множественная замена на целевое ключевое слово/бренд
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: не применимо — опасность знака появляется именно в последовательности (в токене), не в изоляции.

PHAGO_ENTITY_MIMICRY:
  PE_001:
    INPUT: "јquery.com"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: CRITICAL
    NOTE: кириллическая ј имитирует само ИМЯ верифицированного проекта/бренда (не просто структуру) — прямая мимикрия существования сущности. Поэтому реестр помечает знак PHAGO ●; коммерческие защиты от двойников часто упускают этот класс.
  PE_002:
    INPUT: "јsonwebtoken (package)"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: HIGH
    NOTE: выдача себя за официальное имя пакета через двойника в имени (typosquat цепочки поставок).

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена латинской j (U+006A) на кириллическую ј (U+0458) в имени бренда/пакета
  A2: смешение кириллической ј с греческой йот ϳ / математической sans-serif j для усложнения детекции
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: кириллическая ј обходит латинский блоклист ключевых слов (јackpot)
  B2: кириллическая ј в почтовом домене (team@projeсt-јoin.example) для фишинга
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: смешанный токен `јquery` (SC1) — письменности внутри одного слова
  C2: множественная замена `јаvascript` (SC2) на целевое ключевое слово
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: хэндл `@јenkins_ci` имитирует аккаунт проекта
  D2: "јoin-official" — двойник в псевдо-официальном имени
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: `јquery.com` — мимикрия имени проекта/бренда (PE_001)
  E2: `јsonwebtoken` — мимикрия официального пакета (PE_002)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у буквы нет спящих/активных эпох (см. раздел 5).
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: `јquery.com` with Cyrillic ј is the jQuery domain
  EXPECTED: FAIL_BRAND_NAME_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: a string with Cyrillic ј is machine-equal to its Latin spelling
  EXPECTED: FAIL_CODEPOINT_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: any Cyrillic ј in text is an attack
  EXPECTED: FAIL_OVERBLOCK_MIMICRY (обратная ошибка: настоящий сербский — не подделка)
  RESULT: FAIL
MUTATION_04:
  CLAIM: an ASCII filter on "jackpot" will catch "јackpot"
  EXPECTED: FAIL_ASCII_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: the handle `@јenkins_ci` is the same account as `@jenkins_ci`
  EXPECTED: FAIL_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: swapping j→ј in an identifier is harmless
  EXPECTED: FAIL_IDENTIFIER_INTERCHANGE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как отличить легитимный односкриптовый сербский/македонский текст от подделки без ложных срабатываний?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (правило «смешение письменностей внутри одного токена» — забота интегратора; см. прототип Vakhter confusable_cards.py)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует формулу LOOKS_SAME ≠ IS_SAME и правило «подделка = смешение, не присутствие».
OQ2:
  QUESTION: нужна ли полная таблица UTS #39 confusables + корпус брендов/пакетов для случая целой письменности?
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
