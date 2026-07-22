PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_ZERO_WIDTH_SPACE_U200B_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
TRANSLATION_NOTE: Русский оригинал (авторитетный). Английское зеркало — SIGN_CORE_CARD_ZERO_WIDTH_SPACE_U200B_GEN3_v0_3_EN. Кодпойнты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_ZERO_WIDTH_SPACE_U200B_GEN3_v0_3_RU
CODEPOINT: U+200B
VISIBLE_FORM: ⟨ZWSP⟩
UNICODE_NAME: ZERO WIDTH SPACE
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: пробел нулевой ширины / невидимый разделитель токенов (обход блоклиста)
CATEGORY_ROADMAP: LLM (invisible zero-width injection) · PHAGO: — (маскировка токена)
GLYPH_NOTE: VISIBLE_FORM использует маркер ⟨ZWSP⟩; сам знак (U+200B) — невидимый Format-символ (Cf) с нулевой шириной, и НИКОГДА не пишется буквально — буквальный ZWSP молча разбил бы токены в этом документе. Примеры используют ⟨ZWSP⟩/%E2%80%8B, но не байт.

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
VISIBLE_FORM: ⟨ZWSP⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: ZWSP_FORM ≠ EFFECT
SIGN_CATEGORY:
  - невидимый Format-символ нулевой ширины и нулевого продвижения (точка возможного переноса)
  - легитимное типографское использование (разрешить перенос внутри длинного неразрывного токена/URL)
  - (при злоупотреблении) невидимый разделитель токенов, разбивающий ключевое слово, чтобы совпадение блоклиста провалилось
  - (при злоупотреблении) невидимая нагрузка, переживающая обзор «только по виду», пока парсер её игнорирует

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — непечатаемость не делает знак инертным
  2. NOT_ZERO_WIDTH_MEANS_ABSENT — нулевая ширина продвижения не означает, что байта нет
  3. NOT_WHITESPACE_EQUIVALENT — это не обычный пробел; блоклист/токенизатор, трактующий его как разделитель или игнорирующий его, расходятся, вызывая десинхрон
  4. NOT_DISPLAY_ONLY — читатель не видит ничего, но байты проходят сквозь разбор
  5. NOT_ENCODED_SAFE — «%E2%80%8B» может быть декодирован обратно в ZWSP позже
  6. NOT_AUTHORITY — он не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сам по себе он ничего не исполняет; он обманывает фильтры и читателей
  8. NOT_TRUST_SIGNAL — он не повышает доверие
  9. NOT_NORMALIZED_AWAY_PROOF — присутствие знака не означает, что нормализация его удалила
  10. NOT_SANITIZED_PROOF — присутствие символа не означает, что ввод санирован
  11. NOT_SINGLE_TOKEN_PROOF — «jav⟨ZWSP⟩ascript» может отображаться как одно слово, но разбираться как два (или наоборот)

BASE_FORMULAS:
  ZWSP_FORM ≠ EFFECT
  ZWSP_FORM ≠ ZERO_WIDTH_MEANS_ABSENT_PROOF
  ZWSP_FORM ≠ WHITESPACE_EQUIVALENT_PROOF
  ZWSP_FORM ≠ DISPLAY_ONLY_PROOF
  ZWSP_FORM ≠ ENCODED_SAFETY_PROOF
  ZWSP_FORM ≠ AUTHORITY
  ZWSP_FORM ≠ EXECUTION_TRIGGER
  ZWSP_FORM ≠ NORMALIZED_AWAY_PROOF
  ZWSP_FORM ≠ INVISIBLE_HARMLESS_PROOF
  ZWSP_FORM ≠ SANITIZED_PROOF
  ZWSP_FORM ≠ SINGLE_TOKEN_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: ZWSP (ZONE_1) имеет параллельные функции (легитимная точка переноса vs. невидимое разбиение токенов), сосуществующие без культурной прецессии. Полисемия стабильного Format-символа.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: форматирующий control нулевого продвижения без жестового предшественника; обход через разбиение токенов надстроен цифровой эпохой параллельно с легитимной типографикой точки переноса.

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
    INPUT: "ZWSP is U+200B in Unicode"
    CONTEXT: именование символа в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWSP_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "a zero width space is a line-break opportunity"
    CONTEXT: описание легитимного типографского использования в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWSP_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <ZWSP> here"
    CONTEXT: документационный маркер, не байт
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWSP_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "it lets a long URL wrap without a visible space"
    CONTEXT: описание свойства точки переноса в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWSP_FORM ≠ WHITESPACE_EQUIVALENT_PROOF
  SAFE_CASE_005:
    INPUT: "normalization or stripping may remove it"
    CONTEXT: описание санитайзера в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWSP_FORM ≠ NORMALIZED_AWAY_PROOF
  SAFE_CASE_006:
    INPUT: "it has zero advance width when rendered"
    CONTEXT: проза про метрику глифа
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWSP_FORM ≠ ZERO_WIDTH_MEANS_ABSENT_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: BLOCKLIST_KEYWORD_SPLIT
    INPUT: "jav<ZWSP>ascript: in a URL scheme check"
    CONTEXT: ZWSP разбивает ключевое слово, чтобы подстрочный блоклист не совпал
    RISK: HIGH
    ATTACK: блоклист видит «jav» + «ascript» и упускает «javascript», пока снисходительный парсер их сшивает
    GUARD: ZWSP_FORM ≠ SINGLE_TOKEN_PROOF
  RISK_CASE_002:
    NAME: INVISIBLE_IN_IDENTIFIER
    INPUT: "admin<ZWSP> vs admin (two distinct usernames)"
    CONTEXT: невидимый символ делает два идентификатора неравными при одинаковом виде
    RISK: HIGH
    ATTACK: «admin<ZWSP>» регистрируется как двойник «admin» для выдачи себя за другого
    GUARD: ZWSP_FORM ≠ ZERO_WIDTH_MEANS_ABSENT_PROOF
  RISK_CASE_003:
    NAME: FILTER_PARSER_DESYNC
    INPUT: "a filter strips ZWSP but the downstream parser does not (or vice versa)"
    CONTEXT: две стадии расходятся в том, присутствует ли ZWSP
    RISK: HIGH
    ATTACK: проверка видит одну строку, исполнитель — другую → обход
    GUARD: ZWSP_FORM ≠ WHITESPACE_EQUIVALENT_PROOF
  RISK_CASE_004:
    NAME: ENCODED_ZWSP_BYPASS
    INPUT: "value%E2%80%8Btail (with a later decode)"
    CONTEXT: percent-кодированный ZWSP, декодируемый обратно перед использованием
    RISK: HIGH
    ATTACK: «%E2%80%8B» декодируется в ZWSP ПОСЛЕ проверки → разбиение токена возвращается
    GUARD: ZWSP_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: HOMOGLYPH_STACK
    INPUT: "раy<ZWSP>раl (invisible split + confusable letters combined)"
    CONTEXT: ZWSP в связке с похожими буквами для усиления подделки
    RISK: MEDIUM
    ATTACK: невидимое разбиение плюс буквы-двойники проводят враждебную строку через поверхностный обзор
    GUARD: ZWSP_FORM ≠ EFFECT
  RISK_CASE_006:
    NAME: INVISIBLE_FLOOD
    INPUT: "a run of many ZWSP inserted between every character"
    CONTEXT: массовая невидимая вставка, чтобы победить наивное сопоставление и раздуть длину
    RISK: MEDIUM
    ATTACK: каждое ключевое слово раскрошено на одиночные символы, так что ни одно подстрочное правило не совпадает
    GUARD: ZWSP_FORM ≠ SINGLE_TOKEN_PROOF

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨ZWNJ⟩
    CODEPOINT: U+200C
    NAME: ZERO WIDTH NON-JOINER
    RISK: HIGH
    RULE: ZERO_WIDTH_NON_JOINER ≠ ZERO_WIDTH_SPACE (ZWNJ управляет соединением лигатур; ZWSP — точка переноса — разная функция, оба невидимы)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨ZWJ⟩
    CODEPOINT: U+200D
    NAME: ZERO WIDTH JOINER
    RISK: HIGH
    RULE: ZERO_WIDTH_JOINER ≠ ZERO_WIDTH_SPACE (ZWJ форсирует соединение/эмодзи-последовательности; ZWSP разбивает — противоположное намерение, оба невидимы)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨WJ⟩
    CODEPOINT: U+2060
    NAME: WORD JOINER
    RISK: HIGH
    RULE: WORD_JOINER ≠ ZERO_WIDTH_SPACE (WJ запрещает перенос; ZWSP разрешает — обратная семантика, оба нулевой ширины)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨ZWNBSP⟩
    CODEPOINT: U+FEFF
    NAME: ZERO WIDTH NO-BREAK SPACE
    RISK: MEDIUM
    RULE: ZERO_WIDTH_NO_BREAK_SPACE ≠ ZERO_WIDTH_SPACE (U+FEFF также служит BOM; другая роль, оба невидимы)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨SP⟩
    CODEPOINT: U+0020
    NAME: SPACE
    RISK: LOW
    RULE: SPACE ≠ ZERO_WIDTH_SPACE (обычный пробел с видимым продвижением, не control нулевой ширины)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "it has zero width, so it is effectively not there"
    RESPONSE: ZWSP_FORM ≠ ZERO_WIDTH_MEANS_ABSENT_PROOF
    RULE: нулевая ширина продвижения — метрика отображения; байт присутствует в данных
  CG2:
    TRIGGER: "an invisible char cannot be dangerous"
    RESPONSE: ZWSP_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: невидимость ортогональна эффекту; ZWSP создаёт десинхрон фильтра/парсера
  CG3:
    TRIGGER: "it is just a space, treat it like whitespace"
    RESPONSE: ZWSP_FORM ≠ WHITESPACE_EQUIVALENT_PROOF
    RULE: это не обычный пробел; стадии расходятся по нему, вызывая десинхрон
  CG4:
    TRIGGER: "'%E2%80%8B' is safe forever"
    RESPONSE: ZWSP_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в ZWSP перед использованием
  CG5:
    TRIGGER: "normalization always strips it"
    RESPONSE: ZWSP_FORM ≠ NORMALIZED_AWAY_PROOF
    RULE: не все конвейеры нормализуют; присутствие не подразумевает удаление
  CG6:
    TRIGGER: "the string looks like one word, so it is one token"
    RESPONSE: ZWSP_FORM ≠ SINGLE_TOKEN_PROOF
    RULE: единство отображения не подразумевает единство токена; невидимое разбиение может прятаться внутри

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "keyword with an interior ZWSP"
      NAME: SPLIT_KEYWORD
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: ZWSP внутри заблокированного ключевого слова для обхода подстрочного совпадения
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "ZWSP between every character"
      NAME: INVISIBLE_FLOOD
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: массовая вставка, крошащая все токены
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "ZWSP + confusable letters"
      NAME: INVISIBLE_HOMOGLYPH_STACK
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: невидимое разбиение в связке с похожими буквами для подделки
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: не применимо — последовательности с ZWSP центральны для невидимого разбиения токенов.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: ZWSP разбивает/маскирует токены (маскировка токена), но не имитирует существование верифицированной сущности. Его риски — десинхрон фильтра/парсера и путаница идентификаторов, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена ZWSP на ZWNJ (U+200C) / WJ (U+2060) / ZWNBSP (U+FEFF) для смены невидимого байта / обхода ZWSP-только-фильтра
  A2: percent-кодирование "%E2%80%8B" для проскока мимо сканера сырых байтов
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: разбиение ключевого слова "jav<ZWSP>ascript:" для победы над подстрочным блоклистом
  B2: десинхрон фильтра/парсера (одна стадия срезает ZWSP, другая — нет)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "ZWSP between every character" (SC2) — невидимый флуд, крошащий токены
  C2: "keyword with an interior ZWSP" (SC1) — разбитое ключевое слово
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: ZWSP подан как безобидная «точка переноса» внутри враждебного поля
  D2: "%E2%80%8B" как «безопасный» кодированный текст с последующим декодом
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: невидимая путаница идентификаторов (admin<ZWSP> vs admin)
  E2: N/A — вектор: невидимое разбиение, побеждающее наивный сопоставитель
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: нулевая ширина означает, что символ фактически отсутствует
  EXPECTED: FAIL_ZERO_WIDTH_MEANS_ABSENT_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: невидимый символ не может быть опасен
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: ZWSP эквивалентен обычному пробелу
  EXPECTED: FAIL_WHITESPACE_EQUIVALENT_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%E2%80%8B" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: нормализация всегда срезает ZWSP
  EXPECTED: FAIL_NORMALIZED_AWAY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: строка, выглядящая как одно слово, есть один токен
  EXPECTED: FAIL_SINGLE_TOKEN_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как обнаруживать невидимые символы нулевой ширины (200B-200D, 2060, FEFF) внутри токенов и обеспечить единое решение по нормализации для фильтра и парсера, без ложных срабатываний на легитимных точках переноса и требуемых письменностью джойнерах?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (нормализатор, решающий один раз — срезать-или-отклонить невидимки до и проверки, и исполнителя, с allowlist для письменностей, требующих ZWNJ/ZWJ — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «нулевая ширина — метрика отображения, не отсутствие; невидимые разбиения ломают подстрочное сопоставление и десинхронизируют стадии».
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
