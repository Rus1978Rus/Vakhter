PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_RIGHT_TO_LEFT_ISOLATE_U2067_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
TRANSLATION_NOTE: Русский оригинал (авторитетный). Английское зеркало — SIGN_CORE_CARD_RIGHT_TO_LEFT_ISOLATE_U2067_GEN3_v0_3_EN. Кодпойнты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_RIGHT_TO_LEFT_ISOLATE_U2067_GEN3_v0_3_RU
CODEPOINT: U+2067
VISIBLE_FORM: ⟨RLI⟩
UNICODE_NAME: RIGHT-TO-LEFT ISOLATE
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: право-налево изолят / ограниченный по области bidi-разворот (зеркало LRI)
CATEGORY_ROADMAP: LLM (bidi isolate reorder, Trojan Source) · PHAGO: — (маскировка структуры)
GLYPH_NOTE: VISIBLE_FORM использует маркер ⟨RLI⟩; сам знак (U+2067) — невидимый Bidi_Control (Cf) и НИКОГДА не пишется буквально — буквальный RLI переупорядочил бы этот документ. Примеры используют ⟨RLI⟩/⟨PDI⟩/%E2%81%A7, но не байт.

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
VISIBLE_FORM: ⟨RLI⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: RLI_FORM ≠ EFFECT
SIGN_CATEGORY:
  - двунаправленный изолят (открывает RTL-прогон, изолированный от окружения)
  - Unicode Bidi_Control, современная рекомендуемая замена вложениям/оверрайдам
  - легитимная ограниченная по области RTL-раскладка (не влияет на соседей)
  - (при злоупотреблении) зеркало LRI — более новый control, который пропускает фильтр старых вложений/оверрайдов

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — непечатаемость не делает знак инертным
  2. NOT_ISOLATE_MEANS_SAFE — «рекомендуемый» ≠ безопасный; он всё равно переупорядочивает ВНУТРИ своей области и всё равно обманывает
  3. NOT_DISPLAY_ONLY — он переупорядочивает ВИЗУАЛЬНЫЙ прогон, при неизменных логических байтах (десинхрон)
  4. NOT_SCOPE_CONTAINS_ALL — незакрытый изолят всё равно «протекает» до конца абзаца
  5. NOT_ENCODED_SAFE — «%E2%81%A7» может быть декодирован обратно в изолят позже
  6. NOT_AUTHORITY — он не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сам по себе он ничего не исполняет; он обманывает читателя
  8. NOT_TRUST_SIGNAL — он не повышает доверие
  9. NOT_EMBEDDING_ONLY_FILTER_SAFE — фильтр, обрабатывающий только вложения/оверрайды (202A-202E), пропускает изоляты (2066-2069)
  10. NOT_SANITIZED_PROOF — присутствие изолята не означает, что ввод санирован
  11. NOT_BALANCED_PROOF — изоляту нужен парный PDI; его присутствие не есть баланс

BASE_FORMULAS:
  RLI_FORM ≠ EFFECT
  RLI_FORM ≠ ISOLATE_MEANS_SAFE_PROOF
  RLI_FORM ≠ DISPLAY_ONLY_PROOF
  RLI_FORM ≠ SCOPE_CONTAINMENT_PROOF
  RLI_FORM ≠ ENCODED_SAFETY_PROOF
  RLI_FORM ≠ AUTHORITY
  RLI_FORM ≠ EXECUTION_TRIGGER
  RLI_FORM ≠ EMBEDDING_ONLY_FILTER_PROOF
  RLI_FORM ≠ INVISIBLE_HARMLESS_PROOF
  RLI_FORM ≠ SANITIZED_PROOF
  RLI_FORM ≠ BALANCED_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: RLI (ZONE_1) имеет параллельные функции (легитимная ограниченная RTL-раскладка vs. обман визуального порядка внутри области), сосуществующие без культурной прецессии. Полисемия стабильного Bidi_Control.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: форматирующий изолят-control без жестового предшественника; применение «разворот-обман» надстроено цифровой эпохой параллельно с легитимной ограниченной раскладкой.

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
    INPUT: "RLI is U+2067 in Unicode"
    CONTEXT: именование control в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLI_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "isolates are the modern recommended bidi control"
    CONTEXT: описание легитимной ограниченной раскладки в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLI_FORM ≠ ISOLATE_MEANS_SAFE_PROOF
  SAFE_CASE_003:
    INPUT: "the marker is written as <RLI> here"
    CONTEXT: документационный маркер, не байт
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLI_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "an isolate does not affect surrounding text"
    CONTEXT: описание свойства ограничения области в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLI_FORM ≠ SCOPE_CONTAINMENT_PROOF
  SAFE_CASE_005:
    INPUT: "a properly terminated isolate (RLI...PDI)"
    CONTEXT: описание сбалансированного легитимного использования
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLI_FORM ≠ BALANCED_PROOF
  SAFE_CASE_006:
    INPUT: "the Bidirectional Algorithm scopes the isolate"
    CONTEXT: проза про UBA
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLI_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: LEGACY_FILTER_GAP
    INPUT: "input passing a strip that only handles 202A-202E"
    CONTEXT: изолят проскакивает фильтр, знающий только вложения/оверрайды
    RISK: HIGH
    ATTACK: более новый изолят (2066-2069) не смоделирован, поэтому разворот переживает очистку
    GUARD: RLI_FORM ≠ EMBEDDING_ONLY_FILTER_PROOF
  RISK_CASE_002:
    NAME: IN_SCOPE_CODE_REORDER
    INPUT: 'safe = true <RLI> // danger? <PDI>'
    CONTEXT: изолят переупорядочивает прогон кода внутри своей области
    RISK: HIGH
    ATTACK: даже ограниченный, изолят переупорядочивает видимые токены, так что логика ≠ отображение
    GUARD: RLI_FORM ≠ ISOLATE_MEANS_SAFE_PROOF
  RISK_CASE_003:
    NAME: UNTERMINATED_ISOLATE_BLEED
    INPUT: "label<RLI>rest of the paragraph with no PDI"
    CONTEXT: изолят без PDI, протекающий до конца абзаца
    RISK: HIGH
    ATTACK: незакрытый изолят переупорядочивает всё до конца абзаца, за пределами задуманной области
    GUARD: RLI_FORM ≠ SCOPE_CONTAINMENT_PROOF
  RISK_CASE_004:
    NAME: ISOLATE_TERMINATOR_MISMATCH
    INPUT: "RLI closed with <PDF> instead of PDI"
    CONTEXT: изолят закрыт неверным терминатором (PDF, не PDI)
    RISK: MEDIUM
    ATTACK: парсер, спаривающий изолят с PDF, неверно отслеживает вложенность и оставляет изолят открытым
    GUARD: RLI_FORM ≠ BALANCED_PROOF
  RISK_CASE_005:
    NAME: ENCODED_ISOLATE_BYPASS
    INPUT: "value%E2%81%A7tail (with a later decode)"
    CONTEXT: percent-кодированный RLI, декодируемый обратно перед отображением
    RISK: HIGH
    ATTACK: «%E2%81%A7» декодируется в изолят ПОСЛЕ проверки → обман разворота
    GUARD: RLI_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: BIDI_HOMOGLYPH_STACK
    INPUT: "раyраl<RLI> ... (bidi + confusable letters combined)"
    CONTEXT: изолят в связке с похожими буквами для усиления подделки
    RISK: MEDIUM
    ATTACK: изолят плюс буквы-двойники проводят враждебную строку через поверхностный визуальный обзор
    GUARD: RLI_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨LRI⟩
    CODEPOINT: U+2066
    NAME: LEFT-TO-RIGHT ISOLATE
    RISK: HIGH
    RULE: LEFT_TO_RIGHT_ISOLATE ≠ RIGHT_TO_LEFT_ISOLATE (зеркальный изолят, противоположное направление; наивный фильтр их смешивает)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨FSI⟩
    CODEPOINT: U+2068
    NAME: FIRST STRONG ISOLATE
    RISK: HIGH
    RULE: FIRST_STRONG_ISOLATE ≠ RIGHT_TO_LEFT_ISOLATE (FSI авто-выбирает направление по первому сильному символу — управляемо атакующим)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨RLE⟩
    CODEPOINT: U+202B
    NAME: RIGHT-TO-LEFT EMBEDDING
    RISK: MEDIUM
    RULE: RIGHT_TO_LEFT_EMBEDDING ≠ RIGHT_TO_LEFT_ISOLATE (вложение влияет на соседей; изолят ограничивает область — разные модели)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨PDI⟩
    CODEPOINT: U+2069
    NAME: POP DIRECTIONAL ISOLATE
    RISK: LOW
    RULE: POP_DIRECTIONAL_ISOLATE ≠ RIGHT_TO_LEFT_ISOLATE (терминатор, не открыватель)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨RLO⟩
    CODEPOINT: U+202E
    NAME: RIGHT-TO-LEFT OVERRIDE
    RISK: LOW
    RULE: RIGHT_TO_LEFT_OVERRIDE ≠ RIGHT_TO_LEFT_ISOLATE (оверрайд форсирует и влияет на соседей; изолят ограничивает область)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "isolates are recommended, so an isolate is safe"
    RESPONSE: RLI_FORM ≠ ISOLATE_MEANS_SAFE_PROOF
    RULE: рекомендован для корректности, не для иммунитета; он всё равно переупорядочивает внутри области и обманывает
  CG2:
    TRIGGER: "an invisible control char cannot be dangerous"
    RESPONSE: RLI_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: невидимость ортогональна эффекту; RLI создаёт визуально/логический десинхрон
  CG3:
    TRIGGER: "an isolate contains its effect, so nothing leaks"
    RESPONSE: RLI_FORM ≠ SCOPE_CONTAINMENT_PROOF
    RULE: незакрытый изолят протекает до конца абзаца
  CG4:
    TRIGGER: "'%E2%81%A7' is safe forever"
    RESPONSE: RLI_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в изолят перед отображением
  CG5:
    TRIGGER: "our bidi filter handles embeddings and overrides, so we are covered"
    RESPONSE: RLI_FORM ≠ EMBEDDING_ONLY_FILTER_PROOF
    RULE: изоляты (2066-2069) — отдельный, более новый диапазон, который старый фильтр пропускает
  CG6:
    TRIGGER: "the presence of an isolate means the input is sanitized"
    RESPONSE: RLI_FORM ≠ SANITIZED_PROOF
    RULE: присутствие знака ничего не говорит о санации

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "RLI ... PDI"
      NAME: BALANCED_ISOLATE_SPAN
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: ограниченный изолят-спан для переупорядочивания конкретного токена
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "RLI (no PDI)"
      NAME: UNTERMINATED_BLEED
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: изолят без терминатора, протекающий до конца абзаца
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "RLI ... PDF"
      NAME: WRONG_TERMINATOR
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: изолят, закрытый PDF вместо PDI, с неверным отслеживанием вложенности
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: не применимо — последовательности с RLI центральны для ограниченного обмана визуального порядка.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: RLI переупорядочивает ограниченный прогон (маскировка структуры), но не имитирует существование верифицированной сущности. Его риски — визуально/логический десинхрон, а не мимикрия сущности. (Подделка имени файла естественнее с оверрайдом; см. RLO/LRO.)
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена RLI на LRI (U+2066) / FSI (U+2068) для смены направления / обхода RLI-только-фильтра
  A2: percent-кодирование "%E2%81%A7" для проскока мимо сканера сырых байтов
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: пробел старого фильтра (изолят переживает очистку только 202A-202E)
  B2: разворот кода внутри области safe=true <RLI> // danger? <PDI>
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "RLI (no PDI)" (SC2) — незакрытое протекание до конца абзаца
  C2: "RLI ... PDF" (SC3) — неверный терминатор
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: RLI подан как безобидный «рекомендуемый безопасный» изолят внутри поля кода
  D2: "%E2%81%A7" как «безопасный» кодированный текст с последующим декодом
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: ограниченный разворот, обманывающий обозревателя
  E2: N/A — вектор: изолят более нового диапазона, обходящий старый embedding-only фильтр
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: изолят безопасен, потому что это рекомендуемый control
  EXPECTED: FAIL_ISOLATE_MEANS_SAFE_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: невидимый control-символ не может быть опасен
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: изолят содержит свой эффект, ничего не протекает
  EXPECTED: FAIL_SCOPE_CONTAINMENT_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%E2%81%A7" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: фильтр вложений/оверрайдов покрывает и изоляты
  EXPECTED: FAIL_EMBEDDING_ONLY_FILTER_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: присутствие изолята доказывает, что ввод санирован
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как смоделировать полный набор Bidi_Control, включая изоляты (2066-2069) и авто-направление FSI, без ложных срабатываний на легитимном ограниченном тексте смешанного направления?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (стековый чекер, покрывающий вложения, оверрайды И изоляты, спаривающий каждый открыватель со своим корректным терминатором + отклоняющий незакрытые/неверные терминаторы — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «изоляты рекомендованы, но не иммунны; старый embedding-only фильтр их пропускает».
ALL_OPEN_QUESTIONS_CLOSED: NO (delegated, non-blocking)

============================================================
11. PATCH_HISTORY
============================================================
PATCH_HISTORY:
  v0_1_PATCH_01: первичное создание (Ruslan Malyavsky, 2026-07-21) — черновик из шаблона GEN3_v0_3 (Vakhter); не конвейер-ран.
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
