PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_NULL_U0000_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: Русский оригинал (authoritative). Английское зеркало — SIGN_CORE_CARD_NULL_U0000_GEN3_v0_3_EN. Кодпоинты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_NULL_U0000_GEN3_v0_3_RU
CODEPOINT: U+0000
VISIBLE_FORM: ␀
UNICODE_NAME: <control> NULL (NUL)
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: нулевой байт / NUL (непечатаемый)
CATEGORY_ROADMAP: INJ (усечение null-байтом, обход фильтра) · PHAGO: — (подделка границы строки)
GLYPH_NOTE: VISIBLE_FORM использует ␀ (U+2400 SYMBOL FOR NULL) как печатаемую картинку; сам знак (U+0000) — непечатаемый управляющий символ.

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
VISIBLE_FORM: ␀
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: NULL_FORM ≠ EFFECT
SIGN_CATEGORY:
  - терминатор C-строки (конец null-terminated строки)
  - паддинг / байт-заполнитель в бинарных форматах
  - разделитель полей/записей в некоторых бинарных протоколах
  - sentinel «нет значения» в низкоуровневых данных

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_TERMINATOR_ONLY — NUL не просто безобидный конец строки (он может усечь провалидированное значение)
  2. NOT_TRUNCATION_SAFE — NUL может обрезать строку так, что проверенный суффикс отбрасывается у приёмника
  3. NOT_INVISIBLE_MEANS_HARMLESS — то, что он непечатаемый, не делает его инертным
  4. NOT_EMPTY_EQUIVALENT — NUL — это реальный байт, а не отсутствие данных
  5. NOT_ENCODED_SAFE — "%00" / "\\0" / "\\u0000" могут быть раскодированы обратно в NUL позже
  6. NOT_AUTHORITY — NUL не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сам по себе ничего не исполняет; усечение делает контекст
  8. NOT_TRUST_SIGNAL — не повышает доверие
  9. NOT_LANGUAGE_UNIFORM — один слой хранит байты после NUL, другой останавливается на нём (рассинхрон)
  10. NOT_SANITIZED_PROOF — наличие NUL не значит, что ввод санитизирован
  11. NOT_OUTPUT_CONTEXT_PROOF — безопасность зависит от того, как каждый слой обрабатывает NUL

BASE_FORMULAS:
  NULL_FORM ≠ EFFECT
  NULL_FORM ≠ TERMINATOR_ONLY_PROOF
  NULL_FORM ≠ TRUNCATION_SAFETY_PROOF
  NULL_FORM ≠ INVISIBLE_HARMLESS_PROOF
  NULL_FORM ≠ EMPTY_EQUIVALENCE_PROOF
  NULL_FORM ≠ ENCODED_SAFETY_PROOF
  NULL_FORM ≠ AUTHORITY
  NULL_FORM ≠ EXECUTION_TRIGGER
  NULL_FORM ≠ LANGUAGE_UNIFORMITY_PROOF
  NULL_FORM ≠ SANITIZED_PROOF
  NULL_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: NUL (ZONE_1) имеет параллельные функции (терминатор C-строки, паддинг, sentinel), сосуществующие без культурной прецессии. Полисемия стабильного управляющего кода.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1
  NOTE: телетайпный/idle управляющий код без жестового предшественника; функции терминатора строки/sentinel надстроены цифровой эпохой параллельно.

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
    INPUT: "strings end with \\0 in C"
    CONTEXT: NUL, показанный как escape в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: NULL_FORM ≠ TERMINATOR_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: "NUL is 0x00 in ASCII"
    CONTEXT: название управляющего кода в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: NULL_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the null terminator ends a C string"
    CONTEXT: описание роли терминатора в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: NULL_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "printf('%c', 0) writes a NUL"
    CONTEXT: пример кода, показанный как литеральный текст
    EXPECTED: INFO
    RISK: NONE
    GUARD: NULL_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "the file is NUL-padded to 512 bytes"
    CONTEXT: описание легитимного бинарного паддинга
    EXPECTED: INFO
    RISK: NONE
    GUARD: NULL_FORM ≠ TRUNCATION_SAFETY_PROOF
  SAFE_CASE_006:
    INPUT: "find -print0 uses NUL separators"
    CONTEXT: описание вывода инструмента с NUL-разделителями
    EXPECTED: INFO
    RISK: NONE
    GUARD: NULL_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: PATH_EXTENSION_TRUNCATION
    INPUT: "shell.php%00.jpg"
    CONTEXT: NUL усекает путь, обходя проверку расширения
    RISK: CRITICAL
    ATTACK: "%00" обрезает строку на ".php" после того, как расширение ".jpg" прошло проверку
    GUARD: NULL_FORM ≠ TRUNCATION_SAFETY_PROOF
  RISK_CASE_002:
    NAME: WAF_FILTER_TRUNCATION
    INPUT: "safe\\0<script>alert(1)</script>"
    CONTEXT: NUL заставляет сканер прекратить чтение до полезной нагрузки
    RISK: HIGH
    ATTACK: фильтр на C останавливается на NUL; следующий слой всё ещё обрабатывает хвост (XSS/SQLi)
    GUARD: NULL_FORM ≠ LANGUAGE_UNIFORMITY_PROOF
  RISK_CASE_003:
    NAME: LOG_TRUNCATION_HIDE
    INPUT: "user login\\0 ADMIN ESCALATION"
    CONTEXT: NUL усекает строку лога, скрывая хвост
    RISK: HIGH
    ATTACK: просмотрщик останавливается на NUL, скрывая дописанное действие атакующего
    GUARD: NULL_FORM ≠ EFFECT
  RISK_CASE_004:
    NAME: AUTH_STRING_TRUNCATION
    INPUT: "admin\\0ignored"
    CONTEXT: NUL обрезает имя пользователя до привилегированного префикса
    RISK: HIGH
    ATTACK: один слой сравнивает "admin\\0ignored", другой аутентифицирует "admin"
    GUARD: NULL_FORM ≠ EMPTY_EQUIVALENCE_PROOF
  RISK_CASE_005:
    NAME: ENCODED_NUL_BYPASS
    INPUT: "value%00.. (с поздним декодированием)"
    CONTEXT: кодированный NUL декодируется обратно перед приёмником
    RISK: HIGH
    ATTACK: "%00" декодируется в NUL ПОСЛЕ валидации → усечение/обход
    GUARD: NULL_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: NUL_INSERTION_EVASION
    INPUT: "jav\\0ascript:alert(1)"
    CONTEXT: NUL, вставленный в середину токена, чтобы сломать совпадение ключевого слова
    RISK: MEDIUM
    ATTACK: NUL расщепляет "javascript" для наивного матчера, но вырезается дальше по цепочке
    GUARD: NULL_FORM ≠ SANITIZED_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ␀
    CODEPOINT: U+2400
    NAME: SYMBOL FOR NULL
    RISK: LOW
    RULE: SYMBOL_FOR_NULL ≠ NULL (печатаемая картинка, вставленная там, где подразумевается реальный NUL)
  CONFUSABLE_002:
    VISIBLE_FORM: ␦
    CODEPOINT: U+001A
    NAME: SUBSTITUTE
    RISK: MEDIUM
    RULE: SUBSTITUTE ≠ NULL (Ctrl-Z / DOS EOF; другой sentinel усечения, который смешивает blanket-фильтр)
  CONFUSABLE_003:
    VISIBLE_FORM: ␄
    CODEPOINT: U+0004
    NAME: END OF TRANSMISSION
    RISK: LOW
    RULE: END_OF_TRANSMISSION ≠ NULL (терминатор потока, не терминатор C-строки)
  CONFUSABLE_004:
    VISIBLE_FORM: ␡
    CODEPOINT: U+007F
    NAME: DELETE
    RISK: LOW
    RULE: DELETE ≠ NULL (управляющий, часто вырезаемый вместе с NUL, но ведёт себя иначе)
  CONFUSABLE_005:
    VISIBLE_FORM: ␁
    CODEPOINT: U+0001
    NAME: START OF HEADING
    RISK: LOW
    RULE: START_OF_HEADING ≠ NULL (соседний C0-управляющий, который фильтр «вырезать только NUL» оставляет)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "NUL — это всегда просто терминатор строки"
    RESPONSE: NULL_FORM ≠ TERMINATOR_ONLY_PROOF
    RULE: NUL может усечь провалидированное значение так, что проверенный суффикс отбрасывается
  CG2:
    TRIGGER: "невидимый управляющий символ не может быть опасен"
    RESPONSE: NULL_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: невидимость ортогональна эффекту; NUL управляет границами строки
  CG3:
    TRIGGER: "NUL — то же самое, что пусто / нет данных"
    RESPONSE: NULL_FORM ≠ EMPTY_EQUIVALENCE_PROOF
    RULE: NUL — реальный байт, который может обрезать, расщепить или рассинхронизировать значение
  CG4:
    TRIGGER: "'%00' / '\\0' безопасен навсегда"
    RESPONSE: NULL_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в NUL перед приёмником
  CG5:
    TRIGGER: "каждый слой обрабатывает NUL одинаково"
    RESPONSE: NULL_FORM ≠ LANGUAGE_UNIFORMITY_PROOF
    RULE: C останавливается на NUL; управляемые строки хранят хвост → рассинхрон усечения
  CG6:
    TRIGGER: "наличие NUL значит, что ввод санитизирован"
    RESPONSE: NULL_FORM ≠ SANITIZED_PROOF
    RULE: наличие знака ничего не говорит о санитизации

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "value + NUL + ext"
      NAME: EXTENSION_TRUNCATION
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: NUL обрезает имя файла после проверки допустимого расширения
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "prefix + NUL + tail"
      NAME: FILTER_TRUNCATION
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: NUL заставляет сканер остановиться до хвоста полезной нагрузки
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "token + NUL + token"
      NAME: KEYWORD_SPLIT
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: NUL расщепляет ключевое слово для наивного матчера
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — последовательности с NUL центральны для обхода усечением/рассинхроном.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: NUL усекает или расщепляет ГРАНИЦУ строки, но не имитирует существование верифицированной сущности. Его риски — усечение/рассинхрон, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена NUL на SUBSTITUTE (U+001A) как альтернативный sentinel усечения
  A2: кодирование NUL как "%00" / "\\u0000" для проскальзывания мимо raw-byte фильтра
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: усечение расширения пути shell.php%00.jpg
  B2: усечение фильтра safe\\0<script>...
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "value + NUL + ext" (SC1) — усечение расширения
  C2: "token + NUL + token" (SC3) — расщепление ключевого слова
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: NUL подан как безобидный паддинг внутри проверяемого значения
  D2: "%00" как «безопасный» кодированный текст с поздним декодированием
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: усечение проверки расширения в загрузке файла
  E2: N/A — вектор: усечение строки аутентификации в компараторе логина
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: NUL — всегда просто терминатор строки
  EXPECTED: FAIL_TERMINATOR_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: невидимый управляющий символ не может быть опасен
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: NUL — то же самое, что пусто / нет данных
  EXPECTED: FAIL_EMPTY_EQUIVALENCE_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%00" / "\0" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: каждый слой обрабатывает NUL одинаково
  EXPECTED: FAIL_LANGUAGE_UNIFORMITY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: наличие NUL доказывает санитизацию ввода
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как отвергать/нормализовать NUL единообразно на всех слоях (C / управляемый / БД) без ложных срабатываний на легитимном бинарном паддинге или выводе с NUL-разделителями?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (ранний отказ от NUL в текстовых полях + работа со строками по длине, а не по NUL + согласованное декодирование — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «NUL — реальный байт; слои, останавливающиеся на нём, рассинхронизируются со слоями, которые нет».
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
