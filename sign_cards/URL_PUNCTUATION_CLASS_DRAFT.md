PRIVATE AUTHORIAL PROJECT / ЧАСТНЫЙ АВТОРСКИЙ ПРОЕКТ · COMMERCIAL USE PROHIBITED

# SIGN CORE CARD — URL-PUNCTUATION CLASS (dot / slash / at / colon) (class card, DRAFT)

DOCUMENT_ID: SIGN_CORE_CARD_URL_PUNCTUATION_CLASS_GEN3_v0_1 · DOCUMENT_TYPE: SIGN_CORE_CARD · TEMPLATE_LINE: GEN3_v0_3
STATUS: WORKING_DRAFT / NOT_LOCKED / NOT_RUNTIME / NOT_VALIDATOR / NOT_PRODUCTION / NOT_CONVEYOR_RUN
PRIORITY_TIER: P0 (visible-deception axis) · RAW_PROTOTYPE: `code/range/urlpunct_cards.py` · HARNESS: `code/range/range_urlpunct.py`
SCOPE: the URL-structural punctuation family — dot `.`, slash `/`, at `@`, colon `:` — their non-ASCII look-alikes, and real-ASCII deceptive structure. Builds on the MSL/MIP legacy per-sign cards DOT U+002E, SOLIDUS U+002F, AT U+0040 (ARTIFACT_CONFIRMED line). Confusable LETTERS are a sibling card (CONFUSABLE_CLASS).

🇬🇧 [English](#english) · 🇷🇺 [Русский](#русский)

---

<a name="english"></a>
## English

DRAFT_NOTE (2026-07-20): the CLASS card for the URL-structural punctuation used to deceive — dot / slash / at / colon. It CONSOLIDATES the proven MSL/MIP legacy per-sign cards (DOT, SOLIDUS scheme-patch, AT userinfo model) into one visible-deception class card. Governing law: **PUNCT_FORM ≠ URL_STRUCTURE_PROOF** — the danger is not the ASCII punctuation (it is everywhere in prose) but (a) a LOOK-ALIKE that renders like a delimiter yet is a different codepoint (IDN resolvers normalize `google。com` → `google.com`), and (b) real ASCII punctuation in a deceptive position (the `@` userinfo trick). The ASCII **dot** is the shared pivot with the future numeric/IP card — this card owns the dot FAMILY; numeric will reuse the ASCII dot for `1.0.0.1`-style segmentation. WORKING_DRAFT, NON-CONVEYOR.

**0. UNIVERSALITY.** BOUND_TO_SPECIFIC_SIGN: CLASS (URL-structural punctuation + look-alikes) · AFTER_USE_RESIDUE: FORBIDDEN · SIGN_DATA_IS_SESSION_ONLY: YES

**1. COMMON_CONVEYOR_DISCIPLINE.** v0_3 · RUN_CARD_REQUIRED_BEFORE_LOCK: YES · MODEL_FAMILY_DIVERSITY_REQUIRED: YES · ADVERSARIAL_EVIDENCE_REQUIRED: YES · MUTATION_CHECK_REQUIRED: YES · LIMITATION_STATEMENT_REQUIRED: YES. TRACKER: WORKING_DRAFT YES; PREFLIGHT PENDING; CONVEYOR_REVIEW PENDING; WORKINGLY_CLOSED NO.

**2. META.** ZONE: ZONE_1. WHY_THIS_SIGN_MATTERS: the dot/slash/at/colon are the delimiters that decide what a URL MEANS — where the host ends, where userinfo ends, where the scheme ends. Bend a delimiter and the human reads one destination while the resolver dials another: `google。com` (ideographic dot normalizes to `.`), `paypal.com@evil.ru` (everything before `@` is userinfo, real host is `evil.ru`). The MSL/MIP legacy proved the model — DOT RISK_CASE_002 (`paypal.com.security-check.ru`), SOLIDUS `://`-scheme vs `//`-traversal, AT scheme-aware userinfo — and it proved the legit EXCEPTIONS that keep false positives down (email, federated handle, clean URL, CJK prose). INTERACTS_WITH: CONFUSABLE_CLASS (letter look-alikes — same LOOKS_SAME ≠ IS_SAME law, sibling axis), METACHAR_CLASS (`/ @ : ` as operator-face), the FUTURE numeric/IP card (shares the ASCII dot), CANONICALIZATION_PRE_PASS (a look-alike can arrive percent/entity-encoded / punycode).

**3. REQUIRED_GENERAL_GUARDS.** RAW_SIGN_INPUT_STATUS: DATA_ONLY · NO_EXECUTION_FROM_SIGN: YES · NO_TRUST_FROM_SIGN: YES · DECODE_BEFORE_TRUST: YES · JUDGE_STRUCTURE_NOT_PRESENCE: YES (a dot in prose is fine) · SCHEME_PRESENCE → URL_CONTEXT_MODE: YES (from the legacy SOLIDUS patch — scheme raises scrutiny, never lowers).

**4. SIGN IDENTITY — LAYER_A (LOCK: PERMANENT).** BASE_MODE: DATA_ONLY_DELIMITER · BASE_MODE_FORMULA: PUNCT_FORM ≠ URL_STRUCTURE_PROOF ; DELIMITER_LOOKALIKE ≠ ASCII_DELIMITER ; SCHEME_SEPARATOR ≠ DOUBLE_SOLIDUS_ATTACK.

| Delimiter | ASCII | Look-alikes (→ ASCII) | Priority | Attack mechanism | Legitimate use (stays OK) |
|---|---|---|---|---|---|
| dot | U+002E | 。U+3002 ．U+FF0E ｡U+FF61 ․U+2024 ‧U+2027 (·U+00B7 MED) | HIGH | host/domain spoof; IDN normalizes to `.` | sentence/decimal/version/extension dot; CJK 。 in prose |
| slash | U+002F | ／U+FF0F ∕U+2215 ⁄U+2044 | HIGH | path/host separator spoof; `//` traversal | `://` scheme, path `/` |
| at | U+0040 | ＠U+FF20 ﹫U+FE6B | HIGH | userinfo redirect (`host@realhost`) | email local@host; federated `@user@server` |
| colon | U+003A | ：U+FF1A ∶U+2236 ꞉U+A789 | MED | scheme/port confusion | `http:` scheme, `time:` prose, CJK ： |

WHAT_THIS_SIGN_IS_NOT: (1) NOT_STRUCTURE_BY_PRESENCE — a dot is not a domain boundary, an `@` is not always userinfo; (2) NOT_ATTACK_IN_PROSE — sentence dots, emails, version numbers are OK; (3) NOT_FINAL_SURFACE — a look-alike may arrive percent/entity-encoded or as punycode and must be decoded first.
BASE_FORMULAS: DELIMITER_LOOKALIKE_IN_HOST = SPOOF ; USERINFO_SPOOF = DOTTED_DOMAIN@HOST ; SCHEME_SEPARATOR(`://`) = URL_CONTEXT (not an attack) ; DOUBLE_SLASH_NO_SCHEME = TRAVERSAL_CANDIDATE.

**5. SEMANTIC_EPOCH_TRACKER (LOCK: REVIEWABLE).** EPOCH_TRACKER: NOT_APPLICABLE for the class — these delimiters have parallel functions (prose vs. URL) that co-exist, not epochs. But the ATTACK surface grew with IDN and URL-embedding contexts; browsers normalize look-alikes and display userinfo warnings, back-ends often still compare raw. NOTE: BROWSER_NORMALIZATION ≠ BACKEND_NORMALIZATION.

**6. EFFECT_FIELDS — LAYER_C (LOCK: SESSION).** authority / trust / verification / proof / execution / permission / status / role_assignment / runtime / existence effect: all NONE. EFFECT_FIELDS_ALL_NONE: YES · CLOSED_SCHEMA: YES.

**7. SAFE / RISK / GUARDS — LAYER_B (LOCK: REVIEWABLE).**
- ALARM (conclusive): a dot/slash/at/colon LOOK-ALIKE glued between Latin/ASCII host chars (`google。com`, `admin＠host.com`) — shows the ASCII skeleton; an AT USERINFO spoof — `LEFT@RIGHT` where LEFT is already a dotted domain and the context is URL-ish (`paypal.com@evil.ru`).
- OK (clean): prose punctuation (`End of sentence.`, `version 2.5.1`, `report.pdf`); a plain email (`ivan@example.com` — local part has no dot); a federated handle (`@user@mastodon.social`); a clean URL (`http://example.com/page`); CJK prose (`文です。次の文`).
SAFE_CASES (from the legacy cards, must stay OK): DOT — `3.14`, `document.pdf`, `version 2.5.1`, `Please wait...`; AT — `ivan@example.com`, `@user@mastodon.social`; SOLIDUS — `http://example.com/page`.
RISK_CASES: `google。com` / `google．com` (dot look-alike) ALARM → `google.com`; `admin＠host.com` (at look-alike) ALARM; `paypal.com@evil.ru` (userinfo) ALARM; `evil.com／／bank.com` (slash look-alike) ALARM. (Open: `paypal.com.security-check.ru` subdomain-position spoof — see Q1.)
GUARD_PRINCIPLE: judge URL STRUCTURE, not mere presence; a look-alike delimiter in a host is a spoof (show the ASCII skeleton); `@` is userinfo only when the left side is itself a dotted domain (keeps email/federated OK); `://` sets URL-context (raises scrutiny, never lowers).

**8. ADVERSARIAL_COVERAGE — RUN_CARD SEED.** each delimiter look-alike in a host; one vs. several substitutions; userinfo with and without a scheme; `//` with vs. without a scheme; the legit exceptions (email, federated handle, clean URL, CJK prose, version/extension dots) must stay OK; every case ALSO percent/entity-encoded / punycode (pre-pass path). MODEL_FAMILY_DIVERSITY_REQUIRED: YES.

**9. MUTATION_CHECK.** literal look-alike ↔ `%XX` / `&#N;` ↔ punycode; delimiter at host boundary vs. in prose; `@` with dotted vs. plain left part. INVARIANT: after canonicalization one verdict; a host look-alike / userinfo spoof stays ALARM, prose/email/clean-URL stays OK across all forms.

**10. KNOWN_OPEN_QUESTIONS.** Q1: the subdomain-position spoof (`brand.com.attacker.tld`, DOT legacy RISK_CASE_002) — needs a registrable-domain / brand model, not just a look-alike check. Q2: the `://`-scheme / `//`-traversal branch from the legacy SOLIDUS scheme-patch (scheme → URL_CONTEXT, `//` no-scheme → traversal candidate) — carry it in fully with scheme validation (RFC 3986 §3.1). Q3: the SHARED-DOT handoff to the numeric/IP card — the ASCII dot in `1.0.0.1` / `1.92.168.1.1` (DOT legacy RISK_CASE_006) is where this card meets the numeric axis. Q4: colon port/scheme confusion and the `..`/`../../../` traversal sequences (DOT legacy SEQUENCE_LAYER).

**11. PATCH_HISTORY.** v0_1 (2026-07-20): first draft of the URL-punctuation CLASS card — consolidates the legacy DOT/SOLIDUS/AT model into a visible-deception class card (look-alike delimiters + scheme-aware userinfo), paired with `urlpunct_cards.py`. Not conveyor-run.

**12. LIMITATION_STATEMENT.** (1) WORKING_DRAFT / NOT_CONVEYOR_RUN. (2) Covers look-alike delimiters + at-userinfo; the subdomain-position spoof (Q1), the full `//`-scheme branch (Q2), and the traversal sequences (Q4) are open. (3) The dot look-alike list is the high-value subset, not the full confusables table. (4) Userinfo uses a dotted-left-part heuristic; an exotic legit `a.b@host` (rare) could flag — acceptable for a draft. (5) Percent/punycode-delivered look-alikes need the pre-pass in front.

**13. INTEGRATION_INTERFACE_STATUS.** INTEGRATION_STATUS: PROTOTYPED (raw). RAW_PROTOTYPE: `urlpunct_cards.py::urlpunct_cards_reader(text) -> Finding`. HARNESS: `range_urlpunct.py`. LIVE RESULT (real MSL + supplement + digit + metachar + confusable as baseline): **url-punct spoofs 2/6 (33%) → 6/6 (100%), legit cases 5/5 → 5/5, 0 new FP** — the added catches are the dot/at look-alikes and the no-scheme userinfo the baseline misses; every legacy-proven exception (email, federated handle, clean URL, CJK prose, version dots) stays OK. REQUIRES for closing: subdomain-position model (Q1); full scheme branch (Q2); numeric-dot handoff (Q3); pre-pass in front; conveyor review.

> HOW THE RAW PROTOTYPE WORKS: `MSL_MIP_HOME=/path/to/msl_mip python code/range/range_urlpunct.py` scans delimiter-look-alike and userinfo spoofs plus the legacy legit exceptions BEFORE (MSL baseline) and AFTER (+ this url-punct card), printing the before/after verdict per case plus totals; email, federated handle, clean URL and CJK prose stay OK.

---

<a name="русский"></a>
## Русский

DRAFT_NOTE (2026-07-20): КЛАССОВАЯ карточка URL-структурной пунктуации, используемой для обмана — точка / слэш / at / двоеточие. КОНСОЛИДИРУЕТ проверенные легаси-карточки MSL/MIP по знакам (DOT, SOLIDUS scheme-patch, AT userinfo-модель) в одну карточку видимого обмана. Управляющий закон: **PUNCT_FORM ≠ ДОКАЗАТЕЛЬСТВО_URL_СТРУКТУРЫ** — опасность не в ASCII-пунктуации (она повсюду в прозе), а в (а) ДВОЙНИКЕ, который рисуется как разделитель, но это другой кодпоинт (IDN-резолверы нормализуют `google。com` → `google.com`), и (б) настоящей ASCII-пунктуации в обманной позиции (трюк userinfo с `@`). ASCII-**точка** — общий стержень с будущей числовой/IP-карточкой: эта карточка владеет семейством точки; числовая переиспользует ASCII-точку для сегментации вида `1.0.0.1`. WORKING_DRAFT, БЕЗКОНВЕЙЕРНО.

**0. UNIVERSALITY.** BOUND_TO_SPECIFIC_SIGN: CLASS (URL-структурная пунктуация + двойники) · AFTER_USE_RESIDUE: FORBIDDEN · SIGN_DATA_IS_SESSION_ONLY: YES

**1. COMMON_CONVEYOR_DISCIPLINE.** v0_3 · RUN_CARD_REQUIRED_BEFORE_LOCK: YES · MODEL_FAMILY_DIVERSITY_REQUIRED: YES · ADVERSARIAL_EVIDENCE_REQUIRED: YES · MUTATION_CHECK_REQUIRED: YES · LIMITATION_STATEMENT_REQUIRED: YES. TRACKER: WORKING_DRAFT YES; PREFLIGHT PENDING; CONVEYOR_REVIEW PENDING; WORKINGLY_CLOSED NO.

**2. META.** ZONE: ZONE_1. WHY_THIS_SIGN_MATTERS: точка/слэш/at/двоеточие — разделители, решающие, что URL ЗНАЧИТ: где кончается хост, где userinfo, где схема. Изогни разделитель — и человек читает один адрес, а резолвер набирает другой: `google。com` (идеографическая точка нормализуется в `.`), `paypal.com@evil.ru` (всё до `@` это userinfo, настоящий хост `evil.ru`). Легаси MSL/MIP доказало модель — DOT RISK_CASE_002 (`paypal.com.security-check.ru`), SOLIDUS `://`-схема vs `//`-traversal, AT scheme-aware userinfo — и доказало легит-ИСКЛЮЧЕНИЯ, что держат ложные внизу (почта, федеративный хэндл, чистый URL, CJK-проза). INTERACTS_WITH: CONFUSABLE_CLASS (буквы-двойники — тот же закон ВЫГЛЯДИТ_ОДИНАКОВО ≠ ОДНО_И_ТО_ЖЕ, родственная ось), METACHAR_CLASS (`/ @ : ` как operator-face), БУДУЩАЯ числовая/IP-карточка (общая ASCII-точка), CANONICALIZATION_PRE_PASS (двойник может прийти percent/entity-кодированным / punycode).

**3. REQUIRED_GENERAL_GUARDS.** RAW_SIGN_INPUT_STATUS: DATA_ONLY · NO_EXECUTION_FROM_SIGN: YES · NO_TRUST_FROM_SIGN: YES · DECODE_BEFORE_TRUST: YES · JUDGE_STRUCTURE_NOT_PRESENCE: YES (точка в прозе — норма) · SCHEME_PRESENCE → URL_CONTEXT_MODE: YES (из легаси SOLIDUS-патча — схема повышает scrutiny, не понижает).

**4. SIGN IDENTITY — LAYER_A (LOCK: PERMANENT).** BASE_MODE: DATA_ONLY_DELIMITER · BASE_MODE_FORMULA: PUNCT_FORM ≠ ДОКАЗАТЕЛЬСТВО_URL_СТРУКТУРЫ ; DELIMITER_LOOKALIKE ≠ ASCII_DELIMITER ; SCHEME_SEPARATOR ≠ DOUBLE_SOLIDUS_ATTACK.

| Разделитель | ASCII | Двойники (→ ASCII) | Приоритет | Механизм атаки | Легит-применение (остаётся OK) |
|---|---|---|---|---|---|
| точка | U+002E | 。U+3002 ．U+FF0E ｡U+FF61 ․U+2024 ‧U+2027 (·U+00B7 СРЕД) | ВЫСОКИЙ | спуф хоста/домена; IDN нормализует в `.` | точка предложения/десятичная/версия/расширение; CJK 。 в прозе |
| слэш | U+002F | ／U+FF0F ∕U+2215 ⁄U+2044 | ВЫСОКИЙ | спуф разделителя пути/хоста; `//` traversal | схема `://`, путь `/` |
| at | U+0040 | ＠U+FF20 ﹫U+FE6B | ВЫСОКИЙ | userinfo-редирект (`host@realhost`) | почта local@host; федеративный `@user@server` |
| двоеточие | U+003A | ：U+FF1A ∶U+2236 ꞉U+A789 | СРЕД. | путаница схемы/порта | схема `http:`, `time:` в прозе, CJK ： |

WHAT_THIS_SIGN_IS_NOT: (1) NOT_STRUCTURE_BY_PRESENCE — точка не граница домена, `@` не всегда userinfo; (2) NOT_ATTACK_IN_PROSE — точки предложений, почта, номера версий это OK; (3) NOT_FINAL_SURFACE — двойник может прийти percent/entity-кодированным или punycode, сперва декод.
BASE_FORMULAS: DELIMITER_LOOKALIKE_IN_HOST = СПУФ ; USERINFO_SPOOF = DOTTED_DOMAIN@HOST ; SCHEME_SEPARATOR(`://`) = URL_CONTEXT (не атака) ; DOUBLE_SLASH_NO_SCHEME = КАНДИДАТ_TRAVERSAL.

**5. SEMANTIC_EPOCH_TRACKER (LOCK: REVIEWABLE).** EPOCH_TRACKER: NOT_APPLICABLE для класса — у разделителей параллельные функции (проза vs. URL), сосуществующие, не эпохи. Но поверхность АТАКИ выросла с IDN и контекстами встраивания URL; браузеры нормализуют двойников и предупреждают о userinfo, бэкенды часто сравнивают сырое. NOTE: НОРМАЛИЗАЦИЯ_БРАУЗЕРА ≠ НОРМАЛИЗАЦИЯ_БЭКЕНДА.

**6. EFFECT_FIELDS — LAYER_C (LOCK: SESSION).** authority / trust / verification / proof / execution / permission / status / role_assignment / runtime / existence effect: всё NONE. EFFECT_FIELDS_ALL_NONE: YES · CLOSED_SCHEMA: YES.

**7. SAFE / RISK / GUARDS — LAYER_B (LOCK: REVIEWABLE).**
- ALARM (conclusive): двойник точки/слэша/at/двоеточия, вклиненный между Latin/ASCII хост-символами (`google。com`, `admin＠host.com`) — показан ASCII-скелет; AT USERINFO-спуф — `LEFT@RIGHT`, где LEFT уже точечный домен и контекст URL-подобный (`paypal.com@evil.ru`).
- OK (чистое): пунктуация прозы (`End of sentence.`, `version 2.5.1`, `report.pdf`); обычная почта (`ivan@example.com` — в локальной части нет точки); федеративный хэндл (`@user@mastodon.social`); чистый URL (`http://example.com/page`); CJK-проза (`文です。次の文`).
SAFE_CASES (из легаси-карточек, должны остаться OK): DOT — `3.14`, `document.pdf`, `version 2.5.1`, `Please wait...`; AT — `ivan@example.com`, `@user@mastodon.social`; SOLIDUS — `http://example.com/page`.
RISK_CASES: `google。com` / `google．com` (двойник точки) ALARM → `google.com`; `admin＠host.com` (двойник at) ALARM; `paypal.com@evil.ru` (userinfo) ALARM; `evil.com／／bank.com` (двойник слэша) ALARM. (Открыто: `paypal.com.security-check.ru` спуф позицией поддомена — см. Q1.)
GUARD_PRINCIPLE: судить URL-СТРУКТУРУ, не одно присутствие; двойник-разделитель в хосте это спуф (показать ASCII-скелет); `@` это userinfo лишь когда левая сторона сама точечный домен (держит почту/федеративный OK); `://` задаёт URL-контекст (повышает scrutiny, не понижает).

**8. ADVERSARIAL_COVERAGE — RUN_CARD SEED.** каждый двойник-разделитель в хосте; одна vs. несколько подмен; userinfo со схемой и без; `//` со схемой и без; легит-исключения (почта, федеративный хэндл, чистый URL, CJK-проза, точки версии/расширения) должны остаться OK; каждый кейс ТАКЖЕ percent/entity-кодированный / punycode (путь pre-pass). MODEL_FAMILY_DIVERSITY_REQUIRED: YES.

**9. MUTATION_CHECK.** литеральный двойник ↔ `%XX` / `&#N;` ↔ punycode; разделитель на границе хоста vs. в прозе; `@` с точечной vs. простой левой частью. INVARIANT: после канонизации один вердикт; двойник в хосте / userinfo-спуф остаётся ALARM, проза/почта/чистый-URL остаётся OK во всех формах.

**10. KNOWN_OPEN_QUESTIONS.** Q1: спуф позицией поддомена (`brand.com.attacker.tld`, DOT легаси RISK_CASE_002) — нужна модель регистрируемого домена / брендов, не только проверка двойника. Q2: ветка `://`-схема / `//`-traversal из легаси SOLIDUS scheme-patch (схема → URL_CONTEXT, `//` без схемы → кандидат traversal) — внести полностью с валидацией схемы (RFC 3986 §3.1). Q3: передача ОБЩЕЙ-ТОЧКИ числовой/IP-карточке — ASCII-точка в `1.0.0.1` / `1.92.168.1.1` (DOT легаси RISK_CASE_006) — место стыка этой карточки с числовой осью. Q4: путаница порта/схемы двоеточием и последовательности `..`/`../../../` traversal (DOT легаси SEQUENCE_LAYER).

**11. PATCH_HISTORY.** v0_1 (2026-07-20): первый черновик URL-пунктуационной КЛАССОВОЙ карточки — консолидирует легаси-модель DOT/SOLIDUS/AT в карточку видимого обмана (двойники-разделители + scheme-aware userinfo), в паре с `urlpunct_cards.py`. Не прогонялся через конвейер.

**12. LIMITATION_STATEMENT.** (1) WORKING_DRAFT / NOT_CONVEYOR_RUN. (2) Покрывает двойники-разделители + at-userinfo; спуф позицией поддомена (Q1), полная ветка `//`-схемы (Q2) и последовательности traversal (Q4) открыты. (3) Список двойников точки — высокоценное подмножество, не полная таблица confusables. (4) Userinfo использует эвристику точечной-левой-части; экзотический легит `a.b@host` (редко) мог бы флагнуть — приемлемо для черновика. (5) Percent/punycode-доставленные двойники требуют pre-pass впереди.

**13. INTEGRATION_INTERFACE_STATUS.** INTEGRATION_STATUS: PROTOTYPED (сырой). RAW_PROTOTYPE: `urlpunct_cards.py::urlpunct_cards_reader(text) -> Finding`. HARNESS: `range_urlpunct.py`. ЖИВОЙ РЕЗУЛЬТАТ (настоящий MSL + supplement + digit + metachar + confusable как база): **url-punct спуфы 2/6 (33%) → 6/6 (100%), легит-кейсы 5/5 → 5/5, 0 новых FP** — добавленные уловы это двойники точки/at и userinfo-без-схемы, которые база пропускает; каждое легаси-проверенное исключение (почта, федеративный хэндл, чистый URL, CJK-проза, точки версий) остаётся OK. ТРЕБУЕТСЯ для закрытия: модель позиции поддомена (Q1); полная ветка схемы (Q2); стык числовой-точки (Q3); pre-pass впереди; конвейер-ревью.

> КАК РАБОТАЕТ СЫРОЙ ПРОТОТИП: `MSL_MIP_HOME=/path/to/msl_mip python code/range/range_urlpunct.py` сканирует спуфы двойников-разделителей и userinfo плюс легаси легит-исключения BEFORE (база MSL) и AFTER (+ эта url-punct карточка), печатая вердикт до/после по кейсу и итоги; почта, федеративный хэндл, чистый URL и CJK-проза остаются OK.
