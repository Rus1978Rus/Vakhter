PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_ZERO_WIDTH_JOINER_U200D_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
TRANSLATION_NOTE: Русский оригинал (авторитетный). Английское зеркало — SIGN_CORE_CARD_ZERO_WIDTH_JOINER_U200D_GEN3_v0_3_EN. Кодпойнты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_ZERO_WIDTH_JOINER_U200D_GEN3_v0_3_RU
CODEPOINT: U+200D
VISIBLE_FORM: ⟨ZWJ⟩
UNICODE_NAME: ZERO WIDTH JOINER
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: соединитель нулевой ширины / control эмодзи-последовательностей и курсивного соединения (один графем, много кодпойнтов)
CATEGORY_ROADMAP: LLM (invisible zero-width injection) · PHAGO: — (маскировка токена / длины)
GLYPH_NOTE: VISIBLE_FORM использует маркер ⟨ZWJ⟩; сам знак (U+200D) — невидимый Format-символ (Cf) и НИКОГДА не пишется буквально. Примеры используют ⟨ZWJ⟩/%E2%80%8D, но не байт. ZWJ ТРЕБУЕТСЯ для построения эмодзи-ZWJ-последовательностей, поэтому его нельзя слепо срезать.

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
VISIBLE_FORM: ⟨ZWJ⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: ZWJ_FORM ≠ EFFECT
SIGN_CATEGORY:
  - невидимый Format-символ, ФОРСИРУЮЩИЙ соединение: курсивное соединение и эмодзи-ZWJ-последовательности (много кодпойнтов → один графем)
  - легитимен и ТРЕБУЕТСЯ для отрисовки составных эмодзи (напр. многолюдных / профессиональных эмодзи) и некоторых письменностей
  - (при злоупотреблении) один отображаемый графем прячет несколько кодпойнтов → десинхрон длины/разбора
  - (при злоупотреблении) невидимый символ, вставленный в идентификатор/ключевое слово для победы над сопоставлением

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — непечатаемость не делает знак инертным
  2. NOT_SAFE_TO_BLINDLY_STRIP — он требуется для формирования эмодзи-ZWJ-последовательностей; удаление ломает легитимные графемы
  3. NOT_ZWNJ — он ФОРСИРУЕТ соединение; ZWNJ его запрещает — точные противоположности, оба невидимы
  4. NOT_ONE_GRAPHEME_IS_ONE_CODEPOINT — один отображаемый глиф может быть многими кодпойнтами, соединёнными ZWJ (длина лжёт)
  5. NOT_ENCODED_SAFE — «%E2%80%8D» может быть декодирован обратно в ZWJ позже
  6. NOT_AUTHORITY — он не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сам по себе он ничего не исполняет; он обманывает фильтры, читателей и проверки длины
  8. NOT_TRUST_SIGNAL — он не повышает доверие
  9. NOT_MEANINGLESS_NOISE — требуемая орфография/эмодзи в одном контексте, атакующий символ в другом
  10. NOT_SANITIZED_PROOF — присутствие символа не означает, что ввод санирован
  11. NOT_LENGTH_TRUTH — счёт графемов и счёт кодпойнтов расходятся, когда ZWJ соединяет прогоны

BASE_FORMULAS:
  ZWJ_FORM ≠ EFFECT
  ZWJ_FORM ≠ SAFE_TO_BLINDLY_STRIP_PROOF
  ZWJ_FORM ≠ ZWNJ_EQUIVALENCE_PROOF
  ZWJ_FORM ≠ ONE_GRAPHEME_ONE_CODEPOINT_PROOF
  ZWJ_FORM ≠ ENCODED_SAFETY_PROOF
  ZWJ_FORM ≠ AUTHORITY
  ZWJ_FORM ≠ EXECUTION_TRIGGER
  ZWJ_FORM ≠ MEANINGLESS_NOISE_PROOF
  ZWJ_FORM ≠ INVISIBLE_HARMLESS_PROOF
  ZWJ_FORM ≠ SANITIZED_PROOF
  ZWJ_FORM ≠ LENGTH_TRUTH_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: ZWJ (ZONE_1) имеет параллельные функции (требуемое эмодзи/курсивное соединение vs. невидимая инъекция и маскировка длины), сосуществующие без культурной прецессии. Полисемия стабильного Format-символа; его эмодзи-роль делает слепое срезание небезопасным.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: control соединения с реальной эмодзи/орфографической ролью, но без жестового предшественника; злоупотребление через маскировку длины и инъекцию надстроено цифровой эпохой параллельно с требуемым использованием.

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
    INPUT: "ZWJ is U+200D in Unicode"
    CONTEXT: именование символа в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWJ_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "ZWJ joins codepoints into one emoji grapheme"
    CONTEXT: описание функции эмодзи-последовательности в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWJ_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <ZWJ> here"
    CONTEXT: документационный маркер, не байт
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWJ_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "emoji ZWJ sequences require the joiner"
    CONTEXT: описание легитимного требуемого использования в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWJ_FORM ≠ SAFE_TO_BLINDLY_STRIP_PROOF
  SAFE_CASE_005:
    INPUT: "it forces joining, the opposite of a non-joiner"
    CONTEXT: отличие от ZWNJ в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWJ_FORM ≠ ZWNJ_EQUIVALENCE_PROOF
  SAFE_CASE_006:
    INPUT: "grapheme count and codepoint count can differ"
    CONTEXT: проза про метрики длины текста
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWJ_FORM ≠ ONE_GRAPHEME_ONE_CODEPOINT_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: LENGTH_COUNT_DESYNC
    INPUT: "one displayed emoji that is 5 codepoints joined by ZWJ"
    CONTEXT: проверка длины, где счёт графемов и кодпойнтов расходятся
    RISK: HIGH
    ATTACK: ввод, который «выглядит как 1 символ», есть много кодпойнтов, побеждая лимит длины или раздувая хранилище
    GUARD: ZWJ_FORM ≠ LENGTH_TRUTH_PROOF
  RISK_CASE_002:
    NAME: INVISIBLE_IN_IDENTIFIER
    INPUT: "ad<ZWJ>min vs admin (look-alike username)"
    CONTEXT: ZWJ внутри ASCII-идентификатора делает его неравным при одинаковом виде
    RISK: HIGH
    ATTACK: «ad<ZWJ>min» регистрируется как двойник «admin» для выдачи себя за другого
    GUARD: ZWJ_FORM ≠ ONE_GRAPHEME_ONE_CODEPOINT_PROOF
  RISK_CASE_003:
    NAME: OVERBROAD_STRIP_BREAKS_EMOJI
    INPUT: "a filter deletes all ZWJ, splitting a family emoji into parts"
    CONTEXT: слепое срезание, портящее легитимную эмодзи-ZWJ-последовательность (вред от ложного срабатывания)
    RISK: MEDIUM
    ATTACK: чересчур рьяный санитайзер превращает один задуманный глиф в несколько, меняя смысл
    GUARD: ZWJ_FORM ≠ SAFE_TO_BLINDLY_STRIP_PROOF
  RISK_CASE_004:
    NAME: ENCODED_ZWJ_BYPASS
    INPUT: "value%E2%80%8Dtail (with a later decode)"
    CONTEXT: percent-кодированный ZWJ, декодируемый обратно перед использованием
    RISK: HIGH
    ATTACK: «%E2%80%8D» декодируется в ZWJ ПОСЛЕ проверки → скрытое соединение возвращается
    GUARD: ZWJ_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: INVISIBLE_FAMILY_CONFLATION
    INPUT: "a filter treating ZWJ the same as ZWNJ or ZWSP"
    CONTEXT: наивный фильтр, смешивающий невидимое семейство, неверно обрабатывает соединитель
    RISK: MEDIUM
    ATTACK: правило, настроенное под нежёсткий разделитель, неверно обрабатывает ZWJ (либо упускает атаку, либо ломает эмодзи)
    GUARD: ZWJ_FORM ≠ ZWNJ_EQUIVALENCE_PROOF
  RISK_CASE_006:
    NAME: HOMOGLYPH_STACK
    INPUT: "раy<ZWJ>раl (invisible joiner + confusable letters combined)"
    CONTEXT: ZWJ в связке с похожими буквами для усиления подделки
    RISK: MEDIUM
    ATTACK: невидимый символ плюс буквы-двойники проводят враждебную строку через поверхностный обзор
    GUARD: ZWJ_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨ZWNJ⟩
    CODEPOINT: U+200C
    NAME: ZERO WIDTH NON-JOINER
    RISK: HIGH
    RULE: ZERO_WIDTH_NON_JOINER ≠ ZERO_WIDTH_JOINER (ZWNJ запрещает соединение; ZWJ форсирует — точные противоположности, оба невидимы)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨ZWSP⟩
    CODEPOINT: U+200B
    NAME: ZERO WIDTH SPACE
    RISK: HIGH
    RULE: ZERO_WIDTH_SPACE ≠ ZERO_WIDTH_JOINER (ZWSP — точка переноса; ZWJ форсирует соединение — разная функция, оба невидимы)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨WJ⟩
    CODEPOINT: U+2060
    NAME: WORD JOINER
    RISK: MEDIUM
    RULE: WORD_JOINER ≠ ZERO_WIDTH_JOINER («joiner» только в названии: WJ запрещает перенос строки, ZWJ соединяет глифы — разные уровни)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨ZWNBSP⟩
    CODEPOINT: U+FEFF
    NAME: ZERO WIDTH NO-BREAK SPACE
    RISK: MEDIUM
    RULE: ZERO_WIDTH_NO_BREAK_SPACE ≠ ZERO_WIDTH_JOINER (U+FEFF также служит BOM; другая роль, оба невидимы)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨VS16⟩
    CODEPOINT: U+FE0F
    NAME: VARIATION SELECTOR-16
    RISK: LOW
    RULE: VARIATION_SELECTOR_16 ≠ ZERO_WIDTH_JOINER (VS16 запрашивает эмодзи-представление; оба встречаются в эмодзи-последовательностях, но делают разную работу)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "just strip every ZWJ, it is invisible junk"
    RESPONSE: ZWJ_FORM ≠ SAFE_TO_BLINDLY_STRIP_PROOF
    RULE: он требуется для построения эмодзи-ZWJ-последовательностей; слепое срезание портит легитимные графемы
  CG2:
    TRIGGER: "an invisible char cannot be dangerous"
    RESPONSE: ZWJ_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: невидимость ортогональна эффекту; ZWJ создаёт десинхрон длины и идентификатора
  CG3:
    TRIGGER: "treat ZWJ the same as a non-joiner"
    RESPONSE: ZWJ_FORM ≠ ZWNJ_EQUIVALENCE_PROOF
    RULE: они точные противоположности; их смешение неверно обрабатывает один
  CG4:
    TRIGGER: "'%E2%80%8D' is safe forever"
    RESPONSE: ZWJ_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в ZWJ перед использованием
  CG5:
    TRIGGER: "one glyph means one codepoint"
    RESPONSE: ZWJ_FORM ≠ ONE_GRAPHEME_ONE_CODEPOINT_PROOF
    RULE: ZWJ-последовательность отрисовывает много кодпойнтов как один графем; счёты расходятся
  CG6:
    TRIGGER: "the length check counted it, so the length is safe"
    RESPONSE: ZWJ_FORM ≠ LENGTH_TRUTH_PROOF
    RULE: счёты графемов и кодпойнтов различаются; лимит длины можно победить или ложно превысить

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "emoji ZWJ sequence (codepoint + ZWJ + codepoint ...)"
      NAME: JOINED_GRAPHEME
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: много кодпойнтов, отображаемых как один глиф, расходящихся со счётом кодпойнтов
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "ASCII identifier with an interior ZWJ"
      NAME: SPLIT_IDENTIFIER
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: ZWJ внутри ASCII-имени для выдачи себя за другого или победы над сопоставлением
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "long ZWJ chain"
      NAME: GRAPHEME_BOMB
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: очень длинная цепочка соединённых кодпойнтов, раздувающая обработку/хранилище за одним глифом
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: не применимо — ядро поведения ZWJ есть соединение последовательностей.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: ZWJ соединяет/маскирует токены и длины (маскировка токена/длины), но не имитирует существование верифицированной сущности. Его риски — десинхрон длины и путаница идентификаторов, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена ZWJ на ZWNJ (U+200C) / ZWSP (U+200B) / WJ (U+2060) для смены невидимого байта / обхода ZWJ-только-фильтра
  A2: percent-кодирование "%E2%80%8D" для проскока мимо сканера сырых байтов
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: десинхрон счёта длины (один отображаемый эмодзи = много кодпойнтов, побеждающих лимит длины)
  B2: чрезмерно широкое срезание разбивает семейный эмодзи (вред от ложного срабатывания)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "long ZWJ chain" (SC3) — графем-бомба за одним глифом
  C2: "ASCII identifier with an interior ZWJ" (SC2) — разбитый идентификатор
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: ZWJ подан как «просто эмодзи-соединитель», чтобы его проигнорировали, а затем злоупотребить в идентификаторе
  D2: "%E2%80%8D" как «безопасный» кодированный текст с последующим декодом
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: невидимая путаница идентификаторов (ad<ZWJ>min vs admin)
  E2: N/A — вектор: смешение невидимого семейства, неверно обрабатывающее соединитель
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: слепо срезать каждый ZWJ безопасно
  EXPECTED: FAIL_SAFE_TO_BLINDLY_STRIP_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: невидимый символ не может быть опасен
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: ZWJ эквивалентен нежёсткому разделителю
  EXPECTED: FAIL_ZWNJ_EQUIVALENCE_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%E2%80%8D" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: один отображаемый глиф есть ровно один кодпойнт
  EXPECTED: FAIL_ONE_GRAPHEME_ONE_CODEPOINT_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: счёт графемов есть истинная длина
  EXPECTED: FAIL_LENGTH_TRUTH_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как блокировать ZWJ, используемый как невидимый инъектор в идентификатор или графем-бомба, сохраняя его внутри легитимных эмодзи-ZWJ-последовательностей и требуемых письменностей — контекстно-зависимая, а не сплошная политика, плюс политика длины, считающая кодпойнты, а не графемы для лимитов?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (контекстно-зависимый нормализатор + политика длины на основе кодпойнтов: отклонять/помечать ZWJ внутри ASCII-only идентификаторов, лимитировать по кодпойнтам, сохранять эмодзи-последовательности — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «один графем не есть один кодпойнт; ZWJ требуется для эмодзи, но атакующий символ в идентификаторах; слепое срезание само по себе вред».
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
