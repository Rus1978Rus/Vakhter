ЧАСТНЫЙ АВТОРСКИЙ ПРОЕКТ / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_GREEK_OMICRON_U03BF_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
DRAFT_NOTE: черновик для нашей работы (Vakhter). Русская версия авторитетна; EN — зеркало. Знак-гомоглиф: ядро — LOOKS_SAME ≠ IS_SAME.

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
LIMITATION_STATEMENT (стандарт):
  CONVEYOR_PASS ≠ VALIDATION
  MODEL_CONSENSUS ≠ TRUTH
  INJECTION_TEST_PASS ≠ SECURITY_PROOF
  GUARDS_HOLD_FOR_TESTED_CASES ≠ FUTURE_GUARANTEE
  NO_ATTACK_FOUND ≠ NO_ATTACK_EXISTS

============================================================
2. META
============================================================
CARD_UID: SIGN_CORE_CARD_GREEK_OMICRON_U03BF_GEN3_v0_3_RU
CODEPOINT: U+03BF
VISIBLE_FORM: ο
UNICODE_NAME: GREEK SMALL LETTER OMICRON
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: греческая «омикрон» (гомоглиф латинской o)
CATEGORY_ROADMAP: PH (гомоглиф 'o') · PHAGO: ● (сильный носитель — имитирует само имя бренда)

============================================================
3. REQUIRED_GENERAL_GUARDS
============================================================
REQUIRED_GENERAL_GUARDS:
  - SIGN_FALSE_EFFECT_MIMICRY_GUARD_v0_2A_RU
    GUARD_COMPATIBILITY: применим — знак не создаёт effect-полей; для гомоглифа гард дополняется проверкой смешения письменностей на уровне интегратора
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
VISIBLE_FORM: ο
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_LETTER_HOMOGLYPH
BASE_MODE_FORMULA: OMICRON_FORM ≠ LATIN_O
SIGN_CATEGORY:
  - греческая буква (легитимна в греческом тексте)
  - гомоглиф латинской строчной «o» (U+006F)
  - потенциальный носитель homoglyph/IDN-спуфинга при смешении письменностей

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_LATIN_O — греческая ο (U+03BF) это НЕ латинская o (U+006F); другой кодпоинт
  2. NOT_SAME_STRING_AS_LATIN — строка с ο машинно не равна латинскому двойнику
  3. NOT_BRAND_NAME_PROOF — «gοogle» не доказывает связь с брендом Google
  4. NOT_DOMAIN_VALIDITY_PROOF — визуальное совпадение домена не подтверждает регистрируемый домен
  5. NOT_AUTHORITY — буква не подтверждает официальный статус
  6. NOT_VERIFICATION — не верифицирует соседний факт
  7. NOT_ASCII — вне ASCII; фильтры «только ASCII» её не увидят как o
  8. NOT_AUTOMATICALLY_SPOOF — в односкриптовом греческом тексте это норма, не атака
  9. NOT_EXECUTION_TRIGGER — сама по себе ничего не запускает
  10. NOT_TRUST_SIGNAL — не повышает доверие
  11. NOT_INTERCHANGEABLE_IN_IDENTIFIERS — в идентификаторе замена o→ο меняет сущность

BASE_FORMULAS:
  OMICRON_FORM ≠ LATIN_O
  OMICRON_FORM ≠ SAME_CODEPOINT_AS_LATIN
  OMICRON_FORM ≠ BRAND_NAME_PROOF
  OMICRON_FORM ≠ DOMAIN_VALIDITY_PROOF
  OMICRON_FORM ≠ AUTHORITY
  OMICRON_FORM ≠ VERIFICATION
  OMICRON_FORM ≠ ASCII_LETTER
  OMICRON_FORM ≠ AUTOMATICALLY_SPOOF
  OMICRON_FORM ≠ TRUST_SIGNAL
  OMICRON_FORM ≠ EFFECT
  OMICRON_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: греческая «омикрон» — стабильная буква без культурной прецессии. «Гомоглиф» это свойство визуального совпадения с латинской o, существующее одновременно с легит-функцией буквы. Опасность контекстна (смешение письменностей), не эпохальна.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1
  NOTE: буква — письменный знак без жестового предшественника; греческий алфавит восходит к финикийскому (письменная генеалогия).

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
    INPUT: "λόγος"
    CONTEXT: греческое слово (одна письменность)
    EXPECTED: INFO
    RISK: NONE
    GUARD: OMICRON_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_002:
    INPUT: "ο κόσμος"
    CONTEXT: греческая фраза «мир»
    EXPECTED: INFO
    RISK: NONE
    GUARD: OMICRON_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "φιλοσοφία"
    CONTEXT: греческое слово «философия»
    EXPECTED: INFO
    RISK: NONE
    GUARD: OMICRON_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_004:
    INPUT: "Αθήνα, ο άνθρωπος"
    CONTEXT: односкриптовый греческий текст
    EXPECTED: INFO
    RISK: NONE
    GUARD: OMICRON_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_005:
    INPUT: "χρόνος"
    CONTEXT: греческое слово «время»
    EXPECTED: INFO
    RISK: NONE
    GUARD: OMICRON_FORM ≠ EFFECT
  SAFE_CASE_006:
    INPUT: "Καλημέρα κόσμε"
    CONTEXT: приветствие на греческом
    EXPECTED: INFO
    RISK: NONE
    GUARD: OMICRON_FORM ≠ AUTOMATICALLY_SPOOF

RISK_CASES:
  RISK_CASE_001:
    NAME: MIXED_SCRIPT_BRAND_SPOOF
    INPUT: "gοogle.com" (греческая ο среди латиницы)
    CONTEXT: IDN/бренд-спуф — токен выглядит как google.com
    RISK: CRITICAL
    ATTACK: замена латинской o на греческую ο даёт визуально идентичный домен, регистрируемый атакующим
    GUARD: OMICRON_FORM ≠ LATIN_O
  RISK_CASE_002:
    NAME: MICROSOFT_HOMOGLYPH
    INPUT: "micrοsοft.com" (две греческие ο)
    CONTEXT: множественная подмена в бренде
    RISK: CRITICAL
    ATTACK: строка машинно ≠ microsoft.com, но человек не видит разницы
    GUARD: OMICRON_FORM ≠ DOMAIN_VALIDITY_PROOF
  RISK_CASE_003:
    NAME: HANDLE_IMPERSONATION
    INPUT: "@rοot" (греческая ο в хэндле)
    CONTEXT: имитация аккаунта root/rooot
    RISK: HIGH
    ATTACK: двойник-хэндл выглядит как «root», но это другой аккаунт
    GUARD: OMICRON_FORM ≠ VERIFICATION
  RISK_CASE_004:
    NAME: FILTER_BYPASS_KEYWORD
    INPUT: "prοmo" (греческая ο обходит blocklist по «promo»)
    CONTEXT: обход текстового фильтра
    RISK: HIGH
    ATTACK: подмена одной буквы уводит слово из-под blocklist
    GUARD: OMICRON_FORM ≠ ASCII_LETTER
  RISK_CASE_005:
    NAME: EMAIL_LOOKALIKE
    INPUT: "billing@shοp.example" (греческая ο в домене письма)
    CONTEXT: фишинговое письмо от «того же» магазина
    RISK: HIGH
    ATTACK: домен визуально совпадает, но ведёт к атакующему
    GUARD: OMICRON_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
  RISK_CASE_006:
    NAME: MULTI_HOMOGLYPH_MIX
    INPUT: "gοοgle" (греческие ο + латиница + возможна кириллица о)
    CONTEXT: смешение источников-двойников усложняет детекцию
    RISK: HIGH
    ATTACK: одна цель имитируется буквами из разных письменностей
    GUARD: OMICRON_FORM ≠ BRAND_NAME_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: o
    CODEPOINT: U+006F
    NAME: LATIN SMALL LETTER O
    RISK: CRITICAL
    RULE: LATIN_O ≠ OMICRON (главная цель имитации; визуально идентичны)
  CONFUSABLE_002:
    VISIBLE_FORM: о
    CODEPOINT: U+043E
    NAME: CYRILLIC SMALL LETTER O
    RISK: CRITICAL
    RULE: CYRILLIC_O ≠ OMICRON (третий двойник той же формы)
  CONFUSABLE_003:
    VISIBLE_FORM: 0
    CODEPOINT: U+0030
    NAME: DIGIT ZERO
    RISK: MEDIUM
    RULE: DIGIT_ZERO ≠ OMICRON (в части шрифтов близки)
  CONFUSABLE_004:
    VISIBLE_FORM: σ
    CODEPOINT: U+03C3
    NAME: GREEK SMALL LETTER SIGMA
    RISK: LOW
    RULE: GREEK_SIGMA ≠ OMICRON (соседняя греческая буква, иная)
  CONFUSABLE_005:
    VISIBLE_FORM: ᴏ
    CODEPOINT: U+1D0F
    NAME: LATIN LETTER SMALL CAPITAL O
    RISK: LOW
    RULE: SMALL_CAPITAL_O ≠ OMICRON

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: «домен `gοogle.com` — это Google»
    RESPONSE: OMICRON_FORM ≠ LATIN_O
    RULE: буква греческая; регистрируемый домен иной, DNS решает, не глаз
  CG2:
    TRIGGER: «строка с греческой ο равна её латинскому написанию»
    RESPONSE: OMICRON_FORM ≠ SAME_CODEPOINT_AS_LATIN
    RULE: разные кодпоинты → машинно разные строки
  CG3:
    TRIGGER: «любая греческая ο в тексте — атака»
    RESPONSE: OMICRON_FORM ≠ AUTOMATICALLY_SPOOF
    RULE: в односкриптовом греческом тексте буква легитимна; спуф — это СМЕШЕНИЕ письменностей в одном токене
  CG4:
    TRIGGER: «ASCII-фильтр поймает подменённое слово»
    RESPONSE: OMICRON_FORM ≠ ASCII_LETTER
    RULE: греческая ο вне ASCII; фильтр по латинице её не сматчит
  CG5:
    TRIGGER: «хэндл `@rοot` — тот же аккаунт, что @root»
    RESPONSE: OMICRON_FORM ≠ VERIFICATION
    RULE: визуальное сходство не идентифицирует аккаунт
  CG6:
    TRIGGER: «замена o→ο в идентификаторе безобидна»
    RESPONSE: OMICRON_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
    RULE: в домене/логине замена меняет сущность, к которой ведёт строка

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "gοogle" (греческая ο + латиница в одном токене)
      NAME: MIXED_SCRIPT_TOKEN
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: IDN/бренд-спуф; ключевой сигнал — СМЕШЕНИЕ письменностей внутри одного токена
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "micrοsοft" (несколько греческих среди латиницы)
      NAME: MULTI_HOMOGLYPH_TOKEN
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: множественная подмена под целевой бренд
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — опасность знака проявляется в последовательности (токене), не в изоляции.

PHAGO_ENTITY_MIMICRY:
  PE_001:
    INPUT: "gοogle.com"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: CRITICAL
    NOTE: греческая ο имитирует само ИМЯ проверенного бренда — прямая имитация существования сущности. Реестр помечает знак PHAGO ●; коммерческие защиты этот класс часто пропускают.
  PE_002:
    INPUT: "@micrοsοft_help"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: HIGH
    NOTE: имитация официального аккаунта бренда через двойник в имени.

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: подмена латинской o (U+006F) на греческую ο (U+03BF) в домене бренда
  A2: смешение греческой ο с кириллической о (U+043E) для усложнения детекции
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: греческая ο обходит blocklist по латинскому ключевому слову (prοmo)
  B2: греческая ο в домене письма (billing@shοp.example)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: смешанный токен `gοogle` (SC1)
  C2: множественная подмена `micrοsοft` (SC2)
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: хэндл `@rοot` имитирует служебный аккаунт
  D2: «prοmο-official» — двойник в псевдо-официальном имени
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: `gοogle.com` — имитация имени бренда (PE_001)
  E2: `@micrοsοft_help` — имитация официального аккаунта (PE_002)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у буквы нет дремлющих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: `gοogle.com` с греческой ο — это домен Google
  EXPECTED: FAIL_BRAND_NAME_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: строка с греческой ο машинно равна латинскому написанию
  EXPECTED: FAIL_CODEPOINT_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: любая греческая ο в тексте — атака
  EXPECTED: FAIL_OVERBLOCK_MIMICRY (обратная ошибка: настоящий греческий — не спуф)
  RESULT: FAIL
MUTATION_04:
  CLAIM: ASCII-фильтр по «promo» поймает «prοmo»
  EXPECTED: FAIL_ASCII_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: хэндл `@rοot` — тот же аккаунт, что `@root`
  EXPECTED: FAIL_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: замена o→ο в идентификаторе безобидна
  EXPECTED: FAIL_IDENTIFIER_INTERCHANGE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как отличать легит односкриптовый греческий текст от спуфа без ложных срабатываний?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (правило «смешение письменностей в одном токене» — уровень интегратора; см. прототип Vakhter confusable_cards.py)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует формулу LOOKS_SAME ≠ IS_SAME и правило «спуф = смешение, не присутствие».
ALL_OPEN_QUESTIONS_CLOSED: NO (делегирован, не блокирует)

============================================================
11. PATCH_HISTORY
============================================================
PATCH_HISTORY:
  v0_1_PATCH_01: первичное создание (Ruslan Malyavsky, 2026-07-21) — черновик по шаблону GEN3_v0_3 (Vakhter), знак-гомоглиф; не прогонялся через конвейер.
PATCHES_APPLIED: 1
PATCHES_VERIFIED: 0/1

============================================================
12. LIMITATION_STATEMENT
============================================================
LIMITATION_STATEMENT:
  THIS_CARD IS A WORKING_DRAFT ARTIFACT (до ARTIFACT_CONFIRMED)
  NOT A FINAL_STANDARD
  NOT A PARSER
  NOT A RUNTIME
  NOT A SECURITY_CERTIFICATE
  NOT_CONVEYOR_RUN (черновик для нашей работы; конвейер — отдельный проект)
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
