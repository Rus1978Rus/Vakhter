PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_FIRST_STRONG_ISOLATE_U2068_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
TRANSLATION_NOTE: Русский оригинал (авторитетный). Английское зеркало — SIGN_CORE_CARD_FIRST_STRONG_ISOLATE_U2068_GEN3_v0_3_EN. Кодпойнты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_FIRST_STRONG_ISOLATE_U2068_GEN3_v0_3_RU
CODEPOINT: U+2068
VISIBLE_FORM: ⟨FSI⟩
UNICODE_NAME: FIRST STRONG ISOLATE
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: изолят по первому сильному / bidi-изолят с авто-направлением (направление по первому сильному символу)
CATEGORY_ROADMAP: LLM (bidi isolate reorder, Trojan Source) · PHAGO: — (маскировка структуры)
GLYPH_NOTE: VISIBLE_FORM использует маркер ⟨FSI⟩; сам знак (U+2068) — невидимый Bidi_Control (Cf) и НИКОГДА не пишется буквально — буквальный FSI переупорядочил бы этот документ. Примеры используют ⟨FSI⟩/⟨PDI⟩/%E2%81%A8, но не байт.

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
VISIBLE_FORM: ⟨FSI⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: FSI_FORM ≠ EFFECT
SIGN_CATEGORY:
  - двунаправленный изолят, направление которого выбирается по ПЕРВОМУ СИЛЬНОМУ символу внутри него
  - Unicode Bidi_Control, часть современного рекомендуемого набора изолятов (2066-2069)
  - легитимная авто-направленная раскладка (например, имя неизвестной письменности, встроенное в текст)
  - (при злоупотреблении) направление управляемо атакующим: кто подаёт первый сильный символ, тот рулит прогоном

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — непечатаемость не делает знак инертным
  2. NOT_AUTO_DIRECTION_MEANS_SAFE — авто-выбор направления это функция, а не свойство безопасности; выбор управляется данными и, значит, атакующим
  3. NOT_DIRECTION_FIXED — в отличие от LRI/RLI, направление FSI НЕ фиксировано; оно зависит от содержимого и может переворачиваться
  4. NOT_DISPLAY_ONLY — он переупорядочивает ВИЗУАЛЬНЫЙ прогон, при неизменных логических байтах (десинхрон)
  5. NOT_SCOPE_CONTAINS_ALL — незакрытый FSI всё равно «протекает» до конца абзаца
  6. NOT_ENCODED_SAFE — «%E2%81%A8» может быть декодирован обратно в изолят позже
  7. NOT_AUTHORITY — он не подтверждает официальность
  8. NOT_EXECUTION_TRIGGER — сам по себе он ничего не исполняет; он обманывает читателя
  9. NOT_EMBEDDING_ONLY_FILTER_SAFE — фильтр, обрабатывающий только вложения/оверрайды (202A-202E), пропускает изоляты (2066-2069)
  10. NOT_SANITIZED_PROOF — присутствие изолята не означает, что ввод санирован
  11. NOT_BALANCED_PROOF — изоляту нужен парный PDI; его присутствие не есть баланс

BASE_FORMULAS:
  FSI_FORM ≠ EFFECT
  FSI_FORM ≠ AUTO_DIRECTION_MEANS_SAFE_PROOF
  FSI_FORM ≠ DIRECTION_FIXED_PROOF
  FSI_FORM ≠ DISPLAY_ONLY_PROOF
  FSI_FORM ≠ SCOPE_CONTAINMENT_PROOF
  FSI_FORM ≠ ENCODED_SAFETY_PROOF
  FSI_FORM ≠ AUTHORITY
  FSI_FORM ≠ EXECUTION_TRIGGER
  FSI_FORM ≠ EMBEDDING_ONLY_FILTER_PROOF
  FSI_FORM ≠ INVISIBLE_HARMLESS_PROOF
  FSI_FORM ≠ SANITIZED_PROOF
  FSI_FORM ≠ BALANCED_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: FSI (ZONE_1) имеет параллельные функции (легитимное авто-направление контента неизвестной письменности vs. управляемый атакующим переворот направления), сосуществующие без культурной прецессии. Полисемия стабильного Bidi_Control.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: управляемый содержимым форматирующий изолят-control без жестового предшественника; обман через управление направлением надстроен цифровой эпохой параллельно с легитимной авто-направленной раскладкой.

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
    INPUT: "FSI is U+2068 in Unicode"
    CONTEXT: именование control в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: FSI_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "FSI picks direction from the first strong character"
    CONTEXT: описание правила авто-направления в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: FSI_FORM ≠ AUTO_DIRECTION_MEANS_SAFE_PROOF
  SAFE_CASE_003:
    INPUT: "the marker is written as <FSI> here"
    CONTEXT: документационный маркер, не байт
    EXPECTED: INFO
    RISK: NONE
    GUARD: FSI_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "auto-direction helps display names of unknown script"
    CONTEXT: описание легитимного использования раскладки в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: FSI_FORM ≠ AUTO_DIRECTION_MEANS_SAFE_PROOF
  SAFE_CASE_005:
    INPUT: "a properly terminated isolate (FSI...PDI)"
    CONTEXT: описание сбалансированного легитимного использования
    EXPECTED: INFO
    RISK: NONE
    GUARD: FSI_FORM ≠ BALANCED_PROOF
  SAFE_CASE_006:
    INPUT: "the Bidirectional Algorithm scopes the isolate"
    CONTEXT: проза про UBA
    EXPECTED: INFO
    RISK: NONE
    GUARD: FSI_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: ATTACKER_STEERED_DIRECTION
    INPUT: "FSI + attacker-supplied first strong char sets the run RTL"
    CONTEXT: первый сильный символ — это данные атакующего, значит направление выбрано атакующим
    RISK: HIGH
    ATTACK: атакующий ставит сильный RTL-символ первым, переворачивая весь изолят в RTL и переупорядочивая его
    GUARD: FSI_FORM ≠ AUTO_DIRECTION_MEANS_SAFE_PROOF
  RISK_CASE_002:
    NAME: LEGACY_FILTER_GAP
    INPUT: "input passing a strip that only handles 202A-202E"
    CONTEXT: изолят проскакивает фильтр, знающий только вложения/оверрайды
    RISK: HIGH
    ATTACK: более новый изолят (2066-2069) не смоделирован, поэтому разворот переживает очистку
    GUARD: FSI_FORM ≠ EMBEDDING_ONLY_FILTER_PROOF
  RISK_CASE_003:
    NAME: UNTERMINATED_ISOLATE_BLEED
    INPUT: "label<FSI>rest of the paragraph with no PDI"
    CONTEXT: FSI без PDI, протекающий до конца абзаца
    RISK: HIGH
    ATTACK: незакрытый изолят переупорядочивает всё до конца абзаца, за пределами задуманной области
    GUARD: FSI_FORM ≠ SCOPE_CONTAINMENT_PROOF
  RISK_CASE_004:
    NAME: DIRECTION_FLIP_ON_EDIT
    INPUT: "FSI run whose first strong char changes after an edit"
    CONTEXT: правка контента у начала молча переворачивает направление изолята
    RISK: MEDIUM
    ATTACK: поскольку направление управляется содержимым, поздняя правка меняет отображение, не меняя сам FSI
    GUARD: FSI_FORM ≠ DIRECTION_FIXED_PROOF
  RISK_CASE_005:
    NAME: ENCODED_ISOLATE_BYPASS
    INPUT: "value%E2%81%A8tail (with a later decode)"
    CONTEXT: percent-кодированный FSI, декодируемый обратно перед отображением
    RISK: HIGH
    ATTACK: «%E2%81%A8» декодируется в изолят ПОСЛЕ проверки → обман разворота
    GUARD: FSI_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: BIDI_HOMOGLYPH_STACK
    INPUT: "раyраl<FSI> ... (bidi + confusable letters combined)"
    CONTEXT: FSI в связке с похожими буквами для усиления подделки
    RISK: MEDIUM
    ATTACK: изолят плюс буквы-двойники проводят враждебную строку через поверхностный визуальный обзор
    GUARD: FSI_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨LRI⟩
    CODEPOINT: U+2066
    NAME: LEFT-TO-RIGHT ISOLATE
    RISK: HIGH
    RULE: LEFT_TO_RIGHT_ISOLATE ≠ FIRST_STRONG_ISOLATE (у LRI направление фиксировано LTR; у FSI — выбирается по содержимому)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨RLI⟩
    CODEPOINT: U+2067
    NAME: RIGHT-TO-LEFT ISOLATE
    RISK: HIGH
    RULE: RIGHT_TO_LEFT_ISOLATE ≠ FIRST_STRONG_ISOLATE (у RLI направление фиксировано RTL; у FSI — выбирается по содержимому)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨PDI⟩
    CODEPOINT: U+2069
    NAME: POP DIRECTIONAL ISOLATE
    RISK: LOW
    RULE: POP_DIRECTIONAL_ISOLATE ≠ FIRST_STRONG_ISOLATE (терминатор, не открыватель)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨RLE⟩
    CODEPOINT: U+202B
    NAME: RIGHT-TO-LEFT EMBEDDING
    RISK: MEDIUM
    RULE: RIGHT_TO_LEFT_EMBEDDING ≠ FIRST_STRONG_ISOLATE (вложение влияет на соседей и фиксированного направления; FSI ограничивает область и авто-выбирает)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨RLO⟩
    CODEPOINT: U+202E
    NAME: RIGHT-TO-LEFT OVERRIDE
    RISK: LOW
    RULE: RIGHT_TO_LEFT_OVERRIDE ≠ FIRST_STRONG_ISOLATE (оверрайд форсирует направление и влияет на соседей; FSI ограничивает область и выводит его)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "auto-direction is a convenience, so FSI is safe"
    RESPONSE: FSI_FORM ≠ AUTO_DIRECTION_MEANS_SAFE_PROOF
    RULE: направление выбирается из данных, поэтому атакующий, контролирующий первый сильный символ, контролирует направление
  CG2:
    TRIGGER: "an invisible control char cannot be dangerous"
    RESPONSE: FSI_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: невидимость ортогональна эффекту; FSI создаёт визуально/логический десинхрон
  CG3:
    TRIGGER: "FSI always shows text the same way"
    RESPONSE: FSI_FORM ≠ DIRECTION_FIXED_PROOF
    RULE: направление FSI зависит от содержимого и может переворачиваться при его изменении
  CG4:
    TRIGGER: "'%E2%81%A8' is safe forever"
    RESPONSE: FSI_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в изолят перед отображением
  CG5:
    TRIGGER: "our bidi filter handles embeddings and overrides, so we are covered"
    RESPONSE: FSI_FORM ≠ EMBEDDING_ONLY_FILTER_PROOF
    RULE: изоляты (2066-2069) — отдельный, более новый диапазон, который старый фильтр пропускает
  CG6:
    TRIGGER: "the presence of an isolate means the input is sanitized"
    RESPONSE: FSI_FORM ≠ SANITIZED_PROOF
    RULE: присутствие знака ничего не говорит о санации

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "FSI <strong RTL> ... PDI"
      NAME: STEERED_ISOLATE_SPAN
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: FSI, чей первый сильный символ — подложенный атакующим RTL, переворачивающий спан
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "FSI (no PDI)"
      NAME: UNTERMINATED_BLEED
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: FSI без терминатора, протекающий до конца абзаца
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "FSI ... PDF"
      NAME: WRONG_TERMINATOR
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: FSI, закрытый PDF вместо PDI, с неверным отслеживанием вложенности
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: не применимо — последовательности с FSI центральны для обмана визуального порядка, управляемого содержимым.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: FSI переупорядочивает ограниченный прогон, направление которого выбрано по содержимому (маскировка структуры), но не имитирует существование верифицированной сущности. Его риски — визуально/логический десинхрон, а не мимикрия сущности. (Подделка имени файла естественнее с оверрайдом; см. RLO/LRO.)
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена FSI на LRI (U+2066) / RLI (U+2067) для фиксации направления / обхода FSI-только-фильтра
  A2: percent-кодирование "%E2%81%A8" для проскока мимо сканера сырых байтов
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: подложенный атакующим первый сильный символ рулит направлением FSI в RTL
  B2: пробел старого фильтра (изолят переживает очистку только 202A-202E)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "FSI (no PDI)" (SC2) — незакрытое протекание до конца абзаца
  C2: "FSI ... PDF" (SC3) — неверный терминатор
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: FSI подан как безобидное «удобство авто-направления» внутри поля кода
  D2: "%E2%81%A8" как «безопасный» кодированный текст с последующим декодом
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: управляемый содержимым разворот, обманывающий обозревателя
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
  CLAIM: авто-направление это удобство, поэтому FSI безопасен
  EXPECTED: FAIL_AUTO_DIRECTION_MEANS_SAFE_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: невидимый control-символ не может быть опасен
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: FSI всегда показывает текст одинаково
  EXPECTED: FAIL_DIRECTION_FIXED_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%E2%81%A8" безопасен навсегда
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
  QUESTION: как смоделировать направление FSI, выводимое из содержимого (направление зависит от первого сильного символа, который может быть данными атакующего), без ложных срабатываний на легитимном авто-направлении контента неизвестной письменности?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (стековый чекер, покрывающий вложения, оверрайды И изоляты, разрешающий направление FSI из содержимого, спаривающий каждый открыватель со своим корректным терминатором + отклоняющий незакрытые/неверные терминаторы — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «направление FSI управляется данными, значит атакующим; авто-направление не есть свойство безопасности».
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
