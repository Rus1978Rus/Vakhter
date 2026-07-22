PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_GREEK_LUNATE_SIGMA_U03F2_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
TRANSLATION_NOTE: Русский оригинал (авторитетный источник). Английский документ SIGN_CORE_CARD_GREEK_LUNATE_SIGMA_U03F2_GEN3_v0_3_EN — зеркало. Кодовые точки, имена полей и формулы идентичны. Гомоглиф: базовый закон — ВЫГЛЯДИТ_ОДИНАКОВО ≠ ЯВЛЯЕТСЯ_ТЕМ_ЖЕ. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_GREEK_LUNATE_SIGMA_U03F2_GEN3_v0_3_RU
CODEPOINT: U+03F2
VISIBLE_FORM: ϲ
UNICODE_NAME: GREEK LUNATE SIGMA SYMBOL
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Руслан Малявский
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: греческая «ϲ» лунная сигма (гомоглиф латинской строчной c; читается /с/, а не /к/)
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
VISIBLE_FORM: ϲ
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_LETTER_HOMOGLYPH
BASE_MODE_FORMULA: GREEK_LUNATE_SIGMA_FORM ≠ LATIN_C
SIGN_CATEGORY:
  - греческая лунная сигма — типографский вариант сигмы (звук /с/; законна в греческом, особенно византийском / церковном наборе)
  - гомоглиф латинской строчной «c» (U+0063)
  - потенциальный носитель гомоглиф / IDN-подмены при смешении письменностей

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_LATIN_C — греческая ϲ (U+03F2) НЕ латинская c (U+0063); другая кодовая точка И другой звук (/с/, не /к/)
  2. NOT_SAME_STRING_AS_LATIN — строка с греческой ϲ машинно не равна латинскому двойнику
  3. NOT_BRAND_NAME_PROOF — «ϲoinbase» не доказывает связь с брендом Coinbase
  4. NOT_DOMAIN_VALIDITY_PROOF — визуальное совпадение домена не подтверждает регистрируемый домен
  5. NOT_AUTHORITY — буква не подтверждает официальный статус
  6. NOT_VERIFICATION — она не верифицирует смежный факт
  7. NOT_ASCII — вне ASCII; фильтры «только ASCII» не видят её как c
  8. NOT_AUTOMATICALLY_SPOOF — в односкриптовом греческом тексте это норма, не атака
  9. NOT_EXECUTION_TRIGGER — сама по себе ничего не запускает
  10. NOT_TRUST_SIGNAL — не повышает доверие к содержимому
  11. NOT_EFFECT — форма буквы не создаёт эффекта
  12. NOT_INTERCHANGEABLE_IN_IDENTIFIERS — в идентификаторе/домене замена c→ϲ меняет сущность

BASE_FORMULAS:
  GREEK_LUNATE_SIGMA_FORM ≠ LATIN_C
  GREEK_LUNATE_SIGMA_FORM ≠ SAME_CODEPOINT_AS_LATIN
  GREEK_LUNATE_SIGMA_FORM ≠ BRAND_NAME_PROOF
  GREEK_LUNATE_SIGMA_FORM ≠ DOMAIN_VALIDITY_PROOF
  GREEK_LUNATE_SIGMA_FORM ≠ AUTHORITY
  GREEK_LUNATE_SIGMA_FORM ≠ VERIFICATION
  GREEK_LUNATE_SIGMA_FORM ≠ ASCII_LETTER
  GREEK_LUNATE_SIGMA_FORM ≠ AUTOMATICALLY_SPOOF
  GREEK_LUNATE_SIGMA_FORM ≠ TRUST_SIGNAL
  GREEK_LUNATE_SIGMA_FORM ≠ EFFECT
  GREEK_LUNATE_SIGMA_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: греческая лунная сигма — устойчивый вариант буквы без культурной прецессии функций. «Гомоглиф» — не эпоха, а свойство визуального совпадения с латинской c, сосуществующее с законной функцией буквы. Опасность контекстна (смешение письменностей), а не эпохальна — поэтому SEMANTIC_EPOCH_TRACKER не применяется.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1 (physical gesture)
  NOTE: буква — письменный знак без жестового предшественника; лунная сигма — письменный глиф-вариант греческой сигмы.

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
    INPUT: "ϲοφία και αλήθεια" (мудрость и истина, греческий с лунной сигмой)
    CONTEXT: обычный греческий текст (одна письменность)
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREEK_LUNATE_SIGMA_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_002:
    INPUT: "κόϲμοϲ και φύϲη" (космос и природа, греческий)
    CONTEXT: греческая фраза, где лунная сигма — обычная буква
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREEK_LUNATE_SIGMA_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "ϲταυρόϲ" (крест, греческий)
    CONTEXT: односкриптовое греческое слово
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREEK_LUNATE_SIGMA_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_004:
    INPUT: "ϲελήνη και ήλιοϲ" (луна и солнце, греческий)
    CONTEXT: односкриптовая греческая фраза
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREEK_LUNATE_SIGMA_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "ϲτέφανοϲ" (венец, греческий)
    CONTEXT: греческое слово с лунной сигмой
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREEK_LUNATE_SIGMA_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_006:
    INPUT: "ϲῶμα και ψυχή" (тело и душа, греческий)
    CONTEXT: односкриптовая греческая фраза
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREEK_LUNATE_SIGMA_FORM ≠ AUTOMATICALLY_SPOOF

RISK_CASES:
  RISK_CASE_001:
    NAME: BRAND_HOMOGLYPH
    INPUT: "ϲoinbase-login.com" (греческая ϲ в начале бренда)
    CONTEXT: IDN/бренд-подмена — токен выглядит как coinbase, но первый символ греческий
    RISK: CRITICAL
    ATTACK: замена латинской c на греческую ϲ даёт визуально идентичный бренд, который регистрирует атакующий
    GUARD: GREEK_LUNATE_SIGMA_FORM ≠ LATIN_C
  RISK_CASE_002:
    NAME: MIDTOKEN_BRAND_SUBSTITUTION
    INPUT: "faϲebook-login.com" (греческая ϲ внутри бренда)
    CONTEXT: подстановка в середине токена в бренд-фразе
    RISK: CRITICAL
    ATTACK: строка машинно-≠ facebook, но человек не видит разницы
    GUARD: GREEK_LUNATE_SIGMA_FORM ≠ DOMAIN_VALIDITY_PROOF
  RISK_CASE_003:
    NAME: HANDLE_IMPERSONATION
    INPUT: "@ϲhaseSupport" (греческая ϲ в хэндле)
    CONTEXT: имитация бренд-аккаунта в чате/соцсети
    RISK: HIGH
    ATTACK: похожий хэндл выглядит как chaseSupport, но это другой аккаунт
    GUARD: GREEK_LUNATE_SIGMA_FORM ≠ VERIFICATION
  RISK_CASE_004:
    NAME: FILTER_BYPASS_KEYWORD
    INPUT: "ϲlick" (греческая ϲ обходит блок-лист «click»)
    CONTEXT: обход текстового фильтра, ищущего латинское слово
    RISK: HIGH
    ATTACK: одна заменённая буква выводит слово из-под блок-листа
    GUARD: GREEK_LUNATE_SIGMA_FORM ≠ ASCII_LETTER
  RISK_CASE_005:
    NAME: EMAIL_LOOKALIKE
    INPUT: "billing@ϲitibank-secure.example" (греческая ϲ в почтовом домене)
    CONTEXT: фишинговое письмо от «той же» компании
    RISK: HIGH
    ATTACK: домен выглядит идентично, но ведёт к атакующему
    GUARD: GREEK_LUNATE_SIGMA_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
  RISK_CASE_006:
    NAME: MULTI_HOMOGLYPH_ON_TARGET
    INPUT: "ϲostϲo" (две греческие ϲ вокруг латинских букв, имитируя costco)
    CONTEXT: несколько подстановок в одном токене (ϲ греческие, ost/o латинские — смешение письменностей)
    RISK: HIGH
    ATTACK: цепочка двойников имитирует всё латинское имя бренда
    GUARD: GREEK_LUNATE_SIGMA_FORM ≠ BRAND_NAME_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: c
    CODEPOINT: U+0063
    NAME: LATIN SMALL LETTER C
    RISK: CRITICAL
    RULE: LATIN_C ≠ GREEK_LUNATE_SIGMA (главная цель имитации; визуально идентична во многих шрифтах)
  CONFUSABLE_002:
    VISIBLE_FORM: с
    CODEPOINT: U+0441
    NAME: CYRILLIC SMALL LETTER ES
    RISK: HIGH
    RULE: CYRILLIC_ES ≠ GREEK_LUNATE_SIGMA (третья письменность с той же формой c; усложняет детекцию)
  CONFUSABLE_003:
    VISIBLE_FORM: ｃ
    CODEPOINT: U+FF43
    NAME: FULLWIDTH LATIN SMALL LETTER C
    RISK: MEDIUM
    RULE: FULLWIDTH_SMALL_C ≠ GREEK_LUNATE_SIGMA (полноширинная латинская c; иная форма совместимости)
  CONFUSABLE_004:
    VISIBLE_FORM: 𝖼
    CODEPOINT: U+1D5BC
    NAME: MATHEMATICAL SANS-SERIF SMALL C
    RISK: MEDIUM
    RULE: MATH_SANS_SMALL_C ≠ GREEK_LUNATE_SIGMA (математически-стилизованная латинская c для обхода простых фильтров)
  CONFUSABLE_005:
    VISIBLE_FORM: 𝐜
    CODEPOINT: U+1D41C
    NAME: MATHEMATICAL BOLD SMALL C
    RISK: LOW
    RULE: MATH_BOLD_SMALL_C ≠ GREEK_LUNATE_SIGMA (полужирная латинская c)
  CONFUSABLE_006:
    VISIBLE_FORM: 𝑐
    CODEPOINT: U+1D450
    NAME: MATHEMATICAL ITALIC SMALL C
    RISK: LOW
    RULE: MATH_ITALIC_SMALL_C ≠ GREEK_LUNATE_SIGMA (курсивная латинская c)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "бренд `ϲoinbase` — это Coinbase"
    RESPONSE: GREEK_LUNATE_SIGMA_FORM ≠ LATIN_C
    RULE: первый символ — греческая лунная сигма (/с/); регистрируемый домен/имя иные — решает DNS, а не глаз
  CG2:
    TRIGGER: "строка с греческой ϲ равна её латинскому написанию"
    RESPONSE: GREEK_LUNATE_SIGMA_FORM ≠ SAME_CODEPOINT_AS_LATIN
    RULE: разные кодовые точки → машинно-разные строки
  CG3:
    TRIGGER: "любая греческая ϲ в тексте — атака"
    RESPONSE: GREEK_LUNATE_SIGMA_FORM ≠ AUTOMATICALLY_SPOOF
    RULE: в односкриптовом греческом тексте буква законна; подмена — это СМЕСЬ письменностей в одном токене
  CG4:
    TRIGGER: "ASCII-фильтр поймает заменённое слово"
    RESPONSE: GREEK_LUNATE_SIGMA_FORM ≠ ASCII_LETTER
    RULE: греческая ϲ вне ASCII; латинский фильтр её не сматчит
  CG5:
    TRIGGER: "хэндл `@ϲhaseSupport` — тот же аккаунт, что @chaseSupport"
    RESPONSE: GREEK_LUNATE_SIGMA_FORM ≠ VERIFICATION
    RULE: визуальное сходство не идентифицирует аккаунт
  CG6:
    TRIGGER: "замена c→ϲ в идентификаторе безвредна"
    RESPONSE: GREEK_LUNATE_SIGMA_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
    RULE: в домене/логине/токене замена меняет сущность, к которой строка резолвится

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "ϲoinbase" (греческая ϲ + латиница в одном токене)
      NAME: MIXED_SCRIPT_TOKEN
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: IDN/бренд-подмена; ключевой сигнал — СМЕШЕНИЕ письменностей внутри одного токена
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "ϲostϲo" (две греческие ϲ вокруг латинских букв)
      NAME: MULTI_HOMOGLYPH_TOKEN
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: множественная подстановка на целевой бренд
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — опасность знака проявляется именно в последовательности (токене), а не в изоляции.

PHAGO_ENTITY_MIMICRY:
  PE_001:
    INPUT: "ϲoinbase-login.com"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: CRITICAL
    NOTE: греческая ϲ имитирует само ИМЯ верифицированного бренда (не просто структуру) — прямая имитация существования сущности. Поэтому реестр помечает знак PHAGO ●; коммерческие защиты от двойников часто пропускают этот класс.
  PE_002:
    INPUT: "@ϲhaseSupport"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: HIGH
    NOTE: имитация официального саппорт-аккаунта бренда через двойника в имени.

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена латинской c (U+0063) греческой ϲ (U+03F2) в бренд-домене
  A2: смешение греческой ϲ с кириллической es с / math sans-serif c для усложнения детекции
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: греческая ϲ обходит латинский блок-лист (ϲlick)
  B2: греческая ϲ в почтовом домене (billing@ϲitibank-secure.example) для фишинга
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: смешанный токен `ϲoinbase` (SC1) — письменности внутри одного слова
  C2: множественная подстановка `ϲostϲo` (SC2) на целевой бренд
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: хэндл `@ϲhaseSupport` имитирует бренд-аккаунт
  D2: "ϲitibank-secure" — двойник в псевдо-официальном имени
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: `ϲoinbase-login.com` — имитация имени бренда (PE_001)
  E2: `@ϲhaseSupport` — имитация официального аккаунта (PE_002)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у буквы нет спящих/активных эпох (см. раздел 5).
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: `ϲoinbase-login.com` с греческой ϲ — домен Coinbase
  EXPECTED: FAIL_BRAND_NAME_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: строка с греческой ϲ машинно равна её латинскому написанию
  EXPECTED: FAIL_CODEPOINT_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: любая греческая ϲ в тексте — атака
  EXPECTED: FAIL_OVERBLOCK_MIMICRY (обратная ошибка: подлинный греческий — не подмена)
  RESULT: FAIL
MUTATION_04:
  CLAIM: ASCII-фильтр на "click" поймает "ϲlick"
  EXPECTED: FAIL_ASCII_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: хэндл `@ϲhaseSupport` — тот же аккаунт, что `@chaseSupport`
  EXPECTED: FAIL_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: замена c→ϲ в идентификаторе безвредна
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
