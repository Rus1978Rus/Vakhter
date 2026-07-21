PRIVATE AUTHORIAL PROJECT / ЧАСТНЫЙ АВТОРСКИЙ ПРОЕКТ · COMMERCIAL USE PROHIBITED

# SIGN CORE CARD — CONFUSABLE / HOMOGLYPH CLASS (class card, DRAFT)

DOCUMENT_ID: SIGN_CORE_CARD_CONFUSABLE_CLASS_GEN3_v0_1 · DOCUMENT_TYPE: SIGN_CORE_CARD · TEMPLATE_LINE: GEN3_v0_3
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
PRIORITY_TIER: P0 (visible-deception axis) · RAW_PROTOTYPE: `code/range/confusable_cards.py` · HARNESS: `code/range/range_confusable.py`
SCOPE: cross-script look-alike letters — Cyrillic and Greek letters confusable with Latin, plus U+2010 HYPHEN. This is the FIRST visible-deception card; the invisible / default-ignorable contour is a separate family (INVISIBLE / BIDI / TAG / VS / WHITESPACE / MONITORED / PREPENDED).

🇬🇧 [English](#english) · 🇷🇺 [Русский](#русский)

---

<a name="english"></a>
## English

DRAFT_NOTE (2026-07-20): the first CLASS card for the **visible-deception** axis — the danger is a character you CAN see that looks like a different one. Governing law: **LOOKS_SAME ≠ IS_SAME.** `paypal.com` and `pаypal.com` render identically, but the second has a Cyrillic `а` (U+0430) among Latin letters — a mixed-script confusable (the IDN / brand spoof). The structural signal is NOT "a non-Latin letter exists" (that flags all Russian) — it is a SINGLE TOKEN that mixes a base script with look-alike letters of another. A blanket "whole-script, no native anchor" rule was tested and REJECTED (it fired on ~25% of ordinary Russian words); whole-script confusion is judged only against a target. WORKING_DRAFT, NON-CONVEYOR.

**0. UNIVERSALITY.** BOUND_TO_SPECIFIC_SIGN: CLASS (cross-script confusable letters) · AFTER_USE_RESIDUE: FORBIDDEN · SIGN_DATA_IS_SESSION_ONLY: YES

**1. COMMON_CONVEYOR_DISCIPLINE.** v0_3 · RUN_CARD_REQUIRED_BEFORE_LOCK: YES · MODEL_FAMILY_DIVERSITY_REQUIRED: YES · ADVERSARIAL_EVIDENCE_REQUIRED: YES · MUTATION_CHECK_REQUIRED: YES · LIMITATION_STATEMENT_REQUIRED: YES. TRACKER: WORKING_DRAFT YES; PREFLIGHT PENDING; CONVEYOR_REVIEW PENDING; WORKINGLY_CLOSED NO.

**2. META.** ZONE: ZONE_1. WHY_THIS_SIGN_MATTERS: homoglyph spoofing is the backbone of phishing — a domain, brand, or handle rendered with one or two foreign look-alike letters passes the eye and, in an IDN, resolves to an attacker's registration. Unicode UTS #39 defines confusables (a skeleton map) and mixed-script / whole-script confusable detection; the mixed-script case is the low-false-positive workhorse. INTERACTS_WITH: the base MSL reader (already carries a Cyrillic look-alike set — this card consolidates the axis as a class card and EXTENDS it to Greek and to whole-script-on-target), CANONICALIZATION_PRE_PASS (a look-alike can arrive percent/entity-encoded), WHITESPACE_CLASS / METACHAR_CLASS (a confusable next to a domain delimiter compounds the spoof).

**3. REQUIRED_GENERAL_GUARDS.** RAW_SIGN_INPUT_STATUS: DATA_ONLY · NO_EXECUTION_FROM_SIGN: YES · NO_TRUST_FROM_SIGN: YES · DECODE_BEFORE_TRUST: YES · JUDGE_MIX_NOT_MERE_FOREIGNNESS: YES (a foreign letter alone is not a spoof) · NEVER_FLAG_GENUINE_NATIVE_TEXT: YES (real Russian/Greek stays OK).

**4. SIGN IDENTITY — LAYER_A (LOCK: PERMANENT).** BASE_MODE: DATA_ONLY_VISIBLE_LOOKALIKE · BASE_MODE_FORMULA: LOOKS_SAME ≠ IS_SAME ; SPOOF = SCRIPT_MIX_IN_ONE_TOKEN or WHOLE_SCRIPT_ON_TARGET.

| Source | Examples (→ Latin skeleton) | Priority | Attack mechanism | Legitimate use (stays OK) |
|---|---|---|---|---|
| Cyrillic look-alikes | а→a е→e о→o р→p с→c у→y х→x і→i ѕ→s ј→j (and caps А В Е К М Н О Р С Т Х У) | HIGH | mixed into a Latin token — IDN / brand spoof | genuine Russian text (single-script) |
| Greek look-alikes | ο→o α→a ρ→p ν→v ι→i κ→k (and caps Α Β Ε Η Ι Κ Μ Ν Ο Ρ Τ Υ Χ) | HIGH | mixed into a Latin token | genuine Greek text (single-script) |
| U+2010 HYPHEN | ‐ → - | MED | look-alike for ASCII hyphen in a domain | typographic hyphen in prose |

WHAT_THIS_SIGN_IS_NOT: (1) NOT_SPOOF_BY_FOREIGNNESS — a non-Latin letter is only a spoof when MIXED into another script's token; (2) NOT_ABOUT_SINGLE_SCRIPT — genuine Russian/Greek/CJK text is legitimate; (3) NOT_FINAL_SURFACE — a look-alike may arrive percent/entity-encoded and must be decoded first.
BASE_FORMULAS: MIXED_SCRIPT_CONFUSABLE = LATIN + FOREIGN_LOOKALIKE_IN_ONE_TOKEN ; WHOLE_SCRIPT_SPOOF = ALL_FOREIGN ∧ SKELETON ∈ TARGETS ; SKELETON = map each look-alike to its Latin twin.

**5. SEMANTIC_EPOCH_TRACKER (LOCK: REVIEWABLE).** EPOCH_TRACKER: the attack surface grew with IDN (internationalized domain names) and with platforms allowing non-ASCII handles; browsers added punycode / mixed-script display rules in response, but back-end string matching often still compares raw. NOTE: BROWSER_DISPLAY_DEFENSE ≠ BACKEND_DEFENSE.

**6. EFFECT_FIELDS — LAYER_C (LOCK: SESSION).** authority / trust / verification / proof / execution / permission / status / role_assignment / runtime / existence effect: all NONE. EFFECT_FIELDS_ALL_NONE: YES · CLOSED_SCHEMA: YES.

**7. SAFE / RISK / GUARDS — LAYER_B (LOCK: REVIEWABLE).**
Keys on SCRIPT-MIX within one token, plus a target check for the whole-script case:
- ALARM (conclusive): a token mixes Latin with Cyrillic/Greek letters that are Latin confusables (`pаypal`, `gοogle`) — the Latin skeleton is shown; OR a wholly-foreign token whose skeleton equals a known target (`уаһоо` → `yahoo`).
- OK (clean): a single-script token (all Latin, all Cyrillic, all Greek, CJK); a genuine native word; accented Latin.
SAFE_CASES (must stay OK): `paypal.com`; `привет мир как дела` (genuine Russian — incl. words built only from look-alike letters like `соус`, `орех`); `Zürich café résumé`; `日本語 の 文書`.
RISK_CASES: `pаypal.com` (Cyrillic а) ALARM → impersonates `paypal`; `аpple.com` ALARM; `gοogle.com` (Greek ο) ALARM; `micrоsоft` ALARM; `уаһоо.com` (all Cyrillic) ALARM → `yahoo`.
GUARD_PRINCIPLE: fire on the MIX, not on mere foreignness; show the Latin skeleton so the impersonation is legible; keep genuine single-script text OK; judge whole-script only against a target list.

**8. ADVERSARIAL_COVERAGE — RUN_CARD SEED.** Cyrillic and Greek look-alikes in brands/domains/handles; one vs. several substituted letters; leading vs. medial substitution; U+2010 in a hyphenated domain; genuine Russian/Greek/CJK (must stay OK, incl. all-look-alike words); whole-script on and off the target list; every case ALSO percent/entity-encoded (pre-pass path). MODEL_FAMILY_DIVERSITY_REQUIRED: YES.

**9. MUTATION_CHECK.** literal look-alike ↔ `%XX` / `&#N;` ↔ punycode; one substitution vs. many; look-alike at start/middle/end of a token. INVARIANT: after canonicalization one verdict; a mixed-script token stays ALARM, genuine single-script stays OK across all forms.

**10. KNOWN_OPEN_QUESTIONS.** Q1: replace the hand-built Cyrillic/Greek map and DEMO_TARGETS with the full Unicode confusables (UTS #39) skeleton table and a real brand/domain corpus. Q2: more source scripts (Armenian, Latin-Extended look-alikes, fullwidth forms, digit/letter confusables like 0/O 1/l). Q3: numeral confusables (roman numerals U+2160+, superscripts) and the visible-punctuation phishing set (`.` `/` `@` fullwidth forms) — likely their own sibling cards. Q4: a same-skeleton-collision check (two inputs sharing a skeleton) for near-duplicate detection.

**11. PATCH_HISTORY.** v0_1 (2026-07-20): first draft of the confusable/homoglyph CLASS card (visible-deception axis) — mixed-script ALARM + target-gated whole-script, paired with `confusable_cards.py`. The blanket no-anchor WATCH was tested and rejected (Russian false positives). Not conveyor-run.

**12. LIMITATION_STATEMENT.** (1) WORKING_DRAFT / NOT_CONVEYOR_RUN. (2) The confusable map is a hand-built high-value subset (Cyrillic + Greek + U+2010), not the full UTS #39 table (Q1). (3) Whole-script detection is gated on a small DEMO_TARGETS list — it will MISS whole-script spoofs of brands not on the list (deliberate, to avoid Russian false positives) (Q1). (4) Cyrillic mixed-script overlaps the base MSL reader; this card's net-new coverage is Greek + whole-script-on-target + the documented method. (5) Not a language detector; percent/punycode-delivered look-alikes need the pre-pass in front.

**13. INTEGRATION_INTERFACE_STATUS.** INTEGRATION_STATUS: PROTOTYPED (raw). RAW_PROTOTYPE: `confusable_cards.py::confusable_cards_reader(text) -> Finding`. HARNESS: `range_confusable.py`. LIVE RESULT (real MSL + supplement + digit + metachar as baseline): **homoglyph spoofs 5/6 (83%) → 6/6 (100%), genuine text 4/4 → 4/4, 0 new FP**; the added catch is the Greek-omicron spoof (`gοogle`) the baseline misses, and an FP-stress over 25 ordinary Russian words flags **0**. REQUIRES for closing: full UTS #39 confusables + brand corpus (Q1); more scripts (Q2); numeral/punctuation siblings (Q3); pre-pass in front; conveyor review.

> HOW THE RAW PROTOTYPE WORKS: `MSL_MIP_HOME=/path/to/msl_mip python code/range/range_confusable.py` scans Cyrillic/Greek homoglyph spoofs, a whole-script target case, and genuine single-script text (Latin, Russian, accented, CJK) BEFORE (MSL baseline) and AFTER (+ this confusable card), printing the before/after verdict per case plus totals; real Russian stays OK by the mix-not-foreignness rule.

---

<a name="русский"></a>
## Русский

DRAFT_NOTE (2026-07-20): первая КЛАССОВАЯ карточка оси **видимого обмана** — опасность в символе, который ВИДНО, но он похож на другой. Управляющий закон: **ВЫГЛЯДИТ_ОДИНАКОВО ≠ ОДНО_И_ТО_ЖЕ.** `paypal.com` и `pаypal.com` рисуются одинаково, но во втором кириллическая `а` (U+0430) среди латинских букв — mixed-script confusable (IDN / бренд-спуф). Структурный сигнал НЕ «есть не-латинская буква» (это флагнуло бы весь русский) — это ОДИН ТОКЕН, смешивающий базовую письменность с похожими буквами другой. Бланкетное правило «whole-script, нет родного якоря» протестировано и ОТКЛОНЕНО (срабатывало на ~25% обычных русских слов); whole-script судится только против цели. WORKING_DRAFT, БЕЗКОНВЕЙЕРНО.

**0. UNIVERSALITY.** BOUND_TO_SPECIFIC_SIGN: CLASS (межскриптовые похожие буквы) · AFTER_USE_RESIDUE: FORBIDDEN · SIGN_DATA_IS_SESSION_ONLY: YES

**1. COMMON_CONVEYOR_DISCIPLINE.** v0_3 · RUN_CARD_REQUIRED_BEFORE_LOCK: YES · MODEL_FAMILY_DIVERSITY_REQUIRED: YES · ADVERSARIAL_EVIDENCE_REQUIRED: YES · MUTATION_CHECK_REQUIRED: YES · LIMITATION_STATEMENT_REQUIRED: YES. TRACKER: WORKING_DRAFT YES; PREFLIGHT PENDING; CONVEYOR_REVIEW PENDING; WORKINGLY_CLOSED NO.

**2. META.** ZONE: ZONE_1. WHY_THIS_SIGN_MATTERS: гомоглиф-спуфинг — хребет фишинга: домен, бренд или хэндл, отрисованный одной-двумя чужими похожими буквами, проходит глаз и в IDN резолвится на регистрацию атакующего. Unicode UTS #39 определяет confusables (карту скелетов) и детекцию mixed-script / whole-script; mixed-script — рабочая лошадка с малым числом ложных. INTERACTS_WITH: базовый MSL-ридер (уже несёт набор кириллических похожих — эта карточка консолидирует ось как классовую карточку и РАСШИРЯЕТ на греческий и whole-script-по-цели), CANONICALIZATION_PRE_PASS (похожая может прийти percent/entity-кодированной), WHITESPACE_CLASS / METACHAR_CLASS (confusable рядом с доменным разделителем усиливает спуф).

**3. REQUIRED_GENERAL_GUARDS.** RAW_SIGN_INPUT_STATUS: DATA_ONLY · NO_EXECUTION_FROM_SIGN: YES · NO_TRUST_FROM_SIGN: YES · DECODE_BEFORE_TRUST: YES · JUDGE_MIX_NOT_MERE_FOREIGNNESS: YES (одна чужая буква не спуф) · NEVER_FLAG_GENUINE_NATIVE_TEXT: YES (настоящий русский/греческий остаётся OK).

**4. SIGN IDENTITY — LAYER_A (LOCK: PERMANENT).** BASE_MODE: DATA_ONLY_VISIBLE_LOOKALIKE · BASE_MODE_FORMULA: ВЫГЛЯДИТ_ОДИНАКОВО ≠ ОДНО_И_ТО_ЖЕ ; СПУФ = СМЕШЕНИЕ_ПИСЬМЕННОСТЕЙ_В_ОДНОМ_ТОКЕНЕ или WHOLE_SCRIPT_ПО_ЦЕЛИ.

| Источник | Примеры (→ латинский скелет) | Приоритет | Механизм атаки | Легит-применение (остаётся OK) |
|---|---|---|---|---|
| Кириллические похожие | а→a е→e о→o р→p с→c у→y х→x і→i ѕ→s ј→j (и заглавные А В Е К М Н О Р С Т Х У) | ВЫСОКИЙ | вмешаны в латинский токен — IDN / бренд-спуф | настоящий русский текст (одна письменность) |
| Греческие похожие | ο→o α→a ρ→p ν→v ι→i κ→k (и заглавные Α Β Ε Η Ι Κ Μ Ν Ο Ρ Τ Υ Χ) | ВЫСОКИЙ | вмешаны в латинский токен | настоящий греческий текст (одна письменность) |
| U+2010 HYPHEN | ‐ → - | СРЕД. | похож на ASCII-дефис в домене | типографический дефис в прозе |

WHAT_THIS_SIGN_IS_NOT: (1) NOT_SPOOF_BY_FOREIGNNESS — не-латинская буква спуф лишь СМЕШАННАЯ в токен другой письменности; (2) NOT_ABOUT_SINGLE_SCRIPT — настоящий русский/греческий/CJK легитимен; (3) NOT_FINAL_SURFACE — похожая может прийти percent/entity-кодированной, сперва декод.
BASE_FORMULAS: MIXED_SCRIPT_CONFUSABLE = ЛАТИНИЦА + ЧУЖАЯ_ПОХОЖАЯ_В_ОДНОМ_ТОКЕНЕ ; WHOLE_SCRIPT_SPOOF = ВСЁ_ЧУЖОЕ ∧ СКЕЛЕТ ∈ ЦЕЛИ ; СКЕЛЕТ = каждую похожую в её латинского двойника.

**5. SEMANTIC_EPOCH_TRACKER (LOCK: REVIEWABLE).** EPOCH_TRACKER: поверхность атаки выросла с IDN (интернационализированные домены) и с платформами, разрешающими не-ASCII хэндлы; браузеры в ответ добавили punycode / правила отображения mixed-script, но бэкенд-сравнение строк часто всё ещё сырое. NOTE: ЗАЩИТА_ОТОБРАЖЕНИЯ_БРАУЗЕРА ≠ ЗАЩИТА_БЭКЕНДА.

**6. EFFECT_FIELDS — LAYER_C (LOCK: SESSION).** authority / trust / verification / proof / execution / permission / status / role_assignment / runtime / existence effect: всё NONE. EFFECT_FIELDS_ALL_NONE: YES · CLOSED_SCHEMA: YES.

**7. SAFE / RISK / GUARDS — LAYER_B (LOCK: REVIEWABLE).**
Ключ на СМЕШЕНИИ письменностей в одном токене плюс проверка цели для whole-script:
- ALARM (conclusive): токен смешивает латиницу с кириллическими/греческими буквами-конфьюзаблами (`pаypal`, `gοogle`) — показан латинский скелет; ИЛИ полностью-чужой токен, чей скелет равен известной цели (`уаһоо` → `yahoo`).
- OK (чистое): одно-скриптовый токен (вся латиница, весь кириллик, весь греческий, CJK); настоящее родное слово; акцентированная латиница.
SAFE_CASES (должны остаться OK): `paypal.com`; `привет мир как дела` (настоящий русский — включая слова только из похожих букв, как `соус`, `орех`); `Zürich café résumé`; `日本語 の 文書`.
RISK_CASES: `pаypal.com` (кириллическая а) ALARM → имперсонирует `paypal`; `аpple.com` ALARM; `gοogle.com` (греческая ο) ALARM; `micrоsоft` ALARM; `уаһоо.com` (весь кириллик) ALARM → `yahoo`.
GUARD_PRINCIPLE: срабатывать на СМЕШЕНИИ, не на чуждости; показывать латинский скелет, чтобы имперсонация была читаема; держать настоящий одно-скриптовый текст OK; судить whole-script лишь против списка целей.

**8. ADVERSARIAL_COVERAGE — RUN_CARD SEED.** кириллические и греческие похожие в брендах/доменах/хэндлах; одна vs. несколько подменённых букв; ведущая vs. срединная подмена; U+2010 в дефисном домене; настоящий русский/греческий/CJK (должны остаться OK, включая слова из одних похожих); whole-script в списке целей и вне его; каждый кейс ТАКЖЕ percent/entity-кодированный (путь pre-pass). MODEL_FAMILY_DIVERSITY_REQUIRED: YES.

**9. MUTATION_CHECK.** литеральная похожая ↔ `%XX` / `&#N;` ↔ punycode; одна подмена vs. много; похожая в начале/середине/конце токена. INVARIANT: после канонизации один вердикт; mixed-script токен остаётся ALARM, настоящий одно-скриптовый остаётся OK во всех формах.

**10. KNOWN_OPEN_QUESTIONS.** Q1: заменить ручную карту кириллица/греческий и DEMO_TARGETS полной таблицей скелетов Unicode confusables (UTS #39) и настоящим корпусом брендов/доменов. Q2: больше письменностей-источников (армянский, Latin-Extended похожие, полноширинные формы, конфьюзаблы цифра/буква вроде 0/O 1/l). Q3: числовые конфьюзаблы (римские цифры U+2160+, надстрочные) и набор видимой пунктуации фишинга (`.` `/` `@` полноширинные формы) — вероятно, свои родственные карточки. Q4: проверка коллизии по скелету (два входа с общим скелетом) для детекции near-дубликатов.

**11. PATCH_HISTORY.** v0_1 (2026-07-20): первый черновик confusable/homoglyph КЛАССОВОЙ карточки (ось видимого обмана) — mixed-script ALARM + whole-script по цели, в паре с `confusable_cards.py`. Бланкетное no-anchor WATCH протестировано и отклонено (русские ложные). Не прогонялся через конвейер.

**12. LIMITATION_STATEMENT.** (1) WORKING_DRAFT / NOT_CONVEYOR_RUN. (2) Карта конфьюзаблов — ручное высокоценное подмножество (кириллица + греческий + U+2010), не полная таблица UTS #39 (Q1). (3) Whole-script детекция ограничена малым списком DEMO_TARGETS — пропустит whole-script спуфы брендов не из списка (намеренно, чтобы избежать русских ложных) (Q1). (4) Кириллический mixed-script пересекается с базовым MSL-ридером; чистый новый охват этой карточки — греческий + whole-script-по-цели + задокументированный метод. (5) Не детектор языка; percent/punycode-доставленные похожие требуют pre-pass впереди.

**13. INTEGRATION_INTERFACE_STATUS.** INTEGRATION_STATUS: PROTOTYPED (сырой). RAW_PROTOTYPE: `confusable_cards.py::confusable_cards_reader(text) -> Finding`. HARNESS: `range_confusable.py`. ЖИВОЙ РЕЗУЛЬТАТ (настоящий MSL + supplement + digit + metachar как база): **гомоглиф-спуфы 5/6 (83%) → 6/6 (100%), настоящий текст 4/4 → 4/4, 0 новых FP**; добавленный улов — греческо-омикрон спуф (`gοogle`), который база пропускает, а FP-стресс по 25 обычным русским словам даёт **0**. ТРЕБУЕТСЯ для закрытия: полный UTS #39 confusables + корпус брендов (Q1); больше письменностей (Q2); числовые/пунктуационные родственники (Q3); pre-pass впереди; конвейер-ревью.

> КАК РАБОТАЕТ СЫРОЙ ПРОТОТИП: `MSL_MIP_HOME=/path/to/msl_mip python code/range/range_confusable.py` сканирует кириллические/греческие гомоглиф-спуфы, whole-script кейс-цель и настоящий одно-скриптовый текст (латиница, русский, акцентированный, CJK) BEFORE (база MSL) и AFTER (+ эта confusable-карточка), печатая вердикт до/после по кейсу и итоги; настоящий русский остаётся OK по правилу смешение-не-чуждость.
