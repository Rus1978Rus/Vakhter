PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_LEFT_TO_RIGHT_MARK_U200E_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
TRANSLATION_NOTE: Русский оригинал (авторитетный). Английское зеркало — SIGN_CORE_CARD_LEFT_TO_RIGHT_MARK_U200E_GEN3_v0_3_EN. Кодпойнты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_LEFT_TO_RIGHT_MARK_U200E_GEN3_v0_3_RU
CODEPOINT: U+200E
VISIBLE_FORM: ⟨LRM⟩
UNICODE_NAME: LEFT-TO-RIGHT MARK
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: лево-направо метка / невидимый сильный LTR-символ (зеркало RLM)
CATEGORY_ROADMAP: LLM (invisible bidi direction injection) · PHAGO: — (маскировка порядка)
GLYPH_NOTE: VISIBLE_FORM использует маркер ⟨LRM⟩; сам знак (U+200E) — невидимый Bidi_Control (Cf) и НИКОГДА не пишется буквально — буквальный LRM мог бы переупорядочить этот документ. Примеры используют ⟨LRM⟩/%E2%80%8E, но не байт. Как и RLM, LRM — сильный СИМВОЛ, а не открыватель/закрыватель формата.

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
VISIBLE_FORM: ⟨LRM⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: LRM_FORM ≠ EFFECT
SIGN_CATEGORY:
  - невидимый символ нулевой ширины, действующий как СИЛЬНЫЙ лево-направо символ
  - легитимное bidi-использование: фиксация нейтральных символов к LTR или восстановление LTR-контекста после RTL-прогона
  - он задаёт направление БЕЗ какого-либо вложения/оверрайда/изолята — без формат-открывателя или терминатора
  - (при злоупотреблении) невидимая инъекция направления, которую фильтр только-формата (202x/206x) пропускает; «выглядящий по умолчанию» LTR легко проглядеть

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — непечатаемость не делает знак инертным
  2. NOT_A_FORMAT_CONTROL — это сильный символ, не вложение/оверрайд/изолят; без терминатора, без вложенности
  3. NOT_CAUGHT_BY_FORMAT_ONLY_FILTER — фильтр, срезающий только U+202A–202E / U+2066–2069, не трогает U+200E
  4. NOT_DIRECTIONLESS — он несёт сильную LTR-направленность, способную зафиксировать или перевернуть разрешённый порядок соседних нейтралов/чисел
  5. NOT_RLM — U+200E это LTR; U+200F (RLM) это RTL; это метки противоположного направления
  6. NOT_DEFAULT_MEANS_NOOP — «выглядит как нормальный LTR по умолчанию» не значит, что он ничего не делает; он может переопределить унаследованный RTL-контекст
  7. NOT_ENCODED_SAFE — «%E2%80%8E» может быть декодирован обратно в LRM позже
  8. NOT_AUTHORITY — он не подтверждает официальность
  9. NOT_EXECUTION_TRIGGER — сам по себе он ничего не исполняет; он обманывает визуальный порядок
  10. NOT_SANITIZED_PROOF — присутствие символа не означает, что ввод санирован
  11. NOT_SINGLE_ORDER_PROOF — строка, которая «читается в одну сторону», может переупорядочиться вокруг скрытого LRM

BASE_FORMULAS:
  LRM_FORM ≠ EFFECT
  LRM_FORM ≠ FORMAT_CONTROL_PROOF
  LRM_FORM ≠ CAUGHT_BY_FORMAT_ONLY_FILTER_PROOF
  LRM_FORM ≠ DIRECTIONLESS_PROOF
  LRM_FORM ≠ RLM_EQUIVALENCE_PROOF
  LRM_FORM ≠ DEFAULT_MEANS_NOOP_PROOF
  LRM_FORM ≠ ENCODED_SAFETY_PROOF
  LRM_FORM ≠ AUTHORITY
  LRM_FORM ≠ EXECUTION_TRIGGER
  LRM_FORM ≠ INVISIBLE_HARMLESS_PROOF
  LRM_FORM ≠ SANITIZED_PROOF
  LRM_FORM ≠ SINGLE_ORDER_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: LRM (ZONE_1) имеет параллельные функции (легитимная фиксация направления нейтралов vs. невидимая инъекция направления), сосуществующие без культурной прецессии. Полисемия стабильной Bidi_Control-метки.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: невидимая метка сильного направления без жестового предшественника; злоупотребление через инъекцию направления надстроено цифровой эпохой параллельно с легитимной фиксацией нейтралов.

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
    INPUT: "LRM is U+200E in Unicode"
    CONTEXT: именование символа в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: LRM_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "LRM fixes neutral characters to left-to-right"
    CONTEXT: описание легитимной bidi-функции в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: LRM_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <LRM> here"
    CONTEXT: документационный маркер, не байт
    EXPECTED: INFO
    RISK: NONE
    GUARD: LRM_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "it is a strong character, not a format control"
    CONTEXT: отличие от LRO/LRE/LRI в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: LRM_FORM ≠ FORMAT_CONTROL_PROOF
  SAFE_CASE_005:
    INPUT: "LRM is left-to-right, RLM is right-to-left"
    CONTEXT: отличие от U+200F в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: LRM_FORM ≠ RLM_EQUIVALENCE_PROOF
  SAFE_CASE_006:
    INPUT: "a bidi-aware normalizer can handle the marks too"
    CONTEXT: описание аккуратной санитизации в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: LRM_FORM ≠ CAUGHT_BY_FORMAT_ONLY_FILTER_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: FORMAT_ONLY_FILTER_GAP
    INPUT: "input passing a strip that removes only 202A-202E and 2066-2069"
    CONTEXT: LRM проскакивает фильтр, знающий только формат-контролы
    RISK: HIGH
    ATTACK: сильная метка переупорядочивает нейтралы без формат-открывателя, который фильтр мог бы поймать
    GUARD: LRM_FORM ≠ CAUGHT_BY_FORMAT_ONLY_FILTER_PROOF
  RISK_CASE_002:
    NAME: RTL_CONTEXT_NEUTRALIZE
    INPUT: "an LRM forcing LTR inside an otherwise RTL run"
    CONTEXT: LRM переопределяет унаследованный RTL-контекст, так что нейтралы разрешаются LTR
    RISK: HIGH
    ATTACK: невидимая метка меняет, как сумма/путь/метка читаются внутри RTL-текста
    GUARD: LRM_FORM ≠ DEFAULT_MEANS_NOOP_PROOF
  RISK_CASE_003:
    NAME: MARK_VS_OVERRIDE_CONFUSION
    INPUT: "a reviewer expecting an LRO but the payload uses an LRM"
    CONTEXT: анализ, настроенный на оверрайды, упускает разворот на основе метки
    RISK: MEDIUM
    ATTACK: поскольку LRM это метка (без терминатора), проверка, сфокусированная на оверрайдах, её не моделирует
    GUARD: LRM_FORM ≠ FORMAT_CONTROL_PROOF
  RISK_CASE_004:
    NAME: ENCODED_LRM_BYPASS
    INPUT: "value%E2%80%8Etail (with a later decode)"
    CONTEXT: percent-кодированный LRM, декодируемый обратно перед отображением
    RISK: HIGH
    ATTACK: «%E2%80%8E» декодируется в LRM ПОСЛЕ проверки → разворот возвращается
    GUARD: LRM_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: MARK_PAIR_GAP
    INPUT: "input using U+200F (RLM) or U+061C (ALM) where only U+200E is filtered"
    CONTEXT: другие невидимые метки направления проскакивают мимо фильтра только-LRM
    RISK: MEDIUM
    ATTACK: фильтрация только U+200E упускает RLM/ALM, которые инъецируют противоположное/производное направление
    GUARD: LRM_FORM ≠ RLM_EQUIVALENCE_PROOF
  RISK_CASE_006:
    NAME: BIDI_HOMOGLYPH_STACK
    INPUT: "раyраl<LRM> ... (mark + confusable letters combined)"
    CONTEXT: LRM в связке с похожими буквами для усиления подделки
    RISK: MEDIUM
    ATTACK: невидимая метка плюс буквы-двойники проводят враждебную строку через поверхностный визуальный обзор
    GUARD: LRM_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨RLM⟩
    CODEPOINT: U+200F
    NAME: RIGHT-TO-LEFT MARK
    RISK: HIGH
    RULE: RIGHT_TO_LEFT_MARK ≠ LEFT_TO_RIGHT_MARK (невидимая сильная метка противоположного направления; наивный фильтр их смешивает)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨ALM⟩
    CODEPOINT: U+061C
    NAME: ARABIC LETTER MARK
    RISK: HIGH
    RULE: ARABIC_LETTER_MARK ≠ LEFT_TO_RIGHT_MARK (сильная RTL-метка в арабском блоке; противоположное направление и другой «район», который фильтр может упустить)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨LRO⟩
    CODEPOINT: U+202D
    NAME: LEFT-TO-RIGHT OVERRIDE
    RISK: MEDIUM
    RULE: LEFT_TO_RIGHT_OVERRIDE ≠ LEFT_TO_RIGHT_MARK (оверрайд форсирует направление и имеет терминатор; метка — сильный символ без обоих)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨LRI⟩
    CODEPOINT: U+2066
    NAME: LEFT-TO-RIGHT ISOLATE
    RISK: MEDIUM
    RULE: LEFT_TO_RIGHT_ISOLATE ≠ LEFT_TO_RIGHT_MARK (изолят ограничивает область и требует PDI; метка ничего не ограничивает и не требует терминатора)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨ZWSP⟩
    CODEPOINT: U+200B
    NAME: ZERO WIDTH SPACE
    RISK: LOW
    RULE: ZERO_WIDTH_SPACE ≠ LEFT_TO_RIGHT_MARK (оба невидимы, но ZWSP — точка переноса, не несущая направления)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "our bidi filter strips the format controls, so we are covered"
    RESPONSE: LRM_FORM ≠ CAUGHT_BY_FORMAT_ONLY_FILTER_PROOF
    RULE: LRM — сильная метка, не control 202x/206x; срезание только формата её пропускает
  CG2:
    TRIGGER: "an invisible char cannot be dangerous"
    RESPONSE: LRM_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: невидимость ортогональна эффекту; LRM переупорядочивает нейтралы невидимо
  CG3:
    TRIGGER: "it just sets the normal LTR default, so it is a no-op"
    RESPONSE: LRM_FORM ≠ DEFAULT_MEANS_NOOP_PROOF
    RULE: он может переопределить унаследованный RTL-контекст; «выглядит по умолчанию» не есть «без эффекта»
  CG4:
    TRIGGER: "'%E2%80%8E' is safe forever"
    RESPONSE: LRM_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в LRM перед отображением
  CG5:
    TRIGGER: "an invisible mark carries no direction"
    RESPONSE: LRM_FORM ≠ DIRECTIONLESS_PROOF
    RULE: LRM — сильный LTR-символ; он фиксирует/переворачивает порядок соседних нейтралов
  CG6:
    TRIGGER: "we filter U+200E, so the marks are handled"
    RESPONSE: LRM_FORM ≠ RLM_EQUIVALENCE_PROOF
    RULE: RLM (U+200F) и ALM (U+061C) — отдельные метки направления

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "RTL run + interior LRM"
      NAME: RTL_CONTEXT_FLIP
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: LRM, форсирующий LTR на нейтралах внутри RTL-текста
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "LRM used where a format-only filter runs"
      NAME: FORMAT_FILTER_GAP
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: метка, выживающая из-за срезания только контролов 202x/206x
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "mixed LRM + RLM + ALM"
      NAME: MARK_FAMILY_MIX
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: несколько меток направления вместе для обхода фильтра только-LRM
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: не применимо — эффект LRM на порядок окружающей последовательности.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: LRM переупорядочивает нейтральные прогоны (маскировка порядка), но не имитирует существование верифицированной сущности. Его риски — десинхрон визуального порядка, а не мимикрия сущности. (Подделка имени файла естественнее с оверрайдом; см. RLO/LRO.)
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена LRM на RLM (U+200F) / ALM (U+061C) для смены метки направления / обхода фильтра только-LRM
  A2: percent-кодирование "%E2%80%8E" для проскока мимо сканера сырых байтов
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: пробел фильтра только-формата (LRM переживает срезание 202A-202E / 2066-2069)
  B2: нейтрализация RTL-контекста (LRM форсирует LTR внутри RTL-прогона)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "RTL run + interior LRM" (SC1) — переворот RTL-контекста
  C2: "mixed LRM + RLM + ALM" (SC3) — смесь семейства меток
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: LRM подан как безобидное «направление по умолчанию», пока он нейтрализует RTL-контекст
  D2: "%E2%80%8E" как «безопасный» кодированный текст с последующим декодом
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: невидимый разворот нейтралов, обманывающий обозревателя
  E2: N/A — вектор: разворот на основе метки, обходящий фильтр только-формат-контролов
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: срезание формат-контролов покрывает и LRM
  EXPECTED: FAIL_CAUGHT_BY_FORMAT_ONLY_FILTER_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: невидимый символ не может быть опасен
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: LRM лишь задаёт значение по умолчанию, значит это no-op
  EXPECTED: FAIL_DEFAULT_MEANS_NOOP_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%E2%80%8E" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: невидимая метка не несёт направления
  EXPECTED: FAIL_DIRECTIONLESS_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: фильтрация U+200E обрабатывает все метки направления
  EXPECTED: FAIL_RLM_EQUIVALENCE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как смоделировать невидимые метки направления (U+200E LRM, U+200F RLM, U+061C ALM) наряду с bidi формат-контролами, чтобы bidi-фильтр ловил и развороты на основе меток, без ложных срабатываний на легитимной фиксации направления нейтралов?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (bidi-нормализатор, покрывающий метки И формат-контролы, разрешающий порядок детерминированно и помечающий подозрительные развороты на основе меток — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «LRM — сильная метка направления, не формат-control и не no-op; фильтр, срезающий только 202x/206x, её пропускает».
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
