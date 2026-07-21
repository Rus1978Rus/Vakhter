PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_DOLLAR_SIGN_U0024_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: Русский оригинал (authoritative). Английское зеркало — SIGN_CORE_CARD_DOLLAR_SIGN_U0024_GEN3_v0_3_EN. Кодпоинты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_DOLLAR_SIGN_U0024_GEN3_v0_3_RU
CODEPOINT: U+0024
VISIBLE_FORM: $
UNICODE_NAME: DOLLAR SIGN
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: знак доллара / раскрытие переменной
CATEGORY_ROADMAP: INJ (раскрытие переменной/команды shell, шаблон) · PHAGO: — (интерполяция)

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
VISIBLE_FORM: $
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: DOLLAR_SIGN_FORM ≠ EFFECT
SIGN_CATEGORY:
  - раскрытие переменной shell ($VAR, ${VAR})
  - подстановка команды shell ($(cmd))
  - маркер шаблона / интерполяции (${expr}, $name)
  - символ валюты / якорь конца в регэкспе (в тексте или шаблонах)

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_CURRENCY_ONLY — "$" не всегда символ валюты (в shell он раскрывает)
  2. NOT_VARIABLE_SAFE — раскрытие переменной может вставить подконтрольные атакующему значения в команду
  3. NOT_SUBSTITUTION_SAFE — "$(...)" выполняет вложенную команду как обратные кавычки
  4. NOT_ESCAPED_PROOF — наличие "$" не значит, что он экранирован/в одинарных кавычках
  5. NOT_ENCODED_SAFE — "%24" может быть раскодирован обратно в "$" позже
  6. NOT_AUTHORITY — "$" не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сам по себе ничего не исполняет; раскрытие делает контекст
  8. NOT_TRUST_SIGNAL — не повышает доверие
  9. NOT_TEMPLATE_SAFE — "${...}" в шаблоне может вычислить выражение (SSTI/JS)
  10. NOT_SANITIZED_PROOF — наличие "$" не значит, что ввод санитизирован
  11. NOT_OUTPUT_CONTEXT_PROOF — безопасность зависит от контекста исполнения/разбора

BASE_FORMULAS:
  DOLLAR_SIGN_FORM ≠ EFFECT
  DOLLAR_SIGN_FORM ≠ CURRENCY_ONLY_PROOF
  DOLLAR_SIGN_FORM ≠ VARIABLE_SAFETY_PROOF
  DOLLAR_SIGN_FORM ≠ SUBSTITUTION_SAFETY_PROOF
  DOLLAR_SIGN_FORM ≠ ESCAPED_PROOF
  DOLLAR_SIGN_FORM ≠ ENCODED_SAFETY_PROOF
  DOLLAR_SIGN_FORM ≠ AUTHORITY
  DOLLAR_SIGN_FORM ≠ EXECUTION_TRIGGER
  DOLLAR_SIGN_FORM ≠ TEMPLATE_SAFETY_PROOF
  DOLLAR_SIGN_FORM ≠ SANITIZED_PROOF
  DOLLAR_SIGN_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: "$" (ZONE_1) имеет параллельные функции (валюта, раскрытие shell, подстановка команды, маркер шаблона, якорь регэкспа), сосуществующие без культурной прецессии. Полисемия стабильного знака.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1
  NOTE: валютно-письменный знак без жестового предшественника; функции раскрытия/подстановки/шаблона надстроены цифровой эпохой параллельно.

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
    INPUT: "Total: $19.99"
    CONTEXT: денежная сумма в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: DOLLAR_SIGN_FORM ≠ CURRENCY_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: "It costs $5 and $10"
    CONTEXT: денежные величины в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: DOLLAR_SIGN_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "regex: word$"
    CONTEXT: якорь конца строки в регэкспе (как литеральный текст)
    EXPECTED: INFO
    RISK: NONE
    GUARD: DOLLAR_SIGN_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "the $ symbol on the keyboard"
    CONTEXT: название глифа доллара в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: DOLLAR_SIGN_FORM ≠ CURRENCY_ONLY_PROOF
  SAFE_CASE_005:
    INPUT: "jQuery uses $ as an alias"
    CONTEXT: "$" как идентификатор в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: DOLLAR_SIGN_FORM ≠ EFFECT
  SAFE_CASE_006:
    INPUT: "price rose from $2 to $3"
    CONTEXT: две денежные суммы в предложении
    EXPECTED: INFO
    RISK: NONE
    GUARD: DOLLAR_SIGN_FORM ≠ CURRENCY_ONLY_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: COMMAND_SUBSTITUTION
    INPUT: "echo $(rm -rf ~)"
    CONTEXT: "$(...)" исполняет вложенную команду
    RISK: CRITICAL
    ATTACK: shell выполняет команду внутри "$(...)" и вставляет её вывод
    GUARD: DOLLAR_SIGN_FORM ≠ SUBSTITUTION_SAFETY_PROOF
  RISK_CASE_002:
    NAME: VARIABLE_SPLICE
    INPUT: "cp $USERFILE /etc/ (USERFILE=/etc/passwd; evil)"
    CONTEXT: подконтрольная атакующему переменная, вставленная в команду
    RISK: HIGH
    ATTACK: "$USERFILE" раскрывается в значение атакующего, меняя смысл команды
    GUARD: DOLLAR_SIGN_FORM ≠ VARIABLE_SAFETY_PROOF
  RISK_CASE_003:
    NAME: SSTI_TEMPLATE_EVAL
    INPUT: "${T(java.lang.Runtime).getRuntime().exec('id')}"
    CONTEXT: server-side template injection через "${...}"
    RISK: CRITICAL
    ATTACK: "${...}" вычисляется движком шаблона, исполняя код
    GUARD: DOLLAR_SIGN_FORM ≠ TEMPLATE_SAFETY_PROOF
  RISK_CASE_004:
    NAME: NOSQL_OPERATOR_INJECTION
    INPUT: '{"user": {"$ne": null}}'
    CONTEXT: "$"-префиксный оператор MongoDB, внедрённый через JSON
    RISK: HIGH
    ATTACK: "$ne" превращает сопоставление значения во всегда-истинный запрос (обход аутентификации)
    GUARD: DOLLAR_SIGN_FORM ≠ EFFECT
  RISK_CASE_005:
    NAME: ENCODED_DOLLAR_BYPASS
    INPUT: "cmd%24%28id%29 (с поздним декодированием)"
    CONTEXT: кодированный "$(" декодируется обратно перед исполнением
    RISK: HIGH
    ATTACK: %24%28 декодируется в "$(" ПОСЛЕ проверки → подстановка команды
    GUARD: DOLLAR_SIGN_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_DOLLAR_BYPASS
    INPUT: "＄(id) (полноширинный ＄ U+FF04)"
    CONTEXT: похожий знак для обхода фильтра "$"
    RISK: MEDIUM
    ATTACK: фильтр ищет ASCII "$", нормализатор может свернуть ＄ в "$"
    GUARD: DOLLAR_SIGN_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ＄
    CODEPOINT: U+FF04
    NAME: FULLWIDTH DOLLAR SIGN
    RISK: HIGH
    RULE: FULLWIDTH_DOLLAR_SIGN ≠ DOLLAR_SIGN (обходит фильтр, ищущий ASCII "$")
  CONFUSABLE_002:
    VISIBLE_FORM: ﹩
    CODEPOINT: U+FE69
    NAME: SMALL DOLLAR SIGN
    RISK: MEDIUM
    RULE: SMALL_DOLLAR_SIGN ≠ DOLLAR_SIGN
  CONFUSABLE_003:
    VISIBLE_FORM: ৳
    CODEPOINT: U+09F3
    NAME: BENGALI RUPEE SIGN
    RISK: LOW
    RULE: BENGALI_RUPEE ≠ DOLLAR_SIGN (только валютный двойник по виду)
  CONFUSABLE_004:
    VISIBLE_FORM: ₴
    CODEPOINT: U+20B4
    NAME: HRYVNIA SIGN
    RISK: LOW
    RULE: HRYVNIA ≠ DOLLAR_SIGN (только валютный двойник по виду)
  CONFUSABLE_005:
    VISIBLE_FORM: Ѕ
    CODEPOINT: U+0405
    NAME: CYRILLIC CAPITAL LETTER DZE
    RISK: LOW
    RULE: CYRILLIC_DZE ≠ DOLLAR_SIGN (перекрытие только по S-образной форме со штрихом)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "'$' — это всегда символ валюты"
    RESPONSE: DOLLAR_SIGN_FORM ≠ CURRENCY_ONLY_PROOF
    RULE: в shell "$" раскрывает переменные и запускает "$(...)"
  CG2:
    TRIGGER: "раскрытие переменной просто подставляет текст, оно не может навредить"
    RESPONSE: DOLLAR_SIGN_FORM ≠ VARIABLE_SAFETY_PROOF
    RULE: раскрытое значение может изменить смысл команды или вставить новые аргументы
  CG3:
    TRIGGER: "'${...}' в шаблоне инертен"
    RESPONSE: DOLLAR_SIGN_FORM ≠ TEMPLATE_SAFETY_PROOF
    RULE: движок шаблона может вычислить "${...}" как выражение (SSTI)
  CG4:
    TRIGGER: "'%24' безопасен навсегда"
    RESPONSE: DOLLAR_SIGN_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в "$" перед исполнением
  CG5:
    TRIGGER: "фильтр по ASCII '$' ловит все знаки доллара"
    RESPONSE: DOLLAR_SIGN_FORM ≠ EFFECT
    RULE: полноширинный ＄ (U+FF04) — другой кодпоинт
  CG6:
    TRIGGER: "наличие '$' значит, что ввод санитизирован"
    RESPONSE: DOLLAR_SIGN_FORM ≠ SANITIZED_PROOF
    RULE: наличие знака ничего не говорит о санитизации

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "$("
      NAME: COMMAND_SUBSTITUTION
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: открытие подстановки команды, исполняющей вложенную команду
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "${"
      NAME: EXPANSION_OR_TEMPLATE
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: раскрытие переменной или вычисление выражения шаблона (SSTI)
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "$IFS"
      NAME: FIELD_SEPARATOR_ABUSE
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: использование "$IFS" для вставки пробелов в фильтруемую команду
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — последовательности с "$" центральны для инъекции раскрытия/подстановки.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: "$" раскрывает/подставляет/интерполирует значения, но не имитирует существование верифицированной сущности. Его риски — раскрытие/вычисление, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена ASCII "$" на полноширинный ＄ (U+FF04) для обхода фильтра
  A2: замена на малый ﹩ (U+FE69)
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: подстановка команды echo $(rm -rf ~)
  B2: инъекция оператора NoSQL {"$ne": null}
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "$(" (SC1) — подстановка команды
  C2: "${" (SC2) — раскрытие / вычисление шаблона
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: "$" подан как безобидный символ валюты внутри поля команды
  D2: "%24" как «безопасный» кодированный текст с поздним декодированием
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: подстановка в шаблон OS-команды
  E2: N/A — вектор: вычисление SSTI-выражения в рендеримом шаблоне
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: "$" — всегда символ валюты
  EXPECTED: FAIL_CURRENCY_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: раскрытие переменной не может навредить
  EXPECTED: FAIL_VARIABLE_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: "${...}" в шаблоне инертен
  EXPECTED: FAIL_TEMPLATE_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%24" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: фильтр по ASCII "$" ловит все похожие знаки доллара
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: наличие "$" доказывает санитизацию ввода
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как нейтрализовать "$" по контексту (shell/шаблон/NoSQL) без ложных срабатываний на валюте/регэкспе/тексте?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (одинарные кавычки/exec через вектор аргументов + песочница шаблонов + фильтрация ключей-операторов — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «безопасность '$' решается контекстом исполнения/разбора».
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
