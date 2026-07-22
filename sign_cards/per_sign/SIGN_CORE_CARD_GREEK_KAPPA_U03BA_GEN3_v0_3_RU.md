PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_GREEK_KAPPA_U03BA_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
TRANSLATION_NOTE: Русский оригинал (авторитетный источник). Английский документ SIGN_CORE_CARD_GREEK_KAPPA_U03BA_GEN3_v0_3_EN — зеркало. Кодовые точки, имена полей и формулы идентичны. Гомоглиф: базовый закон — ВЫГЛЯДИТ_ОДИНАКОВО ≠ ЯВЛЯЕТСЯ_ТЕМ_ЖЕ. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_GREEK_KAPPA_U03BA_GEN3_v0_3_RU
CODEPOINT: U+03BA
VISIBLE_FORM: κ
UNICODE_NAME: GREEK SMALL LETTER KAPPA
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Руслан Малявский
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: греческая «κ» каппа (гомоглиф латинской строчной k; читается /к/)
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
VISIBLE_FORM: κ
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_LETTER_HOMOGLYPH
BASE_MODE_FORMULA: GREEK_KAPPA_FORM ≠ LATIN_SMALL_K
SIGN_CATEGORY:
  - греческая строчная буква каппа (звучит /к/; легитимна в греческой письменности)
  - гомоглиф латинской строчной «k» (U+006B)
  - потенциальный носитель гомоглифного / IDN-спуфинга при смешении письменностей

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_LATIN_SMALL_K — греческая κ (U+03BA) НЕ есть латинская k (U+006B); другая кодовая точка в другой письменности
  2. NOT_SAME_STRING_AS_LATIN — строка с греческой κ не машинно-равна своему латинскому двойнику
  3. NOT_BRAND_NAME_PROOF — «κaspersky» не доказывает связь с брендом Kaspersky
  4. NOT_DOMAIN_VALIDITY_PROOF — визуальное совпадение домена не подтверждает регистрируемый домен
  5. NOT_AUTHORITY — буква не подтверждает официальный статус
  6. NOT_VERIFICATION — не верифицирует соседний факт
  7. NOT_ASCII — не входит в ASCII; фильтры «только ASCII» не видят её как k
  8. NOT_AUTOMATICALLY_SPOOF — в односкриптовом греческом тексте она нормальна, не атака
  9. NOT_EXECUTION_TRIGGER — сама по себе ничего не запускает
  10. NOT_TRUST_SIGNAL — не повышает доверие к содержимому
  11. NOT_EFFECT — форма буквы не создаёт эффекта
  12. NOT_INTERCHANGEABLE_IN_IDENTIFIERS — в идентификаторе/домене замена k→κ меняет сущность

BASE_FORMULAS:
  GREEK_KAPPA_FORM ≠ LATIN_SMALL_K
  GREEK_KAPPA_FORM ≠ SAME_CODEPOINT_AS_LATIN
  GREEK_KAPPA_FORM ≠ BRAND_NAME_PROOF
  GREEK_KAPPA_FORM ≠ DOMAIN_VALIDITY_PROOF
  GREEK_KAPPA_FORM ≠ AUTHORITY
  GREEK_KAPPA_FORM ≠ VERIFICATION
  GREEK_KAPPA_FORM ≠ ASCII_LETTER
  GREEK_KAPPA_FORM ≠ AUTOMATICALLY_SPOOF
  GREEK_KAPPA_FORM ≠ TRUST_SIGNAL
  GREEK_KAPPA_FORM ≠ EFFECT
  GREEK_KAPPA_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: греческая «κ» каппа — стабильная буква без культурной прецессии функций. «Гомоглиф» — не эпоха, а свойство визуального совпадения с латинской k, сосуществующее с легитимной функцией буквы. Опасность контекстна (смешение письменностей), а не эпохальна — поэтому SEMANTIC_EPOCH_TRACKER не применяется.
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
    INPUT: "καλημέρα κόσμε" (доброе утро мир, греческий)
    CONTEXT: обычный греческий текст (один скрипт)
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREEK_KAPPA_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_002:
    INPUT: "κόσμος και φύση" (мир и природа, греческий)
    CONTEXT: греческая фраза, где «κ» — обычная буква
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREEK_KAPPA_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "καρδιά και ψυχή" (сердце и душа, греческий)
    CONTEXT: односкриптовая греческая фраза
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREEK_KAPPA_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_004:
    INPUT: "κύκλος και γραμμή" (круг и линия, греческий)
    CONTEXT: односкриптовая греческая фраза с «κ»
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREEK_KAPPA_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "κιθάρα και τραγούδι" (гитара и песня, греческий)
    CONTEXT: греческие слова с «κ»
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREEK_KAPPA_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_006:
    INPUT: "καλό και κακό" (добро и зло, греческий)
    CONTEXT: односкриптовая греческая фраза
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREEK_KAPPA_FORM ≠ AUTOMATICALLY_SPOOF

RISK_CASES:
  RISK_CASE_001:
    NAME: BRAND_HOMOGLYPH
    INPUT: "κaspersky-login.com"
    CONTEXT: IDN/бренд-спуф — токен выглядит как kaspersky, но первый символ греческий
    RISK: CRITICAL
    ATTACK: замена латинской k на греческую κ даёт визуально идентичный бренд, который регистрирует атакующий
    GUARD: GREEK_KAPPA_FORM ≠ LATIN_SMALL_K
  RISK_CASE_002:
    NAME: BRAND_SUBSTITUTION
    INPUT: "κraken-exchange.com"
    CONTEXT: ведущая подмена в названии бренда
    RISK: CRITICAL
    ATTACK: строка машинно-≠ kraken, но человек не видит разницы
    GUARD: GREEK_KAPPA_FORM ≠ DOMAIN_VALIDITY_PROOF
  RISK_CASE_003:
    NAME: HANDLE_IMPERSONATION
    INPUT: "@κrakenHelp"
    CONTEXT: имперсонация бренд-аккаунта в чате/соцсети
    RISK: HIGH
    ATTACK: похожий хэндл выглядит как krakenHelp, но это другой аккаунт
    GUARD: GREEK_KAPPA_FORM ≠ VERIFICATION
  RISK_CASE_004:
    NAME: FILTER_BYPASS_KEYWORD
    INPUT: "κill"
    CONTEXT: обход текстового фильтра, ищущего латинское слово
    RISK: HIGH
    ATTACK: одна подменённая буква выводит слово из-под блок-листа
    GUARD: GREEK_KAPPA_FORM ≠ ASCII_LETTER
  RISK_CASE_005:
    NAME: EMAIL_LOOKALIKE
    INPUT: "no-reply@κohls-deals.example"
    CONTEXT: фишинговое письмо от «той же» компании
    RISK: HIGH
    ATTACK: домен выглядит идентично, но ведёт к атакующему
    GUARD: GREEK_KAPPA_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
  RISK_CASE_006:
    NAME: MULTI_HOMOGLYPH_ON_TARGET
    INPUT: "κiκ"
    CONTEXT: две греческие κ вокруг латинской i, имитирующие kik (κ греческая, i латиница — смешение письменностей)
    RISK: HIGH
    ATTACK: цепочка двойников имитирует всё латинское слово
    GUARD: GREEK_KAPPA_FORM ≠ BRAND_NAME_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: k
    CODEPOINT: U+006B
    NAME: LATIN SMALL LETTER K
    RISK: CRITICAL
    RULE: LATIN_SMALL_K ≠ GREEK_KAPPA (главная цель имперсонации; визуально схожа во многих шрифтах)
  CONFUSABLE_002:
    VISIBLE_FORM: к
    CODEPOINT: U+043A
    NAME: CYRILLIC SMALL LETTER KA
    RISK: HIGH
    RULE: CYRILLIC_KA ≠ GREEK_KAPPA (третий скрипт с той же формой k; усложняет детекцию)
  CONFUSABLE_003:
    VISIBLE_FORM: ｋ
    CODEPOINT: U+FF4B
    NAME: FULLWIDTH LATIN SMALL LETTER K
    RISK: MEDIUM
    RULE: FULLWIDTH_SMALL_K ≠ GREEK_KAPPA (полноширинная латинская k; другая форма совместимости)
  CONFUSABLE_004:
    VISIBLE_FORM: 𝑘
    CODEPOINT: U+1D458
    NAME: MATHEMATICAL ITALIC SMALL K
    RISK: MEDIUM
    RULE: MATH_ITALIC_SMALL_K ≠ GREEK_KAPPA (математически-стилизованная латинская k для обхода простых фильтров)
  CONFUSABLE_005:
    VISIBLE_FORM: 𝗄
    CODEPOINT: U+1D5C4
    NAME: MATHEMATICAL SANS-SERIF SMALL K
    RISK: LOW
    RULE: MATH_SANS_SMALL_K ≠ GREEK_KAPPA (sans-serif-стилизованная латинская k)
  CONFUSABLE_006:
    VISIBLE_FORM: ⲕ
    CODEPOINT: U+2C95
    NAME: COPTIC SMALL LETTER KAPA
    RISK: LOW
    RULE: COPTIC_KAPA ≠ GREEK_KAPPA (коптская буква с той же формой k)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: «бренд `κaspersky` — это Kaspersky»
    RESPONSE: GREEK_KAPPA_FORM ≠ LATIN_SMALL_K
    RULE: первый символ — греческая каппа; регистрируемый домен/имя другой — решает DNS, а не глаз
  CG2:
    TRIGGER: «строка с греческой κ равна её латинскому написанию»
    RESPONSE: GREEK_KAPPA_FORM ≠ SAME_CODEPOINT_AS_LATIN
    RULE: разные кодовые точки → машинно-разные строки
  CG3:
    TRIGGER: «любая греческая κ в тексте — атака»
    RESPONSE: GREEK_KAPPA_FORM ≠ AUTOMATICALLY_SPOOF
    RULE: в односкриптовом греческом тексте буква легитимна; спуф — это СМЕШЕНИЕ письменностей в одном токене
  CG4:
    TRIGGER: «ASCII-фильтр поймает подменённое слово»
    RESPONSE: GREEK_KAPPA_FORM ≠ ASCII_LETTER
    RULE: греческая κ вне ASCII; латинский фильтр её не сматчит
  CG5:
    TRIGGER: «хэндл `@κrakenHelp` — тот же аккаунт, что и @krakenHelp»
    RESPONSE: GREEK_KAPPA_FORM ≠ VERIFICATION
    RULE: визуальное сходство не идентифицирует аккаунт
  CG6:
    TRIGGER: «замена k→κ в идентификаторе безвредна»
    RESPONSE: GREEK_KAPPA_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
    RULE: в домене/логине/токене замена меняет сущность, к которой резолвится строка

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "κaspersky" (греческая κ + латиница в одном токене)
      NAME: MIXED_SCRIPT_TOKEN
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: IDN/бренд-спуф; ключевой сигнал — СМЕШЕНИЕ письменностей внутри одного токена
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "κiκ" (две греческие κ вокруг латинской i)
      NAME: MULTI_HOMOGLYPH_TOKEN
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: множественная подмена на целевое слово
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: не применимо — опасность знака проявляется именно в последовательности (в токене), а не в изоляции.

PHAGO_ENTITY_MIMICRY:
  PE_001:
    INPUT: "κaspersky-login.com"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: CRITICAL
    NOTE: греческая κ имитирует само ИМЯ верифицированного бренда (а не только структуру) — прямая имитация существования сущности. Поэтому реестр помечает знак PHAGO ●; коммерческие защиты от двойников этот класс часто пропускают.
  PE_002:
    INPUT: "@κrakenHelp"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: HIGH
    NOTE: имперсонация официального аккаунта поддержки бренда через двойника в имени.

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена латинской k (U+006B) на греческую κ (U+03BA) в домене бренда
  A2: смешение греческой κ с кириллической ка к / математически-стилизованной k для усложнения детекции
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: греческая κ обходит латинский блок-лист ключевых слов (κill)
  B2: греческая κ в почтовом домене (no-reply@κohls-deals.example) для фишинга
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: смешанный токен `κaspersky` (SC1) — письменности внутри одного слова
  C2: множественная подмена `κiκ` (SC2) на целевое слово
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: хэндл `@κrakenHelp` имитирует бренд-аккаунт
  D2: "κohls-deals" — двойник в псевдо-официальном имени
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: `κaspersky-login.com` — имитация имени бренда (PE_001)
  E2: `@κrakenHelp` — имитация официального аккаунта (PE_002)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, буква не имеет спящих/активных эпох (см. раздел 5).
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: `κaspersky-login.com` с греческой κ — это домен Kaspersky
  EXPECTED: FAIL_BRAND_NAME_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: строка с греческой κ машинно-равна её латинскому написанию
  EXPECTED: FAIL_CODEPOINT_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: любая греческая κ в тексте — атака
  EXPECTED: FAIL_OVERBLOCK_MIMICRY (обратная ошибка: подлинный греческий — не спуф)
  RESULT: FAIL
MUTATION_04:
  CLAIM: ASCII-фильтр на "kill" поймает "κill"
  EXPECTED: FAIL_ASCII_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: хэндл `@κrakenHelp` — тот же аккаунт, что и `@krakenHelp`
  EXPECTED: FAIL_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: замена k→κ в идентификаторе безвредна
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
