PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_RIGHT_SQUARE_BRACKET_U005D_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: Русский оригинал (authoritative). Английское зеркало — SIGN_CORE_CARD_RIGHT_SQUARE_BRACKET_U005D_GEN3_v0_3_EN. Кодпоинты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_RIGHT_SQUARE_BRACKET_U005D_GEN3_v0_3_RU
CODEPOINT: U+005D
VISIBLE_FORM: ]
UNICODE_NAME: RIGHT SQUARE BRACKET
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: правая квадратная скобка / закрытие индекса и массива
CATEGORY_ROADMAP: INJ (закрытие param-array/вложенного ключа, закрытие regex-класса) · PHAGO: — (подделка закрытия вложенного ключа)

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
VISIBLE_FORM: ]
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: RIGHT_SQUARE_BRACKET_FORM ≠ EFFECT
SIGN_CATEGORY:
  - закрытие доступа массив/индекс (arr[i], obj[key])
  - закрытие массива JSON ([1, 2, 3])
  - закрытие символьного класса регэкспа ([a-z])
  - закрытие вложенного ключа в строке запроса (a[b]=1)

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INDEX_ONLY — "]" не всегда безобидное закрытие (она завершает вложенный ключ / массив)
  2. NOT_ARRAY_SAFE — "]" завершает внедрённую структуру вложенного ключа/массива
  3. NOT_KEY_SCOPED — "]" завершает "[__proto__]"/"[role]", так что ключ вступает в силу
  4. NOT_ESCAPED_PROOF — наличие "]" не значит, что она закавычена/экранирована
  5. NOT_ENCODED_SAFE — "%5D" может быть раскодирована обратно в "]" позже
  6. NOT_AUTHORITY — "]" не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сама по себе ничего не исполняет; завершение ключа/массива делает контекст
  8. NOT_TRUST_SIGNAL — не повышает доверие
  9. NOT_REGEX_CLASS_SAFE — "]" закрывает символьный класс; неверно поставленная "]" меняет совпадение
  10. NOT_SANITIZED_PROOF — наличие "]" не значит, что ввод санитизирован
  11. NOT_OUTPUT_CONTEXT_PROOF — безопасность зависит от контекста разбора/связывания

BASE_FORMULAS:
  RIGHT_SQUARE_BRACKET_FORM ≠ EFFECT
  RIGHT_SQUARE_BRACKET_FORM ≠ INDEX_ONLY_PROOF
  RIGHT_SQUARE_BRACKET_FORM ≠ ARRAY_SAFETY_PROOF
  RIGHT_SQUARE_BRACKET_FORM ≠ KEY_SCOPE_PROOF
  RIGHT_SQUARE_BRACKET_FORM ≠ ESCAPED_PROOF
  RIGHT_SQUARE_BRACKET_FORM ≠ ENCODED_SAFETY_PROOF
  RIGHT_SQUARE_BRACKET_FORM ≠ AUTHORITY
  RIGHT_SQUARE_BRACKET_FORM ≠ EXECUTION_TRIGGER
  RIGHT_SQUARE_BRACKET_FORM ≠ REGEX_CLASS_SAFETY_PROOF
  RIGHT_SQUARE_BRACKET_FORM ≠ SANITIZED_PROOF
  RIGHT_SQUARE_BRACKET_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: "]" (ZONE_1) имеет параллельные функции (закрытие массива/индекса, закрытие массива JSON, закрытие класса регэкспа, закрытие вложенного ключа запроса), сосуществующие без культурной прецессии. Полисемия стабильного знака.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1
  NOTE: пунктуационно-математическая скобка без жестового предшественника; функции индекса/массива/класса надстроены цифровой эпохой параллельно.

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
    INPUT: "arr[0] returns the first item"
    CONTEXT: индексация массива, показанная как текст
    EXPECTED: INFO
    RISK: NONE
    GUARD: RIGHT_SQUARE_BRACKET_FORM ≠ INDEX_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: "JSON [1, 2, 3]"
    CONTEXT: корректный массив JSON, показанный как текст
    EXPECTED: INFO
    RISK: NONE
    GUARD: RIGHT_SQUARE_BRACKET_FORM ≠ ARRAY_SAFETY_PROOF
  SAFE_CASE_003:
    INPUT: "regex [a-z]+ matches letters"
    CONTEXT: описание символьного класса регэкспа
    EXPECTED: INFO
    RISK: NONE
    GUARD: RIGHT_SQUARE_BRACKET_FORM ≠ REGEX_CLASS_SAFETY_PROOF
  SAFE_CASE_004:
    INPUT: "see reference [12] in the bibliography"
    CONTEXT: номер цитаты в скобках
    EXPECTED: INFO
    RISK: NONE
    GUARD: RIGHT_SQUARE_BRACKET_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "the ] key on a keyboard"
    CONTEXT: название клавиши скобки в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: RIGHT_SQUARE_BRACKET_FORM ≠ INDEX_ONLY_PROOF
  SAFE_CASE_006:
    INPUT: "[INFO] log line prefix"
    CONTEXT: скобочный тег уровня лога
    EXPECTED: INFO
    RISK: NONE
    GUARD: RIGHT_SQUARE_BRACKET_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: PROTOTYPE_POLLUTION_CLOSE
    INPUT: "obj[__proto__][isAdmin]=true"
    CONTEXT: "]" завершает вложенный ключ, достигающий прототипа
    RISK: CRITICAL
    ATTACK: "]" финализирует "[__proto__]", так что Object.prototype загрязняется
    GUARD: RIGHT_SQUARE_BRACKET_FORM ≠ KEY_SCOPE_PROOF
  RISK_CASE_002:
    NAME: MASS_ASSIGN_CLOSE
    INPUT: "user[role]=admin"
    CONTEXT: "]" завершает вложенный параметр, связанный с моделью
    RISK: HIGH
    ATTACK: "]" завершает "user[role]", так что привилегированное поле массово присваивается
    GUARD: RIGHT_SQUARE_BRACKET_FORM ≠ ARRAY_SAFETY_PROOF
  RISK_CASE_003:
    NAME: ARRAY_TYPE_CLOSE
    INPUT: "id[]=1 (завершение массива, где ожидается скаляр)"
    CONTEXT: "]" завершает параметр-массив
    RISK: MEDIUM
    ATTACK: "]" финализирует "id[]", так что значение — массив (путаница типов)
    GUARD: RIGHT_SQUARE_BRACKET_FORM ≠ EFFECT
  RISK_CASE_004:
    NAME: REGEX_CLASS_CLOSE_SHIFT
    INPUT: "[a-z]] (лишняя ], сдвигающая границу класса)"
    CONTEXT: неверно поставленная "]", меняющая место окончания символьного класса
    RISK: MEDIUM
    ATTACK: ранняя/поздняя "]" меняет класс, так что он совпадает с непреднамеренными символами
    GUARD: RIGHT_SQUARE_BRACKET_FORM ≠ REGEX_CLASS_SAFETY_PROOF
  RISK_CASE_005:
    NAME: ENCODED_BRACKET_BYPASS
    INPUT: "obj%5B__proto__%5D (с поздним декодированием)"
    CONTEXT: кодированная "]" декодируется обратно перед связывателем
    RISK: HIGH
    ATTACK: %5D декодируется в "]" ПОСЛЕ проверки → завершает связывание вложенного ключа
    GUARD: RIGHT_SQUARE_BRACKET_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_BRACKET_BYPASS
    INPUT: "obj［key］ (полноширинная ］ U+FF3D)"
    CONTEXT: похожий знак для обхода фильтра "]"
    RISK: MEDIUM
    ATTACK: фильтр ищет ASCII "]", нормализатор может свернуть ］ в "]"
    GUARD: RIGHT_SQUARE_BRACKET_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ］
    CODEPOINT: U+FF3D
    NAME: FULLWIDTH RIGHT SQUARE BRACKET
    RISK: HIGH
    RULE: FULLWIDTH_RIGHT_SQUARE_BRACKET ≠ RIGHT_SQUARE_BRACKET (обходит фильтр, ищущий ASCII "]")
  CONFUSABLE_002:
    VISIBLE_FORM: ﹈
    CODEPOINT: U+FE48
    NAME: PRESENTATION FORM FOR VERTICAL RIGHT SQUARE BRACKET
    RISK: MEDIUM
    RULE: PRESENTATION_VERTICAL_RIGHT_SQUARE_BRACKET ≠ RIGHT_SQUARE_BRACKET
  CONFUSABLE_003:
    VISIBLE_FORM: ⁆
    CODEPOINT: U+2046
    NAME: RIGHT SQUARE BRACKET WITH QUILL
    RISK: LOW
    RULE: RIGHT_SQUARE_BRACKET_WITH_QUILL ≠ RIGHT_SQUARE_BRACKET
  CONFUSABLE_004:
    VISIBLE_FORM: ❳
    CODEPOINT: U+2773
    NAME: LIGHT RIGHT TORTOISE SHELL BRACKET ORNAMENT
    RISK: LOW
    RULE: LIGHT_RIGHT_TORTOISE_SHELL_BRACKET_ORNAMENT ≠ RIGHT_SQUARE_BRACKET
  CONFUSABLE_005:
    VISIBLE_FORM: 〛
    CODEPOINT: U+301B
    NAME: RIGHT WHITE SQUARE BRACKET
    RISK: LOW
    RULE: RIGHT_WHITE_SQUARE_BRACKET ≠ RIGHT_SQUARE_BRACKET

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "']' — это всегда безобидное закрытие"
    RESPONSE: RIGHT_SQUARE_BRACKET_FORM ≠ INDEX_ONLY_PROOF
    RULE: "]" завершает вложенные ключи, массивы и классы регэкспа
  CG2:
    TRIGGER: "закрытие массива/ключа не может быть опасным"
    RESPONSE: RIGHT_SQUARE_BRACKET_FORM ≠ ARRAY_SAFETY_PROOF
    RULE: "]" завершает "[role]"/"[__proto__]", так что внедрённый ключ вступает в силу
  CG3:
    TRIGGER: "']' просто завершает строковый ключ"
    RESPONSE: RIGHT_SQUARE_BRACKET_FORM ≠ KEY_SCOPE_PROOF
    RULE: завершённый вложенный ключ может загрязнить прототип или массово присвоить
  CG4:
    TRIGGER: "'%5D' безопасен навсегда"
    RESPONSE: RIGHT_SQUARE_BRACKET_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в "]" перед связывателем
  CG5:
    TRIGGER: "фильтр по ASCII ']' ловит все скобки"
    RESPONSE: RIGHT_SQUARE_BRACKET_FORM ≠ EFFECT
    RULE: полноширинная ］ (U+FF3D) — другой кодпоинт
  CG6:
    TRIGGER: "наличие ']' значит, что ввод санитизирован"
    RESPONSE: RIGHT_SQUARE_BRACKET_FORM ≠ SANITIZED_PROOF
    RULE: наличие знака ничего не говорит о санитизации

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "__proto__]"
      NAME: PROTOTYPE_POLLUTION_CLOSE
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: завершение вложенного ключа, достигающего прототипа объекта
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "role]"
      NAME: MASS_ASSIGNMENT_CLOSE
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: завершение привилегированного вложенного поля для связывания
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "]]"
      NAME: REGEX_CLASS_SHIFT
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: лишняя "]", сдвигающая границу класса регэкспа
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — последовательности с "]" центральны для инъекции вложенного ключа/массива.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: "]" закрывает индекс/массив/вложенный ключ, но не имитирует существование верифицированной сущности. Его риски — инъекция вложенного ключа/массива, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена ASCII "]" на полноширинную ］ (U+FF3D) для обхода фильтра
  A2: замена на presentation form ﹈ (U+FE48)
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: закрытие prototype pollution obj[__proto__][isAdmin]=true
  B2: закрытие массового присваивания user[role]=admin
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "__proto__]" (SC1) — закрытие prototype pollution
  C2: "]]" (SC3) — сдвиг границы regex-класса
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: "]" подан как безобидное закрытие индекса внутри поля параметра
  D2: "%5D" как «безопасный» кодированный текст с поздним декодированием
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: завершение prototype pollution в граф объектов JS
  E2: N/A — вектор: завершение массового присваивания в модель
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: "]" — всегда безобидное закрытие
  EXPECTED: FAIL_INDEX_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: закрытие массива/ключа не может быть опасным
  EXPECTED: FAIL_ARRAY_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: "]" просто завершает строковый ключ
  EXPECTED: FAIL_KEY_SCOPE_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%5D" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: фильтр по ASCII "]" ловит все похожие скобки
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: наличие "]" доказывает санитизацию ввода
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как безопасно связывать завершённые "]" вложенные ключи (запрос/JSON/регэксп) без ложных срабатываний на индексации/массивах/цитатах/тегах логов?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (блокировка ключей __proto__/constructor + явное allow-list связывание + безопасное построение regex-класса — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «безопасность ']' решается контекстом разбора/связывания».
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
