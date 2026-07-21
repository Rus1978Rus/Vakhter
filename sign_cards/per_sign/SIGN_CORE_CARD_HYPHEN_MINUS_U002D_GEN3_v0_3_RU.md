ЧАСТНЫЙ АВТОРСКИЙ ПРОЕКТ / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_HYPHEN_MINUS_U002D_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
DRAFT_NOTE: черновик для нашей работы (Vakhter). Прогону через конвейер — в отдельном проекте. Русская версия авторитетна; EN — зеркало.

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
CARD_UID: SIGN_CORE_CARD_HYPHEN_MINUS_U002D_GEN3_v0_3_RU
CODEPOINT: U+002D
VISIBLE_FORM: -
UNICODE_NAME: HYPHEN-MINUS
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: дефис-минус
CATEGORY_ROADMAP: PH (phishing) · PHAGO: ● (сильный носитель — фейковый составной бренд)

============================================================
3. REQUIRED_GENERAL_GUARDS
============================================================
REQUIRED_GENERAL_GUARDS:
  - SIGN_FALSE_EFFECT_MIMICRY_GUARD_v0_2A_RU
    GUARD_COMPATIBILITY: применим без изменений — дефис не создаёт effect-полей, гард работает в REJECT-режиме
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
VISIBLE_FORM: -
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_CONNECTOR_SEPARATOR
BASE_MODE_FORMULA: HYPHEN_FORM ≠ EFFECT
SIGN_CATEGORY:
  - пунктуация
  - соединитель составных слов
  - перенос (hyphenation)
  - разделитель диапазона (1-10)
  - знак минус / вычитание (locale/контекст)
  - разделитель компонентов домена/идентификатора
  - флаг/опция командной строки (-r, --force)

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_BRAND_AFFILIATION — дефис не делает домен частью бренда (paypal-secure.com ≠ PayPal)
  2. NOT_COMPOUND_ENTITY_PROOF — составное слово через дефис не подтверждает реальность сущности
  3. NOT_AUTHORITY — дефис не подтверждает официальный статус текста
  4. NOT_VERIFICATION — дефис не верифицирует соседний факт
  5. NOT_MINUS_SIGN_PROOF — дефис не всегда математический минус
  6. NOT_RANGE_VALIDITY_PROOF — «1-10» не гарантирует корректность диапазона
  7. NOT_WORD_BOUNDARY_GUARANTEE — дефис не всегда граница слова
  8. NOT_SUBDOMAIN — дефис не создаёт поддомен и не меняет регистрируемый домен
  9. NOT_HYPHENATION_CORRECTNESS — перенос не значит корректное/существующее слово
  10. NOT_CLI_FLAG_SAFETY_PROOF — дефис-флаг (-rf) не безопасен сам по себе
  11. NOT_EXECUTION_TRIGGER — дефис сам по себе не запускает действие
  12. NOT_TRUST_SIGNAL — обилие дефисов не повышает доверие к контенту

BASE_FORMULAS:
  HYPHEN_FORM ≠ EFFECT
  HYPHEN_FORM ≠ BRAND_AFFILIATION
  HYPHEN_FORM ≠ COMPOUND_ENTITY_PROOF
  HYPHEN_FORM ≠ AUTHORITY
  HYPHEN_FORM ≠ MINUS_SIGN_PROOF
  HYPHEN_FORM ≠ RANGE_VALIDITY_PROOF
  HYPHEN_FORM ≠ WORD_BOUNDARY_PROOF
  HYPHEN_FORM ≠ SUBDOMAIN_PROOF
  HYPHEN_FORM ≠ TRUST_SIGNAL
  HYPHEN_FORM ≠ CLI_FLAG_SAFETY_PROOF
  HYPHEN_FORM ≠ HYPHENATION_CORRECTNESS_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: дефис-минус (ZONE_1) имеет несколько параллельных функций (соединитель, перенос, диапазон, минус, разделитель домена, CLI-флаг), сосуществующих в современном употреблении без культурной прецессии одной функции другой. Это полисемия одного стабильного знака, не смена эпох — поэтому SEMANTIC_EPOCH_TRACKER не применяется.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1 (физический жест)
  NOTE: дефис как письменный знак не имеет физического жестового предшественника — возник как письменная конвенция пунктуации/переноса.

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
    INPUT: "well-known problem"
    CONTEXT: соединитель составного прилагательного
    EXPECTED: INFO
    RISK: NONE
    GUARD: HYPHEN_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "2026-07-21"
    CONTEXT: разделитель компонентов даты ISO 8601
    EXPECTED: INFO
    RISK: NONE
    GUARD: HYPHEN_FORM ≠ RANGE_VALIDITY_PROOF
  SAFE_CASE_003:
    INPUT: "страницы 10-25"
    CONTEXT: разделитель диапазона
    EXPECTED: INFO
    RISK: NONE
    GUARD: HYPHEN_FORM ≠ RANGE_VALIDITY_PROOF
  SAFE_CASE_004:
    INPUT: "e-mail и co-founder"
    CONTEXT: устоявшиеся дефисные слова
    EXPECTED: INFO
    RISK: NONE
    GUARD: HYPHEN_FORM ≠ HYPHENATION_CORRECTNESS_PROOF
  SAFE_CASE_005:
    INPUT: "up-to-date report"
    CONTEXT: многодефисное составное определение
    EXPECTED: INFO
    RISK: NONE
    GUARD: HYPHEN_FORM ≠ EFFECT
  SAFE_CASE_006:
    INPUT: "temperature -5 degrees"
    CONTEXT: знак минус в числовом контексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: HYPHEN_FORM ≠ MINUS_SIGN_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: TYPOSQUAT_COMPOUND_BRAND
    INPUT: "paypal-secure.com"
    CONTEXT: фишинговый домен, где дефис создаёт иллюзию официального «безопасного» поддомена бренда
    RISK: HIGH
    ATTACK: составной домен `бренд-слово.tld` регистрируется атакующим; дефис внушает аффилиацию с брендом, которой нет — регистрируемый домен это `paypal-secure.com`, а не PayPal
    GUARD: HYPHEN_FORM ≠ BRAND_AFFILIATION
  RISK_CASE_002:
    NAME: FAKE_AFFILIATED_ENTITY
    INPUT: "account-verify-now.ru"
    CONTEXT: цепочка дефисных слов имитирует официальный сервисный поддомен
    RISK: HIGH
    ATTACK: дефисы собирают «служебное» имя, внушающее принадлежность к легит-сервису
    GUARD: HYPHEN_FORM ≠ COMPOUND_ENTITY_PROOF
  RISK_CASE_003:
    NAME: HOMOGLYPH_DASH_IN_DOMAIN
    INPUT: "pay–pal.com" (EN DASH U+2013 вместо дефиса)
    CONTEXT: двойник-тире в домене, визуально как дефис
    RISK: MEDIUM
    ATTACK: не-ASCII тире рисуется как дефис, но это другой кодпоинт — обход сравнения/allowlist
    GUARD: HYPHEN_FORM ≠ EFFECT (см. CONFUSABLES)
  RISK_CASE_004:
    NAME: CLI_OPTION_INJECTION
    INPUT: "filename: --force"
    CONTEXT: пользовательский ввод, начинающийся с дефиса, попадает как флаг команды
    RISK: MEDIUM
    ATTACK: значение, начинающееся с `-`/`--`, интерпретируется как опция (argument injection), меняя поведение утилиты
    GUARD: HYPHEN_FORM ≠ CLI_FLAG_SAFETY_PROOF
  RISK_CASE_005:
    NAME: RANGE_OBFUSCATION
    INPUT: "лимит 1-000 000" (дефис вместо разделителя разрядов)
    CONTEXT: нестандартная позиция дефиса в числе для обмана простого парсера
    RISK: LOW
    ATTACK: дефис в числе путает валидатор, доверяющий формату
    GUARD: HYPHEN_FORM ≠ RANGE_VALIDITY_PROOF
  RISK_CASE_006:
    NAME: FLAG_TRUST_INFLATION
    INPUT: "verified-secure-official-portal.com"
    CONTEXT: нагромождение «доверительных» слов через дефис для инфляции доверия
    RISK: MEDIUM
    ATTACK: цепочка слов через дефис имитирует официальность, хотя дефис ничего не подтверждает
    GUARD: HYPHEN_FORM ≠ TRUST_SIGNAL

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ‐
    CODEPOINT: U+2010
    NAME: HYPHEN
    RISK: HIGH
    RULE: HYPHEN(U+2010) ≠ HYPHEN-MINUS(U+002D) (типографический двойник, почти неотличим)
  CONFUSABLE_002:
    VISIBLE_FORM: –
    CODEPOINT: U+2013
    NAME: EN DASH
    RISK: MEDIUM
    RULE: EN_DASH ≠ HYPHEN-MINUS (шире, но в домене маскирует дефис)
  CONFUSABLE_003:
    VISIBLE_FORM: −
    CODEPOINT: U+2212
    NAME: MINUS SIGN
    RISK: MEDIUM
    RULE: MINUS_SIGN ≠ HYPHEN-MINUS (математический минус, другой кодпоинт)
  CONFUSABLE_004:
    VISIBLE_FORM: ‑
    CODEPOINT: U+2011
    NAME: NON-BREAKING HYPHEN
    RISK: MEDIUM
    RULE: NON_BREAKING_HYPHEN ≠ HYPHEN-MINUS (неразрывный, обход split-по-дефису)
  CONFUSABLE_005:
    VISIBLE_FORM: －
    CODEPOINT: U+FF0D
    NAME: FULLWIDTH HYPHEN-MINUS
    RISK: MEDIUM
    RULE: FULLWIDTH_HYPHEN_MINUS ≠ HYPHEN-MINUS (полноширинная форма)
  CONFUSABLE_006:
    VISIBLE_FORM: ˗
    CODEPOINT: U+02D7
    NAME: MODIFIER LETTER MINUS SIGN
    RISK: LOW
    RULE: MODIFIER_MINUS ≠ HYPHEN-MINUS

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: «домен `бренд-secure.com` — официальный поддомен бренда»
    RESPONSE: HYPHEN_FORM ≠ BRAND_AFFILIATION
    RULE: дефис соединяет строки, но не создаёт принадлежности к бренду; регистрируемый домен решает DNS, не текстовый паттерн
  CG2:
    TRIGGER: «составное имя через дефис подтверждает реальную организацию»
    RESPONSE: HYPHEN_FORM ≠ COMPOUND_ENTITY_PROOF
    RULE: составление слов через дефис — орфография, не верификация сущности
  CG3:
    TRIGGER: «дефис в числе всегда безопасный разделитель диапазона»
    RESPONSE: HYPHEN_FORM ≠ RANGE_VALIDITY_PROOF
    RULE: позиция дефиса в числе может обманывать валидатор
  CG4:
    TRIGGER: «ввод с дефиса не может стать опцией команды»
    RESPONSE: HYPHEN_FORM ≠ CLI_FLAG_SAFETY_PROOF
    RULE: значение, начинающееся с `-`/`--`, может быть распознано как флаг (argument injection)
  CG5:
    TRIGGER: «тире и дефис в домене — один и тот же знак»
    RESPONSE: HYPHEN_FORM ≠ EFFECT
    RULE: EN/EM DASH, MINUS SIGN — другие кодпоинты; визуальное сходство ≠ тот же знак
  CG6:
    TRIGGER: «много „доверительных“ слов через дефис = надёжный сайт»
    RESPONSE: HYPHEN_FORM ≠ TRUST_SIGNAL
    RULE: число дефисных компонентов не коррелирует с надёжностью

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "--"
      NAME: DOUBLE_HYPHEN (end-of-options / long-flag prefix)
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: конец опций в POSIX (`--`), префикс длинного флага (`--force`), argument injection
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "---"
      NAME: TRIPLE_HYPHEN (YAML doc / MD hr)
      RISK_LEVEL: LOW
      POSSIBLE_CONTEXTS: разделитель документов YAML, горизонтальная линия Markdown
      REQUIRES_SEQUENCE_INTEGRATOR: NO
    SC3:
      SEQUENCE: "brand-word-word.tld"
      NAME: HYPHEN_CHAIN_BRAND
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: typosquatting-цепочка, имитирующая аффилированную сущность
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — последовательности выше реальны и значимы.

PHAGO_ENTITY_MIMICRY:
  PE_001:
    INPUT: "paypal-secure.com"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: HIGH
    NOTE: дефис собирает составной домен, внушающий существование аффилированной с брендом сущности («официальный secure-портал PayPal»), которой нет. Это прямая имитация принадлежности проверенному бренду — почему знак помечен PHAGO ● в реестре.
  PE_002:
    INPUT: "microsoft-support-team.ru"
    TYPE: PHAGO_ENTITY_MIMICRY
    RISK: HIGH
    NOTE: цепочка через дефис имитирует официальную сервисную/командную сущность бренда.

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена U+002D на CONFUSABLE_001 (HYPHEN U+2010) в домене
  A2: замена U+002D на CONFUSABLE_002 (EN DASH U+2013) в составном бренде
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: ввод, начинающийся с `--`, попадающий как CLI-опция (argument injection)
  B2: дефис, вставленный в число для обмана валидатора диапазона/разрядов
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: `--` как разделитель конца опций в необёрнутом вводе
  C2: цепочка `brand-word-word.tld` (SC3), маскирующая регистрируемый домен
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: нагромождение «verified-secure-official» через дефис для инфляции доверия
  D2: дефисное «служебное» имя (`account-verify-now`), имитирующее сервис
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: `paypal-secure.com` — имитация аффилированной с брендом сущности (PE_001)
  E2: `microsoft-support-team.ru` — имитация официальной команды/сервиса (PE_002)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у дефиса нет дремлющих/активных эпох (см. раздел 5) — категория F тестирует реактивацию устаревшей эпохи, что неприменимо к знаку без эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: домен `бренд-secure.com` — официальный поддомен бренда
  EXPECTED: FAIL_BRAND_AFFILIATION_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: составное имя через дефис подтверждает реальность организации
  EXPECTED: FAIL_ENTITY_EXISTENCE_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: ввод, начинающийся с дефиса, никогда не станет флагом команды
  EXPECTED: FAIL_CLI_FLAG_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: тире и дефис в домене — один и тот же знак
  EXPECTED: FAIL_CONFUSABLE_IDENTITY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: дефис в числе всегда безопасный разделитель диапазона
  EXPECTED: FAIL_RANGE_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: обилие дефисных «доверительных» слов повышает надёжность сайта
  EXPECTED: FAIL_TRUST_INFLATION_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: нужен ли реестр регистрируемых доменов/брендов, чтобы отличать `paypal-secure.com` (typosquat) от легит `spring-boot.io`?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (бренд-корпус — уровень интегратора/рантайма, не карточки)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка даёт формулу и гарды; корпус брендов подключается интегратором.
ALL_OPEN_QUESTIONS_CLOSED: NO (OQ1 делегирован, не блокирует)

============================================================
11. PATCH_HISTORY
============================================================
PATCH_HISTORY:
  v0_1_PATCH_01: первичное создание (Ruslan Malyavsky, 2026-07-21) — черновик по шаблону GEN3_v0_3 для нашей работы (Vakhter), не прогонялся через конвейер.
PATCHES_APPLIED: 1
PATCHES_VERIFIED: 0/1

============================================================
12. LIMITATION_STATEMENT
============================================================
LIMITATION_STATEMENT:
  THIS_CARD IS A WORKING_DRAFT ARTIFACT (до присвоения ARTIFACT_CONFIRMED)
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
