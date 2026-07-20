PRIVATE AUTHORIAL PROJECT / ЧАСТНЫЙ АВТОРСКИЙ ПРОЕКТ · COMMERCIAL USE PROHIBITED

# SIGN CORE CARD — HANGUL-FILLER / INVISIBLE-LETTER CLASS (class card, DRAFT)

DOCUMENT_ID: SIGN_CORE_CARD_HANGUL_FILLER_CLASS_GEN3_v0_1 · DOCUMENT_TYPE: SIGN_CORE_CARD · TEMPLATE_LINE: GEN3_v0_3
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
PRIORITY_TIER: P1 (contour completion) · RAW_PROTOTYPE: `code/range/hangul_filler_cards.py` · HARNESS: `code/range/range_contour_tail.py`
SCOPE: U+115F, U+1160, U+3164, U+FFA0 — default-ignorable Hangul fillers (category Lo). Part of the assigned non-Cf tail of the Default_Ignorable contour, alongside SCRIPT_IGNORABLE and RESERVED_IGNORABLE.

🇬🇧 [English](#english) · 🇷🇺 [Русский](#русский)

---

<a name="english"></a>
## English

DRAFT_NOTE (2026-07-20): the CLASS card for the Hangul fillers — invisible signs whose trap is their **category**: they are **Lo (Letter, other)** — real letters — yet default-ignorable, so they render to nothing. A cleanup that strips format (Cf) and marks (Mn) never touches them, because they are neither. U+3164 HANGUL FILLER is the classic blank-username / blank-nickname spoof (a "name" that looks empty but is a real character); the choseong/jungseong fillers pad incomplete Korean syllable blocks. Governing law: **HANGUL_FILLER ≠ EMPTY** — a filler inside real Hangul composition is legitimate, a filler standing as a blank identifier or padding a non-Korean token is a spoof. WORKING_DRAFT, NON-CONVEYOR.

**0. UNIVERSALITY.** BOUND_TO_SPECIFIC_SIGN: CLASS (Hangul fillers, category Lo, default-ignorable) · AFTER_USE_RESIDUE: FORBIDDEN · SIGN_DATA_IS_SESSION_ONLY: YES

**1. COMMON_CONVEYOR_DISCIPLINE.** v0_3 · RUN_CARD_REQUIRED_BEFORE_LOCK: YES · MODEL_FAMILY_DIVERSITY_REQUIRED: YES · ADVERSARIAL_EVIDENCE_REQUIRED: YES · MUTATION_CHECK_REQUIRED: YES · LIMITATION_STATEMENT_REQUIRED: YES. TRACKER: WORKING_DRAFT YES; PREFLIGHT PENDING; CONVEYOR_REVIEW PENDING; WORKINGLY_CLOSED NO.

**2. META.** ZONE: ZONE_1. WHY_THIS_SIGN_MATTERS: an invisible LETTER is more dangerous than an invisible format char in one way — it survives filters that reason "letters are safe content, format is suspect". U+3164 has a long history in game/chat platforms as a blank name and in username/domain spoofing (an "empty" account, a duplicate-looking handle). The choseong (U+115F) and jungseong (U+1160) fillers are legitimate placeholders for incomplete syllable blocks in Korean input, and U+FFA0 is their halfwidth form (Unicode UAX #44 category Lo; Default_Ignorable_Code_Point=Yes). INTERACTS_WITH: INVISIBLE_CLASS (adjacent invisible axis, but Cf vs. Lo), NOTARIUS (a filler shifts the codepoint count while the visible length looks unchanged), CANONICALIZATION_PRE_PASS (a filler can arrive as `&#12644;` and must be decoded first).

**3. REQUIRED_GENERAL_GUARDS.** RAW_SIGN_INPUT_STATUS: DATA_ONLY · NO_EXECUTION_FROM_SIGN: YES · NO_TRUST_FROM_SIGN: YES · DECODE_BEFORE_TRUST: YES · JUDGE_IN_CONTEXT_NOT_ON_PRESENCE: YES · NEVER_BLIND_STRIP: YES (a filler carries real structure inside Korean composition) · TREAT_INVISIBLE_LETTER_AS_LETTER-AND-INVISIBLE: YES.

**4. SIGN IDENTITY — LAYER_A (LOCK: PERMANENT).** BASE_MODE: DATA_ONLY_INVISIBLE_LETTER · BASE_MODE_FORMULA: FILLER_FORM ≠ EFFECT ; FILLER ≠ EMPTY ; BLANK_LOOK ≠ BLANK_STRING.

| Codepoint | Name | Cat | Priority | Attack mechanism | Legitimate use (do NOT blind-strip) |
|---|---|---|---|---|---|
| U+3164 | HANGUL FILLER | Lo | HIGH | blank / empty-looking username, handle spoof, empty-field bypass | placeholder in Korean layout |
| U+115F | HANGUL CHOSEONG FILLER | Lo | MED | invisible padding / token split | placeholder for a missing leading consonant |
| U+1160 | HANGUL JUNGSEONG FILLER | Lo | MED | invisible padding / token split | placeholder for a missing medial vowel |
| U+FFA0 | HALFWIDTH HANGUL FILLER | Lo | MED | halfwidth blank spoof | halfwidth placeholder |

WHAT_THIS_SIGN_IS_NOT: (1) NOT_A_FORMAT_CHAR — it is a LETTER (Lo); a Cf/Mn filter never sees it; (2) NOT_AN_EMPTY_STRING — it looks blank but is a real code point; (3) NOT_STRIPPABLE — deleting a filler corrupts real Korean composition; (4) NOT_FINAL_SURFACE — may arrive entity/percent-encoded and must be decoded first.
BASE_FORMULAS: FILLER ≠ EMPTY ; IN_HANGUL_COMPOSITION = OK ; BLANK_IDENTIFIER or ASCII_PADDING = SPOOF.

**5. SEMANTIC_EPOCH_TRACKER (LOCK: REVIEWABLE).** EPOCH_TRACKER: U+3164's meaning drifted from "typographic placeholder" to "de-facto blank-name character" as online identity systems spread — the codepoint didn't change, the abuse surface did. NOTE: TYPOGRAPHIC_ORIGIN ≠ TYPOGRAPHIC_USE_TODAY.

**6. EFFECT_FIELDS — LAYER_C (LOCK: SESSION).** authority / trust / verification / proof / execution / permission / status / role_assignment / runtime / existence effect: all NONE. EFFECT_FIELDS_ALL_NONE: YES · CLOSED_SCHEMA: YES.

**7. SAFE / RISK / GUARDS — LAYER_B (LOCK: REVIEWABLE).**
Three-way: **ALARM** on a blank/padding spoof, **OK** on real composition, **WATCH** on an unexplained filler.
- ALARM (conclusive): the whole (trimmed) string is nothing but fillers (blank identifier); a filler padding/splitting a non-Korean ASCII token (`admin‹FILLER› login`).
- OK (clean, "composition" vouch): every filler is flanked by Hangul jamo / syllables (real incomplete-block composition).
- WATCH: a filler present without composition context and without a proven spoof — held, not stripped.
SAFE_CASES (must stay OK): Korean text using choseong/jungseong fillers in composition; ordinary Hangul with a filler between jamo.
RISK_CASES: a username that is only U+3164 (blank) ALARM; `admin‹FILLER›` (padding) ALARM; a lone filler in Latin prose WATCH.
GUARD_PRINCIPLE: an invisible-LOOKING letter is judged on codepoint + context, never on rendered width; composition vouches OK; blank-only or ASCII-padding is a spoof; never auto-strip a filler inside Korean text.

**8. ADVERSARIAL_COVERAGE — RUN_CARD SEED.** blank-only identifier; filler between ASCII letters; filler prefixing/suffixing a handle; filler between Hangul (must stay OK); every case ALSO delivered entity/percent-encoded (pre-pass path). MODEL_FAMILY_DIVERSITY_REQUIRED: YES.

**9. MUTATION_CHECK.** literal filler ↔ `&#N;` ↔ `%XX` byte form; single vs. repeated; blank-only vs. embedded. INVARIANT: after canonicalization one verdict; a composition case stays OK, a blank/padding case stays ALARM across all forms.

**10. KNOWN_OPEN_QUESTIONS.** Q1: a fuller Korean-composition model (a filler is legit only in a well-formed incomplete syllable block, not merely next to one jamo). Q2: identity-field policy — a filler anywhere in a username/handle is higher-risk than in free prose; the verdict could carry the field context. Q3: combine with the length-witness so a filler-padded string is also caught by the visible-vs-codepoint length gap.

**11. PATCH_HISTORY.** v0_1 (2026-07-20): first draft of the Hangul-filler CLASS card (invisible-letter axis, Lo), paired with `hangul_filler_cards.py`. Not conveyor-run.

**12. LIMITATION_STATEMENT.** (1) WORKING_DRAFT / NOT_CONVEYOR_RUN. (2) The composition vouch checks for adjacent Hangul, not a well-formed syllable block (Q1). (3) No identity-field awareness yet (Q2). (4) Entity/percent-delivered fillers are caught only WITH the pre-pass in front. (5) Not a Korean-language-intent detector.

**13. INTEGRATION_INTERFACE_STATUS.** INTEGRATION_STATUS: PROTOTYPED (raw). RAW_PROTOTYPE: `hangul_filler_cards.py::hangul_filler_cards_reader(text) -> Finding`. HARNESS: `range_contour_tail.py`. LIVE RESULT (real MSL + all 6 invisible axes as baseline, shared with the other two tail cards): **tail threats 0/6 → 6/6, legit in-script 4/4 kept, 0 new FP** — the blank-username and ASCII-padding spoofs move to ALARM while Hangul composition stays OK. REQUIRES for closing: composition model (Q1); identity-field policy (Q2); pre-pass in front; conveyor review.

> HOW THE RAW PROTOTYPE WORKS: `MSL_MIP_HOME=/path/to/msl_mip python code/range/range_contour_tail.py` runs this card with the other two tail cards, scanning filler spoofs and legit Hangul composition BEFORE (MSL + all invisible axes) and AFTER (+ the tail), printing the before/after verdict per case plus totals.

---

<a name="русский"></a>
## Русский

DRAFT_NOTE (2026-07-20): КЛАССОВАЯ карточка филлеров хангыля — невидимых знаков, чья ловушка в их **категории**: это **Lo (Letter, other)** — настоящие буквы — но default-ignorable, поэтому рисуются в ничто. Очистка, вырезающая формат (Cf) и марки (Mn), их не трогает, ведь они ни то ни другое. U+3164 HANGUL FILLER — классический спуф пустого имени / ника («имя», выглядящее пустым, но реальный знак); филлеры чосон/чунсон дополняют неполные корейские слоговые блоки. Управляющий закон: **HANGUL_FILLER ≠ ПУСТО** — филлер внутри настоящей композиции хангыля легитимен, филлер как пустой идентификатор или набивка не-корейского токена это спуф. WORKING_DRAFT, БЕЗКОНВЕЙЕРНО.

**0. UNIVERSALITY.** BOUND_TO_SPECIFIC_SIGN: CLASS (филлеры хангыля, категория Lo, default-ignorable) · AFTER_USE_RESIDUE: FORBIDDEN · SIGN_DATA_IS_SESSION_ONLY: YES

**1. COMMON_CONVEYOR_DISCIPLINE.** v0_3 · RUN_CARD_REQUIRED_BEFORE_LOCK: YES · MODEL_FAMILY_DIVERSITY_REQUIRED: YES · ADVERSARIAL_EVIDENCE_REQUIRED: YES · MUTATION_CHECK_REQUIRED: YES · LIMITATION_STATEMENT_REQUIRED: YES. TRACKER: WORKING_DRAFT YES; PREFLIGHT PENDING; CONVEYOR_REVIEW PENDING; WORKINGLY_CLOSED NO.

**2. META.** ZONE: ZONE_1. WHY_THIS_SIGN_MATTERS: невидимая БУКВА опаснее невидимого форматного знака в одном: она переживает фильтры, рассуждающие «буквы это безопасный контент, формат подозрителен». У U+3164 долгая история в игровых/чат-платформах как пустое имя и в спуфе имён/доменов (пустой аккаунт, похожий-дубликат-хэндл). Филлеры чосон (U+115F) и чунсон (U+1160) — легит-заполнители для неполных слоговых блоков в корейском вводе, а U+FFA0 — их полуширинная форма (Unicode UAX #44 категория Lo; Default_Ignorable_Code_Point=Yes). INTERACTS_WITH: INVISIBLE_CLASS (смежная невидимая ось, но Cf vs. Lo), NOTARIUS (филлер сдвигает счётчик кодпоинтов при неизменной видимой длине), CANONICALIZATION_PRE_PASS (филлер может прийти как `&#12644;`, сперва декод).

**3. REQUIRED_GENERAL_GUARDS.** RAW_SIGN_INPUT_STATUS: DATA_ONLY · NO_EXECUTION_FROM_SIGN: YES · NO_TRUST_FROM_SIGN: YES · DECODE_BEFORE_TRUST: YES · JUDGE_IN_CONTEXT_NOT_ON_PRESENCE: YES · NEVER_BLIND_STRIP: YES (филлер несёт настоящую структуру внутри корейской композиции) · TREAT_INVISIBLE_LETTER_AS_LETTER-AND-INVISIBLE: YES.

**4. SIGN IDENTITY — LAYER_A (LOCK: PERMANENT).** BASE_MODE: DATA_ONLY_INVISIBLE_LETTER · BASE_MODE_FORMULA: FILLER_FORM ≠ EFFECT ; FILLER ≠ ПУСТО ; ПУСТОЙ_ВИД ≠ ПУСТАЯ_СТРОКА.

| Кодпоинт | Имя | Кат | Приоритет | Механизм атаки | Легит-применение (НЕ вырезать слепо) |
|---|---|---|---|---|---|
| U+3164 | HANGUL FILLER | Lo | ВЫСОКИЙ | пустое/пусто-выглядящее имя, спуф хэндла, обход «поле пусто» | заполнитель в корейской раскладке |
| U+115F | HANGUL CHOSEONG FILLER | Lo | СРЕД. | невидимая набивка / разрыв токена | заполнитель отсутствующей начальной согласной |
| U+1160 | HANGUL JUNGSEONG FILLER | Lo | СРЕД. | невидимая набивка / разрыв токена | заполнитель отсутствующей срединной гласной |
| U+FFA0 | HALFWIDTH HANGUL FILLER | Lo | СРЕД. | полуширинный пустой спуф | полуширинный заполнитель |

WHAT_THIS_SIGN_IS_NOT: (1) NOT_A_FORMAT_CHAR — это БУКВА (Lo); Cf/Mn-фильтр её не видит; (2) NOT_AN_EMPTY_STRING — выглядит пусто, но реальный кодпоинт; (3) NOT_STRIPPABLE — удаление филлера портит настоящую корейскую композицию; (4) NOT_FINAL_SURFACE — может прийти entity/percent-кодированным, сперва декод.
BASE_FORMULAS: FILLER ≠ ПУСТО ; В_КОМПОЗИЦИИ_ХАНГЫЛЯ = OK ; ПУСТОЙ_ИДЕНТИФИКАТОР или ASCII_НАБИВКА = СПУФ.

**5. SEMANTIC_EPOCH_TRACKER (LOCK: REVIEWABLE).** EPOCH_TRACKER: смысл U+3164 сместился от «типографический заполнитель» к «де-факто знак пустого имени» с распространением онлайн-систем идентичности — кодпоинт не менялся, менялась поверхность злоупотребления. NOTE: ТИПОГРАФИЧЕСКОЕ_ПРОИСХОЖДЕНИЕ ≠ ТИПОГРАФИЧЕСКОЕ_ПРИМЕНЕНИЕ_СЕГОДНЯ.

**6. EFFECT_FIELDS — LAYER_C (LOCK: SESSION).** authority / trust / verification / proof / execution / permission / status / role_assignment / runtime / existence effect: всё NONE. EFFECT_FIELDS_ALL_NONE: YES · CLOSED_SCHEMA: YES.

**7. SAFE / RISK / GUARDS — LAYER_B (LOCK: REVIEWABLE).**
Трёхстороннее: **ALARM** на пустом/набивочном спуфе, **OK** на настоящей композиции, **WATCH** на необъяснённом филлере.
- ALARM (conclusive): вся (обрезанная) строка это только филлеры (пустой идентификатор); филлер, набивающий/рвущий не-корейский ASCII-токен (`admin‹FILLER› login`).
- OK (чистое, вауч «композиция»): каждый филлер обрамлён хангыль-джамо / слогами (настоящая композиция неполного блока).
- WATCH: филлер без контекста композиции и без доказанного спуфа — держим, не вырезаем.
SAFE_CASES (должны остаться OK): корейский текст с филлерами чосон/чунсон в композиции; обычный хангыль с филлером между джамо.
RISK_CASES: имя пользователя, состоящее только из U+3164 (пусто) ALARM; `admin‹FILLER›` (набивка) ALARM; одиночный филлер в латинской прозе WATCH.
GUARD_PRINCIPLE: невидимо-ВЫГЛЯДЯЩАЯ буква судится по кодпоинту + контексту, никогда по видимой ширине; композиция вауч OK; только-пусто или ASCII-набивка это спуф; никогда не авто-вырезать филлер внутри корейского текста.

**8. ADVERSARIAL_COVERAGE — RUN_CARD SEED.** только-пустой идентификатор; филлер между ASCII-буквами; филлер в начале/конце хэндла; филлер между хангыль (должно остаться OK); каждый кейс ТАКЖЕ доставлен entity/percent-кодированным (путь pre-pass). MODEL_FAMILY_DIVERSITY_REQUIRED: YES.

**9. MUTATION_CHECK.** литеральный филлер ↔ `&#N;` ↔ байтовая форма `%XX`; одиночный vs. повторённый; только-пусто vs. встроенный. INVARIANT: после канонизации один вердикт; кейс композиции остаётся OK, пустой/набивочный остаётся ALARM во всех формах.

**10. KNOWN_OPEN_QUESTIONS.** Q1: более полная модель корейской композиции (филлер легитимен лишь в корректном неполном слоговом блоке, не просто рядом с одним джамо). Q2: политика поля идентичности — филлер где угодно в имени/хэндле рискованнее, чем в свободной прозе; вердикт мог бы нести контекст поля. Q3: совместить с уликой-длины, чтобы строка с набивкой-филлером ловилась ещё и зазором видимая-vs-кодпоинтная длина.

**11. PATCH_HISTORY.** v0_1 (2026-07-20): первый черновик КЛАССОВОЙ карточки филлеров хангыля (ось невидимой буквы, Lo), в паре с `hangul_filler_cards.py`. Не прогонялся через конвейер.

**12. LIMITATION_STATEMENT.** (1) WORKING_DRAFT / NOT_CONVEYOR_RUN. (2) Вауч композиции проверяет соседний хангыль, не корректный слоговой блок (Q1). (3) Осознания поля идентичности пока нет (Q2). (4) Entity/percent-доставленные филлеры ловятся только С pre-pass впереди. (5) Не детектор корейского языкового смысла.

**13. INTEGRATION_INTERFACE_STATUS.** INTEGRATION_STATUS: PROTOTYPED (сырой). RAW_PROTOTYPE: `hangul_filler_cards.py::hangul_filler_cards_reader(text) -> Finding`. HARNESS: `range_contour_tail.py`. ЖИВОЙ РЕЗУЛЬТАТ (настоящий MSL + все 6 невидимых осей как база, общая с двумя другими хвостовыми карточками): **хвостовые угрозы 0/6 → 6/6, легит в-скрипте 4/4, 0 новых FP** — спуфы пустого имени и ASCII-набивки переходят в ALARM, а композиция хангыля остаётся OK. ТРЕБУЕТСЯ для закрытия: модель композиции (Q1); политика поля идентичности (Q2); pre-pass впереди; конвейер-ревью.

> КАК РАБОТАЕТ СЫРОЙ ПРОТОТИП: `MSL_MIP_HOME=/path/to/msl_mip python code/range/range_contour_tail.py` прогоняет эту карточку с двумя другими хвостовыми, сканируя спуфы филлеров и легит-композицию хангыля BEFORE (MSL + все невидимые оси) и AFTER (+ хвост), печатая вердикт до/после по кейсу и итоги.
