PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_EXCLAMATION_MARK_U0021_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: Русский оригинал (authoritative). Английское зеркало — SIGN_CORE_CARD_EXCLAMATION_MARK_U0021_GEN3_v0_3_EN. Кодпоинты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_EXCLAMATION_MARK_U0021_GEN3_v0_3_RU
CODEPOINT: U+0021
VISIBLE_FORM: !
UNICODE_NAME: EXCLAMATION MARK
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: восклицательный знак / отрицание и история
CATEGORY_ROADMAP: INJ (history expansion shell, логическое отрицание) · PHAGO: — (инверсия условия)

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
VISIBLE_FORM: !
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: EXCLAMATION_MARK_FORM ≠ EFFECT
SIGN_CATEGORY:
  - логическое NOT / не-равно (!x, a != b)
  - history expansion shell (!!, !$, !cmd)
  - выделение / междометие в тексте
  - специальный маркер в конфигах (например, YAML-теги, ! отрицание в шаблонах)

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_PUNCTUATION_ONLY — "!" не всегда выделение (в shell он раскрывает историю)
  2. NOT_NEGATION_SAFE — отрицание "!" может инвертировать авторизацию/условие
  3. NOT_HISTORY_SAFE — "!!" / "!cmd" повторно исполняет или раскрывается в предыдущие/другие команды
  4. NOT_ESCAPED_PROOF — наличие "!" не значит, что он закавычен/экранирован
  5. NOT_ENCODED_SAFE — "%21" может быть раскодирован обратно в "!" позже
  6. NOT_AUTHORITY — "!" не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сам по себе ничего не исполняет; раскрытие/отрицание делает контекст
  8. NOT_TRUST_SIGNAL — не повышает доверие
  9. NOT_PATTERN_SCOPE_SAFE — "!" в glob/gitignore/ACL-шаблоне инвертирует смысл правила
  10. NOT_SANITIZED_PROOF — наличие "!" не значит, что ввод санитизирован
  11. NOT_OUTPUT_CONTEXT_PROOF — безопасность зависит от контекста разбора/раскрытия

BASE_FORMULAS:
  EXCLAMATION_MARK_FORM ≠ EFFECT
  EXCLAMATION_MARK_FORM ≠ PUNCTUATION_ONLY_PROOF
  EXCLAMATION_MARK_FORM ≠ NEGATION_SAFETY_PROOF
  EXCLAMATION_MARK_FORM ≠ HISTORY_SAFETY_PROOF
  EXCLAMATION_MARK_FORM ≠ ESCAPED_PROOF
  EXCLAMATION_MARK_FORM ≠ ENCODED_SAFETY_PROOF
  EXCLAMATION_MARK_FORM ≠ AUTHORITY
  EXCLAMATION_MARK_FORM ≠ EXECUTION_TRIGGER
  EXCLAMATION_MARK_FORM ≠ PATTERN_SCOPE_PROOF
  EXCLAMATION_MARK_FORM ≠ SANITIZED_PROOF
  EXCLAMATION_MARK_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: "!" (ZONE_1) имеет параллельные функции (выделение, логическое NOT, history shell, отрицание шаблона), сосуществующие без культурной прецессии. Полисемия стабильного знака.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1
  NOTE: знак пунктуации без жестового предшественника; функции отрицания/истории/шаблона надстроены цифровой эпохой параллельно.

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
    INPUT: "Hello world!"
    CONTEXT: выделение в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: EXCLAMATION_MARK_FORM ≠ PUNCTUATION_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: "if (a != b)"
    CONTEXT: сравнение «не равно» в коде
    EXPECTED: INFO
    RISK: NONE
    GUARD: EXCLAMATION_MARK_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "return !flag"
    CONTEXT: логическое NOT в коде (как литеральный текст)
    EXPECTED: INFO
    RISK: NONE
    GUARD: EXCLAMATION_MARK_FORM ≠ NEGATION_SAFETY_PROOF
  SAFE_CASE_004:
    INPUT: "5! = 120"
    CONTEXT: обозначение факториала в математическом тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: EXCLAMATION_MARK_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "Wait!"
    CONTEXT: междометие в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: EXCLAMATION_MARK_FORM ≠ PUNCTUATION_ONLY_PROOF
  SAFE_CASE_006:
    INPUT: "the shebang starts with #!"
    CONTEXT: описание строки shebang в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: EXCLAMATION_MARK_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: SHELL_HISTORY_EXPANSION
    INPUT: "echo hi; !!"
    CONTEXT: "!!" повторно запускает предыдущую команду через history expansion
    RISK: HIGH
    ATTACK: интерактивный shell раскрывает "!!" для повторного выполнения предыдущей (возможно привилегированной) команды
    GUARD: EXCLAMATION_MARK_FORM ≠ HISTORY_SAFETY_PROOF
  RISK_CASE_002:
    NAME: HISTORY_ARG_INJECTION
    INPUT: "rm !$"
    CONTEXT: "!$" раскрывается в последний аргумент предыдущей команды
    RISK: MEDIUM
    ATTACK: "!$" подтягивает предыдущий аргумент (например, чувствительный путь) в новую команду
    GUARD: EXCLAMATION_MARK_FORM ≠ HISTORY_SAFETY_PROOF
  RISK_CASE_003:
    NAME: NEGATION_LOGIC_INVERSION
    INPUT: "allow if !isBlocked (атакующий делает isBlocked undefined)"
    CONTEXT: "!" переворачивает решение об авторизации на нестрогом значении
    RISK: HIGH
    ATTACK: "!undefined" становится true, инвертируя блокировку в разрешение
    GUARD: EXCLAMATION_MARK_FORM ≠ NEGATION_SAFETY_PROOF
  RISK_CASE_004:
    NAME: GITIGNORE_ACL_UNNEGATE
    INPUT: "!secret.key (повторно включить исключённый файл)"
    CONTEXT: "!" снимает игнорирование пути в gitignore/ACL-шаблоне
    RISK: MEDIUM
    ATTACK: "!" обращает исключение, так что секрет снова включается/отгружается
    GUARD: EXCLAMATION_MARK_FORM ≠ PATTERN_SCOPE_PROOF
  RISK_CASE_005:
    NAME: ENCODED_BANG_BYPASS
    INPUT: "cmd%21%21 (с поздним декодированием)"
    CONTEXT: кодированный "!!" декодируется обратно перед shell
    RISK: MEDIUM
    ATTACK: %21%21 декодируется в "!!" ПОСЛЕ проверки → history expansion
    GUARD: EXCLAMATION_MARK_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_BANG_BYPASS
    INPUT: "！！ (полноширинный ！ U+FF01)"
    CONTEXT: похожий знак для обхода фильтра "!"
    RISK: LOW
    ATTACK: фильтр ищет ASCII "!", нормализатор может свернуть ！ в "!"
    GUARD: EXCLAMATION_MARK_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ！
    CODEPOINT: U+FF01
    NAME: FULLWIDTH EXCLAMATION MARK
    RISK: HIGH
    RULE: FULLWIDTH_EXCLAMATION_MARK ≠ EXCLAMATION_MARK (обходит фильтр, ищущий ASCII "!")
  CONFUSABLE_002:
    VISIBLE_FORM: ǃ
    CODEPOINT: U+01C3
    NAME: LATIN LETTER RETROFLEX CLICK
    RISK: HIGH
    RULE: RETROFLEX_CLICK ≠ EXCLAMATION_MARK (буква, идентичная по виду "!")
  CONFUSABLE_003:
    VISIBLE_FORM: ‼
    CODEPOINT: U+203C
    NAME: DOUBLE EXCLAMATION MARK
    RISK: LOW
    RULE: DOUBLE_EXCLAMATION_MARK ≠ EXCLAMATION_MARK (один глиф, похожий на "!!")
  CONFUSABLE_004:
    VISIBLE_FORM: ❗
    CODEPOINT: U+2757
    NAME: HEAVY EXCLAMATION MARK SYMBOL
    RISK: LOW
    RULE: HEAVY_EXCLAMATION_SYMBOL ≠ EXCLAMATION_MARK
  CONFUSABLE_005:
    VISIBLE_FORM: ﹗
    CODEPOINT: U+FE57
    NAME: SMALL EXCLAMATION MARK
    RISK: MEDIUM
    RULE: SMALL_EXCLAMATION_MARK ≠ EXCLAMATION_MARK

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "'!' — это всегда выделение"
    RESPONSE: EXCLAMATION_MARK_FORM ≠ PUNCTUATION_ONLY_PROOF
    RULE: в shell "!" раскрывает историю; в коде он отрицает
  CG2:
    TRIGGER: "отрицание не может быть опасным"
    RESPONSE: EXCLAMATION_MARK_FORM ≠ NEGATION_SAFETY_PROOF
    RULE: "!" может инвертировать авторизацию/условие на нестрогом значении
  CG3:
    TRIGGER: "'!!' — это просто два восклицательных знака"
    RESPONSE: EXCLAMATION_MARK_FORM ≠ HISTORY_SAFETY_PROOF
    RULE: интерактивный shell раскрывает "!!"/"!$" в предыдущие команды/аргументы
  CG4:
    TRIGGER: "'%21' безопасен навсегда"
    RESPONSE: EXCLAMATION_MARK_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в "!" перед shell
  CG5:
    TRIGGER: "фильтр по ASCII '!' ловит все восклицательные знаки"
    RESPONSE: EXCLAMATION_MARK_FORM ≠ EFFECT
    RULE: полноширинный ！ (U+FF01) и retroflex click ǃ (U+01C3) — другие кодпоинты
  CG6:
    TRIGGER: "наличие '!' значит, что ввод санитизирован"
    RESPONSE: EXCLAMATION_MARK_FORM ≠ SANITIZED_PROOF
    RULE: наличие знака ничего не говорит о санитизации

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "!!"
      NAME: HISTORY_REEXEC
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: повторное выполнение предыдущей команды shell
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "!$"
      NAME: HISTORY_LAST_ARG
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: подтягивание последнего аргумента предыдущей команды
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "!pattern"
      NAME: PATTERN_UNNEGATE
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: инверсия правила gitignore/ACL/glob
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — последовательности с "!" центральны для злоупотребления историей/отрицанием.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: "!" раскрывает историю или инвертирует условие/шаблон, но не имитирует существование верифицированной сущности. Его риски — раскрытие/инверсия, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена ASCII "!" на полноширинный ！ (U+FF01) для обхода фильтра
  A2: замена на retroflex click ǃ (U+01C3), букву идентичного вида
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: history expansion shell echo hi; !!
  B2: инверсия логики отрицания allow if !isBlocked
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "!!" (SC1) — повторное исполнение из истории
  C2: "!pattern" (SC3) — снятие отрицания gitignore/ACL
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: "!" подан как безобидное выделение внутри поля команды
  D2: "%21" как «безопасный» кодированный текст с поздним декодированием
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: history expansion в интерактивный shell
  E2: N/A — вектор: инверсия условия в проверке авторизации
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: "!" — всегда выделение
  EXPECTED: FAIL_PUNCTUATION_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: отрицание не может быть опасным
  EXPECTED: FAIL_NEGATION_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: "!!" — это просто два восклицательных знака
  EXPECTED: FAIL_HISTORY_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%21" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: фильтр по ASCII "!" ловит все похожие восклицательные знаки
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: наличие "!" доказывает санитизацию ввода
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как нейтрализовать "!" по контексту (интерактивный shell/отрицание/шаблон) без ложных срабатываний на выделении/факториале/!=?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (отключение history expansion в неинтерактивных контекстах + строгое приведение к boolean + ревью правил-шаблонов — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «безопасность '!' решается контекстом разбора/раскрытия».
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
