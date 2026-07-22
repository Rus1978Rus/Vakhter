PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_CYRILLIC_CAPITAL_U_U0423_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
TRANSLATION_NOTE: Русский оригинал (авторитетный источник). Английский документ SIGN_CORE_CARD_CYRILLIC_CAPITAL_U_U0423_GEN3_v0_3_EN — зеркало. Кодовые точки, имена полей и формулы идентичны. Гомоглиф: базовый закон — ВЫГЛЯДИТ_ОДИНАКОВО ≠ ЯВЛЯЕТСЯ_ТЕМ_ЖЕ. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_CYRILLIC_CAPITAL_U_U0423_GEN3_v0_3_RU
CODEPOINT: U+0423
VISIBLE_FORM: У
UNICODE_NAME: CYRILLIC CAPITAL LETTER U
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Руслан Малявский
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: кириллическая «У» (гомоглиф латинской заглавной Y; читается /у/)
CATEGORY_ROADMAP: PH (фишинг) · PHAGO: ● (сильный носитель — имитирует само имя бренда)

============================================================
3. REQUIRED_GENERAL_GUARDS
============================================================
REQUIRED_GENERAL_GUARDS:
  - SIGN_FALSE_EFFECT_MIMICRY_GUARD_v0_2A_RU
    GUARD_COMPATIBILITY: применимо — знак не создаёт полей-эффектов; для гомоглифа гард расширяется проверкой смешения письменностей на уровне интегратора
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
VISIBLE_FORM: У
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_LETTER_HOMOGLYPH
BASE_MODE_FORMULA: CYRILLIC_CAP_U_FORM ≠ LATIN_CAP_Y
SIGN_CATEGORY:
  - кириллическая заглавная буква «У» (звучит /у/, НЕ /y/; легитимна в русском / других кириллических письменностях)
  - гомоглиф латинской заглавной «Y» (U+0059)
  - потенциальный носитель гомоглифного / IDN-спуфинга при смешении письменностей

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_LATIN_CAP_Y — кириллическая У (U+0423) НЕ есть латинская Y (U+0059); другая кодовая точка И другой звук (/у/, а не /y/)
  2. NOT_SAME_STRING_AS_LATIN — строка с кириллической У не машинно-равна своему латинскому двойнику
  3. NOT_BRAND_NAME_PROOF — «УouTube» не доказывает связь с брендом YouTube
  4. NOT_DOMAIN_VALIDITY_PROOF — визуальное совпадение домена не подтверждает регистрируемый домен
  5. NOT_AUTHORITY — буква не подтверждает официальный статус
  6. NOT_VERIFICATION — не верифицирует соседний факт
  7. NOT_ASCII — не входит в ASCII; фильтры «только ASCII» не видят её как Y
  8. NOT_AUTOMATICALLY_SPOOF — в односкриптовом русском тексте она нормальна, не атака
  9. NOT_EXECUTION_TRIGGER — сама по себе ничего не запускает
  10. NOT_TRUST_SIGNAL — не повышает доверие к содержимому
  11. NOT_EFFECT — форма буквы не создаёт эффекта
  12. NOT_INTERCHANGEABLE_IN_IDENTIFIERS — в идентификаторе/домене замена Y→У меняет сущность

BASE_FORMULAS:
  CYRILLIC_CAP_U_FORM ≠ LATIN_CAP_Y
  CYRILLIC_CAP_U_FORM ≠ SAME_CODEPOINT_AS_LATIN
  CYRILLIC_CAP_U_FORM ≠ BRAND_NAME_PROOF
  CYRILLIC_CAP_U_FORM ≠ DOMAIN_VALIDITY_PROOF
  CYRILLIC_CAP_U_FORM ≠ AUTHORITY
  CYRILLIC_CAP_U_FORM ≠ VERIFICATION
  CYRILLIC_CAP_U_FORM ≠ ASCII_LETTER
  CYRILLIC_CAP_U_FORM ≠ AUTOMATICALLY_SPOOF
  CYRILLIC_CAP_U_FORM ≠ TRUST_SIGNAL
  CYRILLIC_CAP_U_FORM ≠ EFFECT
  CYRILLIC_CAP_U_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: кириллическая «У» — стабильная буква без культурной прецессии функций. Несовпадение «форма Y / звук У» — постоянное свойство, а не эпоха: буква читается /у/ в кириллице, выглядя как латинская Y. Опасность контекстна (смешение письменностей), а не эпохальна — поэтому SEMANTIC_EPOCH_TRACKER не применяется.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1 (физический жест)
  NOTE: буква — письменный знак без жестового предшественника; кириллица восходит к греческому уставу (письменная генеалогия).

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
    INPUT: "Уральские горы"
    CONTEXT: обычный русский текст (один скрипт)
    EXPECTED: INFO
    RISK: NONE
    GUARD: CYRILLIC_CAP_U_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_002:
    INPUT: "Ульяновск и Уфа"
    CONTEXT: русские топонимы
    EXPECTED: INFO
    RISK: NONE
    GUARD: CYRILLIC_CAP_U_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "Утро в лесу"
    CONTEXT: русские слова, где «У» — обычная заглавная
    EXPECTED: INFO
    RISK: NONE
    GUARD: CYRILLIC_CAP_U_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_004:
    INPUT: "Учебный год"
    CONTEXT: односкриптовая кириллическая фраза
    EXPECTED: INFO
    RISK: NONE
    GUARD: CYRILLIC_CAP_U_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "Университет и наука"
    CONTEXT: русские слова, начинающиеся на «У»
    EXPECTED: INFO
    RISK: NONE
    GUARD: CYRILLIC_CAP_U_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_006:
    INPUT: "Ульяна и Устинья"
    CONTEXT: два имени на «У», всё кириллица
    EXPECTED: INFO
    RISK: NONE
    GUARD: CYRILLIC_CAP_U_FORM ≠ AUTOMATICALLY_SPOOF

RISK_CASES:
  RISK_CASE_001:
    NAME: BRAND_HOMOGLYPH
    INPUT: "УouTube-login.com"
    CONTEXT: IDN/бренд-спуф — токен выглядит как YouTube, но первый символ кириллический
    RISK: CRITICAL
    ATTACK: замена латинской Y на кириллическую У даёт визуально идентичный бренд, который регистрирует атакующий
    GUARD: CYRILLIC_CAP_U_FORM ≠ LATIN_CAP_Y
  RISK_CASE_002:
    NAME: ALLCAPS_BRAND_SUBSTITUTION
    INPUT: "УAHOO-mail-alert.com"
    CONTEXT: ведущая подмена в капслок-названии бренда
    RISK: CRITICAL
    ATTACK: строка машинно-≠ YAHOO, но человек не видит разницы
    GUARD: CYRILLIC_CAP_U_FORM ≠ DOMAIN_VALIDITY_PROOF
  RISK_CASE_003:
    NAME: HANDLE_IMPERSONATION
    INPUT: "@УelpSupport"
    CONTEXT: имперсонация бренд-аккаунта в чате/соцсети
    RISK: HIGH
    ATTACK: похожий хэндл выглядит как YelpSupport, но это другой аккаунт
    GUARD: CYRILLIC_CAP_U_FORM ≠ VERIFICATION
  RISK_CASE_004:
    NAME: FILTER_BYPASS_KEYWORD
    INPUT: "УES"
    CONTEXT: обход текстового фильтра, ищущего латинское слово
    RISK: HIGH
    ATTACK: одна подменённая буква выводит слово из-под блок-листа
    GUARD: CYRILLIC_CAP_U_FORM ≠ ASCII_LETTER
  RISK_CASE_005:
    NAME: EMAIL_LOOKALIKE
    INPUT: "no-reply@Уandex-secure.example"
    CONTEXT: фишинговое письмо от «той же» компании
    RISK: HIGH
    ATTACK: домен выглядит идентично, но ведёт к атакующему
    GUARD: CYRILLIC_CAP_U_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
  RISK_CASE_006:
    NAME: MULTI_HOMOGLYPH_ON_TARGET
    INPUT: "УМCA"
    CONTEXT: кириллические У и М перед латинскими CA, имитирующие YMCA (У и М кириллица, CA латиница — смешение письменностей)
    RISK: HIGH
    ATTACK: цепочка двойников имитирует всю латинскую аббревиатуру
    GUARD: CYRILLIC_CAP_U_FORM ≠ BRAND_NAME_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: Y
    CODEPOINT: U+0059
    NAME: LATIN CAPITAL LETTER Y
    RISK: CRITICAL
    RULE: LATIN_CAP_Y ≠ CYRILLIC_CAP_U (главная цель имперсонации; визуально идентична во многих шрифтах)
  CONFUSABLE_002:
    VISIBLE_FORM: Υ
    CODEPOINT: U+03A5
    NAME: GREEK CAPITAL LETTER UPSILON
    RISK: HIGH
    RULE: GREEK_CAP_UPSILON ≠ CYRILLIC_CAP_U (третий скрипт с той же формой Y; усложняет детекцию)
  CONFUSABLE_003:
    VISIBLE_FORM: 𝗬
    CODEPOINT: U+1D5EC
    NAME: MATHEMATICAL SANS-SERIF BOLD CAPITAL Y
    RISK: MEDIUM
    RULE: MATH_SANS_CAP_Y ≠ CYRILLIC_CAP_U (математически-стилизованная латинская Y для обхода простых фильтров)
  CONFUSABLE_004:
    VISIBLE_FORM: Ｙ
    CODEPOINT: U+FF39
    NAME: FULLWIDTH LATIN CAPITAL LETTER Y
    RISK: MEDIUM
    RULE: FULLWIDTH_CAP_Y ≠ CYRILLIC_CAP_U (полноширинная латинская Y; другая форма совместимости)
  CONFUSABLE_005:
    VISIBLE_FORM: Ɏ
    CODEPOINT: U+024E
    NAME: LATIN CAPITAL LETTER Y WITH STROKE
    RISK: LOW
    RULE: LATIN_CAP_Y_STROKE ≠ CYRILLIC_CAP_U (латинский двойник Y с диакритикой)
  CONFUSABLE_006:
    VISIBLE_FORM: Ұ
    CODEPOINT: U+04B0
    NAME: CYRILLIC CAPITAL LETTER STRAIGHT U WITH STROKE
    RISK: LOW
    RULE: CYRILLIC_STRAIGHT_U_STROKE ≠ CYRILLIC_CAP_U (родственная кириллическая буква; отдельный знак, не этот)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: «бренд `УouTube` — это YouTube»
    RESPONSE: CYRILLIC_CAP_U_FORM ≠ LATIN_CAP_Y
    RULE: первый символ — кириллическая У (/у/); регистрируемый домен/имя другой — решает DNS, а не глаз
  CG2:
    TRIGGER: «строка с кириллической У равна её латинскому написанию»
    RESPONSE: CYRILLIC_CAP_U_FORM ≠ SAME_CODEPOINT_AS_LATIN
    RULE: разные кодовые точки → машинно-разные строки
  CG3:
    TRIGGER: «любая кириллическая У в тексте — атака»
    RESPONSE: CYRILLIC_CAP_U_FORM ≠ AUTOMATICALLY_SPOOF
    RULE: в односкриптовом русском тексте буква легитимна; спуф — это СМЕШЕНИЕ письменностей в одном токене
  CG4:
    TRIGGER: «ASCII-фильтр поймает подменённое слово»
    RESPONSE: CYRILLIC_CAP_U_FORM ≠ ASCII_LETTER
    RULE: кириллическая У вне ASCII; латинский фильтр её не сматчит
  CG5:
    TRIGGER: «хэндл `@УelpSupport` — тот же аккаунт, что и @YelpSupport»
    RESPONSE: CYRILLIC_CAP_U_FORM ≠ VERIFICATION
    RULE: визуальное сходство не идентифицирует аккаунт
  CG6:
    TRIGGER: «замена Y→У в идентификаторе безвредна»
    RESPONSE: CYRILLIC_CAP_U_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
    RULE: в домене/логине/токене замена меняет сущность, к которой резолвится строка

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "УouTube" (кириллическая У + латиница в одном токене)
      NAME: MIXED_SCRIPT_TOKEN
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: IDN/бренд-спуф; ключевой сигнал — СМЕШЕНИЕ письменностей внутри одного токена
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "УМCA" (кириллические У и М перед латинскими CA)
      NAME: MULTI_HOMOGLYPH_TOKEN
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: множественная подмена на целевую капслок-аббревиатуру
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: не применимо — опасность знака проявляется именно в последовательности (в токене), а не в изоляции.

PHAGO_ENTITY_MIMICRY:
  PE_001:
    INPUT: "УouTube-login.com"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: CRITICAL
    NOTE: кириллическая У имитирует само ИМЯ верифицированного бренда (а не только структуру) — прямая имитация существования сущности. Поэтому реестр помечает знак PHAGO ●; коммерческие защиты от двойников этот класс часто пропускают.
  PE_002:
    INPUT: "@УelpSupport"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: HIGH
    NOTE: имперсонация официального аккаунта поддержки бренда через двойника в имени.

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена латинской Y (U+0059) на кириллическую У (U+0423) в домене бренда
  A2: смешение кириллической У с греческой Upsilon Υ / математической sans-serif Y для усложнения детекции
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: кириллическая У обходит латинский блок-лист ключевых слов (УES)
  B2: кириллическая У в почтовом домене (no-reply@Уandex-secure.example) для фишинга
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: смешанный токен `УouTube` (SC1) — письменности внутри одного слова
  C2: множественная подмена `УМCA` (SC2) на целевую аббревиатуру
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: хэндл `@УelpSupport` имитирует бренд-аккаунт
  D2: "Уandex-secure" — двойник в псевдо-официальном имени
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: `УouTube-login.com` — имитация имени бренда (PE_001)
  E2: `@УelpSupport` — имитация официального аккаунта (PE_002)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, буква не имеет спящих/активных эпох (см. раздел 5).
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: `УouTube-login.com` с кириллической У — это домен YouTube
  EXPECTED: FAIL_BRAND_NAME_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: строка с кириллической У машинно-равна её латинскому написанию
  EXPECTED: FAIL_CODEPOINT_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: любая кириллическая У в тексте — атака
  EXPECTED: FAIL_OVERBLOCK_MIMICRY (обратная ошибка: подлинный русский — не спуф)
  RESULT: FAIL
MUTATION_04:
  CLAIM: ASCII-фильтр на "YES" поймает "УES"
  EXPECTED: FAIL_ASCII_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: хэндл `@УelpSupport` — тот же аккаунт, что и `@YelpSupport`
  EXPECTED: FAIL_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: замена Y→У в идентификаторе безвредна
  EXPECTED: FAIL_IDENTIFIER_INTERCHANGE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как отличить легитимный односкриптовый русский текст от спуфа без ложных срабатываний?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (правило «смешение письменностей внутри одного токена» — забота интегратора; см. прототип Vakhter confusable_cards.py)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует формулу LOOKS_SAME ≠ IS_SAME и правило «спуф = смешение, а не присутствие».
OQ2:
  QUESTION: нужна ли полная таблица UTS #39 confusables + корпус брендов для случая целого скрипта?
  STATUS: OPEN
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: делегировано рантайму/интегратору.
ALL_OPEN_QUESTIONS_CLOSED: NO (делегировано, не блокирует)

============================================================
11. PATCH_HISTORY
============================================================
PATCH_HISTORY:
  v0_1_PATCH_01: первичное создание (Руслан Малявский, 2026-07-22) — черновик из шаблона GEN3_v0_3 (Vakhter), знак-гомоглиф; не прогон конвейера.
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
