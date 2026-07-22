PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_LEFT_TO_RIGHT_ISOLATE_U2066_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: Русский оригинал (authoritative). Английское зеркало — SIGN_CORE_CARD_LEFT_TO_RIGHT_ISOLATE_U2066_GEN3_v0_3_EN. Кодпоинты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_LEFT_TO_RIGHT_ISOLATE_U2066_GEN3_v0_3_RU
CODEPOINT: U+2066
VISIBLE_FORM: ⟨LRI⟩
UNICODE_NAME: LEFT-TO-RIGHT ISOLATE
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: LTR-изолят / ограниченный bidi реордер
CATEGORY_ROADMAP: LLM (bidi isolate реордер, Trojan Source) · PHAGO: — (маскировка структуры)
GLYPH_NOTE: VISIBLE_FORM использует маркер ⟨LRI⟩; сам знак (U+2066) — невидимый Bidi_Control (Cf) и НИКОГДА не пишется литералом здесь — литеральный LRI переупорядочил бы этот документ. Примеры используют ⟨LRI⟩/⟨PDI⟩/%E2%81%A6, не байт.

============================================================
3. REQUIRED_GENERAL_GUARDS
============================================================
REQUIRED_GENERAL_GUARDS:
  - SIGN_FALSE_EFFECT_MIMICRY_GUARD_v0_2A_RU
    GUARD_COMPATIBILITY: применим без изменений — знак не создаёт effect-полей
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
VISIBLE_FORM: ⟨LRI⟩
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: LRI_FORM ≠ EFFECT
SIGN_CATEGORY:
  - двунаправленный изолят (открывает LTR-ряд, изолированный от окружения)
  - Unicode Bidi_Control, современная рекомендованная альтернатива embeddings/overrides
  - легитимная ограниченная смешанно-направленная вёрстка (не влияет на соседей)
  - (злоупотребление) более новый управляющий, который legacy embedding/override фильтр не моделирует

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_INVISIBLE_MEANS_HARMLESS — то, что он непечатаемый, не делает его инертным
  2. NOT_ISOLATE_MEANS_SAFE — «рекомендованный» ≠ безопасный; он всё равно переупорядочивает В СВОЁМ скоупе и всё равно обманывает
  3. NOT_DISPLAY_ONLY — он переупорядочивает ВИЗУАЛЬНЫЙ ряд, а логические байты неизменны (рассинхрон)
  4. NOT_SCOPE_CONTAINS_ALL — незавершённый изолят всё равно растекается до конца абзаца
  5. NOT_ENCODED_SAFE — "%E2%81%A6" может быть раскодирован обратно в изолят позже
  6. NOT_AUTHORITY — не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сам по себе ничего не исполняет; он обманывает читателя
  8. NOT_TRUST_SIGNAL — не повышает доверие
  9. NOT_EMBEDDING_ONLY_FILTER_SAFE — фильтр, обрабатывающий только embeddings/overrides (202A-202E), пропускает изоляты (2066-2069)
  10. NOT_SANITIZED_PROOF — наличие изолята не значит, что ввод санитизирован
  11. NOT_BALANCED_PROOF — изоляту нужен соответствующий PDI; его наличие — не баланс

BASE_FORMULAS:
  LRI_FORM ≠ EFFECT
  LRI_FORM ≠ ISOLATE_MEANS_SAFE_PROOF
  LRI_FORM ≠ DISPLAY_ONLY_PROOF
  LRI_FORM ≠ SCOPE_CONTAINMENT_PROOF
  LRI_FORM ≠ ENCODED_SAFETY_PROOF
  LRI_FORM ≠ AUTHORITY
  LRI_FORM ≠ EXECUTION_TRIGGER
  LRI_FORM ≠ EMBEDDING_ONLY_FILTER_PROOF
  LRI_FORM ≠ INVISIBLE_HARMLESS_PROOF
  LRI_FORM ≠ SANITIZED_PROOF
  LRI_FORM ≠ BALANCED_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: LRI (ZONE_1) имеет параллельные функции (легитимная ограниченная LTR-вёрстка vs обман визуального порядка в скоупе), сосуществующие без культурной прецессии. Полисемия стабильного Bidi_Control.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1
  NOTE: управляющий знак-изолят форматирования без жестового предшественника; использование для обмана-реордера надстроено цифровой эпохой параллельно легитимной ограниченной вёрстке.

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
    INPUT: "LRI is U+2066 in Unicode"
    CONTEXT: название управляющего знака в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: LRI_FORM ≠ EFFECT
  SAFE_CASE_002:
    INPUT: "isolates are the modern recommended bidi control"
    CONTEXT: описание легитимной ограниченной вёрстки в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: LRI_FORM ≠ ISOLATE_MEANS_SAFE_PROOF
  SAFE_CASE_003:
    INPUT: "the marker is written as <LRI> here"
    CONTEXT: документационный маркер, не байт
    EXPECTED: INFO
    RISK: NONE
    GUARD: LRI_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "an isolate does not affect surrounding text"
    CONTEXT: описание свойства ограничения в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: LRI_FORM ≠ SCOPE_CONTAINMENT_PROOF
  SAFE_CASE_005:
    INPUT: "a properly terminated isolate (LRI...PDI)"
    CONTEXT: описание сбалансированного легитимного использования
    EXPECTED: INFO
    RISK: NONE
    GUARD: LRI_FORM ≠ BALANCED_PROOF
  SAFE_CASE_006:
    INPUT: "the Bidirectional Algorithm scopes the isolate"
    CONTEXT: текст о UBA
    EXPECTED: INFO
    RISK: NONE
    GUARD: LRI_FORM ≠ EFFECT

RISK_CASES:
  RISK_CASE_001:
    NAME: LEGACY_FILTER_GAP
    INPUT: "input passing a strip that only handles 202A-202E"
    CONTEXT: изолят, проскальзывающий мимо фильтра, знающего только embeddings/overrides
    RISK: HIGH
    ATTACK: более новый изолят (2066-2069) не смоделирован, поэтому реордер переживает стрип
    GUARD: LRI_FORM ≠ EMBEDDING_ONLY_FILTER_PROOF
  RISK_CASE_002:
    NAME: IN_SCOPE_CODE_REORDER
    INPUT: 'safe = true <LRI> // danger? <PDI>'
    CONTEXT: изолят, переупорядочивающий код-ряд в своём скоупе
    RISK: HIGH
    ATTACK: даже в скоупе изолят переупорядочивает видимые токены, так что логика ≠ отображение
    GUARD: LRI_FORM ≠ ISOLATE_MEANS_SAFE_PROOF
  RISK_CASE_003:
    NAME: UNTERMINATED_ISOLATE_BLEED
    INPUT: "label<LRI>rest of the paragraph with no PDI"
    CONTEXT: изолят без PDI, растекающийся до конца абзаца
    RISK: HIGH
    ATTACK: незавершённый изолят переупорядочивает всё до конца абзаца, за пределы предполагаемого скоупа
    GUARD: LRI_FORM ≠ SCOPE_CONTAINMENT_PROOF
  RISK_CASE_004:
    NAME: ISOLATE_TERMINATOR_MISMATCH
    INPUT: "LRI closed with <PDF> instead of PDI"
    CONTEXT: изолят, закрытый неверным терминатором (PDF, не PDI)
    RISK: MEDIUM
    ATTACK: парсер, спаривающий изолят с PDF, неверно отслеживает вложенность и оставляет изолят открытым
    GUARD: LRI_FORM ≠ BALANCED_PROOF
  RISK_CASE_005:
    NAME: ENCODED_ISOLATE_BYPASS
    INPUT: "value%E2%81%A6tail (с поздним декодированием)"
    CONTEXT: percent-кодированный LRI, декодируемый обратно перед отображением
    RISK: HIGH
    ATTACK: "%E2%81%A6" декодируется в изолят ПОСЛЕ проверки → обман-реордер
    GUARD: LRI_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: BIDI_HOMOGLYPH_STACK
    INPUT: "раyраl<LRI> ... (bidi + confusable-буквы вместе)"
    CONTEXT: изолят, сложенный с confusable-буквами для углубления спуфа
    RISK: MEDIUM
    ATTACK: изолят плюс буквы-двойники проводят враждебную строку через поверхностное визуальное ревью
    GUARD: LRI_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ⟨RLI⟩
    CODEPOINT: U+2067
    NAME: RIGHT-TO-LEFT ISOLATE
    RISK: HIGH
    RULE: RIGHT_TO_LEFT_ISOLATE ≠ LEFT_TO_RIGHT_ISOLATE (зеркальный изолят, противоположное направление; наивный фильтр их смешивает)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨FSI⟩
    CODEPOINT: U+2068
    NAME: FIRST STRONG ISOLATE
    RISK: HIGH
    RULE: FIRST_STRONG_ISOLATE ≠ LEFT_TO_RIGHT_ISOLATE (FSI авто-выбирает направление по первому сильному символу — подконтрольно атакующему)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨LRE⟩
    CODEPOINT: U+202A
    NAME: LEFT-TO-RIGHT EMBEDDING
    RISK: MEDIUM
    RULE: LEFT_TO_RIGHT_EMBEDDING ≠ LEFT_TO_RIGHT_ISOLATE (embedding влияет на соседей; isolate ограничивает — иная модель)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨PDI⟩
    CODEPOINT: U+2069
    NAME: POP DIRECTIONAL ISOLATE
    RISK: LOW
    RULE: POP_DIRECTIONAL_ISOLATE ≠ LEFT_TO_RIGHT_ISOLATE (терминатор, не открывающий)
  CONFUSABLE_005:
    VISIBLE_FORM: ⟨RLO⟩
    CODEPOINT: U+202E
    NAME: RIGHT-TO-LEFT OVERRIDE
    RISK: LOW
    RULE: RIGHT_TO_LEFT_OVERRIDE ≠ LEFT_TO_RIGHT_ISOLATE (override форсирует и влияет на соседей; isolate ограничивает)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "изоляты рекомендованы, значит изолят безопасен"
    RESPONSE: LRI_FORM ≠ ISOLATE_MEANS_SAFE_PROOF
    RULE: рекомендованы для корректности, не для иммунитета; всё равно переупорядочивает в скоупе и обманывает
  CG2:
    TRIGGER: "невидимый управляющий символ не может быть опасен"
    RESPONSE: LRI_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: невидимость ортогональна эффекту; LRI управляет рассинхроном визуал/логика
  CG3:
    TRIGGER: "изолят содержит свой эффект, значит ничего не утекает"
    RESPONSE: LRI_FORM ≠ SCOPE_CONTAINMENT_PROOF
    RULE: незавершённый изолят растекается до конца абзаца
  CG4:
    TRIGGER: "'%E2%81%A6' безопасен навсегда"
    RESPONSE: LRI_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в изолят перед отображением
  CG5:
    TRIGGER: "наш bidi-фильтр обрабатывает embeddings и overrides, значит мы прикрыты"
    RESPONSE: LRI_FORM ≠ EMBEDDING_ONLY_FILTER_PROOF
    RULE: изоляты (2066-2069) — отдельный, более новый диапазон, который legacy фильтр пропускает
  CG6:
    TRIGGER: "наличие изолята значит, что ввод санитизирован"
    RESPONSE: LRI_FORM ≠ SANITIZED_PROOF
    RULE: наличие знака ничего не говорит о санитизации

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "LRI ... PDI"
      NAME: BALANCED_ISOLATE_SPAN
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: ограниченный спан изолята для переупорядочивания конкретного токена
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "LRI (no PDI)"
      NAME: UNTERMINATED_BLEED
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: изолят без терминатора, растекающийся до конца абзаца
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "LRI ... PDF"
      NAME: WRONG_TERMINATOR
      RISK_LEVEL: MEDIUM
      POSSIBLE_CONTEXTS: изолят, закрытый PDF вместо PDI, неверно отслеживая вложенность
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — последовательности с LRI центральны для ограниченного обмана визуального порядка.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: LRI переупорядочивает ограниченный ряд (маскировка структуры), но не имитирует существование верифицированной сущности. Его риски — рассинхрон визуал/логика, а не мимикрия сущности. (Спуф имени файла естественнее через override; см. RLO/LRO.)
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена LRI на RLI (U+2067) / FSI (U+2068) для варьирования направления / обхода LRI-only фильтра
  A2: percent-кодирование "%E2%81%A6" для проскальзывания мимо raw-byte скана
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: пробел legacy-фильтра (изолят переживает 202A-202E-only стрип)
  B2: реордер кода в скоупе safe=true <LRI> // danger? <PDI>
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "LRI (no PDI)" (SC2) — незавершённое растекание до конца абзаца
  C2: "LRI ... PDF" (SC3) — неверный терминатор
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: LRI подан как безобидный «рекомендованный безопасный» изолят внутри поля кода
  D2: "%E2%81%A6" как «безопасный» кодированный текст с поздним декодированием
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: ограниченный реордер, обманывающий ревьюера
  E2: N/A — вектор: изолят из более нового диапазона, обходящий legacy embedding-only фильтр
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: изолят безопасен, потому что это рекомендованный управляющий
  EXPECTED: FAIL_ISOLATE_MEANS_SAFE_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: невидимый управляющий символ не может быть опасен
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: изолят содержит свой эффект, ничего не утекает
  EXPECTED: FAIL_SCOPE_CONTAINMENT_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%E2%81%A6" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: фильтр embedding/override покрывает и изоляты
  EXPECTED: FAIL_EMBEDDING_ONLY_FILTER_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: наличие изолята доказывает санитизацию ввода
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как смоделировать полный набор Bidi_Control вкл. изоляты (2066-2069) и авто-направление FSI без ложных срабатываний на легитимном ограниченном смешанном тексте?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (стек-проверка, покрывающая embeddings, overrides И изоляты, спаривающая каждый открывающий с правильным терминатором + отвергающая незавершённые/неверный-терминатор — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «изоляты рекомендованы, не иммунны; legacy embedding-only фильтр их пропускает».
ALL_OPEN_QUESTIONS_CLOSED: NO (делегировано, не блокирует)

============================================================
11. PATCH_HISTORY
============================================================
PATCH_HISTORY:
  v0_1_PATCH_01: первичное создание (Ruslan Malyavsky, 2026-07-21) — черновик по шаблону GEN3_v0_3 (Vakhter); не прогнан по конвейеру.
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
  NOT_CONVEYOR_RUN (черновик для нашей работы; конвейер — отдельный проект)
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
