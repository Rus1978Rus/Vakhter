ЧАСТНЫЙ АВТОРСКИЙ ПРОЕКТ / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_LESS_THAN_U003C_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
DRAFT_NOTE: черновик для нашей работы (Vakhter). Русская версия авторитетна; EN — зеркало.

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
LIMITATION_STATEMENT (стандарт):
  CONVEYOR_PASS ≠ VALIDATION
  MODEL_CONSENSUS ≠ TRUTH
  INJECTION_TEST_PASS ≠ SECURITY_PROOF
  GUARDS_HOLD_FOR_TESTED_CASES ≠ FUTURE_GUARANTEE
  NO_ATTACK_FOUND ≠ NO_ATTACK_EXISTS

============================================================
2. META
============================================================
CARD_UID: SIGN_CORE_CARD_LESS_THAN_U003C_GEN3_v0_3_RU
CODEPOINT: U+003C
VISIBLE_FORM: <
UNICODE_NAME: LESS-THAN SIGN
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: меньше / открытие тега
CATEGORY_ROADMAP: INJ (открытие XSS-тега) · PHAGO: — (маскировка структуры)

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
VISIBLE_FORM: <
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: LESS_THAN_FORM ≠ EFFECT
SIGN_CATEGORY:
  - оператор сравнения «меньше» (a < b)
  - открытие тега HTML/XML (<script>, <div>)
  - редирект/heredoc ввода в shell (< file, << EOF)
  - обобщённая угловая скобка

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_TAG_SAFE — «<» не делает открытый тег безопасным (исполняет БРАУЗЕР, не «<»)
  2. NOT_COMPARISON_ONLY — «<» не всегда сравнение (в HTML-контексте это тег)
  3. NOT_ESCAPED_PROOF — присутствие «<» не значит, что он экранирован
  4. NOT_ENCODED_SAFE — «&lt;» может быть декодирован обратно в «<» позже
  5. NOT_AUTHORITY — «<» не подтверждает официальность
  6. NOT_EXECUTION_TRIGGER — сам по себе ничего не исполняет
  7. NOT_TRUST_SIGNAL — не повышает доверие
  8. NOT_HTML_CONTEXT_SAFE — тот же ввод безопасен в тексте, но опасен в HTML
  9. NOT_SANITIZED_PROOF — наличие «<» не значит, что вход санитизирован
  10. NOT_TEXT_LITERAL — «<» не всегда литеральный текст (может открывать разметку)
  11. NOT_OUTPUT_CONTEXT_PROOF — безопасность зависит от контекста вывода (HTML/атрибут/JS)

BASE_FORMULAS:
  LESS_THAN_FORM ≠ EFFECT
  LESS_THAN_FORM ≠ TAG_SAFETY_PROOF
  LESS_THAN_FORM ≠ COMPARISON_ONLY_PROOF
  LESS_THAN_FORM ≠ ESCAPED_PROOF
  LESS_THAN_FORM ≠ ENCODED_SAFETY_PROOF
  LESS_THAN_FORM ≠ AUTHORITY
  LESS_THAN_FORM ≠ EXECUTION_TRIGGER
  LESS_THAN_FORM ≠ TRUST_SIGNAL
  LESS_THAN_FORM ≠ HTML_CONTEXT_SAFETY_PROOF
  LESS_THAN_FORM ≠ SANITIZED_PROOF
  LESS_THAN_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: «<» (ZONE_1) имеет параллельные функции (сравнение, открытие тега, редирект ввода), сосуществующие без культурной прецессии. Полисемия стабильного знака.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1
  NOTE: математический/письменный знак без жестового предшественника; функция разметки наложена цифровой эпохой параллельно.

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
    INPUT: "5 < 10"
    CONTEXT: числовое сравнение
    EXPECTED: INFO
    RISK: NONE
    GUARD: LESS_THAN_FORM ≠ COMPARISON_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: "if (i < n)"
    CONTEXT: сравнение в коде
    EXPECTED: INFO
    RISK: NONE
    GUARD: LESS_THAN_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "цена < 100 рублей"
    CONTEXT: сравнение в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: LESS_THAN_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "&lt;div&gt; (показано как текст)"
    CONTEXT: entity-кодирование, отображается как текст, не как тег
    EXPECTED: INFO
    RISK: NONE
    GUARD: LESS_THAN_FORM ≠ ENCODED_SAFETY_PROOF
  SAFE_CASE_005:
    INPUT: "x <= y"
    CONTEXT: оператор «меньше либо равно»
    EXPECTED: INFO
    RISK: NONE
    GUARD: LESS_THAN_FORM ≠ EFFECT
  SAFE_CASE_006:
    INPUT: "a < b и b < c"
    CONTEXT: цепочка сравнений
    EXPECTED: INFO
    RISK: NONE
    GUARD: LESS_THAN_FORM ≠ COMPARISON_ONLY_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: XSS_SCRIPT_TAG
    INPUT: "<script>alert(document.cookie)</script>"
    CONTEXT: пользовательский ввод попадает в HTML без экранирования
    RISK: CRITICAL
    ATTACK: «<» открывает тег <script>; браузер исполняет его как код (XSS)
    GUARD: LESS_THAN_FORM ≠ HTML_CONTEXT_SAFETY_PROOF
  RISK_CASE_002:
    NAME: XSS_EVENT_HANDLER
    INPUT: "<img src=x onerror=alert(1)>"
    CONTEXT: тег с обработчиком события
    RISK: CRITICAL
    ATTACK: «<img …onerror>» исполняет JS без <script>
    GUARD: LESS_THAN_FORM ≠ SANITIZED_PROOF
  RISK_CASE_003:
    NAME: XSS_SVG_ONLOAD
    INPUT: "<svg onload=alert(1)>"
    CONTEXT: SVG-тег с onload
    RISK: HIGH
    ATTACK: <svg onload> обходит фильтры, ищущие только <script>
    GUARD: LESS_THAN_FORM ≠ TAG_SAFETY_PROOF
  RISK_CASE_004:
    NAME: ENCODED_TAG_BYPASS
    INPUT: "&lt;script&gt; (с последующим двойным декодом)"
    CONTEXT: кодированный тег, декодируемый обратно до вывода
    RISK: HIGH
    ATTACK: &lt; декодируется в «<» ПОСЛЕ проверки → тег оживает
    GUARD: LESS_THAN_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: ATTRIBUTE_BREAKOUT
    INPUT: 'value"><script>…'
    CONTEXT: выход из атрибута через «>» и открытие нового тега «<»
    RISK: CRITICAL
    ATTACK: закрытие атрибута/тега и «<script>» инъектирует новый тег
    GUARD: LESS_THAN_FORM ≠ OUTPUT_CONTEXT_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_LT_BYPASS
    INPUT: "＜script＞ (полноширинные ＜ U+FF1C)"
    CONTEXT: двойник-угол для обхода фильтра тегов
    RISK: MEDIUM
    ATTACK: фильтр ищет ASCII «<», нормализатор может привести ＜ к «<»
    GUARD: LESS_THAN_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ＜
    CODEPOINT: U+FF1C
    NAME: FULLWIDTH LESS-THAN SIGN
    RISK: HIGH
    RULE: FULLWIDTH_LESS_THAN ≠ LESS_THAN (обход фильтра тегов, ищущего ASCII «<»)
  CONFUSABLE_002:
    VISIBLE_FORM: ‹
    CODEPOINT: U+2039
    NAME: SINGLE LEFT-POINTING ANGLE QUOTATION MARK
    RISK: MEDIUM
    RULE: SINGLE_LEFT_ANGLE_QUOTE ≠ LESS_THAN
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨
    CODEPOINT: U+27E8
    NAME: MATHEMATICAL LEFT ANGLE BRACKET
    RISK: LOW
    RULE: MATH_LEFT_ANGLE ≠ LESS_THAN
  CONFUSABLE_004:
    VISIBLE_FORM: 〈
    CODEPOINT: U+3008
    NAME: LEFT ANGLE BRACKET
    RISK: LOW
    RULE: CJK_LEFT_ANGLE ≠ LESS_THAN
  CONFUSABLE_005:
    VISIBLE_FORM: ˂
    CODEPOINT: U+02C2
    NAME: MODIFIER LETTER LEFT ARROWHEAD
    RISK: LOW
    RULE: LEFT_ARROWHEAD ≠ LESS_THAN

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: «раз ввод дошёл до вывода, „<“ уже безопасен»
    RESPONSE: LESS_THAN_FORM ≠ HTML_CONTEXT_SAFETY_PROOF
    RULE: безопасность зависит от контекста вывода; экранировать по контексту (HTML/атрибут/JS)
  CG2:
    TRIGGER: «„<“ — это всегда сравнение»
    RESPONSE: LESS_THAN_FORM ≠ COMPARISON_ONLY_PROOF
    RULE: в HTML-контексте «<» открывает тег, не сравнивает
  CG3:
    TRIGGER: «фильтр по „<script>“ ловит все XSS»
    RESPONSE: LESS_THAN_FORM ≠ TAG_SAFETY_PROOF
    RULE: <img onerror>, <svg onload> исполняют JS без <script>
  CG4:
    TRIGGER: «„&lt;“ навсегда безопасен»
    RESPONSE: LESS_THAN_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: entity может декодироваться обратно в «<» до вывода
  CG5:
    TRIGGER: «ASCII-фильтр по „<“ ловит все угловые»
    RESPONSE: LESS_THAN_FORM ≠ EFFECT
    RULE: полноширинный ＜ (U+FF1C) — другой кодпоинт
  CG6:
    TRIGGER: «наличие „<“ значит, что вход санитизирован»
    RESPONSE: LESS_THAN_FORM ≠ SANITIZED_PROOF
    RULE: присутствие знака ничего не говорит о санитизации

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "<script"
      NAME: SCRIPT_TAG_OPEN
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: открытие исполняемого тега; классический XSS
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "</"
      NAME: TAG_CLOSE
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: закрытие тега; выход из текстового контекста (</textarea> и т.п.)
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "<!--"
      NAME: HTML_COMMENT_OPEN
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: открытие комментария; условные комментарии / манипуляция парсером
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — последовательности с «<» ключевы для разметки/XSS.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: «<» маскирует/открывает СТРУКТУРУ разметки (тег), но не имитирует существование проверенной сущности (бренда/аккаунта). Риски — инъекция/исполнение, не entity-mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена ASCII «<» на полноширинный ＜ (U+FF1C) для обхода фильтра тегов
  A2: смешение «<» с ‹ (U+2039) в фильтре
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: <script>/<img onerror> в HTML-контексте (XSS)
  B2: выход из атрибута value"><script>
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: «<script» (SC1) как открытие исполняемого тега
  C2: «</textarea>» для выхода из текстового контекста
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: <svg onload> обходит фильтр, ищущий только <script>
  D2: «&lt;script&gt;» как «безопасный» кодированный текст с последующим декодом
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не носитель PHAGO; вектор: инъекция тега в шаблон
  E2: N/A — вектор: обход санитайзера двойником ＜
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет дремлющих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: раз ввод дошёл до вывода, «<» уже безопасен
  EXPECTED: FAIL_OUTPUT_CONTEXT_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: «<» — это всегда сравнение
  EXPECTED: FAIL_COMPARISON_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: фильтр по «<script>» ловит все XSS
  EXPECTED: FAIL_TAG_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: «&lt;» навсегда безопасен
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: ASCII-фильтр по «<» ловит все угловые двойники
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: наличие «<» доказывает санитизацию входа
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как экранировать «<» по контексту вывода (HTML-текст/атрибут/JS/URL) без ложных срабатываний на сравнение?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (контекстно-зависимое экранирование при выводе — уровень интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «безопасность „<“ определяется контекстом вывода».
ALL_OPEN_QUESTIONS_CLOSED: NO (делегирован, не блокирует)

============================================================
11. PATCH_HISTORY
============================================================
PATCH_HISTORY:
  v0_1_PATCH_01: первичное создание (Ruslan Malyavsky, 2026-07-21) — черновик по шаблону GEN3_v0_3 (Vakhter); не прогонялся через конвейер.
PATCHES_APPLIED: 1
PATCHES_VERIFIED: 0/1

============================================================
12. LIMITATION_STATEMENT
============================================================
LIMITATION_STATEMENT:
  THIS_CARD IS A WORKING_DRAFT ARTIFACT (до ARTIFACT_CONFIRMED)
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
