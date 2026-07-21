ЧАСТНЫЙ АВТОРСКИЙ ПРОЕКТ / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_TILDE_U007E_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
DRAFT_NOTE: черновик для нашей работы (Vakhter). Русская версия авторитетна; EN — зеркало.

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
CARD_UID: SIGN_CORE_CARD_TILDE_U007E_GEN3_v0_3_RU
CODEPOINT: U+007E
VISIBLE_FORM: ~
UNICODE_NAME: TILDE
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: тильда
CATEGORY_ROADMAP: PH (пути домашних директорий, tilde-expansion) · PHAGO: — (маскировка структуры)

============================================================
3. REQUIRED_GENERAL_GUARDS
============================================================
REQUIRED_GENERAL_GUARDS:
  - SIGN_FALSE_EFFECT_MIMICRY_GUARD_v0_2A_RU
    GUARD_COMPATIBILITY: применим без изменений — знак не создаёт effect-полей
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
VISIBLE_FORM: ~
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_MARKER
BASE_MODE_FORMULA: TILDE_FORM ≠ EFFECT
SIGN_CATEGORY:
  - маркер домашней директории (~/, ~user) в shell/URL
  - знак «приблизительно» (~5 минут)
  - побитовое НЕ в языках программирования (~x)
  - маркер резервной/временной копии (file~)
  - тильда-раскрытие в оболочке (tilde expansion)

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_HOME_PATH_SAFE — «~/…» не гарантирует безопасный путь (возможен обход)
  2. NOT_USER_ENUM_SAFE — «~user» может раскрывать существование пользователей
  3. NOT_APPROX_PROOF — «~5» не подтверждает корректность приблизительного значения
  4. NOT_BACKUP_HIDDEN — «file~» (бэкап редактора) может раскрывать исходник
  5. NOT_AUTHORITY — «~» не подтверждает официальность
  6. NOT_EXECUTION_TRIGGER — сам по себе ничего не исполняет
  7. NOT_TRUST_SIGNAL — не повышает доверие
  8. NOT_EXPANSION_SAFE — «~» в shell раскрывается в путь (не литерал)
  9. NOT_PATH_END — «~» не отмечает конец пути
  10. NOT_BITWISE_SAFE — «~x» меняет значение (побитовое НЕ)
  11. NOT_TILDE_LITERAL — «~» не всегда литеральный символ (оболочка раскрывает)

BASE_FORMULAS:
  TILDE_FORM ≠ EFFECT
  TILDE_FORM ≠ HOME_PATH_SAFETY_PROOF
  TILDE_FORM ≠ USER_ENUMERATION_SAFETY_PROOF
  TILDE_FORM ≠ APPROX_VALIDITY_PROOF
  TILDE_FORM ≠ BACKUP_CONCEALMENT_PROOF
  TILDE_FORM ≠ AUTHORITY
  TILDE_FORM ≠ TRUST_SIGNAL
  TILDE_FORM ≠ EXPANSION_SAFETY_PROOF
  TILDE_FORM ≠ PATH_END_PROOF
  TILDE_FORM ≠ BITWISE_SAFETY_PROOF
  TILDE_FORM ≠ TILDE_LITERAL_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: «~» (ZONE_1) имеет параллельные функции (дом. директория, приблизительно, побитовое НЕ, бэкап-маркер), сосуществующие без культурной прецессии. Полисемия стабильного знака.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1
  NOTE: письменный/диакритический знак без жестового предшественника; функции пути/expansion наложены цифровой эпохой параллельно.

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
    INPUT: "примерно ~5 минут"
    CONTEXT: знак «приблизительно»
    EXPECTED: INFO
    RISK: NONE
    GUARD: TILDE_FORM ≠ APPROX_VALIDITY_PROOF
  SAFE_CASE_002:
    INPUT: "cd ~/documents"
    CONTEXT: домашняя директория пользователя
    EXPECTED: INFO
    RISK: NONE
    GUARD: TILDE_FORM ≠ HOME_PATH_SAFETY_PROOF
  SAFE_CASE_003:
    INPUT: "mask = ~x"
    CONTEXT: побитовое НЕ
    EXPECTED: INFO
    RISK: NONE
    GUARD: TILDE_FORM ≠ BITWISE_SAFETY_PROOF
  SAFE_CASE_004:
    INPUT: "диапазон 3 ~ 4"
    CONTEXT: приблизительный диапазон (стилистически)
    EXPECTED: INFO
    RISK: NONE
    GUARD: TILDE_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "волнистое тире ~ в тексте"
    CONTEXT: типографический знак
    EXPECTED: INFO
    RISK: NONE
    GUARD: TILDE_FORM ≠ EFFECT
  SAFE_CASE_006:
    INPUT: "config.txt~ (бэкап редактора)"
    CONTEXT: локальный временный файл (в доверенной среде)
    EXPECTED: INFO
    RISK: NONE
    GUARD: TILDE_FORM ≠ BACKUP_CONCEALMENT_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: HOME_PATH_TRAVERSAL
    INPUT: "~/../../etc/passwd"
    CONTEXT: раскрытие «~» в домашний путь + обход вверх
    RISK: HIGH
    ATTACK: «~» раскрывается в домашнюю директорию, «../../» выводит за её пределы
    GUARD: TILDE_FORM ≠ HOME_PATH_SAFETY_PROOF
  RISK_CASE_002:
    NAME: USER_ENUMERATION
    INPUT: "https://site.com/~admin/"
    CONTEXT: mod_userdir раскрывает наличие пользователя
    RISK: MEDIUM
    ATTACK: разница ответов для «~admin» vs «~nouser» перечисляет пользователей
    GUARD: TILDE_FORM ≠ USER_ENUMERATION_SAFETY_PROOF
  RISK_CASE_003:
    NAME: BACKUP_SOURCE_DISCLOSURE
    INPUT: "https://site.com/config.php~"
    CONTEXT: бэкап-файл редактора отдаётся как текст
    RISK: HIGH
    ATTACK: «config.php~» не исполняется как PHP → сервер отдаёт ИСХОДНИК (утечка секретов)
    GUARD: TILDE_FORM ≠ BACKUP_CONCEALMENT_PROOF
  RISK_CASE_004:
    NAME: UNSAFE_TILDE_EXPANSION
    INPUT: "rm ~/*"
    CONTEXT: раскрытие «~» в оболочке при небезопасной подстановке
    RISK: HIGH
    ATTACK: «~» раскрывается в домашний путь; неожиданное удаление содержимого
    GUARD: TILDE_FORM ≠ EXPANSION_SAFETY_PROOF
  RISK_CASE_005:
    NAME: ROOT_HOME_ACCESS
    INPUT: "/~root/.ssh/"
    CONTEXT: попытка доступа к домашней директории root
    RISK: HIGH
    ATTACK: «~root» указывает на приватную директорию; попытка чтения ключей
    GUARD: TILDE_FORM ≠ HOME_PATH_SAFETY_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_TILDE_BYPASS
    INPUT: "～/etc" (полноширинная ～ U+FF5E)
    CONTEXT: двойник-тильда для обхода фильтра пути
    RISK: LOW
    ATTACK: фильтр ищет ASCII «~», нормализатор может привести ～ к «~»
    GUARD: TILDE_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ～
    CODEPOINT: U+FF5E
    NAME: FULLWIDTH TILDE
    RISK: MEDIUM
    RULE: FULLWIDTH_TILDE ≠ TILDE (обход фильтра, ищущего ASCII «~»)
  CONFUSABLE_002:
    VISIBLE_FORM: ∼
    CODEPOINT: U+223C
    NAME: TILDE OPERATOR
    RISK: LOW
    RULE: TILDE_OPERATOR ≠ TILDE (математический оператор)
  CONFUSABLE_003:
    VISIBLE_FORM: ⁓
    CODEPOINT: U+2053
    NAME: SWUNG DASH
    RISK: LOW
    RULE: SWUNG_DASH ≠ TILDE
  CONFUSABLE_004:
    VISIBLE_FORM: ˜
    CODEPOINT: U+02DC
    NAME: SMALL TILDE
    RISK: LOW
    RULE: SMALL_TILDE ≠ TILDE
  CONFUSABLE_005:
    VISIBLE_FORM: 〜
    CODEPOINT: U+301C
    NAME: WAVE DASH
    RISK: LOW
    RULE: WAVE_DASH ≠ TILDE

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: «„~/…“ всегда остаётся внутри домашней директории»
    RESPONSE: TILDE_FORM ≠ HOME_PATH_SAFETY_PROOF
    RULE: «../» после «~» выводит за пределы дома; нормализовать путь после раскрытия
  CG2:
    TRIGGER: «„~admin“ — безобидная ссылка»
    RESPONSE: TILDE_FORM ≠ USER_ENUMERATION_SAFETY_PROOF
    RULE: разные ответы для существующих/несуществующих «~user» перечисляют аккаунты
  CG3:
    TRIGGER: «„file~“ — просто имя, сервер его не отдаст»
    RESPONSE: TILDE_FORM ≠ BACKUP_CONCEALMENT_PROOF
    RULE: бэкап «*.php~» может отдаваться как текст → раскрытие исходника
  CG4:
    TRIGGER: «„~“ в команде — литеральный символ»
    RESPONSE: TILDE_FORM ≠ TILDE_LITERAL_PROOF
    RULE: оболочка раскрывает «~» в домашний путь; экранировать при литеральном смысле
  CG5:
    TRIGGER: «„~“ отмечает конец пути»
    RESPONSE: TILDE_FORM ≠ PATH_END_PROOF
    RULE: «~» это префикс/маркер, не конец пути
  CG6:
    TRIGGER: «фильтр по ASCII „~“ ловит все тильды»
    RESPONSE: TILDE_FORM ≠ EFFECT
    RULE: полноширинная ～ (U+FF5E) — другой кодпоинт

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "~/.."
      NAME: HOME_TRAVERSAL
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: раскрытие дома + обход вверх (доступ за пределы)
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "~user"
      NAME: USERDIR
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: mod_userdir / перечисление пользователей
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "*~"
      NAME: BACKUP_SUFFIX
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: бэкап-файл редактора → раскрытие исходника
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — последовательности с «~» ключевы для путей/файлов.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: «~» маскирует СТРУКТУРУ путей/файлов (домашняя директория, бэкап, expansion), но не имитирует существование проверенной сущности (бренда/аккаунта). Риски — обход пути/раскрытие, не entity-mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена ASCII «~» на полноширинную ～ (U+FF5E) для обхода фильтра пути
  A2: смешение «~» с ∼ (U+223C) в фильтре
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: «~/../../etc/passwd» — обход через раскрытие дома
  B2: «rm ~/*» — небезопасное tilde-expansion в оболочке
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: «~/..» (SC1) — обход за пределы дома
  C2: «*.php~» (SC3) — раскрытие исходника через бэкап
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: «/~admin/» — перечисление пользователей (mod_userdir)
  D2: «~5% гарантия» — псевдо-точность знаком «приблизительно»
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не носитель PHAGO; вектор: доступ к «~root/.ssh»
  E2: N/A — вектор: раскрытие бэкапа с секретами (config~)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет дремлющих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: «~/…» всегда остаётся внутри домашней директории
  EXPECTED: FAIL_HOME_PATH_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: «~admin» — безобидная ссылка без раскрытия пользователей
  EXPECTED: FAIL_USER_ENUMERATION_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: «file~» сервер никогда не отдаст как текст
  EXPECTED: FAIL_BACKUP_DISCLOSURE_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: «~» в команде — литеральный символ
  EXPECTED: FAIL_TILDE_EXPANSION_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: «~» отмечает конец пути
  EXPECTED: FAIL_PATH_END_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: ASCII-фильтр по «~» ловит все варианты знака
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как безопасно раскрывать «~»/«~user» и нормализовать путь без обхода?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (нормализация пути ПОСЛЕ раскрытия + запрет «~user» вне allowlist — уровень интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «раскрытие „~“ + „../“ может выйти за пределы дома».
ALL_OPEN_QUESTIONS_CLOSED: NO (делегирован, не блокирует)

============================================================
11. PATCH_HISTORY
============================================================
PATCH_HISTORY:
  v0_1_PATCH_01: первичное создание (Ruslan Malyavsky, 2026-07-21) — черновик по шаблону GEN3_v0_3 (Vakhter); не прогонялся через конвейер.
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
