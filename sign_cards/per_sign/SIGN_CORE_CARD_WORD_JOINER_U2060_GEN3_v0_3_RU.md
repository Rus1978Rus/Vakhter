PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_WORD_JOINER_U2060_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
TRANSLATION_NOTE: Русский оригинал (авторитетный). Английское зеркало — SIGN_CORE_CARD_WORD_JOINER_U2060_GEN3_v0_3_EN. Кодпойнты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_WORD_JOINER_U2060_GEN3_v0_3_RU
CODEPOINT: U+2060
VISIBLE_FORM: ⟨WJ⟩
UNICODE_NAME: WORD JOINER
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: соединитель слов / невидимый неразрывный клей (инверсия ZWSP; замена FEFF-как-ZWNBSP)
CATEGORY_ROADMAP: LLM (invisible zero-width injection) · PHAGO: — (маскировка токена)
GLYPH_NOTE: VISIBLE_FORM использует маркер ⟨WJ⟩; сам знак (U+2060) — невидимый Format-символ (Cf) с нулевым продвижением и НИКОГДА не пишется буквально. Примеры используют ⟨WJ⟩/%E2%81%A0, но не байт. WJ запрещает перенос строки в своей позиции; он НЕ соединяет глифы как ZWJ.

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
VISIBLE_FORM: ⟨WJ⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: WJ_FORM ≠ EFFECT
SIGN_CATEGORY:
  - невидимый Format-символ нулевого продвижения, ЗАПРЕЩАЮЩИЙ перенос строки в своей позиции («клей»)
  - инверсия ZWSP: ZWSP разрешает перенос, WJ его предотвращает
  - рекомендуемая замена U+FEFF, используемого как неразрывный пробел нулевой ширины
  - (при злоупотреблении) невидимый клей, вставленный в идентификатор/ключевое слово для победы над сопоставлением, без видимой подсказки

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — непечатаемость не делает знак инертным
  2. NOT_ZERO_WIDTH_MEANS_ABSENT — нулевая ширина продвижения не означает, что байта нет
  3. NOT_ZWSP_INVERSE_MEANS_SAFE — быть инверсией ZWSP (неразрывность vs перенос) не делает его безобидным; это всё равно невидимый внутренний символ
  4. NOT_A_GLYPH_JOINER — несмотря на «joiner» в названии, он НЕ комбинирует глифы как ZWJ; он лишь запрещает перенос
  5. NOT_ENCODED_SAFE — «%E2%81%A0» может быть декодирован обратно в WJ позже
  6. NOT_AUTHORITY — он не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сам по себе он ничего не исполняет; он обманывает фильтры и читателей
  8. NOT_TRUST_SIGNAL — он не повышает доверие
  9. NOT_BOM — U+2060 не есть маркер порядка байтов; фильтр, реагирующий только на U+FEFF, его пропускает
  10. NOT_SANITIZED_PROOF — присутствие символа не означает, что ввод санирован
  11. NOT_SINGLE_TOKEN_PROOF — «ad⟨WJ⟩min» может отображаться как «admin», но сравниваться неравно

BASE_FORMULAS:
  WJ_FORM ≠ EFFECT
  WJ_FORM ≠ ZERO_WIDTH_MEANS_ABSENT_PROOF
  WJ_FORM ≠ ZWSP_INVERSE_MEANS_SAFE_PROOF
  WJ_FORM ≠ GLYPH_JOINER_PROOF
  WJ_FORM ≠ ENCODED_SAFETY_PROOF
  WJ_FORM ≠ AUTHORITY
  WJ_FORM ≠ EXECUTION_TRIGGER
  WJ_FORM ≠ BOM_PROOF
  WJ_FORM ≠ INVISIBLE_HARMLESS_PROOF
  WJ_FORM ≠ SANITIZED_PROOF
  WJ_FORM ≠ SINGLE_TOKEN_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: WJ (ZONE_1) имеет параллельные функции (легитимный неразрывный клей vs. невидимая инъекция в идентификатор), сосуществующие без культурной прецессии. Полисемия стабильного Format-символа.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: control подавления переноса строки без жестового предшественника; злоупотребление через инъекцию в идентификатор надстроено цифровой эпохой параллельно с легитимной неразрывной типографикой.

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
    INPUT: "WJ is U+2060 in Unicode"
    CONTEXT: именование символа в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: WJ_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "a word joiner forbids a line break at its position"
    CONTEXT: описание функции неразрывности в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: WJ_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <WJ> here"
    CONTEXT: документационный маркер, не байт
    EXPECTED: INFO
    RISK: NONE
    GUARD: WJ_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "it replaces FEFF used as a no-break space"
    CONTEXT: описание рекомендуемого современного использования в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: WJ_FORM ≠ BOM_PROOF
  SAFE_CASE_005:
    INPUT: "it is the inverse of a zero width space"
    CONTEXT: отличие от ZWSP в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: WJ_FORM ≠ ZWSP_INVERSE_MEANS_SAFE_PROOF
  SAFE_CASE_006:
    INPUT: "it does not combine glyphs the way a zero width joiner does"
    CONTEXT: отличие от ZWJ в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: WJ_FORM ≠ GLYPH_JOINER_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: KEYWORD_SPLIT
    INPUT: "jav<WJ>ascript: in a URL scheme check"
    CONTEXT: WJ разбивает ключевое слово, чтобы подстрочный блоклист не совпал
    RISK: HIGH
    ATTACK: блоклист упускает «javascript», пока снисходительный парсер игнорирует WJ
    GUARD: WJ_FORM ≠ SINGLE_TOKEN_PROOF
  RISK_CASE_002:
    NAME: INVISIBLE_IN_IDENTIFIER
    INPUT: "ad<WJ>min vs admin (look-alike username)"
    CONTEXT: WJ внутри ASCII-идентификатора делает его неравным при одинаковом виде
    RISK: HIGH
    ATTACK: «ad<WJ>min» регистрируется как двойник «admin» для выдачи себя за другого
    GUARD: WJ_FORM ≠ ZERO_WIDTH_MEANS_ABSENT_PROOF
  RISK_CASE_003:
    NAME: BOM_ONLY_FILTER_GAP
    INPUT: "input passing a filter that strips only U+FEFF"
    CONTEXT: WJ проскакивает фильтр, знающий только форму BOM
    RISK: MEDIUM
    ATTACK: фильтр, реагирующий на U+FEFF, упускает U+2060, так что невидимый клей выживает
    GUARD: WJ_FORM ≠ BOM_PROOF
  RISK_CASE_004:
    NAME: ENCODED_WJ_BYPASS
    INPUT: "value%E2%81%A0tail (with a later decode)"
    CONTEXT: percent-кодированный WJ, декодируемый обратно перед использованием
    RISK: HIGH
    ATTACK: «%E2%81%A0» декодируется в WJ ПОСЛЕ проверки → скрытое разбиение возвращается
    GUARD: WJ_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: INVISIBLE_FAMILY_CONFLATION
    INPUT: "a filter treating WJ the same as ZWJ (both say 'joiner')"
    CONTEXT: наивный фильтр, смешивающий названия, неверно обрабатывает WJ
    RISK: MEDIUM
    ATTACK: правило, предполагающее, что WJ соединяет глифы, обрабатывает его неверно; он лишь запрещает перенос
    GUARD: WJ_FORM ≠ GLYPH_JOINER_PROOF
  RISK_CASE_006:
    NAME: HOMOGLYPH_STACK
    INPUT: "раy<WJ>раl (invisible glue + confusable letters combined)"
    CONTEXT: WJ в связке с похожими буквами для усиления подделки
    RISK: MEDIUM
    ATTACK: невидимый символ плюс буквы-двойники проводят враждебную строку через поверхностный обзор
    GUARD: WJ_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨ZWSP⟩
    CODEPOINT: U+200B
    NAME: ZERO WIDTH SPACE
    RISK: HIGH
    RULE: ZERO_WIDTH_SPACE ≠ WORD_JOINER (ZWSP разрешает перенос; WJ запрещает — обратная семантика, оба нулевой ширины)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨ZWNBSP⟩
    CODEPOINT: U+FEFF
    NAME: ZERO WIDTH NO-BREAK SPACE
    RISK: HIGH
    RULE: ZERO_WIDTH_NO_BREAK_SPACE ≠ WORD_JOINER (та же работа неразрывности, но U+FEFF дублирует BOM; WJ — рекомендуемая не-BOM форма)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨ZWJ⟩
    CODEPOINT: U+200D
    NAME: ZERO WIDTH JOINER
    RISK: MEDIUM
    RULE: ZERO_WIDTH_JOINER ≠ WORD_JOINER («joiner» только в названии: ZWJ комбинирует глифы, WJ запрещает перенос — разные уровни)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨NBSP⟩
    CODEPOINT: U+00A0
    NAME: NO-BREAK SPACE
    RISK: MEDIUM
    RULE: NO_BREAK_SPACE ≠ WORD_JOINER (NBSP — неразрывный пробел с видимым продвижением; WJ нулевой ширины)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨FA⟩
    CODEPOINT: U+2061
    NAME: FUNCTION APPLICATION
    RISK: LOW
    RULE: FUNCTION_APPLICATION ≠ WORD_JOINER (невидимый математический оператор, следующий в блоке; другое назначение, оба невидимы)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "it has zero width, so it is effectively not there"
    RESPONSE: WJ_FORM ≠ ZERO_WIDTH_MEANS_ABSENT_PROOF
    RULE: нулевая ширина продвижения — метрика отображения; байт присутствует в данных
  CG2:
    TRIGGER: "an invisible char cannot be dangerous"
    RESPONSE: WJ_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: невидимость ортогональна эффекту; WJ создаёт десинхрон фильтра/идентификатора
  CG3:
    TRIGGER: "we already strip the BOM, so we are covered"
    RESPONSE: WJ_FORM ≠ BOM_PROOF
    RULE: WJ — это U+2060, не U+FEFF; фильтр только-BOM его пропускает
  CG4:
    TRIGGER: "'%E2%81%A0' is safe forever"
    RESPONSE: WJ_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в WJ перед использованием
  CG5:
    TRIGGER: "it is a joiner, so it combines glyphs like ZWJ"
    RESPONSE: WJ_FORM ≠ GLYPH_JOINER_PROOF
    RULE: WJ лишь запрещает перенос строки; он не комбинирует глифы
  CG6:
    TRIGGER: "the string looks like admin, so it is admin"
    RESPONSE: WJ_FORM ≠ SINGLE_TOKEN_PROOF
    RULE: единство отображения не подразумевает равенство байтов; невидимый символ может прятаться внутри

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "ASCII identifier with an interior WJ"
      NAME: SPLIT_IDENTIFIER
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: WJ внутри ASCII-имени/ключевого слова для победы над сопоставлением или выдачи себя за другого
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "WJ where a BOM-only filter runs"
      NAME: BOM_ONLY_GAP
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: невидимый клей, выживающий из-за срезания только U+FEFF
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "WJ + confusable letters"
      NAME: INVISIBLE_HOMOGLYPH_STACK
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: невидимый символ в связке с похожими буквами для подделки
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: не применимо — последовательности с WJ центральны для невидимого склеивания токенов.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: WJ склеивает/маскирует токены (маскировка токена), но не имитирует существование верифицированной сущности. Его риски — десинхрон фильтра/парсера и путаница идентификаторов, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена WJ на ZWSP (U+200B) / ZWNBSP (U+FEFF) / NBSP (U+00A0) для смены невидимого байта / обхода WJ-только-фильтра
  A2: percent-кодирование "%E2%81%A0" для проскока мимо сканера сырых байтов
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: разбиение ключевого слова "jav<WJ>ascript:" для победы над подстрочным блоклистом
  B2: пробел фильтра только-BOM (WJ выживает у фильтра, срезающего только U+FEFF)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "ASCII identifier with an interior WJ" (SC1) — разбитый идентификатор
  C2: "WJ + confusable letters" (SC3) — невидимый гомоглиф-стек
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: WJ подан как безобидный «неразрывный клей» внутри враждебного поля
  D2: "%E2%81%A0" как «безопасный» кодированный текст с последующим декодом
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: невидимая путаница идентификаторов (ad<WJ>min vs admin)
  E2: N/A — вектор: смешение по названию с ZWJ, неверно обрабатывающее WJ
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
  CLAIM: срезание BOM покрывает и соединитель слов
  EXPECTED: FAIL_BOM_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%E2%81%A0" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: соединитель слов комбинирует глифы как соединитель нулевой ширины
  EXPECTED: FAIL_GLYPH_JOINER_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: строка, выглядящая как admin, есть admin
  EXPECTED: FAIL_SINGLE_TOKEN_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как обнаруживать всё невидимое неразрывное/клеевое семейство (2060, FEFF, 00A0 и родственники) и обеспечить единое решение по нормализации для фильтра и парсера, не реагируя только на U+FEFF?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (нормализатор, покрывающий весь невидимый набор — не только BOM — решающий срезать-или-отклонить один раз до и проверки, и исполнителя — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «WJ — инверсия ZWSP и не-BOM неразрывная форма; фильтр только-BOM его пропускает, и он не соединитель глифов вопреки названию».
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
