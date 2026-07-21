PRIVATE AUTHORED PROJECT / COMMERCIAL USE PROHIBITED

DOCUMENT_ID: SIGN_CORE_CARD_CARRIAGE_RETURN_U000D_GEN3_v0_3_RU
DOCUMENT_TYPE: SIGN_CORE_CARD
TEMPLATE_LINE: GEN3_v0_3
DOCUMENT_STATUS: WORKING_DRAFT
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
SOURCE_TEMPLATE: SIGN_CORE_CARD_TEMPLATE_GEN3_v0_3_EN
BASED_ON_RULESET: SIGN_CORE_CARD_CONVEYOR_RULES_GEN3_v0_3_EN
TRANSLATION_NOTE: Русский оригинал (authoritative). Английское зеркало — SIGN_CORE_CARD_CARRIAGE_RETURN_U000D_GEN3_v0_3_EN. Кодпоинты, имена полей и формулы идентичны. ЧЕРНОВИК для нашей работы (Vakhter); конвейер — отдельный проект.

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
CARD_UID: SIGN_CORE_CARD_CARRIAGE_RETURN_U000D_GEN3_v0_3_RU
CODEPOINT: U+000D
VISIBLE_FORM: ␍
UNICODE_NAME: <control> CARRIAGE RETURN (CR)
ZONE: ZONE_1
DOCUMENT_STATUS: WORKING_DRAFT
TEMPLATE_LINE: GEN3_v0_3
AUTHOR: Ruslan Malyavsky
CREATED_AT: 2026-07-21
VERSION: v0_1
AUTHOR_DECISION_REFERENCE: PENDING
RUN_CARD_REFERENCE: PENDING
RUN_CARD_STATUS: NOT_STARTED
DISPLAY_NAME: возврат каретки / CR (непечатаемый)
CATEGORY_ROADMAP: INJ (CRLF/инъекция заголовков, подделка логов) · PHAGO: — (подделка границы записи)
GLYPH_NOTE: VISIBLE_FORM использует ␍ (U+240D SYMBOL FOR CARRIAGE RETURN) как печатаемую картинку; сам знак (U+000D) — непечатаемый управляющий символ.

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
VISIBLE_FORM: ␍
LOOKS_SIMILAR_IS_NOT_SAME_SIGN: YES
RAW_SIGN_INPUT_STATUS: DATA_ONLY
BASE_MODE: DATA_ONLY_DELIMITER
BASE_MODE_FORMULA: CARRIAGE_RETURN_FORM ≠ EFFECT
SIGN_CATEGORY:
  - терминатор строки (половина CRLF) в сетевых протоколах
  - компонент новой строки в legacy Mac / Windows
  - управление возвратом курсора в терминалах
  - граница записи/поля в некоторых форматах

WHAT_THIS_SIGN_IS_NOT:
  1. NOT_NEWLINE_ONLY — CR не всегда «просто новая строка» (в заголовке он завершает/внедряет строку)
  2. NOT_BOUNDARY_SAFE — граница строки позволяет атакующему подделать новый заголовок/запись
  3. NOT_INVISIBLE_MEANS_HARMLESS — то, что он непечатаемый, не делает его инертным
  4. NOT_ESCAPED_PROOF — показанный "\r" не доказывает, что реальный CR нейтрализован
  5. NOT_ENCODED_SAFE — "%0D" / "\r" могут быть раскодированы обратно в CR позже
  6. NOT_AUTHORITY — CR не подтверждает официальность
  7. NOT_EXECUTION_TRIGGER — сам по себе ничего не исполняет; расщепление делает контекст
  8. NOT_TRUST_SIGNAL — не повышает доверие
  9. NOT_HEADER_SAFE — CR (или CRLF) в заголовке включает расщепление ответа/лога
  10. NOT_LF_STRIPPED_SAFE — вырезание только LF оставляет одиночный CR, соблюдаемый частью парсеров
  11. NOT_SANITIZED_PROOF — наличие CR не значит, что ввод санитизирован

BASE_FORMULAS:
  CARRIAGE_RETURN_FORM ≠ EFFECT
  CARRIAGE_RETURN_FORM ≠ NEWLINE_ONLY_PROOF
  CARRIAGE_RETURN_FORM ≠ BOUNDARY_SAFETY_PROOF
  CARRIAGE_RETURN_FORM ≠ INVISIBLE_HARMLESS_PROOF
  CARRIAGE_RETURN_FORM ≠ ESCAPED_PROOF
  CARRIAGE_RETURN_FORM ≠ ENCODED_SAFETY_PROOF
  CARRIAGE_RETURN_FORM ≠ AUTHORITY
  CARRIAGE_RETURN_FORM ≠ EXECUTION_TRIGGER
  CARRIAGE_RETURN_FORM ≠ HEADER_SAFETY_PROOF
  CARRIAGE_RETURN_FORM ≠ LF_STRIP_SAFETY_PROOF
  CARRIAGE_RETURN_FORM ≠ SANITIZED_PROOF

============================================================
5. SEMANTIC_EPOCH_TRACKER
SEMANTIC_EPOCH_TRACKER_LOCK: REVIEWABLE
============================================================
EPOCH_TRACKER: NOT_APPLICABLE
NOTE: CR (ZONE_1) имеет параллельные функции (половина CRLF, legacy-новая строка, возврат курсора), сосуществующие без культурной прецессии. Полисемия стабильного управляющего кода.
LAYER_ANOMALY:
  ABSENT_PHYSICAL_LAYER: YES, уровень L1
  NOTE: управляющий код печатной машинки/телетайпа без жестового предшественника; функции границы протокола надстроены цифровой эпохой параллельно.

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
    INPUT: "line one\\r\\nline two"
    CONTEXT: CRLF, показанный как escape в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: CARRIAGE_RETURN_FORM ≠ NEWLINE_ONLY_PROOF
  SAFE_CASE_002:
    INPUT: "use \\r\\n on Windows"
    CONTEXT: описание соглашения о новой строке в тексте
    EXPECTED: INFO
    RISK: NONE
    GUARD: CARRIAGE_RETURN_FORM ≠ EFFECT
  SAFE_CASE_003:
    INPUT: "the \\r escape returns the cursor"
    CONTEXT: escape внутри документации (как литеральный текст)
    EXPECTED: INFO
    RISK: NONE
    GUARD: CARRIAGE_RETURN_FORM ≠ EFFECT
  SAFE_CASE_004:
    INPUT: "CR is 0x0D in ASCII"
    CONTEXT: название управляющего кода в документации
    EXPECTED: INFO
    RISK: NONE
    GUARD: CARRIAGE_RETURN_FORM ≠ NEWLINE_ONLY_PROOF
  SAFE_CASE_005:
    INPUT: "progress bar uses \\r to redraw"
    CONTEXT: описание поведения возврата курсора в терминале
    EXPECTED: INFO
    RISK: NONE
    GUARD: CARRIAGE_RETURN_FORM ≠ EFFECT
  SAFE_CASE_006:
    INPUT: "a properly stored multi-line comment"
    CONTEXT: легитимный многострочный свободный текст в хранимом поле
    EXPECTED: INFO
    RISK: NONE
    GUARD: CARRIAGE_RETURN_FORM ≠ BOUNDARY_SAFETY_PROOF

RISK_CASES:
  RISK_CASE_001:
    NAME: HTTP_RESPONSE_SPLITTING
    INPUT: "value%0D%0ASet-Cookie:%20admin=1"
    CONTEXT: внедрённый CRLF, начинающий поддельный заголовок HTTP
    RISK: CRITICAL
    ATTACK: "%0D%0A" декодируется в CRLF и внедряет подконтрольный атакующему заголовок/тело
    GUARD: CARRIAGE_RETURN_FORM ≠ HEADER_SAFETY_PROOF
  RISK_CASE_002:
    NAME: LONE_CR_HEADER_SPLIT
    INPUT: "value%0DSet-Cookie:%20admin=1"
    CONTEXT: одиночный CR, трактуемый как перенос снисходительным парсером
    RISK: HIGH
    ATTACK: фильтр вырезал только LF; парсер всё равно расщепляет по одиночному CR
    GUARD: CARRIAGE_RETURN_FORM ≠ LF_STRIP_SAFETY_PROOF
  RISK_CASE_003:
    NAME: LOG_FORGING
    INPUT: "user%0D%0A2026-01-01 ADMIN login OK"
    CONTEXT: внедрённый CRLF, подделывающий фальшивую строку лога
    RISK: HIGH
    ATTACK: CRLF начинает новую запись лога, полностью подконтрольную атакующему
    GUARD: CARRIAGE_RETURN_FORM ≠ BOUNDARY_SAFETY_PROOF
  RISK_CASE_004:
    NAME: SMTP_HEADER_INJECTION
    INPUT: "addr@x.com%0D%0ABcc:%20victim@y.com"
    CONTEXT: внедрённый CRLF, добавляющий заголовок письма
    RISK: HIGH
    ATTACK: CRLF внедряет лишний заголовок SMTP (Bcc) в поле отправки почты
    GUARD: CARRIAGE_RETURN_FORM ≠ HEADER_SAFETY_PROOF
  RISK_CASE_005:
    NAME: ENCODED_CR_BYPASS
    INPUT: "value\\u000dInjected (с поздним декодированием)"
    CONTEXT: \\u000d декодируется обратно в CR перед приёмником
    RISK: HIGH
    ATTACK: кодированный CR декодируется ПОСЛЕ проверки → инъекция строки
    GUARD: CARRIAGE_RETURN_FORM ≠ ENCODED_SAFETY_PROOF
  RISK_CASE_006:
    NAME: LOG_OVERWRITE_ILLUSION
    INPUT: "real entry%0DFAKE entry"
    CONTEXT: CR перерисовывает строку лога в терминале, скрывая настоящую
    RISK: MEDIUM
    ATTACK: CR возвращает курсор, так что в консоли виден только поддельный текст
    GUARD: CARRIAGE_RETURN_FORM ≠ EFFECT

CONFUSABLES:
  CONFUSABLE_001:
    VISIBLE_FORM: ␊
    CODEPOINT: U+000A
    NAME: LINE FEED
    RISK: HIGH
    RULE: LINE_FEED ≠ CARRIAGE_RETURN (LF отдельно или CRLF тоже может расщепить строку)
  CONFUSABLE_002:
    VISIBLE_FORM: ⟨NEL⟩
    CODEPOINT: U+0085
    NAME: NEXT LINE
    RISK: MEDIUM
    RULE: NEXT_LINE ≠ CARRIAGE_RETURN (NEL — перенос строки C1, соблюдаемый некоторыми парсерами)
  CONFUSABLE_003:
    VISIBLE_FORM: ⟨LSEP⟩
    CODEPOINT: U+2028
    NAME: LINE SEPARATOR
    RISK: MEDIUM
    RULE: LINE_SEPARATOR ≠ CARRIAGE_RETURN (перенос в JS/некоторых парсерах, невидим для фильтра CR)
  CONFUSABLE_004:
    VISIBLE_FORM: ⟨PSEP⟩
    CODEPOINT: U+2029
    NAME: PARAGRAPH SEPARATOR
    RISK: MEDIUM
    RULE: PARAGRAPH_SEPARATOR ≠ CARRIAGE_RETURN
  CONFUSABLE_005:
    VISIBLE_FORM: ␌
    CODEPOINT: U+000C
    NAME: FORM FEED
    RISK: LOW
    RULE: FORM_FEED ≠ CARRIAGE_RETURN (FF — разрыв страницы/строки, трактуемый частью инструментов как пробел)

CONTRADICTION_GUARDS:
  CG1:
    TRIGGER: "CR — это всегда просто новая строка"
    RESPONSE: CARRIAGE_RETURN_FORM ≠ NEWLINE_ONLY_PROOF
    RULE: в заголовке/логе/протоколе CR завершает строку и может внедрить новую
  CG2:
    TRIGGER: "невидимый управляющий символ не может быть опасен"
    RESPONSE: CARRIAGE_RETURN_FORM ≠ INVISIBLE_HARMLESS_PROOF
    RULE: невидимость ортогональна эффекту; CR управляет границами строки
  CG3:
    TRIGGER: "вырезать LF достаточно, чтобы остановить инъекцию строки"
    RESPONSE: CARRIAGE_RETURN_FORM ≠ LF_STRIP_SAFETY_PROOF
    RULE: одиночный CR всё ещё соблюдается как перенос многими снисходительными парсерами
  CG4:
    TRIGGER: "'%0D' / '\\r' безопасен навсегда"
    RESPONSE: CARRIAGE_RETURN_FORM ≠ ENCODED_SAFETY_PROOF
    RULE: кодированная форма может быть декодирована обратно в CR перед приёмником
  CG5:
    TRIGGER: "фильтр CR ловит все переносы строк"
    RESPONSE: CARRIAGE_RETURN_FORM ≠ EFFECT
    RULE: LF (U+000A), NEL (U+0085), U+2028/U+2029 тоже переносят строку в некоторых парсерах
  CG6:
    TRIGGER: "наличие CR значит, что ввод санитизирован"
    RESPONSE: CARRIAGE_RETURN_FORM ≠ SANITIZED_PROOF
    RULE: наличие знака ничего не говорит о санитизации

SEQUENCE_LAYER_BOUNDARY:
  SIGN_SAFE_ALONE ≠ SIGN_SAFE_IN_SEQUENCE: YES
  SEQUENCE_CANDIDATES:
    SC1:
      SEQUENCE: "CR+LF"
      NAME: CRLF_HEADER_TERMINATOR
      RISK_LEVEL: CRITICAL
      POSSIBLE_CONTEXTS: пара CRLF, завершающая и внедряющая заголовки HTTP
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC2:
      SEQUENCE: "CRLF+CRLF"
      NAME: HEADER_BODY_SPLIT
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: пустая строка, завершающая заголовки и начинающая внедрённое тело
      REQUIRES_SEQUENCE_INTEGRATOR: YES
    SC3:
      SEQUENCE: "lone CR"
      NAME: LF_STRIP_BYPASS
      RISK_LEVEL: HIGH
      POSSIBLE_CONTEXTS: одиночный CR, переживающий LF-only фильтр и всё ещё расщепляющий
      REQUIRES_SEQUENCE_INTEGRATOR: YES
  IF NOT_APPLICABLE: неприменимо — последовательности с CR центральны для CRLF/инъекции заголовков/логов.

PHAGO_ENTITY_MIMICRY:
  NOT_APPLICABLE:
    REASON: CR подделывает ГРАНИЦУ записи/строки, но не имитирует существование верифицированной сущности. Его риски — расщепление/подделка, а не мимикрия сущности.
    REVIEW_REQUIRED: YES

============================================================
8. ADVERSARIAL_COVERAGE — RUN_CARD SEED
============================================================
MIN_TOTAL_VECTORS: 10 (5 категорий A-E, CATEGORY_F NOT_APPLICABLE для ZONE_1)
CATEGORY_A: FORM_MANIPULATION (2)
  A1: замена CR на одиночный LF (U+000A) для переживания CR-only фильтра
  A2: замена на NEL (U+0085) как перенос строки C1
CATEGORY_B: CONTEXT_INJECTION (2)
  B1: расщепление ответа HTTP value%0D%0ASet-Cookie:%20admin=1
  B2: расщепление заголовка одиночным CR value%0DSet-Cookie:%20admin=1
CATEGORY_C: SEQUENCE_MANIPULATION (2)
  C1: "CR+LF" (SC1) — инъекция терминатора заголовка HTTP
  C2: "lone CR" (SC3) — обход LF-фильтра
CATEGORY_D: SEMANTIC_MIMICRY (2)
  D1: CR подан как безобидная новая строка внутри поля заголовка
  D2: "%0D" как «безопасный» кодированный текст с поздним декодированием
CATEGORY_E: PHAGO_ENTITY_MIMICRY (2)
  E1: N/A — знак не PHAGO-носитель; вектор: инъекция поддельного заголовка в ответ
  E2: N/A — вектор: инъекция поддельной строки лога через CRLF в конвейер логов
CATEGORY_F: SEMANTIC_LAYER_MANIPULATION
  NOT_APPLICABLE
  REASON: ZONE_1, у знака нет спящих/активных эпох.
ACTUAL_TOTAL_VECTORS: 10
COVERAGE_STATUS: SUFFICIENT (10 ≥ 10)

============================================================
9. MUTATION_CHECK
============================================================
MUTATION_01:
  CLAIM: CR — всегда просто новая строка
  EXPECTED: FAIL_NEWLINE_ONLY_MIMICRY
  RESULT: FAIL
MUTATION_02:
  CLAIM: невидимый управляющий символ не может быть опасен
  EXPECTED: FAIL_INVISIBLE_HARMLESS_MIMICRY
  RESULT: FAIL
MUTATION_03:
  CLAIM: вырезать LF достаточно, чтобы остановить инъекцию строки
  EXPECTED: FAIL_LF_STRIP_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_04:
  CLAIM: "%0D" / "\r" безопасен навсегда
  EXPECTED: FAIL_ENCODED_SAFETY_MIMICRY
  RESULT: FAIL
MUTATION_05:
  CLAIM: фильтр CR ловит все переносы строк
  EXPECTED: FAIL_CONFUSABLE_COVERAGE_MIMICRY
  RESULT: FAIL
MUTATION_06:
  CLAIM: наличие CR доказывает санитизацию ввода
  EXPECTED: FAIL_SANITIZED_MIMICRY
  RESULT: FAIL

============================================================
10. KNOWN_OPEN_QUESTIONS
============================================================
OQ1:
  QUESTION: как вырезать/нормализовать И CR, И LF (и NEL/LSEP) по протоколу без ложных срабатываний на легитимных многострочных текстовых полях?
  STATUS: CLOSED_AS_DELEGATED_TO_INTEGRATOR (вырезание полного набора переносов строк из значений заголовков + структурированное логирование + протоколо-зависимое кодирование — забота интегратора/рантайма)
  BLOCKS_WORKINGLY_CLOSED: NO
  NOTE: карточка фиксирует правило «вырезать один LF недостаточно; одиночный CR всё ещё расщепляет».
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
