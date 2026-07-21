PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_VARIATION_SELECTOR_16_UFE0F_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: Русский оригинал (authoritative). Английское зеркало — SIGN_CORE_CARD_VARIATION_SELECTOR_16_UFE0F_GEN3_v0_3_EN. Кодпоинты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_VARIATION_SELECTOR_16_UFE0F_GEN3_v0_3_RU
CODEPOINT: U+FE0F
VISIBLE_FORM: ⟨VS16⟩
UNICODE_NAME: VARIATION SELECTOR-16
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: селектор вариации-16 / emoji-презентация и невидимый носитель
CATEGORY_ROADMAP: LLM (невидимый Mn-носитель, путаница презентации) · PHAGO: — (носитель / модификатор презентации)
GLYPH_NOTE: VISIBLE_FORM использует маркер ⟨VS16⟩; сам знак (U+FE0F) — невидимая nonspacing-метка (Mn, Default_Ignorable) и НИКОГДА не пишется литералом здесь. Примеры используют ⟨VS16⟩/%EF%B8%8F, не байт.

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
VISIBLE_FORM: ⟨VS16⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: VS16_FORM ≠ EFFECT
SIGN_CATEGORY:
  - селектор emoji-презентации (форсирует emoji-рендеринг базового символа)
  - невидимая nonspacing-метка (Mn), Default_Ignorable
  - компонент ZWJ emoji-последовательностей (эмодзи семьи/флагов/профессий)
  - (злоупотребление) невидимый носитель, дописанный для контрабанды или паддинга токена

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — то, что он непечатаемый, не делает его инертным
  2. NOT_PRESENTATION_ONLY — он может переключить базовый символ между text и emoji-рендерингом (рассинхрон отображения)
  3. NOT_ZERO_LENGTH — это реальный кодпоинт, меняющий длину байтов, хеши и сравнения
  4. NOT_TRIM_PROOF — «чистый» токен может нести невидимый хвостовой VS16
  5. NOT_ENCODED_SAFE — "%EF%B8%8F" может быть раскодирован обратно в VS16 позже
  6. NOT_AUTHORITY — не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сам по себе ничего не исполняет; он паддит/модифицирует рендеринг
  8. NOT_TRUST_SIGNAL — не повышает доверие
  9. NOT_IDENTIFIER_SAFE — дописанный VS16 делает два «одинаково выглядящих» идентификатора разными
  10. NOT_SANITIZED_PROOF — наличие VS16 не значит, что ввод санитизирован
  11. NOT_NORMALIZE_STABLE — наличие/отсутствие меняет идентичность emoji-последовательности между системами

BASE_FORMULAS:
  VS16_FORM ≠ EFFECT
  VS16_FORM ≠ PRESENTATION_ONLY_PROOF
  VS16_FORM ≠ ZERO_LENGTH_PROOF
  VS16_FORM ≠ TRIM_SAFETY_PROOF
  VS16_FORM ≠ ESCAPED_PROOF
  VS16_FORM ≠ ENCODED_SAFETY_PROOF
  VS16_FORM ≠ AUTHORITY
  VS16_FORM ≠ EXECUTION_TRIGGER
  VS16_FORM ≠ INVISIBLE_HARMLESS_PROOF
  VS16_FORM ≠ IDENTIFIER_EQUALITY_PROOF
  VS16_FORM ≠ SANITIZED_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: VS16 (ZONE_1) имеет параллельные функции (легитимная emoji-презентация vs невидимый носитель/паддинг), сосуществующие без культурной прецессии. Полисемия стабильного селектора вариации.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1
  NOTE: управляющая метка презентации без жестового предшественника; использование как носитель/контрабанда надстроено цифровой эпохой параллельно легитимному emoji-рендерингу.

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
    INPUT: "VS16 is U+FE0F in Unicode"
    CONTEXT: название селектора в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: VS16_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "the heart emoji uses a base char + VS16"
    CONTEXT: описание легитимной emoji-презентации в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: VS16_FORM ≠ PRESENTATION_ONLY_PROOF
  SAFE_CASE_003:
    INPUT: "the marker is written as <VS16> here"
    CONTEXT: документационный маркер, не байт
    EXPECTED: INFO
    RISK: NONE
    GUARD: VS16_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "variation selectors pick a glyph variant"
    CONTEXT: текст о селекторах вариации
    EXPECTED: INFO
    RISK: NONE
    GUARD: VS16_FORM ≠ EFFECT
  SAFE_CASE_005:
    INPUT: "ZWJ emoji sequences may include VS16"
    CONTEXT: описание легитимной структуры emoji-последовательности
    EXPECTED: INFO
    RISK: NONE
    GUARD: VS16_FORM ≠ ZERO_LENGTH_PROOF
  SAFE_CASE_006:
    INPUT: "VS15 selects text, VS16 selects emoji"
    CONTEXT: текст, противопоставляющий два селектора
    EXPECTED: INFO
    RISK: NONE
    GUARD: VS16_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: INVISIBLE_CARRIER_SMUGGLE
    INPUT: "admin<VS16><VS16><VS16> (невидимый паддинг после токена)"
    CONTEXT: VS16, повторённый для контрабанды невидимого содержимого мимо визуального ревью
    RISK: HIGH
    ATTACK: невидимые метки несут/паддят содержимое, которого человек не видит, но машина хранит/матчит
    GUARD: VS16_FORM ≠ INVISIBLE_HARMLESS_PROOF
  RISK_CASE_002:
    NAME: IDENTIFIER_LOOKALIKE_SPLIT
    INPUT: "user<VS16> vs user (два одинаково выглядящих, байт-разных имени)"
    CONTEXT: дописанный VS16, делающий два одинаково выглядящих идентификатора разными
    RISK: HIGH
    ATTACK: "user<VS16>" и "user" отображаются одинаково, но обходят проверку уникальности/allow-list
    GUARD: VS16_FORM ≠ IDENTIFIER_EQUALITY_PROOF
  RISK_CASE_003:
    NAME: PRESENTATION_FLIP_DECEPTION
    INPUT: "digit<VS16> rendered as an emoji instead of text"
    CONTEXT: VS16, переключающий рендеринг базового символа, чтобы скрыть/изменить его смысл
    RISK: MEDIUM
    ATTACK: базовый символ отображается как emoji, не совпадая с тем, что предполагает фильтр/читатель
    GUARD: VS16_FORM ≠ PRESENTATION_ONLY_PROOF
  RISK_CASE_004:
    NAME: TRIM_BYPASS_TRAILING_VS
    INPUT: "value<VS16> (невидимый хвостовой селектор переживает обрезку краёв)"
    CONTEXT: хвостовой VS16, который внешняя обрезка пропускает
    RISK: MEDIUM
    ATTACK: обрезка пробелов оставляет невидимый VS16, так что «очищенное» значение всё ещё отличается
    GUARD: VS16_FORM ≠ TRIM_SAFETY_PROOF
  RISK_CASE_005:
    NAME: ENCODED_VS_BYPASS
    INPUT: "token%EF%B8%8F (с поздним декодированием)"
    CONTEXT: percent-кодированный VS16, декодируемый обратно после проверки
    RISK: MEDIUM
    ATTACK: "%EF%B8%8F" декодируется в VS16 ПОСЛЕ валидации → носитель/расщепление идентификатора
    GUARD: VS16_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: EMOJI_SEQUENCE_TAMPER
    INPUT: "base<ZWJ>base<VS16> (манипулированная ZWJ+VS последовательность)"
    CONTEXT: VS16 в сочетании с ZWJ для создания неоднозначной/раздутой emoji-последовательности
    RISK: MEDIUM
    ATTACK: подделанная последовательность отображается по-разному между системами, рассинхронизируя отображение с байтами
    GUARD: VS16_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨VS15⟩
    CODEPOINT: U+FE0E
    NAME: VARIATION SELECTOR-15
    RISK: HIGH
    RULE: VARIATION_SELECTOR_15 ≠ VARIATION_SELECTOR_16 (text vs emoji презентация; противоположный рендер, та же невидимость)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨VS1⟩
    CODEPOINT: U+FE00
    NAME: VARIATION SELECTOR-1
    RISK: MEDIUM
    RULE: VARIATION_SELECTOR_1 ≠ VARIATION_SELECTOR_16 (другой селектор, который VS16-only фильтр пропускает)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨ZWJ⟩
    CODEPOINT: U+200D
    NAME: ZERO WIDTH JOINER
    RISK: HIGH
    RULE: ZERO_WIDTH_JOINER ≠ VARIATION_SELECTOR_16 (Cf-джойнер в тех же emoji-последовательностях; иной механизм, та же невидимость)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨VS17⟩
    CODEPOINT: U+E0100
    NAME: VARIATION SELECTOR-17
    RISK: LOW
    RULE: VARIATION_SELECTOR_17 ≠ VARIATION_SELECTOR_16 (идеографический селектор вариации, ещё один невидимый носитель)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨ZWSP⟩
    CODEPOINT: U+200B
    NAME: ZERO WIDTH SPACE
    RISK: MEDIUM
    RULE: ZERO_WIDTH_SPACE ≠ VARIATION_SELECTOR_16 (другой невидимый, который поверхностный «strip invisibles» может трактовать одинаково)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "VS16 меняет только презентацию, значит косметика"
    RESPONSE: VS16_FORM ≠ PRESENTATION_ONLY_PROOF
    RULE: он переключает text↔emoji рендеринг и паддит байты; сдвигаются и отображение, и идентичность
  CG2:
    TRIGGER: "невидимая метка не может быть опасной"
    RESPONSE: VS16_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: невидимость ортогональна эффекту; VS16 — реальный кодпоинт-носитель
  CG3:
    TRIGGER: "две одинаково выглядящие строки равны"
    RESPONSE: VS16_FORM ≠ IDENTIFIER_EQUALITY_PROOF
    RULE: дописанный VS16 делает похожие строки байт-разными (обход уникальности)
  CG4:
    TRIGGER: "'%EF%B8%8F' безопасен навсегда"
    RESPONSE: VS16_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в VS16 перед приёмником
  CG5:
    TRIGGER: "обрезка значения удаляет селектор"
    RESPONSE: VS16_FORM ≠ TRIM_SAFETY_PROOF
    RULE: обрезка краёв оставляет невидимый хвостовой VS16
  CG6:
    TRIGGER: "наличие VS16 значит, что ввод санитизирован"
    RESPONSE: VS16_FORM ≠ SANITIZED_PROOF
    RULE: наличие знака ничего не говорит о санитизации

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "base + VS16"
      NAME: PRESENTATION_FLIP
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: форсирование emoji-рендеринга базового символа для изменения его читаемого смысла
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "ZWJ + base + VS16"
      NAME: EMOJI_SEQUENCE_CRAFT
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: создание неоднозначной/раздутой ZWJ emoji-последовательности
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "VS16 x N"
      NAME: INVISIBLE_PADDING
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: повторяющиеся невидимые метки для контрабанды/паддинга содержимого
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — последовательности с VS16 центральны для невидимого носителя / обмана презентации.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: VS16 модифицирует презентацию или несёт невидимое содержимое, но не имитирует существование верифицированной сущности. Его риски — носитель/расщепление идентификатора/рассинхрон презентации, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена VS16 на VS15 (U+FE0E) / VS1 (U+FE00) для обхода VS16-only фильтра
  A2: percent-кодирование "%EF%B8%8F" для проскальзывания мимо raw-byte скана
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: контрабанда невидимого носителя admin<VS16><VS16><VS16>
  B2: расщепление идентификатора-двойника user<VS16> vs user
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "base + VS16" (SC1) — переключение презентации
  C2: "VS16 x N" (SC3) — невидимый паддинг
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: VS16 подан как безобидная emoji-презентация внутри поля идентификатора
  D2: "%EF%B8%8F" как «безопасный» кодированный текст с поздним декодированием
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: обход уникальности через невидимое расщепление имени пользователя
  E2: N/A — вектор: переключение презентации, рассинхронизирующее предположение фильтра с рендером
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: VS16 — косметика только презентации
  EXPECTED: FAIL_PRESENTATION_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: невидимая метка не может быть опасной
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: две одинаково выглядящие строки равны
  EXPECTED: FAIL_IDENTIFIER_EQUALITY_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%EF%B8%8F" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: обрезка удаляет селектор
  EXPECTED: FAIL_TRIM_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: наличие VS16 доказывает санитизацию ввода
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как нормализовать/отвергать VS16 в идентификаторах и учётных данных (байт-равенство после NFC, стирать лишние селекторы) без поломки легитимного emoji-рендеринга в отображаемом тексте?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (канонизация идентификаторов + emoji-осведомлённый allow-контекст + стирание лишних селекторов вне валидных emoji-последовательностей — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «VS16 — реальный невидимый носитель; look-alike ≠ байт-равно».
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
