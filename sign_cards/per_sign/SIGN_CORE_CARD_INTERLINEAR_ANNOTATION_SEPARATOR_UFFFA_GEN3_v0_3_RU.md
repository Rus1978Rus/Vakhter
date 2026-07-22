PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_INTERLINEAR_ANNOTATION_SEPARATOR_UFFFA_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
TRANSLATION_NOTE: Русский оригинал (авторитетный). Английское зеркало — SIGN_CORE_CARD_INTERLINEAR_ANNOTATION_SEPARATOR_UFFFA_GEN3_v0_3_EN. Кодпойнты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_INTERLINEAR_ANNOTATION_SEPARATOR_UFFFA_GEN3_v0_3_RU
CODEPOINT: U+FFFA
VISIBLE_FORM: ⟨IAS⟩
UNICODE_NAME: INTERLINEAR ANNOTATION SEPARATOR
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: разделитель интерлинейной аннотации / граница, где кончается базовый текст и начинается скрытая аннотация
CATEGORY_ROADMAP: LLM (invisible annotation-payload injection) · PHAGO: — (маскировка скрытой нагрузки)
GLYPH_NOTE: VISIBLE_FORM использует маркер ⟨IAS⟩; сам знак (U+FFFA) — невидимый Format-символ (Cf) и НИКОГДА не пишется буквально. Примеры используют ⟨IAS⟩/%EF%BF%BA, но не байт. Он делит базовый текст и аннотацию внутри спана якорь (U+FFF9) … терминатор (U+FFFB); всё после него до терминатора есть скрытая аннотация.

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
VISIBLE_FORM: ⟨IAS⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: IAS_FORM ≠ EFFECT
SIGN_CATEGORY:
  - невидимый Format-символ, ДЕЛЯЩИЙ аннотируемый базовый текст и аннотацию внутри аннотационного спана
  - легитимное (внутреннее) использование: отметить переход от базы к аннотации, между якорем и терминатором
  - он явно НЕ предназначен для обмена простым текстом (внутренняя, внеполосная конструкция)
  - (при злоупотреблении) граница, после которой начинается протащенная аннотационная нагрузка — край носителя, который обзор «только по виду» не переходит

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — непечатаемость не делает знак инертным
  2. NOT_FOR_INTERCHANGE — он определён для внутреннего использования; его присутствие в обмениваемом тексте аномально, не нормально
  3. NOT_BASE_IS_WHOLE — текст до разделителя это лишь база; аннотация после него — реальный контент
  4. NOT_ANCHOR — U+FFFA это разделитель, не открыватель (U+FFF9); он предполагает уже открытый спан
  5. NOT_ENCODED_SAFE — «%EF%BF%BA» может быть декодирован обратно в разделитель позже
  6. NOT_AUTHORITY — он не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сам по себе он ничего не исполняет; он ограничивает скрытую нагрузку
  8. NOT_TRUST_SIGNAL — он не повышает доверие
  9. NOT_TERMINATOR — он не закрывает спан; закрывает TERMINATOR (U+FFFB), и его отсутствие оставляет аннотацию открытой
  10. NOT_SANITIZED_PROOF — присутствие символа не означает, что ввод санирован
  11. NOT_SINGLE_TEXT_PROOF — видимый базовый текст не есть весь контент; скрытая аннотация следует за разделителем

BASE_FORMULAS:
  IAS_FORM ≠ EFFECT
  IAS_FORM ≠ FOR_INTERCHANGE_PROOF
  IAS_FORM ≠ BASE_IS_WHOLE_PROOF
  IAS_FORM ≠ ANCHOR_PROOF
  IAS_FORM ≠ ENCODED_SAFETY_PROOF
  IAS_FORM ≠ AUTHORITY
  IAS_FORM ≠ EXECUTION_TRIGGER
  IAS_FORM ≠ TERMINATOR_PROOF
  IAS_FORM ≠ INVISIBLE_HARMLESS_PROOF
  IAS_FORM ≠ SANITIZED_PROOF
  IAS_FORM ≠ SINGLE_TEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: IAS (ZONE_1) имеет параллельные функции (внутреннее деление база/аннотация vs. невидимая инъекция границы нагрузки), сосуществующие без культурной прецессии. Полисемия стабильного Format-символа.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: control деления аннотации без жестового предшественника; злоупотребление через границу нагрузки надстроено цифровой эпохой параллельно с внутренним использованием аннотации.

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
    INPUT: "IAS is U+FFFA in Unicode"
    CONTEXT: именование символа в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAS_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "the separator divides base text from annotation"
    CONTEXT: описание внутренней функции в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAS_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <IAS> here"
    CONTEXT: документационный маркер, не байт
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAS_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "it is not intended for plain-text interchange"
    CONTEXT: описание задуманной области в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAS_FORM ≠ FOR_INTERCHANGE_PROOF
  SAFE_CASE_005:
    INPUT: "it is the separator, not the anchor"
    CONTEXT: отличие от U+FFF9 в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAS_FORM ≠ ANCHOR_PROOF
  SAFE_CASE_006:
    INPUT: "it does not close the span"
    CONTEXT: отличие от терминатора в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAS_FORM ≠ TERMINATOR_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: PAYLOAD_AFTER_SEPARATOR
    INPUT: "base<IAS>hidden annotation payload up to the terminator"
    CONTEXT: аннотация после разделителя, несущая контент, который обзор «только по виду» не читает
    RISK: HIGH
    ATTACK: нагрузка после разделителя протаскивает данные/инструкции мимо шага «только по виду»
    GUARD: IAS_FORM ≠ BASE_IS_WHOLE_PROOF
  RISK_CASE_002:
    NAME: RENDER_DISAGREEMENT
    INPUT: "one consumer shows the base (before IAS), another the annotation (after IAS)"
    CONTEXT: два компонента разрешают спан по-разному вокруг разделителя
    RISK: HIGH
    ATTACK: проверка читает базу, исполнитель аннотацию → обход в этом пробеле
    GUARD: IAS_FORM ≠ SINGLE_TEXT_PROOF
  RISK_CASE_003:
    NAME: SEPARATOR_WITHOUT_ANCHOR
    INPUT: "an IAS with no preceding anchor"
    CONTEXT: блуждающий разделитель, на который снисходительный парсер всё же может среагировать
    RISK: MEDIUM
    ATTACK: разделитель вне контекста запускает обработку аннотации там, где ничего не открывалось
    GUARD: IAS_FORM ≠ ANCHOR_PROOF
  RISK_CASE_004:
    NAME: ENCODED_IAS_BYPASS
    INPUT: "value%EF%BF%BAtail (with a later decode)"
    CONTEXT: percent-кодированный разделитель, декодируемый обратно перед использованием
    RISK: HIGH
    ATTACK: «%EF%BF%BA» декодируется в разделитель ПОСЛЕ проверки → граница скрытой нагрузки возвращается
    GUARD: IAS_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: UNTERMINATED_ANNOTATION
    INPUT: "an IAS whose annotation is never closed by a terminator"
    CONTEXT: открытая аннотация, чья протяжённость зависит от потребителя
    RISK: MEDIUM
    ATTACK: незакрытая аннотация поглощает следующий текст по-разному в разных парсерах
    GUARD: IAS_FORM ≠ TERMINATOR_PROOF
  RISK_CASE_006:
    NAME: INVISIBLE_HOMOGLYPH_STACK
    INPUT: "раyраl<IAS>... (annotation control + confusable letters combined)"
    CONTEXT: разделитель в связке с похожими буквами для усиления подделки
    RISK: MEDIUM
    ATTACK: невидимый control плюс буквы-двойники проводят враждебную строку через поверхностный обзор
    GUARD: IAS_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨IAA⟩
    CODEPOINT: U+FFF9
    NAME: INTERLINEAR ANNOTATION ANCHOR
    RISK: HIGH
    RULE: INTERLINEAR_ANNOTATION_ANCHOR ≠ INTERLINEAR_ANNOTATION_SEPARATOR (открыватель спана; разделитель его предполагает и делит базу и аннотацию)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨IAT⟩
    CODEPOINT: U+FFFB
    NAME: INTERLINEAR ANNOTATION TERMINATOR
    RISK: HIGH
    RULE: INTERLINEAR_ANNOTATION_TERMINATOR ≠ INTERLINEAR_ANNOTATION_SEPARATOR (закрыватель; разделитель лишь делит, он не закрывает)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨TAG-SP⟩
    CODEPOINT: U+E0020
    NAME: TAG SPACE
    RISK: MEDIUM
    RULE: TAG_SPACE ≠ INTERLINEAR_ANNOTATION_SEPARATOR (tag-блочная невидимка, несущая ASCII; другой механизм протаскивания)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨ZWSP⟩
    CODEPOINT: U+200B
    NAME: ZERO WIDTH SPACE
    RISK: LOW
    RULE: ZERO_WIDTH_SPACE ≠ INTERLINEAR_ANNOTATION_SEPARATOR (одиночная невидимка точки переноса, не разделитель аннотации)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨OBJ⟩
    CODEPOINT: U+FFFC
    NAME: OBJECT REPLACEMENT CHARACTER
    RISK: LOW
    RULE: OBJECT_REPLACEMENT_CHARACTER ≠ INTERLINEAR_ANNOTATION_SEPARATOR (соседний спецсимвол, заменяющий встроенный объект; другое назначение)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "it is a normal interchange character"
    RESPONSE: IAS_FORM ≠ FOR_INTERCHANGE_PROOF
    RULE: он определён для внутреннего использования; в обмениваемом тексте он аномален
  CG2:
    TRIGGER: "an invisible char cannot be dangerous"
    RESPONSE: IAS_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: невидимость ортогональна эффекту; разделитель ограничивает скрытую нагрузку
  CG3:
    TRIGGER: "the base text is the whole content"
    RESPONSE: IAS_FORM ≠ BASE_IS_WHOLE_PROOF
    RULE: аннотация после разделителя — реальный контент, а не ничто
  CG4:
    TRIGGER: "'%EF%BF%BA' is safe forever"
    RESPONSE: IAS_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в разделитель перед использованием
  CG5:
    TRIGGER: "the separator opens the span"
    RESPONSE: IAS_FORM ≠ ANCHOR_PROOF
    RULE: якорь (U+FFF9) открывает; разделитель лишь делит уже открытый спан
  CG6:
    TRIGGER: "the separator closes the annotation"
    RESPONSE: IAS_FORM ≠ TERMINATOR_PROOF
    RULE: терминатор (U+FFFB) закрывает; без него аннотация остаётся открытой

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "IAA ... IAS <payload> IAT"
      NAME: HIDDEN_ANNOTATION_PAYLOAD
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: нагрузка после разделителя, скрытая от обзора «только по виду»
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "IAS with no anchor or no terminator"
      NAME: MALFORMED_SPAN
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: блуждающий/несбалансированный разделитель, обрабатываемый несогласованно в разных парсерах
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "IAS + confusable letters"
      NAME: INVISIBLE_HOMOGLYPH_STACK
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: аннотационный control в связке с похожими буквами для подделки
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: не применимо — смысл разделителя по своей природе о спане, который он делит.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: IAS ограничивает скрытую аннотационную нагрузку (маскировка скрытой нагрузки), но не имитирует существование верифицированной сущности. Его риски — протаскивание скрытой нагрузки и расхождение отображения, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена/комбинация с ANCHOR (U+FFF9) / TERMINATOR (U+FFFB) или другими невидимками для варьирования конструкции
  A2: percent-кодирование "%EF%BF%BA" для проскока мимо сканера сырых байтов
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: нагрузка после разделителя (скрытая аннотация, которую обзор «только по виду» упускает)
  B2: расхождение отображения (один потребитель читает базу, другой аннотацию)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "IAS with no anchor or no terminator" (SC2) — некорректный спан
  C2: "IAA ... IAS <payload> IAT" (SC1) — скрытая аннотационная нагрузка
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: IAS подан как «нормальный символ обмена», чтобы его нагрузка не трактовалась как аномалия
  D2: "%EF%BF%BA" как «безопасный» кодированный текст с последующим декодом
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: протаскивание скрытой нагрузки, невидимое обозревателю
  E2: N/A — вектор: разделитель без якоря, запускающий обработку аннотации вне контекста
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: это нормальный символ обмена
  EXPECTED: FAIL_FOR_INTERCHANGE_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: невидимый символ не может быть опасен
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: базовый текст есть весь контент
  EXPECTED: FAIL_BASE_IS_WHOLE_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%EF%BF%BA" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: разделитель открывает спан
  EXPECTED: FAIL_ANCHOR_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: разделитель закрывает аннотацию
  EXPECTED: FAIL_TERMINATOR_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как трактовать контролы интерлинейной аннотации (U+FFF9/FFFA/FFFB) как внеполосные аномалии в обмениваемом тексте — срезая или отклоняя весь спан, вынося на поверхность аннотацию после разделителя и отклоняя некорректные/несбалансированные спаны — не ломая легитимный внутренний конвейер аннотаций?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (нормализатор, спаривающий якорь-разделитель-терминатор, отклоняющий блуждающие/несбалансированные контролы и декодирующий-и-показывающий аннотационную нагрузку на границе обозреватель/модель — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «разделитель отмечает, где кончается база и начинается скрытая аннотация; базовый текст не есть весь контент».
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
