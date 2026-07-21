PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_LEFT_CURLY_BRACKET_U007B_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: Русский оригинал (authoritative). Английское зеркало — SIGN_CORE_CARD_LEFT_CURLY_BRACKET_U007B_GEN3_v0_3_EN. Кодпоинты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_LEFT_CURLY_BRACKET_U007B_GEN3_v0_3_RU
CODEPOINT: U+007B
VISIBLE_FORM: {
UNICODE_NAME: LEFT CURLY BRACKET
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: левая фигурная скобка / открытие шаблона и объекта
CATEGORY_ROADMAP: INJ (SSTI-шаблон, объект/brace expansion) · PHAGO: — (подделка открытия структуры)

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
VISIBLE_FORM: {
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: LEFT_CURLY_BRACKET_FORM ≠ EFFECT
SIGN_CATEGORY:
  - открытие блока кода ({ ... })
  - открытие объекта JSON/dict/set ({"k": "v"})
  - открытие выражения шаблона ({{ expr }}, ${...}, {0})
  - открытие brace expansion shell ({a,b})

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_BLOCK_ONLY — "{" не всегда безобидный блок кода/объекта (он открывает выражения шаблона)
  2. NOT_TEMPLATE_SAFE — "{{" / "{%" открывает выражение, которое движок шаблона может вычислить (SSTI/RCE)
  3. NOT_OBJECT_SAFE — открытие объекта может внедрить ключи/операторы (NoSQL/JSON)
  4. NOT_ESCAPED_PROOF — наличие "{" не значит, что она закавычена/экранирована
  5. NOT_ENCODED_SAFE — "%7B" может быть раскодирована обратно в "{" позже
  6. NOT_AUTHORITY — "{" не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сама по себе ничего не исполняет; открытие/вычисление делает контекст
  8. NOT_TRUST_SIGNAL — не повышает доверие
  9. NOT_FORMAT_SAFE — "{0}"/"{name}" может утечь или проиндексировать в форматной строке
  10. NOT_SANITIZED_PROOF — наличие "{" не значит, что ввод санитизирован
  11. NOT_OUTPUT_CONTEXT_PROOF — безопасность зависит от контекста разбора/вычисления

BASE_FORMULAS:
  LEFT_CURLY_BRACKET_FORM ≠ EFFECT
  LEFT_CURLY_BRACKET_FORM ≠ BLOCK_ONLY_PROOF
  LEFT_CURLY_BRACKET_FORM ≠ TEMPLATE_SAFETY_PROOF
  LEFT_CURLY_BRACKET_FORM ≠ OBJECT_SAFETY_PROOF
  LEFT_CURLY_BRACKET_FORM ≠ ESCAPED_PROOF
  LEFT_CURLY_BRACKET_FORM ≠ ENCODED_SAFETY_PROOF
  LEFT_CURLY_BRACKET_FORM ≠ AUTHORITY
  LEFT_CURLY_BRACKET_FORM ≠ EXECUTION_TRIGGER
  LEFT_CURLY_BRACKET_FORM ≠ FORMAT_SAFETY_PROOF
  LEFT_CURLY_BRACKET_FORM ≠ SANITIZED_PROOF
  LEFT_CURLY_BRACKET_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: "{" (ZONE_1) имеет параллельные функции (блок кода, объект, выражение шаблона, brace expansion), сосуществующие без культурной прецессии. Полисемия стабильного знака.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1
  NOTE: пунктуационно-математическая фигурная скобка без жестового предшественника; функции блока/объекта/шаблона надстроены цифровой эпохой параллельно.

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
    INPUT: "the set {1, 2, 3}"
    CONTEXT: математическое множество в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: LEFT_CURLY_BRACKET_FORM ≠ BLOCK_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: 'JSON {"name": "Ann"}'
    CONTEXT: корректный объект JSON, показанный как текст
    EXPECTED: INFO
    RISK: NONE
    GUARD: LEFT_CURLY_BRACKET_FORM ≠ OBJECT_SAFETY_PROOF
  SAFE_CASE_003:
    INPUT: "if (x) { doThing() }"
    CONTEXT: блок кода, показанный как литеральный текст
    EXPECTED: INFO
    RISK: NONE
    GUARD: LEFT_CURLY_BRACKET_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "CSS rule: body { margin: 0 }"
    CONTEXT: блок объявлений CSS
    EXPECTED: INFO
    RISK: NONE
    GUARD: LEFT_CURLY_BRACKET_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "the { key on a keyboard"
    CONTEXT: название клавиши фигурной скобки в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: LEFT_CURLY_BRACKET_FORM ≠ BLOCK_ONLY_PROOF
  SAFE_CASE_006:
    INPUT: "quantifier a{2,3} in a regex"
    CONTEXT: описание квантора регэкспа в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: LEFT_CURLY_BRACKET_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: SSTI_TEMPLATE_INJECTION
    INPUT: "{{7*7}} then {{config.items()}}"
    CONTEXT: "{{" открывает выражение, вычисляемое движком шаблона
    RISK: CRITICAL
    ATTACK: "{{...}}" вычисляется на сервере, утекая конфиг или исполняя код (SSTI/RCE)
    GUARD: LEFT_CURLY_BRACKET_FORM ≠ TEMPLATE_SAFETY_PROOF
  RISK_CASE_002:
    NAME: NOSQL_OBJECT_INJECTION
    INPUT: '{"$gt": ""}'
    CONTEXT: "{" открывает внедрённый объект-оператор NoSQL
    RISK: HIGH
    ATTACK: "{" внедряет оператор "$gt", превращая сопоставление значения во всегда-истинное (обход аутентификации)
    GUARD: LEFT_CURLY_BRACKET_FORM ≠ OBJECT_SAFETY_PROOF
  RISK_CASE_003:
    NAME: FORMAT_STRING_LEAK
    INPUT: "{0.__class__.__mro__} in a format string"
    CONTEXT: "{" открывает форматное поле, обходящее внутренности объекта
    RISK: HIGH
    ATTACK: "{0...}" индексирует объекты, утекая секреты/globals через str.format
    GUARD: LEFT_CURLY_BRACKET_FORM ≠ FORMAT_SAFETY_PROOF
  RISK_CASE_004:
    NAME: SHELL_BRACE_EXPANSION
    INPUT: "cp file {a,../../etc/passwd}"
    CONTEXT: "{" открывает brace expansion shell в лишние цели
    RISK: MEDIUM
    ATTACK: "{a,b}" раскрывает один аргумент в несколько, достигая непреднамеренных путей
    GUARD: LEFT_CURLY_BRACKET_FORM ≠ EFFECT
  RISK_CASE_005:
    NAME: ENCODED_BRACE_BYPASS
    INPUT: "%7B%7B7*7%7D%7D (с поздним декодированием)"
    CONTEXT: кодированный "{{" декодируется обратно перед движком шаблона
    RISK: HIGH
    ATTACK: %7B декодируется в "{" ПОСЛЕ проверки → вычисление шаблона
    GUARD: LEFT_CURLY_BRACKET_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_BRACE_BYPASS
    INPUT: "｛｛7*7｝｝ (полноширинная ｛ U+FF5B)"
    CONTEXT: похожий знак для обхода фильтра "{"
    RISK: MEDIUM
    ATTACK: фильтр ищет ASCII "{", нормализатор может свернуть ｛ в "{"
    GUARD: LEFT_CURLY_BRACKET_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ｛
    CODEPOINT: U+FF5B
    NAME: FULLWIDTH LEFT CURLY BRACKET
    RISK: HIGH
    RULE: FULLWIDTH_LEFT_CURLY_BRACKET ≠ LEFT_CURLY_BRACKET (обходит фильтр, ищущий ASCII "{")
  CONFUSABLE_002:
    VISIBLE_FORM: ﹛
    CODEPOINT: U+FE5B
    NAME: SMALL LEFT CURLY BRACKET
    RISK: MEDIUM
    RULE: SMALL_LEFT_CURLY_BRACKET ≠ LEFT_CURLY_BRACKET
  CONFUSABLE_003:
    VISIBLE_FORM: ❴
    CODEPOINT: U+2774
    NAME: MEDIUM LEFT CURLY BRACKET ORNAMENT
    RISK: LOW
    RULE: MEDIUM_LEFT_CURLY_BRACKET_ORNAMENT ≠ LEFT_CURLY_BRACKET
  CONFUSABLE_004:
    VISIBLE_FORM: ⦃
    CODEPOINT: U+2983
    NAME: LEFT WHITE CURLY BRACKET
    RISK: LOW
    RULE: LEFT_WHITE_CURLY_BRACKET ≠ LEFT_CURLY_BRACKET
  CONFUSABLE_005:
    VISIBLE_FORM: 𝄔
    CODEPOINT: U+1D114
    NAME: MUSICAL SYMBOL BRACE
    RISK: LOW
    RULE: MUSICAL_SYMBOL_BRACE ≠ LEFT_CURLY_BRACKET

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "'{' — это всегда безобидный блок кода/объекта"
    RESPONSE: LEFT_CURLY_BRACKET_FORM ≠ BLOCK_ONLY_PROOF
    RULE: "{{" / "{%" открывает выражение шаблона, которое движок может вычислить
  CG2:
    TRIGGER: "блок шаблона — это инертный текст"
    RESPONSE: LEFT_CURLY_BRACKET_FORM ≠ TEMPLATE_SAFETY_PROOF
    RULE: движок шаблона вычисляет выражение (SSTI/RCE)
  CG3:
    TRIGGER: "объект JSON не может быть опасным"
    RESPONSE: LEFT_CURLY_BRACKET_FORM ≠ OBJECT_SAFETY_PROOF
    RULE: "{" может внедрить оператор NoSQL ($gt/$ne) или подделать ключ
  CG4:
    TRIGGER: "'%7B' безопасен навсегда"
    RESPONSE: LEFT_CURLY_BRACKET_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в "{" перед движком
  CG5:
    TRIGGER: "фильтр по ASCII '{' ловит все фигурные скобки"
    RESPONSE: LEFT_CURLY_BRACKET_FORM ≠ EFFECT
    RULE: полноширинная ｛ (U+FF5B) и малая ﹛ (U+FE5B) — другие кодпоинты
  CG6:
    TRIGGER: "наличие '{' значит, что ввод санитизирован"
    RESPONSE: LEFT_CURLY_BRACKET_FORM ≠ SANITIZED_PROOF
    RULE: наличие знака ничего не говорит о санитизации

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "{{"
      NAME: TEMPLATE_EXPR_OPEN
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: открытие вычисляемого выражения шаблона (SSTI)
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: '{"$'
      NAME: NOSQL_OPERATOR_OPEN
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: открытие внедрённого объекта-оператора NoSQL
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "{%"
      NAME: TEMPLATE_TAG_OPEN
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: открытие управляющего тега шаблона (if/for/include)
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — последовательности с "{" центральны для инъекции шаблона/объекта.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: "{" открывает блок/объект/выражение шаблона, но не имитирует существование верифицированной сущности. Его риски — инъекция шаблона/объекта, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена ASCII "{" на полноширинную ｛ (U+FF5B) для обхода фильтра
  A2: замена на малую ﹛ (U+FE5B)
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: инъекция шаблона SSTI {{7*7}}
  B2: инъекция объекта NoSQL {"$gt": ""}
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "{{" (SC1) — открытие выражения шаблона
  C2: '{"$' (SC2) — открытие оператора NoSQL
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: "{" подан как безобидный блок JSON/кода внутри поля шаблона
  D2: "%7B" как «безопасный» кодированный текст с поздним декодированием
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: выражение шаблона в рендеримую страницу
  E2: N/A — вектор: инъекция объекта-оператора в запрос NoSQL
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: "{" — всегда безобидный блок кода/объекта
  EXPECTED: FAIL_BLOCK_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: блок шаблона — это инертный текст
  EXPECTED: FAIL_TEMPLATE_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: объект JSON не может быть опасным
  EXPECTED: FAIL_OBJECT_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%7B" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: фильтр по ASCII "{" ловит все похожие фигурные скобки
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: наличие "{" доказывает санитизацию ввода
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как экранировать "{" по контексту (шаблон/JSON/shell/формат) без ложных срабатываний на блоках кода/множествах/CSS/квантора регэкспа?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (песочница/logic-less шаблоны + JSON по схеме + безопасные API форматирования + отключение brace expansion — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «безопасность '{' решается контекстом разбора/вычисления».
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
