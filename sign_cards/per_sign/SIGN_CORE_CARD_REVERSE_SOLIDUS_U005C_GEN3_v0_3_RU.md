PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_REVERSE_SOLIDUS_U005C_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: Русский оригинал (authoritative). Английское зеркало — SIGN_CORE_CARD_REVERSE_SOLIDUS_U005C_GEN3_v0_3_EN. Кодпоинты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_REVERSE_SOLIDUS_U005C_GEN3_v0_3_RU
CODEPOINT: U+005C
VISIBLE_FORM: \
UNICODE_NAME: REVERSE SOLIDUS
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: обратная косая черта / символ экранирования
CATEGORY_ROADMAP: INJ (рассинхрон экранирования, обход каталогов) · PHAGO: — (нейтрализация разделителя)

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
VISIBLE_FORM: \
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: REVERSE_SOLIDUS_FORM ≠ EFFECT
SIGN_CATEGORY:
  - символ экранирования в строках/регэкспе (\n, \", \\)
  - разделитель путей Windows (C:\dir\file)
  - маркер продолжения строки (\ в конце строки)
  - экранирование метасимвола регэкспа (\. \d)

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_ESCAPE_ONLY — "\" не всегда безобидное экранирование (он может НЕЙТРАЛИЗОВАТЬ следующий разделитель)
  2. NOT_NEUTRALIZE_SAFE — экранирование может рассинхронизироваться между слоями декодирования (один видит данные, другой — разделитель)
  3. NOT_PATH_SEPARATOR_SAFE — "\" в пути может подниматься по каталогам (..\..\)
  4. NOT_ESCAPED_PROOF — ведущий "\" не доказывает, что следующий символ реально экранирован дальше по цепочке
  5. NOT_ENCODED_SAFE — "%5C" может быть раскодирован обратно в "\" позже
  6. NOT_AUTHORITY — "\" не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сам по себе ничего не исполняет; рассинхрон делает контекст
  8. NOT_TRUST_SIGNAL — не повышает доверие
  9. NOT_DOUBLE_BACKSLASH_SAFE — "\\" может свернуться в "\" и снова активировать следующее экранирование
  10. NOT_SANITIZED_PROOF — наличие "\" не значит, что ввод санитизирован
  11. NOT_OUTPUT_CONTEXT_PROOF — безопасность зависит от каждого слоя декодирования/разбора

BASE_FORMULAS:
  REVERSE_SOLIDUS_FORM ≠ EFFECT
  REVERSE_SOLIDUS_FORM ≠ ESCAPE_ONLY_PROOF
  REVERSE_SOLIDUS_FORM ≠ NEUTRALIZE_SAFETY_PROOF
  REVERSE_SOLIDUS_FORM ≠ PATH_SEPARATOR_SAFETY_PROOF
  REVERSE_SOLIDUS_FORM ≠ ESCAPED_PROOF
  REVERSE_SOLIDUS_FORM ≠ ENCODED_SAFETY_PROOF
  REVERSE_SOLIDUS_FORM ≠ AUTHORITY
  REVERSE_SOLIDUS_FORM ≠ EXECUTION_TRIGGER
  REVERSE_SOLIDUS_FORM ≠ DOUBLE_BACKSLASH_SAFETY_PROOF
  REVERSE_SOLIDUS_FORM ≠ SANITIZED_PROOF
  REVERSE_SOLIDUS_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: "\" (ZONE_1) имеет параллельные функции (экранирование строк, путь Windows, продолжение строки, экранирование регэкспа), сосуществующие без культурной прецессии. Полисемия стабильного знака.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1
  NOTE: ASCII-знак, введённый для вычислений, без жестового предшественника; функции экранирования/пути/продолжения надстроены цифровой эпохой параллельно.

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
    INPUT: "C:\\Users\\doc.txt"
    CONTEXT: обычный путь файла Windows
    EXPECTED: INFO
    RISK: NONE
    GUARD: REVERSE_SOLIDUS_FORM ≠ PATH_SEPARATOR_SAFETY_PROOF
  SAFE_CASE_002:
    INPUT: "line one \\n line two"
    CONTEXT: escape-последовательность, показанная как текст
    EXPECTED: INFO
    RISK: NONE
    GUARD: REVERSE_SOLIDUS_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "regex: \\d+"
    CONTEXT: класс цифр регэкспа (как литеральный текст)
    EXPECTED: INFO
    RISK: NONE
    GUARD: REVERSE_SOLIDUS_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "a long command \\ continued"
    CONTEXT: маркер продолжения строки shell
    EXPECTED: INFO
    RISK: NONE
    GUARD: REVERSE_SOLIDUS_FORM ≠ ESCAPE_ONLY_PROOF
  SAFE_CASE_005:
    INPUT: "the \\ key is above Enter"
    CONTEXT: название клавиши backslash в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: REVERSE_SOLIDUS_FORM ≠ EFFECT
  SAFE_CASE_006:
    INPUT: "path = home\\docs"
    CONTEXT: фрагмент относительного пути как текст
    EXPECTED: INFO
    RISK: NONE
    GUARD: REVERSE_SOLIDUS_FORM ≠ PATH_SEPARATOR_SAFETY_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: QUOTE_ESCAPE_DESYNC
    INPUT: 'value\\" OR 1=1 -- '
    CONTEXT: обратный слэш заставляет декодер неверно обработать следующую кавычку
    RISK: CRITICAL
    ATTACK: один слой видит \\" как экранированную кавычку, следующий видит " как разделитель → SQLi
    GUARD: REVERSE_SOLIDUS_FORM ≠ NEUTRALIZE_SAFETY_PROOF
  RISK_CASE_002:
    NAME: PATH_TRAVERSAL
    INPUT: "..\\..\\..\\windows\\win.ini"
    CONTEXT: подъём по каталогам с разделителями backslash
    RISK: HIGH
    ATTACK: "..\\" поднимается по дереву, чтобы читать файлы вне назначенного каталога
    GUARD: REVERSE_SOLIDUS_FORM ≠ PATH_SEPARATOR_SAFETY_PROOF
  RISK_CASE_003:
    NAME: DOUBLE_BACKSLASH_COLLAPSE
    INPUT: 'input\\\\" (\\\\ сворачивается в \\, снова активируя кавычку)'
    CONTEXT: чётное число backslash сворачивается, оставляя живую кавычку
    RISK: HIGH
    ATTACK: "\\\\" декодируется в "\\", поэтому следующая " НЕ экранирована дальше по цепочке
    GUARD: REVERSE_SOLIDUS_FORM ≠ DOUBLE_BACKSLASH_SAFETY_PROOF
  RISK_CASE_004:
    NAME: REGEX_METACHAR_UNESCAPE
    INPUT: "\\Qinjected\\E (злоупотребление quote-блоком регэкспа)"
    CONTEXT: манипуляция экранированием регэкспа для смены семантики совпадения
    RISK: MEDIUM
    ATTACK: "\\Q...\\E" или лишний "\\" меняет то, что совпадает в allow-list-регэкспе
    GUARD: REVERSE_SOLIDUS_FORM ≠ EFFECT
  RISK_CASE_005:
    NAME: ENCODED_BACKSLASH_BYPASS
    INPUT: "..%5C..%5Cwin.ini (с поздним декодированием)"
    CONTEXT: кодированный "\" декодируется обратно в разделитель пути после проверки
    RISK: HIGH
    ATTACK: %5C декодируется в "\" ПОСЛЕ валидации → обход каталогов
    GUARD: REVERSE_SOLIDUS_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: FULLWIDTH_BACKSLASH_BYPASS
    INPUT: "..＼..＼win.ini (полноширинный ＼ U+FF3C)"
    CONTEXT: похожий знак для обхода фильтра "\"
    RISK: MEDIUM
    ATTACK: фильтр ищет ASCII "\", нормализатор может свернуть ＼ в "\"
    GUARD: REVERSE_SOLIDUS_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ＼
    CODEPOINT: U+FF3C
    NAME: FULLWIDTH REVERSE SOLIDUS
    RISK: HIGH
    RULE: FULLWIDTH_REVERSE_SOLIDUS ≠ REVERSE_SOLIDUS (обходит фильтр, ищущий ASCII "\")
  CONFUSABLE_002:
    VISIBLE_FORM: ﹨
    CODEPOINT: U+FE68
    NAME: SMALL REVERSE SOLIDUS
    RISK: MEDIUM
    RULE: SMALL_REVERSE_SOLIDUS ≠ REVERSE_SOLIDUS
  CONFUSABLE_003:
    VISIBLE_FORM: ⧵
    CODEPOINT: U+29F5
    NAME: REVERSE SOLIDUS OPERATOR
    RISK: MEDIUM
    RULE: REVERSE_SOLIDUS_OPERATOR ≠ REVERSE_SOLIDUS
  CONFUSABLE_004:
    VISIBLE_FORM: ∖
    CODEPOINT: U+2216
    NAME: SET MINUS
    RISK: LOW
    RULE: SET_MINUS ≠ REVERSE_SOLIDUS
  CONFUSABLE_005:
    VISIBLE_FORM: ⧹
    CODEPOINT: U+29F9
    NAME: BIG REVERSE SOLIDUS
    RISK: LOW
    RULE: BIG_REVERSE_SOLIDUS ≠ REVERSE_SOLIDUS

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "'\\' — это всегда безобидное экранирование"
    RESPONSE: REVERSE_SOLIDUS_FORM ≠ ESCAPE_ONLY_PROOF
    RULE: экранирование может нейтрализовать следующий разделитель и рассинхронизировать декодеры
  CG2:
    TRIGGER: "экранирование кавычки всегда делает её безопасной"
    RESPONSE: REVERSE_SOLIDUS_FORM ≠ NEUTRALIZE_SAFETY_PROOF
    RULE: следующий слой может не соблюдать экранирование; считать backslash на каждом слое
  CG3:
    TRIGGER: "'\\' в пути — это просто разделитель"
    RESPONSE: REVERSE_SOLIDUS_FORM ≠ PATH_SEPARATOR_SAFETY_PROOF
    RULE: "..\\" может выйти за пределы назначенного каталога
  CG4:
    TRIGGER: "'%5C' / '\\\\' безопасен навсегда"
    RESPONSE: REVERSE_SOLIDUS_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная/удвоенная форма может свернуться обратно в "\" дальше по цепочке
  CG5:
    TRIGGER: "фильтр по ASCII '\\' ловит все обратные слэши"
    RESPONSE: REVERSE_SOLIDUS_FORM ≠ EFFECT
    RULE: полноширинный ＼ (U+FF3C) — другой кодпоинт
  CG6:
    TRIGGER: "наличие '\\' значит, что ввод санитизирован"
    RESPONSE: REVERSE_SOLIDUS_FORM ≠ SANITIZED_PROOF
    RULE: наличие знака ничего не говорит о санитизации

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: '\\"'
      NAME: ESCAPE_DESYNC
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: обратный слэш-кавычка, обрабатываемый по-разному разными декодерами
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "..\\"
      NAME: PATH_TRAVERSAL
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: подъём по каталогам через разделители backslash
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "\\\\"
      NAME: DOUBLE_COLLAPSE
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: чётное число backslash, сворачивающееся для повторной активации следующего разделителя
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — последовательности с "\" центральны для рассинхрона экранирования и обхода каталогов.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: "\" экранирует/нейтрализует разделители или разделяет пути, но не имитирует существование верифицированной сущности. Его риски — рассинхрон/обход каталогов, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена ASCII "\" на полноширинный ＼ (U+FF3C) для обхода фильтра
  A2: замена на reverse-solidus operator ⧵ (U+29F5)
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: рассинхрон экранирования value\\" OR 1=1 --
  B2: обход каталогов ..\\..\\..\\windows\\win.ini
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: '\\"' (SC1) — рассинхрон экранирования
  C2: "\\\\" (SC3) — сворачивание двойного backslash
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: "\" подан как безобидный разделитель пути внутри поля инъекции
  D2: "%5C" как «безопасный» кодированный текст с поздним декодированием
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: рассинхрон экранирования в построитель запросов
  E2: N/A — вектор: обход каталогов через кодированный backslash в файловый API
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: "\" — всегда безобидное экранирование
  EXPECTED: FAIL_ESCAPE_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: экранирование кавычки всегда делает её безопасной
  EXPECTED: FAIL_NEUTRALIZE_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: "\" в пути — это просто разделитель
  EXPECTED: FAIL_PATH_SEPARATOR_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%5C" / "\\\\" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: фильтр по ASCII "\" ловит все похожие обратные слэши
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: наличие "\" доказывает санитизацию ввода
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как считать/нормализовать "\" на каждом слое декодирования (SQL/JSON/путь) без ложных срабатываний на путях Windows/регэкспе/экранировании?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (послойная канонизация + параметризованные запросы + канонизация-затем-проверка пути — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «безопасность '\' решается на каждом слое декодирования/разбора».
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
