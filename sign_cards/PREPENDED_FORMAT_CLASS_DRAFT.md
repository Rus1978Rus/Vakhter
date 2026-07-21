PRIVATE AUTHORIAL PROJECT / ЧАСТНЫЙ АВТОРСКИЙ ПРОЕКТ · COMMERCIAL USE PROHIBITED

# SIGN CORE CARD — PREPENDED / ENCLOSING-FORMAT CLASS (class card, DRAFT)

DOCUMENT_ID: SIGN_CORE_CARD_PREPENDED_FORMAT_CLASS_GEN3_v0_1 · DOCUMENT_TYPE: SIGN_CORE_CARD · TEMPLATE_LINE: GEN3_v0_3
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
PRIORITY_TIER: P1/P2 (Cf-not-DI tail — outside "class 138") · RAW_PROTOTYPE: `code/range/prepended_format_cards.py` · HARNESS: `code/range/range_prepended.py`
SCOPE: the format (Cf) characters that are NOT default-ignorable — U+0600–0605, U+06DD, U+070F, U+0890, U+0891, U+08E2, U+110BD, U+110CD (prepended concatenation marks); U+FFF9–FFFB (interlinear annotation); U+13430–1343F (Egyptian format). This is the sibling of the Default_Ignorable contour, not part of it.

🇬🇧 [English](#english) · 🇷🇺 [Русский](#русский)

---

<a name="english"></a>
## English

DRAFT_NOTE (2026-07-20): the CLASS card for the **Cf-but-NOT-default-ignorable** tail — the reason "class 138" is 138 and not 163. Of Unicode's 163 format (Cf) characters, 25 assigned ones are NOT default-ignorable, and they are different in kind: they **ACT on their scope instead of hiding.** A prepended concatenation mark takes the following digits as its scope and encloses/annotates them; an interlinear-annotation or Egyptian-segment control brackets a run. Because they DO something visible/structural, they sit OUTSIDE the invisible contour — hence a separate card. Governing law: **PREPENDED_FORMAT ≠ INVISIBLE ; the danger is SCOPE, not concealment** — a mark pointed at the wrong scope (foreign digits, a security token) or an unbalanced bracket. WORKING_DRAFT, NON-CONVEYOR.

**0. UNIVERSALITY.** BOUND_TO_SPECIFIC_SIGN: CLASS (Cf-not-DI format: prepended concatenation marks + bracketing/annotation controls) · AFTER_USE_RESIDUE: FORBIDDEN · SIGN_DATA_IS_SESSION_ONLY: YES

**1. COMMON_CONVEYOR_DISCIPLINE.** v0_3 · RUN_CARD_REQUIRED_BEFORE_LOCK: YES · MODEL_FAMILY_DIVERSITY_REQUIRED: YES · ADVERSARIAL_EVIDENCE_REQUIRED: YES · MUTATION_CHECK_REQUIRED: YES · LIMITATION_STATEMENT_REQUIRED: YES. TRACKER: WORKING_DRAFT YES; PREFLIGHT PENDING; CONVEYOR_REVIEW PENDING; WORKINGLY_CLOSED NO.

**2. META.** ZONE: ZONE_1. WHY_THIS_SIGN_MATTERS: these are the format characters a defender who only knows "invisibles" will miss from the OTHER direction — they are format (Cf) yet render as visible marks or as structure, so an invisible-scanner passes them and a text-scanner mis-scopes them. Two mechanism branches: **prepended concatenation marks** (Arabic/Syriac/Kaithi number & abbreviation signs) prepend to and enclose the FOLLOWING characters — Unicode's "prepended concatenation mark" property; point one at foreign digits and the enclosing/number effect lands where it should not (amount/number spoofing). **Bracketing/annotation controls** (interlinear annotation FFF9–FFFB, Egyptian segment/join 13430–1343F) come in ANCHOR..SEPARATOR..TERMINATOR triples or BEGIN..END pairs; unbalance them and a parser desyncs or hidden "annotation" text diverges from display — Unicode explicitly says interlinear annotation is NOT for open interchange. INTERACTS_WITH: WHITESPACE_CLASS (both reason about scope/structure, not concealment), METACHAR_CLASS (a mis-scoped mark against a metacharacter), CANONICALIZATION_PRE_PASS (decode entity/percent first).

**3. REQUIRED_GENERAL_GUARDS.** RAW_SIGN_INPUT_STATUS: DATA_ONLY · NO_EXECUTION_FROM_SIGN: YES · NO_TRUST_FROM_SIGN: YES · DECODE_BEFORE_TRUST: YES · JUDGE_SCOPE_NOT_JUST_PRESENCE: YES · NEVER_BLIND_STRIP: YES (a mark scopes real Arabic/Egyptian text) · NOT_PART_OF_138: YES (Cf but not default-ignorable).

**4. SIGN IDENTITY — LAYER_A (LOCK: PERMANENT).** BASE_MODE: DATA_ONLY_SCOPING_FORMAT · BASE_MODE_FORMULA: PREPENDED_FORMAT ≠ INVISIBLE ; DANGER = SCOPE ; MARK ⟶ ITS_OWN_SCRIPT_SCOPE.

| Codepoint(s) | Name | Branch | Priority | Attack mechanism | Legitimate use (do NOT blind-strip) |
|---|---|---|---|---|---|
| U+0600–U+0605 | ARABIC NUMBER SIGN / SANAH / FOOTNOTE MARKER / SAFHA / SAMVAT / NUMBER MARK ABOVE | prepend | HIGH | encloses foreign digits / security token — number spoofing | prefixes Arabic-Indic digits |
| U+06DD | ARABIC END OF AYAH | prepend | HIGH | scope abuse over non-Arabic content | encloses an Arabic verse number |
| U+0890 / U+0891 | ARABIC POUND / PIASTRE MARK ABOVE | prepend | HIGH | currency-mark scope abuse | prefixes Arabic-Indic amount digits |
| U+08E2 | ARABIC DISPUTED END OF AYAH | prepend | MED | scope abuse | encloses an Arabic verse number |
| U+070F | SYRIAC ABBREVIATION MARK | prepend | MED | over-scoping following letters | marks a Syriac abbreviation |
| U+110BD / U+110CD | KAITHI NUMBER SIGN / ABOVE | prepend | MED | scope abuse over foreign digits | prefixes Kaithi digits |
| U+FFF9 / U+FFFA / U+FFFB | INTERLINEAR ANNOTATION ANCHOR / SEPARATOR / TERMINATOR | bracket | HIGH | imbalance / orphan → hidden annotation, parser desync | ruby/interlinear (NOT for open interchange) |
| U+13430–U+1343F | EGYPTIAN HIEROGLYPH format (joiners, inserts, BEGIN/END SEGMENT; 13439–1343F reserved) | bracket | MED | unbalanced segment brackets | hieroglyph layout / quadrat structure |

WHAT_THIS_SIGN_IS_NOT: (1) NOT_DEFAULT_IGNORABLE — it renders / structures, it does not hide; (2) NOT_IN_CLASS_138 — Cf, but the 25 that are excluded from the default-ignorable set; (3) NOT_STRIPPABLE — deleting a mark corrupts real Arabic numbers / Egyptian layout; (4) NOT_FINAL_SURFACE — may arrive entity/percent-encoded and must be decoded first.
BASE_FORMULAS: IN_SCRIPT_SCOPE = OK ; WRONG_SCOPE or ORPHAN = ALARM ; UNBALANCED_BRACKET = ALARM ; ANNOTATION_PRESENT = WITNESS.

**5. SEMANTIC_EPOCH_TRACKER (LOCK: REVIEWABLE).** EPOCH_TRACKER: the prepended-concatenation-mark property was formalized relatively recently and new marks (U+0890/0891) were added in Unicode 14 — a version-blind tool may not scope them; the interlinear annotation carve-out ("not for interchange") is long-standing. NOTE: NEWLY_PROPERTIED ≠ SAFELY_HANDLED (a stack that doesn't know a mark's scope mis-lays-out following digits).

**6. EFFECT_FIELDS — LAYER_C (LOCK: SESSION).** authority / trust / verification / proof / execution / permission / status / role_assignment / runtime / existence effect: all NONE. EFFECT_FIELDS_ALL_NONE: YES · CLOSED_SCHEMA: YES.

**7. SAFE / RISK / GUARDS — LAYER_B (LOCK: REVIEWABLE).**
Three tiers, keyed on SCOPE and BALANCE:
- ALARM (conclusive): a prepended concatenation mark NOT scoping its own script's digits/letters (an Arabic number sign over ASCII digits, an end-of-ayah not on Arabic digits, an orphan at end of string); unbalanced interlinear annotation (anchor ≠ terminator); an orphan separator with no annotation open; unbalanced Egyptian segment brackets.
- WATCH (witness): balanced interlinear annotation present — Unicode says it is not for open interchange, so even balanced it is held for review.
- OK (clean, "in-script scope" vouch): a prepended mark immediately followed by its own script's digits/letters (Arabic number sign + Arabic-Indic digits); a balanced Egyptian segment; nothing present.
SAFE_CASES (must stay OK): `‹ARABIC NUMBER SIGN›١٢٣` (sign scoping Arabic digits); a balanced Egyptian BEGIN..‹glyph›..END segment; plain text.
RISK_CASES: `amount ‹ARABIC NUMBER SIGN›1000 USD` (sign over ASCII digits) ALARM; `verse ‹END OF AYAH› ok` (orphan) ALARM; `base‹ANCHOR›hidden ruby` (no terminator) ALARM; `a‹SEPARATOR›b` (orphan separator) ALARM; `glyph ‹BEGIN SEGMENT›…` (no end) ALARM; a balanced `‹ANCHOR›kana‹TERMINATOR›` WATCH.
GUARD_PRINCIPLE: judge SCOPE, not mere presence — a mark on its own script is legit, a mark on foreign/ASCII content or a broken bracket is the attack; interlinear annotation is a witness even when balanced; never strip a mark that scopes real content.

**8. ADVERSARIAL_COVERAGE — RUN_CARD SEED.** Arabic/Kaithi number sign over ASCII digits, over letters, over a metacharacter, orphaned at end; unbalanced and nested interlinear annotation; orphan separator; unbalanced Egyptian segment; legit Arabic-digit and Egyptian-segment cases (must stay OK); every case ALSO delivered entity/percent-encoded (pre-pass path). MODEL_FAMILY_DIVERSITY_REQUIRED: YES.

**9. MUTATION_CHECK.** literal mark ↔ `&#N;` ↔ `%XX` byte form; in-scope vs. wrong-scope; balanced vs. off-by-one bracket. INVARIANT: after canonicalization one verdict; an in-script scope stays OK, a wrong scope / imbalance stays ALARM, a balanced annotation stays WITNESS across all forms.

**10. KNOWN_OPEN_QUESTIONS.** Q1: full prepended-concatenation-mark scope model — how many following digits a given mark legitimately encloses, so an over-long scope is caught even over own-script digits. Q2: nested-annotation grammar (anchor/separator/terminator ordering and nesting), beyond the count-balance used here. Q3: whether U+13439–1343F (reserved Egyptian format) belong here or in RESERVED_IGNORABLE (they are Cf-adjacent reserved, not default-ignorable).

**11. PATCH_HISTORY.** v0_1 (2026-07-20): first draft of the prepended/enclosing-format CLASS card — the Cf-not-DI sibling that explains why the contour is 138 — paired with `prepended_format_cards.py`. Not conveyor-run.

**12. LIMITATION_STATEMENT.** (1) WORKING_DRAFT / NOT_CONVEYOR_RUN. (2) PCM scope is checked one character ahead (is the NEXT character an own-script digit/letter), not the full number span (Q1). (3) Annotation balance is a count check, not a grammar (nesting/order) check (Q2). (4) Reserved Egyptian format (13439–1343F) is not owned here (Q3). (5) Entity/percent-delivered marks are caught only WITH the pre-pass in front.

**13. INTEGRATION_INTERFACE_STATUS.** INTEGRATION_STATUS: PROTOTYPED (raw). RAW_PROTOTYPE: `prepended_format_cards.py::prepended_format_cards_reader(text) -> Finding`. HARNESS: `range_prepended.py`. LIVE RESULT (real MSL + all 6 invisible axes + the 3 tail cards as baseline): **scope-abuse/imbalance 0/5 (0%) → 5/5 (100%), legit in-script 3/3 → 3/3, 0 new FP**; balanced interlinear annotation is held at WATCH (not-for-interchange witness). REQUIRES for closing: full PCM scope model (Q1); annotation grammar (Q2); reserved-Egyptian decision (Q3); pre-pass in front; conveyor review.

> HOW THE RAW PROTOTYPE WORKS: `MSL_MIP_HOME=/path/to/msl_mip python code/range/range_prepended.py` scans scope-abuse and bracket-imbalance cases, the annotation witness case, and legit in-script content BEFORE (MSL + all invisible axes + tail) and AFTER (+ this prepended-format axis), printing the before/after verdict per case, the WITNESS tier, and totals.

---

<a name="русский"></a>
## Русский

DRAFT_NOTE (2026-07-20): КЛАССОВАЯ карточка хвоста **Cf, но НЕ default-ignorable** — причины, почему «класс 138» это 138, а не 163. Из 163 форматных (Cf) знаков Unicode 25 назначенных НЕ default-ignorable, и они иного рода: они **ДЕЙСТВУЮТ на свою область вместо сокрытия.** Prepended concatenation mark берёт следующие цифры своей областью и обрамляет/аннотирует их; interlinear-annotation или Egyptian-segment контроль скобит прогон. Поскольку они ДЕЛАЮТ что-то видимое/структурное, они лежат ВНЕ невидимого контура — отсюда отдельная карточка. Управляющий закон: **PREPENDED_FORMAT ≠ НЕВИДИМЫЙ ; опасность в ОБЛАСТИ, не в сокрытии** — марка, наведённая на неправильную область (чужие цифры, security-токен), или несбалансированная скобка. WORKING_DRAFT, БЕЗКОНВЕЙЕРНО.

**0. UNIVERSALITY.** BOUND_TO_SPECIFIC_SIGN: CLASS (Cf-не-DI формат: prepended concatenation marks + скобящие/аннотационные контроли) · AFTER_USE_RESIDUE: FORBIDDEN · SIGN_DATA_IS_SESSION_ONLY: YES

**1. COMMON_CONVEYOR_DISCIPLINE.** v0_3 · RUN_CARD_REQUIRED_BEFORE_LOCK: YES · MODEL_FAMILY_DIVERSITY_REQUIRED: YES · ADVERSARIAL_EVIDENCE_REQUIRED: YES · MUTATION_CHECK_REQUIRED: YES · LIMITATION_STATEMENT_REQUIRED: YES. TRACKER: WORKING_DRAFT YES; PREFLIGHT PENDING; CONVEYOR_REVIEW PENDING; WORKINGLY_CLOSED NO.

**2. META.** ZONE: ZONE_1. WHY_THIS_SIGN_MATTERS: это форматные знаки, которые защитник, знающий лишь «невидимки», пропустит с ДРУГОЙ стороны — они формат (Cf), но рисуются видимыми марками или как структура, поэтому невидимка-сканер их пропускает, а текст-сканер неправильно скоупит. Две ветки механизма: **prepended concatenation marks** (арабские/сирийские/кайтхи числовые и аббревиатурные знаки) прибавляются к и обрамляют СЛЕДУЮЩИЕ символы — свойство Unicode «prepended concatenation mark»; наведи одну на чужие цифры, и обрамляющий/числовой эффект ляжет туда, куда не должен (спуф суммы/числа). **Скобящие/аннотационные контроли** (interlinear annotation FFF9–FFFB, египетский segment/join 13430–1343F) идут тройками ANCHOR..SEPARATOR..TERMINATOR или парами BEGIN..END; разбалансируй их — и парсер десинхронизируется или скрытый «аннотационный» текст разойдётся с отображением — Unicode прямо говорит, что interlinear annotation НЕ для открытого обмена. INTERACTS_WITH: WHITESPACE_CLASS (обе рассуждают об области/структуре, не о сокрытии), METACHAR_CLASS (неправильно-скоупленная марка против метасимвола), CANONICALIZATION_PRE_PASS (сперва декод entity/percent).

**3. REQUIRED_GENERAL_GUARDS.** RAW_SIGN_INPUT_STATUS: DATA_ONLY · NO_EXECUTION_FROM_SIGN: YES · NO_TRUST_FROM_SIGN: YES · DECODE_BEFORE_TRUST: YES · JUDGE_SCOPE_NOT_JUST_PRESENCE: YES · NEVER_BLIND_STRIP: YES (марка скоупит настоящий арабский/египетский текст) · NOT_PART_OF_138: YES (Cf, но не default-ignorable).

**4. SIGN IDENTITY — LAYER_A (LOCK: PERMANENT).** BASE_MODE: DATA_ONLY_SCOPING_FORMAT · BASE_MODE_FORMULA: PREPENDED_FORMAT ≠ НЕВИДИМЫЙ ; ОПАСНОСТЬ = ОБЛАСТЬ ; МАРКА ⟶ ОБЛАСТЬ_СВОЕЙ_ПИСЬМЕННОСТИ.

| Кодпоинт(ы) | Имя | Ветка | Приоритет | Механизм атаки | Легит-применение (НЕ вырезать слепо) |
|---|---|---|---|---|---|
| U+0600–U+0605 | ARABIC NUMBER SIGN / SANAH / FOOTNOTE MARKER / SAFHA / SAMVAT / NUMBER MARK ABOVE | prepend | ВЫСОКИЙ | обрамляет чужие цифры / security-токен — спуф числа | префиксует арабо-индийские цифры |
| U+06DD | ARABIC END OF AYAH | prepend | ВЫСОКИЙ | scope abuse над не-арабским контентом | обрамляет номер арабского аята |
| U+0890 / U+0891 | ARABIC POUND / PIASTRE MARK ABOVE | prepend | ВЫСОКИЙ | scope abuse валютной марки | префиксует арабо-индийские цифры суммы |
| U+08E2 | ARABIC DISPUTED END OF AYAH | prepend | СРЕД. | scope abuse | обрамляет номер арабского аята |
| U+070F | SYRIAC ABBREVIATION MARK | prepend | СРЕД. | over-scoping следующих букв | маркирует сирийскую аббревиатуру |
| U+110BD / U+110CD | KAITHI NUMBER SIGN / ABOVE | prepend | СРЕД. | scope abuse над чужими цифрами | префиксует кайтхи-цифры |
| U+FFF9 / U+FFFA / U+FFFB | INTERLINEAR ANNOTATION ANCHOR / SEPARATOR / TERMINATOR | bracket | ВЫСОКИЙ | дисбаланс / сирота → скрытая аннотация, десинхрон парсера | ruby/interlinear (НЕ для открытого обмена) |
| U+13430–U+1343F | EGYPTIAN HIEROGLYPH формат (joiners, inserts, BEGIN/END SEGMENT; 13439–1343F зарезервированы) | bracket | СРЕД. | несбалансированные скобки сегмента | раскладка иероглифов / структура квадрата |

WHAT_THIS_SIGN_IS_NOT: (1) NOT_DEFAULT_IGNORABLE — он рисует / структурирует, не прячет; (2) NOT_IN_CLASS_138 — Cf, но те 25, что исключены из default-ignorable набора; (3) NOT_STRIPPABLE — удаление марки портит настоящие арабские числа / египетскую раскладку; (4) NOT_FINAL_SURFACE — может прийти entity/percent-кодированным, сперва декод.
BASE_FORMULAS: IN_SCRIPT_SCOPE = OK ; WRONG_SCOPE или ORPHAN = ALARM ; UNBALANCED_BRACKET = ALARM ; ANNOTATION_PRESENT = WITNESS.

**5. SEMANTIC_EPOCH_TRACKER (LOCK: REVIEWABLE).** EPOCH_TRACKER: свойство prepended-concatenation-mark формализовано относительно недавно, а новые марки (U+0890/0891) добавлены в Unicode 14 — версия-слепой инструмент может их не скоупить; carve-out interlinear annotation («не для обмена») давний. NOTE: НОВОЕ_СВОЙСТВО ≠ БЕЗОПАСНАЯ_ОБРАБОТКА (стек, не знающий области марки, неправильно раскладывает следующие цифры).

**6. EFFECT_FIELDS — LAYER_C (LOCK: SESSION).** authority / trust / verification / proof / execution / permission / status / role_assignment / runtime / existence effect: всё NONE. EFFECT_FIELDS_ALL_NONE: YES · CLOSED_SCHEMA: YES.

**7. SAFE / RISK / GUARDS — LAYER_B (LOCK: REVIEWABLE).**
Три яруса, ключ на ОБЛАСТИ и БАЛАНСЕ:
- ALARM (conclusive): prepended concatenation mark, НЕ скоупящая цифры/буквы своей письменности (арабский number sign над ASCII-цифрами, end-of-ayah не на арабских цифрах, сирота в конце строки); несбалансированная interlinear annotation (anchor ≠ terminator); сиротский separator без открытой аннотации; несбалансированные египетские скобки сегмента.
- WATCH (свидетель): сбалансированная interlinear annotation присутствует — Unicode говорит, она не для открытого обмена, поэтому даже сбалансированная держится на ревью.
- OK (чистое, вауч «in-script область»): prepended-марка сразу за которой цифры/буквы своей письменности (арабский number sign + арабо-индийские цифры); сбалансированный египетский сегмент; ничего нет.
SAFE_CASES (должны остаться OK): `‹ARABIC NUMBER SIGN›١٢٣` (знак скоупит арабские цифры); сбалансированный египетский BEGIN..‹глиф›..END сегмент; обычный текст.
RISK_CASES: `amount ‹ARABIC NUMBER SIGN›1000 USD` (знак над ASCII-цифрами) ALARM; `verse ‹END OF AYAH› ok` (сирота) ALARM; `base‹ANCHOR›hidden ruby` (нет terminator) ALARM; `a‹SEPARATOR›b` (сиротский separator) ALARM; `glyph ‹BEGIN SEGMENT›…` (нет end) ALARM; сбалансированный `‹ANCHOR›kana‹TERMINATOR›` WATCH.
GUARD_PRINCIPLE: судить ОБЛАСТЬ, не одно присутствие — марка на своей письменности легитимна, марка на чужом/ASCII контенте или сломанная скобка это атака; interlinear annotation свидетель даже сбалансированная; никогда не вырезать марку, скоупящую настоящий контент.

**8. ADVERSARIAL_COVERAGE — RUN_CARD SEED.** арабский/кайтхи number sign над ASCII-цифрами, над буквами, над метасимволом, осиротелый в конце; несбалансированная и вложенная interlinear annotation; сиротский separator; несбалансированный египетский сегмент; легит арабо-цифровые и египетско-сегментные кейсы (должны остаться OK); каждый кейс ТАКЖЕ доставлен entity/percent-кодированным (путь pre-pass). MODEL_FAMILY_DIVERSITY_REQUIRED: YES.

**9. MUTATION_CHECK.** литеральная марка ↔ `&#N;` ↔ байтовая форма `%XX`; in-scope vs. wrong-scope; сбалансированная vs. скобка с ошибкой на единицу. INVARIANT: после канонизации один вердикт; in-script область остаётся OK, неправильная область / дисбаланс остаётся ALARM, сбалансированная аннотация остаётся WITNESS во всех формах.

**10. KNOWN_OPEN_QUESTIONS.** Q1: полная модель области prepended-concatenation-mark — сколько следующих цифр марка легитимно обрамляет, чтобы слишком-длинная область ловилась даже над цифрами своей письменности. Q2: грамматика вложенной аннотации (порядок и вложенность anchor/separator/terminator), помимо использованного здесь баланса-по-счёту. Q3: относятся ли U+13439–1343F (зарезервированный египетский формат) сюда или в RESERVED_IGNORABLE (они Cf-смежные зарезервированные, не default-ignorable).

**11. PATCH_HISTORY.** v0_1 (2026-07-20): первый черновик prepended/enclosing-format КЛАССОВОЙ карточки — Cf-не-DI родственника, объясняющего, почему контур это 138 — в паре с `prepended_format_cards.py`. Не прогонялся через конвейер.

**12. LIMITATION_STATEMENT.** (1) WORKING_DRAFT / NOT_CONVEYOR_RUN. (2) Область PCM проверяется на один символ вперёд (следующий ли символ цифра/буква своей письменности), не весь пролёт числа (Q1). (3) Баланс аннотации это проверка счёта, не грамматики (вложенность/порядок) (Q2). (4) Зарезервированный египетский формат (13439–1343F) здесь не владеется (Q3). (5) Entity/percent-доставленные марки ловятся только С pre-pass впереди.

**13. INTEGRATION_INTERFACE_STATUS.** INTEGRATION_STATUS: PROTOTYPED (сырой). RAW_PROTOTYPE: `prepended_format_cards.py::prepended_format_cards_reader(text) -> Finding`. HARNESS: `range_prepended.py`. ЖИВОЙ РЕЗУЛЬТАТ (настоящий MSL + все 6 невидимых осей + 3 хвостовые карточки как база): **scope-abuse/дисбаланс 0/5 (0%) → 5/5 (100%), легит in-script 3/3 → 3/3, 0 новых FP**; сбалансированная interlinear annotation держится на WATCH (свидетель не-для-обмена). ТРЕБУЕТСЯ для закрытия: полная модель области PCM (Q1); грамматика аннотации (Q2); решение по зарезервированному египетскому (Q3); pre-pass впереди; конвейер-ревью.

> КАК РАБОТАЕТ СЫРОЙ ПРОТОТИП: `MSL_MIP_HOME=/path/to/msl_mip python code/range/range_prepended.py` сканирует кейсы scope-abuse и дисбаланса скобок, кейс-свидетель аннотации и легит in-script контент BEFORE (MSL + все невидимые оси + хвост) и AFTER (+ эта prepended-format ось), печатая вердикт до/после по кейсу, ярус WITNESS и итоги.
