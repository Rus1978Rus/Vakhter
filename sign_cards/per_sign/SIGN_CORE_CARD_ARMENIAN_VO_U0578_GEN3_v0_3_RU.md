PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_ARMENIAN_VO_U0578_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
TRANSLATION_NOTE: Русский оригинал (авторитетный источник). Английский документ SIGN_CORE_CARD_ARMENIAN_VO_U0578_GEN3_v0_3_EN — зеркало. Кодовые точки, имена полей и формулы идентичны. Гомоглиф: базовый закон — ВЫГЛЯДИТ_ОДИНАКОВО ≠ ЯВЛЯЕТСЯ_ТЕМ_ЖЕ. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_ARMENIAN_VO_U0578_GEN3_v0_3_RU
CODEPOINT: U+0578
VISIBLE_FORM: ո
UNICODE_NAME: ARMENIAN SMALL LETTER VO
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Руслан Малявский
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: армянская «ո» во (гомоглиф латинской строчной n)
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
VISIBLE_FORM: ո
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_LETTER_HOMOGLYPH
BASE_MODE_FORMULA: ARMENIAN_VO_FORM ≠ LATIN_SMALL_N
SIGN_CATEGORY:
  - армянская во (vo) — гласная буква армянского алфавита
  - гомоглиф латинской строчной «n» (U+006E)
  - потенциальный носитель гомоглиф / IDN-подмены при смешении письменностей

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_LATIN_SMALL_N — армянская ո (U+0578) НЕ латинская n (U+006E); другая кодовая точка и гласный /o/ (в начале слова /vo/)
  2. NOT_SAME_STRING_AS_LATIN — строка с этой буквой машинно не равна латинскому двойнику
  3. NOT_BRAND_NAME_PROOF — токен-двойник не доказывает связь с настоящим брендом
  4. NOT_DOMAIN_VALIDITY_PROOF — визуальное совпадение домена не подтверждает регистрируемый домен
  5. NOT_AUTHORITY — буква не подтверждает официальный статус
  6. NOT_VERIFICATION — она не верифицирует смежный факт
  7. NOT_ASCII — вне ASCII; фильтры «только ASCII» не видят её как n
  8. NOT_AUTOMATICALLY_SPOOF — в односкриптовом родном тексте это норма, не атака
  9. NOT_EXECUTION_TRIGGER — сама по себе ничего не запускает
  10. NOT_TRUST_SIGNAL — не повышает доверие к содержимому
  11. NOT_EFFECT — форма буквы не создаёт эффекта
  12. NOT_INTERCHANGEABLE_IN_IDENTIFIERS — в идентификаторе/домене замена n→ո меняет сущность

BASE_FORMULAS:
  ARMENIAN_VO_FORM ≠ LATIN_SMALL_N
  ARMENIAN_VO_FORM ≠ SAME_CODEPOINT_AS_LATIN
  ARMENIAN_VO_FORM ≠ BRAND_NAME_PROOF
  ARMENIAN_VO_FORM ≠ DOMAIN_VALIDITY_PROOF
  ARMENIAN_VO_FORM ≠ AUTHORITY
  ARMENIAN_VO_FORM ≠ VERIFICATION
  ARMENIAN_VO_FORM ≠ ASCII_LETTER
  ARMENIAN_VO_FORM ≠ AUTOMATICALLY_SPOOF
  ARMENIAN_VO_FORM ≠ TRUST_SIGNAL
  ARMENIAN_VO_FORM ≠ EFFECT
  ARMENIAN_VO_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: армянская буква во (vo) — устойчивая буква без культурной прецессии функций. «Гомоглиф» — не эпоха, а свойство визуального совпадения с латинской n, сосуществующее с законной функцией буквы. Опасность контекстна (смешение письменностей), а не эпохальна — поэтому SEMANTIC_EPOCH_TRACKER не применяется.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1 (physical gesture)
  NOTE: буква — письменный знак без жестового предшественника; буква во (vo) — письменный глиф армянская письменности.

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
    INPUT: "որդի" (армянский (сын))
    CONTEXT: односкриптовый родной текст
    EXPECTED: INFO
    RISK: NONE
    GUARD: ARMENIAN_VO_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_002:
    INPUT: "ոսկի" (армянский (золото))
    CONTEXT: односкриптовый родной текст
    EXPECTED: INFO
    RISK: NONE
    GUARD: ARMENIAN_VO_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "ոտք" (армянский (нога))
    CONTEXT: односкриптовый родной текст
    EXPECTED: INFO
    RISK: NONE
    GUARD: ARMENIAN_VO_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_004:
    INPUT: "ով" (армянский (кто))
    CONTEXT: односкриптовый родной текст
    EXPECTED: INFO
    RISK: NONE
    GUARD: ARMENIAN_VO_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "որս" (армянский (охота))
    CONTEXT: односкриптовый родной текст
    EXPECTED: INFO
    RISK: NONE
    GUARD: ARMENIAN_VO_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_006:
    INPUT: "ողջ" (армянский (целый/живой))
    CONTEXT: односкриптовый родной текст
    EXPECTED: INFO
    RISK: NONE
    GUARD: ARMENIAN_VO_FORM ≠ AUTOMATICALLY_SPOOF

RISK_CASES:
  RISK_CASE_001:
    NAME: BRAND_HOMOGLYPH
    INPUT: "ոetflix-login.com" (IDN/бренд-подмена — токен выглядит как netflix, но буква — армянская)
    CONTEXT: IDN/бренд-подмена — токен выглядит как netflix, но буква — армянская
    RISK: CRITICAL
    ATTACK: замена латинской n на армянская ո даёт визуально идентичный бренд, который регистрирует атакующий
    GUARD: ARMENIAN_VO_FORM ≠ LATIN_SMALL_N
  RISK_CASE_002:
    NAME: BRAND_DOMAIN_SUBSTITUTION
    INPUT: "liոkedin" (двойник внутри токена `linkedin`)
    CONTEXT: двойник внутри токена `linkedin`
    RISK: CRITICAL
    ATTACK: строка машинно-≠ linkedin, но человек не видит разницы
    GUARD: ARMENIAN_VO_FORM ≠ DOMAIN_VALIDITY_PROOF
  RISK_CASE_003:
    NAME: HANDLE_IMPERSONATION
    INPUT: "@ոortonSupport" (имитация бренд-аккаунта в чате/соцсети)
    CONTEXT: имитация бренд-аккаунта в чате/соцсети
    RISK: HIGH
    ATTACK: похожий хэндл выглядит как nortonSupport, но это другой аккаунт
    GUARD: ARMENIAN_VO_FORM ≠ VERIFICATION
  RISK_CASE_004:
    NAME: FILTER_BYPASS_KEYWORD
    INPUT: "logiո" (обход текстового фильтра, ищущего латинское слово `login`)
    CONTEXT: обход текстового фильтра, ищущего латинское слово `login`
    RISK: HIGH
    ATTACK: одна заменённая буква выводит слово из-под блок-листа
    GUARD: ARMENIAN_VO_FORM ≠ ASCII_LETTER
  RISK_CASE_005:
    NAME: EMAIL_LOOKALIKE
    INPUT: "billing@ոorton-secure.example" (фишинговое письмо от «той же» компании)
    CONTEXT: фишинговое письмо от «той же» компании
    RISK: HIGH
    ATTACK: домен выглядит идентично, но ведёт к атакующему
    GUARD: ARMENIAN_VO_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
  RISK_CASE_006:
    NAME: SECOND_TARGET_BRAND
    INPUT: "biոance-billing.com" (ещё один целевой бренд (binance), открытый двойником)
    CONTEXT: ещё один целевой бренд (binance), открытый двойником
    RISK: HIGH
    ATTACK: цепочка двойников имитирует всё латинское имя бренда
    GUARD: ARMENIAN_VO_FORM ≠ BRAND_NAME_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: n
    CODEPOINT: U+006E
    NAME: LATIN SMALL LETTER N
    RISK: CRITICAL
    RULE: LATIN_SMALL_LETTER_N ≠ ARMENIAN_VO_FORM (главная цель имитации; визуально идентична во многих шрифтах)
  CONFUSABLE_002:
    VISIBLE_FORM: ｎ
    CODEPOINT: U+FF4E
    NAME: FULLWIDTH LATIN SMALL LETTER N
    RISK: MEDIUM
    RULE: FULLWIDTH_LATIN_SMALL_LETTER_N ≠ ARMENIAN_VO_FORM (полноширинная латинская форма; иная форма совместимости)
  CONFUSABLE_003:
    VISIBLE_FORM: 𝗇
    CODEPOINT: U+1D5C7
    NAME: MATHEMATICAL SANS-SERIF SMALL N
    RISK: MEDIUM
    RULE: MATHEMATICAL_SANS_SERIF_SMALL_N ≠ ARMENIAN_VO_FORM (математически-стилизованная латинская буква для обхода простых фильтров)
  CONFUSABLE_004:
    VISIBLE_FORM: 𝐧
    CODEPOINT: U+1D427
    NAME: MATHEMATICAL BOLD SMALL N
    RISK: LOW
    RULE: MATHEMATICAL_BOLD_SMALL_N ≠ ARMENIAN_VO_FORM (полужирная латинская буква)
  CONFUSABLE_005:
    VISIBLE_FORM: 𝑛
    CODEPOINT: U+1D45B
    NAME: MATHEMATICAL ITALIC SMALL N
    RISK: LOW
    RULE: MATHEMATICAL_ITALIC_SMALL_N ≠ ARMENIAN_VO_FORM (курсивная латинская буква)
  CONFUSABLE_006:
    VISIBLE_FORM: 𝚗
    CODEPOINT: U+1D697
    NAME: MATHEMATICAL MONOSPACE SMALL N
    RISK: LOW
    RULE: MATHEMATICAL_MONOSPACE_SMALL_N ≠ ARMENIAN_VO_FORM (моноширинная латинская буква)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "бренд `ոetflix` — это Netflix"
    RESPONSE: ARMENIAN_VO_FORM ≠ LATIN_SMALL_N
    RULE: буква — армянская ո (и гласный /o/ (в начале слова /vo/)); регистрируемый домен/имя иные — решает DNS, а не глаз
  CG2:
    TRIGGER: "строка с этой буквой равна её латинскому написанию"
    RESPONSE: ARMENIAN_VO_FORM ≠ SAME_CODEPOINT_AS_LATIN
    RULE: разные кодовые точки → машинно-разные строки
  CG3:
    TRIGGER: "любое появление этой буквы в тексте — атака"
    RESPONSE: ARMENIAN_VO_FORM ≠ AUTOMATICALLY_SPOOF
    RULE: в односкриптовом родном тексте буква законна; подмена — это СМЕСЬ письменностей в одном токене
  CG4:
    TRIGGER: "ASCII-фильтр поймает заменённое слово"
    RESPONSE: ARMENIAN_VO_FORM ≠ ASCII_LETTER
    RULE: буква вне ASCII; латинский фильтр её не сматчит
  CG5:
    TRIGGER: "хэндл `@ոortonSupport` — тот же аккаунт, что латинский"
    RESPONSE: ARMENIAN_VO_FORM ≠ VERIFICATION
    RULE: визуальное сходство не идентифицирует аккаунт
  CG6:
    TRIGGER: "замена n→ո в идентификаторе безвредна"
    RESPONSE: ARMENIAN_VO_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
    RULE: в домене/логине/токене замена меняет сущность, к которой строка резолвится

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "ոetflix-login.com" (армянская ո + латиница в одном токене)
      NAME: MIXED_SCRIPT_TOKEN
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: IDN/бренд-подмена; ключевой сигнал — СМЕШЕНИЕ письменностей внутри одного токена
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "biոance-billing.com" (двойник с заглавной в начале на целевой бренд)
      NAME: MULTI_HOMOGLYPH_TOKEN
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: множественная/начальная подстановка на целевой бренд
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: not applicable — опасность знака проявляется именно в последовательности (токене), а не в изоляции.

PHAGO_ENTITY_MIMICRY:
  PE_001:
    INPUT: "ոetflix-login.com"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: CRITICAL
    NOTE: буква имитирует само ИМЯ верифицированного бренда (не просто структуру) — прямая имитация существования сущности. Поэтому реестр помечает знак PHAGO ●; коммерческие защиты от двойников часто пропускают этот класс.
  PE_002:
    INPUT: "@ոortonSupport"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: HIGH
    NOTE: имитация официального саппорт-аккаунта бренда через двойника в имени.

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена латинской n (U+006E) на армянская ո (U+0578) в бренд-домене
  A2: смешение ո с math/полноширинной латинской n для усложнения детекции
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: ո обходит латинский блок-лист (logiո)
  B2: ո в почтовом домене (billing@ոorton-secure.example) для фишинга
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: смешанный токен `ոetflix-login.com` (SC1) — письменности внутри одного слова
  C2: начальная/множественная подстановка `biոance-billing.com` (SC2) на целевой бренд
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: хэндл `@ոortonSupport` имитирует бренд-аккаунт
  D2: `billing@ոorton-secure.example` — двойник в псевдо-официальном имени
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: `ոetflix-login.com` — имитация имени бренда (PE_001)
  E2: `@ոortonSupport` — имитация официального аккаунта (PE_002)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у буквы нет спящих/активных эпох (см. раздел 5).
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: `ոetflix-login.com` с ո — домен настоящего бренда
  EXPECTED: FAIL_BRAND_NAME_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: строка с этой буквой машинно равна её латинскому написанию
  EXPECTED: FAIL_CODEPOINT_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: любое появление этой буквы в тексте — атака
  EXPECTED: FAIL_OVERBLOCK_MIMICRY (обратная ошибка: подлинный родной текст — не подмена)
  RESULT: FAIL
MUTATION_04:
  CLAIM: ASCII-фильтр на латинское слово поймает `logiո`
  EXPECTED: FAIL_ASCII_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: хэндл `@ոortonSupport` — тот же аккаунт, что латинский
  EXPECTED: FAIL_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: замена n→ո в идентификаторе безвредна
  EXPECTED: FAIL_IDENTIFIER_INTERCHANGE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как отличить законный односкриптовый родной текст от подмены без ложных срабатываний?
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
