PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_INTERLINEAR_ANNOTATION_ANCHOR_UFFF9_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
TRANSLATION_NOTE: Русский оригинал (авторитетный). Английское зеркало — SIGN_CORE_CARD_INTERLINEAR_ANNOTATION_ANCHOR_UFFF9_GEN3_v0_3_EN. Кодпойнты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_INTERLINEAR_ANNOTATION_ANCHOR_UFFF9_GEN3_v0_3_RU
CODEPOINT: U+FFF9
VISIBLE_FORM: ⟨IAA⟩
UNICODE_NAME: INTERLINEAR ANNOTATION ANCHOR
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: якорь интерлинейной аннотации / открыватель спана скрытой аннотации (не для обмена)
CATEGORY_ROADMAP: LLM (invisible annotation-span injection) · PHAGO: — (маскировка скрытой нагрузки)
GLYPH_NOTE: VISIBLE_FORM использует маркер ⟨IAA⟩; сам знак (U+FFF9) — невидимый Format-символ (Cf) и НИКОГДА не пишется буквально. Примеры используют ⟨IAA⟩/%EF%BF%B9, но не байт. Он открывает спан интерлинейной аннотации (с SEPARATOR U+FFFA и TERMINATOR U+FFFB), который НЕ предназначен для обмена простым текстом.

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
VISIBLE_FORM: ⟨IAA⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: IAA_FORM ≠ EFFECT
SIGN_CATEGORY:
  - невидимый Format-символ, ОТКРЫВАЮЩИЙ спан интерлинейной аннотации
  - легитимное (внутреннее) использование: отметить, где начинается аннотируемый базовый текст, в паре с SEPARATOR и TERMINATOR
  - он явно НЕ предназначен для обмена простым текстом (внутренняя, внеполосная конструкция)
  - (при злоупотреблении) открывает скрытый спан, чей аннотационный контент разные потребители показывают, скрывают или отбрасывают несогласованно → вектор троянской аннотации

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — непечатаемость не делает знак инертным
  2. NOT_FOR_INTERCHANGE — он определён для внутреннего использования; его присутствие в обмениваемом тексте аномально, не нормально
  3. NOT_EMPTY_SPAN — он открывает спан, способный нести скрытый аннотационный контент, а не ничто
  4. NOT_RENDERED_UNIFORMLY — некоторые потребители показывают базовый текст, некоторые аннотацию, некоторые отбрасывают спан → расхождение отображения
  5. NOT_ENCODED_SAFE — «%EF%BF%B9» может быть декодирован обратно в якорь позже
  6. NOT_AUTHORITY — он не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сам по себе он ничего не исполняет; он обрамляет скрытый спан
  8. NOT_TRUST_SIGNAL — он не повышает доверие
  9. NOT_SELF_CLOSING — незакрытый якорь (без TERMINATOR) оставляет открытый спан, чья протяжённость зависит от потребителя
  10. NOT_SANITIZED_PROOF — присутствие символа не означает, что ввод санирован
  11. NOT_SINGLE_TEXT_PROOF — видимый базовый текст не есть весь контент; скрытая аннотация едет внутри спана

BASE_FORMULAS:
  IAA_FORM ≠ EFFECT
  IAA_FORM ≠ FOR_INTERCHANGE_PROOF
  IAA_FORM ≠ EMPTY_SPAN_PROOF
  IAA_FORM ≠ RENDERED_UNIFORMLY_PROOF
  IAA_FORM ≠ ENCODED_SAFETY_PROOF
  IAA_FORM ≠ AUTHORITY
  IAA_FORM ≠ EXECUTION_TRIGGER
  IAA_FORM ≠ SELF_CLOSING_PROOF
  IAA_FORM ≠ INVISIBLE_HARMLESS_PROOF
  IAA_FORM ≠ SANITIZED_PROOF
  IAA_FORM ≠ SINGLE_TEXT_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: IAA (ZONE_1) имеет параллельные функции (внутреннее обрамление аннотации vs. невидимая инъекция скрытого спана), сосуществующие без культурной прецессии. Полисемия стабильного Format-символа.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: control обрамления аннотации без жестового предшественника; злоупотребление через инъекцию скрытого спана надстроено цифровой эпохой параллельно с внутренним использованием аннотации.

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
    INPUT: "IAA is U+FFF9 in Unicode"
    CONTEXT: именование символа в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAA_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "the anchor opens an interlinear annotation span"
    CONTEXT: описание внутренней функции в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAA_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <IAA> here"
    CONTEXT: документационный маркер, не байт
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAA_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "it is not intended for plain-text interchange"
    CONTEXT: описание задуманной области в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAA_FORM ≠ FOR_INTERCHANGE_PROOF
  SAFE_CASE_005:
    INPUT: "it pairs with a separator and a terminator"
    CONTEXT: описание структуры спана в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAA_FORM ≠ SELF_CLOSING_PROOF
  SAFE_CASE_006:
    INPUT: "a filter can strip the annotation controls"
    CONTEXT: описание аккуратной санитизации в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAA_FORM ≠ SANITIZED_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: HIDDEN_ANNOTATION_SMUGGLING
    INPUT: "visible base text plus a hidden annotation inside an IAA...SEP...TERM span"
    CONTEXT: аннотационный спан, несущий контент, который некоторые потребители не отображают
    RISK: HIGH
    ATTACK: скрытая аннотация протаскивает данные/инструкции мимо обзора «только по виду»
    GUARD: IAA_FORM ≠ SINGLE_TEXT_PROOF
  RISK_CASE_002:
    NAME: RENDER_DISAGREEMENT
    INPUT: "one consumer shows the base text, another the annotation"
    CONTEXT: два компонента разрешают спан по-разному
    RISK: HIGH
    ATTACK: проверка видит одну строку, исполнитель/рендерер другую → обход в этом пробеле
    GUARD: IAA_FORM ≠ RENDERED_UNIFORMLY_PROOF
  RISK_CASE_003:
    NAME: UNTERMINATED_ANCHOR_BLEED
    INPUT: "an IAA with no TERMINATOR"
    CONTEXT: открытый аннотационный спан, чья протяжённость зависит от потребителя
    RISK: MEDIUM
    ATTACK: незакрытый спан поглощает следующий текст по-разному в разных парсерах
    GUARD: IAA_FORM ≠ SELF_CLOSING_PROOF
  RISK_CASE_004:
    NAME: ENCODED_IAA_BYPASS
    INPUT: "value%EF%BF%B9tail (with a later decode)"
    CONTEXT: percent-кодированный якорь, декодируемый обратно перед использованием
    RISK: HIGH
    ATTACK: «%EF%BF%B9» декодируется в якорь ПОСЛЕ проверки → скрытый спан возвращается
    GUARD: IAA_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: INTERCHANGE_ANOMALY_IGNORED
    INPUT: "an IAA appearing in interchanged plain text"
    CONTEXT: конвейер, не трактующий внеполосный control как аномалию
    RISK: MEDIUM
    ATTACK: поскольку он не ожидается в обмене, обработка не определена и эксплуатируема
    GUARD: IAA_FORM ≠ FOR_INTERCHANGE_PROOF
  RISK_CASE_006:
    NAME: INVISIBLE_HOMOGLYPH_STACK
    INPUT: "раyраl<IAA>... (annotation control + confusable letters combined)"
    CONTEXT: якорь в связке с похожими буквами для усиления подделки
    RISK: MEDIUM
    ATTACK: невидимый control плюс буквы-двойники проводят враждебную строку через поверхностный обзор
    GUARD: IAA_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨IAS⟩
    CODEPOINT: U+FFFA
    NAME: INTERLINEAR ANNOTATION SEPARATOR
    RISK: HIGH
    RULE: INTERLINEAR_ANNOTATION_SEPARATOR ≠ INTERLINEAR_ANNOTATION_ANCHOR (разделитель, начинающий скрытую аннотацию; другая роль в том же спане)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨IAT⟩
    CODEPOINT: U+FFFB
    NAME: INTERLINEAR ANNOTATION TERMINATOR
    RISK: HIGH
    RULE: INTERLINEAR_ANNOTATION_TERMINATOR ≠ INTERLINEAR_ANNOTATION_ANCHOR (закрыватель; его присутствие отмечает, но не доказывает сбалансированный спан)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨TAG⟩
    CODEPOINT: U+E0001
    NAME: LANGUAGE TAG
    RISK: MEDIUM
    RULE: LANGUAGE_TAG ≠ INTERLINEAR_ANNOTATION_ANCHOR (другой внеполосный невидимый механизм протаскивания; другая конструкция)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨ZWSP⟩
    CODEPOINT: U+200B
    NAME: ZERO WIDTH SPACE
    RISK: LOW
    RULE: ZERO_WIDTH_SPACE ≠ INTERLINEAR_ANNOTATION_ANCHOR (одиночная невидимка точки переноса, не открыватель спана)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨OBJ⟩
    CODEPOINT: U+FFFC
    NAME: OBJECT REPLACEMENT CHARACTER
    RISK: LOW
    RULE: OBJECT_REPLACEMENT_CHARACTER ≠ INTERLINEAR_ANNOTATION_ANCHOR (соседний спецсимвол, заменяющий встроенный объект; другое назначение)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "it is a normal interchange character"
    RESPONSE: IAA_FORM ≠ FOR_INTERCHANGE_PROOF
    RULE: он определён для внутреннего использования; в обмениваемом тексте он аномален
  CG2:
    TRIGGER: "an invisible char cannot be dangerous"
    RESPONSE: IAA_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: невидимость ортогональна эффекту; якорь обрамляет скрытый спан
  CG3:
    TRIGGER: "the span is empty, so nothing is hidden"
    RESPONSE: IAA_FORM ≠ EMPTY_SPAN_PROOF
    RULE: он может нести реальный аннотационный контент, который некоторые потребители не показывают
  CG4:
    TRIGGER: "'%EF%BF%B9' is safe forever"
    RESPONSE: IAA_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в якорь перед использованием
  CG5:
    TRIGGER: "every consumer renders the span the same way"
    RESPONSE: IAA_FORM ≠ RENDERED_UNIFORMLY_PROOF
    RULE: потребители показывают базу, аннотацию или ничего — они расходятся
  CG6:
    TRIGGER: "the anchor closes itself"
    RESPONSE: IAA_FORM ≠ SELF_CLOSING_PROOF
    RULE: без TERMINATOR спан открыт и его протяжённость зависит от потребителя

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "IAA ... IAS ... IAT (full annotation span)"
      NAME: HIDDEN_ANNOTATION
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: сбалансированный спан, чья аннотационная часть скрыта от обзора «только по виду»
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "IAA with no IAT"
      NAME: UNTERMINATED_SPAN
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: открытый спан, поглощающий следующий текст по-разному в разных парсерах
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "IAA + confusable letters"
      NAME: INVISIBLE_HOMOGLYPH_STACK
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: аннотационный control в связке с похожими буквами для подделки
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: не применимо — смысл якоря по своей природе о спане, который он открывает.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: IAA обрамляет скрытую аннотационную нагрузку (маскировка скрытой нагрузки), но не имитирует существование верифицированной сущности. Его риски — протаскивание скрытого спана и расхождение отображения, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена/комбинация с SEPARATOR (U+FFFA) / TERMINATOR (U+FFFB) или другими невидимками для варьирования конструкции
  A2: percent-кодирование "%EF%BF%B9" для проскока мимо сканера сырых байтов
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: протаскивание скрытой аннотации (контент внутри IAA...SEP...TERM, который обзор «только по виду» упускает)
  B2: расхождение отображения (один потребитель показывает базу, другой аннотацию)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "IAA with no IAT" (SC2) — незакрытый спан
  C2: "IAA ... IAS ... IAT" (SC1) — скрытая аннотация
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: IAA подан как «нормальный символ обмена», чтобы его спан не трактовался как аномалия
  D2: "%EF%BF%B9" как «безопасный» кодированный текст с последующим декодом
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: протаскивание скрытой аннотации, невидимое обозревателю
  E2: N/A — вектор: игнорируемая аномалия обмена, оставляющая обработку неопределённой
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
  CLAIM: аннотационный спан пуст
  EXPECTED: FAIL_EMPTY_SPAN_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%EF%BF%B9" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: каждый потребитель отрисовывает спан идентично
  EXPECTED: FAIL_RENDERED_UNIFORMLY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: якорь закрывает себя сам
  EXPECTED: FAIL_SELF_CLOSING_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как трактовать контролы интерлинейной аннотации (U+FFF9/FFFA/FFFB) как внеполосные аномалии в обмениваемом тексте — срезая или отклоняя весь спан и вынося на поверхность любую скрытую аннотацию — не ломая легитимный внутренний конвейер аннотаций?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (нормализатор, отклоняющий/помечающий аннотационные спаны в обмене, спаривающий якорь-разделитель-терминатор и декодирующий-и-показывающий скрытую аннотацию на границе обозреватель/модель — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «якорь открывает скрытый, не-для-обмена аннотационный спан; его контент не есть видимый текст, и потребители отрисовывают его несогласованно».
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
