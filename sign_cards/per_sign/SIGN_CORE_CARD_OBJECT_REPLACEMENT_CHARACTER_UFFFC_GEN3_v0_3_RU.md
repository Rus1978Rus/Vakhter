PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_OBJECT_REPLACEMENT_CHARACTER_UFFFC_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
TRANSLATION_NOTE: Русский оригинал (авторитетный). Английское зеркало — SIGN_CORE_CARD_OBJECT_REPLACEMENT_CHARACTER_UFFFC_GEN3_v0_3_EN. Кодпойнты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_OBJECT_REPLACEMENT_CHARACTER_UFFFC_GEN3_v0_3_RU
CODEPOINT: U+FFFC
VISIBLE_FORM: ⟨OBJ⟩
UNICODE_NAME: OBJECT REPLACEMENT CHARACTER
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: символ замены объекта / плейсхолдер, замещающий внеполосный встроенный контент
CATEGORY_ROADMAP: LLM (embedded-object placeholder injection) · PHAGO: — (маскировка встроенной нагрузки)
GLYPH_NOTE: VISIBLE_FORM использует маркер ⟨OBJ⟩; сам знак (U+FFFC) — Symbol (категория So), обычно отображаемый как плейсхолдер-рамка, и НЕ пишется буквально — буквальный U+FFFC вставил бы плейсхолдер в этот документ. Примеры используют ⟨OBJ⟩/%EF%BF%BC, но не байт. Он отмечает позицию встроенного объекта (изображение/OLE/вложение), чей реальный контент едет внеполосно.

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
VISIBLE_FORM: ⟨OBJ⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: OBJ_FORM ≠ EFFECT
SIGN_CATEGORY:
  - плейсхолдер-Symbol (категория So), отмечающий, ГДЕ в тексте сидит встроенный объект
  - легитимное использование: представить позицию встроенного изображения / OLE-объекта / вложения в потоке форматированного текста
  - глиф-плейсхолдер НЕ есть объект; реальный встроенный контент несётся внеполосно
  - (при злоупотреблении) маркер скрытого встроенного контента, который представление простого текста не показывает, или токен, разрешаемый потребителем через загрузку/отрисовку объекта

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_THE_OBJECT — плейсхолдер замещает объект; фактический контент (изображение/OLE/вложение) находится в другом месте
  2. NOT_EMPTY — его присутствие означает, что встроенный контент прикреплён, а не что текст полон сам по себе
  3. NOT_PLAIN_TEXT_COMPLETE — извлечение простого текста показывает плейсхолдер, но отбрасывает встроенную нагрузку
  4. NOT_INERT_ON_RESOLVE — разрешение плейсхолдера может загрузить или отрисовать объект со своими рисками (SSRF, макрос, парсер)
  5. NOT_ENCODED_SAFE — «%EF%BF%BC» может быть декодирован обратно в плейсхолдер позже
  6. NOT_AUTHORITY — он не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сам по себе он ничего не исполняет; объект, на который он указывает, может
  8. NOT_TRUST_SIGNAL — он не повышает доверие
  9. NOT_A_SPACE — хотя часто отрисовывается как рамка/зазор, это плейсхолдер контента, не пробел
  10. NOT_SANITIZED_PROOF — присутствие символа не означает, что ввод (или встроенный объект) санирован
  11. NOT_SINGLE_STREAM_PROOF — видимый текст и встроенный объект — два потока; плейсхолдер связывает их, но не есть целое

BASE_FORMULAS:
  OBJ_FORM ≠ EFFECT
  OBJ_FORM ≠ THE_OBJECT_PROOF
  OBJ_FORM ≠ EMPTY_PROOF
  OBJ_FORM ≠ PLAIN_TEXT_COMPLETE_PROOF
  OBJ_FORM ≠ INERT_ON_RESOLVE_PROOF
  OBJ_FORM ≠ ENCODED_SAFETY_PROOF
  OBJ_FORM ≠ AUTHORITY
  OBJ_FORM ≠ EXECUTION_TRIGGER
  OBJ_FORM ≠ A_SPACE_PROOF
  OBJ_FORM ≠ SANITIZED_PROOF
  OBJ_FORM ≠ SINGLE_STREAM_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: OBJ (ZONE_1) имеет параллельные функции (легитимный плейсхолдер встроенного объекта vs. инъекция скрытого встроенного контента), сосуществующие без культурной прецессии. Полисемия стабильного символа-плейсхолдера.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: символ-плейсхолдер контента без жестового предшественника; злоупотребление через скрытый встроенный контент надстроено цифровой эпохой параллельно с легитимным встраиванием форматированного текста.

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
    INPUT: "OBJ is U+FFFC in Unicode"
    CONTEXT: именование символа в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: OBJ_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "the object replacement character marks an embedded object position"
    CONTEXT: описание легитимной функции в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: OBJ_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <OBJ> here"
    CONTEXT: документационный маркер, не байт
    EXPECTED: INFO
    RISK: NONE
    GUARD: OBJ_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "the placeholder is not the embedded object itself"
    CONTEXT: описание связи плейсхолдера в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: OBJ_FORM ≠ THE_OBJECT_PROOF
  SAFE_CASE_005:
    INPUT: "a plain-text extract shows the placeholder but not the object"
    CONTEXT: описание поведения извлечения в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: OBJ_FORM ≠ PLAIN_TEXT_COMPLETE_PROOF
  SAFE_CASE_006:
    INPUT: "it is a content placeholder, not whitespace"
    CONTEXT: отличие от пробела в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: OBJ_FORM ≠ A_SPACE_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: HIDDEN_EMBEDDED_CONTENT
    INPUT: "visible text plus an OBJ pointing to an out-of-band object"
    CONTEXT: встроенный объект, который обзор простого текста никогда не видит
    RISK: HIGH
    ATTACK: объект несёт данные/эксплойт, который текстовое представление отбрасывает, протаскивая его мимо шага «только по виду»
    GUARD: OBJ_FORM ≠ PLAIN_TEXT_COMPLETE_PROOF
  RISK_CASE_002:
    NAME: RESOLVE_SIDE_EFFECT
    INPUT: "a consumer that fetches/renders the object referenced by the placeholder"
    CONTEXT: разрешение плейсхолдера, запускающее сетевую загрузку или парсер
    RISK: HIGH
    ATTACK: разрешение объекта вызывает SSRF, запуск макроса или эксплойт парсера документов
    GUARD: OBJ_FORM ≠ INERT_ON_RESOLVE_PROOF
  RISK_CASE_003:
    NAME: STREAM_DESYNC
    INPUT: "the text stream and the object stream disagreeing on what is present"
    CONTEXT: проверка, читающая текст, но не встроенный объект
    RISK: HIGH
    ATTACK: чекер видит безобидный текст, рендерер/исполнитель видит враждебный объект → обход
    GUARD: OBJ_FORM ≠ SINGLE_STREAM_PROOF
  RISK_CASE_004:
    NAME: ENCODED_OBJ_BYPASS
    INPUT: "value%EF%BF%BCtail (with a later decode)"
    CONTEXT: percent-кодированный плейсхолдер, декодируемый обратно перед использованием
    RISK: MEDIUM
    ATTACK: «%EF%BF%BC» декодируется в плейсхолдер ПОСЛЕ проверки → ссылка на встроенный объект возвращается
    GUARD: OBJ_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: PLACEHOLDER_ASSUMED_EMPTY
    INPUT: "a pipeline treating an OBJ as an empty/whitespace slot"
    CONTEXT: предположение, что плейсхолдер ничего не несёт
    RISK: MEDIUM
    ATTACK: считаемый-пустым слот на деле привязывает реальный встроенный контент, обрабатываемый в другом месте
    GUARD: OBJ_FORM ≠ EMPTY_PROOF
  RISK_CASE_006:
    NAME: INVISIBLE_HOMOGLYPH_STACK
    INPUT: "раyраl<OBJ>... (placeholder + confusable letters combined)"
    CONTEXT: плейсхолдер в связке с похожими буквами для усиления подделки
    RISK: LOW
    ATTACK: плейсхолдер плюс буквы-двойники заставляют подделанную строку читаться как нормальная запись
    GUARD: OBJ_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨REPL⟩
    CODEPOINT: U+FFFD
    NAME: REPLACEMENT CHARACTER
    RISK: HIGH
    RULE: REPLACEMENT_CHARACTER ≠ OBJECT_REPLACEMENT_CHARACTER (U+FFFD отмечает ошибку декодирования / невалидный байт; U+FFFC отмечает валидный встроенный объект — противоположные смыслы, соседние кодпойнты)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨IAT⟩
    CODEPOINT: U+FFFB
    NAME: INTERLINEAR ANNOTATION TERMINATOR
    RISK: MEDIUM
    RULE: INTERLINEAR_ANNOTATION_TERMINATOR ≠ OBJECT_REPLACEMENT_CHARACTER (соседний аннотационный control; не плейсхолдер объекта)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨SUB⟩
    CODEPOINT: U+001A
    NAME: SUBSTITUTE
    RISK: MEDIUM
    RULE: SUBSTITUTE ≠ OBJECT_REPLACEMENT_CHARACTER (C0-control, исторически использовавшийся как замена; другой механизм)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨NBSP⟩
    CODEPOINT: U+00A0
    NAME: NO-BREAK SPACE
    RISK: LOW
    RULE: NO_BREAK_SPACE ≠ OBJECT_REPLACEMENT_CHARACTER (пробел, который может отрисоваться как похожий зазор; не плейсхолдер контента)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨GEOM-BOX⟩
    CODEPOINT: U+25A1
    NAME: WHITE SQUARE
    RISK: LOW
    RULE: WHITE_SQUARE ≠ OBJECT_REPLACEMENT_CHARACTER (видимый глиф рамки, за который плейсхолдер часто принимают; обычный геометрический символ)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "the placeholder is the object"
    RESPONSE: OBJ_FORM ≠ THE_OBJECT_PROOF
    RULE: он замещает объект, несомый внеполосно; глиф не есть контент
  CG2:
    TRIGGER: "the text extract is the whole message"
    RESPONSE: OBJ_FORM ≠ PLAIN_TEXT_COMPLETE_PROOF
    RULE: извлечение отбрасывает встроенный объект; плейсхолдер отмечает, чего не хватает
  CG3:
    TRIGGER: "resolving the placeholder is harmless"
    RESPONSE: OBJ_FORM ≠ INERT_ON_RESOLVE_PROOF
    RULE: загрузка/отрисовка объекта может вызвать SSRF, макрос или эксплойт парсера
  CG4:
    TRIGGER: "'%EF%BF%BC' is safe forever"
    RESPONSE: OBJ_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в плейсхолдер перед использованием
  CG5:
    TRIGGER: "an OBJ is an empty slot"
    RESPONSE: OBJ_FORM ≠ EMPTY_PROOF
    RULE: он привязывает реальный встроенный контент, обрабатываемый в другом месте
  CG6:
    TRIGGER: "text and object are one stream, so checking text is enough"
    RESPONSE: OBJ_FORM ≠ SINGLE_STREAM_PROOF
    RULE: объект — отдельный поток; проверка одного текста его упускает

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "text + OBJ + out-of-band object"
      NAME: EMBEDDED_PAYLOAD
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: встроенный объект, скрытый от обзора простого текста и разрешаемый рендерером
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "OBJ with a dangling/attacker-controlled object reference"
      NAME: RESOLVE_TARGET_ABUSE
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: плейсхолдер, указывающий на цель загрузки/разбора, управляемую атакующим
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "OBJ + confusable letters"
      NAME: PLACEHOLDER_HOMOGLYPH_STACK
      RISK_LEVEL: LOW
      POSSIBLE_CONTEXTS: плейсхолдер в связке с похожими буквами для подделки
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: не применимо — смысл плейсхолдера по своей природе о встроенном объекте, который он привязывает.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: OBJ привязывает внеполосную встроенную нагрузку (маскировка встроенной нагрузки), но не имитирует существование верифицированной сущности. Его риски — скрытый встроенный контент и побочные эффекты во время разрешения, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: путаница с REPLACEMENT CHARACTER (U+FFFD) / глифом рамки (U+25A1) для маскировки смысла плейсхолдера
  A2: percent-кодирование "%EF%BF%BC" для проскока мимо сканера сырых байтов
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: скрытый встроенный контент (OBJ, указывающий на объект, который текстовый обзор упускает)
  B2: побочный эффект разрешения (загрузка/отрисовка объекта вызывает SSRF/макрос/парсер)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "OBJ with a dangling/attacker-controlled object reference" (SC2) — злоупотребление целью разрешения
  C2: "text + OBJ + out-of-band object" (SC1) — встроенная нагрузка
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: OBJ подан как «пустая рамка», чтобы обозреватель счёл слот безобидным
  D2: "%EF%BF%BC" как «безопасный» кодированный текст с последующим декодом
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: протаскивание встроенной нагрузки, невидимое обзору «только текст»
  E2: N/A — вектор: десинхрон потоков (текст проверен, объект исполнен)
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: плейсхолдер есть встроенный объект
  EXPECTED: FAIL_THE_OBJECT_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: извлечение простого текста есть всё сообщение
  EXPECTED: FAIL_PLAIN_TEXT_COMPLETE_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: разрешение плейсхолдера инертно
  EXPECTED: FAIL_INERT_ON_RESOLVE_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%EF%BF%BC" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: OBJ есть пустой слот
  EXPECTED: FAIL_EMPTY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: текст и объект — единый поток
  EXPECTED: FAIL_SINGLE_STREAM_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как трактовать символ замены объекта как указатель на отдельный недоверенный встроенный поток — валидируя объект с той же строгостью, что и текст, и никогда не загружая/отрисовывая его неявно — не ломая легитимное встраивание форматированного текста?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (интегратор, привязывающий каждый OBJ к его встроенному объекту, валидирующий/сканирующий поток объекта и ставящий любую загрузку/отрисовку за явную политику — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «плейсхолдер не есть объект и не пуст; реальный встроенный контент — отдельный поток, который проверка только-текста и неявное разрешение оба обрабатывают неверно».
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
