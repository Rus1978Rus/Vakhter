PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_ROMAN_SMALL_I_U2170_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
TRANSLATION_NOTE: Русский оригинал (авторитетный источник). Английский документ SIGN_CORE_CARD_ROMAN_SMALL_I_U2170_GEN3_v0_3_EN — зеркало. Кодовые точки, имена полей и формулы идентичны. Гомоглиф: базовый закон — ВЫГЛЯДИТ_ОДИНАКОВО ≠ ЯВЛЯЕТСЯ_ТЕМ_ЖЕ. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_ROMAN_SMALL_I_U2170_GEN3_v0_3_RU
CODEPOINT: U+2170
VISIBLE_FORM: ⅰ
UNICODE_NAME: SMALL ROMAN NUMERAL ONE
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Руслан Малявский
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: римская цифра «ⅰ» малая один (гомоглиф латинской строчной i)
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
VISIBLE_FORM: ⅰ
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_LETTER_HOMOGLYPH
BASE_MODE_FORMULA: ROMAN_SMALL_I_FORM ≠ LATIN_I
SIGN_CATEGORY:
  - римская цифро-буквоформа «малая римская один» (означает 1 как самостоятельную цифру; символ блока Number Forms)
  - гомоглиф латинской строчной «i» (U+0069)
  - потенциальный носитель гомоглифного спуфинга при вставке ВНУТРЬ латинского слова

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_LATIN_I — римская ⅰ (U+2170) НЕ есть латинская i (U+0069); другая кодовая точка И это цифра (значение 1), а не буква
  2. NOT_SAME_STRING_AS_LATIN — строка с римской ⅰ не машинно-равна своему латинскому двойнику
  3. NOT_BRAND_NAME_PROOF — «ⅰnstagram» не доказывает связь с брендом Instagram
  4. NOT_DOMAIN_VALIDITY_PROOF — визуальное совпадение домена не подтверждает регистрируемый домен
  5. NOT_AUTHORITY — форма не подтверждает официальный статус
  6. NOT_VERIFICATION — не верифицирует соседний факт
  7. NOT_ASCII — не входит в ASCII; фильтры «только ASCII» не видят её как i
  8. NOT_AUTOMATICALLY_SPOOF — как самостоятельная римская цифра она нормальна, не атака
  9. NOT_EXECUTION_TRIGGER — сама по себе ничего не запускает
  10. NOT_TRUST_SIGNAL — не повышает доверие к содержимому
  11. NOT_EFFECT — форма цифры не создаёт эффекта
  12. NOT_INTERCHANGEABLE_IN_IDENTIFIERS — в идентификаторе/домене замена i→ⅰ меняет сущность

BASE_FORMULAS:
  ROMAN_SMALL_I_FORM ≠ LATIN_I
  ROMAN_SMALL_I_FORM ≠ SAME_CODEPOINT_AS_LATIN
  ROMAN_SMALL_I_FORM ≠ BRAND_NAME_PROOF
  ROMAN_SMALL_I_FORM ≠ DOMAIN_VALIDITY_PROOF
  ROMAN_SMALL_I_FORM ≠ AUTHORITY
  ROMAN_SMALL_I_FORM ≠ VERIFICATION
  ROMAN_SMALL_I_FORM ≠ ASCII_LETTER
  ROMAN_SMALL_I_FORM ≠ AUTOMATICALLY_SPOOF
  ROMAN_SMALL_I_FORM ≠ TRUST_SIGNAL
  ROMAN_SMALL_I_FORM ≠ EFFECT
  ROMAN_SMALL_I_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: римская «ⅰ» малая один — стабильная цифро-форма без культурной прецессии функций. «Гомоглиф» — не эпоха, а свойство визуального совпадения с латинской i, сосуществующее с легитимной цифровой функцией формы. Опасность контекстна (вставка внутрь латинского слова), а не эпохальна — поэтому SEMANTIC_EPOCH_TRACKER не применяется.
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
    INPUT: "part ⅰ" (часть 1, римская цифра)
    CONTEXT: самостоятельная римская цифра (отдельный токен)
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_SMALL_I_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_002:
    INPUT: "volume ⅰ" (том 1, римская цифра)
    CONTEXT: римская цифра как цельный токен, не внутри слова
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_SMALL_I_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "ⅰⅰ guests" (2 гостя, римская цифра)
    CONTEXT: цельный токен из римских цифр
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_SMALL_I_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_004:
    INPUT: "chapter ⅰ" (глава 1, римская цифра)
    CONTEXT: цельный токен из римских цифр рядом с латинским словом
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_SMALL_I_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "ⅰⅴ chapters" (4 главы, римская цифра)
    CONTEXT: цельный токен из римских цифр
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_SMALL_I_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_006:
    INPUT: "ⅰⅹ items" (9 предметов, римская цифра)
    CONTEXT: цельный токен из римских цифр
    EXPECTED: INFO
    RISK: NONE
    GUARD: ROMAN_SMALL_I_FORM ≠ AUTOMATICALLY_SPOOF

RISK_CASES:
  RISK_CASE_001:
    NAME: BRAND_HOMOGLYPH
    INPUT: "ⅰnstagram-login.com"
    CONTEXT: IDN/бренд-спуф — токен выглядит как instagram, но первый символ — римская цифра
    RISK: CRITICAL
    ATTACK: замена латинской i на римскую ⅰ даёт визуально идентичный бренд, который регистрирует атакующий
    GUARD: ROMAN_SMALL_I_FORM ≠ LATIN_I
  RISK_CASE_002:
    NAME: MIDTOKEN_BRAND_SUBSTITUTION
    INPUT: "twⅰtter-alert.com"
    CONTEXT: подмена в середине токена бренда
    RISK: CRITICAL
    ATTACK: строка машинно-≠ twitter, но человек не видит разницы
    GUARD: ROMAN_SMALL_I_FORM ≠ DOMAIN_VALIDITY_PROOF
  RISK_CASE_003:
    NAME: HANDLE_IMPERSONATION
    INPUT: "@ⅰntuitCare"
    CONTEXT: имперсонация бренд-аккаунта в чате/соцсети
    RISK: HIGH
    ATTACK: похожий хэндл выглядит как intuitCare, но это другой аккаунт
    GUARD: ROMAN_SMALL_I_FORM ≠ VERIFICATION
  RISK_CASE_004:
    NAME: FILTER_BYPASS_KEYWORD
    INPUT: "ⅰnvoice"
    CONTEXT: обход текстового фильтра, ищущего латинское слово
    RISK: HIGH
    ATTACK: одна подменённая литера выводит слово из-под блок-листа
    GUARD: ROMAN_SMALL_I_FORM ≠ ASCII_LETTER
  RISK_CASE_005:
    NAME: EMAIL_LOOKALIKE
    INPUT: "no-reply@ⅰcloud-secure.example"
    CONTEXT: фишинговое письмо от «той же» компании
    RISK: HIGH
    ATTACK: домен выглядит идентично, но ведёт к атакующему
    GUARD: ROMAN_SMALL_I_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
  RISK_CASE_006:
    NAME: MULTI_HOMOGLYPH_ON_TARGET
    INPUT: "fⅰjⅰ"
    CONTEXT: две римские ⅰ среди латинских букв, имитирующие fiji (ⅰ римская, f/j латиница — цифра-в-слове)
    RISK: HIGH
    ATTACK: цепочка двойников имитирует всё латинское имя бренда
    GUARD: ROMAN_SMALL_I_FORM ≠ BRAND_NAME_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: i
    CODEPOINT: U+0069
    NAME: LATIN SMALL LETTER I
    RISK: CRITICAL
    RULE: LATIN_I ≠ ROMAN_SMALL_I (главная цель имперсонации; визуально идентична во многих шрифтах)
  CONFUSABLE_002:
    VISIBLE_FORM: і
    CODEPOINT: U+0456
    NAME: CYRILLIC SMALL LETTER BYELORUSSIAN-UKRAINIAN I
    RISK: HIGH
    RULE: CYRILLIC_I ≠ ROMAN_SMALL_I (другой скрипт с той же формой i; усложняет детекцию)
  CONFUSABLE_003:
    VISIBLE_FORM: ｉ
    CODEPOINT: U+FF49
    NAME: FULLWIDTH LATIN SMALL LETTER I
    RISK: MEDIUM
    RULE: FULLWIDTH_SMALL_I ≠ ROMAN_SMALL_I (полноширинная латинская i; другая форма совместимости)
  CONFUSABLE_004:
    VISIBLE_FORM: 𝗂
    CODEPOINT: U+1D5C2
    NAME: MATHEMATICAL SANS-SERIF SMALL I
    RISK: MEDIUM
    RULE: MATH_SANS_SMALL_I ≠ ROMAN_SMALL_I (математически-стилизованная латинская i для обхода простых фильтров)
  CONFUSABLE_005:
    VISIBLE_FORM: 𝐢
    CODEPOINT: U+1D422
    NAME: MATHEMATICAL BOLD SMALL I
    RISK: LOW
    RULE: MATH_BOLD_SMALL_I ≠ ROMAN_SMALL_I (жирная латинская i)
  CONFUSABLE_006:
    VISIBLE_FORM: 𝑖
    CODEPOINT: U+1D456
    NAME: MATHEMATICAL ITALIC SMALL I
    RISK: LOW
    RULE: MATH_ITALIC_SMALL_I ≠ ROMAN_SMALL_I (курсивная латинская i)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: «бренд `ⅰnstagram` — это Instagram»
    RESPONSE: ROMAN_SMALL_I_FORM ≠ LATIN_I
    RULE: первый символ — римская цифра (1); регистрируемый домен/имя другой — решает DNS, а не глаз
  CG2:
    TRIGGER: «строка с римской ⅰ равна её латинскому написанию»
    RESPONSE: ROMAN_SMALL_I_FORM ≠ SAME_CODEPOINT_AS_LATIN
    RULE: разные кодовые точки → машинно-разные строки
  CG3:
    TRIGGER: «любая римская ⅰ в тексте — атака»
    RESPONSE: ROMAN_SMALL_I_FORM ≠ AUTOMATICALLY_SPOOF
    RULE: самостоятельная римская цифра легитимна; спуф — это цифро-форма, вставленная ВНУТРЬ латинского слова
  CG4:
    TRIGGER: «ASCII-фильтр поймает подменённое слово»
    RESPONSE: ROMAN_SMALL_I_FORM ≠ ASCII_LETTER
    RULE: римская ⅰ вне ASCII; латинский фильтр её не сматчит
  CG5:
    TRIGGER: «хэндл `@ⅰntuitCare` — тот же аккаунт, что и @intuitCare»
    RESPONSE: ROMAN_SMALL_I_FORM ≠ VERIFICATION
    RULE: визуальное сходство не идентифицирует аккаунт
  CG6:
    TRIGGER: «замена i→ⅰ в идентификаторе безвредна»
    RESPONSE: ROMAN_SMALL_I_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
    RULE: в домене/логине/токене замена меняет сущность, к которой резолвится строка

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "ⅰnstagram" (римская ⅰ + латиница в одном токене)
      NAME: NUMERAL_IN_WORD_TOKEN
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: IDN/бренд-спуф; ключевой сигнал — римская цифро-форма ВНУТРИ ASCII-латинского слова
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "fⅰjⅰ" (две римские ⅰ среди латинских букв)
      NAME: MULTI_HOMOGLYPH_TOKEN
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: множественная подмена на целевой бренд
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: не применимо — опасность знака проявляется именно в последовательности (в токене), а не в изоляции.

PHAGO_ENTITY_MIMICRY:
  PE_001:
    INPUT: "ⅰnstagram-login.com"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: CRITICAL
    NOTE: римская ⅰ имитирует само ИМЯ верифицированного бренда (а не только структуру) — прямая имитация существования сущности. Поэтому реестр помечает знак PHAGO ●; коммерческие защиты от двойников этот класс часто пропускают.
  PE_002:
    INPUT: "@ⅰntuitCare"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: HIGH
    NOTE: имперсонация официального аккаунта поддержки бренда через двойника в имени.

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена латинской i (U+0069) на римскую ⅰ (U+2170) в домене бренда
  A2: смешение римской ⅰ с кириллической і / математической sans-serif i для усложнения детекции
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: римская ⅰ обходит латинский блок-лист ключевых слов (ⅰnvoice)
  B2: римская ⅰ в почтовом домене (no-reply@ⅰcloud-secure.example) для фишинга
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: токен-цифра-в-слове `ⅰnstagram` (SC1) — римская форма внутри одного слова
  C2: множественная подмена `fⅰjⅰ` (SC2) на целевой бренд
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: хэндл `@ⅰntuitCare` имитирует бренд-аккаунт
  D2: "ⅰcloud-secure" — двойник в псевдо-официальном имени
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: `ⅰnstagram-login.com` — имитация имени бренда (PE_001)
  E2: `@ⅰntuitCare` — имитация официального аккаунта (PE_002)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, форма не имеет спящих/активных эпох (см. раздел 5).
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: `ⅰnstagram-login.com` с римской ⅰ — это домен Instagram
  EXPECTED: FAIL_BRAND_NAME_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: строка с римской ⅰ машинно-равна её латинскому написанию
  EXPECTED: FAIL_CODEPOINT_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: любая римская ⅰ в тексте — атака
  EXPECTED: FAIL_OVERBLOCK_MIMICRY (обратная ошибка: самостоятельная римская цифра — не спуф)
  RESULT: FAIL
MUTATION_04:
  CLAIM: ASCII-фильтр на "invoice" поймает "ⅰnvoice"
  EXPECTED: FAIL_ASCII_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: хэндл `@ⅰntuitCare` — тот же аккаунт, что и `@intuitCare`
  EXPECTED: FAIL_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: замена i→ⅰ в идентификаторе безвредна
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
