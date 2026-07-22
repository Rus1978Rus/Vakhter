PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_ZERO_WIDTH_NO_BREAK_SPACE_UFEFF_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
TRANSLATION_NOTE: Русский оригинал (авторитетный). Английское зеркало — SIGN_CORE_CARD_ZERO_WIDTH_NO_BREAK_SPACE_UFEFF_GEN3_v0_3_EN. Кодпойнты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_ZERO_WIDTH_NO_BREAK_SPACE_UFEFF_GEN3_v0_3_RU
CODEPOINT: U+FEFF
VISIBLE_FORM: ⟨ZWNBSP/BOM⟩
UNICODE_NAME: ZERO WIDTH NO-BREAK SPACE
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: неразрывный пробел нулевой ширины / маркер порядка байтов (позиционно-зависимая двойная роль)
CATEGORY_ROADMAP: LLM (invisible zero-width injection, encoding confusion) · PHAGO: — (маскировка токена / кодировки)
GLYPH_NOTE: VISIBLE_FORM использует маркер ⟨ZWNBSP/BOM⟩; сам знак (U+FEFF) — невидимый Format-символ (Cf) и НИКОГДА не пишется буквально — буквальный ведущий U+FEFF был бы трактован как BOM этого файла. Примеры используют ⟨BOM⟩/%EF%BB%BF, но не байт.

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
VISIBLE_FORM: ⟨ZWNBSP/BOM⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: BOM_FORM ≠ EFFECT
SIGN_CATEGORY:
  - невидимый Format-символ с ПОЗИЦИОННО-ЗАВИСИМОЙ двойной ролью
  - в начале потока: маркер порядка байтов (сигнализирует кодировку/порядок байтов), обычно срезается
  - в середине потока: неразрывный пробел нулевой ширины (устарел для этого; WJ — современная замена)
  - (при злоупотреблении) невидимый внутренний символ / путаница определения кодировки / невидимый клей, который срезание BOM пропускает в середине потока

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — непечатаемость не делает знак инертным
  2. NOT_ALWAYS_A_BOM — только ВЕДУЩИЙ U+FEFF есть BOM; в середине потока это неразрывный пробел нулевой ширины, не метаданные
  3. NOT_ALWAYS_STRIPPED — срезание, удаляющее только ведущий BOM, оставляет внутренние U+FEFF на месте
  4. NOT_ENCODING_TRUTH — BOM это подсказка, не доказательство; он может лгать о фактической кодировке или не совпадать с ней
  5. NOT_ENCODED_SAFE — «%EF%BB%BF» может быть декодирован обратно в U+FEFF позже
  6. NOT_AUTHORITY — он не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сам по себе он ничего не исполняет; он обманывает фильтры и логику кодировки
  8. NOT_TRUST_SIGNAL — он не повышает доверие
  9. NOT_WJ — для работы неразрывности он вытеснен U+2060; трактовка их как взаимозаменяемых пропускает один
  10. NOT_SANITIZED_PROOF — присутствие символа не означает, что ввод санирован
  11. NOT_SINGLE_TOKEN_PROOF — внутренний U+FEFF может разбить ключевое слово, выглядя как ничто

BASE_FORMULAS:
  BOM_FORM ≠ EFFECT
  BOM_FORM ≠ ALWAYS_A_BOM_PROOF
  BOM_FORM ≠ ALWAYS_STRIPPED_PROOF
  BOM_FORM ≠ ENCODING_TRUTH_PROOF
  BOM_FORM ≠ ENCODED_SAFETY_PROOF
  BOM_FORM ≠ AUTHORITY
  BOM_FORM ≠ EXECUTION_TRIGGER
  BOM_FORM ≠ WJ_EQUIVALENCE_PROOF
  BOM_FORM ≠ INVISIBLE_HARMLESS_PROOF
  BOM_FORM ≠ SANITIZED_PROOF
  BOM_FORM ≠ SINGLE_TOKEN_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: U+FEFF (ZONE_1) имеет параллельные функции (ведущие метаданные BOM vs. внутренний неразрывный пробел vs. невидимая инъекция), сосуществующие без культурной прецессии. Его смысл позиционно-зависим, а не эпохо-зависим.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: control кодировки/неразрывности без жестового предшественника; злоупотребление через внутреннюю инъекцию и путаницу кодировки надстроено цифровой эпохой параллельно с легитимным использованием BOM.

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
    INPUT: "U+FEFF is the byte order mark"
    CONTEXT: именование символа в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: BOM_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "a leading BOM signals encoding"
    CONTEXT: описание легитимной ведущей роли в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: BOM_FORM ≠ ENCODING_TRUTH_PROOF
  SAFE_CASE_003:
    INPUT: "the marker is written as <BOM> here"
    CONTEXT: документационный маркер, не байт
    EXPECTED: INFO
    RISK: NONE
    GUARD: BOM_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "mid-stream it is a zero width no-break space"
    CONTEXT: описание позиционно-зависимой роли в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: BOM_FORM ≠ ALWAYS_A_BOM_PROOF
  SAFE_CASE_005:
    INPUT: "WJ is the modern replacement for the no-break use"
    CONTEXT: описание устаревания в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: BOM_FORM ≠ WJ_EQUIVALENCE_PROOF
  SAFE_CASE_006:
    INPUT: "a leading BOM is usually stripped on read"
    CONTEXT: описание нормальной обработки в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: BOM_FORM ≠ ALWAYS_STRIPPED_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: INTERIOR_BOM_SURVIVES_STRIP
    INPUT: "text with a mid-stream U+FEFF after a leading-BOM strip"
    CONTEXT: срезание, удаляющее только ведущий BOM, оставляя внутренние копии
    RISK: HIGH
    ATTACK: внутренний U+FEFF действует как невидимый клей/разделитель, которого санитайзер не коснулся
    GUARD: BOM_FORM ≠ ALWAYS_STRIPPED_PROOF
  RISK_CASE_002:
    NAME: KEYWORD_SPLIT
    INPUT: "jav<BOM>ascript: in a URL scheme check"
    CONTEXT: внутренний U+FEFF разбивает ключевое слово, чтобы подстрочный блоклист не совпал
    RISK: HIGH
    ATTACK: блоклист упускает «javascript», пока снисходительный парсер игнорирует U+FEFF
    GUARD: BOM_FORM ≠ SINGLE_TOKEN_PROOF
  RISK_CASE_003:
    NAME: ENCODING_MISDETECTION
    INPUT: "a BOM that does not match the actual byte encoding"
    CONTEXT: лживый/несовпадающий BOM уводит определение кодировки в сторону
    RISK: MEDIUM
    ATTACK: декодер доверяет подсказке BOM и неверно декодирует нагрузку, меняя её смысл
    GUARD: BOM_FORM ≠ ENCODING_TRUTH_PROOF
  RISK_CASE_004:
    NAME: ENCODED_BOM_BYPASS
    INPUT: "value%EF%BB%BFtail (with a later decode)"
    CONTEXT: percent-кодированный U+FEFF, декодируемый обратно перед использованием
    RISK: HIGH
    ATTACK: «%EF%BB%BF» декодируется в U+FEFF ПОСЛЕ проверки → скрытое разбиение возвращается
    GUARD: BOM_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: WJ_CONFLATION_GAP
    INPUT: "a filter handling U+FEFF but not U+2060 (or vice versa)"
    CONTEXT: трактовка неразрывной пары как одного, пропуская другого
    RISK: MEDIUM
    ATTACK: правило, настроенное под BOM, упускает WJ, так что невидимый клей выживает
    GUARD: BOM_FORM ≠ WJ_EQUIVALENCE_PROOF
  RISK_CASE_006:
    NAME: HOMOGLYPH_STACK
    INPUT: "раy<BOM>раl (invisible char + confusable letters combined)"
    CONTEXT: внутренний U+FEFF в связке с похожими буквами для усиления подделки
    RISK: MEDIUM
    ATTACK: невидимый символ плюс буквы-двойники проводят враждебную строку через поверхностный обзор
    GUARD: BOM_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨WJ⟩
    CODEPOINT: U+2060
    NAME: WORD JOINER
    RISK: HIGH
    RULE: WORD_JOINER ≠ ZERO_WIDTH_NO_BREAK_SPACE (та же работа неразрывности, но WJ — не-BOM современная форма; U+FEFF дублирует BOM)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨ZWSP⟩
    CODEPOINT: U+200B
    NAME: ZERO WIDTH SPACE
    RISK: HIGH
    RULE: ZERO_WIDTH_SPACE ≠ ZERO_WIDTH_NO_BREAK_SPACE (ZWSP разрешает перенос; U+FEFF запрещает и может быть BOM)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨NBSP⟩
    CODEPOINT: U+00A0
    NAME: NO-BREAK SPACE
    RISK: MEDIUM
    RULE: NO_BREAK_SPACE ≠ ZERO_WIDTH_NO_BREAK_SPACE (NBSP — пробел с видимым продвижением; U+FEFF нулевой ширины и способен быть BOM)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨ZWJ⟩
    CODEPOINT: U+200D
    NAME: ZERO WIDTH JOINER
    RISK: LOW
    RULE: ZERO_WIDTH_JOINER ≠ ZERO_WIDTH_NO_BREAK_SPACE (ZWJ комбинирует глифы; U+FEFF — неразрывный пробел / BOM)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨MVS⟩
    CODEPOINT: U+180E
    NAME: MONGOLIAN VOWEL SEPARATOR
    RISK: LOW
    RULE: MONGOLIAN_VOWEL_SEPARATOR ≠ ZERO_WIDTH_NO_BREAK_SPACE (исторически трактовался как пробел нулевой ширины; ещё один невидимый format-символ, который фильтр, настроенный на BOM, упускает)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "a U+FEFF is always a BOM, so it is metadata"
    RESPONSE: BOM_FORM ≠ ALWAYS_A_BOM_PROOF
    RULE: только ведущий U+FEFF есть BOM; в середине потока это неразрывный пробел в данных
  CG2:
    TRIGGER: "an invisible char cannot be dangerous"
    RESPONSE: BOM_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: невидимость ортогональна эффекту; внутренний U+FEFF создаёт десинхрон фильтра и кодировки
  CG3:
    TRIGGER: "we strip the BOM, so U+FEFF is gone"
    RESPONSE: BOM_FORM ≠ ALWAYS_STRIPPED_PROOF
    RULE: срезание ведущего BOM оставляет внутренние U+FEFF нетронутыми
  CG4:
    TRIGGER: "'%EF%BB%BF' is safe forever"
    RESPONSE: BOM_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в U+FEFF перед использованием
  CG5:
    TRIGGER: "the BOM tells us the encoding for sure"
    RESPONSE: BOM_FORM ≠ ENCODING_TRUTH_PROOF
    RULE: BOM — подсказка, которая может лгать или не совпадать с фактическими байтами
  CG6:
    TRIGGER: "U+FEFF and U+2060 are the same no-break char"
    RESPONSE: BOM_FORM ≠ WJ_EQUIVALENCE_PROOF
    RULE: WJ — не-BOM современная форма; обработка одного не есть обработка другого

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "leading U+FEFF then payload"
      NAME: BOM_PREFIX
      RISK_LEVEL: LOW
      POSSIBLE_CONTEXTS: легитимный/ожидаемый BOM, который должен срезаться один раз при чтении
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "interior U+FEFF inside a token"
      NAME: INTERIOR_GLUE
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: внутренний U+FEFF, разбивающий ключевое слово после срезания ведущего BOM
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "U+FEFF + confusable letters"
      NAME: INVISIBLE_HOMOGLYPH_STACK
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: невидимый символ в связке с похожими буквами для подделки
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: не применимо — именно позиция в последовательности решает смысл U+FEFF.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: U+FEFF маскирует токены и путает кодировку (маскировка токена/кодировки), но не имитирует существование верифицированной сущности. Его риски — десинхрон фильтра/кодировки, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена U+FEFF на WJ (U+2060) / ZWSP (U+200B) для смены невидимого байта / обхода фильтра только-BOM
  A2: percent-кодирование "%EF%BB%BF" для проскока мимо сканера сырых байтов
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: внутренний U+FEFF, переживающий срезание ведущего BOM и разбивающий ключевое слово
  B2: неверное определение кодировки через лживый/несовпадающий BOM
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "interior U+FEFF inside a token" (SC2) — внутренний клей
  C2: "U+FEFF + confusable letters" (SC3) — невидимый гомоглиф-стек
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: внутренний U+FEFF подан как «просто безобидный BOM», чтобы его проигнорировали, а затем злоупотребить в середине потока
  D2: "%EF%BB%BF" как «безопасный» кодированный текст с последующим декодом
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: невидимая путаница идентификатора/ключевого слова через внутренний U+FEFF
  E2: N/A — вектор: смешение неразрывной пары (U+FEFF vs U+2060), оставляющее один необработанным
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: U+FEFF всегда есть BOM
  EXPECTED: FAIL_ALWAYS_A_BOM_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: невидимый символ не может быть опасен
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: срезание ведущего BOM удаляет каждый U+FEFF
  EXPECTED: FAIL_ALWAYS_STRIPPED_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%EF%BB%BF" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: BOM доказывает кодировку
  EXPECTED: FAIL_ENCODING_TRUTH_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: U+FEFF и U+2060 взаимозаменяемы
  EXPECTED: FAIL_WJ_EQUIVALENCE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как срезать ведущий BOM один раз для кодировки, всё ещё ловя внутренний U+FEFF как невидимый инъектор, и трактовать BOM как недоверенную подсказку кодировки, а не доказательство?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (читатель, потребляющий не более одного ведущего BOM, помечающий/отклоняющий внутренний U+FEFF и валидирующий заявленную vs. обнаруженную кодировку — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «смысл U+FEFF позиционно-зависим: ведущий = подсказка BOM (не истина), внутренний = невидимый неразрывный пробел, который срезание BOM пропускает».
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
