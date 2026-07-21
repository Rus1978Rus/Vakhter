PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_ASTERISK_U002A_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: Русский оригинал (authoritative). Английское зеркало — SIGN_CORE_CARD_ASTERISK_U002A_GEN3_v0_3_EN. Кодпоинты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_ASTERISK_U002A_GEN3_v0_3_RU
CODEPOINT: U+002A
VISIBLE_FORM: *
UNICODE_NAME: ASTERISK
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: звёздочка / подстановочный знак (wildcard)
CATEGORY_ROADMAP: INJ (glob/regex/LDAP/SQL wildcard) · PHAGO: — (расширение области совпадения)

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
VISIBLE_FORM: *
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: ASTERISK_FORM ≠ EFFECT
SIGN_CATEGORY:
  - glob-wildcard shell (*.txt)
  - квантор регэкспа «ноль или более» (a*)
  - wildcard SQL/LDAP (SELECT *, cn=*)
  - умножение / сноска / маркер выделения в тексте

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_MULTIPLY_ONLY — "*" не всегда умножение (в shell он делает glob по файлам)
  2. NOT_WILDCARD_SAFE — wildcard расширяет совпадение на непреднамеренные цели
  3. NOT_GLOB_SCOPED — "*" может раскрыться в файлы/аргументы вне назначенного набора
  4. NOT_ESCAPED_PROOF — наличие "*" не значит, что он закавычен/экранирован
  5. NOT_ENCODED_SAFE — "%2A" может быть раскодирован обратно в "*" позже
  6. NOT_AUTHORITY — "*" не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сам по себе ничего не исполняет; раскрытие делает контекст
  8. NOT_TRUST_SIGNAL — не повышает доверие
  9. NOT_LDAP_FILTER_SAFE — "*" в LDAP-фильтре может превратить равенство в «любой» (обход аутентификации)
  10. NOT_SANITIZED_PROOF — наличие "*" не значит, что ввод санитизирован
  11. NOT_OUTPUT_CONTEXT_PROOF — безопасность зависит от контекста разбора/раскрытия

BASE_FORMULAS:
  ASTERISK_FORM ≠ EFFECT
  ASTERISK_FORM ≠ MULTIPLY_ONLY_PROOF
  ASTERISK_FORM ≠ WILDCARD_SAFETY_PROOF
  ASTERISK_FORM ≠ GLOB_SCOPE_PROOF
  ASTERISK_FORM ≠ ESCAPED_PROOF
  ASTERISK_FORM ≠ ENCODED_SAFETY_PROOF
  ASTERISK_FORM ≠ AUTHORITY
  ASTERISK_FORM ≠ EXECUTION_TRIGGER
  ASTERISK_FORM ≠ LDAP_FILTER_SAFETY_PROOF
  ASTERISK_FORM ≠ SANITIZED_PROOF
  ASTERISK_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: "*" (ZONE_1) имеет параллельные функции (умножение, glob, квантор регэкспа, wildcard SQL/LDAP, сноска), сосуществующие без культурной прецессии. Полисемия стабильного знака.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1
  NOTE: типографско-математический знак без жестового предшественника; функции glob/регэкспа/wildcard надстроены цифровой эпохой параллельно.

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
    INPUT: "3 * 4 = 12"
    CONTEXT: умножение в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: ASTERISK_FORM ≠ MULTIPLY_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: "see the footnote *"
    CONTEXT: маркер сноски в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: ASTERISK_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "**bold** in Markdown"
    CONTEXT: маркеры выделения (как литеральный текст)
    EXPECTED: INFO
    RISK: NONE
    GUARD: ASTERISK_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "rating: 5 stars *****"
    CONTEXT: звёздочки как глифы звёзд в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: ASTERISK_FORM ≠ MULTIPLY_ONLY_PROOF
  SAFE_CASE_005:
    INPUT: "list all *.txt files"
    CONTEXT: описание glob-шаблона в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: ASTERISK_FORM ≠ GLOB_SCOPE_PROOF
  SAFE_CASE_006:
    INPUT: "the * key on a phone"
    CONTEXT: название клавиши звёздочки в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: ASTERISK_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: LDAP_WILDCARD_AUTH_BYPASS
    INPUT: "cn=*)(uid=*"
    CONTEXT: wildcard LDAP-фильтра, превращающий равенство в «любой»
    RISK: CRITICAL
    ATTACK: "*" совпадает с любым значением, а "(...)" внедряет логику фильтра → обход аутентификации
    GUARD: ASTERISK_FORM ≠ LDAP_FILTER_SAFETY_PROOF
  RISK_CASE_002:
    NAME: GLOB_ARG_INJECTION
    INPUT: "rm * (или rm -rf ./*)"
    CONTEXT: glob, раскрывающийся в непреднамеренные файлы/аргументы
    RISK: HIGH
    ATTACK: "*" раскрывается в каждую запись, возможно в имена файлов, похожие на флаги (-rf)
    GUARD: ASTERISK_FORM ≠ GLOB_SCOPE_PROOF
  RISK_CASE_003:
    NAME: REGEX_QUANTIFIER_REDOS
    INPUT: "(a+)*$ на длинном вводе"
    CONTEXT: вложенный квантор, вызывающий катастрофический бэктрекинг
    RISK: HIGH
    ATTACK: "*" над группой запускает ReDoS (отказ в обслуживании)
    GUARD: ASTERISK_FORM ≠ EFFECT
  RISK_CASE_004:
    NAME: SQL_WILDCARD_OVERMATCH
    INPUT: "name LIKE '%*%' расширяющий поиск"
    CONTEXT: wildcard, расширяющий запрос за пределы замысла
    RISK: MEDIUM
    ATTACK: "*"/"%" расширяет совпадение, раскрывая больше строк, чем задумано
    GUARD: ASTERISK_FORM ≠ WILDCARD_SAFETY_PROOF
  RISK_CASE_005:
    NAME: ENCODED_ASTERISK_BYPASS
    INPUT: "cn=%2A (с поздним декодированием)"
    CONTEXT: кодированный "*" декодируется обратно перед фильтром
    RISK: MEDIUM
    ATTACK: %2A декодируется в "*" ПОСЛЕ проверки → wildcard-совпадение
    GUARD: ASTERISK_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_ASTERISK_BYPASS
    INPUT: "cn=＊ (полноширинный ＊ U+FF0A)"
    CONTEXT: похожий знак для обхода фильтра "*"
    RISK: MEDIUM
    ATTACK: фильтр ищет ASCII "*", нормализатор может свернуть ＊ в "*"
    GUARD: ASTERISK_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ＊
    CODEPOINT: U+FF0A
    NAME: FULLWIDTH ASTERISK
    RISK: HIGH
    RULE: FULLWIDTH_ASTERISK ≠ ASTERISK (обходит фильтр, ищущий ASCII "*")
  CONFUSABLE_002:
    VISIBLE_FORM: ∗
    CODEPOINT: U+2217
    NAME: ASTERISK OPERATOR
    RISK: MEDIUM
    RULE: ASTERISK_OPERATOR ≠ ASTERISK
  CONFUSABLE_003:
    VISIBLE_FORM: ⁎
    CODEPOINT: U+204E
    NAME: LOW ASTERISK
    RISK: LOW
    RULE: LOW_ASTERISK ≠ ASTERISK
  CONFUSABLE_004:
    VISIBLE_FORM: ✱
    CODEPOINT: U+2731
    NAME: HEAVY ASTERISK
    RISK: LOW
    RULE: HEAVY_ASTERISK ≠ ASTERISK
  CONFUSABLE_005:
    VISIBLE_FORM: ٭
    CODEPOINT: U+066D
    NAME: ARABIC FIVE POINTED STAR
    RISK: LOW
    RULE: ARABIC_FIVE_POINTED_STAR ≠ ASTERISK

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "'*' — это всегда умножение"
    RESPONSE: ASTERISK_FORM ≠ MULTIPLY_ONLY_PROOF
    RULE: в shell/регэкспе/LDAP "*" — это wildcard/квантор
  CG2:
    TRIGGER: "wildcard не может быть опасен"
    RESPONSE: ASTERISK_FORM ≠ WILDCARD_SAFETY_PROOF
    RULE: "*" расширяет совпадение на непреднамеренные цели или раскрывается в неожиданные аргументы
  CG3:
    TRIGGER: "'*' в LDAP просто значит, что поле присутствует"
    RESPONSE: ASTERISK_FORM ≠ LDAP_FILTER_SAFETY_PROOF
    RULE: "*" превращает фильтр равенства в «любой», позволяя обход аутентификации
  CG4:
    TRIGGER: "'%2A' безопасен навсегда"
    RESPONSE: ASTERISK_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в "*" перед фильтром
  CG5:
    TRIGGER: "фильтр по ASCII '*' ловит все звёздочки"
    RESPONSE: ASTERISK_FORM ≠ EFFECT
    RULE: полноширинный ＊ (U+FF0A) и asterisk operator ∗ (U+2217) — другие кодпоинты
  CG6:
    TRIGGER: "наличие '*' значит, что ввод санитизирован"
    RESPONSE: ASTERISK_FORM ≠ SANITIZED_PROOF
    RULE: наличие знака ничего не говорит о санитизации

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "*)("
      NAME: LDAP_FILTER_INJECTION
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: wildcard плюс скобки фильтра, внедряющие логику LDAP
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "./*"
      NAME: GLOB_ARG_EXPANSION
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: glob, раскрывающийся в файлы, похожие на флаги команды
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: ")*"
      NAME: REGEX_NESTED_QUANTIFIER
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: квантор над группой, вызывающий катастрофический бэктрекинг
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — последовательности с "*" центральны для злоупотребления wildcard/glob/регэкспом.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: "*" расширяет совпадение или раскрывает glob, но не имитирует существование верифицированной сущности. Его риски — сверх-совпадение/раскрытие, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена ASCII "*" на полноширинный ＊ (U+FF0A) для обхода фильтра
  A2: замена на asterisk operator ∗ (U+2217)
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: обход аутентификации LDAP wildcard cn=*)(uid=*
  B2: сверх-совпадение SQL/LDAP name LIKE '%*%'
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "*)(" (SC1) — инъекция фильтра LDAP
  C2: ")*" (SC3) — вложенный квантор регэкспа (ReDoS)
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: "*" подан как безобидное умножение внутри поля фильтра
  D2: "%2A" как «безопасный» кодированный текст с поздним декодированием
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: обход аутентификации wildcard в LDAP-bind
  E2: N/A — вектор: раскрытие glob в вектор аргументов shell
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: "*" — всегда умножение
  EXPECTED: FAIL_MULTIPLY_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: wildcard не может быть опасен
  EXPECTED: FAIL_WILDCARD_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: "*" в LDAP просто значит, что поле присутствует
  EXPECTED: FAIL_LDAP_FILTER_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%2A" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: фильтр по ASCII "*" ловит все похожие звёздочки
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: наличие "*" доказывает санитизацию ввода
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как экранировать "*" по контексту (LDAP/glob/регэксп/SQL) без ложных срабатываний на умножении/сносках/Markdown?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (экранирование LDAP-фильтра + отключение glob/закавычивание + таймаут/экранирование регэкспа + параметризованный LIKE — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «безопасность '*' решается контекстом разбора/раскрытия».
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
