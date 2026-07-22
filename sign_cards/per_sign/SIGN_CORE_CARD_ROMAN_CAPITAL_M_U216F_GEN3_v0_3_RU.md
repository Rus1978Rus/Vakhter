PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_ROMAN_CAPITAL_M_U216F_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
TRANSLATION_NOTE: Русский оригинал (авторитетный источник). Английский документ SIGN_CORE_CARD_ROMAN_CAPITAL_M_U216F_GEN3_v0_3_EN — зеркало. Кодовые точки, имена полей и формулы идентичны. Гомоглиф: базовый закон — ВЫГЛЯДИТ_ОДИНАКОВО ≠ ЯВЛЯЕТСЯ_ТЕМ_ЖЕ. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_ROMAN_CAPITAL_M_U216F_GEN3_v0_3_RU
CODEPOINT: U+216F
VISIBLE_FORM: Ⅿ
UNICODE_NAME: ROMAN NUMERAL ONE THOUSAND
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Руслан Малявский
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: римская цифра «Ⅿ» тысяча (гомоглиф латинской заглавной M)
CATEGORY_ROADMAP: PH (фишинг) · PHAGO: ● (сильный носитель — имитирует само имя бренда)

============================================================
3. REQUIRED_GENERAL_GUARDS
============================================================
REQUIRED_GENERAL_GUARDS:
  - SIGN_FALSE_EFFECT_MIMICRY_GUARD_v0_2A_RU
    GUARD_COMPATIBILITY: применимо — знак не создаёт полей-эффектов; для гомоглифа-цифроформы гард расширяется проверкой «римская цифро-форма внутри латинского слова» на уровне интегратора
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
VISIBLE_FORM: Ⅿ
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_LETTER_HOMOGLYPH
BASE_MODE_FORMULA: ROMAN_CAP_M_FORM ≠ LATIN_CAP_M
SIGN_CATEGORY:
  - римская цифро-буквоформа «римская тысяча» (означает 1000 как самостоятельную цифру; символ блока Number Forms)
  - гомоглиф латинской заглавной «M» (U+004D)
  - потенциальный носитель гомоглифного спуфинга при вставке ВНУТРЬ латинского слова

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_LATIN_CAP_M — римская Ⅿ (U+216F) НЕ есть латинская M (U+004D); другая кодовая точка И это цифра (значение 1000), а не буква
  2. NOT_SAME_STRING_AS_LATIN — строка с римской Ⅿ не машинно-равна своему латинскому двойнику
  3. NOT_BRAND_NAME_PROOF — «ⅯETA» не доказывает связь с брендом Meta
  4. NOT_DOMAIN_VALIDITY_PROOF — визуальное совпадение домена не подтверждает регистрируемый домен
  5. NOT_AUTHORITY — форма не подтверждает официальный статус
  6. NOT_VERIFICATION — не верифицирует соседний факт
  7. NOT_ASCII — не входит в ASCII; фильтры «только ASCII» не видят её как M
  8. NOT_AUTOMATICALLY_SPOOF — как самостоятельная римская цифра она нормальна, не атака
  9. NOT_EXECUTION_TRIGGER — сама по себе ничего не запускает
  10. NOT_TRUST_SIGNAL — не повышает доверие к содержимому
  11. NOT_EFFECT — форма цифры не создаёт эффекта
  12. NOT_INTERCHANGEABLE_IN_IDENTIFIERS — в идентификаторе/домене замена M→Ⅿ меняет сущность

BASE_FORMULAS:
  ROMAN_CAP_M_FORM ≠ LATIN_CAP_M
  ROMAN_CAP_M_FORM ≠ SAME_CODEPOINT_AS_LATIN
  ROMAN_CAP_M_FORM ≠ BRAND_NAME_PROOF
  ROMAN_CAP_M_FORM ≠ DOMAIN_VALIDITY_PROOF
  ROMAN_CAP_M_FORM ≠ AUTHORITY
  ROMAN_CAP_M_FORM ≠ VERIFICATION
  ROMAN_CAP_M_FORM ≠ ASCII_LETTER
  ROMAN_CAP_M_FORM ≠ AUTOMATICALLY_SPOOF
  ROMAN_CAP_M_FORM ≠ TRUST_SIGNAL
  ROMAN_CAP_M_FORM ≠ EFFECT
  ROMAN_CAP_M_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: римская «Ⅿ» тысяча — стабильная цифро-форма без культурной прецессии функций. «Гомоглиф» — не эпоха, а свойство визуального совпадения с латинской M, сосуществующее с легитимной цифровой функцией формы. Опасность контекстна (вставка внутрь латинского слова), а не эпохальна — поэтому SEMANTIC_EPOCH_TRACKER не применяется.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1 (физический жест)
  NOTE: цифро-форма — письменный знак без жестового предшественника; римские цифро-буквоформы — кодировка Number Forms латинских букв, используемых как цифры.

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
    INPUT: "Ⅿ years" (1000 лет, римская цифра)
    CONTEXT: самостоятельная римская цифра (отдельный токен)
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_CAP_M_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_002:
    INPUT: "Page Ⅿ" (страница 1000, римская цифра)
    CONTEXT: римская цифра как цельный токен, не внутри слова
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_CAP_M_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "Volume Ⅿ" (том 1000, римская цифра)
    CONTEXT: самостоятельный токен римской цифры рядом с латинским словом
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_CAP_M_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_004:
    INPUT: "Chapter Ⅿ" (глава 1000, римская цифра)
    CONTEXT: самостоятельный токен римской цифры рядом с латинским словом
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_CAP_M_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "ⅯⅮ coins" (1500 монет, римская цифра)
    CONTEXT: цельный токен из римских цифр
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_CAP_M_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_006:
    INPUT: "ⅯⅭ items" (1100 предметов, римская цифра)
    CONTEXT: цельный токен из римских цифр
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_CAP_M_FORM ≠ AUTOMATICALLY_SPOOF

RISK_CASES:
  RISK_CASE_001:
    NAME: BRAND_HOMOGLYPH
    INPUT: "ⅯETA-ads.com"
    CONTEXT: IDN/бренд-спуф — токен выглядит как META, но первый символ — римская цифра
    RISK: CRITICAL
    ATTACK: замена латинской M на римскую Ⅿ даёт визуально идентичный бренд, который регистрирует атакующий
    GUARD: ROMAN_CAP_M_FORM ≠ LATIN_CAP_M
  RISK_CASE_002:
    NAME: ALLCAPS_BRAND_SUBSTITUTION
    INPUT: "ⅯGM-rewards-deal.com"
    CONTEXT: ведущая подмена в капслок-названии бренда
    RISK: CRITICAL
    ATTACK: строка машинно-≠ MGM, но человек не видит разницы
    GUARD: ROMAN_CAP_M_FORM ≠ DOMAIN_VALIDITY_PROOF
  RISK_CASE_003:
    NAME: HANDLE_IMPERSONATION
    INPUT: "@ⅯcAfeeHelp"
    CONTEXT: имперсонация бренд-аккаунта в чате/соцсети
    RISK: HIGH
    ATTACK: похожий хэндл выглядит как McAfeeHelp, но это другой аккаунт
    GUARD: ROMAN_CAP_M_FORM ≠ VERIFICATION
  RISK_CASE_004:
    NAME: FILTER_BYPASS_KEYWORD
    INPUT: "ⅯENU"
    CONTEXT: обход текстового фильтра, ищущего латинское слово
    RISK: HIGH
    ATTACK: одна подменённая литера выводит слово из-под блок-листа
    GUARD: ROMAN_CAP_M_FORM ≠ ASCII_LETTER
  RISK_CASE_005:
    NAME: EMAIL_LOOKALIKE
    INPUT: "no-reply@ⅯICROSOFT-secure.example"
    CONTEXT: фишинговое письмо от «той же» компании
    RISK: HIGH
    ATTACK: домен выглядит идентично, но ведёт к атакующему
    GUARD: ROMAN_CAP_M_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
  RISK_CASE_006:
    NAME: MULTI_HOMOGLYPH_ON_TARGET
    INPUT: "ⅯAXIⅯ"
    CONTEXT: две римские Ⅿ вокруг латинских букв, имитирующие MAXIM (Ⅿ римская, AXI латиница — цифра-в-слове)
    RISK: HIGH
    ATTACK: цепочка двойников имитирует всё латинское имя бренда
    GUARD: ROMAN_CAP_M_FORM ≠ BRAND_NAME_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: M
    CODEPOINT: U+004D
    NAME: LATIN CAPITAL LETTER M
    RISK: CRITICAL
    RULE: LATIN_CAP_M ≠ ROMAN_CAP_M (главная цель имперсонации; визуально идентична во многих шрифтах)
  CONFUSABLE_002:
    VISIBLE_FORM: М
    CODEPOINT: U+041C
    NAME: CYRILLIC CAPITAL LETTER EM
    RISK: HIGH
    RULE: CYRILLIC_CAP_EM ≠ ROMAN_CAP_M (другой скрипт с той же формой M; усложняет детекцию)
  CONFUSABLE_003:
    VISIBLE_FORM: Ｍ
    CODEPOINT: U+FF2D
    NAME: FULLWIDTH LATIN CAPITAL LETTER M
    RISK: MEDIUM
    RULE: FULLWIDTH_CAP_M ≠ ROMAN_CAP_M (полноширинная латинская M; другая форма совместимости)
  CONFUSABLE_004:
    VISIBLE_FORM: 𝗠
    CODEPOINT: U+1D5E0
    NAME: MATHEMATICAL SANS-SERIF BOLD CAPITAL M
    RISK: MEDIUM
    RULE: MATH_SANS_CAP_M ≠ ROMAN_CAP_M (математически-стилизованная латинская M для обхода простых фильтров)
  CONFUSABLE_005:
    VISIBLE_FORM: 𝐌
    CODEPOINT: U+1D40C
    NAME: MATHEMATICAL BOLD CAPITAL M
    RISK: LOW
    RULE: MATH_BOLD_CAP_M ≠ ROMAN_CAP_M (жирная латинская M)
  CONFUSABLE_006:
    VISIBLE_FORM: 𝑀
    CODEPOINT: U+1D440
    NAME: MATHEMATICAL ITALIC CAPITAL M
    RISK: LOW
    RULE: MATH_ITALIC_CAP_M ≠ ROMAN_CAP_M (курсивная латинская M)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: «бренд `ⅯETA` — это Meta»
    RESPONSE: ROMAN_CAP_M_FORM ≠ LATIN_CAP_M
    RULE: первый символ — римская цифра (1000); регистрируемый домен/имя другой — решает DNS, а не глаз
  CG2:
    TRIGGER: «строка с римской Ⅿ равна её латинскому написанию»
    RESPONSE: ROMAN_CAP_M_FORM ≠ SAME_CODEPOINT_AS_LATIN
    RULE: разные кодовые точки → машинно-разные строки
  CG3:
    TRIGGER: «любая римская Ⅿ в тексте — атака»
    RESPONSE: ROMAN_CAP_M_FORM ≠ AUTOMATICALLY_SPOOF
    RULE: самостоятельная римская цифра легитимна; спуф — это цифро-форма, вставленная ВНУТРЬ латинского слова
  CG4:
    TRIGGER: «ASCII-фильтр поймает подменённое слово»
    RESPONSE: ROMAN_CAP_M_FORM ≠ ASCII_LETTER
    RULE: римская Ⅿ вне ASCII; латинский фильтр её не сматчит
  CG5:
    TRIGGER: «хэндл `@ⅯcAfeeHelp` — тот же аккаунт, что и @McAfeeHelp»
    RESPONSE: ROMAN_CAP_M_FORM ≠ VERIFICATION
    RULE: визуальное сходство не идентифицирует аккаунт
  CG6:
    TRIGGER: «замена M→Ⅿ в идентификаторе безвредна»
    RESPONSE: ROMAN_CAP_M_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
    RULE: в домене/логине/токене замена меняет сущность, к которой резолвится строка

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "ⅯETA" (римская Ⅿ + латиница в одном токене)
      NAME: NUMERAL_IN_WORD_TOKEN
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: IDN/бренд-спуф; ключевой сигнал — римская цифро-форма ВНУТРИ ASCII-латинского слова
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "ⅯAXIⅯ" (две римские Ⅿ среди латинских заглавных)
      NAME: MULTI_HOMOGLYPH_TOKEN
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: множественная подмена на целевой капслок-бренд
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: не применимо — опасность знака проявляется именно в последовательности (в токене), а не в изоляции.

PHAGO_ENTITY_MIMICRY:
  PE_001:
    INPUT: "ⅯETA-ads.com"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: CRITICAL
    NOTE: римская Ⅿ имитирует само ИМЯ верифицированного бренда (а не только структуру) — прямая имитация существования сущности. Поэтому реестр помечает знак PHAGO ●; коммерческие защиты от двойников этот класс часто пропускают.
  PE_002:
    INPUT: "@ⅯcAfeeHelp"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: HIGH
    NOTE: имперсонация официального аккаунта поддержки бренда через двойника в имени.

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена латинской M (U+004D) на римскую Ⅿ (U+216F) в домене бренда
  A2: смешение римской Ⅿ с кириллической Em М / математической sans-serif M для усложнения детекции
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: римская Ⅿ обходит латинский блок-лист ключевых слов (ⅯENU)
  B2: римская Ⅿ в почтовом домене (no-reply@ⅯICROSOFT-secure.example) для фишинга
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: токен-цифра-в-слове `ⅯETA` (SC1) — римская форма внутри одного слова
  C2: множественная подмена `ⅯAXIⅯ` (SC2) на целевой бренд
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: хэндл `@ⅯcAfeeHelp` имитирует бренд-аккаунт
  D2: "ⅯICROSOFT-secure" — двойник в псевдо-официальном имени
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: `ⅯETA-ads.com` — имитация имени бренда (PE_001)
  E2: `@ⅯcAfeeHelp` — имитация официального аккаунта (PE_002)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, форма не имеет спящих/активных эпох (см. раздел 5).
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: `ⅯETA-ads.com` с римской Ⅿ — это домен Meta
  EXPECTED: FAIL_BRAND_NAME_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: строка с римской Ⅿ машинно-равна её латинскому написанию
  EXPECTED: FAIL_CODEPOINT_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: любая римская Ⅿ в тексте — атака
  EXPECTED: FAIL_OVERBLOCK_MIMICRY (обратная ошибка: самостоятельная римская цифра — не спуф)
  RESULT: FAIL
MUTATION_04:
  CLAIM: ASCII-фильтр на "MENU" поймает "ⅯENU"
  EXPECTED: FAIL_ASCII_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: хэндл `@ⅯcAfeeHelp` — тот же аккаунт, что и `@McAfeeHelp`
  EXPECTED: FAIL_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: замена M→Ⅿ в идентификаторе безвредна
  EXPECTED: FAIL_IDENTIFIER_INTERCHANGE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как отличить легитимную самостоятельную римскую цифру от цифро-формы, вставленной в слово, без ложных срабатываний?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (правило «римская цифро-форма внутри ASCII-латинского слова» — забота интегратора; см. прототип Vakhter confusable_cards.py)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует формулу LOOKS_SAME ≠ IS_SAME и правило «спуф = цифра-в-слове, а не самостоятельная».
OQ2:
  QUESTION: нужна ли полная таблица UTS #39 confusables + корпус брендов для случая целого слова?
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
