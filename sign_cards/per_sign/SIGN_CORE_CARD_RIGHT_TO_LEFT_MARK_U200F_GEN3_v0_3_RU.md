PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_RIGHT_TO_LEFT_MARK_U200F_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
TRANSLATION_NOTE: Русский оригинал (авторитетный). Английское зеркало — SIGN_CORE_CARD_RIGHT_TO_LEFT_MARK_U200F_GEN3_v0_3_EN. Кодпойнты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_RIGHT_TO_LEFT_MARK_U200F_GEN3_v0_3_RU
CODEPOINT: U+200F
VISIBLE_FORM: ⟨RLM⟩
UNICODE_NAME: RIGHT-TO-LEFT MARK
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: право-налево метка / невидимый сильный RTL-символ (формат-control не нужен)
CATEGORY_ROADMAP: LLM (invisible bidi direction injection) · PHAGO: — (маскировка порядка)
GLYPH_NOTE: VISIBLE_FORM использует маркер ⟨RLM⟩; сам знак (U+200F) — невидимый Bidi_Control (Cf) и НИКОГДА не пишется буквально — буквальный RLM мог бы переупорядочить этот документ. Примеры используют ⟨RLM⟩/%E2%80%8F, но не байт. В отличие от RLO/RLE/RLI, RLM — сильный СИМВОЛ, а не открыватель/закрыватель формата.

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
VISIBLE_FORM: ⟨RLM⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: RLM_FORM ≠ EFFECT
SIGN_CATEGORY:
  - невидимый символ нулевой ширины, действующий как СИЛЬНЫЙ право-налево символ
  - легитимное bidi-использование: фиксация направления нейтральных символов (пунктуация, цифры) в смешанном тексте
  - он задаёт направление БЕЗ какого-либо вложения/оверрайда/изолята — без формат-открывателя или терминатора
  - (при злоупотреблении) невидимая инъекция направления, которую фильтр, срезающий только формат-контролы 202x/206x, полностью пропускает

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — непечатаемость не делает знак инертным
  2. NOT_A_FORMAT_CONTROL — это сильный символ, не вложение/оверрайд/изолят; у него нет терминатора и вложенности
  3. NOT_CAUGHT_BY_FORMAT_ONLY_FILTER — фильтр, срезающий только U+202A–202E / U+2066–2069, не трогает U+200F
  4. NOT_DIRECTIONLESS — он несёт сильную RTL-направленность, способную перевернуть разрешённый порядок соседних нейтралов/чисел
  5. NOT_LRM — U+200F это RTL; U+200E (LRM) это LTR; это метки противоположного направления
  6. NOT_ENCODED_SAFE — «%E2%80%8F» может быть декодирован обратно в RLM позже
  7. NOT_AUTHORITY — он не подтверждает официальность
  8. NOT_EXECUTION_TRIGGER — сам по себе он ничего не исполняет; он обманывает визуальный порядок
  9. NOT_TRUST_SIGNAL — он не повышает доверие
  10. NOT_SANITIZED_PROOF — присутствие символа не означает, что ввод санирован
  11. NOT_SINGLE_ORDER_PROOF — строка, которая «читается слева направо», может переупорядочиться вокруг скрытого RLM

BASE_FORMULAS:
  RLM_FORM ≠ EFFECT
  RLM_FORM ≠ FORMAT_CONTROL_PROOF
  RLM_FORM ≠ CAUGHT_BY_FORMAT_ONLY_FILTER_PROOF
  RLM_FORM ≠ DIRECTIONLESS_PROOF
  RLM_FORM ≠ LRM_EQUIVALENCE_PROOF
  RLM_FORM ≠ ENCODED_SAFETY_PROOF
  RLM_FORM ≠ AUTHORITY
  RLM_FORM ≠ EXECUTION_TRIGGER
  RLM_FORM ≠ INVISIBLE_HARMLESS_PROOF
  RLM_FORM ≠ SANITIZED_PROOF
  RLM_FORM ≠ SINGLE_ORDER_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: RLM (ZONE_1) имеет параллельные функции (легитимная фиксация направления нейтралов vs. невидимая инъекция направления), сосуществующие без культурной прецессии. Полисемия стабильной Bidi_Control-метки.
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
    INPUT: "RLM is U+200F in Unicode"
    CONTEXT: именование символа в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLM_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "RLM fixes the direction of neutral characters"
    CONTEXT: описание легитимной bidi-функции в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLM_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <RLM> here"
    CONTEXT: документационный маркер, не байт
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLM_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "it is a strong character, not a format control"
    CONTEXT: отличие от RLO/RLE/RLI в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLM_FORM ≠ FORMAT_CONTROL_PROOF
  SAFE_CASE_005:
    INPUT: "RLM is right-to-left, LRM is left-to-right"
    CONTEXT: отличие от U+200E в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLM_FORM ≠ LRM_EQUIVALENCE_PROOF
  SAFE_CASE_006:
    INPUT: "a bidi-aware normalizer can handle the marks too"
    CONTEXT: описание аккуратной санитизации в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: RLM_FORM ≠ CAUGHT_BY_FORMAT_ONLY_FILTER_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: FORMAT_ONLY_FILTER_GAP
    INPUT: "input passing a strip that removes only 202A-202E and 2066-2069"
    CONTEXT: RLM проскакивает фильтр, знающий только формат-контролы
    RISK: HIGH
    ATTACK: сильная метка переупорядочивает нейтралы без формат-открывателя, который фильтр мог бы поймать
    GUARD: RLM_FORM ≠ CAUGHT_BY_FORMAT_ONLY_FILTER_PROOF
  RISK_CASE_002:
    NAME: NEUTRAL_REORDER
    INPUT: "digits/punctuation around a hidden RLM flipping visible order"
    CONTEXT: RLM задаёт направление соседних нейтралов, так что порядок отображения меняется
    RISK: HIGH
    ATTACK: сумма, дата или путь читаются в другом порядке, чем хранятся
    GUARD: RLM_FORM ≠ SINGLE_ORDER_PROOF
  RISK_CASE_003:
    NAME: MARK_VS_OVERRIDE_CONFUSION
    INPUT: "a reviewer expecting an RLO but the payload uses an RLM"
    CONTEXT: анализ, настроенный на оверрайды, упускает разворот на основе метки
    RISK: MEDIUM
    ATTACK: поскольку RLM это метка (без терминатора), проверка, сфокусированная на оверрайдах, её не моделирует
    GUARD: RLM_FORM ≠ FORMAT_CONTROL_PROOF
  RISK_CASE_004:
    NAME: ENCODED_RLM_BYPASS
    INPUT: "value%E2%80%8Ftail (with a later decode)"
    CONTEXT: percent-кодированный RLM, декодируемый обратно перед отображением
    RISK: HIGH
    ATTACK: «%E2%80%8F» декодируется в RLM ПОСЛЕ проверки → разворот возвращается
    GUARD: RLM_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: MARK_PAIR_GAP
    INPUT: "input using U+200E (LRM) or U+061C (ALM) where only U+200F is filtered"
    CONTEXT: другие невидимые метки направления проскакивают мимо фильтра только-RLM
    RISK: MEDIUM
    ATTACK: фильтрация только U+200F упускает LRM/ALM, которые инъецируют противоположное/производное направление
    GUARD: RLM_FORM ≠ LRM_EQUIVALENCE_PROOF
  RISK_CASE_006:
    NAME: BIDI_HOMOGLYPH_STACK
    INPUT: "раyраl<RLM> ... (mark + confusable letters combined)"
    CONTEXT: RLM в связке с похожими буквами для усиления подделки
    RISK: MEDIUM
    ATTACK: невидимая метка плюс буквы-двойники проводят враждебную строку через поверхностный визуальный обзор
    GUARD: RLM_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨LRM⟩
    CODEPOINT: U+200E
    NAME: LEFT-TO-RIGHT MARK
    RISK: HIGH
    RULE: LEFT_TO_RIGHT_MARK ≠ RIGHT_TO_LEFT_MARK (невидимая сильная метка противоположного направления; наивный фильтр их смешивает)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨ALM⟩
    CODEPOINT: U+061C
    NAME: ARABIC LETTER MARK
    RISK: HIGH
    RULE: ARABIC_LETTER_MARK ≠ RIGHT_TO_LEFT_MARK (сильная RTL-метка арабского контекста; ещё одна невидимая метка направления, которую фильтр может упустить)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨RLO⟩
    CODEPOINT: U+202E
    NAME: RIGHT-TO-LEFT OVERRIDE
    RISK: MEDIUM
    RULE: RIGHT_TO_LEFT_OVERRIDE ≠ RIGHT_TO_LEFT_MARK (оверрайд форсирует направление и имеет терминатор; метка — сильный символ без обоих)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨RLI⟩
    CODEPOINT: U+2067
    NAME: RIGHT-TO-LEFT ISOLATE
    RISK: MEDIUM
    RULE: RIGHT_TO_LEFT_ISOLATE ≠ RIGHT_TO_LEFT_MARK (изолят ограничивает область и требует PDI; метка ничего не ограничивает и не требует терминатора)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨ZWSP⟩
    CODEPOINT: U+200B
    NAME: ZERO WIDTH SPACE
    RISK: LOW
    RULE: ZERO_WIDTH_SPACE ≠ RIGHT_TO_LEFT_MARK (оба невидимы, но ZWSP — точка переноса, не несущая направления)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "our bidi filter strips the format controls, so we are covered"
    RESPONSE: RLM_FORM ≠ CAUGHT_BY_FORMAT_ONLY_FILTER_PROOF
    RULE: RLM — сильная метка, не control 202x/206x; срезание только формата её пропускает
  CG2:
    TRIGGER: "an invisible char cannot be dangerous"
    RESPONSE: RLM_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: невидимость ортогональна эффекту; RLM переупорядочивает нейтралы невидимо
  CG3:
    TRIGGER: "it is an override, so look for a terminator"
    RESPONSE: RLM_FORM ≠ FORMAT_CONTROL_PROOF
    RULE: это сильный символ без терминатора и без вложенности
  CG4:
    TRIGGER: "'%E2%80%8F' is safe forever"
    RESPONSE: RLM_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в RLM перед отображением
  CG5:
    TRIGGER: "an invisible mark carries no direction"
    RESPONSE: RLM_FORM ≠ DIRECTIONLESS_PROOF
    RULE: RLM — сильный RTL-символ; он фиксирует/переворачивает порядок соседних нейтралов
  CG6:
    TRIGGER: "we filter U+200F, so the marks are handled"
    RESPONSE: RLM_FORM ≠ LRM_EQUIVALENCE_PROOF
    RULE: LRM (U+200E) и ALM (U+061C) — отдельные метки направления

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "neutrals + interior RLM"
      NAME: NEUTRAL_ORDER_FLIP
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: RLM, переворачивающий видимый порядок цифр/пунктуации вокруг себя
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "RLM used where a format-only filter runs"
      NAME: FORMAT_FILTER_GAP
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: метка, выживающая из-за срезания только контролов 202x/206x
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "mixed RLM + LRM + ALM"
      NAME: MARK_FAMILY_MIX
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: несколько меток направления вместе для обхода фильтра только-RLM
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: не применимо — эффект RLM на порядок окружающей последовательности.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: RLM переупорядочивает нейтральные прогоны (маскировка порядка), но не имитирует существование верифицированной сущности. Его риски — десинхрон визуального порядка, а не мимикрия сущности. (Подделка имени файла естественнее с оверрайдом; см. RLO/LRO.)
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена RLM на LRM (U+200E) / ALM (U+061C) для смены метки направления / обхода фильтра только-RLM
  A2: percent-кодирование "%E2%80%8F" для проскока мимо сканера сырых байтов
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: пробел фильтра только-формата (RLM переживает срезание 202A-202E / 2066-2069)
  B2: разворот нейтралов (цифры/пунктуация переворачиваются вокруг скрытого RLM)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "neutrals + interior RLM" (SC1) — переворот порядка нейтралов
  C2: "mixed RLM + LRM + ALM" (SC3) — смесь семейства меток
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: RLM подан как безобидная «фиксация направления», пока он переупорядочивает нагрузку
  D2: "%E2%80%8F" как «безопасный» кодированный текст с последующим декодом
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
  CLAIM: срезание формат-контролов покрывает и RLM
  EXPECTED: FAIL_CAUGHT_BY_FORMAT_ONLY_FILTER_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: невидимый символ не может быть опасен
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: RLM это формат-control с терминатором
  EXPECTED: FAIL_FORMAT_CONTROL_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%E2%80%8F" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: невидимая метка не несёт направления
  EXPECTED: FAIL_DIRECTIONLESS_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: фильтрация U+200F обрабатывает все метки направления
  EXPECTED: FAIL_LRM_EQUIVALENCE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как смоделировать невидимые метки направления (U+200E LRM, U+200F RLM, U+061C ALM) наряду с bidi формат-контролами, чтобы bidi-фильтр ловил и развороты на основе меток, без ложных срабатываний на легитимной фиксации направления нейтралов?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (bidi-нормализатор, покрывающий метки И формат-контролы, разрешающий порядок детерминированно и помечающий подозрительные развороты на основе меток — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «RLM — сильная метка направления, не формат-control; фильтр, срезающий только 202x/206x, её пропускает».
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
