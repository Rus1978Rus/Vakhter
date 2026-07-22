PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_ARABIC_LETTER_MARK_U061C_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
TRANSLATION_NOTE: Русский оригинал (авторитетный). Английское зеркало — SIGN_CORE_CARD_ARABIC_LETTER_MARK_U061C_GEN3_v0_3_EN. Кодпойнты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_ARABIC_LETTER_MARK_U061C_GEN3_v0_3_RU
CODEPOINT: U+061C
VISIBLE_FORM: ⟨ALM⟩
UNICODE_NAME: ARABIC LETTER MARK
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: арабская буквенная метка / невидимая сильная RTL-метка вне блока U+200x
CATEGORY_ROADMAP: LLM (invisible bidi direction injection) · PHAGO: — (маскировка порядка)
GLYPH_NOTE: VISIBLE_FORM использует маркер ⟨ALM⟩; сам знак (U+061C) — невидимый Bidi_Control (Cf) в арабском блоке и НИКОГДА не пишется буквально — буквальный ALM мог бы переупорядочить этот документ. Примеры используют ⟨ALM⟩/%D8%9C, но не байт. ALM — сильная метка, как RLM, но находится в U+061C, а не в диапазоне невидимок U+200x.

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
VISIBLE_FORM: ⟨ALM⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: ALM_FORM ≠ EFFECT
SIGN_CATEGORY:
  - невидимый символ нулевой ширины, действующий как СИЛЬНЫЙ право-налево (арабского типа) символ
  - легитимное bidi-использование: заставить следующее число/нейтрал принять обработку направления арабской письменности
  - он задаёт направление БЕЗ какого-либо вложения/оверрайда/изолята — без формат-открывателя или терминатора
  - (при злоупотреблении) невидимая инъекция направления, живущая в U+061C, так что фильтр, сканирующий только невидимки U+200x/202x/206x, полностью её пропускает

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — непечатаемость не делает знак инертным
  2. NOT_A_FORMAT_CONTROL — это сильный символ, не вложение/оверрайд/изолят; без терминатора, без вложенности
  3. NOT_IN_THE_U200X_RANGE — он находится в U+061C в арабском блоке, не среди невидимок U+200B–200F, на которых может фокусироваться сканер
  4. NOT_DIRECTIONLESS — он несёт сильную RTL-направленность, способную перевернуть разрешённый порядок соседних нейтралов/чисел
  5. NOT_RLM — он ведёт себя как RLM, но это отдельный кодпойнт (U+061C ≠ U+200F); обработка одного не есть обработка другого
  6. NOT_ARABIC_TEXT_ONLY — его риск не ограничен арабским контентом; его можно вбросить в любую строку для управления направлением
  7. NOT_ENCODED_SAFE — «%D8%9C» может быть декодирован обратно в ALM позже
  8. NOT_AUTHORITY — он не подтверждает официальность
  9. NOT_EXECUTION_TRIGGER — сам по себе он ничего не исполняет; он обманывает визуальный порядок
  10. NOT_SANITIZED_PROOF — присутствие символа не означает, что ввод санирован
  11. NOT_SINGLE_ORDER_PROOF — строка, которая «читается в одну сторону», может переупорядочиться вокруг скрытого ALM

BASE_FORMULAS:
  ALM_FORM ≠ EFFECT
  ALM_FORM ≠ FORMAT_CONTROL_PROOF
  ALM_FORM ≠ IN_U200X_RANGE_PROOF
  ALM_FORM ≠ DIRECTIONLESS_PROOF
  ALM_FORM ≠ RLM_EQUIVALENCE_PROOF
  ALM_FORM ≠ ARABIC_TEXT_ONLY_PROOF
  ALM_FORM ≠ ENCODED_SAFETY_PROOF
  ALM_FORM ≠ AUTHORITY
  ALM_FORM ≠ EXECUTION_TRIGGER
  ALM_FORM ≠ INVISIBLE_HARMLESS_PROOF
  ALM_FORM ≠ SANITIZED_PROOF
  ALM_FORM ≠ SINGLE_ORDER_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: ALM (ZONE_1) имеет параллельные функции (легитимная фиксация направления арабского контекста vs. невидимая инъекция направления), сосуществующие без культурной прецессии. Полисемия стабильной Bidi_Control-метки.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: невидимая метка сильного направления (Unicode 6.3) без жестового предшественника; злоупотребление через инъекцию направления надстроено цифровой эпохой параллельно с легитимным использованием арабского контекста.

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
    INPUT: "ALM is U+061C in Unicode"
    CONTEXT: именование символа в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: ALM_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "ALM sets Arabic-script direction for a following number"
    CONTEXT: описание легитимной bidi-функции в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: ALM_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <ALM> here"
    CONTEXT: документационный маркер, не байт
    EXPECTED: INFO
    RISK: NONE
    GUARD: ALM_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "it is a strong character, not a format control"
    CONTEXT: отличие от оверрайдов/изолятов в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: ALM_FORM ≠ FORMAT_CONTROL_PROOF
  SAFE_CASE_005:
    INPUT: "it sits at U+061C, not in the U+200x block"
    CONTEXT: описание расположения кодпойнта в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: ALM_FORM ≠ IN_U200X_RANGE_PROOF
  SAFE_CASE_006:
    INPUT: "a bidi-aware normalizer can handle the marks too"
    CONTEXT: описание аккуратной санитизации в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: ALM_FORM ≠ RLM_EQUIVALENCE_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: RANGE_SCAN_GAP
    INPUT: "input passing a scanner that only checks U+200B-200F and 202x/206x"
    CONTEXT: ALM проскакивает фильтр, сфокусированный на невидимках U+200x
    RISK: HIGH
    ATTACK: метка в U+061C вне сканируемого диапазона, так что разворот выживает
    GUARD: ALM_FORM ≠ IN_U200X_RANGE_PROOF
  RISK_CASE_002:
    NAME: NEUTRAL_REORDER
    INPUT: "digits/punctuation around a hidden ALM flipping visible order"
    CONTEXT: ALM задаёт направление соседних нейтралов, так что порядок отображения меняется
    RISK: HIGH
    ATTACK: сумма, дата или путь читаются в другом порядке, чем хранятся
    GUARD: ALM_FORM ≠ SINGLE_ORDER_PROOF
  RISK_CASE_003:
    NAME: RLM_ONLY_FILTER_GAP
    INPUT: "a filter that removes RLM (U+200F) but not ALM (U+061C)"
    CONTEXT: осведомлённый о метках фильтр, всё ещё упускающий метку арабского блока
    RISK: MEDIUM
    ATTACK: ALM делает то же RTL-управление, что и RLM, но фильтр смоделировал только RLM
    GUARD: ALM_FORM ≠ RLM_EQUIVALENCE_PROOF
  RISK_CASE_004:
    NAME: ENCODED_ALM_BYPASS
    INPUT: "value%D8%9Ctail (with a later decode)"
    CONTEXT: percent-кодированный ALM, декодируемый обратно перед отображением
    RISK: HIGH
    ATTACK: «%D8%9C» декодируется в ALM ПОСЛЕ проверки → разворот возвращается
    GUARD: ALM_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: NON_ARABIC_CONTEXT_INJECTION
    INPUT: "an ALM dropped into an otherwise Latin/ASCII string"
    CONTEXT: ALM, управляющий направлением в контенте, который вовсе не арабский
    RISK: MEDIUM
    ATTACK: предполагая, что ALM важен только в арабском тексте, фильтр игнорирует его в латинском вводе, где он всё равно переупорядочивает
    GUARD: ALM_FORM ≠ ARABIC_TEXT_ONLY_PROOF
  RISK_CASE_006:
    NAME: BIDI_HOMOGLYPH_STACK
    INPUT: "раyраl<ALM> ... (mark + confusable letters combined)"
    CONTEXT: ALM в связке с похожими буквами для усиления подделки
    RISK: MEDIUM
    ATTACK: невидимая метка плюс буквы-двойники проводят враждебную строку через поверхностный визуальный обзор
    GUARD: ALM_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨RLM⟩
    CODEPOINT: U+200F
    NAME: RIGHT-TO-LEFT MARK
    RISK: HIGH
    RULE: RIGHT_TO_LEFT_MARK ≠ ARABIC_LETTER_MARK (то же RTL-управление, но RLM в U+200F, тогда как ALM в U+061C — фильтр может смоделировать лишь одного)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨LRM⟩
    CODEPOINT: U+200E
    NAME: LEFT-TO-RIGHT MARK
    RISK: HIGH
    RULE: LEFT_TO_RIGHT_MARK ≠ ARABIC_LETTER_MARK (невидимая сильная метка противоположного направления; наивный фильтр их смешивает)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨RLO⟩
    CODEPOINT: U+202E
    NAME: RIGHT-TO-LEFT OVERRIDE
    RISK: MEDIUM
    RULE: RIGHT_TO_LEFT_OVERRIDE ≠ ARABIC_LETTER_MARK (оверрайд форсирует направление и имеет терминатор; метка — сильный символ без обоих)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨ARABIC-SEMI⟩
    CODEPOINT: U+061B
    NAME: ARABIC SEMICOLON
    RISK: LOW
    RULE: ARABIC_SEMICOLON ≠ ARABIC_LETTER_MARK (видимый знак пунктуации рядом с ALM в блоке; видимый, не невидимая метка направления)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨ZWSP⟩
    CODEPOINT: U+200B
    NAME: ZERO WIDTH SPACE
    RISK: LOW
    RULE: ZERO_WIDTH_SPACE ≠ ARABIC_LETTER_MARK (оба невидимы, но ZWSP — точка переноса, не несущая направления)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "our scanner covers the U+200x invisibles, so we are covered"
    RESPONSE: ALM_FORM ≠ IN_U200X_RANGE_PROOF
    RULE: ALM в U+061C, вне диапазона U+200x, на котором может фокусироваться сканер
  CG2:
    TRIGGER: "an invisible char cannot be dangerous"
    RESPONSE: ALM_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: невидимость ортогональна эффекту; ALM переупорядочивает нейтралы невидимо
  CG3:
    TRIGGER: "it is an override, so look for a terminator"
    RESPONSE: ALM_FORM ≠ FORMAT_CONTROL_PROOF
    RULE: это сильный символ без терминатора и без вложенности
  CG4:
    TRIGGER: "'%D8%9C' is safe forever"
    RESPONSE: ALM_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в ALM перед отображением
  CG5:
    TRIGGER: "ALM only matters inside Arabic text"
    RESPONSE: ALM_FORM ≠ ARABIC_TEXT_ONLY_PROOF
    RULE: он может управлять направлением, вброшенный в любую строку, включая латиницу/ASCII
  CG6:
    TRIGGER: "we strip RLM, so this direction mark is handled"
    RESPONSE: ALM_FORM ≠ RLM_EQUIVALENCE_PROOF
    RULE: ALM (U+061C) — отдельный кодпойнт от RLM (U+200F)

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "neutrals + interior ALM"
      NAME: NEUTRAL_ORDER_FLIP
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: ALM, переворачивающий видимый порядок цифр/пунктуации вокруг себя
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "ALM used where a U+200x-only scanner runs"
      NAME: RANGE_SCAN_GAP
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: метка, выживающая из-за сканирования только диапазона U+200x
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "mixed ALM + RLM + LRM"
      NAME: MARK_FAMILY_MIX
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: несколько меток направления вместе для обхода фильтра одного кодпойнта
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: не применимо — эффект ALM на порядок окружающей последовательности.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: ALM переупорядочивает нейтральные прогоны (маскировка порядка), но не имитирует существование верифицированной сущности. Его риски — десинхрон визуального порядка, а не мимикрия сущности. (Подделка имени файла естественнее с оверрайдом; см. RLO/LRO.)
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена ALM на RLM (U+200F) / LRM (U+200E) для смены метки направления / обхода фильтра одного кодпойнта
  A2: percent-кодирование "%D8%9C" для проскока мимо сканера сырых байтов
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: пробел диапазонного сканирования (ALM в U+061C переживает сканирование только U+200x)
  B2: инъекция в неарабский контекст (ALM переупорядочивает внутри латиницы/ASCII, где считается нерелевантным)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "neutrals + interior ALM" (SC1) — переворот порядка нейтралов
  C2: "mixed ALM + RLM + LRM" (SC3) — смесь семейства меток
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: ALM подан как «только-арабская» фиксация направления, пока он переупорядочивает неарабскую нагрузку
  D2: "%D8%9C" как «безопасный» кодированный текст с последующим декодом
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: невидимый разворот нейтралов, обманывающий обозревателя
  E2: N/A — вектор: метка вне сканируемого диапазона, обходящая фильтр, сфокусированный на U+200x
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: сканирование невидимок U+200x покрывает и ALM
  EXPECTED: FAIL_IN_U200X_RANGE_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: невидимый символ не может быть опасен
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: ALM это формат-control с терминатором
  EXPECTED: FAIL_FORMAT_CONTROL_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%D8%9C" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: ALM важен только внутри арабского текста
  EXPECTED: FAIL_ARABIC_TEXT_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: срезание RLM обрабатывает и ALM
  EXPECTED: FAIL_RLM_EQUIVALENCE_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как перечислить ВСЕ невидимые метки и контролы направления по свойству (Bidi_Control), а не по диапазону кодпойнтов, чтобы метка вроде ALM в U+061C ловилась наряду с семейством U+200x/202x/206x, без ложных срабатываний на легитимной фиксации направления арабского контекста?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (bidi-нормализатор, реагирующий на свойство Bidi_Control, а не на жёстко заданный диапазон, покрывающий U+061C вместе с набором U+200x/202x/206x — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «ALM — сильная RTL-метка вне диапазона U+200x; диапазонный сканер её пропускает, и она не только-арабская».
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
