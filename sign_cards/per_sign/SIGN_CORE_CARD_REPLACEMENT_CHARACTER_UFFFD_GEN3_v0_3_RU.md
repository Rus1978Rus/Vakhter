PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_REPLACEMENT_CHARACTER_UFFFD_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
TRANSLATION_NOTE: Русский оригинал (авторитетный). Английское зеркало — SIGN_CORE_CARD_REPLACEMENT_CHARACTER_UFFFD_GEN3_v0_3_EN. Кодпойнты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_REPLACEMENT_CHARACTER_UFFFD_GEN3_v0_3_RU
CODEPOINT: U+FFFD
VISIBLE_FORM: ⟨REPL⟩
UNICODE_NAME: REPLACEMENT CHARACTER
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: символ замены / маркер ошибки декодирования (контент уже был невалиден или потерян)
CATEGORY_ROADMAP: LLM (lossy-decode / mojibake injection) · PHAGO: — (маскировка повреждения)
GLYPH_NOTE: VISIBLE_FORM использует маркер ⟨REPL⟩; сам знак (U+FFFD) — Symbol (категория So), обычно показываемый как чёрный ромб со знаком вопроса, и НЕ пишется буквально. Примеры используют ⟨REPL⟩/%EF%BF%BD, но не байт. Это то, что декодер подставляет вместо невалидной/недекодируемой последовательности байтов.

============================================================
3. REQUIRED_GENERAL_GUARDS
============================================================
REQUIRED_GENERAL_GUARDS:
  - SIGN_FALSE_EFFECT_MIMICRY_GUARD_v0_2A_RU
    GUARD_COMPATIBILITY: применим без изменений — знак не создаёт полей-эффектов
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
VISIBLE_FORM: ⟨REPL⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: REPL_FORM ≠ EFFECT
SIGN_CATEGORY:
  - Symbol, который декодер подставляет вместо невалидной / недекодируемой последовательности байтов
  - легитимное использование: сигнализировать, что байт не удалось декодировать (видимый маркер ошибки декодирования)
  - его присутствие означает, что контент УЖЕ был изменён или потерян на более раннем шаге декодирования
  - (при злоупотреблении) отпечаток потерянного при транскодировании, эксплуатируемый атакующим — намеренный mojibake, чтобы проверка-до-декода и использование-после-декода расходились

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_ORIGINAL_CONTENT — это подстановка; оригинальный байт(ы), который он заменил, потерян или изменён
  2. NOT_ONE_BYTE — декодер может выдать один U+FFFD на невалидный байт или один на плохую последовательность; счёт зависит от декодера, не от исходной длины
  3. NOT_HARMLESS_NOISE — его присутствие сигнализирует об ошибке декодирования выше по потоку, которая могла отбросить или переформировать значимые данные
  4. NOT_OBJECT_REPLACEMENT — U+FFFD отмечает ошибку декодирования; U+FFFC отмечает валидный встроенный объект — противоположные смыслы, соседние кодпойнты
  5. NOT_ENCODED_SAFE — «%EF%BF%BD» может быть декодирован обратно в символ замены позже
  6. NOT_AUTHORITY — он не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сам по себе он ничего не исполняет; он отмечает повреждение
  8. NOT_TRUST_SIGNAL — он не повышает доверие
  9. NOT_STABLE_DECODE — разные декодеры подставляют по-разному (счёт/позиция), так что проверка-до-декода ≠ использование-после-декода
  10. NOT_SANITIZED_PROOF — присутствие символа не означает, что ввод санирован; он может прятать удалённую нагрузку
  11. NOT_ROUNDTRIP_PROOF — после подстановки данные не могут вернуться round-trip к оригинальным байтам

BASE_FORMULAS:
  REPL_FORM ≠ EFFECT
  REPL_FORM ≠ ORIGINAL_CONTENT_PROOF
  REPL_FORM ≠ ONE_BYTE_PROOF
  REPL_FORM ≠ HARMLESS_NOISE_PROOF
  REPL_FORM ≠ OBJECT_REPLACEMENT_PROOF
  REPL_FORM ≠ ENCODED_SAFETY_PROOF
  REPL_FORM ≠ AUTHORITY
  REPL_FORM ≠ EXECUTION_TRIGGER
  REPL_FORM ≠ STABLE_DECODE_PROOF
  REPL_FORM ≠ SANITIZED_PROOF
  REPL_FORM ≠ ROUNDTRIP_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: REPL (ZONE_1) имеет параллельные функции (легитимный сигнал ошибки декодирования vs. отпечаток потерянного транскодирования / mojibake-инъекции), сосуществующие без культурной прецессии. Полисемия стабильного символа-подстановки.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: символ-подстановка ошибки декодирования без жестового предшественника; злоупотребление через потерянное транскодирование надстроено цифровой эпохой параллельно с легитимной сигнализацией об ошибке.

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
    INPUT: "REPL is U+FFFD in Unicode"
    CONTEXT: именование символа в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: REPL_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "a decoder emits U+FFFD for an invalid byte"
    CONTEXT: описание легитимной функции в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: REPL_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <REPL> here"
    CONTEXT: документационный маркер, не байт
    EXPECTED: INFO
    RISK: NONE
    GUARD: REPL_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "it is a substitution, not the original content"
    CONTEXT: описание того, что он заменил, в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: REPL_FORM ≠ ORIGINAL_CONTENT_PROOF
  SAFE_CASE_005:
    INPUT: "it marks a decode error, not an embedded object"
    CONTEXT: отличие от U+FFFC в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: REPL_FORM ≠ OBJECT_REPLACEMENT_PROOF
  SAFE_CASE_006:
    INPUT: "its presence signals earlier corruption to investigate"
    CONTEXT: описание его как диагностики в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: REPL_FORM ≠ HARMLESS_NOISE_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: DECODE_TIMING_DESYNC
    INPUT: "a check run on raw bytes and a use run after decoding to U+FFFD"
    CONTEXT: проверка-до-декода и использование-после-декода видят разные строки
    RISK: HIGH
    ATTACK: невалидная последовательность проходит проверку сырых байтов, затем декодируется в другую строку, которую использует исполнитель
    GUARD: REPL_FORM ≠ STABLE_DECODE_PROOF
  RISK_CASE_002:
    NAME: MOJIBAKE_FILTER_EVASION
    INPUT: "deliberately malformed bytes that decode to REPL, splitting a keyword"
    CONTEXT: подложенные невалидные байты, чтобы подстрочное совпадение провалилось после подстановки
    RISK: HIGH
    ATTACK: искажённая последовательность разбивает «javascript» на куски вокруг REPL, которые снисходительная стадия сшивает/игнорирует
    GUARD: REPL_FORM ≠ ORIGINAL_CONTENT_PROOF
  RISK_CASE_003:
    NAME: SUBSTITUTION_COUNT_SHIFT
    INPUT: "a bad sequence one decoder replaces with 1 REPL and another with 3"
    CONTEXT: декодеры расходятся в том, сколько U+FFFD выдать
    RISK: MEDIUM
    ATTACK: длина/смещение, вычисленное на одном декодере, неверно индексирует на другом → сдвиг разбора
    GUARD: REPL_FORM ≠ ONE_BYTE_PROOF
  RISK_CASE_004:
    NAME: ENCODED_REPL_BYPASS
    INPUT: "value%EF%BF%BDtail (with a later decode)"
    CONTEXT: percent-кодированный символ замены, декодируемый обратно перед использованием
    RISK: MEDIUM
    ATTACK: «%EF%BF%BD» декодируется в буквальный U+FFFD ПОСЛЕ проверки, имитируя ошибку декодирования для запутывания обработки
    GUARD: REPL_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: HIDDEN_STRIPPED_PAYLOAD
    INPUT: "a REPL where meaningful bytes were dropped during transcode"
    CONTEXT: трактовка REPL как безобидного, пока он маскирует удалённый контент
    RISK: MEDIUM
    ATTACK: подстановка прячет, что данные (напр. control или разделитель) были молча потеряны, меняя смысл
    GUARD: REPL_FORM ≠ HARMLESS_NOISE_PROOF
  RISK_CASE_006:
    NAME: OBJECT_CONFUSION
    INPUT: "a pipeline treating U+FFFD like U+FFFC (embedded object)"
    CONTEXT: путаница маркера ошибки декодирования с плейсхолдером объекта
    RISK: LOW
    ATTACK: обработка одного как другого неверно маршрутизирует логику ошибки vs встроенного объекта
    GUARD: REPL_FORM ≠ OBJECT_REPLACEMENT_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨OBJ⟩
    CODEPOINT: U+FFFC
    NAME: OBJECT REPLACEMENT CHARACTER
    RISK: HIGH
    RULE: OBJECT_REPLACEMENT_CHARACTER ≠ REPLACEMENT_CHARACTER (U+FFFC отмечает валидный встроенный объект; U+FFFD отмечает ошибку декодирования — противоположные смыслы, соседние кодпойнты)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨SUB⟩
    CODEPOINT: U+001A
    NAME: SUBSTITUTE
    RISK: MEDIUM
    RULE: SUBSTITUTE ≠ REPLACEMENT_CHARACTER (C0-control, исторически использовавшийся для символа замены; другой, более старый механизм)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨QMARK⟩
    CODEPOINT: U+003F
    NAME: QUESTION MARK
    RISK: MEDIUM
    RULE: QUESTION_MARK ≠ REPLACEMENT_CHARACTER (некоторые транскодеры подставляют ASCII «?» вместо недекодируемых символов; другая, неоднозначная подстановка)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨BLACK-DIAMOND⟩
    CODEPOINT: U+25C6
    NAME: BLACK DIAMOND
    RISK: LOW
    RULE: BLACK_DIAMOND ≠ REPLACEMENT_CHARACTER (глиф ромба, как REPL часто рисуют; обычный геометрический символ)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨NULL⟩
    CODEPOINT: U+0000
    NAME: NULL
    RISK: LOW
    RULE: NULL ≠ REPLACEMENT_CHARACTER (NUL иногда подставляется или на нём происходит усечение; другой механизм повреждения)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "the REPL is the original content"
    RESPONSE: REPL_FORM ≠ ORIGINAL_CONTENT_PROOF
    RULE: это подстановка; байты, которые он заменил, потеряны или изменены
  CG2:
    TRIGGER: "one REPL means one lost byte"
    RESPONSE: REPL_FORM ≠ ONE_BYTE_PROOF
    RULE: декодеры выдают зависящий от декодера счёт U+FFFD; это не исходная длина
  CG3:
    TRIGGER: "a REPL is just harmless noise"
    RESPONSE: REPL_FORM ≠ HARMLESS_NOISE_PROOF
    RULE: он сигнализирует об ошибке декодирования выше по потоку, которая могла отбросить значимые данные
  CG4:
    TRIGGER: "'%EF%BF%BD' is safe forever"
    RESPONSE: REPL_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в буквальный U+FFFD перед использованием
  CG5:
    TRIGGER: "check-before-decode equals use-after-decode"
    RESPONSE: REPL_FORM ≠ STABLE_DECODE_PROOF
    RULE: декодирование в U+FFFD меняет строку; две стадии расходятся
  CG6:
    TRIGGER: "U+FFFD and U+FFFC are the same replacement char"
    RESPONSE: REPL_FORM ≠ OBJECT_REPLACEMENT_PROOF
    RULE: один отмечает ошибку декодирования, другой — валидный встроенный объект — противоположные смыслы

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "malformed bytes -> REPL inside a keyword"
      NAME: MOJIBAKE_SPLIT
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: невалидная последовательность, декодирующаяся в REPL, разбивающий заблокированное ключевое слово
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "raw check then decode-to-REPL"
      NAME: DECODE_TIMING_GAP
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: проверка на байтах и использование на декодированной строке, расходящиеся
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "REPL count varying across decoders"
      NAME: OFFSET_SHIFT
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: длина/смещение, вычисленное на одном декодере, неверно индексирующее на другом
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: не применимо — риск REPL именно о времени декодирования и подстановке в последовательности.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: REPL отмечает/маскирует повреждение (маскировка повреждения), но не имитирует существование верифицированной сущности. Его риски — десинхрон времени декодирования и скрытая потеря данных, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: путаница с OBJECT REPLACEMENT (U+FFFC) / подстановкой ASCII «?» для маскировки ошибки декодирования
  A2: percent-кодирование "%EF%BF%BD" для инъекции буквального символа замены мимо сканера сырых байтов
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: десинхрон времени декодирования (проверка сырых байтов vs использование декодированной строки)
  B2: обход фильтра через mojibake (искажённые байты декодируются в REPL, разбивающий ключевое слово)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "REPL count varying across decoders" (SC3) — сдвиг смещения
  C2: "malformed bytes -> REPL inside a keyword" (SC1) — mojibake-разбиение
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: REPL подан как «безобидный шум», пока он маскирует удалённые/потерянные байты
  D2: "%EF%BF%BD" как «безопасный» кодированный маркер ошибки декодирования с последующим декодом
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: скрытая потеря данных за подстановкой
  E2: N/A — вектор: путаница ошибки декодирования / встроенного объекта (U+FFFD vs U+FFFC)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: REPL есть оригинальный контент
  EXPECTED: FAIL_ORIGINAL_CONTENT_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: один REPL равен одному потерянному байту
  EXPECTED: FAIL_ONE_BYTE_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: REPL — безобидный шум
  EXPECTED: FAIL_HARMLESS_NOISE_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%EF%BF%BD" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: проверка-до-декода равна использованию-после-декода
  EXPECTED: FAIL_STABLE_DECODE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: U+FFFD то же самое, что U+FFFC
  EXPECTED: FAIL_OBJECT_REPLACEMENT_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как декодировать один раз к канонической форме до любой проверки или использования (никогда не проверяя сырые байты, а затем используя декодированную строку), и трактовать любой U+FFFD как жёсткий сигнал повреждения выше по потоку для отклонения или расследования — не ломая легитимную отчётность об ошибках?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (конвейер, декодирующий-затем-проверяющий на одной канонической строке и помечающий/отклоняющий вводы, содержащие маркеры ошибок декодирования — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «U+FFFD — потерянная подстановка, не оригинал; его счёт зависит от декодера, и проверка-до-декода расходится с использованием-после-декода».
ALL_OPEN_QUESTIONS_CLOSED: NO (delegated, non-blocking)

============================================================
11. PATCH_HISTORY
============================================================
PATCH_HISTORY:
  v0_1_PATCH_01: первичное создание (Ruslan Malyavsky, 2026-07-22) — черновик из шаблона GEN3_v0_3 (Vakhter); не конвейер-ран.
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
  NOT_CONVEYOR_RUN (draft for our work; conveyor is a separate project)
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
