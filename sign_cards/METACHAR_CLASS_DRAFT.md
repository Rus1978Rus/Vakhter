PRIVATE AUTHORIAL PROJECT / ЧАСТНЫЙ АВТОРСКИЙ ПРОЕКТ · COMMERCIAL USE PROHIBITED

# SIGN CORE CARD — METACHARACTER CLASS (class card, DRAFT)

DOCUMENT_ID: SIGN_CORE_CARD_METACHAR_CLASS_GEN3_v0_1 · DOCUMENT_TYPE: SIGN_CORE_CARD · TEMPLATE_LINE: GEN3_v0_3
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
RAW_PROTOTYPE: `code/range/metachar_cards.py` · HARNESS: `code/range/range_meta.py`

🇬🇧 [English](#english) · 🇷🇺 [Русский](#русский)

---

<a name="english"></a>
## English

DRAFT_NOTE (2026-07-20): a draft of the CLASS card for the metacharacter family — the punctuation signs that become an OPERATOR when the surrounding text is code (a query, a shell line, markup, an HTTP header). It follows the MSL/MIP method: a sign is DATA until context makes it operational; the card fires on the sign IN ITS GRAMMAR, not on bare presence. The drafts are deliberately NON-CONVEYOR for now — conveyor closing is a separate project; here we only need the raw prototype to run so we can see the shape of the detection.

**0. UNIVERSALITY.** BOUND_TO_SPECIFIC_SIGN: CLASS (' " ` | ; & $ ( ) < > : = %00 CR LF) · AFTER_USE_RESIDUE: FORBIDDEN · SIGN_DATA_IS_SESSION_ONLY: YES

**1. COMMON_CONVEYOR_DISCIPLINE.** CONVEYOR_DISCIPLINE_VERSION: v0_3 · RUN_CARD_REQUIRED_BEFORE_LOCK: YES · MODEL_FAMILY_DIVERSITY_REQUIRED: YES · ADVERSARIAL_EVIDENCE_REQUIRED: YES · MUTATION_CHECK_REQUIRED: YES · LIMITATION_STATEMENT_REQUIRED: YES. STATUS_PROGRESSION_TRACKER: WORKING_DRAFT YES; STRUCTURAL_PREFLIGHT_PASS PENDING; CONVEYOR_REVIEW_PASS PENDING; WORKINGLY_CLOSED NO.

**2. META.** ZONE: ZONE_1 (stable written signs, polysemous). WHY_THIS_SIGN_MATTERS: each of these signs is harmless prose punctuation AND the operator that ends a string, chains a command, opens a tag, or splits a header. The danger is not the glyph — it is the glyph landing in an executable GRAMMAR. INTERACTS_WITH: DIGIT_CLASS (each sign is reconstructable via percent-encoding — %27 ' , %60 ` , %7C | , %3C < , %00 NUL, %0D%0A CRLF), CANONICALIZATION_PRE_PASS (must decode before this card reads), DOT/SOLIDUS/AT cards.

**3. REQUIRED_GENERAL_GUARDS.** RAW_SIGN_INPUT_STATUS: DATA_ONLY · NO_EXECUTION_FROM_SIGN: YES · NO_TRUST_FROM_SIGN: YES · DECODE_BEFORE_TRUST: YES · JUDGE_IN_CONTEXT_NOT_ON_PRESENCE: YES.

**4. SIGN IDENTITY — LAYER_A: STABLE CORE (LOCK: PERMANENT).**
BASE_MODE: DATA_ONLY_GLYPH · BASE_MODE_FORMULA: METACHAR_FORM ≠ EFFECT.
CONTEXT_MODES (a metacharacter has one benign and one operational face):
- PROSE_FACE: an apostrophe in `don't`, quotes around `'hello'`, math `a < b`, a table `a | b`, markdown `` `code` `` — DATA, no effect.
- OPERATOR_FACE: the same glyph next to a grammar keyword — `' OR 1=1`, `` `whoami` ``, `| nc`, `<script>`, a header name after CRLF — OPERATIONAL.
SIGN_CATEGORY: string_delimiter (' "); command_substitution (` $( )); command_separator (| ; &); markup_delimiter (< >); protocol_delimiter (: = for URLs/headers); terminator/control (%00 NUL, CR, LF).
WHAT_THIS_SIGN_IS_NOT: (1) NOT_EFFECT_BY_PRESENCE — a lone `'` or `|` is not an attack; the operator face needs a grammar around it; (2) NOT_FINAL_SURFACE — the sign may arrive percent-encoded (%27, %7C) and must be decoded first; (3) NOT_LANGUAGE_INTENT — the card reads the sign's grammar, not the sentence's meaning.
BASE_FORMULAS: METACHAR_FORM ≠ EFFECT ; ≠ FINAL_SURFACE ; PRESENCE ≠ OPERATOR ; OPERATOR = SIGN + GRAMMAR.

**5. SEMANTIC_EPOCH_TRACKER (LOCK: REVIEWABLE).** EPOCH_TRACKER: NOT_APPLICABLE. NOTE: these signs carry prose and operator functions simultaneously across many grammars (SQL, shell, HTML, HTTP) — polysemy of a stable class, not an epoch shift.

**6. EFFECT_FIELDS — LAYER_C (LOCK: SESSION).** authority / trust / verification / proof / execution / permission / status / role_assignment / runtime / existence effect: all NONE. EFFECT_FIELDS_ALL_NONE: YES · CLOSED_SCHEMA: YES.

**7. SAFE / RISK / GUARDS — LAYER_B (LOCK: REVIEWABLE).**
SAFE_CASES (must stay INFO): "I don't think it's a problem" (apostrophe); "she said 'hello there'" (quotes); "if a < b and c > d" (math); "call the `print()` function" (markdown code); "col A | col B | col C" (table pipe); "the flag is true|false" (boolean); "the <b> tag makes text bold" (HTML mention); "I love bash scripting" (shell word); multi-line text (bare CR/LF). GUARD in all: PRESENCE ≠ OPERATOR — no grammar, no fire.
RISK_CASES: R-SQLI quote + SQL operator `id=1' OR '1'='1`, `admin'--`, `1' UNION SELECT` → ALARM, sig `sqli`; R-CMDI backtick/`$( )`/`| ; &` + command word `` `whoami` ``, `$(id)`, `host | nc evil`, `x; rm -rf /` → ALARM, sig `cmdi`; R-XSS `<script>`, `<img onerror=`, `javascript:` → ALARM, sig `xss`; R-NULL `%00` in a path/filename → ALARM, sig `null_byte` (string truncation / extension bypass); R-CRLF CR/LF followed by a header name (`\r\nSet-Cookie:`) → ALARM, sig `crlf` (header/log injection).
GUARD_PRINCIPLE (the FP-safety of the whole class): the card matches the sign ONLY inside its operator grammar (quote next to a SQL keyword; backtick wrapping a command; CRLF immediately before a header name). Bare punctuation in prose never fires.

**8. ADVERSARIAL_COVERAGE — RUN_CARD SEED.** SEED_ATTACKS_REQUIRED_IN_RUN: SQLi (quote+operator, comment, UNION); command injection (backtick, `$()`, pipe, chain); XSS (script tag, event handler, `javascript:`); NUL truncation; CRLF header injection; each of the above delivered PERCENT-ENCODED (to test the pre-pass path). BENIGN_CONTROLS_REQUIRED: apostrophe, quotes, math `<`/`>`, markdown code, table pipe, boolean or, HTML mention, shell word.

**9. MUTATION_CHECK.** MUTATIONS_TO_SURVIVE: literal ↔ percent-encoded (`'` ↔ `%27`, `|` ↔ `%7C`, `<` ↔ `%3C`); case of the grammar keyword (`OR` ↔ `or`); whitespace padding between sign and keyword. INVARIANT: after canonicalization all variants yield ONE verdict.

**10. KNOWN_OPEN_QUESTIONS.** Q1: grammar coverage — LDAP/NoSQL/XPath operator families and PowerShell cmdlets are not yet in the operator set. Q2: nested/second-order contexts (a value that becomes a query only downstream). Q3: how much whitespace/comment obfuscation between sign and keyword to tolerate before it is ReDoS-risky (the prototype bounds it — see LIMITATION).

**11. PATCH_HISTORY.** v0_1 (2026-07-20): first draft of the metacharacter CLASS card, paired with the existing `metachar_cards.py` prototype. Not conveyor-run.

**12. LIMITATION_STATEMENT.** (1) WORKING_DRAFT / NOT_CONVEYOR_RUN: this is a spec + raw prototype, not a closed detector. (2) Detection is contextual PATTERN matching, not a full grammar parser — a sufficiently novel grammar can evade it (that is why point 9's list is open). (3) Percent-encoded delivery is only caught WITH the CANONICALIZATION_PRE_PASS in front. (4) The prototype bounds every wildcard (`[^}]{0,200}`, `[ \t]{0,16}`) to stay linear — this trades some exotic-spacing coverage for ReDoS-safety, on purpose. (5) It does not cover language-level intent (that is the semantic layer beside MSL, blind by design).

**13. INTEGRATION_INTERFACE_STATUS.** INTEGRATION_STATUS: PROTOTYPED (raw). RAW_PROTOTYPE: `metachar_cards.py::metachar_cards_reader(text) -> Finding`. HARNESS: `range_meta.py`. LIVE RESULT (real MSL, `MSL_MIP_HOME` set): **metachar threats 2/11 (18%) → 11/11 (100%), benign 9/9 kept clean, 0 new FP.** REQUIRES for closing: CANONICALIZATION_PRE_PASS in front; conveyor review (the separate project); expansion of the operator set (§10).

> HOW THE RAW PROTOTYPE WORKS: run `MSL_MIP_HOME=/path/to/msl_mip python code/range/range_meta.py`. It scans each case with real MSL alone (BEFORE) and with MSL + this card (AFTER), and prints the before/after verdict per case plus the totals. That is the card "working" before any conveyor touches it.

---

<a name="русский"></a>
## Русский

DRAFT_NOTE (2026-07-20): черновик КЛАССОВОЙ карточки семейства метасимволов — знаков пунктуации, которые становятся ОПЕРАТОРОМ, когда окружающий текст — это код (запрос, shell-строка, разметка, HTTP-заголовок). Следует методу MSL/MIP: знак — это ДАННЫЕ, пока контекст не сделает его операционным; карточка срабатывает на знак В ЕГО ГРАММАТИКЕ, а не на голое присутствие. Черновики намеренно БЕЗКОНВЕЙЕРНЫ пока — закрытие конвейером это отдельный проект; здесь нужно лишь, чтобы сырой прототип бежал и была видна форма детекции.

**0. UNIVERSALITY.** BOUND_TO_SPECIFIC_SIGN: CLASS (' " ` | ; & $ ( ) < > : = %00 CR LF) · AFTER_USE_RESIDUE: FORBIDDEN · SIGN_DATA_IS_SESSION_ONLY: YES

**1. COMMON_CONVEYOR_DISCIPLINE.** CONVEYOR_DISCIPLINE_VERSION: v0_3 · RUN_CARD_REQUIRED_BEFORE_LOCK: YES · MODEL_FAMILY_DIVERSITY_REQUIRED: YES · ADVERSARIAL_EVIDENCE_REQUIRED: YES · MUTATION_CHECK_REQUIRED: YES · LIMITATION_STATEMENT_REQUIRED: YES. STATUS_PROGRESSION_TRACKER: WORKING_DRAFT YES; STRUCTURAL_PREFLIGHT_PASS PENDING; CONVEYOR_REVIEW_PASS PENDING; WORKINGLY_CLOSED NO.

**2. META.** ZONE: ZONE_1 (стабильные письменные знаки, полисемичные). WHY_THIS_SIGN_MATTERS: каждый из этих знаков — и безобидная пунктуация текста, И оператор, который закрывает строку, сцепляет команду, открывает тег или расщепляет заголовок. Опасность не в глифе — а в том, что глиф попал в исполняемую ГРАММАТИКУ. INTERACTS_WITH: DIGIT_CLASS (каждый знак воссоздаётся percent-кодировкой — %27 ' , %60 ` , %7C | , %3C < , %00 NUL, %0D%0A CRLF), CANONICALIZATION_PRE_PASS (должен декодировать до чтения этой карточкой), карточки DOT/SOLIDUS/AT.

**3. REQUIRED_GENERAL_GUARDS.** RAW_SIGN_INPUT_STATUS: DATA_ONLY · NO_EXECUTION_FROM_SIGN: YES · NO_TRUST_FROM_SIGN: YES · DECODE_BEFORE_TRUST: YES · JUDGE_IN_CONTEXT_NOT_ON_PRESENCE: YES.

**4. SIGN IDENTITY — LAYER_A: STABLE CORE (LOCK: PERMANENT).**
BASE_MODE: DATA_ONLY_GLYPH · BASE_MODE_FORMULA: METACHAR_FORM ≠ EFFECT.
CONTEXT_MODES (у метасимвола одно безобидное лицо и одно операционное):
- PROSE_FACE: апостроф в `don't`, кавычки `'hello'`, математика `a < b`, таблица `a | b`, markdown `` `code` `` — ДАННЫЕ, нет эффекта.
- OPERATOR_FACE: тот же глиф рядом с грамматическим ключевым словом — `' OR 1=1`, `` `whoami` ``, `| nc`, `<script>`, имя заголовка после CRLF — ОПЕРАЦИОННЫЙ.
SIGN_CATEGORY: string_delimiter (' "); command_substitution (` $( )); command_separator (| ; &); markup_delimiter (< >); protocol_delimiter (: = для URL/заголовков); terminator/control (%00 NUL, CR, LF).
WHAT_THIS_SIGN_IS_NOT: (1) NOT_EFFECT_BY_PRESENCE — одинокий `'` или `|` не атака; операционному лицу нужна грамматика вокруг; (2) NOT_FINAL_SURFACE — знак может прийти percent-кодированным (%27, %7C) и должен быть сперва раскрыт; (3) NOT_LANGUAGE_INTENT — карточка читает грамматику знака, не смысл предложения.
BASE_FORMULAS: METACHAR_FORM ≠ EFFECT ; ≠ FINAL_SURFACE ; PRESENCE ≠ OPERATOR ; OPERATOR = SIGN + GRAMMAR.

**5. SEMANTIC_EPOCH_TRACKER (LOCK: REVIEWABLE).** EPOCH_TRACKER: NOT_APPLICABLE. NOTE: эти знаки несут функции текста и оператора одновременно во многих грамматиках (SQL, shell, HTML, HTTP) — полисемия стабильного класса, не смена эпох.

**6. EFFECT_FIELDS — LAYER_C (LOCK: SESSION).** authority / trust / verification / proof / execution / permission / status / role_assignment / runtime / existence effect: всё NONE. EFFECT_FIELDS_ALL_NONE: YES · CLOSED_SCHEMA: YES.

**7. SAFE / RISK / GUARDS — LAYER_B (LOCK: REVIEWABLE).**
SAFE_CASES (должны остаться INFO): "I don't think it's a problem" (апостроф); "she said 'hello there'" (кавычки); "if a < b and c > d" (математика); "call the `print()` function" (markdown-код); "col A | col B | col C" (таблица-pipe); "the flag is true|false" (булево); "the <b> tag makes text bold" (упоминание HTML); "I love bash scripting" (shell-слово); многострочный текст (голые CR/LF). GUARD везде: PRESENCE ≠ OPERATOR — нет грамматики, нет срабатывания.
RISK_CASES: R-SQLI кавычка + SQL-оператор `id=1' OR '1'='1`, `admin'--`, `1' UNION SELECT` → ALARM, sig `sqli`; R-CMDI backtick/`$( )`/`| ; &` + команда `` `whoami` ``, `$(id)`, `host | nc evil`, `x; rm -rf /` → ALARM, sig `cmdi`; R-XSS `<script>`, `<img onerror=`, `javascript:` → ALARM, sig `xss`; R-NULL `%00` в пути/имени файла → ALARM, sig `null_byte` (обрыв строки / обход расширения); R-CRLF CR/LF + имя заголовка (`\r\nSet-Cookie:`) → ALARM, sig `crlf` (инъекция заголовка/лога).
GUARD_PRINCIPLE (FP-безопасность всего класса): карточка матчит знак ТОЛЬКО внутри его операторной грамматики (кавычка рядом с SQL-словом; backtick, обрамляющий команду; CRLF прямо перед именем заголовка). Голая пунктуация в тексте не срабатывает никогда.

**8. ADVERSARIAL_COVERAGE — RUN_CARD SEED.** SEED_ATTACKS_REQUIRED_IN_RUN: SQLi (кавычка+оператор, комментарий, UNION); command injection (backtick, `$()`, pipe, цепочка); XSS (script-тег, обработчик события, `javascript:`); NUL-обрыв; CRLF-инъекция заголовка; каждое из выше — доставленное PERCENT-КОДИРОВАННЫМ (проверить путь pre-pass). BENIGN_CONTROLS_REQUIRED: апостроф, кавычки, математика `<`/`>`, markdown-код, таблица-pipe, булево or, упоминание HTML, shell-слово.

**9. MUTATION_CHECK.** MUTATIONS_TO_SURVIVE: литерал ↔ percent-код (`'` ↔ `%27`, `|` ↔ `%7C`, `<` ↔ `%3C`); регистр грамматического слова (`OR` ↔ `or`); пробельная набивка между знаком и словом. INVARIANT: после канонизации все варианты дают ОДИН вердикт.

**10. KNOWN_OPEN_QUESTIONS.** Q1: охват грамматик — семейства LDAP/NoSQL/XPath и командлеты PowerShell ещё не в наборе операторов. Q2: вложенные/второго порядка контексты (значение, становящееся запросом лишь ниже по потоку). Q3: сколько пробельно-комментарной обфускации между знаком и словом терпеть, прежде чем это станет ReDoS-риском (прототип это ограничивает — см. LIMITATION).

**11. PATCH_HISTORY.** v0_1 (2026-07-20): первый черновик КЛАССОВОЙ карточки метасимволов, в паре с существующим прототипом `metachar_cards.py`. Не прогонялся через конвейер.

**12. LIMITATION_STATEMENT.** (1) WORKING_DRAFT / NOT_CONVEYOR_RUN: это спека + сырой прототип, а не закрытый детектор. (2) Детекция — контекстное СОВПАДЕНИЕ ПО ПАТТЕРНУ, не полный парсер грамматики — достаточно новая грамматика может уйти (потому список в п.9 открыт). (3) Percent-кодированная доставка ловится ТОЛЬКО с CANONICALIZATION_PRE_PASS впереди. (4) Прототип ограничивает каждый wildcard (`[^}]{0,200}`, `[ \t]{0,16}`), чтобы остаться линейным — это намеренный размен части экзотического пробельного охвата на ReDoS-безопасность. (5) Не покрывает языковой смысл (это смысловой слой рядом с MSL, слеп by design).

**13. INTEGRATION_INTERFACE_STATUS.** INTEGRATION_STATUS: PROTOTYPED (сырой). RAW_PROTOTYPE: `metachar_cards.py::metachar_cards_reader(text) -> Finding`. HARNESS: `range_meta.py`. ЖИВОЙ РЕЗУЛЬТАТ (настоящий MSL, задан `MSL_MIP_HOME`): **метасимвольные угрозы 2/11 (18%) → 11/11 (100%), безобидное 9/9 остаётся чистым, 0 новых FP.** ТРЕБУЕТСЯ для закрытия: CANONICALIZATION_PRE_PASS впереди; конвейер-ревью (отдельный проект); расширение набора операторов (п.10).

> КАК РАБОТАЕТ СЫРОЙ ПРОТОТИП: запусти `MSL_MIP_HOME=/path/to/msl_mip python code/range/range_meta.py`. Он сканирует каждый кейс настоящим MSL в одиночку (BEFORE) и MSL + эта карточка (AFTER), печатает вердикт до/после по каждому кейсу и итоги. Это карточка «в работе» ещё до того, как её коснётся конвейер.
