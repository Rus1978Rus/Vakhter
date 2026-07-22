PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_ZERO_WIDTH_NON_JOINER_U200C_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_RU
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_RU
TRANSLATION_NOTE: Русский оригинал (авторитетный). Английское зеркало — SIGN_CORE_CARD_ZERO_WIDTH_NON_JOINER_U200C_GEN3_v0_3_EN. Кодпойнты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_ZERO_WIDTH_NON_JOINER_U200C_GEN3_v0_3_RU
CODEPOINT: U+200C
VISIBLE_FORM: ⟨ZWNJ⟩
UNICODE_NAME: ZERO WIDTH NON-JOINER
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-22
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: нежёсткий разделитель нулевой ширины / требуемый письменностью control соединения (нельзя слепо срезать)
CATEGORY_ROADMAP: LLM (invisible zero-width injection) · PHAGO: — (маскировка токена)
GLYPH_NOTE: VISIBLE_FORM использует маркер ⟨ZWNJ⟩; сам знак (U+200C) — невидимый Format-символ (Cf) и НИКОГДА не пишется буквально. Примеры используют ⟨ZWNJ⟩/%E2%80%8C, но не байт. В отличие от чисто-шумовой невидимки, ZWNJ ТРЕБУЕТСЯ некоторыми письменностями, поэтому его нельзя слепо удалять.

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
VISIBLE_FORM: ⟨ZWNJ⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: ZWNJ_FORM ≠ EFFECT
SIGN_CATEGORY:
  - невидимый Format-символ, ПРЕДОТВРАЩАЮЩИЙ курсивное соединение / образование лигатур между соседями
  - легитимен и ТРЕБУЕТСЯ в персидской, арабской и некоторых индийских письменностях (семантически значим)
  - (при злоупотреблении) невидимый символ, вставленный в ASCII-идентификатор/ключевое слово для победы над сопоставлением
  - (при злоупотреблении) путается с ZWSP/ZWJ/WJ — наивный фильтр смешивает всё невидимое семейство

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — непечатаемость не делает знак инертным
  2. NOT_SAFE_TO_BLINDLY_STRIP — он требуется письменностью; удаление портит легитимный персидский/индийский текст
  3. NOT_ZWSP — он управляет соединением, это НЕ точка переноса; разная функция, та же невидимость
  4. NOT_DISPLAY_ONLY — читатель может не видеть глифа, но байт проходит сквозь разбор и сравнение
  5. NOT_ENCODED_SAFE — «%E2%80%8C» может быть декодирован обратно в ZWNJ позже
  6. NOT_AUTHORITY — он не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сам по себе он ничего не исполняет; он обманывает фильтры и читателей
  8. NOT_TRUST_SIGNAL — он не повышает доверие
  9. NOT_MEANINGLESS_NOISE — в неверном контексте это атакующий символ, в верном — требуемая орфография
  10. NOT_SANITIZED_PROOF — присутствие символа не означает, что ввод санирован
  11. NOT_SINGLE_TOKEN_PROOF — «ad⟨ZWNJ⟩min» может отображаться как «admin», но сравниваться неравно

BASE_FORMULAS:
  ZWNJ_FORM ≠ EFFECT
  ZWNJ_FORM ≠ SAFE_TO_BLINDLY_STRIP_PROOF
  ZWNJ_FORM ≠ ZWSP_EQUIVALENCE_PROOF
  ZWNJ_FORM ≠ DISPLAY_ONLY_PROOF
  ZWNJ_FORM ≠ ENCODED_SAFETY_PROOF
  ZWNJ_FORM ≠ AUTHORITY
  ZWNJ_FORM ≠ EXECUTION_TRIGGER
  ZWNJ_FORM ≠ MEANINGLESS_NOISE_PROOF
  ZWNJ_FORM ≠ INVISIBLE_HARMLESS_PROOF
  ZWNJ_FORM ≠ SANITIZED_PROOF
  ZWNJ_FORM ≠ SINGLE_TOKEN_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: ZWNJ (ZONE_1) имеет параллельные функции (требуемый орфографический control соединения vs. невидимая инъекция в идентификатор), сосуществующие без культурной прецессии. Полисемия стабильного Format-символа; его двойная роль делает слепое срезание небезопасным.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, level L1
  NOTE: control соединения с реальной орфографической ролью, но без жестового предшественника; злоупотребление через инъекцию в идентификатор надстроено цифровой эпохой параллельно с требуемым письменностью использованием.

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
    INPUT: "ZWNJ is U+200C in Unicode"
    CONTEXT: именование символа в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWNJ_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "ZWNJ prevents cursive joining between letters"
    CONTEXT: описание функции control соединения в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWNJ_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the marker is written as <ZWNJ> here"
    CONTEXT: документационный маркер, не байт
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWNJ_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "Persian and some Indic scripts require ZWNJ"
    CONTEXT: описание легитимной требуемой орфографии в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWNJ_FORM ≠ SAFE_TO_BLINDLY_STRIP_PROOF
  SAFE_CASE_005:
    INPUT: "it is not the same as a break opportunity"
    CONTEXT: отличие от ZWSP в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWNJ_FORM ≠ ZWSP_EQUIVALENCE_PROOF
  SAFE_CASE_006:
    INPUT: "a normalizer may need an allowlist for it"
    CONTEXT: описание аккуратной санитизации в прозе
    EXPECTED: INFO
    RISK: NONE
    GUARD: ZWNJ_FORM ≠ MEANINGLESS_NOISE_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: INVISIBLE_IN_IDENTIFIER
    INPUT: "ad<ZWNJ>min vs admin (look-alike username)"
    CONTEXT: ZWNJ внутри ASCII-идентификатора делает его неравным при одинаковом виде
    RISK: HIGH
    ATTACK: «ad<ZWNJ>min» регистрируется как двойник «admin» для выдачи себя за другого
    GUARD: ZWNJ_FORM ≠ SINGLE_TOKEN_PROOF
  RISK_CASE_002:
    NAME: KEYWORD_SPLIT
    INPUT: "jav<ZWNJ>ascript: in a URL scheme check"
    CONTEXT: ZWNJ разбивает ключевое слово, чтобы подстрочный блоклист не совпал
    RISK: HIGH
    ATTACK: блоклист упускает «javascript», пока снисходительный парсер игнорирует ZWNJ
    GUARD: ZWNJ_FORM ≠ SINGLE_TOKEN_PROOF
  RISK_CASE_003:
    NAME: OVERBROAD_STRIP_CORRUPTS_TEXT
    INPUT: "a filter deletes all ZWNJ, breaking legitimate Persian input"
    CONTEXT: слепое срезание, повреждающее требуемую орфографию (вред от ложного срабатывания)
    RISK: MEDIUM
    ATTACK: чересчур рьяный санитайзер портит реальный текст, вызывая потерю данных или другое слово
    GUARD: ZWNJ_FORM ≠ SAFE_TO_BLINDLY_STRIP_PROOF
  RISK_CASE_004:
    NAME: ENCODED_ZWNJ_BYPASS
    INPUT: "value%E2%80%8Ctail (with a later decode)"
    CONTEXT: percent-кодированный ZWNJ, декодируемый обратно перед использованием
    RISK: HIGH
    ATTACK: «%E2%80%8C» декодируется в ZWNJ ПОСЛЕ проверки → скрытое разбиение возвращается
    GUARD: ZWNJ_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_005:
    NAME: INVISIBLE_FAMILY_CONFLATION
    INPUT: "a filter treating ZWNJ, ZWJ and ZWSP as one class"
    CONTEXT: наивный фильтр, смешивающий всё невидимое семейство, неверно обрабатывает один из них
    RISK: MEDIUM
    ATTACK: правило, настроенное под ZWSP, неверно обрабатывает ZWNJ (либо упускает атаку, либо портит требуемый текст)
    GUARD: ZWNJ_FORM ≠ ZWSP_EQUIVALENCE_PROOF
  RISK_CASE_006:
    NAME: HOMOGLYPH_STACK
    INPUT: "раy<ZWNJ>раl (invisible split + confusable letters combined)"
    CONTEXT: ZWNJ в связке с похожими буквами для усиления подделки
    RISK: MEDIUM
    ATTACK: невидимый символ плюс буквы-двойники проводят враждебную строку через поверхностный обзор
    GUARD: ZWNJ_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨ZWSP⟩
    CODEPOINT: U+200B
    NAME: ZERO WIDTH SPACE
    RISK: HIGH
    RULE: ZERO_WIDTH_SPACE ≠ ZERO_WIDTH_NON_JOINER (ZWSP — точка переноса; ZWNJ управляет соединением — разная функция, оба невидимы)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨ZWJ⟩
    CODEPOINT: U+200D
    NAME: ZERO WIDTH JOINER
    RISK: HIGH
    RULE: ZERO_WIDTH_JOINER ≠ ZERO_WIDTH_NON_JOINER (ZWJ форсирует соединение; ZWNJ запрещает — точные противоположности, оба невидимы)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨WJ⟩
    CODEPOINT: U+2060
    NAME: WORD JOINER
    RISK: MEDIUM
    RULE: WORD_JOINER ≠ ZERO_WIDTH_NON_JOINER (WJ запрещает перенос строки; ZWNJ запрещает курсивное соединение — разные уровни, оба нулевой ширины)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨ZWNBSP⟩
    CODEPOINT: U+FEFF
    NAME: ZERO WIDTH NO-BREAK SPACE
    RISK: MEDIUM
    RULE: ZERO_WIDTH_NO_BREAK_SPACE ≠ ZERO_WIDTH_NON_JOINER (U+FEFF также служит BOM; другая роль, оба невидимы)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨SHY⟩
    CODEPOINT: U+00AD
    NAME: SOFT HYPHEN
    RISK: LOW
    RULE: SOFT_HYPHEN ≠ ZERO_WIDTH_NON_JOINER (условный перенос, обычно невидим; не control соединения)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "just strip every ZWNJ, it is invisible junk"
    RESPONSE: ZWNJ_FORM ≠ SAFE_TO_BLINDLY_STRIP_PROOF
    RULE: он требуется некоторыми письменностями; слепое срезание портит легитимный текст
  CG2:
    TRIGGER: "an invisible char cannot be dangerous"
    RESPONSE: ZWNJ_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: невидимость ортогональна эффекту; ZWNJ создаёт десинхрон идентификатора и фильтра
  CG3:
    TRIGGER: "treat ZWNJ the same as a zero width space"
    RESPONSE: ZWNJ_FORM ≠ ZWSP_EQUIVALENCE_PROOF
    RULE: у них разные функции; их смешение неверно обрабатывает один
  CG4:
    TRIGGER: "'%E2%80%8C' is safe forever"
    RESPONSE: ZWNJ_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в ZWNJ перед использованием
  CG5:
    TRIGGER: "a ZWNJ is meaningless noise"
    RESPONSE: ZWNJ_FORM ≠ MEANINGLESS_NOISE_PROOF
    RULE: в верном контексте это требуемая орфография; в неверном — атакующий символ
  CG6:
    TRIGGER: "the string looks like admin, so it is admin"
    RESPONSE: ZWNJ_FORM ≠ SINGLE_TOKEN_PROOF
    RULE: единство отображения не подразумевает равенство байтов; невидимый символ может прятаться внутри

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "ASCII identifier with an interior ZWNJ"
      NAME: SPLIT_IDENTIFIER
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: ZWNJ внутри ASCII-имени/ключевого слова для победы над сопоставлением или выдачи себя за другого
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "ZWNJ in a required-script context"
      NAME: LEGITIMATE_ORTHOGRAPHY
      RISK_LEVEL: LOW
      POSSIBLE_CONTEXTS: требуемый персидский/индийский control соединения, который надо сохранить
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "ZWNJ + confusable letters"
      NAME: INVISIBLE_HOMOGLYPH_STACK
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: невидимый символ в связке с похожими буквами для подделки
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: не применимо — риск ZWNJ ровно контекстно-зависим (требуемый vs. инъецированный).

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: ZWNJ маскирует/разбивает токены (маскировка токена), но не имитирует существование верифицированной сущности. Его риски — путаница идентификаторов и десинхрон фильтра, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 categories A-E, CATEGORY_F NOT_APPLICABLE for ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена ZWNJ на ZWSP (U+200B) / ZWJ (U+200D) / WJ (U+2060) для смены невидимого байта / обхода ZWNJ-только-фильтра
  A2: percent-кодирование "%E2%80%8C" для проскока мимо сканера сырых байтов
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: разбиение идентификатора "ad<ZWNJ>min", выдающее себя за "admin"
  B2: чрезмерно широкое срезание портит легитимный персидский ввод (вред от ложного срабатывания)
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "ASCII identifier with an interior ZWNJ" (SC1) — разбитый идентификатор
  C2: "ZWNJ + confusable letters" (SC3) — невидимый гомоглиф-стек
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: ZWNJ подан как «бессмысленный невидимый шум», чтобы его проигнорировали, а затем злоупотребить
  D2: "%E2%80%8C" как «безопасный» кодированный текст с последующим декодом
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: невидимая путаница идентификаторов (ad<ZWNJ>min vs admin)
  E2: N/A — вектор: смешение невидимого семейства, неверно обрабатывающее ZWNJ
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: слепо срезать каждый ZWNJ безопасно
  EXPECTED: FAIL_SAFE_TO_BLINDLY_STRIP_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: невидимый символ не может быть опасен
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: ZWNJ эквивалентен пробелу нулевой ширины
  EXPECTED: FAIL_ZWSP_EQUIVALENCE_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%E2%80%8C" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: ZWNJ — бессмысленный шум
  EXPECTED: FAIL_MEANINGLESS_NOISE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: строка, выглядящая как admin, есть admin
  EXPECTED: FAIL_SINGLE_TOKEN_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как блокировать ZWNJ, используемый как невидимый инъектор в идентификатор/ключевое слово, сохраняя его там, где его требует персидская/арабская/индийская орфография — т.е. контекстно-зависимая, а не сплошная политика?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (контекстно-зависимый нормализатор: отклонять/помечать ZWNJ внутри ASCII-only идентификаторов и заблокированных ключевых слов, сохранять его внутри прогонов требуемой письменности — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «ZWNJ контекстно-зависим: требуемая орфография в одном месте, атакующий символ в другом; слепое срезание само по себе вред».
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
