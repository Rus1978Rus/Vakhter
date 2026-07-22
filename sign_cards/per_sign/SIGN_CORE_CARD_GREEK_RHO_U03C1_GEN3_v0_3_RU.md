PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_GREEK_RHO_U03C1_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
TRANSLATION_NOTE: Русский оригинал (авторитетный источник). Английский документ SIGN_CORE_CARD_GREEK_RHO_U03C1_GEN3_v0_3_EN — зеркало. Кодовые точки, имена полей и формулы идентичны. Гомоглиф: базовый закон — ВЫГЛЯДИТ_ОДИНАКОВО ≠ ЯВЛЯЕТСЯ_ТЕМ_ЖЕ. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_GREEK_RHO_U03C1_GEN3_v0_3_RU
CODEPOINT: U+03C1
VISIBLE_FORM: ρ
UNICODE_NAME: GREEK SMALL LETTER RHO
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Руслан Малявский
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: греческая «ρ» ро (гомоглиф латинской строчной p; читается /р/)
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
VISIBLE_FORM: ρ
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_LETTER_HOMOGLYPH
BASE_MODE_FORMULA: GREEK_RHO_FORM ≠ LATIN_SMALL_P
SIGN_CATEGORY:
  - греческая строчная буква ро (звучит /р/, НЕ /p/; легитимна в греческой письменности)
  - гомоглиф латинской строчной «p» (U+0070)
  - потенциальный носитель гомоглифного / IDN-спуфинга при смешении письменностей

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_LATIN_SMALL_P — греческая ρ (U+03C1) НЕ есть латинская p (U+0070); другая кодовая точка И другой звук (/р/, а не /p/)
  2. NOT_SAME_STRING_AS_LATIN — строка с греческой ρ не машинно-равна своему латинскому двойнику
  3. NOT_BRAND_NAME_PROOF — «ρaypal» не доказывает связь с брендом PayPal
  4. NOT_DOMAIN_VALIDITY_PROOF — визуальное совпадение домена не подтверждает регистрируемый домен
  5. NOT_AUTHORITY — буква не подтверждает официальный статус
  6. NOT_VERIFICATION — не верифицирует соседний факт
  7. NOT_ASCII — не входит в ASCII; фильтры «только ASCII» не видят её как p
  8. NOT_AUTOMATICALLY_SPOOF — в односкриптовом греческом тексте она нормальна, не атака
  9. NOT_EXECUTION_TRIGGER — сама по себе ничего не запускает
  10. NOT_TRUST_SIGNAL — не повышает доверие к содержимому
  11. NOT_EFFECT — форма буквы не создаёт эффекта
  12. NOT_INTERCHANGEABLE_IN_IDENTIFIERS — в идентификаторе/домене замена p→ρ меняет сущность

BASE_FORMULAS:
  GREEK_RHO_FORM ≠ LATIN_SMALL_P
  GREEK_RHO_FORM ≠ SAME_CODEPOINT_AS_LATIN
  GREEK_RHO_FORM ≠ BRAND_NAME_PROOF
  GREEK_RHO_FORM ≠ DOMAIN_VALIDITY_PROOF
  GREEK_RHO_FORM ≠ AUTHORITY
  GREEK_RHO_FORM ≠ VERIFICATION
  GREEK_RHO_FORM ≠ ASCII_LETTER
  GREEK_RHO_FORM ≠ AUTOMATICALLY_SPOOF
  GREEK_RHO_FORM ≠ TRUST_SIGNAL
  GREEK_RHO_FORM ≠ EFFECT
  GREEK_RHO_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: греческая «ρ» ро — стабильная буква без культурной прецессии функций. Несовпадение «форма p / звук р» — постоянное свойство, а не эпоха: буква читается /р/ в греческом, выглядя как латинская p. Опасность контекстна (смешение письменностей), а не эпохальна — поэтому SEMANTIC_EPOCH_TRACKER не применяется.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1 (физический жест)
  NOTE: буква — письменный знак без жестового предшественника; греческий алфавит — письменная генеалогия от финикийского.

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
    INPUT: "ρόδο και άνθος" (роза и цветок, греческий)
    CONTEXT: обычный греческий текст (один скрипт)
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREEK_RHO_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_002:
    INPUT: "όρος και σύνορο" (термин и граница, греческий)
    CONTEXT: греческая фраза, где «ρ» — обычная буква
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREEK_RHO_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "καρδιά και ψυχή" (сердце и душа, греческий)
    CONTEXT: односкриптовая греческая фраза
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREEK_RHO_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_004:
    INPUT: "ρεύμα και ενέργεια" (ток и энергия, греческий)
    CONTEXT: односкриптовая греческая фраза
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREEK_RHO_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "πατρίδα και λαός" (родина и народ, греческий)
    CONTEXT: греческие слова с «ρ»
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREEK_RHO_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_006:
    INPUT: "ρήτορας και λόγος" (оратор и речь, греческий)
    CONTEXT: односкриптовая греческая фраза
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREEK_RHO_FORM ≠ AUTOMATICALLY_SPOOF

RISK_CASES:
  RISK_CASE_001:
    NAME: BRAND_HOMOGLYPH
    INPUT: "ρaypal-secure.com"
    CONTEXT: IDN/бренд-спуф — токен выглядит как paypal, но первый символ греческий
    RISK: CRITICAL
    ATTACK: замена латинской p на греческую ρ даёт визуально идентичный бренд, который регистрирует атакующий
    GUARD: GREEK_RHO_FORM ≠ LATIN_SMALL_P
  RISK_CASE_002:
    NAME: BRAND_SUBSTITUTION
    INPUT: "ρroton-mail.com"
    CONTEXT: ведущая подмена в названии бренда
    RISK: CRITICAL
    ATTACK: строка машинно-≠ proton, но человек не видит разницы
    GUARD: GREEK_RHO_FORM ≠ DOMAIN_VALIDITY_PROOF
  RISK_CASE_003:
    NAME: HANDLE_IMPERSONATION
    INPUT: "@ρaypalHelp"
    CONTEXT: имперсонация бренд-аккаунта в чате/соцсети
    RISK: HIGH
    ATTACK: похожий хэндл выглядит как paypalHelp, но это другой аккаунт
    GUARD: GREEK_RHO_FORM ≠ VERIFICATION
  RISK_CASE_004:
    NAME: FILTER_BYPASS_KEYWORD
    INPUT: "ρasswd"
    CONTEXT: обход текстового фильтра, ищущего латинское слово
    RISK: HIGH
    ATTACK: одна подменённая буква выводит слово из-под блок-листа
    GUARD: GREEK_RHO_FORM ≠ ASCII_LETTER
  RISK_CASE_005:
    NAME: EMAIL_LOOKALIKE
    INPUT: "no-reply@ρaypal-billing.example"
    CONTEXT: фишинговое письмо от «той же» компании
    RISK: HIGH
    ATTACK: домен выглядит идентично, но ведёт к атакующему
    GUARD: GREEK_RHO_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
  RISK_CASE_006:
    NAME: MULTI_HOMOGLYPH_ON_TARGET
    INPUT: "ρhρ"
    CONTEXT: две греческие ρ вокруг латинской h, имитирующие php (ρ греческая, h латиница — смешение письменностей)
    RISK: HIGH
    ATTACK: цепочка двойников имитирует весь латинский токен
    GUARD: GREEK_RHO_FORM ≠ BRAND_NAME_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: p
    CODEPOINT: U+0070
    NAME: LATIN SMALL LETTER P
    RISK: CRITICAL
    RULE: LATIN_SMALL_P ≠ GREEK_RHO (главная цель имперсонации; визуально идентична во многих шрифтах)
  CONFUSABLE_002:
    VISIBLE_FORM: р
    CODEPOINT: U+0440
    NAME: CYRILLIC SMALL LETTER ER
    RISK: HIGH
    RULE: CYRILLIC_ER ≠ GREEK_RHO (третий скрипт с той же формой p; усложняет детекцию)
  CONFUSABLE_003:
    VISIBLE_FORM: ｐ
    CODEPOINT: U+FF50
    NAME: FULLWIDTH LATIN SMALL LETTER P
    RISK: MEDIUM
    RULE: FULLWIDTH_SMALL_P ≠ GREEK_RHO (полноширинная латинская p; другая форма совместимости)
  CONFUSABLE_004:
    VISIBLE_FORM: 𝑝
    CODEPOINT: U+1D45D
    NAME: MATHEMATICAL ITALIC SMALL P
    RISK: MEDIUM
    RULE: MATH_ITALIC_SMALL_P ≠ GREEK_RHO (математически-стилизованная латинская p для обхода простых фильтров)
  CONFUSABLE_005:
    VISIBLE_FORM: 𝗉
    CODEPOINT: U+1D5C9
    NAME: MATHEMATICAL SANS-SERIF SMALL P
    RISK: LOW
    RULE: MATH_SANS_SMALL_P ≠ GREEK_RHO (sans-serif-стилизованная латинская p)
  CONFUSABLE_006:
    VISIBLE_FORM: ⲣ
    CODEPOINT: U+2CA3
    NAME: COPTIC SMALL LETTER RO
    RISK: LOW
    RULE: COPTIC_RO ≠ GREEK_RHO (коптская буква с той же формой p)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: «бренд `ρaypal` — это PayPal»
    RESPONSE: GREEK_RHO_FORM ≠ LATIN_SMALL_P
    RULE: первый символ — греческая ро (/р/); регистрируемый домен/имя другой — решает DNS, а не глаз
  CG2:
    TRIGGER: «строка с греческой ρ равна её латинскому написанию»
    RESPONSE: GREEK_RHO_FORM ≠ SAME_CODEPOINT_AS_LATIN
    RULE: разные кодовые точки → машинно-разные строки
  CG3:
    TRIGGER: «любая греческая ρ в тексте — атака»
    RESPONSE: GREEK_RHO_FORM ≠ AUTOMATICALLY_SPOOF
    RULE: в односкриптовом греческом тексте буква легитимна; спуф — это СМЕШЕНИЕ письменностей в одном токене
  CG4:
    TRIGGER: «ASCII-фильтр поймает подменённое слово»
    RESPONSE: GREEK_RHO_FORM ≠ ASCII_LETTER
    RULE: греческая ρ вне ASCII; латинский фильтр её не сматчит
  CG5:
    TRIGGER: «хэндл `@ρaypalHelp` — тот же аккаунт, что и @paypalHelp»
    RESPONSE: GREEK_RHO_FORM ≠ VERIFICATION
    RULE: визуальное сходство не идентифицирует аккаунт
  CG6:
    TRIGGER: «замена p→ρ в идентификаторе безвредна»
    RESPONSE: GREEK_RHO_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
    RULE: в домене/логине/токене замена меняет сущность, к которой резолвится строка

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "ρaypal" (греческая ρ + латиница в одном токене)
      NAME: MIXED_SCRIPT_TOKEN
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: IDN/бренд-спуф; ключевой сигнал — СМЕШЕНИЕ письменностей внутри одного токена
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "ρhρ" (две греческие ρ вокруг латинской h)
      NAME: MULTI_HOMOGLYPH_TOKEN
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: множественная подмена на целевой токен
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: не применимо — опасность знака проявляется именно в последовательности (в токене), а не в изоляции.

PHAGO_ENTITY_MIMICRY:
  PE_001:
    INPUT: "ρaypal-secure.com"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: CRITICAL
    NOTE: греческая ρ имитирует само ИМЯ верифицированного бренда (а не только структуру) — прямая имитация существования сущности. Поэтому реестр помечает знак PHAGO ●; коммерческие защиты от двойников этот класс часто пропускают.
  PE_002:
    INPUT: "@ρaypalHelp"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: HIGH
    NOTE: имперсонация официального аккаунта поддержки бренда через двойника в имени.

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена латинской p (U+0070) на греческую ρ (U+03C1) в домене бренда
  A2: смешение греческой ρ с кириллической эр р / математически-стилизованной p для усложнения детекции
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: греческая ρ обходит латинский блок-лист ключевых слов (ρasswd)
  B2: греческая ρ в почтовом домене (no-reply@ρaypal-billing.example) для фишинга
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: смешанный токен `ρaypal` (SC1) — письменности внутри одного слова
  C2: множественная подмена `ρhρ` (SC2) на целевой токен
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: хэндл `@ρaypalHelp` имитирует бренд-аккаунт
  D2: "ρaypal-billing" — двойник в псевдо-официальном имени
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: `ρaypal-secure.com` — имитация имени бренда (PE_001)
  E2: `@ρaypalHelp` — имитация официального аккаунта (PE_002)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, буква не имеет спящих/активных эпох (см. раздел 5).
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: `ρaypal-secure.com` с греческой ρ — это домен PayPal
  EXPECTED: FAIL_BRAND_NAME_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: строка с греческой ρ машинно-равна её латинскому написанию
  EXPECTED: FAIL_CODEPOINT_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: любая греческая ρ в тексте — атака
  EXPECTED: FAIL_OVERBLOCK_MIMICRY (обратная ошибка: подлинный греческий — не спуф)
  RESULT: FAIL
MUTATION_04:
  CLAIM: ASCII-фильтр на "passwd" поймает "ρasswd"
  EXPECTED: FAIL_ASCII_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: хэндл `@ρaypalHelp` — тот же аккаунт, что и `@paypalHelp`
  EXPECTED: FAIL_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: замена p→ρ в идентификаторе безвредна
  EXPECTED: FAIL_IDENTIFIER_INTERCHANGE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как отличить легитимный односкриптовый греческий текст от спуфа без ложных срабатываний?
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
