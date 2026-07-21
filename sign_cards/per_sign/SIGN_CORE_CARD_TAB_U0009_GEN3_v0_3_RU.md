PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_TAB_U0009_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: Русский оригинал (authoritative). Английское зеркало — SIGN_CORE_CARD_TAB_U0009_GEN3_v0_3_EN. Кодпоинты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_TAB_U0009_GEN3_v0_3_RU
CODEPOINT: U+0009
VISIBLE_FORM: ␉
UNICODE_NAME: <control> CHARACTER TABULATION (TAB)
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: табуляция / горизонтальная табуляция (непечатаемый)
CATEGORY_ROADMAP: INJ (обход whitespace-фильтра, инъекция разделителя) · PHAGO: — (путаница границ поля)
GLYPH_NOTE: VISIBLE_FORM использует ␉ (U+2409 SYMBOL FOR HORIZONTAL TABULATION) как печатаемую картинку; сам знак (U+0009) — непечатаемый управляющий символ.

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
VISIBLE_FORM: ␉
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: TAB_FORM ≠ EFFECT
SIGN_CATEGORY:
  - горизонтальный отступ / пробел выравнивания
  - разделитель полей в TSV и некоторых форматах логов
  - разделитель токенов/слов наряду с пробелом в shell (IFS)
  - структурный пробел в Makefile / некоторых форматах конфигов

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_WHITESPACE_ONLY — TAB не всегда «просто отступ» (он разделяет токены/поля shell)
  2. NOT_SPACE_EQUIVALENT — TAB — другой кодпоинт, чем пробел; фильтры расходятся
  3. NOT_INVISIBLE_MEANS_HARMLESS — то, что он непечатаемый, не делает его инертным
  4. NOT_TRIM_PROOF — «обрезанное» значение всё ещё может нести внутренний TAB
  5. NOT_ENCODED_SAFE — "%09" / "\t" могут быть раскодированы обратно в TAB позже
  6. NOT_AUTHORITY — TAB не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сам по себе ничего не исполняет; разделение делает контекст
  8. NOT_TRUST_SIGNAL — не повышает доверие
  9. NOT_DELIMITER_SAFE — TAB может внедрить лишнее поле TSV/лога или расщепить токен
  10. NOT_SANITIZED_PROOF — наличие TAB не значит, что ввод санитизирован
  11. NOT_OUTPUT_CONTEXT_PROOF — безопасность зависит от контекста разбора/формата

BASE_FORMULAS:
  TAB_FORM ≠ EFFECT
  TAB_FORM ≠ WHITESPACE_ONLY_PROOF
  TAB_FORM ≠ SPACE_EQUIVALENCE_PROOF
  TAB_FORM ≠ INVISIBLE_HARMLESS_PROOF
  TAB_FORM ≠ TRIM_SAFETY_PROOF
  TAB_FORM ≠ ENCODED_SAFETY_PROOF
  TAB_FORM ≠ AUTHORITY
  TAB_FORM ≠ EXECUTION_TRIGGER
  TAB_FORM ≠ DELIMITER_SAFETY_PROOF
  TAB_FORM ≠ SANITIZED_PROOF
  TAB_FORM ≠ OUTPUT_CONTEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: TAB (ZONE_1) имеет параллельные функции (отступ, разделитель TSV, разделитель токенов shell, структурный пробел), сосуществующие без культурной прецессии. Полисемия стабильного управляющего кода.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1
  NOTE: управляющий код табулостопа печатной машинки без жестового предшественника; функции разделителя/структуры надстроены цифровой эпохой параллельно.

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
    INPUT: "name\\tvalue"
    CONTEXT: TAB, показанный как escape в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: TAB_FORM ≠ WHITESPACE_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: "use \\t to indent"
    CONTEXT: описание escape-последовательности в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: TAB_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "col1\\tcol2\\tcol3"
    CONTEXT: легитимный заголовок TSV (как литеральный текст)
    EXPECTED: INFO
    RISK: NONE
    GUARD: TAB_FORM ≠ DELIMITER_SAFETY_PROOF
  SAFE_CASE_004:
    INPUT: "TAB is 0x09 in ASCII"
    CONTEXT: название управляющего кода в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: TAB_FORM ≠ WHITESPACE_ONLY_PROOF
  SAFE_CASE_005:
    INPUT: "Makefiles require a \\t for recipe lines"
    CONTEXT: описание структурного использования TAB
    EXPECTED: INFO
    RISK: NONE
    GUARD: TAB_FORM ≠ EFFECT
  SAFE_CASE_006:
    INPUT: "aligned\\tcolumns in a report"
    CONTEXT: отступ/выравнивание в хранимом тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: TAB_FORM ≠ SPACE_EQUIVALENCE_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: TSV_FIELD_INJECTION
    INPUT: "user\\tadmin\\ttrue"
    CONTEXT: внедрённый TAB, добавляющий лишние столбцы TSV
    RISK: HIGH
    ATTACK: TAB внедряет лишние поля (role=admin) в tab-разделённую запись
    GUARD: TAB_FORM ≠ DELIMITER_SAFETY_PROOF
  RISK_CASE_002:
    NAME: WHITESPACE_FILTER_BYPASS
    INPUT: "SELECT\\t*\\tFROM\\tusers"
    CONTEXT: TAB вместо пробелов для обхода фильтра ключевых слов/пробела
    RISK: HIGH
    ATTACK: фильтр, делящий по пробелу, пропускает TAB-разделённые ключевые слова SQL
    GUARD: TAB_FORM ≠ SPACE_EQUIVALENCE_PROOF
  RISK_CASE_003:
    NAME: SHELL_TOKEN_SPLIT
    INPUT: "cmd\\t/etc/passwd"
    CONTEXT: TAB как разделитель IFS для расщепления аргумента
    RISK: HIGH
    ATTACK: TAB (часть дефолтного IFS) расщепляет «единый» аргумент на два токена
    GUARD: TAB_FORM ≠ WHITESPACE_ONLY_PROOF
  RISK_CASE_004:
    NAME: LOG_COLUMN_FORGERY
    INPUT: "ip\\t200 OK\\tadmin-action"
    CONTEXT: внедрённый TAB, подделывающий лишние столбцы лога
    RISK: MEDIUM
    ATTACK: TAB добавляет подконтрольные атакующему столбцы, которым доверяет парсер лога
    GUARD: TAB_FORM ≠ DELIMITER_SAFETY_PROOF
  RISK_CASE_005:
    NAME: ENCODED_TAB_BYPASS
    INPUT: "cmd%09arg (с поздним декодированием)"
    CONTEXT: кодированный TAB декодируется обратно перед приёмником
    RISK: MEDIUM
    ATTACK: %09 декодируется в TAB ПОСЛЕ проверки → расщепление токена/поля
    GUARD: TAB_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: TRIM_BYPASS_INNER_TAB
    INPUT: "ad\\tmin (внутренний TAB переживает обрезку краёв)"
    CONTEXT: внутренний TAB в значении, который внешняя обрезка пропускает
    RISK: MEDIUM
    ATTACK: обрезка краёв оставляет внутренний TAB, который позже расщепляет/нормализуется в "admin"
    GUARD: TAB_FORM ≠ TRIM_SAFETY_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: " "
    CODEPOINT: U+0020
    NAME: SPACE
    RISK: HIGH
    RULE: SPACE ≠ TAB (фильтр только по пробелу пропускает TAB и наоборот; оба — разделители IFS)
  CONFUSABLE_002:
    VISIBLE_FORM: " "
    CODEPOINT: U+00A0
    NAME: NO-BREAK SPACE
    RISK: MEDIUM
    RULE: NO_BREAK_SPACE ≠ TAB (NBSP — пробел, трактуемый некоторыми парсерами иначе)
  CONFUSABLE_003:
    VISIBLE_FORM: " "
    CODEPOINT: U+2003
    NAME: EM SPACE
    RISK: LOW
    RULE: EM_SPACE ≠ TAB (Unicode-пробел, который может свернуться в разделитель в некоторых нормализаторах)
  CONFUSABLE_004:
    VISIBLE_FORM: ␋
    CODEPOINT: U+000B
    NAME: LINE TABULATION
    RISK: MEDIUM
    RULE: LINE_TABULATION ≠ TAB (VT — вертикальная табуляция, трактуемая частью инструментов как пробел)
  CONFUSABLE_005:
    VISIBLE_FORM: "　"
    CODEPOINT: U+3000
    NAME: IDEOGRAPHIC SPACE
    RISK: LOW
    RULE: IDEOGRAPHIC_SPACE ≠ TAB (широкий пробел, который может нормализоваться в разделитель)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "TAB — это всегда просто отступ"
    RESPONSE: TAB_FORM ≠ WHITESPACE_ONLY_PROOF
    RULE: в shell/TSV TAB разделяет токены/поля
  CG2:
    TRIGGER: "TAB — то же самое, что пробел"
    RESPONSE: TAB_FORM ≠ SPACE_EQUIVALENCE_PROOF
    RULE: это разные кодпоинты; фильтр только по пробелу пропускает TAB
  CG3:
    TRIGGER: "невидимый управляющий символ не может быть опасен"
    RESPONSE: TAB_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: невидимость ортогональна эффекту; TAB управляет границами поля/токена
  CG4:
    TRIGGER: "'%09' / '\\t' безопасен навсегда"
    RESPONSE: TAB_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в TAB перед приёмником
  CG5:
    TRIGGER: "обрезка значения удаляет TAB"
    RESPONSE: TAB_FORM ≠ TRIM_SAFETY_PROOF
    RULE: обрезка краёв оставляет внутренний TAB, который всё ещё может расщепить/внедрить
  CG6:
    TRIGGER: "наличие TAB значит, что ввод санитизирован"
    RESPONSE: TAB_FORM ≠ SANITIZED_PROOF
    RULE: наличие знака ничего не говорит о санитизации

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "TAB + field"
      NAME: TSV_FIELD_INJECTION
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: TAB, добавляющий лишнее tab-разделённое поле
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "keyword TAB keyword"
      NAME: SPACE_FILTER_BYPASS
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: TAB вместо пробелов для обхода фильтра ключевых слов/пробела
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "arg TAB arg"
      NAME: IFS_TOKEN_SPLIT
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: TAB в дефолтном IFS, расщепляющий один аргумент на два
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — последовательности с TAB центральны для обхода разделителя/пробела.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: TAB разделяет поля/токены или обходит whitespace-фильтр, но не имитирует существование верифицированной сущности. Его риски — разделитель/расщепление, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена пробела на TAB для обхода фильтра на основе пробела
  A2: замена TAB на NBSP (U+00A0) для запутывания нормализатора пробелов
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: инъекция поля TSV user\\tadmin\\ttrue
  B2: обход whitespace-фильтра SELECT\\t*\\tFROM\\tusers
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "TAB + field" (SC1) — инъекция поля TSV
  C2: "arg TAB arg" (SC3) — расщепление токена IFS
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: TAB подан как безобидный отступ внутри разделённого поля
  D2: "%09" как «безопасный» кодированный текст с поздним декодированием
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: инъекция лишнего поля в импортёр TSV
  E2: N/A — вектор: TAB-расщепление токена в аргумент shell
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: TAB — всегда просто отступ
  EXPECTED: FAIL_WHITESPACE_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: TAB — то же самое, что пробел
  EXPECTED: FAIL_SPACE_EQUIVALENCE_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: невидимый управляющий символ не может быть опасен
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%09" / "\t" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: обрезка значения удаляет TAB
  EXPECTED: FAIL_TRIM_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: наличие TAB доказывает санитизацию ввода
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как нормализовать TAB по формату (TSV/shell/конфиг) без ложных срабатываний на легитимных отступах и выравнивании?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (строгий разбор полей + exec через вектор аргументов + явная нормализация пробелов — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «безопасность TAB решается контекстом разбора/формата».
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
