PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_LEFT_PARENTHESIS_U0028_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: Русский оригинал (authoritative). Английское зеркало — SIGN_CORE_CARD_LEFT_PARENTHESIS_U0028_GEN3_v0_3_EN. Кодпоинты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_LEFT_PARENTHESIS_U0028_GEN3_v0_3_RU
CODEPOINT: U+0028
VISIBLE_FORM: (
UNICODE_NAME: LEFT PARENTHESIS
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: левая скобка / открытие вызова и фильтра
CATEGORY_ROADMAP: INJ (группа LDAP-фильтра, открытие вызова/subshell) · PHAGO: — (подделка группировки)

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
VISIBLE_FORM: (
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: LEFT_PARENTHESIS_FORM ≠ EFFECT
SIGN_CATEGORY:
  - группировка в математике/тексте (a (b))
  - открытие вызова функции (fn(args))
  - группировка LDAP-фильтра ((&(a)(b)))
  - открытие subshell / regex-группы ((cmd), (a|b))

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_GROUPING_ONLY — "(" не всегда безобидная группировка (он открывает вызовы/фильтры/subshell)
  2. NOT_CALL_SAFE — открытие вызова может вызвать функцию с аргументами, сформированными атакующим
  3. NOT_BALANCED_PROOF — одиночная "(" может разбалансировать и внедриться в фильтр/выражение
  4. NOT_ESCAPED_PROOF — наличие "(" не значит, что она закавычена/экранирована
  5. NOT_ENCODED_SAFE — "%28" может быть раскодирована обратно в "(" позже
  6. NOT_AUTHORITY — "(" не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сама по себе ничего не исполняет; открытие группы/вызова делает контекст
  8. NOT_TRUST_SIGNAL — не повышает доверие
  9. NOT_LDAP_GROUP_SAFE — "(" открывает предложение LDAP-фильтра, которое может внедрить логику
  10. NOT_SANITIZED_PROOF — наличие "(" не значит, что ввод санитизирован
  11. NOT_OUTPUT_CONTEXT_PROOF — безопасность зависит от контекста разбора/раскрытия

BASE_FORMULAS:
  LEFT_PARENTHESIS_FORM ≠ EFFECT
  LEFT_PARENTHESIS_FORM ≠ GROUPING_ONLY_PROOF
  LEFT_PARENTHESIS_FORM ≠ CALL_SAFETY_PROOF
  LEFT_PARENTHESIS_FORM ≠ BALANCED_PROOF
  LEFT_PARENTHESIS_FORM ≠ ESCAPED_PROOF
  LEFT_PARENTHESIS_FORM ≠ ENCODED_SAFETY_PROOF
  LEFT_PARENTHESIS_FORM ≠ AUTHORITY
  LEFT_PARENTHESIS_FORM ≠ EXECUTION_TRIGGER
  LEFT_PARENTHESIS_FORM ≠ LDAP_GROUP_SAFETY_PROOF
  LEFT_PARENTHESIS_FORM ≠ SANITIZED_PROOF
  LEFT_PARENTHESIS_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: "(" (ZONE_1) имеет параллельные функции (группировка, открытие вызова, группа LDAP, subshell/regex-группа), сосуществующие без культурной прецессии. Полисемия стабильного знака.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1
  NOTE: пунктуационно-математический знак без жестового предшественника; функции вызова/фильтра/группы надстроены цифровой эпохой параллельно.

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
    INPUT: "the total (with tax) is 20"
    CONTEXT: скобочная группировка в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: LEFT_PARENTHESIS_FORM ≠ GROUPING_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: "call foo(x, y)"
    CONTEXT: вызов функции, показанный как текст
    EXPECTED: INFO
    RISK: NONE
    GUARD: LEFT_PARENTHESIS_FORM ≠ CALL_SAFETY_PROOF
  SAFE_CASE_003:
    INPUT: "(a + b) * c"
    CONTEXT: математическая группировка в выражении
    EXPECTED: INFO
    RISK: NONE
    GUARD: LEFT_PARENTHESIS_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "see figure (3) below"
    CONTEXT: номер ссылки в скобках
    EXPECTED: INFO
    RISK: NONE
    GUARD: LEFT_PARENTHESIS_FORM ≠ GROUPING_ONLY_PROOF
  SAFE_CASE_005:
    INPUT: "emoticon :-)"
    CONTEXT: скобка внутри смайлика
    EXPECTED: INFO
    RISK: NONE
    GUARD: LEFT_PARENTHESIS_FORM ≠ EFFECT
  SAFE_CASE_006:
    INPUT: "regex group (abc) matches abc"
    CONTEXT: описание regex-группы в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: LEFT_PARENTHESIS_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: LDAP_FILTER_GROUP_INJECTION
    INPUT: "*)(uid=*))(|(uid=*"
    CONTEXT: "(" открывает внедрённое предложение LDAP-фильтра
    RISK: CRITICAL
    ATTACK: "(" + ")" переформируют фильтр в OR, совпадающий с любым пользователем (обход аутентификации)
    GUARD: LEFT_PARENTHESIS_FORM ≠ LDAP_GROUP_SAFETY_PROOF
  RISK_CASE_002:
    NAME: SSTI_CALL_OPEN
    INPUT: "{{ cycler.__init__.__globals__.os.popen('id') }}"
    CONTEXT: "(" открывает вызов в server-side шаблоне
    RISK: CRITICAL
    ATTACK: "(" вызывает метод (popen) внутри вычисляемого шаблона → RCE
    GUARD: LEFT_PARENTHESIS_FORM ≠ CALL_SAFETY_PROOF
  RISK_CASE_003:
    NAME: SUBSHELL_OPEN
    INPUT: "$(id) or `(reboot)`"
    CONTEXT: "(" открывает subshell в подстановке команды
    RISK: HIGH
    ATTACK: "(" группирует список команд, исполняемый как subshell
    GUARD: LEFT_PARENTHESIS_FORM ≠ EFFECT
  RISK_CASE_004:
    NAME: REGEX_GROUP_REDOS
    INPUT: "(a+)+ на длинном вводе"
    CONTEXT: "(" открывает вложенную квантифицированную группу (ReDoS)
    RISK: HIGH
    ATTACK: группа плюс кванторы вызывают катастрофический бэктрекинг
    GUARD: LEFT_PARENTHESIS_FORM ≠ EFFECT
  RISK_CASE_005:
    NAME: ENCODED_PAREN_BYPASS
    INPUT: "%28uid=*%29 (с поздним декодированием)"
    CONTEXT: кодированная "(" декодируется обратно перед фильтром
    RISK: MEDIUM
    ATTACK: %28 декодируется в "(" ПОСЛЕ проверки → группировка фильтра
    GUARD: LEFT_PARENTHESIS_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_PAREN_BYPASS
    INPUT: "（uid=* (полноширинная （ U+FF08)"
    CONTEXT: похожий знак для обхода фильтра "("
    RISK: MEDIUM
    ATTACK: фильтр ищет ASCII "(", нормализатор может свернуть （ в "("
    GUARD: LEFT_PARENTHESIS_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: （
    CODEPOINT: U+FF08
    NAME: FULLWIDTH LEFT PARENTHESIS
    RISK: HIGH
    RULE: FULLWIDTH_LEFT_PARENTHESIS ≠ LEFT_PARENTHESIS (обходит фильтр, ищущий ASCII "(")
  CONFUSABLE_002:
    VISIBLE_FORM: ﹙
    CODEPOINT: U+FE59
    NAME: SMALL LEFT PARENTHESIS
    RISK: MEDIUM
    RULE: SMALL_LEFT_PARENTHESIS ≠ LEFT_PARENTHESIS
  CONFUSABLE_003:
    VISIBLE_FORM: ⁽
    CODEPOINT: U+207D
    NAME: SUPERSCRIPT LEFT PARENTHESIS
    RISK: LOW
    RULE: SUPERSCRIPT_LEFT_PARENTHESIS ≠ LEFT_PARENTHESIS
  CONFUSABLE_004:
    VISIBLE_FORM: ₍
    CODEPOINT: U+208D
    NAME: SUBSCRIPT LEFT PARENTHESIS
    RISK: LOW
    RULE: SUBSCRIPT_LEFT_PARENTHESIS ≠ LEFT_PARENTHESIS
  CONFUSABLE_005:
    VISIBLE_FORM: ❨
    CODEPOINT: U+2768
    NAME: MEDIUM LEFT PARENTHESIS ORNAMENT
    RISK: LOW
    RULE: MEDIUM_LEFT_PARENTHESIS_ORNAMENT ≠ LEFT_PARENTHESIS

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "'(' — это всегда безобидная группировка"
    RESPONSE: LEFT_PARENTHESIS_FORM ≠ GROUPING_ONLY_PROOF
    RULE: "(" открывает вызовы, предложения LDAP-фильтра, subshell и regex-группы
  CG2:
    TRIGGER: "открытие вызова не может быть опасным"
    RESPONSE: LEFT_PARENTHESIS_FORM ≠ CALL_SAFETY_PROOF
    RULE: "(" может вызвать метод с аргументами атакующего (SSTI/RCE)
  CG3:
    TRIGGER: "'(' в LDAP просто начинает группу"
    RESPONSE: LEFT_PARENTHESIS_FORM ≠ LDAP_GROUP_SAFETY_PROOF
    RULE: "(" открывает предложение фильтра, которое может внедрить OR/любое совпадение
  CG4:
    TRIGGER: "'%28' безопасен навсегда"
    RESPONSE: LEFT_PARENTHESIS_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в "(" перед парсером
  CG5:
    TRIGGER: "фильтр по ASCII '(' ловит все скобки"
    RESPONSE: LEFT_PARENTHESIS_FORM ≠ EFFECT
    RULE: полноширинная （ (U+FF08) и малая ﹙ (U+FE59) — другие кодпоинты
  CG6:
    TRIGGER: "наличие '(' значит, что ввод санитизирован"
    RESPONSE: LEFT_PARENTHESIS_FORM ≠ SANITIZED_PROOF
    RULE: наличие знака ничего не говорит о санитизации

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: ")(|"
      NAME: LDAP_OR_INJECTION
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: закрытие и повторное открытие фильтра с внедрённым OR
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "$("
      NAME: SUBSHELL_SUBSTITUTION
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: открытие subshell подстановки команды
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "(a+)+"
      NAME: REGEX_NESTED_GROUP
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: вложенная квантифицированная группа, вызывающая ReDoS
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — последовательности с "(" центральны для инъекции фильтра/вызова/subshell.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: "(" открывает группу/вызов/предложение фильтра, но не имитирует существование верифицированной сущности. Его риски — инъекция группировки/вызова, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена ASCII "(" на полноширинную （ (U+FF08) для обхода фильтра
  A2: замена на малую ﹙ (U+FE59)
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: инъекция группы LDAP-фильтра *)(uid=*))(|(uid=*
  B2: открытие вызова SSTI cycler...popen('id')
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: ")(|" (SC1) — инъекция OR в LDAP
  C2: "$(" (SC2) — подстановка subshell
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: "(" подан как безобидная группировка внутри поля фильтра
  D2: "%28" как «безопасный» кодированный текст с поздним декодированием
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: инъекция группы фильтра в LDAP-bind
  E2: N/A — вектор: вызов метода в server-side шаблоне
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: "(" — всегда безобидная группировка
  EXPECTED: FAIL_GROUPING_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: открытие вызова не может быть опасным
  EXPECTED: FAIL_CALL_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: "(" в LDAP просто начинает группу
  EXPECTED: FAIL_LDAP_GROUP_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%28" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: фильтр по ASCII "(" ловит все похожие скобки
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: наличие "(" доказывает санитизацию ввода
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как экранировать "(" по контексту (LDAP/шаблон/shell/регэксп) без ложных срабатываний на тексте/математике/вызовах/смайликах?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (экранирование LDAP-фильтра + песочница шаблонов + exec через вектор аргументов + таймаут регэкспа — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «безопасность '(' решается контекстом разбора/раскрытия».
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
