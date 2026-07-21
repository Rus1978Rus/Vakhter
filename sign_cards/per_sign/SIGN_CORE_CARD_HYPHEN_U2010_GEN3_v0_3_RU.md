ЧАСТНЫЙ АВТОРСКИЙ ПРОЕКТ / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_HYPHEN_U2010_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
DRAFT_NOTE: черновик для нашей работы (Vakhter). Русская версия авторитетна; EN — зеркало. Знак-гомоглиф ASCII-дефиса: ядро — LOOKS_SAME ≠ IS_SAME.

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
CARD_UID: SIGN_CORE_CARD_HYPHEN_U2010_GEN3_v0_3_RU
CODEPOINT: U+2010
VISIBLE_FORM: ‐
UNICODE_NAME: HYPHEN
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: типографский дефис (гомоглиф ASCII-дефиса)
CATEGORY_ROADMAP: PH (путаница Unicode-дефиса и ASCII-дефиса) · PHAGO: ○ (частичный — усиливает составной бренд-спуф)

============================================================
3. REQUIRED_GENERAL_GUARDS
============================================================
REQUIRED_GENERAL_GUARDS:
  - SIGN_FALSE_EFFECT_MIMICRY_GUARD_v0_2A_RU
    GUARD_COMPATIBILITY: применим — знак не создаёт effect-полей; для гомоглифа гард дополняется нормализацией к ASCII на уровне интегратора
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
VISIBLE_FORM: ‐
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_CONNECTOR_HOMOGLYPH
BASE_MODE_FORMULA: HYPHEN_2010_FORM ≠ ASCII_HYPHEN
SIGN_CATEGORY:
  - типографский дефис (правильный знак переноса/соединения в типографике)
  - гомоглиф ASCII-дефиса «-» (U+002D)
  - потенциальный носитель homoglyph-спуфинга в доменах/идентификаторах

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_ASCII_HYPHEN — ‐ (U+2010) это НЕ ASCII-дефис «-» (U+002D); другой кодпоинт
  2. NOT_SAME_STRING_AS_ASCII — строка с ‐ машинно не равна ASCII-написанию
  3. NOT_BRAND_AFFILIATION — «pay‐pal» не делает строку частью бренда
  4. NOT_DOMAIN_VALIDITY_PROOF — визуальное совпадение домена не подтверждает регистрируемый домен
  5. NOT_AUTHORITY — знак не подтверждает официальный статус
  6. NOT_VERIFICATION — не верифицирует соседний факт
  7. NOT_ASCII — вне ASCII; фильтры «только ASCII» не увидят её как «-»
  8. NOT_AUTOMATICALLY_SPOOF — в типографике это норма, не атака
  9. NOT_EXECUTION_TRIGGER — сам по себе ничего не запускает
  10. NOT_TRUST_SIGNAL — не повышает доверие
  11. NOT_INTERCHANGEABLE_IN_IDENTIFIERS — в домене/логине замена «-»→‐ меняет сущность

BASE_FORMULAS:
  HYPHEN_2010_FORM ≠ ASCII_HYPHEN
  HYPHEN_2010_FORM ≠ SAME_CODEPOINT_AS_ASCII
  HYPHEN_2010_FORM ≠ BRAND_AFFILIATION
  HYPHEN_2010_FORM ≠ DOMAIN_VALIDITY_PROOF
  HYPHEN_2010_FORM ≠ AUTHORITY
  HYPHEN_2010_FORM ≠ VERIFICATION
  HYPHEN_2010_FORM ≠ ASCII_CHARACTER
  HYPHEN_2010_FORM ≠ AUTOMATICALLY_SPOOF
  HYPHEN_2010_FORM ≠ TRUST_SIGNAL
  HYPHEN_2010_FORM ≠ EFFECT
  HYPHEN_2010_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: ‐ (типографский дефис) — стабильный знак пунктуации. «Гомоглиф» это свойство визуального совпадения с ASCII-дефисом, существующее одновременно с типографической функцией. Опасность контекстна (подмена в токене/домене), не эпохальна.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1
  NOTE: письменный/типографический знак без жестового предшественника; отделён Unicode от ASCII-дефиса как «истинный» дефис.

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
    INPUT: "well‐known (типографский набор)"
    CONTEXT: типографский дефис в отвёрстанном тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: HYPHEN_2010_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_002:
    INPUT: "поле‐ягода (перенос в книге)"
    CONTEXT: типографский перенос/соединение
    EXPECTED: INFO
    RISK: NONE
    GUARD: HYPHEN_2010_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "e‐book (издательская типографика)"
    CONTEXT: дефисное слово в вёрстке
    EXPECTED: INFO
    RISK: NONE
    GUARD: HYPHEN_2010_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "co‐operation (британская типографика)"
    CONTEXT: типографский дефис в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: HYPHEN_2010_FORM ≠ AUTOMATICALLY_SPOOF
  SAFE_CASE_005:
    INPUT: "twenty‐one (набор чисел прописью)"
    CONTEXT: дефис в числительном (типографика)
    EXPECTED: INFO
    RISK: NONE
    GUARD: HYPHEN_2010_FORM ≠ EFFECT
  SAFE_CASE_006:
    INPUT: "mother‐in‐law (словарная запись)"
    CONTEXT: составное слово в словаре
    EXPECTED: INFO
    RISK: NONE
    GUARD: HYPHEN_2010_FORM ≠ AUTOMATICALLY_SPOOF

RISK_CASES:
  RISK_CASE_001:
    NAME: DOMAIN_HYPHEN_SPOOF
    INPUT: "pay‐pal.com" (U+2010 вместо ASCII-дефиса)
    CONTEXT: IDN/бренд-спуф — токен выглядит как pay-pal.com
    RISK: HIGH
    ATTACK: замена ASCII-дефиса на ‐ даёт визуально идентичный домен, регистрируемый атакующим
    GUARD: HYPHEN_2010_FORM ≠ ASCII_HYPHEN
  RISK_CASE_002:
    NAME: ALLOWLIST_BYPASS
    INPUT: "secure‐bank.example (в allowlist только 'secure-bank')"
    CONTEXT: обход точного сравнения с ASCII-дефисом
    RISK: HIGH
    ATTACK: ‐ ≠ «-», строка не совпадёт с ASCII-записью в allowlist/blocklist
    GUARD: HYPHEN_2010_FORM ≠ SAME_CODEPOINT_AS_ASCII
  RISK_CASE_003:
    NAME: COMPOUND_BRAND_SPOOF
    INPUT: "paypal‐secure.com" (‐ усиливает составной бренд-спуф)
    CONTEXT: составной домен с типографским дефисом
    RISK: MEDIUM
    ATTACK: ‐ имитирует ASCII-дефис в фейковом составном бренде (ср. карточку HYPHEN-MINUS)
    GUARD: HYPHEN_2010_FORM ≠ BRAND_AFFILIATION
  RISK_CASE_004:
    NAME: EMAIL_LOOKALIKE
    INPUT: "info@e‐shop.example"
    CONTEXT: ‐ в домене письма
    RISK: MEDIUM
    ATTACK: домен визуально совпадает с e-shop, но ведёт к атакующему
    GUARD: HYPHEN_2010_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
  RISK_CASE_005:
    NAME: FILTER_BYPASS_KEYWORD
    INPUT: "black‐list (обход blocklist по 'black-list')"
    CONTEXT: обход текстового фильтра по ASCII-дефису
    RISK: MEDIUM
    ATTACK: подмена дефиса уводит фразу из-под фильтра
    GUARD: HYPHEN_2010_FORM ≠ ASCII_CHARACTER
  RISK_CASE_006:
    NAME: MULTI_DASH_MIX
    INPUT: "pay‐pal.com / pay–pal.com" (‐ U+2010 и – U+2013 вместе)
    CONTEXT: смешение разных тире-двойников усложняет детекцию
    RISK: MEDIUM
    ATTACK: несколько не-ASCII тире имитируют один и тот же ASCII-дефис
    GUARD: HYPHEN_2010_FORM ≠ DOMAIN_VALIDITY_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: -
    CODEPOINT: U+002D
    NAME: HYPHEN-MINUS
    RISK: HIGH
    RULE: ASCII_HYPHEN ≠ HYPHEN(U+2010) (главная цель имитации; почти неотличимы)
  CONFUSABLE_002:
    VISIBLE_FORM: ‑
    CODEPOINT: U+2011
    NAME: NON-BREAKING HYPHEN
    RISK: MEDIUM
    RULE: NON_BREAKING_HYPHEN ≠ HYPHEN(U+2010)
  CONFUSABLE_003:
    VISIBLE_FORM: ‒
    CODEPOINT: U+2012
    NAME: FIGURE DASH
    RISK: LOW
    RULE: FIGURE_DASH ≠ HYPHEN(U+2010)
  CONFUSABLE_004:
    VISIBLE_FORM: –
    CODEPOINT: U+2013
    NAME: EN DASH
    RISK: MEDIUM
    RULE: EN_DASH ≠ HYPHEN(U+2010)
  CONFUSABLE_005:
    VISIBLE_FORM: −
    CODEPOINT: U+2212
    NAME: MINUS SIGN
    RISK: MEDIUM
    RULE: MINUS_SIGN ≠ HYPHEN(U+2010)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: «домен `pay‐pal.com` — это pay-pal.com»
    RESPONSE: HYPHEN_2010_FORM ≠ ASCII_HYPHEN
    RULE: ‐ иной кодпоинт; регистрируемый домен решает DNS, не глаз
  CG2:
    TRIGGER: «строка с ‐ совпадёт с ASCII-записью в allowlist»
    RESPONSE: HYPHEN_2010_FORM ≠ SAME_CODEPOINT_AS_ASCII
    RULE: точное сравнение не совпадёт; нормализовать к ASCII перед проверкой
  CG3:
    TRIGGER: «любой ‐ в тексте — атака»
    RESPONSE: HYPHEN_2010_FORM ≠ AUTOMATICALLY_SPOOF
    RULE: в типографике ‐ легитимен; спуф — это подмена в домене/идентификаторе
  CG4:
    TRIGGER: «ASCII-фильтр по „-“ поймает ‐»
    RESPONSE: HYPHEN_2010_FORM ≠ ASCII_CHARACTER
    RULE: ‐ вне ASCII; фильтр по «-» её не сматчит
  CG5:
    TRIGGER: «‐ и „-“ в идентификаторе взаимозаменяемы»
    RESPONSE: HYPHEN_2010_FORM ≠ INTERCHANGEABLE_IN_IDENTIFIERS
    RULE: в домене/логине замена меняет сущность строки
  CG6:
    TRIGGER: «‐ подтверждает принадлежность составного бренда»
    RESPONSE: HYPHEN_2010_FORM ≠ BRAND_AFFILIATION
    RULE: типографский дефис не создаёт аффилиации, как и ASCII-дефис

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "brand‐word.tld"
      NAME: HYPHEN_SPOOF_DOMAIN
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: ‐ имитирует ASCII-дефис в фейковом составном домене
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "‐ + – + −" (смесь тире-двойников)
      NAME: MULTI_DASH_MIX
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: разные не-ASCII тире имитируют один ASCII-дефис
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — опасность знака проявляется в токене/домене, не в изоляции.

PHAGO_ENTITY_MIMICRY:
  PE_001:
    INPUT: "paypal‐secure.com"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: MEDIUM
    NOTE: ‐ имитирует ASCII-дефис в составном домене, внушающем аффилиацию с брендом (как HYPHEN-MINUS, но не-ASCII). Частичный (○) PHAGO — усиливает entity-mimicry дефиса.
  PE_002:
    INPUT: "e‐shop‐official.example"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: MEDIUM
    NOTE: цепочка ‐ собирает «официальное» составное имя, имитирующее сущность.

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: подмена ASCII-дефиса (U+002D) на ‐ (U+2010) в домене бренда
  A2: смешение ‐ с – (U+2013) / − (U+2212) для усложнения детекции
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: ‐ обходит allowlist/blocklist по ASCII-дефису (secure‐bank)
  B2: ‐ в домене письма (info@e‐shop.example)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: фейк-домен `brand‐word.tld` (SC1)
  C2: смесь тире `‐ – −` (SC2)
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: «black‐list» — обход фильтра по фразе
  D2: «verified‐secure» — псевдо-официальное составное имя
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: `paypal‐secure.com` — имитация аффилиации бренда (PE_001)
  E2: `e‐shop‐official.example` — имитация служебной сущности (PE_002)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет дремлющих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: `pay‐pal.com` — это домен pay-pal.com
  EXPECTED: FAIL_ASCII_HYPHEN_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: строка с ‐ совпадёт с ASCII-записью в allowlist
  EXPECTED: FAIL_CODEPOINT_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: любой ‐ в тексте — атака
  EXPECTED: FAIL_OVERBLOCK_MIMICRY (обратная ошибка: типографский дефис — не спуф)
  RESULT: FAIL
MUTATION_04:
  CLAIM: ASCII-фильтр по «-» поймает ‐
  EXPECTED: FAIL_ASCII_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: ‐ и «-» в идентификаторе взаимозаменяемы
  EXPECTED: FAIL_IDENTIFIER_INTERCHANGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: ‐ подтверждает принадлежность составного бренда
  EXPECTED: FAIL_BRAND_AFFILIATION_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: нормализовать все не-ASCII тире к «-» перед сравнением — где грань с легит-типографикой?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (нормализация к ASCII в контексте домена/идентификатора; в прозе ‐ остаётся легит — уровень интегратора)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «‐ ≠ ASCII-дефис; нормализовать в структурном контексте, не в прозе».
ALL_OPEN_QUESTIONS_CLOSED: NO (делегирован, не блокирует)

============================================================
11. PATCH_HISTORY
============================================================
PATCH_HISTORY:
  v0_1_PATCH_01: первичное создание (Ruslan Malyavsky, 2026-07-21) — черновик по шаблону GEN3_v0_3 (Vakhter), знак-гомоглиф ASCII-дефиса; не прогонялся через конвейер.
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
