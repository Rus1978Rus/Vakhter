PRIVATE AUTHORIAL PROJECT / ЧАСТНЫЙ АВТОРСКИЙ ПРОЕКТ · COMMERCIAL USE PROHIBITED

# SIGN CORE CARD — WHITESPACE / SPACE-LOOKALIKE CLASS (class card, DRAFT)

DOCUMENT_ID: SIGN_CORE_CARD_WHITESPACE_CLASS_GEN3_v0_1 · DOCUMENT_TYPE: SIGN_CORE_CARD · TEMPLATE_LINE: GEN3_v0_3
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
PRIORITY_TIER: P1/P2 (split by member) · RAW_PROTOTYPE: `code/range/whitespace_cards.py` · HARNESS: `code/range/range_whitespace.py`
SCOPE: non-ASCII space-like and line/paragraph separators — U+00A0, U+1680, U+2000–U+200A, U+2028, U+2029, U+202F, U+205F, U+3000. Zero-width signs (U+200B+) are the INVISIBLE_CLASS; U+180E is in MONITORED_FORMAT.

🇬🇧 [English](#english) · 🇷🇺 [Русский](#русский)

---

<a name="english"></a>
## English

DRAFT_NOTE (2026-07-20): the CLASS card for the whitespace / space-lookalike family. This card is the clearest illustration of a core priority principle: **being often-abused ≠ being auto-HIGH.** The family splits by *real vector*, not by "looks like a space": the LINE and PARAGRAPH SEPARATORS (U+2028/U+2029) are genuine HIGH members — invisible line breaks that inject records/statements into JS/JSON/CSV/logs — while NBSP and the typographic spaces are mostly a WITNESS tier, because they have massive legitimate use (French thin space, CJK spacing, non-breaking typography). The card is three-tier: **ALARM** (separator, or a lookalike doing delimiter duty against a metacharacter), **WITNESS/WATCH** (a lookalike in an ASCII context — held, not stripped), **OK** (genuine i18n typography). WORKING_DRAFT, NON-CONVEYOR.

**0. UNIVERSALITY.** BOUND_TO_SPECIFIC_SIGN: CLASS (non-ASCII whitespace + line/para separators) · AFTER_USE_RESIDUE: FORBIDDEN · SIGN_DATA_IS_SESSION_ONLY: YES

**1. COMMON_CONVEYOR_DISCIPLINE.** v0_3 · RUN_CARD_REQUIRED_BEFORE_LOCK: YES · MODEL_FAMILY_DIVERSITY_REQUIRED: YES · ADVERSARIAL_EVIDENCE_REQUIRED: YES · MUTATION_CHECK_REQUIRED: YES · LIMITATION_STATEMENT_REQUIRED: YES. TRACKER: WORKING_DRAFT YES; PREFLIGHT PENDING; CONVEYOR_REVIEW PENDING; WORKINGLY_CLOSED NO.

**2. META.** ZONE: ZONE_1. WHY_THIS_SIGN_MATTERS: a space-lookalike passes the eye's "that's a space" check but is a DIFFERENT codepoint, so it breaks tokenization, keyword filters and allowlists that split on the ASCII space (a shell sees `rm‹NBSP›-rf` as one token; a blocklist that greps `drop table` misses `drop‹NBSP›table`). The LINE/PARAGRAPH separators are worse: they are line terminators to a parser but not to a human — U+2028/U+2029 famously broke JSON-in-JS embedding for years (they are valid JSON but were illegal in JS string literals pre-ES2019). Unicode UAX #14 / UAX #44 classify these as Zs (space), Zl (line) and Zp (paragraph). INTERACTS_WITH: METACHAR_CLASS (a lookalike next to a metacharacter is a delimiter masquerade), INVISIBLE_CLASS (adjacent — but these OCCUPY width, they are not zero-width), CANONICALIZATION_PRE_PASS (a space can arrive as `&#160;`/`&nbsp;` and must be decoded first).

**3. REQUIRED_GENERAL_GUARDS.** RAW_SIGN_INPUT_STATUS: DATA_ONLY · NO_EXECUTION_FROM_SIGN: YES · NO_TRUST_FROM_SIGN: YES · DECODE_BEFORE_TRUST: YES · JUDGE_IN_CONTEXT_NOT_ON_PRESENCE: YES · NEVER_BLIND_STRIP: YES (NBSP/NNBSP/CJK space carry real typography) · PRIORITIZE_BY_VECTOR_NOT_BY_LOOK: YES.

**4. SIGN IDENTITY — LAYER_A (LOCK: PERMANENT).** BASE_MODE: DATA_ONLY_SPACING · BASE_MODE_FORMULA: SPACE_LOOKALIKE ≠ ASCII_SPACE ; SEPARATOR = INVISIBLE_NEWLINE ; OFTEN_ABUSED ≠ AUTO_HIGH.

| Codepoint(s) | Name | Cat | Priority | Attack mechanism | Legitimate use (do NOT blind-strip) |
|---|---|---|---|---|---|
| U+2028 | LINE SEPARATOR | Zl | HIGH (P1) | invisible newline — record / JS / log injection | true line break in some formats |
| U+2029 | PARAGRAPH SEPARATOR | Zp | HIGH (P1) | invisible paragraph break — record / statement split | true paragraph break |
| U+00A0 | NO-BREAK SPACE (NBSP) | Zs | WITNESS (P2) | delimiter masquerade, split-on-space bypass | non-breaking typography (everywhere) |
| U+202F | NARROW NO-BREAK SPACE (NNBSP) | Zs | WITNESS (P2) | delimiter masquerade | French thin space, Mongolian |
| U+2000–U+200A | EN/EM/THREE-PER-EM/…/HAIR SPACE | Zs | WITNESS (P2) | token/keyword split, homoglyph gap | fine typographic spacing |
| U+205F | MEDIUM MATHEMATICAL SPACE (MMSP) | Zs | WITNESS (P2) | token split | mathematical layout |
| U+3000 | IDEOGRAPHIC SPACE | Zs | WITNESS (P2) | token split in CJK-adjacent text | CJK word/sentence spacing |
| U+1680 | OGHAM SPACE MARK | Zs | WITNESS (P2) | token split | Ogham script |

WHAT_THIS_SIGN_IS_NOT: (1) NOT_ASCII_SPACE — a different codepoint despite the look; (2) NOT_AUTO_HIGH — most members are witnesses; the separators are the HIGH ones; (3) NOT_STRIPPABLE — deleting NBSP/CJK space corrupts real text; (4) NOT_FINAL_SURFACE — may arrive as `&#160;`/`&nbsp;`/`%C2%A0` and must be decoded first.
BASE_FORMULAS: SPACE_LOOKALIKE ≠ ASCII_SPACE ; SEPARATOR(U+2028/9) = INVISIBLE_NEWLINE ; DELIMITER_MASQUERADE = LOOKALIKE + METACHAR_NEIGHBOUR ; OTHERWISE = WITNESS.

**5. SEMANTIC_EPOCH_TRACKER (LOCK: REVIEWABLE).** EPOCH_TRACKER: U+2028/U+2029 shifted from "obscure format chars" to "known JS-injection primitive" and were finally made legal in JS strings only in ES2019 — the risk profile changed with the ecosystem, not the codepoint. NOTE: LEGALIZED_LATER ≠ HARMLESS_EVERYWHERE (older parsers, other formats still split on them).

**6. EFFECT_FIELDS — LAYER_C (LOCK: SESSION).** authority / trust / verification / proof / execution / permission / status / role_assignment / runtime / existence effect: all NONE. EFFECT_FIELDS_ALL_NONE: YES · CLOSED_SCHEMA: YES.

**7. SAFE / RISK / GUARDS — LAYER_B (LOCK: REVIEWABLE).**
Three tiers, keyed on member and context:
- ALARM (conclusive): U+2028/U+2029 present (invisible newline → injection); a space-lookalike sitting directly against a syntax metacharacter (`rm‹NBSP›-rf`, `cat f‹NNBSP›| sh`, `role‹EMSP›=‹EMSP›admin`) — delimiter masquerade.
- WITNESS / WATCH (held, not stripped, "not auto-HIGH"): a space-lookalike in an ASCII / non-prose context (`hello‹NBSP›world`, `1‹FIGURE SPACE›000`) — flagged for review, never auto-deleted.
- OK (clean, "i18n typography" vouch): a space-lookalike as an ordinary letter-to-letter word gap in text that carries non-ASCII letters (`Café‹NBSP›résumé`, `日本‹IDEOGRAPHIC SPACE›語`); or no lookalikes at all.
SAFE_CASES (must stay OK): accented Latin / CJK prose using non-ASCII spaces as word gaps; plain ASCII text.
RISK_CASES: `user=admin‹LINE SEP›role=root` (record injection) ALARM; `row1‹PARA SEP›; DROP TABLE t` ALARM; `rm‹NBSP›-rf` ALARM; `hello‹NBSP›world` WATCH (witness); `1‹FIGURE SPACE›000` WATCH.
GUARD_PRINCIPLE: prioritize by vector — separators and metachar-adjacent lookalikes ALARM; everything else is a witness at WATCH, never an auto-strip; the eye's "it's a space" is exactly the deception, so judge on codepoint + context.

**8. ADVERSARIAL_COVERAGE — RUN_CARD SEED.** U+2028/9 in a config line, a log line, a JSON value, a CSV field; NBSP/NNBSP/EM space against `-`, `=`, `/`, `|`, `;`; a keyword split by a lookalike (`drop‹NBSP›table`); legit accented / CJK / French-thin-space prose (must stay OK); every case ALSO delivered via `&#N;`/`&nbsp;`/percent (pre-pass path). MODEL_FAMILY_DIVERSITY_REQUIRED: YES.

**9. MUTATION_CHECK.** literal space ↔ `&#160;`/`&nbsp;` ↔ `%XX` byte form; separator at line start/middle/end; lookalike as gap vs. as delimiter. INVARIANT: after canonicalization one verdict; a separator stays ALARM, a legit typographic gap stays OK, an ASCII-context lookalike stays WITNESS across all forms.

**10. KNOWN_OPEN_QUESTIONS.** Q1: format-aware separator policy — U+2028/9 is legal in some targets (modern JS strings, plain text) but injection in others (CSV, logs, old parsers); the verdict could carry the target context. Q2: a keyword-split model — flag a lookalike that splits a specific blocklisted keyword even without a metacharacter neighbour. Q3: promote a witness to ALARM when the same lookalike recurs across a stream (ERG axis), separating a one-off copy-paste artifact from a deliberate pattern.

**11. PATCH_HISTORY.** v0_1 (2026-07-20): first draft of the whitespace / space-lookalike CLASS card with the three-tier vector split (separator / delimiter-masquerade / witness), paired with `whitespace_cards.py`. Not conveyor-run.

**12. LIMITATION_STATEMENT.** (1) WORKING_DRAFT / NOT_CONVEYOR_RUN. (2) The delimiter-masquerade tier fires on a metacharacter neighbour; a lookalike splitting a keyword with no metacharacter neighbour is only a WITNESS for now (Q2). (3) Separator verdict is target-agnostic — it does not yet know that U+2028 is safe in a modern-JS string but unsafe in a CSV field (Q1). (4) The i18n vouch uses "non-ASCII letter present + letter-to-letter gap"; a hostile string that also contains a non-ASCII letter and keeps its lookalike between letters could be vouched — the metachar and separator tiers still fire, but a pure keyword-split is not caught here (Q2). (5) Entity-delivered spaces are caught only WITH the pre-pass in front.

**13. INTEGRATION_INTERFACE_STATUS.** INTEGRATION_STATUS: PROTOTYPED (raw). RAW_PROTOTYPE: `whitespace_cards.py::whitespace_cards_reader(text) -> Finding`. HARNESS: `range_whitespace.py`. LIVE RESULT (real MSL + invisible + bidi + tag + vs as baseline): **sep/delimiter 1/5 (20%) → 5/5 (100%), legit typography 3/3 → 3/3, 0 new FP**; the WITNESS tier (`hello‹NBSP›world`, `1‹FIGURE SPACE›000`) is held at WATCH — a live demonstration of "space-lookalike ≠ automatically dangerous". REQUIRES for closing: format-aware separator policy (Q1); keyword-split model (Q2); recurrence promotion (Q3); pre-pass in front; conveyor review.

> HOW THE RAW PROTOTYPE WORKS: `MSL_MIP_HOME=/path/to/msl_mip python code/range/range_whitespace.py` scans separators, delimiter masquerades, witness cases and legit typography BEFORE (MSL + prior invisible axes) and AFTER (+ this whitespace axis), printing the before/after verdict per case, the WITNESS tier, and totals.

---

<a name="русский"></a>
## Русский

DRAFT_NOTE (2026-07-20): КЛАССОВАЯ карточка семейства пробелов / пробел-двойников. Эта карточка — яснейшая иллюстрация ключевого принципа приоритизации: **часто злоупотребляемое ≠ авто-HIGH.** Семейство делится по *реальному вектору*, а не по «похоже на пробел»: РАЗДЕЛИТЕЛИ СТРОК и АБЗАЦЕВ (U+2028/U+2029) — настоящие HIGH-члены — невидимые переносы строк, впрыскивающие записи/операторы в JS/JSON/CSV/логи — тогда как NBSP и типографические пробелы это в основном ярус WITNESS, потому что у них огромное легит-применение (французский тонкий пробел, CJK-разрядка, неразрывная типографика). Карточка трёхъярусная: **ALARM** (разделитель, или двойник в роли разделителя рядом с метасимволом), **WITNESS/WATCH** (двойник в ASCII-контексте — держим, не вырезаем), **OK** (настоящая i18n-типографика). WORKING_DRAFT, БЕЗКОНВЕЙЕРНО.

**0. UNIVERSALITY.** BOUND_TO_SPECIFIC_SIGN: CLASS (не-ASCII пробелы + разделители строк/абзацев) · AFTER_USE_RESIDUE: FORBIDDEN · SIGN_DATA_IS_SESSION_ONLY: YES

**1. COMMON_CONVEYOR_DISCIPLINE.** v0_3 · RUN_CARD_REQUIRED_BEFORE_LOCK: YES · MODEL_FAMILY_DIVERSITY_REQUIRED: YES · ADVERSARIAL_EVIDENCE_REQUIRED: YES · MUTATION_CHECK_REQUIRED: YES · LIMITATION_STATEMENT_REQUIRED: YES. TRACKER: WORKING_DRAFT YES; PREFLIGHT PENDING; CONVEYOR_REVIEW PENDING; WORKINGLY_CLOSED NO.

**2. META.** ZONE: ZONE_1. WHY_THIS_SIGN_MATTERS: пробел-двойник проходит глазную проверку «это пробел», но это ДРУГОЙ кодпоинт, поэтому он ломает токенизацию, keyword-фильтры и allowlist, разбивающие по ASCII-пробелу (shell видит `rm‹NBSP›-rf` одним токеном; blocklist, ищущий `drop table`, пропускает `drop‹NBSP›table`). Разделители СТРОК/АБЗАЦЕВ хуже: для парсера это терминаторы строки, для человека — нет — U+2028/U+2029 годами ломали встраивание JSON-в-JS (валидны в JSON, но были нелегальны в JS-строках до ES2019). Unicode UAX #14 / UAX #44 классифицируют их как Zs (пробел), Zl (строка), Zp (абзац). INTERACTS_WITH: METACHAR_CLASS (двойник рядом с метасимволом это разделитель-маскировка), INVISIBLE_CLASS (смежная — но эти ЗАНИМАЮТ ширину, они не zero-width), CANONICALIZATION_PRE_PASS (пробел может прийти как `&#160;`/`&nbsp;`, сперва декод).

**3. REQUIRED_GENERAL_GUARDS.** RAW_SIGN_INPUT_STATUS: DATA_ONLY · NO_EXECUTION_FROM_SIGN: YES · NO_TRUST_FROM_SIGN: YES · DECODE_BEFORE_TRUST: YES · JUDGE_IN_CONTEXT_NOT_ON_PRESENCE: YES · NEVER_BLIND_STRIP: YES (NBSP/NNBSP/CJK-пробел несут настоящую типографику) · PRIORITIZE_BY_VECTOR_NOT_BY_LOOK: YES.

**4. SIGN IDENTITY — LAYER_A (LOCK: PERMANENT).** BASE_MODE: DATA_ONLY_SPACING · BASE_MODE_FORMULA: SPACE_LOOKALIKE ≠ ASCII_SPACE ; SEPARATOR = INVISIBLE_NEWLINE ; OFTEN_ABUSED ≠ AUTO_HIGH.

| Кодпоинт(ы) | Имя | Кат | Приоритет | Механизм атаки | Легит-применение (НЕ вырезать слепо) |
|---|---|---|---|---|---|
| U+2028 | LINE SEPARATOR | Zl | ВЫСОКИЙ (P1) | невидимый перенос — впрыск записи / JS / лога | настоящий перенос строки в части форматов |
| U+2029 | PARAGRAPH SEPARATOR | Zp | ВЫСОКИЙ (P1) | невидимый разрыв абзаца — расщепление записи/оператора | настоящий разрыв абзаца |
| U+00A0 | NO-BREAK SPACE (NBSP) | Zs | WITNESS (P2) | разделитель-маскировка, обход split-по-пробелу | неразрывная типографика (повсюду) |
| U+202F | NARROW NO-BREAK SPACE (NNBSP) | Zs | WITNESS (P2) | разделитель-маскировка | французский тонкий пробел, монгольский |
| U+2000–U+200A | EN/EM/THREE-PER-EM/…/HAIR SPACE | Zs | WITNESS (P2) | разбиение токена/ключевого слова, зазор-гомоглиф | тонкая типографическая разрядка |
| U+205F | MEDIUM MATHEMATICAL SPACE (MMSP) | Zs | WITNESS (P2) | разбиение токена | математическая раскладка |
| U+3000 | IDEOGRAPHIC SPACE | Zs | WITNESS (P2) | разбиение токена в CJK-соседнем тексте | CJK-разрядка слов/предложений |
| U+1680 | OGHAM SPACE MARK | Zs | WITNESS (P2) | разбиение токена | огамическое письмо |

WHAT_THIS_SIGN_IS_NOT: (1) NOT_ASCII_SPACE — другой кодпоинт, несмотря на вид; (2) NOT_AUTO_HIGH — большинство членов свидетели; HIGH это разделители; (3) NOT_STRIPPABLE — удаление NBSP/CJK-пробела портит настоящий текст; (4) NOT_FINAL_SURFACE — может прийти как `&#160;`/`&nbsp;`/`%C2%A0`, сперва декод.
BASE_FORMULAS: SPACE_LOOKALIKE ≠ ASCII_SPACE ; SEPARATOR(U+2028/9) = INVISIBLE_NEWLINE ; DELIMITER_MASQUERADE = LOOKALIKE + СОСЕД_МЕТАСИМВОЛ ; ИНАЧЕ = WITNESS.

**5. SEMANTIC_EPOCH_TRACKER (LOCK: REVIEWABLE).** EPOCH_TRACKER: U+2028/U+2029 сместились от «малозаметных форматных символов» к «известному примитиву JS-инъекции» и были легализованы в JS-строках лишь в ES2019 — профиль риска сменился с экосистемой, не с кодпоинтом. NOTE: ЛЕГАЛИЗОВАНО_ПОЗЖЕ ≠ БЕЗВРЕДНО_ВЕЗДЕ (старые парсеры, иные форматы всё ещё разбивают по ним).

**6. EFFECT_FIELDS — LAYER_C (LOCK: SESSION).** authority / trust / verification / proof / execution / permission / status / role_assignment / runtime / existence effect: всё NONE. EFFECT_FIELDS_ALL_NONE: YES · CLOSED_SCHEMA: YES.

**7. SAFE / RISK / GUARDS — LAYER_B (LOCK: REVIEWABLE).**
Три яруса, по члену и контексту:
- ALARM (conclusive): U+2028/U+2029 присутствует (невидимый перенос → инъекция); пробел-двойник вплотную к синтаксическому метасимволу (`rm‹NBSP›-rf`, `cat f‹NNBSP›| sh`, `role‹EMSP›=‹EMSP›admin`) — разделитель-маскировка.
- WITNESS / WATCH (держим, не вырезаем, «не авто-HIGH»): пробел-двойник в ASCII / не-прозаическом контексте (`hello‹NBSP›world`, `1‹FIGURE SPACE›000`) — флаг на ревью, никогда не авто-удаление.
- OK (чистое, вауч «i18n-типографика»): пробел-двойник как обычный зазор буква-к-букве в тексте с не-ASCII буквами (`Café‹NBSP›résumé`, `日本‹IDEOGRAPHIC SPACE›語`); или двойников нет вовсе.
SAFE_CASES (должны остаться OK): акцентированная латиница / CJK-проза, использующая не-ASCII пробелы как зазоры слов; обычный ASCII-текст.
RISK_CASES: `user=admin‹LINE SEP›role=root` (инъекция записи) ALARM; `row1‹PARA SEP›; DROP TABLE t` ALARM; `rm‹NBSP›-rf` ALARM; `hello‹NBSP›world` WATCH (свидетель); `1‹FIGURE SPACE›000` WATCH.
GUARD_PRINCIPLE: приоритизировать по вектору — разделители и метасимвол-соседние двойники ALARM; всё прочее свидетель на WATCH, никогда авто-strip; глазное «это пробел» и есть обман, поэтому судить по кодпоинту + контексту.

**8. ADVERSARIAL_COVERAGE — RUN_CARD SEED.** U+2028/9 в строке конфига, строке лога, значении JSON, поле CSV; NBSP/NNBSP/EM-пробел против `-`, `=`, `/`, `|`, `;`; ключевое слово, разбитое двойником (`drop‹NBSP›table`); легит акцентированная / CJK / французская-тонкий-пробел проза (должна остаться OK); каждый кейс ТАКЖЕ доставлен `&#N;`/`&nbsp;`/percent (путь pre-pass). MODEL_FAMILY_DIVERSITY_REQUIRED: YES.

**9. MUTATION_CHECK.** литеральный пробел ↔ `&#160;`/`&nbsp;` ↔ байтовая форма `%XX`; разделитель в начале/середине/конце строки; двойник как зазор vs. как разделитель. INVARIANT: после канонизации один вердикт; разделитель остаётся ALARM, легит типографический зазор остаётся OK, двойник в ASCII-контексте остаётся WITNESS во всех формах.

**10. KNOWN_OPEN_QUESTIONS.** Q1: политика разделителей с учётом формата — U+2028/9 легален в части целей (современные JS-строки, простой текст), но инъекция в других (CSV, логи, старые парсеры); вердикт мог бы нести контекст цели. Q2: модель разбиения ключевых слов — флагать двойник, разбивающий конкретное blocklist-слово, даже без соседа-метасимвола. Q3: повышать свидетеля до ALARM, когда тот же двойник повторяется по потоку (ось ERG), отделяя одноразовый copy-paste артефакт от намеренного паттерна.

**11. PATCH_HISTORY.** v0_1 (2026-07-20): первый черновик КЛАССОВОЙ карточки пробелов / пробел-двойников с трёхъярусным делением по вектору (разделитель / разделитель-маскировка / свидетель), в паре с `whitespace_cards.py`. Не прогонялся через конвейер.

**12. LIMITATION_STATEMENT.** (1) WORKING_DRAFT / NOT_CONVEYOR_RUN. (2) Ярус разделитель-маскировка срабатывает на соседе-метасимволе; двойник, разбивающий ключевое слово без соседа-метасимвола, пока лишь WITNESS (Q2). (3) Вердикт разделителя не зависит от цели — он ещё не знает, что U+2028 безопасен в современной JS-строке, но опасен в поле CSV (Q1). (4) i18n-вауч использует «есть не-ASCII буква + зазор буква-к-букве»; враждебная строка, содержащая не-ASCII букву и держащая двойник между буквами, могла бы получить вауч — ярусы метасимвола и разделителя всё равно срабатывают, но чистое разбиение ключевого слова здесь не ловится (Q2). (5) Entity-доставленные пробелы ловятся только С pre-pass впереди.

**13. INTEGRATION_INTERFACE_STATUS.** INTEGRATION_STATUS: PROTOTYPED (сырой). RAW_PROTOTYPE: `whitespace_cards.py::whitespace_cards_reader(text) -> Finding`. HARNESS: `range_whitespace.py`. ЖИВОЙ РЕЗУЛЬТАТ (настоящий MSL + invisible + bidi + tag + vs как база): **разделитель/делимитер 1/5 (20%) → 5/5 (100%), легит-типографика 3/3 → 3/3, 0 новых FP**; ярус WITNESS (`hello‹NBSP›world`, `1‹FIGURE SPACE›000`) держится на WATCH — живая демонстрация «пробел-двойник ≠ автоматически опасен». ТРЕБУЕТСЯ для закрытия: политика разделителей с учётом формата (Q1); модель разбиения ключевых слов (Q2); повышение по повтору (Q3); pre-pass впереди; конвейер-ревью.

> КАК РАБОТАЕТ СЫРОЙ ПРОТОТИП: `MSL_MIP_HOME=/path/to/msl_mip python code/range/range_whitespace.py` сканирует разделители, разделитель-маскировки, кейсы-свидетели и легит-типографику BEFORE (MSL + прежние невидимые оси) и AFTER (+ эта пробел-ось), печатая вердикт до/после по кейсу, ярус WITNESS и итоги.
