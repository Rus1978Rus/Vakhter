PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_SOFT_HYPHEN_U00AD_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
TRANSLATION_NOTE: Русский оригинал (авторитетный). Английское зеркало — SIGN_CORE_CARD_SOFT_HYPHEN_U00AD_GEN3_v0_3_EN. Кодпойнты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_SOFT_HYPHEN_U00AD_GEN3_v0_3_RU
CODEPOINT: U+00AD
VISIBLE_FORM: ⟨SHY⟩
UNICODE_NAME: SOFT HYPHEN
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: мягкий перенос / условный дефис, обычно невидимый внутри слова (обход разбиением ключевого слова)
CATEGORY_ROADMAP: LLM (invisible-conditional token injection) · PHAGO: — (маскировка токена)
GLYPH_NOTE: VISIBLE_FORM использует маркер ⟨SHY⟩; сам знак (U+00AD) — невидимый Format-символ (Cf), показывающий дефис ТОЛЬКО в точке переноса строки, и НИКОГДА не пишется буквально — буквальный SHY молча сидел бы внутри слова в этом документе. Примеры используют ⟨SHY⟩/%C2%AD, но не байт.

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
VISIBLE_FORM: ⟨SHY⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: SHY_FORM ≠ EFFECT
SIGN_CATEGORY:
  - невидимый Format-символ, отмечающий разрешённую точку переноса
  - он УСЛОВНЫЙ: обычно невидим внутри слова и отрисовывается как дефис, только если там происходит перенос строки
  - легитимная типографика (позволить длинному слову переноситься между строками)
  - (при злоупотреблении) невидимый внутренний символ, разбивающий ключевое слово для подстрочного совпадения, пока снисходительный парсер его игнорирует

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — обычная непечатаемость не делает знак инертным
  2. NOT_A_REAL_HYPHEN — это НЕ U+002D (дефис-минус); обычно ничего не показывает, появляясь как дефис только в точке переноса
  3. NOT_ALWAYS_INVISIBLE — он становится видимым дефисом ровно тогда, когда на нём происходит перенос строки, так что это условность, а не константа
  4. NOT_SEEN_BY_EVERY_CHECK — подстрочная/ключевая проверка не трактует его как разделитель, но снисходительный потребитель может его отбросить
  5. NOT_ENCODED_SAFE — «%C2%AD» может быть декодирован обратно в SHY позже
  6. NOT_AUTHORITY — он не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сам по себе он ничего не исполняет; он обманывает сопоставление и читателей
  8. NOT_TRUST_SIGNAL — он не повышает доверие
  9. NOT_HYPHEN_MINUS — фильтр, ищущий U+002D, не видит U+00AD
  10. NOT_SANITIZED_PROOF — присутствие символа не означает, что ввод санирован
  11. NOT_SINGLE_TOKEN_PROOF — «jav⟨SHY⟩ascript» может отображаться как одно слово, но сравниваться/разбираться как разбитое

BASE_FORMULAS:
  SHY_FORM ≠ EFFECT
  SHY_FORM ≠ REAL_HYPHEN_PROOF
  SHY_FORM ≠ ALWAYS_INVISIBLE_PROOF
  SHY_FORM ≠ SEEN_BY_EVERY_CHECK_PROOF
  SHY_FORM ≠ ENCODED_SAFETY_PROOF
  SHY_FORM ≠ AUTHORITY
  SHY_FORM ≠ EXECUTION_TRIGGER
  SHY_FORM ≠ HYPHEN_MINUS_PROOF
  SHY_FORM ≠ INVISIBLE_HARMLESS_PROOF
  SHY_FORM ≠ SANITIZED_PROOF
  SHY_FORM ≠ SINGLE_TOKEN_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: SHY (ZONE_1) имеет параллельные функции (легитимная точка переноса vs. невидимое разбиение ключевого слова), сосуществующие без культурной прецессии. Полисемия стабильного Format-символа.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: control условного переноса без жестового предшественника; злоупотребление через разбиение ключевого слова надстроено цифровой эпохой параллельно с легитимным переносом.

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
    INPUT: "SHY is U+00AD in Unicode"
    CONTEXT: именование символа в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: SHY_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "a soft hyphen marks where a word may break"
    CONTEXT: описание легитимной типографики в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: SHY_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <SHY> here"
    CONTEXT: документационный маркер, не байт
    EXPECTED: INFO
    RISK: NONE
    GUARD: SHY_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "it usually shows nothing until a line wraps on it"
    CONTEXT: описание условного свойства в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: SHY_FORM ≠ ALWAYS_INVISIBLE_PROOF
  SAFE_CASE_005:
    INPUT: "it is not the same as a hyphen-minus"
    CONTEXT: отличие от U+002D в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: SHY_FORM ≠ HYPHEN_MINUS_PROOF
  SAFE_CASE_006:
    INPUT: "a normalizer can strip soft hyphens"
    CONTEXT: описание аккуратной санитизации в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: SHY_FORM ≠ SANITIZED_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: KEYWORD_SPLIT
    INPUT: "jav<SHY>ascript: in a URL scheme check"
    CONTEXT: мягкий перенос разбивает ключевое слово, чтобы подстрочный блоклист не совпал
    RISK: HIGH
    ATTACK: блоклист упускает «javascript», пока снисходительный парсер отбрасывает SHY
    GUARD: SHY_FORM ≠ SINGLE_TOKEN_PROOF
  RISK_CASE_002:
    NAME: INVISIBLE_IN_IDENTIFIER
    INPUT: "ad<SHY>min vs admin (look-alike username)"
    CONTEXT: мягкий перенос внутри ASCII-идентификатора делает его неравным при одинаковом виде
    RISK: HIGH
    ATTACK: «ad<SHY>min» регистрируется как двойник «admin» для выдачи себя за другого
    GUARD: SHY_FORM ≠ SINGLE_TOKEN_PROOF
  RISK_CASE_003:
    NAME: CONDITIONAL_REVEAL
    INPUT: "a value that shows a stray hyphen only when the line wraps"
    CONTEXT: SHY, появляющийся как дефис в точке переноса, меняя прочтение
    RISK: MEDIUM
    ATTACK: символ невидим в обзоре, но раскрывает дефис при рендере, меняя смысл (напр. код/серийник)
    GUARD: SHY_FORM ≠ ALWAYS_INVISIBLE_PROOF
  RISK_CASE_004:
    NAME: ENCODED_SHY_BYPASS
    INPUT: "value%C2%ADtail (with a later decode)"
    CONTEXT: percent-кодированный SHY, декодируемый обратно перед использованием
    RISK: HIGH
    ATTACK: «%C2%AD» декодируется в SHY ПОСЛЕ проверки → скрытое разбиение возвращается
    GUARD: SHY_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: HYPHEN_FILTER_GAP
    INPUT: "a filter that normalizes U+002D but not U+00AD"
    CONTEXT: осведомлённый о дефисах фильтр, упускающий мягкий перенос
    RISK: MEDIUM
    ATTACK: нормализация только реального дефиса оставляет невидимый мягкий перенос разбивать токены
    GUARD: SHY_FORM ≠ HYPHEN_MINUS_PROOF
  RISK_CASE_006:
    NAME: INVISIBLE_FLOOD
    INPUT: "a run of many SHY inserted between characters"
    CONTEXT: массовая невидимая вставка для победы над наивным сопоставлением
    RISK: MEDIUM
    ATTACK: каждое ключевое слово раскрошено, так что ни одно подстрочное правило не совпадает
    GUARD: SHY_FORM ≠ SINGLE_TOKEN_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨HYPHEN-MINUS⟩
    CODEPOINT: U+002D
    NAME: HYPHEN-MINUS
    RISK: HIGH
    RULE: HYPHEN_MINUS ≠ SOFT_HYPHEN (видимый ASCII-дефис; SHY невидим внутри слова и показывается только при переносе)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨ZWSP⟩
    CODEPOINT: U+200B
    NAME: ZERO WIDTH SPACE
    RISK: HIGH
    RULE: ZERO_WIDTH_SPACE ≠ SOFT_HYPHEN (оба невидимые разделители, но ZWSP никогда не показывает глиф; SHY может показать дефис при переносе)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨HYPHEN⟩
    CODEPOINT: U+2010
    NAME: HYPHEN
    RISK: MEDIUM
    RULE: HYPHEN ≠ SOFT_HYPHEN (однозначная видимая дефисная пунктуация; не условная невидимка)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨NB-HYPHEN⟩
    CODEPOINT: U+2011
    NAME: NON-BREAKING HYPHEN
    RISK: MEDIUM
    RULE: NON_BREAKING_HYPHEN ≠ SOFT_HYPHEN (видимый дефис, запрещающий перенос; SHY его разрешает и обычно невидим)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨ZWNJ⟩
    CODEPOINT: U+200C
    NAME: ZERO WIDTH NON-JOINER
    RISK: LOW
    RULE: ZERO_WIDTH_NON_JOINER ≠ SOFT_HYPHEN (control соединения, не точка переноса; оба невидимы)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "it is a hyphen, so it is U+002D"
    RESPONSE: SHY_FORM ≠ REAL_HYPHEN_PROOF
    RULE: это U+00AD, обычно невидимый; он показывает дефис только при переносе
  CG2:
    TRIGGER: "an invisible char cannot be dangerous"
    RESPONSE: SHY_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: невидимость ортогональна эффекту; SHY разбивает ключевые слова невидимо
  CG3:
    TRIGGER: "it is always invisible, so a reviewer never sees anything odd"
    RESPONSE: SHY_FORM ≠ ALWAYS_INVISIBLE_PROOF
    RULE: он раскрывает дефис ровно в точке переноса; он условный, не постоянный
  CG4:
    TRIGGER: "'%C2%AD' is safe forever"
    RESPONSE: SHY_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в SHY перед использованием
  CG5:
    TRIGGER: "we normalize hyphens, so this is handled"
    RESPONSE: SHY_FORM ≠ HYPHEN_MINUS_PROOF
    RULE: нормализатор только-U+002D не трогает U+00AD
  CG6:
    TRIGGER: "the string looks like one word, so it is one token"
    RESPONSE: SHY_FORM ≠ SINGLE_TOKEN_PROOF
    RULE: единство отображения не подразумевает единство токена; невидимый SHY может его разбить

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "keyword with an interior SHY"
      NAME: SPLIT_KEYWORD
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: мягкий перенос внутри заблокированного ключевого слова для обхода подстрочного совпадения
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "SHY at a value that later wraps"
      NAME: CONDITIONAL_HYPHEN_REVEAL
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: мягкий перенос, раскрывающий глиф дефиса во время рендера
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "SHY between every character"
      NAME: INVISIBLE_FLOOD
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: массовая вставка, крошащая все токены
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: не применимо — последовательности с SHY центральны для невидимого разбиения ключевых слов.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: SHY разбивает/маскирует токены (маскировка токена), но не имитирует существование верифицированной сущности. Его риски — десинхрон сопоставления и путаница идентификаторов, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена SHY на ZWSP (U+200B) / ZWNJ (U+200C) для смены невидимого разделителя / обхода фильтра только-SHY
  A2: percent-кодирование "%C2%AD" для проскока мимо сканера сырых байтов
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: разбиение ключевого слова "jav<SHY>ascript:" для победы над подстрочным блоклистом
  B2: пробел дефисного фильтра (SHY переживает нормализацию только-U+002D)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "SHY between every character" (SC3) — невидимый флуд
  C2: "keyword with an interior SHY" (SC1) — разбитое ключевое слово
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: SHY подан как безобидная «подсказка переноса» внутри враждебного поля
  D2: "%C2%AD" как «безопасный» кодированный текст с последующим декодом
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: невидимая путаница идентификаторов (ad<SHY>min vs admin)
  E2: N/A — вектор: условное раскрытие дефиса в точке переноса
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: мягкий перенос это дефис-минус
  EXPECTED: FAIL_REAL_HYPHEN_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: невидимый символ не может быть опасен
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: мягкий перенос всегда невидим
  EXPECTED: FAIL_ALWAYS_INVISIBLE_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%C2%AD" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: нормализация дефис-минуса обрабатывает мягкий перенос
  EXPECTED: FAIL_HYPHEN_MINUS_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: строка, выглядящая как одно слово, есть один токен
  EXPECTED: FAIL_SINGLE_TOKEN_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как срезать или отклонять мягкий перенос (и семейство невидимых разделителей) внутри токенов до подстрочного сопоставления и сравнения, сохраняя легитимные подсказки переноса в отображаемом тексте?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (нормализатор, удаляющий мягкие переносы из ключей сопоставления/сравнения, оставляя их только в слое отображения — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «SHY — условная невидимка: не реальный дефис, не всегда невидим и не ловится фильтром только-U+002D».
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
