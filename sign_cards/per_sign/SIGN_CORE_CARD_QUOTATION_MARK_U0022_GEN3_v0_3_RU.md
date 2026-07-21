PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_QUOTATION_MARK_U0022_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: Русский оригинал (authoritative). Английское зеркало — SIGN_CORE_CARD_QUOTATION_MARK_U0022_GEN3_v0_3_EN. Кодпоинты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_QUOTATION_MARK_U0022_GEN3_v0_3_RU
CODEPOINT: U+0022
VISIBLE_FORM: "
UNICODE_NAME: QUOTATION MARK
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: двойная кавычка / разделитель строки
CATEGORY_ROADMAP: INJ (разрыв атрибута/строки в HTML/SQL/JSON) · PHAGO: — (пробой разделителя)

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
VISIBLE_FORM: "
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: QUOTATION_MARK_FORM ≠ EFFECT
SIGN_CATEGORY:
  - разделитель строкового литерала ("text")
  - разделитель значения HTML-атрибута (attr="value")
  - разделитель ключа/значения JSON ({"k":"v"})
  - типографская кавычка прямой речи ("hi")

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_STRING_CLOSE_SAFE — '"' закрывает строку/атрибут; само закрытие открывает контекст пробоя
  2. NOT_QUOTE_ONLY — '"' не всегда литературная кавычка (в коде это разделитель, который ломает значение)
  3. NOT_ESCAPED_PROOF — наличие '"' не значит, что он экранирован (\")
  4. NOT_ENCODED_SAFE — "&quot;" или %22 могут быть раскодированы обратно в '"' позже
  5. NOT_AUTHORITY — '"' не подтверждает официальность
  6. NOT_EXECUTION_TRIGGER — сам по себе ничего не исполняет
  7. NOT_TRUST_SIGNAL — не повышает доверие
  8. NOT_ATTRIBUTE_SAFE — '"' может закрыть значение атрибута и вырваться в контекст тега
  9. NOT_SQL_SAFE — '"' может сломать границу идентификатора/строки в некоторых диалектах SQL
  10. NOT_SANITIZED_PROOF — наличие '"' не значит, что ввод санитизирован
  11. NOT_OUTPUT_CONTEXT_PROOF — безопасность зависит от контекста вывода (HTML/JS/SQL/JSON)
  12. NOT_SMART_QUOTE_EQUIVALENT — фигурная “ ” — другой кодпоинт, не этот разделитель

BASE_FORMULAS:
  QUOTATION_MARK_FORM ≠ EFFECT
  QUOTATION_MARK_FORM ≠ STRING_CLOSE_SAFETY_PROOF
  QUOTATION_MARK_FORM ≠ QUOTE_ONLY_PROOF
  QUOTATION_MARK_FORM ≠ ESCAPED_PROOF
  QUOTATION_MARK_FORM ≠ ENCODED_SAFETY_PROOF
  QUOTATION_MARK_FORM ≠ AUTHORITY
  QUOTATION_MARK_FORM ≠ EXECUTION_TRIGGER
  QUOTATION_MARK_FORM ≠ TRUST_SIGNAL
  QUOTATION_MARK_FORM ≠ ATTRIBUTE_SAFETY_PROOF
  QUOTATION_MARK_FORM ≠ SANITIZED_PROOF
  QUOTATION_MARK_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: '"' (ZONE_1) имеет параллельные функции (литературная кавычка, разделитель строки/атрибута/JSON), сосуществующие без культурной прецессии. Полисемия стабильного знака.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1
  NOTE: письменно-типографский знак без жестового предшественника; функции кода-разделителя надстроены цифровой эпохой параллельно.

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
    INPUT: 'say "hello"'
    CONTEXT: литературная кавычка в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: QUOTATION_MARK_FORM ≠ QUOTE_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: 'attr="value"'
    CONTEXT: корректно закрытый HTML-атрибут
    EXPECTED: INFO
    RISK: NONE
    GUARD: QUOTATION_MARK_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: '{"k":"v"}'
    CONTEXT: корректный JSON
    EXPECTED: INFO
    RISK: NONE
    GUARD: QUOTATION_MARK_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: 'width="100"'
    CONTEXT: числовое значение атрибута
    EXPECTED: INFO
    RISK: NONE
    GUARD: QUOTATION_MARK_FORM ≠ ATTRIBUTE_SAFETY_PROOF
  SAFE_CASE_005:
    INPUT: 'She said "hi" and left'
    CONTEXT: цитата речи в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: QUOTATION_MARK_FORM ≠ QUOTE_ONLY_PROOF
  SAFE_CASE_006:
    INPUT: 'print("done")'
    CONTEXT: корректно закрытый строковый литерал в коде
    EXPECTED: INFO
    RISK: NONE
    GUARD: QUOTATION_MARK_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: ATTRIBUTE_BREAKOUT
    INPUT: '" onmouseover="alert(1)'
    CONTEXT: закрытие значения атрибута и внедрение нового атрибута-обработчика
    RISK: CRITICAL
    ATTACK: '"' закрывает значение, затем внедряется новый атрибут (onmouseover) → XSS
    GUARD: QUOTATION_MARK_FORM ≠ OUTPUT_CONTEXT_PROOF
  RISK_CASE_002:
    NAME: ATTRIBUTE_TAG_BREAKOUT
    INPUT: '"><script>alert(1)</script>'
    CONTEXT: закрытие атрибута и тега, затем открытие нового тега
    RISK: CRITICAL
    ATTACK: '"' закрывает значение, ">" закрывает тег, "<script>" внедряется (XSS)
    GUARD: QUOTATION_MARK_FORM ≠ ATTRIBUTE_SAFETY_PROOF
  RISK_CASE_003:
    NAME: SQL_STRING_BREAK
    INPUT: '" OR "1"="1'
    CONTEXT: пробой границы строки/идентификатора в двойных кавычках SQL
    RISK: CRITICAL
    ATTACK: '"' закрывает литерал и внедряет всегда-истинную логику (SQLi в диалектах с ")
    GUARD: QUOTATION_MARK_FORM ≠ EFFECT
  RISK_CASE_004:
    NAME: JSON_INJECTION
    INPUT: '","admin":true,"x":"'
    CONTEXT: закрытие значения JSON и внедрение нового ключа
    RISK: HIGH
    ATTACK: '"' закрывает значение; в объект внедряется поддельный ключ "admin":true
    GUARD: QUOTATION_MARK_FORM ≠ OUTPUT_CONTEXT_PROOF
  RISK_CASE_005:
    NAME: ESCAPE_DESYNC
    INPUT: '\\" (обратный слэш-кавычка, декодируется несогласованно)'
    CONTEXT: экранированная кавычка, которую один слой считает литералом, а другой — разделителем
    RISK: HIGH
    ATTACK: \" переживает один декодер, но закрывает строку в следующем → рассинхрон границы
    GUARD: QUOTATION_MARK_FORM ≠ ESCAPED_PROOF
  RISK_CASE_006:
    NAME: SMART_QUOTE_BYPASS
    INPUT: '“ onmouseover=alert(1) (фигурная “ U+201C)'
    CONTEXT: похожая кавычка для обхода фильтра, позже свёрнутая в '"'
    RISK: MEDIUM
    ATTACK: фильтр ищет ASCII '"', нормализатор может свернуть “ в '"' после проверки
    GUARD: QUOTATION_MARK_FORM ≠ ENCODED_SAFETY_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ＂
    CODEPOINT: U+FF02
    NAME: FULLWIDTH QUOTATION MARK
    RISK: HIGH
    RULE: FULLWIDTH_QUOTATION_MARK ≠ QUOTATION_MARK (обходит фильтр, ищущий ASCII '"')
  CONFUSABLE_002:
    VISIBLE_FORM: “
    CODEPOINT: U+201C
    NAME: LEFT DOUBLE QUOTATION MARK
    RISK: MEDIUM
    RULE: LEFT_DOUBLE_QUOTE ≠ QUOTATION_MARK
  CONFUSABLE_003:
    VISIBLE_FORM: ”
    CODEPOINT: U+201D
    NAME: RIGHT DOUBLE QUOTATION MARK
    RISK: MEDIUM
    RULE: RIGHT_DOUBLE_QUOTE ≠ QUOTATION_MARK
  CONFUSABLE_004:
    VISIBLE_FORM: „
    CODEPOINT: U+201E
    NAME: DOUBLE LOW-9 QUOTATION MARK
    RISK: LOW
    RULE: DOUBLE_LOW9_QUOTE ≠ QUOTATION_MARK
  CONFUSABLE_005:
    VISIBLE_FORM: ″
    CODEPOINT: U+2033
    NAME: DOUBLE PRIME
    RISK: LOW
    RULE: DOUBLE_PRIME ≠ QUOTATION_MARK

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "'\"' — это всегда литературная кавычка"
    RESPONSE: QUOTATION_MARK_FORM ≠ QUOTE_ONLY_PROOF
    RULE: в коде '"' разделяет/ломает строку или атрибут, а не только цитирует речь
  CG2:
    TRIGGER: "раз ввод дошёл до вывода, '\"' уже безопасен"
    RESPONSE: QUOTATION_MARK_FORM ≠ OUTPUT_CONTEXT_PROOF
    RULE: безопасность зависит от контекста вывода; экранировать по контексту (HTML/JS/SQL/JSON)
  CG3:
    TRIGGER: "'\\\"' значит, что кавычка экранирована"
    RESPONSE: QUOTATION_MARK_FORM ≠ ESCAPED_PROOF
    RULE: экранирование может рассинхронизироваться между декодерами; следующий слой ещё увидит разделитель
  CG4:
    TRIGGER: "'&quot;' безопасен навсегда"
    RESPONSE: QUOTATION_MARK_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: сущность/percent-форма может быть раскодирована обратно в '"' перед выводом
  CG5:
    TRIGGER: "фильтр по ASCII '\"' ловит все кавычки"
    RESPONSE: QUOTATION_MARK_FORM ≠ EFFECT
    RULE: полноширинная ＂ (U+FF02) и фигурные “ ” — другие кодпоинты
  CG6:
    TRIGGER: "наличие '\"' значит, что ввод санитизирован"
    RESPONSE: QUOTATION_MARK_FORM ≠ SANITIZED_PROOF
    RULE: наличие знака ничего не говорит о санитизации

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: '">'
      NAME: ATTRIBUTE_TAG_BREAKOUT
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: закрытие атрибута и тега для внедрения нового тега
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: '" '
      NAME: ATTRIBUTE_INJECTION
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: закрытие значения и внедрение нового атрибута (onmouseover=)
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: '\\"'
      NAME: ESCAPE_DESYNC
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: обратный слэш-кавычка обрабатывается по-разному на разных слоях декодирования
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — последовательности с '"' центральны для пробоя атрибута/строки.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: '"' ломает/закрывает ГРАНИЦУ разделителя (строка/атрибут/JSON), но не имитирует существование верифицированной сущности. Его риски — инъекция/рассинхрон, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена ASCII '"' на полноширинную ＂ (U+FF02) для обхода фильтра
  A2: смешивание '"' с фигурными “ ” (U+201C/U+201D) в фильтре
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: пробой атрибута " onmouseover="alert(1)
  B2: пробой SQL-строки " OR "1"="1
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: '">' (SC1) — пробой атрибута и тега
  C2: '\\"' (SC3) — рассинхрон экранирования между декодерами
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: '","admin":true,"x":"' — внедрение ключа JSON
  D2: "&quot;" как «безопасный» кодированный текст с поздним декодированием
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: внедрение атрибута в шаблон
  E2: N/A — вектор: подделка объекта JSON через пробой разделителя
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: '"' — всегда литературная кавычка
  EXPECTED: FAIL_QUOTE_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: раз ввод дошёл до вывода, '"' уже безопасен
  EXPECTED: FAIL_OUTPUT_CONTEXT_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: '\"' доказывает, что кавычка нейтрализована
  EXPECTED: FAIL_ESCAPED_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "&quot;" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: фильтр по ASCII '"' ловит все похожие кавычки
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: наличие '"' доказывает санитизацию ввода
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как экранировать '"' по контексту (HTML-атрибут/JS-строка/SQL/JSON) без ложных срабатываний на литературной кавычке?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (контекстно-зависимое экранирование вывода + параметризованные запросы — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «безопасность '\"' решается контекстом вывода».
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
