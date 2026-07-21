ЧАСТНЫЙ АВТОРСКИЙ ПРОЕКТ / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_PERCENT_U0025_GEN3_v0_3_RU
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
CARD_UID: SIGN_CORE_CARD_PERCENT_U0025_GEN3_v0_3_RU
CODEPOINT: U+0025
VISIBLE_FORM: %
UNICODE_NAME: PERCENT SIGN
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: процент
CATEGORY_ROADMAP: PH/INJ (URL-обфускация) · PHAGO: — (маскировка структуры, не имитация сущности)

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
VISIBLE_FORM: %
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_ENCODING_MARKER
BASE_MODE_FORMULA: PERCENT_FORM ≠ EFFECT
SIGN_CATEGORY:
  - пунктуация / математический знак (проценты, «50%»)
  - оператор modulo в языках программирования (a % b)
  - маркер percent-кодирования в URL (%XX)
  - спецификатор формата (printf «%s», «%d»)

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_DECODED_SAFE — присутствие %XX не значит, что декодированное значение безопасно
  2. NOT_SINGLE_DECODE_GUARANTEE — вход может быть закодирован дважды (%252F → %2F → /)
  3. NOT_ALWAYS_ENCODING — «%» не всегда percent-кодирование (проценты, modulo, формат)
  4. NOT_PERCENTAGE_PROOF — «%» не доказывает корректность процентного значения
  5. NOT_MODULO_SAFE — «%» как modulo не гарантирует безопасность выражения
  6. NOT_FORMAT_STRING_SAFE — «%s»/«%n» — вектор format-string, не безопасность
  7. NOT_AUTHORITY — «%» не подтверждает официальность
  8. NOT_EXECUTION_TRIGGER — сам по себе ничего не запускает
  9. NOT_TRUST_SIGNAL — не повышает доверие
  10. NOT_STRING_TERMINATION_SAFE — %00 может обрывать строку (null-byte)
  11. NOT_TRAVERSAL_SAFE — %2e%2e%2f может нести обход пути

BASE_FORMULAS:
  PERCENT_FORM ≠ EFFECT
  PERCENT_FORM ≠ DECODED_VALUE_SAFETY_PROOF
  PERCENT_FORM ≠ SINGLE_DECODE_GUARANTEE
  PERCENT_FORM ≠ ENCODING_ONLY_PROOF
  PERCENT_FORM ≠ PERCENTAGE_VALIDITY_PROOF
  PERCENT_FORM ≠ MODULO_SAFETY_PROOF
  PERCENT_FORM ≠ FORMAT_STRING_SAFETY_PROOF
  PERCENT_FORM ≠ AUTHORITY
  PERCENT_FORM ≠ TRUST_SIGNAL
  PERCENT_FORM ≠ STRING_TERMINATION_SAFETY
  PERCENT_FORM ≠ PATH_TRAVERSAL_SAFETY

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: «%» (ZONE_1) имеет параллельные функции (проценты, modulo, percent-кодирование, спецификатор формата), сосуществующие без культурной прецессии. Полисемия стабильного знака, не смена эпох.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1
  NOTE: письменный/типографический знак без жестового предшественника; percent-кодирование — цифровая функция, наложенная позже (RFC 3986), но параллельно математическому смыслу.

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
    INPUT: "скидка 50%"
    CONTEXT: процентное значение в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: PERCENT_FORM ≠ PERCENTAGE_VALIDITY_PROOF
  SAFE_CASE_002:
    INPUT: "загрузка 100%"
    CONTEXT: индикатор прогресса
    EXPECTED: INFO
    RISK: NONE
    GUARD: PERCENT_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "остаток = a % b"
    CONTEXT: modulo в выражении
    EXPECTED: INFO
    RISK: NONE
    GUARD: PERCENT_FORM ≠ MODULO_SAFETY_PROOF
  SAFE_CASE_004:
    INPUT: "https://site.com/path%20name"
    CONTEXT: легит percent-кодирование пробела (%20) в URL
    EXPECTED: INFO
    RISK: NONE
    GUARD: PERCENT_FORM ≠ ENCODING_ONLY_PROOF
  SAFE_CASE_005:
    INPUT: 'printf("%s", name)'
    CONTEXT: корректный спецификатор формата с аргументом
    EXPECTED: INFO
    RISK: NONE
    GUARD: PERCENT_FORM ≠ FORMAT_STRING_SAFETY_PROOF
  SAFE_CASE_006:
    INPUT: "рост на 3% в год"
    CONTEXT: процент в статистике
    EXPECTED: INFO
    RISK: NONE
    GUARD: PERCENT_FORM ≠ PERCENTAGE_VALIDITY_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: ENCODED_SLASH_BYPASS
    INPUT: "/api/%2F..%2Fadmin"
    CONTEXT: percent-кодированный слэш обходит фильтр пути
    RISK: HIGH
    ATTACK: %2F декодируется в «/» ПОСЛЕ проверки, обходя фильтр по литеральному слэшу
    GUARD: PERCENT_FORM ≠ DECODED_VALUE_SAFETY_PROOF
  RISK_CASE_002:
    NAME: NULL_BYTE_TRUNCATION
    INPUT: "file.php%00.jpg"
    CONTEXT: %00 обрывает строку в уязвимом парсере
    RISK: CRITICAL
    ATTACK: null-byte (%00) отсекает «.jpg», оставляя «.php» — обход проверки расширения
    GUARD: PERCENT_FORM ≠ STRING_TERMINATION_SAFETY
  RISK_CASE_003:
    NAME: DOUBLE_ENCODING
    INPUT: "%252F" (двойное кодирование «/»)
    CONTEXT: обход одноразового декодирования
    RISK: HIGH
    ATTACK: %25 → %, затем %2F → / на втором проходе; одноразовый декод не видит слэш
    GUARD: PERCENT_FORM ≠ SINGLE_DECODE_GUARANTEE
  RISK_CASE_004:
    NAME: ENCODED_TRAVERSAL
    INPUT: "%2e%2e%2fetc%2fpasswd"
    CONTEXT: percent-кодированный обход пути (../../)
    RISK: HIGH
    ATTACK: кодирование точек/слэшей уводит traversal из-под сигнатурного фильтра
    GUARD: PERCENT_FORM ≠ PATH_TRAVERSAL_SAFETY
  RISK_CASE_005:
    NAME: CRLF_INJECTION_ENCODED
    INPUT: "name=x%0d%0aSet-Cookie:evil"
    CONTEXT: percent-кодированные CR/LF для расщепления заголовка/лога
    RISK: HIGH
    ATTACK: %0d%0a декодируются в CRLF, внедряя заголовок/строку лога
    GUARD: PERCENT_FORM ≠ DECODED_VALUE_SAFETY_PROOF
  RISK_CASE_006:
    NAME: FORMAT_STRING_ATTACK
    INPUT: 'user input: "%n%n%s"'
    CONTEXT: пользовательский ввод как строка формата
    RISK: HIGH
    ATTACK: %n/%s без аргументов — чтение/запись памяти (format-string уязвимость)
    GUARD: PERCENT_FORM ≠ FORMAT_STRING_SAFETY_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ％
    CODEPOINT: U+FF05
    NAME: FULLWIDTH PERCENT SIGN
    RISK: MEDIUM
    RULE: FULLWIDTH_PERCENT ≠ PERCENT (обход фильтра, ищущего ASCII %)
  CONFUSABLE_002:
    VISIBLE_FORM: ٪
    CODEPOINT: U+066A
    NAME: ARABIC PERCENT SIGN
    RISK: MEDIUM
    RULE: ARABIC_PERCENT ≠ PERCENT
  CONFUSABLE_003:
    VISIBLE_FORM: ﹪
    CODEPOINT: U+FE6A
    NAME: SMALL PERCENT SIGN
    RISK: LOW
    RULE: SMALL_PERCENT ≠ PERCENT
  CONFUSABLE_004:
    VISIBLE_FORM: ‰
    CODEPOINT: U+2030
    NAME: PER MILLE SIGN
    RISK: LOW
    RULE: PER_MILLE ≠ PERCENT (промилле, иная величина)
  CONFUSABLE_005:
    VISIBLE_FORM: ⁒
    CODEPOINT: U+2052
    NAME: COMMERCIAL MINUS SIGN
    RISK: LOW
    RULE: COMMERCIAL_MINUS ≠ PERCENT (визуально схож в части шрифтов)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: «если строка percent-декодирована один раз, она безопасна»
    RESPONSE: PERCENT_FORM ≠ SINGLE_DECODE_GUARANTEE
    RULE: возможно двойное/множественное кодирование; декодировать до стабильной точки, затем проверять
  CG2:
    TRIGGER: «%2F в пути — это просто текст, не слэш»
    RESPONSE: PERCENT_FORM ≠ DECODED_VALUE_SAFETY_PROOF
    RULE: после декодирования %2F становится «/» — проверять ДЕКОДИРОВАННОЕ значение
  CG3:
    TRIGGER: «%00 в имени файла безвреден»
    RESPONSE: PERCENT_FORM ≠ STRING_TERMINATION_SAFETY
    RULE: null-byte может обрывать строку в уязвимом парсере (file.php%00.jpg)
  CG4:
    TRIGGER: «пользовательский ввод можно передать как строку формата»
    RESPONSE: PERCENT_FORM ≠ FORMAT_STRING_SAFETY_PROOF
    RULE: %n/%s во вводе — format-string уязвимость; ввод не должен быть строкой формата
  CG5:
    TRIGGER: «фильтр по ASCII % поймает все проценты»
    RESPONSE: PERCENT_FORM ≠ EFFECT
    RULE: полноширинный ％ / арабский ٪ — другие кодпоинты (см. CONFUSABLES)
  CG6:
    TRIGGER: «наличие % значит percent-кодирование»
    RESPONSE: PERCENT_FORM ≠ ENCODING_ONLY_PROOF
    RULE: % это ещё проценты, modulo и формат; интерпретация зависит от контекста

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "%XX" (% + две hex-цифры)
      NAME: PERCENT_ENCODED_OCTET
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: percent-кодированный байт; опасность зависит от декодированного значения (%2F, %00, %0a)
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "%25XX"
      NAME: DOUBLE_ENCODED_OCTET
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: двойное кодирование для обхода одноразового декода
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "%00"
      NAME: NULL_BYTE
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: обрыв строки, обход проверки расширения/пути
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — последовательности реальны и ключевы для этого знака.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: «%» маскирует СТРУКТУРУ (кодирование, обход фильтров), но не имитирует существование проверенной сущности (бренда/аккаунта). Риски знака — обфускация, не entity-mimicry.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена ASCII % на полноширинный ％ (U+FF05) для обхода фильтра кодирования
  A2: смешение % с арабским ٪ (U+066A) в multibyte-контексте
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: %2F/%2e%2e для обхода фильтра пути после декодирования
  B2: %0d%0a для CRLF-инъекции в заголовок/лог
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: двойное кодирование %252F (SC2) против одноразового декода
  C2: %00 (SC3) для обрыва строки и обхода расширения
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: пользовательский ввод как строка формата «%n%s» (format-string)
  D2: «100%» как псевдо-гарантия («100% безопасно») — инфляция доверия числом
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не носитель PHAGO; вектор заменён на обфускацию: %-кодирование ключевого слова из blocklist
  E2: N/A — вектор: %-кодирование управляющего символа для обхода санитайзера
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет дремлющих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: однократного percent-декодирования достаточно для безопасности
  EXPECTED: FAIL_SINGLE_DECODE_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: %2F в пути — просто текст, не слэш
  EXPECTED: FAIL_DECODED_VALUE_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: %00 в имени файла безвреден
  EXPECTED: FAIL_NULL_BYTE_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: пользовательский ввод можно передать как строку формата
  EXPECTED: FAIL_FORMAT_STRING_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: ASCII-фильтр по % ловит все варианты знака
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: «100% безопасно» подтверждается знаком процента
  EXPECTED: FAIL_TRUST_INFLATION_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: до какой глубины декодировать перед проверкой (риск decode-бомбы)?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (политика итеративного декода до стабильной точки с лимитом — уровень рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «проверять декодированное значение, а не сырой %XX».
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
