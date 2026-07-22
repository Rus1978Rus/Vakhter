PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_GREEK_IOTA_U03B9_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
TRANSLATION_NOTE: Русский оригинал (авторитетный источник). Английский документ SIGN_CORE_CARD_GREEK_IOTA_U03B9_GEN3_v0_3_EN — зеркало. Кодовые точки, имена полей и формулы идентичны. Гомоглиф: базовый закон — ВЫГЛЯДИТ_ОДИНАКОВО ≠ ЯВЛЯЕТСЯ_ТЕМ_ЖЕ. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_GREEK_IOTA_U03B9_GEN3_v0_3_RU
CODEPOINT: U+03B9
VISIBLE_FORM: ι
UNICODE_NAME: GREEK SMALL LETTER IOTA
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Руслан Малявский
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: греческая «ι» йота (гомоглиф латинской строчной i; читается /и/)
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
VISIBLE_FORM: ι
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_LETTER_HOMOGLYPH
BASE_MODE_FORMULA: GREEK_IOTA_FORM ≠ LATIN_SMALL_I
SIGN_CATEGORY:
  - греческая строчная буква йота (звучит /и/; легитимна в греческой письменности)
  - гомоглиф латинской строчной «i» (U+0069)
  - потенциальный носитель гомоглифного / IDN-спуфинга при смешении письменностей

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_LATIN_SMALL_I — греческая ι (U+03B9) НЕ есть латинская i (U+0069); другая кодовая точка в другой письменности (и без точки)
  2. NOT_SAME_STRING_AS_LATIN — строка с греческой ι не машинно-равна своему латинскому двойнику
  3. NOT_BRAND_NAME_PROOF — «ιnstagram» не доказывает связь с брендом Instagram
  4. NOT_DOMAIN_VALIDITY_PROOF — визуальное совпадение домена не подтверждает регистрируемый домен
  5. NOT_AUTHORITY — буква не подтверждает официальный статус
  6. NOT_VERIFICATION — не верифицирует соседний факт
  7. NOT_ASCII — не входит в ASCII; фильтры «только ASCII» не видят её как i
  8. NOT_AUTOMATICALLY_SPOOF — в односкриптовом греческом тексте она нормальна, не атака
  9. NOT_EXECUTION_TRIGGER — сама по себе ничего не запускает
  10. NOT_TRUST_SIGNAL — не повышает доверие к содержимому
  11. NOT_EFFECT — форма буквы не создаёт эффекта
  12. NOT_INTERCHANGEABLE_IN_IDENTIFIERS — в идентификаторе/домене замена i→ι меняет сущность

BASE_FORMULAS:
  GREEK_IOTA_FORM ≠ LATIN_SMALL_I
  GREEK_IOTA_FORM ≠ SAME_CODEPOINT_AS_LATIN
  GREEK_IOTA_FORM ≠ BRAND_NAME_PROOF
  GREEK_IOTA_FORM ≠ DOMAIN_VALIDITY_PROOF
  GREEK_IOTA_FORM ≠ AUTHORITY
  GREEK_IOTA_FORM ≠ VERIFICATION
  GREEK_IOTA_FORM ≠ ASCII_LETTER
  GREEK_IOTA_FORM ≠ AUTOMATICALLY_SPOOF
  GREEK_IOTA_FORM ≠ TRUST_SIGNAL
  GREEK_IOTA_FORM ≠ EFFECT
  GREEK_IOTA_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: греческая «ι» йота — стабильная буква без культурной прецессии функций. «Гомоглиф» — не эпоха, а свойство визуального совпадения с латинской i, сосуществующее с легитимной функцией буквы. Опасность контекстна (смешение письменностей), а не эпохальна — поэтому SEMANTIC_EPOCH_TRACKER не применяется.
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
    INPUT: "ιδέα και σκέψη" (идея и мысль, греческий)
    CONTEXT: обычный греческий текст (один скрипт)
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREEK_IOTA_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_002:
    INPUT: "ιστορία και μύθος" (история и миф, греческий)
    CONTEXT: греческая фраза, где «ι» — обычная буква
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREEK_IOTA_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "ιατρός και νοσοκόμα" (врач и медсестра, греческий)
    CONTEXT: односкриптовая греческая фраза
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREEK_IOTA_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_004:
    INPUT: "φιλία και αγάπη" (дружба и любовь, греческий)
    CONTEXT: односкриптовая греческая фраза с «ι»
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREEK_IOTA_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "νησί και θάλασσα" (остров и море, греческий)
    CONTEXT: греческие слова с «ι»
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREEK_IOTA_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_006:
    INPUT: "κιθάρα και μουσική" (гитара и музыка, греческий)
    CONTEXT: односкриптовая греческая фраза
    EXPECTED: INFO
    RISK: NONE
    GUARD: GREEK_IOTA_FORM ≠ AUTOMATICALLY_SPOOF

RISK_CASES:
  RISK_CASE_001:
    NAME: BRAND_HOMOGLYPH
    INPUT: "ιnstagram-login.com"
    CONTEXT: IDN/бренд-спуф — токен выглядит как instagram, но первый символ греческий
    RISK: CRITICAL
    ATTACK: замена латинской i на греческую ι даёт визуально идентичный бренд, который регистрирует атакующий
    GUARD: GREEK_IOTA_FORM ≠ LATIN_SMALL_I
  RISK_CASE_002:
    NAME: BRAND_SUBSTITUTION
    INPUT: "ιcloud-billing.com"
    CONTEXT: ведущая подмена в названии бренда
    RISK: CRITICAL
    ATTACK: строка машинно-≠ icloud, но человек не видит разницы
    GUARD: GREEK_IOTA_FORM ≠ DOMAIN_VALIDITY_PROOF
  RISK_CASE_003:
    NAME: HANDLE_IMPERSONATION
    INPUT: "@ιnstaHelp"
    CONTEXT: имперсонация бренд-аккаунта в чате/соцсети
    RISK: HIGH
    ATTACK: похожий хэндл выглядит как instaHelp, но это другой аккаунт
    GUARD: GREEK_IOTA_FORM ≠ VERIFICATION
  RISK_CASE_004:
    NAME: FILTER_BYPASS_KEYWORD
    INPUT: "ιframe"
    CONTEXT: обход текстового фильтра, ищущего латинский токен
    RISK: HIGH
    ATTACK: одна подменённая буква выводит токен из-под блок-листа
    GUARD: GREEK_IOTA_FORM ≠ ASCII_LETTER
  RISK_CASE_005:
    NAME: EMAIL_LOOKALIKE
    INPUT: "no-reply@ιnstagram-secure.example"
    CONTEXT: фишинговое письмо от «той же» компании
    RISK: HIGH
    ATTACK: домен выглядит идентично, но ведёт к атакующему
    GUARD: GREEK_IOTA_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
  RISK_CASE_006:
    NAME: MULTI_HOMOGLYPH_ON_TARGET
    INPUT: "mιnι"
    CONTEXT: две греческие ι вокруг латинских букв, имитирующие mini (ι греческая, mn латиница — смешение письменностей)
    RISK: HIGH
    ATTACK: цепочка двойников имитирует всё латинское слово
    GUARD: GREEK_IOTA_FORM ≠ BRAND_NAME_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: i
    CODEPOINT: U+0069
    NAME: LATIN SMALL LETTER I
    RISK: CRITICAL
    RULE: LATIN_SMALL_I ≠ GREEK_IOTA (главная цель имперсонации; визуально схожа во многих шрифтах)
  CONFUSABLE_002:
    VISIBLE_FORM: і
    CODEPOINT: U+0456
    NAME: CYRILLIC SMALL LETTER BYELORUSSIAN-UKRAINIAN I
    RISK: HIGH
    RULE: CYRILLIC_I ≠ GREEK_IOTA (третий скрипт с той же формой i; усложняет детекцию)
  CONFUSABLE_003:
    VISIBLE_FORM: ｉ
    CODEPOINT: U+FF49
    NAME: FULLWIDTH LATIN SMALL LETTER I
    RISK: MEDIUM
    RULE: FULLWIDTH_SMALL_I ≠ GREEK_IOTA (полноширинная латинская i; другая форма совместимости)
  CONFUSABLE_004:
    VISIBLE_FORM: 𝑖
    CODEPOINT: U+1D456
    NAME: MATHEMATICAL ITALIC SMALL I
    RISK: MEDIUM
    RULE: MATH_ITALIC_SMALL_I ≠ GREEK_IOTA (математически-стилизованная латинская i для обхода простых фильтров)
  CONFUSABLE_005:
    VISIBLE_FORM: ı
    CODEPOINT: U+0131
    NAME: LATIN SMALL LETTER DOTLESS I
    RISK: LOW
    RULE: LATIN_DOTLESS_I ≠ GREEK_IOTA (латинская i без точки, близкая к форме йоты)
  CONFUSABLE_006:
    VISIBLE_FORM: 𝗂
    CODEPOINT: U+1D5C2
    NAME: MATHEMATICAL SANS-SERIF SMALL I
    RISK: LOW
    RULE: MATH_SANS_SMALL_I ≠ GREEK_IOTA (sans-serif-стилизованная латинская i)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: «бренд `ιnstagram` — это Instagram»
    RESPONSE: GREEK_IOTA_FORM ≠ LATIN_SMALL_I
    RULE: первый символ — греческая йота; регистрируемый домен/имя другой — решает DNS, а не глаз
  CG2:
    TRIGGER: «строка с греческой ι равна её латинскому написанию»
    RESPONSE: GREEK_IOTA_FORM ≠ SAME_CODEPOINT_AS_LATIN
    RULE: разные кодовые точки → машинно-разные строки
  CG3:
    TRIGGER: «любая греческая ι в тексте — атака»
    RESPONSE: GREEK_IOTA_FORM ≠ AUTOMATICALLY_SPOOF
    RULE: в односкриптовом греческом тексте буква легитимна; спуф — это СМЕШЕНИЕ письменностей в одном токене
  CG4:
    TRIGGER: «ASCII-фильтр поймает подменённый токен»
    RESPONSE: GREEK_IOTA_FORM ≠ ASCII_LETTER
    RULE: греческая ι вне ASCII; латинский фильтр её не сматчит
  CG5:
    TRIGGER: «хэндл `@ιnstaHelp` — тот же аккаунт, что и @instaHelp»
    RESPONSE: GREEK_IOTA_FORM ≠ VERIFICATION
    RULE: визуальное сходство не идентифицирует аккаунт
  CG6:
    TRIGGER: «замена i→ι в идентификаторе безвредна»
    RESPONSE: GREEK_IOTA_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
    RULE: в домене/логине/токене замена меняет сущность, к которой резолвится строка

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "ιnstagram" (греческая ι + латиница в одном токене)
      NAME: MIXED_SCRIPT_TOKEN
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: IDN/бренд-спуф; ключевой сигнал — СМЕШЕНИЕ письменностей внутри одного токена
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "mιnι" (две греческие ι вокруг латинских букв)
      NAME: MULTI_HOMOGLYPH_TOKEN
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: множественная подмена на целевое слово
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: не применимо — опасность знака проявляется именно в последовательности (в токене), а не в изоляции.

PHAGO_ENTITY_MIMICRY:
  PE_001:
    INPUT: "ιnstagram-login.com"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: CRITICAL
    NOTE: греческая ι имитирует само ИМЯ верифицированного бренда (а не только структуру) — прямая имитация существования сущности. Поэтому реестр помечает знак PHAGO ●; коммерческие защиты от двойников этот класс часто пропускают.
  PE_002:
    INPUT: "@ιnstaHelp"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: HIGH
    NOTE: имперсонация официального аккаунта поддержки бренда через двойника в имени.

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена латинской i (U+0069) на греческую ι (U+03B9) в домене бренда
  A2: смешение греческой ι с кириллической і / латинской i без точки для усложнения детекции
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: греческая ι обходит латинский блок-лист токенов (ιframe)
  B2: греческая ι в почтовом домене (no-reply@ιnstagram-secure.example) для фишинга
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: смешанный токен `ιnstagram` (SC1) — письменности внутри одного слова
  C2: множественная подмена `mιnι` (SC2) на целевое слово
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: хэндл `@ιnstaHelp` имитирует бренд-аккаунт
  D2: "ιnstagram-secure" — двойник в псевдо-официальном имени
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: `ιnstagram-login.com` — имитация имени бренда (PE_001)
  E2: `@ιnstaHelp` — имитация официального аккаунта (PE_002)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, буква не имеет спящих/активных эпох (см. раздел 5).
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: `ιnstagram-login.com` с греческой ι — это домен Instagram
  EXPECTED: FAIL_BRAND_NAME_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: строка с греческой ι машинно-равна её латинскому написанию
  EXPECTED: FAIL_CODEPOINT_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: любая греческая ι в тексте — атака
  EXPECTED: FAIL_OVERBLOCK_MIMICRY (обратная ошибка: подлинный греческий — не спуф)
  RESULT: FAIL
MUTATION_04:
  CLAIM: ASCII-фильтр на "iframe" поймает "ιframe"
  EXPECTED: FAIL_ASCII_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: хэндл `@ιnstaHelp` — тот же аккаунт, что и `@instaHelp`
  EXPECTED: FAIL_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: замена i→ι в идентификаторе безвредна
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
