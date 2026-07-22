PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_INTERLINEAR_ANNOTATION_TERMINATOR_UFFFB_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
TRANSLATION_NOTE: Русский оригинал (авторитетный). Английское зеркало — SIGN_CORE_CARD_INTERLINEAR_ANNOTATION_TERMINATOR_UFFFB_GEN3_v0_3_EN. Кодпойнты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_INTERLINEAR_ANNOTATION_TERMINATOR_UFFFB_GEN3_v0_3_RU
CODEPOINT: U+FFFB
VISIBLE_FORM: ⟨IAT⟩
UNICODE_NAME: INTERLINEAR ANNOTATION TERMINATOR
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: терминатор интерлинейной аннотации / закрыватель аннотационного спана (присутствие != баланс)
CATEGORY_ROADMAP: LLM (invisible annotation-span injection) · PHAGO: — (маскировка скрытой нагрузки)
GLYPH_NOTE: VISIBLE_FORM использует маркер ⟨IAT⟩; сам знак (U+FFFB) — невидимый Format-символ (Cf) и НИКОГДА не пишется буквально. Примеры используют ⟨IAT⟩/%EF%BF%BB, но не байт. Он закрывает спан интерлинейной аннотации, открытый якорем (U+FFF9) и разделённый разделителем (U+FFFA); он НЕ для обмена простым текстом.

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
VISIBLE_FORM: ⟨IAT⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: IAT_FORM ≠ EFFECT
SIGN_CATEGORY:
  - невидимый Format-символ, ЗАКРЫВАЮЩИЙ спан интерлинейной аннотации
  - легитимное (внутреннее) использование: завершить аннотацию, открытую якорем и разделённую разделителем
  - он явно НЕ предназначен для обмена простым текстом (внутренняя, внеполосная конструкция)
  - (при злоупотреблении) терминатор, чьё присутствие не доказывает сбалансированный спан, а отсутствие оставляет аннотацию открытой

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — непечатаемость не делает знак инертным
  2. NOT_FOR_INTERCHANGE — он определён для внутреннего использования; его присутствие в обмениваемом тексте аномально, не нормально
  3. NOT_BALANCED_PROOF — терминатор не доказывает, что ему предшествовал парный якорь/разделитель; присутствие не есть баланс
  4. NOT_ANCHOR — U+FFFB это закрыватель, не открыватель (U+FFF9)
  5. NOT_ENCODED_SAFE — «%EF%BF%BB» может быть декодирован обратно в терминатор позже
  6. NOT_AUTHORITY — он не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сам по себе он ничего не исполняет; он завершает скрытый спан
  8. NOT_TRUST_SIGNAL — он не повышает доверие
  9. NOT_SEPARATOR — он не делит базу и аннотацию; делит SEPARATOR (U+FFFA)
  10. NOT_SANITIZED_PROOF — присутствие символа не означает, что ввод санирован
  11. NOT_CONTENT_CLEARED_PROOF — закрытие спана не удаляет скрытую аннотацию, которую нёс спан

BASE_FORMULAS:
  IAT_FORM ≠ EFFECT
  IAT_FORM ≠ FOR_INTERCHANGE_PROOF
  IAT_FORM ≠ BALANCED_PROOF
  IAT_FORM ≠ ANCHOR_PROOF
  IAT_FORM ≠ ENCODED_SAFETY_PROOF
  IAT_FORM ≠ AUTHORITY
  IAT_FORM ≠ EXECUTION_TRIGGER
  IAT_FORM ≠ SEPARATOR_PROOF
  IAT_FORM ≠ INVISIBLE_HARMLESS_PROOF
  IAT_FORM ≠ SANITIZED_PROOF
  IAT_FORM ≠ CONTENT_CLEARED_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: IAT (ZONE_1) имеет параллельные функции (внутреннее закрытие аннотации vs. невидимая инъекция несбалансированного спана), сосуществующие без культурной прецессии. Полисемия стабильного Format-символа.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: control закрытия аннотации без жестового предшественника; злоупотребление через несбалансированный спан надстроено цифровой эпохой параллельно с внутренним использованием аннотации.

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
    INPUT: "IAT is U+FFFB in Unicode"
    CONTEXT: именование символа в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAT_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "the terminator closes an interlinear annotation span"
    CONTEXT: описание внутренней функции в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAT_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <IAT> here"
    CONTEXT: документационный маркер, не байт
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAT_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "it is not intended for plain-text interchange"
    CONTEXT: описание задуманной области в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAT_FORM ≠ FOR_INTERCHANGE_PROOF
  SAFE_CASE_005:
    INPUT: "it is the terminator, not the anchor"
    CONTEXT: отличие от U+FFF9 в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAT_FORM ≠ ANCHOR_PROOF
  SAFE_CASE_006:
    INPUT: "it does not divide base from annotation"
    CONTEXT: отличие от разделителя в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: IAT_FORM ≠ SEPARATOR_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: STRAY_TERMINATOR
    INPUT: "an IAT with no preceding anchor/separator"
    CONTEXT: одинокий терминатор, на который снисходительный парсер всё же может среагировать
    RISK: HIGH
    ATTACK: терминатор вне контекста завершает аннотационное состояние, которое никогда не открывалось, неверно отслеживая разбор
    GUARD: IAT_FORM ≠ BALANCED_PROOF
  RISK_CASE_002:
    NAME: PRESENCE_NOT_BALANCE
    INPUT: "a span that has a terminator but a mismatched or missing anchor"
    CONTEXT: трактовка присутствия терминатора как доказательства корректного спана
    RISK: HIGH
    ATTACK: терминатор принимается как сигнал баланса, так что некорректный спан принимается
    GUARD: IAT_FORM ≠ BALANCED_PROOF
  RISK_CASE_003:
    NAME: CONTENT_NOT_CLEARED
    INPUT: "an annotation closed by IAT whose hidden payload still rode through"
    CONTEXT: предположение, что закрытие спана удаляет протащенную аннотацию
    RISK: MEDIUM
    ATTACK: нагрузка уже была пронесена; терминатор лишь завершает спан, он не удаляет контент
    GUARD: IAT_FORM ≠ CONTENT_CLEARED_PROOF
  RISK_CASE_004:
    NAME: ENCODED_IAT_BYPASS
    INPUT: "value%EF%BF%BBtail (with a later decode)"
    CONTEXT: percent-кодированный терминатор, декодируемый обратно перед использованием
    RISK: HIGH
    ATTACK: «%EF%BF%BB» декодируется в терминатор ПОСЛЕ проверки → структура спана возвращается
    GUARD: IAT_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: INTERCHANGE_ANOMALY_IGNORED
    INPUT: "an IAT appearing in interchanged plain text"
    CONTEXT: конвейер, не трактующий внеполосный control как аномалию
    RISK: MEDIUM
    ATTACK: поскольку он не ожидается в обмене, обработка не определена и эксплуатируема
    GUARD: IAT_FORM ≠ FOR_INTERCHANGE_PROOF
  RISK_CASE_006:
    NAME: INVISIBLE_HOMOGLYPH_STACK
    INPUT: "раyраl<IAT>... (annotation control + confusable letters combined)"
    CONTEXT: терминатор в связке с похожими буквами для усиления подделки
    RISK: MEDIUM
    ATTACK: невидимый control плюс буквы-двойники проводят враждебную строку через поверхностный обзор
    GUARD: IAT_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨IAA⟩
    CODEPOINT: U+FFF9
    NAME: INTERLINEAR ANNOTATION ANCHOR
    RISK: HIGH
    RULE: INTERLINEAR_ANNOTATION_ANCHOR ≠ INTERLINEAR_ANNOTATION_TERMINATOR (открыватель; терминатор закрывает то, что открыл якорь)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨IAS⟩
    CODEPOINT: U+FFFA
    NAME: INTERLINEAR ANNOTATION SEPARATOR
    RISK: HIGH
    RULE: INTERLINEAR_ANNOTATION_SEPARATOR ≠ INTERLINEAR_ANNOTATION_TERMINATOR (разделитель между базой и аннотацией; терминатор лишь закрывает)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨OBJ⟩
    CODEPOINT: U+FFFC
    NAME: OBJECT REPLACEMENT CHARACTER
    RISK: MEDIUM
    RULE: OBJECT_REPLACEMENT_CHARACTER ≠ INTERLINEAR_ANNOTATION_TERMINATOR (соседний спецсимвол, заменяющий встроенный объект; не терминатор спана)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨PDI⟩
    CODEPOINT: U+2069
    NAME: POP DIRECTIONAL ISOLATE
    RISK: LOW
    RULE: POP_DIRECTIONAL_ISOLATE ≠ INTERLINEAR_ANNOTATION_TERMINATOR (терминатор bidi-изолята; другая закрывающая конструкция, где присутствие тоже не есть баланс)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨ZWSP⟩
    CODEPOINT: U+200B
    NAME: ZERO WIDTH SPACE
    RISK: LOW
    RULE: ZERO_WIDTH_SPACE ≠ INTERLINEAR_ANNOTATION_TERMINATOR (одиночная невидимка точки переноса, не закрыватель спана)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "it is a normal interchange character"
    RESPONSE: IAT_FORM ≠ FOR_INTERCHANGE_PROOF
    RULE: он определён для внутреннего использования; в обмениваемом тексте он аномален
  CG2:
    TRIGGER: "an invisible char cannot be dangerous"
    RESPONSE: IAT_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: невидимость ортогональна эффекту; блуждающий терминатор неверно отслеживает разбор спана
  CG3:
    TRIGGER: "a terminator means the span is balanced"
    RESPONSE: IAT_FORM ≠ BALANCED_PROOF
    RULE: присутствие терминатора не доказывает, что ему предшествовал парный якорь/разделитель
  CG4:
    TRIGGER: "'%EF%BF%BB' is safe forever"
    RESPONSE: IAT_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в терминатор перед использованием
  CG5:
    TRIGGER: "the terminator opens or divides the span"
    RESPONSE: IAT_FORM ≠ ANCHOR_PROOF
    RULE: якорь открывает, разделитель делит; терминатор лишь закрывает
  CG6:
    TRIGGER: "closing the span removes the hidden annotation"
    RESPONSE: IAT_FORM ≠ CONTENT_CLEARED_PROOF
    RULE: нагрузка уже была пронесена; закрытие не удаляет контент

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "IAA ... IAS ... IAT (balanced span)"
      NAME: CLOSED_ANNOTATION
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: корректный спан, чья аннотационная часть всё ещё скрыта от обзора «только по виду»
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "IAT with no anchor"
      NAME: STRAY_CLOSE
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: одинокий терминатор, неверно отслеживающий аннотационное состояние в разных парсерах
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "IAT + confusable letters"
      NAME: INVISIBLE_HOMOGLYPH_STACK
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: аннотационный control в связке с похожими буквами для подделки
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: не применимо — смысл терминатора по своей природе о спане, который он закрывает.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: IAT закрывает скрытый аннотационный спан (маскировка скрытой нагрузки), но не имитирует существование верифицированной сущности. Его риски — разбор несбалансированного спана и сохранение нагрузки, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена/комбинация с ANCHOR (U+FFF9) / SEPARATOR (U+FFFA) или другими невидимками для варьирования конструкции
  A2: percent-кодирование "%EF%BF%BB" для проскока мимо сканера сырых байтов
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: присутствие-не-баланс (терминатор принят как доказательство корректного спана)
  B2: контент-не-очищен (закрытие спана предполагается удаляющим протащенную аннотацию)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "IAT with no anchor" (SC2) — блуждающее закрытие
  C2: "IAA ... IAS ... IAT" (SC1) — закрытая аннотация, всё ещё прячущая нагрузку
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: IAT подан как «нормальный символ обмена», чтобы его спан не трактовался как аномалия
  D2: "%EF%BF%BB" как «безопасный» кодированный текст с последующим декодом
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: разбор несбалансированного спана через блуждающий терминатор
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
  CLAIM: терминатор доказывает, что спан сбалансирован
  EXPECTED: FAIL_BALANCED_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%EF%BF%BB" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: терминатор открывает или делит спан
  EXPECTED: FAIL_ANCHOR_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: закрытие спана удаляет скрытую аннотацию
  EXPECTED: FAIL_CONTENT_CLEARED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как обеспечить корректные тройки якорь-разделитель-терминатор в обмениваемом тексте — отклоняя блуждающие или несбалансированные терминаторы и не трактуя терминатор как доказательство баланса — вынося на поверхность любую аннотацию, которую нёс закрытый спан?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (стековый чекер, спаривающий якорь-разделитель-терминатор, отклоняющий несбалансированные/блуждающие контролы и декодирующий-и-показывающий аннотационную нагрузку на границе обозреватель/модель — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «терминатор закрывает, но не доказывает баланс; его присутствие не есть корректный спан, и закрытие не удаляет пронесённую аннотацию».
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
