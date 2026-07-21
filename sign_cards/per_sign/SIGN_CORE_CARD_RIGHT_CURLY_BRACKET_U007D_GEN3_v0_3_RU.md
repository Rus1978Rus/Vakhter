PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_RIGHT_CURLY_BRACKET_U007D_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: Русский оригинал (authoritative). Английское зеркало — SIGN_CORE_CARD_RIGHT_CURLY_BRACKET_U007D_GEN3_v0_3_EN. Кодпоинты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_RIGHT_CURLY_BRACKET_U007D_GEN3_v0_3_RU
CODEPOINT: U+007D
VISIBLE_FORM: }
UNICODE_NAME: RIGHT CURLY BRACKET
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: правая фигурная скобка / закрытие шаблона и объекта
CATEGORY_ROADMAP: INJ (закрытие SSTI-шаблона, закрытие объекта) · PHAGO: — (подделка закрытия структуры)

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
VISIBLE_FORM: }
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: RIGHT_CURLY_BRACKET_FORM ≠ EFFECT
SIGN_CATEGORY:
  - закрытие блока кода ({ ... })
  - закрытие объекта JSON/dict/set ({"k": "v"})
  - закрытие выражения шаблона (}}, })
  - закрытие brace expansion shell ({a,b})

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_BLOCK_ONLY — "}" не всегда безобидное закрытие блока (она завершает выражение шаблона)
  2. NOT_TEMPLATE_SAFE — "}}" закрывает выражение, которое движок затем вычисляет (SSTI/RCE)
  3. NOT_OBJECT_SAFE — "}" закрывает внедрённый объект-оператор/ключ (NoSQL/JSON)
  4. NOT_ESCAPED_PROOF — наличие "}" не значит, что она закавычена/экранирована
  5. NOT_ENCODED_SAFE — "%7D" может быть раскодирована обратно в "}" позже
  6. NOT_AUTHORITY — "}" не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сама по себе ничего не исполняет; закрытие/завершение делает контекст
  8. NOT_TRUST_SIGNAL — не повышает доверие
  9. NOT_BALANCED_PROOF — поставленная "}" может перебалансировать структуру под форму атакующего
  10. NOT_SANITIZED_PROOF — наличие "}" не значит, что ввод санитизирован
  11. NOT_OUTPUT_CONTEXT_PROOF — безопасность зависит от контекста разбора/вычисления

BASE_FORMULAS:
  RIGHT_CURLY_BRACKET_FORM ≠ EFFECT
  RIGHT_CURLY_BRACKET_FORM ≠ BLOCK_ONLY_PROOF
  RIGHT_CURLY_BRACKET_FORM ≠ TEMPLATE_SAFETY_PROOF
  RIGHT_CURLY_BRACKET_FORM ≠ OBJECT_SAFETY_PROOF
  RIGHT_CURLY_BRACKET_FORM ≠ ESCAPED_PROOF
  RIGHT_CURLY_BRACKET_FORM ≠ ENCODED_SAFETY_PROOF
  RIGHT_CURLY_BRACKET_FORM ≠ AUTHORITY
  RIGHT_CURLY_BRACKET_FORM ≠ EXECUTION_TRIGGER
  RIGHT_CURLY_BRACKET_FORM ≠ BALANCED_PROOF
  RIGHT_CURLY_BRACKET_FORM ≠ SANITIZED_PROOF
  RIGHT_CURLY_BRACKET_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: "}" (ZONE_1) имеет параллельные функции (закрытие блока, закрытие объекта, закрытие выражения шаблона, закрытие brace expansion), сосуществующие без культурной прецессии. Полисемия стабильного знака.
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
    GUARD: RIGHT_CURLY_BRACKET_FORM ≠ BLOCK_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: 'JSON {"name": "Ann"}'
    CONTEXT: корректный объект JSON, показанный как текст
    EXPECTED: INFO
    RISK: NONE
    GUARD: RIGHT_CURLY_BRACKET_FORM ≠ OBJECT_SAFETY_PROOF
  SAFE_CASE_003:
    INPUT: "if (x) { doThing() }"
    CONTEXT: блок кода, показанный как литеральный текст
    EXPECTED: INFO
    RISK: NONE
    GUARD: RIGHT_CURLY_BRACKET_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "CSS rule: body { margin: 0 }"
    CONTEXT: блок объявлений CSS
    EXPECTED: INFO
    RISK: NONE
    GUARD: RIGHT_CURLY_BRACKET_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "the } key on a keyboard"
    CONTEXT: название клавиши фигурной скобки в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: RIGHT_CURLY_BRACKET_FORM ≠ BLOCK_ONLY_PROOF
  SAFE_CASE_006:
    INPUT: "quantifier a{2,3} in a regex"
    CONTEXT: описание квантора регэкспа в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: RIGHT_CURLY_BRACKET_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: SSTI_EXPRESSION_CLOSE
    INPUT: "{{7*7}} completing an evaluated expression"
    CONTEXT: "}}" закрывает выражение, чтобы движок его вычислил
    RISK: CRITICAL
    ATTACK: "}}" финализирует "{{...}}", так что оно вычисляется на сервере (SSTI/RCE)
    GUARD: RIGHT_CURLY_BRACKET_FORM ≠ TEMPLATE_SAFETY_PROOF
  RISK_CASE_002:
    NAME: NOSQL_OBJECT_CLOSE
    INPUT: '{"$ne": null}'
    CONTEXT: "}" закрывает внедрённый объект-оператор NoSQL
    RISK: HIGH
    ATTACK: "}" завершает объект "$ne", так что всегда-истинный запрос выполняется (обход аутентификации)
    GUARD: RIGHT_CURLY_BRACKET_FORM ≠ OBJECT_SAFETY_PROOF
  RISK_CASE_003:
    NAME: FORMAT_FIELD_CLOSE
    INPUT: "{0.__class__} closing a format field"
    CONTEXT: "}" завершает форматное поле, обходящее внутренности объекта
    RISK: HIGH
    ATTACK: "}" финализирует "{0...}", так что str.format утекает внутренности/globals
    GUARD: RIGHT_CURLY_BRACKET_FORM ≠ EFFECT
  RISK_CASE_004:
    NAME: JSON_STRUCTURE_REBALANCE
    INPUT: 'x"}, "isAdmin": true, "y": {"a":"'
    CONTEXT: "}" перебалансирует объект JSON для внедрения поддельного ключа
    RISK: HIGH
    ATTACK: "}" закрывает раньше времени, так что "isAdmin": true внедряется как соседний ключ
    GUARD: RIGHT_CURLY_BRACKET_FORM ≠ BALANCED_PROOF
  RISK_CASE_005:
    NAME: ENCODED_BRACE_BYPASS
    INPUT: "%7B%7B7*7%7D%7D (с поздним декодированием)"
    CONTEXT: кодированный "}}" декодируется обратно перед движком шаблона
    RISK: HIGH
    ATTACK: %7D декодируется в "}" ПОСЛЕ проверки → завершает выражение шаблона
    GUARD: RIGHT_CURLY_BRACKET_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_BRACE_BYPASS
    INPUT: "｛｛7*7｝｝ (полноширинная ｝ U+FF5D)"
    CONTEXT: похожий знак для обхода фильтра "}"
    RISK: MEDIUM
    ATTACK: фильтр ищет ASCII "}", нормализатор может свернуть ｝ в "}"
    GUARD: RIGHT_CURLY_BRACKET_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ｝
    CODEPOINT: U+FF5D
    NAME: FULLWIDTH RIGHT CURLY BRACKET
    RISK: HIGH
    RULE: FULLWIDTH_RIGHT_CURLY_BRACKET ≠ RIGHT_CURLY_BRACKET (обходит фильтр, ищущий ASCII "}")
  CONFUSABLE_002:
    VISIBLE_FORM: ﹜
    CODEPOINT: U+FE5C
    NAME: SMALL RIGHT CURLY BRACKET
    RISK: MEDIUM
    RULE: SMALL_RIGHT_CURLY_BRACKET ≠ RIGHT_CURLY_BRACKET
  CONFUSABLE_003:
    VISIBLE_FORM: ❵
    CODEPOINT: U+2775
    NAME: MEDIUM RIGHT CURLY BRACKET ORNAMENT
    RISK: LOW
    RULE: MEDIUM_RIGHT_CURLY_BRACKET_ORNAMENT ≠ RIGHT_CURLY_BRACKET
  CONFUSABLE_004:
    VISIBLE_FORM: ⦄
    CODEPOINT: U+2984
    NAME: RIGHT WHITE CURLY BRACKET
    RISK: LOW
    RULE: RIGHT_WHITE_CURLY_BRACKET ≠ RIGHT_CURLY_BRACKET
  CONFUSABLE_005:
    VISIBLE_FORM: 𝄕
    CODEPOINT: U+1D115
    NAME: MUSICAL SYMBOL BRACKET
    RISK: LOW
    RULE: MUSICAL_SYMBOL_BRACKET ≠ RIGHT_CURLY_BRACKET

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "'}' — это всегда безобидное закрытие блока"
    RESPONSE: RIGHT_CURLY_BRACKET_FORM ≠ BLOCK_ONLY_PROOF
    RULE: "}}" завершает выражение шаблона, которое движок вычисляет
  CG2:
    TRIGGER: "закрытие блока шаблона инертно"
    RESPONSE: RIGHT_CURLY_BRACKET_FORM ≠ TEMPLATE_SAFETY_PROOF
    RULE: завершённое выражение вычисляется (SSTI/RCE)
  CG3:
    TRIGGER: "закрытие объекта JSON не может быть опасным"
    RESPONSE: RIGHT_CURLY_BRACKET_FORM ≠ OBJECT_SAFETY_PROOF
    RULE: "}" завершает внедрённый оператор ($ne) или поддельный соседний ключ
  CG4:
    TRIGGER: "'%7D' безопасен навсегда"
    RESPONSE: RIGHT_CURLY_BRACKET_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в "}" перед движком
  CG5:
    TRIGGER: "фильтр по ASCII '}' ловит все фигурные скобки"
    RESPONSE: RIGHT_CURLY_BRACKET_FORM ≠ EFFECT
    RULE: полноширинная ｝ (U+FF5D) и малая ﹜ (U+FE5C) — другие кодпоинты
  CG6:
    TRIGGER: "наличие '}' значит, что ввод санитизирован"
    RESPONSE: RIGHT_CURLY_BRACKET_FORM ≠ SANITIZED_PROOF
    RULE: наличие знака ничего не говорит о санитизации

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "}}"
      NAME: TEMPLATE_EXPR_CLOSE
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: завершение вычисляемого выражения шаблона (SSTI)
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: '"}'
      NAME: OBJECT_KEY_CLOSE
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: раннее закрытие объекта для внедрения соседнего ключа
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "%}"
      NAME: TEMPLATE_TAG_CLOSE
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: закрытие управляющего тега шаблона (if/for/include)
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — последовательности с "}" центральны для инъекции шаблона/объекта.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: "}" закрывает блок/объект/выражение шаблона, но не имитирует существование верифицированной сущности. Его риски — инъекция шаблона/объекта, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена ASCII "}" на полноширинную ｝ (U+FF5D) для обхода фильтра
  A2: замена на малую ﹜ (U+FE5C)
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: закрытие выражения SSTI {{7*7}}
  B2: закрытие объекта NoSQL {"$ne": null}
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "}}" (SC1) — закрытие выражения шаблона
  C2: '"}' (SC2) — закрытие/перебалансировка ключа объекта
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: "}" подан как безобидное закрытие блока JSON/кода внутри поля шаблона
  D2: "%7D" как «безопасный» кодированный текст с поздним декодированием
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: завершение выражения шаблона в рендеримую страницу
  E2: N/A — вектор: инъекция поддельного соседнего ключа через раннее закрытие объекта
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: "}" — всегда безобидное закрытие блока
  EXPECTED: FAIL_BLOCK_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: закрытие блока шаблона инертно
  EXPECTED: FAIL_TEMPLATE_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: закрытие объекта JSON не может быть опасным
  EXPECTED: FAIL_OBJECT_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%7D" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: фильтр по ASCII "}" ловит все похожие фигурные скобки
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: наличие "}" доказывает санитизацию ввода
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как экранировать "}" по контексту (шаблон/JSON/формат) без ложных срабатываний на блоках кода/множествах/CSS/квантора регэкспа?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (песочница/logic-less шаблоны + JSON по схеме + безопасные API форматирования — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «безопасность '}' решается контекстом разбора/вычисления».
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
