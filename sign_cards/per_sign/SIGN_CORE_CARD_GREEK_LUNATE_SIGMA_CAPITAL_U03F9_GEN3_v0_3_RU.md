PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_GREEK_LUNATE_SIGMA_CAPITAL_U03F9_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
TRANSLATION_NOTE: Русский оригинал (авторитетный источник). Английский документ SIGN_CORE_CARD_GREEK_LUNATE_SIGMA_CAPITAL_U03F9_GEN3_v0_3_EN — зеркало. Кодовые точки, имена полей и формулы идентичны. Гомоглиф: базовый закон — ВЫГЛЯДИТ_ОДИНАКОВО ≠ ЯВЛЯЕТСЯ_ТЕМ_ЖЕ. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_GREEK_LUNATE_SIGMA_CAPITAL_U03F9_GEN3_v0_3_RU
CODEPOINT: U+03F9
VISIBLE_FORM: Ϲ
UNICODE_NAME: GREEK CAPITAL LUNATE SIGMA SYMBOL
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Руслан Малявский
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: греческая «Ϲ» заглавная лунная сигма (гомоглиф латинской заглавной C; читается /с/, а не /к/)
CATEGORY_ROADMAP: PH (фишинг) · PHAGO: ● (сильный носитель — имитирует само имя бренда)

============================================================
3. REQUIRED_GENERAL_GUARDS
============================================================
REQUIRED_GENERAL_GUARDS:
  - SIGN_FALSE_EFFECT_MIMICRY_GUARD_v0_2A_RU
    GUARD_COMPATIBILITY: applicable — знак не создаёт полей-эффектов; для гомоглифа гард расширяется проверкой смешения письменностей на уровне интегратора
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
VISIBLE_FORM: Ϲ
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_LETTER_HOMOGLYPH
BASE_MODE_FORMULA: GREEK_CAPITAL_LUNATE_SIGMA_FORM ≠ LATIN_CAPITAL_C
SIGN_CATEGORY:
  - греческая заглавная лунная сигма — типографский вариант заглавной сигмы (звук /с/; законна в греческом, особенно византийском / церковном наборе)
  - гомоглиф латинской заглавной «C» (U+0043)
  - потенциальный носитель гомоглиф / IDN-подмены при смешении письменностей

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_LATIN_CAPITAL_C — греческая Ϲ (U+03F9) НЕ латинская C (U+0043); другая кодовая точка И другой звук (/с/, не /к/)
  2. NOT_SAME_STRING_AS_LATIN — строка с греческой Ϲ машинно не равна латинскому двойнику
  3. NOT_BRAND_NAME_PROOF — «Ϲoinbase» не доказывает связь с брендом Coinbase
  4. NOT_DOMAIN_VALIDITY_PROOF — визуальное совпадение домена не подтверждает регистрируемый домен
  5. NOT_AUTHORITY — буква не подтверждает официальный статус
  6. NOT_VERIFICATION — она не верифицирует смежный факт
  7. NOT_ASCII — вне ASCII; фильтры «только ASCII» не видят её как C
  8. NOT_AUTOMATICALLY_SPOOF — в односкриптовом греческом тексте это норма, не атака
  9. NOT_EXECUTION_TRIGGER — сама по себе ничего не запускает
  10. NOT_TRUST_SIGNAL — не повышает доверие к содержимому
  11. NOT_EFFECT — форма буквы не создаёт эффекта
  12. NOT_INTERCHANGEABLE_IN_IDENTIFIERS — в идентификаторе/домене замена C→Ϲ меняет сущность

BASE_FORMULAS:
  GREEK_CAPITAL_LUNATE_SIGMA_FORM ≠ LATIN_CAPITAL_C
  GREEK_CAPITAL_LUNATE_SIGMA_FORM ≠ SAME_CODEPOINT_AS_LATIN
  GREEK_CAPITAL_LUNATE_SIGMA_FORM ≠ BRAND_NAME_PROOF
  GREEK_CAPITAL_LUNATE_SIGMA_FORM ≠ DOMAIN_VALIDITY_PROOF
  GREEK_CAPITAL_LUNATE_SIGMA_FORM ≠ AUTHORITY
  GREEK_CAPITAL_LUNATE_SIGMA_FORM ≠ VERIFICATION
  GREEK_CAPITAL_LUNATE_SIGMA_FORM ≠ ASCII_LETTER
  GREEK_CAPITAL_LUNATE_SIGMA_FORM ≠ AUTOMATICALLY_SPOOF
  GREEK_CAPITAL_LUNATE_SIGMA_FORM ≠ TRUST_SIGNAL
  GREEK_CAPITAL_LUNATE_SIGMA_FORM ≠ EFFECT
  GREEK_CAPITAL_LUNATE_SIGMA_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: греческая заглавная лунная сигма — устойчивый вариант буквы без культурной прецессии функций. «Гомоглиф» — не эпоха, а свойство визуального совпадения с латинской C, сосуществующее с законной функцией буквы. Опасность контекстна (смешение письменностей), а не эпохальна — поэтому SEMANTIC_EPOCH_TRACKER не применяется.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1 (physical gesture)
  NOTE: буква — письменный знак без жестового предшественника; заглавная лунная сигма — письменный глиф-вариант греческой заглавной сигмы.

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
    INPUT: "Ϲωκράτηϲ" (Сократ, греческий с лунной сигмой)
    CONTEXT: обычный греческий текст (одна письменность)
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREEK_CAPITAL_LUNATE_SIGMA_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_002:
    INPUT: "Ϲοφία" (София / мудрость, греческий)
    CONTEXT: греческое слово, где заглавная лунная сигма — обычная буква
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREEK_CAPITAL_LUNATE_SIGMA_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "Ϲταυρόϲ" (крест, греческий)
    CONTEXT: односкриптовое греческое слово
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREEK_CAPITAL_LUNATE_SIGMA_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_004:
    INPUT: "Ϲελήνη" (Селена / луна, греческий)
    CONTEXT: односкриптовое греческое слово
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREEK_CAPITAL_LUNATE_SIGMA_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "Ϲωτήρ" (Спаситель, греческий)
    CONTEXT: греческое слово с заглавной лунной сигмой
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREEK_CAPITAL_LUNATE_SIGMA_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_006:
    INPUT: "Ϲύμβολον" (символ, греческий)
    CONTEXT: односкриптовое греческое слово
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREEK_CAPITAL_LUNATE_SIGMA_FORM ≠ AUTOMATICALLY_SPOOF

RISK_CASES:
  RISK_CASE_001:
    NAME: BRAND_HOMOGLYPH
    INPUT: "Ϲoinbase-login.com" (греческая Ϲ в начале бренда)
    CONTEXT: IDN/бренд-подмена — токен выглядит как Coinbase, но первый символ греческий
    RISK: CRITICAL
    ATTACK: замена латинской C на греческую Ϲ даёт визуально идентичный бренд, который регистрирует атакующий
    GUARD: GREEK_CAPITAL_LUNATE_SIGMA_FORM ≠ LATIN_CAPITAL_C
  RISK_CASE_002:
    NAME: BRAND_DOMAIN_SUBSTITUTION
    INPUT: "Ϲomcast-billing.com" (греческая Ϲ открывает бренд-домен)
    CONTEXT: подмена бренда с заглавной в начале в биллинг-домене
    RISK: CRITICAL
    ATTACK: строка машинно-≠ Comcast, но человек не видит разницы
    GUARD: GREEK_CAPITAL_LUNATE_SIGMA_FORM ≠ DOMAIN_VALIDITY_PROOF
  RISK_CASE_003:
    NAME: HANDLE_IMPERSONATION
    INPUT: "@ϹhaseSupport" (греческая Ϲ в хэндле)
    CONTEXT: имитация бренд-аккаунта в чате/соцсети
    RISK: HIGH
    ATTACK: похожий хэндл выглядит как ChaseSupport, но это другой аккаунт
    GUARD: GREEK_CAPITAL_LUNATE_SIGMA_FORM ≠ VERIFICATION
  RISK_CASE_004:
    NAME: FILTER_BYPASS_KEYWORD
    INPUT: "Ϲlick here now" (греческая Ϲ обходит блок-лист «Click»)
    CONTEXT: обход текстового фильтра, ищущего латинское слово
    RISK: HIGH
    ATTACK: одна заменённая заглавная выводит слово из-под блок-листа
    GUARD: GREEK_CAPITAL_LUNATE_SIGMA_FORM ≠ ASCII_LETTER
  RISK_CASE_005:
    NAME: EMAIL_LOOKALIKE
    INPUT: "billing@Ϲitibank-secure.example" (греческая Ϲ в почтовом домене)
    CONTEXT: фишинговое письмо от «той же» компании
    RISK: HIGH
    ATTACK: домен выглядит идентично, но ведёт к атакующему
    GUARD: GREEK_CAPITAL_LUNATE_SIGMA_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
  RISK_CASE_006:
    NAME: MULTI_HOMOGLYPH_ON_TARGET
    INPUT: "Ϲostϲo" (греческая заглавная Ϲ + греческая строчная ϲ вокруг латинских букв, имитируя Costco)
    CONTEXT: несколько подстановок в одном токене (Ϲ/ϲ греческие, ost/o латинские — смешение письменностей)
    RISK: HIGH
    ATTACK: цепочка двойников имитирует всё латинское имя бренда
    GUARD: GREEK_CAPITAL_LUNATE_SIGMA_FORM ≠ BRAND_NAME_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: C
    CODEPOINT: U+0043
    NAME: LATIN CAPITAL LETTER C
    RISK: CRITICAL
    RULE: LATIN_CAPITAL_C ≠ GREEK_CAPITAL_LUNATE_SIGMA (главная цель имитации; визуально идентична во многих шрифтах)
  CONFUSABLE_002:
    VISIBLE_FORM: С
    CODEPOINT: U+0421
    NAME: CYRILLIC CAPITAL LETTER ES
    RISK: HIGH
    RULE: CYRILLIC_CAPITAL_ES ≠ GREEK_CAPITAL_LUNATE_SIGMA (третья письменность с той же формой C; усложняет детекцию)
  CONFUSABLE_003:
    VISIBLE_FORM: Ｃ
    CODEPOINT: U+FF23
    NAME: FULLWIDTH LATIN CAPITAL LETTER C
    RISK: MEDIUM
    RULE: FULLWIDTH_CAPITAL_C ≠ GREEK_CAPITAL_LUNATE_SIGMA (полноширинная латинская C; иная форма совместимости)
  CONFUSABLE_004:
    VISIBLE_FORM: 𝖢
    CODEPOINT: U+1D5A2
    NAME: MATHEMATICAL SANS-SERIF CAPITAL C
    RISK: MEDIUM
    RULE: MATH_SANS_CAPITAL_C ≠ GREEK_CAPITAL_LUNATE_SIGMA (математически-стилизованная латинская C для обхода простых фильтров)
  CONFUSABLE_005:
    VISIBLE_FORM: 𝐂
    CODEPOINT: U+1D402
    NAME: MATHEMATICAL BOLD CAPITAL C
    RISK: LOW
    RULE: MATH_BOLD_CAPITAL_C ≠ GREEK_CAPITAL_LUNATE_SIGMA (полужирная латинская C)
  CONFUSABLE_006:
    VISIBLE_FORM: 𝐶
    CODEPOINT: U+1D436
    NAME: MATHEMATICAL ITALIC CAPITAL C
    RISK: LOW
    RULE: MATH_ITALIC_CAPITAL_C ≠ GREEK_CAPITAL_LUNATE_SIGMA (курсивная латинская C)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "бренд `Ϲoinbase` — это Coinbase"
    RESPONSE: GREEK_CAPITAL_LUNATE_SIGMA_FORM ≠ LATIN_CAPITAL_C
    RULE: первый символ — греческая заглавная лунная сигма (/с/); регистрируемый домен/имя иные — решает DNS, а не глаз
  CG2:
    TRIGGER: "строка с греческой Ϲ равна её латинскому написанию"
    RESPONSE: GREEK_CAPITAL_LUNATE_SIGMA_FORM ≠ SAME_CODEPOINT_AS_LATIN
    RULE: разные кодовые точки → машинно-разные строки
  CG3:
    TRIGGER: "любая греческая Ϲ в тексте — атака"
    RESPONSE: GREEK_CAPITAL_LUNATE_SIGMA_FORM ≠ AUTOMATICALLY_SPOOF
    RULE: в односкриптовом греческом тексте буква законна; подмена — это СМЕСЬ письменностей в одном токене
  CG4:
    TRIGGER: "ASCII-фильтр поймает заменённое слово"
    RESPONSE: GREEK_CAPITAL_LUNATE_SIGMA_FORM ≠ ASCII_LETTER
    RULE: греческая Ϲ вне ASCII; латинский фильтр её не сматчит
  CG5:
    TRIGGER: "хэндл `@ϹhaseSupport` — тот же аккаунт, что @ChaseSupport"
    RESPONSE: GREEK_CAPITAL_LUNATE_SIGMA_FORM ≠ VERIFICATION
    RULE: визуальное сходство не идентифицирует аккаунт
  CG6:
    TRIGGER: "замена C→Ϲ в идентификаторе безвредна"
    RESPONSE: GREEK_CAPITAL_LUNATE_SIGMA_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
    RULE: в домене/логине/токене замена меняет сущность, к которой строка резолвится

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "Ϲoinbase" (греческая Ϲ + латиница в одном токене)
      NAME: MIXED_SCRIPT_TOKEN
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: IDN/бренд-подмена; ключевой сигнал — СМЕШЕНИЕ письменностей внутри одного токена
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "Ϲostϲo" (греческие Ϲ/ϲ вокруг латинских букв)
      NAME: MULTI_HOMOGLYPH_TOKEN
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: множественная подстановка на целевой бренд
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — опасность знака проявляется именно в последовательности (токене), а не в изоляции.

PHAGO_ENTITY_MIMICRY:
  PE_001:
    INPUT: "Ϲoinbase-login.com"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: CRITICAL
    NOTE: греческая Ϲ имитирует само ИМЯ верифицированного бренда (не просто структуру) — прямая имитация существования сущности. Поэтому реестр помечает знак PHAGO ●; коммерческие защиты от двойников часто пропускают этот класс.
  PE_002:
    INPUT: "@ϹhaseSupport"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: HIGH
    NOTE: имитация официального саппорт-аккаунта бренда через двойника в имени.

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена латинской C (U+0043) греческой Ϲ (U+03F9) в бренд-домене
  A2: смешение греческой Ϲ с кириллической заглавной es С / math sans-serif C для усложнения детекции
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: греческая Ϲ обходит латинский блок-лист (Ϲlick here now)
  B2: греческая Ϲ в почтовом домене (billing@Ϲitibank-secure.example) для фишинга
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: смешанный токен `Ϲoinbase` (SC1) — письменности внутри одного слова
  C2: множественная подстановка `Ϲostϲo` (SC2) на целевой бренд
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: хэндл `@ϹhaseSupport` имитирует бренд-аккаунт
  D2: "Ϲitibank-secure" — двойник в псевдо-официальном имени
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: `Ϲoinbase-login.com` — имитация имени бренда (PE_001)
  E2: `@ϹhaseSupport` — имитация официального аккаунта (PE_002)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у буквы нет спящих/активных эпох (см. раздел 5).
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: `Ϲoinbase-login.com` с греческой Ϲ — домен Coinbase
  EXPECTED: FAIL_BRAND_NAME_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: строка с греческой Ϲ машинно равна её латинскому написанию
  EXPECTED: FAIL_CODEPOINT_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: любая греческая Ϲ в тексте — атака
  EXPECTED: FAIL_OVERBLOCK_MIMICRY (обратная ошибка: подлинный греческий — не подмена)
  RESULT: FAIL
MUTATION_04:
  CLAIM: ASCII-фильтр на "Click" поймает "Ϲlick"
  EXPECTED: FAIL_ASCII_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: хэндл `@ϹhaseSupport` — тот же аккаунт, что `@ChaseSupport`
  EXPECTED: FAIL_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: замена C→Ϲ в идентификаторе безвредна
  EXPECTED: FAIL_IDENTIFIER_INTERCHANGE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как отличить законный односкриптовый греческий текст от подмены без ложных срабатываний?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (правило «смесь письменностей в одном токене» — забота интегратора; см. прототип Vakhter confusable_cards.py)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует формулу ВЫГЛЯДИТ_ОДИНАКОВО ≠ ЯВЛЯЕТСЯ_ТЕМ_ЖЕ и правило «подмена = смесь, не наличие».
OQ2:
  QUESTION: нужна ли полная таблица UTS #39 + корпус брендов для whole-script случая?
  STATUS: OPEN
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: делегировано рантайму/интегратору.
ALL_OPEN_QUESTIONS_CLOSED: NO (delegated, non-blocking)

============================================================
11. PATCH_HISTORY
============================================================
PATCH_HISTORY:
  v0_1_PATCH_01: первичное создание (Руслан Малявский, 2026-07-22) — черновик из шаблона GEN3_v0_3 (Vakhter), гомоглиф; не прогонялся конвейером.
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
