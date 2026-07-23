# Author decisions — the log · Журнал авторских решений

AUTHOR / АВТОР: Руслан Малявский · STATUS / СТАТУС: `WORKING DOCUMENT` · 2026-07-22

🇬🇧 [English](#english) · 🇷🇺 [Русский](#русский)

---

Every non-obvious choice in this codebase, in one place, with its reason. The
rationale is not invented here — it is consolidated from the detectors' own
docstrings, the commit history, and the cross-review with the **NOTARIUS**
repository (a sibling project: strong provenance cryptography, naive detection —
the mirror image of this one). Where a decision rejects an approach, the reason
it was rejected is recorded so it is not silently re-tried.

Format: **Decision / Rationale / Status**. Status is one of `ADOPTED`,
`REJECTED`, `DEFERRED`.

---

<a name="english"></a>
## English

### Detection — the confusable / homoglyph front

**AD-1 · The core law is LOOKS_SAME ≠ IS_SAME.**
Decision: the confusable detector keys on the *identity* of a codepoint, not its
rendered shape. `paypal.com` and `pаypal.com` render alike; the second carries a
Cyrillic `а` (U+0430).
Rationale: rendering is the attack surface; identity is ground truth.
Status: `ADOPTED` (code/range/confusable_cards.py).

**AD-2 · The signal is script MIX within one token — not "a foreign letter exists".**
Decision: ALARM when a single token mixes Latin with Cyrillic/Greek lookalikes,
not merely because a non-Latin letter is present.
Rationale: "a non-Latin letter exists" would flag all Russian, all Greek — every
native word. The deception is the *mix inside one token*, or a wholly-foreign
token impersonating a known target.
Status: `ADOPTED`.

**AD-3 · A blanket "whole-script, no native anchor → WATCH" rule was rejected.**
Decision: whole-script confusion is gated on a target skeleton (DEMO_TARGETS),
not flagged on its own.
Rationale: simulated, the blanket rule fired on ~25% of common Russian words
(соус, орех, хор …) — legitimate words built from letters that happen to be
Latin lookalikes. Whole-script confusion is only meaningful *relative to a
target*.
Status: `REJECTED` (the blanket rule); target-gating `ADOPTED`.

**AD-4 · Roman-numeral forms are checked BEFORE the ≥2-letter gate.**
Decision: the Roman-numeral and non-ASCII-dash branches run before the
`len(letters) < 2: continue` gate.
Rationale: a Roman-numeral letter-form (e.g. `Ⅼ` U+216C) is Unicode category Nl,
so `_letters()` does not count it. A short token like `ⅬG` (one ASCII letter +
one Roman form) was therefore skipped and slipped through — a real false-negative
(fixed in commit 8deaf9a; pinned by test_confusable::
test_roman_numeral_short_token_regression).
Status: `ADOPTED`.

**AD-5 · A non-ASCII dash is a spoof only inside a domain-like token.**
Decision: a confusable dash (U+2010, U+2011, U+2013 …) ALARMs only when the token
contains a dot; in ordinary prose it stays OK.
Rationale: `pay‐pal.com` is a domain spoof; `a well‐known author` is legitimate
typography. The dot is the domain tell.
Status: `ADOPTED`.

### Detection — the invisible / bidi front

**AD-6 · Invisibles use a three-way verdict: ALARM / OK / WATCH.**
Decision: a proven smuggle ALARMs; provable legit glue is cleared to OK; an
invisible that is neither is WATCHed (non-conclusive).
Rationale: MSL alone flags an uncarded invisible as a witness but cannot tell a
smuggle from emoji glue — that is context, and context is this layer's job.
Status: `ADOPTED` (code/range/invisible_cards.py).

**AD-7 · Legit glue is vouched narrowly; ZWSP/ZWNJ/BOM/WJ/SHY are never auto-vouched.**
Decision: only ZWJ between emoji, one variation selector on a valid base, a tag
char after a flag base, and *balanced* bidi are cleared. The word-splitting
invisibles are never auto-cleared.
Rationale: those five have no legitimate role inside a word, so their presence
there is signal, not glue.
Status: `ADOPTED`.

**AD-8 · Variation selectors are a SEPARATE detector because they are Mn, not Cf.**
Decision: variation selectors get their own branch (vs_cards.py) rather than
riding the invisible detector.
Rationale: they are Unicode general category **Mn (Nonspacing_Mark), not Cf
(Format)**. The usual "strip all format chars" cleanup reflex misses every one of
them — exactly the gap the emoji-variation-selector smuggling technique exploits.
Status: `ADOPTED`.

### Trust core — provenance, quorum, transparency, integrity

**AD-9 · INTEGRITY ≠ PROVENANCE; SIGNED ≠ NATIVE.**
Decision: two distinct layers — a hash answers "did the container change since the
manifest?"; provenance answers "is this element of legitimate origin?".
Rationale: an attacker who swaps a component AND regenerates the manifest passes a
pure-hash check. A valid signature proves *who attested*, not that the text is
native.
Status: `ADOPTED` (provenance.py, integrity.py).

**AD-10 · A lowering change needs an M-of-N quorum.**
Decision: a change to a component that can LOWER a verdict (ERG / integrator)
requires ≥3 distinct authorised signatures; add-only cards need 1.
Rationale: one stolen or malicious key must not be enough to sign a backdoor that
passes the behavioral battery. Closing that is organizational, not cryptographic.
Status: `ADOPTED` (quorum.py).

**AD-11 · The transparency log is hash-chained and takes time from the caller.**
Decision: an append-only log where each entry commits to the previous one; the
timestamp is passed in by the caller.
Rationale: chaining makes silent removal/alteration detectable; caller-supplied
time keeps the log deterministic and reproducible, and chain integrity does not
depend on it.
Status: `ADOPTED` (transparency.py).

**AD-12 · Signing stays HMAC in-repo; Ed25519 is the sanctioned production upgrade — DEFERRED.**
Decision: provenance/quorum sign with HMAC in this repository; the asymmetric
(Ed25519) upgrade is documented but not vendored in.
Rationale: from the NOTARIUS review, its `envelope_v2.py`/`trace.py` show the
real asymmetric path (author signs with a private key; the gate verifies with the
public key), which closes the HMAC symmetry defect. It is **deferred here** for
two concrete reasons: (a) no Ed25519 provider is installed in this environment
(no PyNaCl, no `cryptography`), so vendoring it would add an unrunnable hard
dependency to a security project; (b) provenance and quorum are quorum-protected
lowering components — swapping their signing primitive is itself an M-of-N change
(AD-10), not a drive-by edit. The security property (you cannot mint NATIVE
provenance without the author's key) is identical under both; only key management
differs.
Status: `DEFERRED` (upgrade path recorded; adopt when a crypto provider is present
and under quorum).

### Method — how the project keeps itself honest

**AD-13 · coverage_lock keeps cards and detector tables in sync, both directions, with no generator.**
Decision: a regression lock asserts (A) every detector homoglyph codepoint has a
full EN+RU card and (B) every homoglyph-family card names a codepoint the detector
actually backs.
Rationale: the card spec and the detector tables are two independent sources of
truth; without a bidirectional lock the manual contract drifts silently. A
generator was avoided so neither side becomes derived/second-class.
Status: `ADOPTED` (code/tools/coverage_lock.py).

**AD-14 · A real assert-based test layer was added, adopted from the NOTARIUS review.**
Decision: a standalone test runner (code/tests/) with hard assertions on each
detector's contract — including a behavioral lock on every table codepoint and
the `ⅬG` false-negative regression.
Rationale: the NOTARIUS repo carried 109 real pytest asserts; this project drove
whole scenarios through range_*.py harnesses but pinned no individual contract,
and the `ⅬG` bug lived in exactly that gap. The runner needs no pytest (there is
none in this environment) yet stays pytest-collectable. 27 tests / 221 checks at
adoption.
Status: `ADOPTED` (code/tests/run_tests.py).

**AD-15 · NOTARIUS's custody / carrier / human-fingerprint machinery was reviewed and NOT taken.**
Decision: Shamir M-of-N custody, mortal TTL carriers, heartbeat/death-pulse, and
the PGP-wordlist human fingerprint stay in NOTARIUS.
Rationale: they solve *secret-splitting and key custody*. Vakhter holds no secret
to split and no key for a human to verify; importing them would be scope creep.
The scanner trichotomy NOTARIUS uses (HIGH/MEDIUM/LIKELY_LEGITIMATE) is already
superseded here by the ALARM/OK/WATCH layer (AD-6) plus the Mn insight (AD-8), so
that too was recorded rather than imported.
Status: `REJECTED` (import); recorded for provenance of the decision.

### Detection — prioritisation and the fullwidth carrier

**AD-16 · New confusable/carrier work is prioritised by real-world attack frequency; fullwidth folds in canonicalization.**
Decision: the confusable table is extended by how often a form is actually abused,
not alphabetically. Under that rule Cyrillic к (U+043A) → k was added (the last
common single-substitution Cyrillic look-alike; the mixed-script check already
fires when any foreign letter is a confusable, so the only real gap is a
single-swap token whose one letter is absent). The next-frequency vector,
fullwidth ASCII (U+FF01–FF5E, U+3000), is handled by FOLDING it to ASCII in the
canonicalization pre-pass — not by a new detector.
Rationale: fullwidth is a compatibility CARRIER, not a script mix, so its home is
the "double bottom" pre-pass beside overlong-UTF8: peel the carrier, let the
readers judge the real sign (fullwidth ＜script＞ / IP / ../ now surface). Scope is
kept to the fullwidth ASCII block only — halfwidth katakana (FF61–FF9F), the
fullwidth white brackets (FF5F–FF60) and real CJK are left untouched — so the fold
adds 0 false positives. `м`/`т`/`ь` were considered and REJECTED as confusables:
they are not in UTS #39 and their glyphs are not reliably ASCII-confusable, and a
security table must not assert a look-alike that isn't one.
Status: `ADOPTED` (code/canonicalization/canonicalize.py :: fold_fullwidth;
code/tests/test_fullwidth.py).

---

<a name="русский"></a>
## Русский

Каждый неочевидный выбор в этом коде — в одном месте, с обоснованием. Обоснование
здесь не выдумано: оно сведено из докстрингов самих детекторов, истории коммитов и
кросс-обзора с репозиторием **NOTARIUS** (родственный проект: сильная криптография
провенанса, наивная детекция — зеркало этого). Где решение что-то отвергает,
причина отказа записана, чтобы её не пробовали заново.

Формат: **Решение / Обоснование / Статус**. Статус — `ПРИНЯТО`, `ОТВЕРГНУТО`,
`ОТЛОЖЕНО`.

### Детекция — фронт конфузаблов / гомоглифов

**AD-1 · Основной закон: ВЫГЛЯДИТ_ОДИНАКОВО ≠ ЯВЛЯЕТСЯ_ТЕМ_ЖЕ.**
Решение: детектор смотрит на *идентичность* кодпоинта, а не на нарисованную
форму. `paypal.com` и `pаypal.com` выглядят одинаково; во втором — кириллическая
`а` (U+0430).
Обоснование: рендер — поверхность атаки; идентичность — истина.
Статус: `ПРИНЯТО`.

**AD-2 · Сигнал — СМЕШЕНИЕ письменностей внутри одного токена, а не «есть чужая буква».**
Решение: тревога, когда один токен смешивает латиницу с кирилло/греческими
двойниками, а не просто из-за наличия нелатинской буквы.
Обоснование: правило «есть нелатинская буква» пометило бы весь русский и весь
греческий — каждое родное слово. Обман — это *смесь внутри токена* или целиком
чужой токен, выдающий себя за известную цель.
Статус: `ПРИНЯТО`.

**AD-3 · Огульное «целиком чужой, без родного якоря → WATCH» отвергнуто.**
Решение: путаница целой письменностью срабатывает только по скелету-цели
(DEMO_TARGETS), сама по себе — нет.
Обоснование: в симуляции огульное правило било по ~25% обычных русских слов
(соус, орех, хор …) — законных слов из букв, случайно похожих на латиницу.
Путаница целой письменностью осмысленна лишь *относительно цели*.
Статус: `ОТВЕРГНУТО` (огульное правило); привязка к цели — `ПРИНЯТО`.

**AD-4 · Римские цифры проверяются ДО барьера «≥2 букв».**
Решение: ветки римских цифр и не-ASCII-дефиса идут до барьера
`len(letters) < 2: continue`.
Обоснование: форма римской цифры (напр. `Ⅼ` U+216C) — категория Unicode Nl, и
`_letters()` её не считает. Короткий токен `ⅬG` (одна ASCII-буква + одна римская
форма) поэтому пропускался — реальный ложноотрицательный (починен в 8deaf9a;
закреплён test_confusable::test_roman_numeral_short_token_regression).
Статус: `ПРИНЯТО`.

**AD-5 · Не-ASCII-дефис — подмена только внутри доменоподобного токена.**
Решение: конфузабл-дефис (U+2010, U+2011, U+2013 …) даёт тревогу лишь если в
токене есть точка; в обычной прозе — чисто.
Обоснование: `pay‐pal.com` — подмена домена; `a well‐known author` — законная
типографика. Точка — признак домена.
Статус: `ПРИНЯТО`.

### Детекция — фронт невидимок / bidi

**AD-6 · У невидимок трёхзначный вердикт: ALARM / OK / WATCH.**
Решение: доказанная контрабанда — тревога; доказуемый законный «клей» — чисто;
невидимка, которая ни то ни другое — WATCH (неокончательно).
Обоснование: сам MSL помечает некартированную невидимку как свидетеля, но не
отличает контрабанду от эмодзи-клея — это контекст, а контекст — работа этого
слоя.
Статус: `ПРИНЯТО`.

**AD-7 · Законный клей заверяется узко; ZWSP/ZWNJ/BOM/WJ/SHY не заверяются никогда.**
Решение: чисто только ZWJ между эмодзи, один селектор вариации на валидной базе,
tag-символ после флаг-базы и *сбалансированный* bidi. Невидимки, рвущие слово, не
заверяются автоматически.
Обоснование: у этих пяти нет законной роли внутри слова, поэтому их присутствие
там — сигнал, а не клей.
Статус: `ПРИНЯТО`.

**AD-8 · Селекторы вариаций — ОТДЕЛЬНЫЙ детектор, потому что они Mn, а не Cf.**
Решение: селекторам вариаций дана своя ветка (vs_cards.py), а не общая с
невидимками.
Обоснование: они — категория Unicode **Mn (Nonspacing_Mark), а не Cf (Format)**.
Привычный рефлекс «вырезать все format-символы» пропускает их все — именно ту
щель, что эксплуатирует контрабанда через эмодзи-селекторы.
Статус: `ПРИНЯТО`.

### Ядро доверия — провенанс, кворум, прозрачность, целостность

**AD-9 · ЦЕЛОСТНОСТЬ ≠ ПРОВЕНАНС; ПОДПИСАНО ≠ РОДНОЕ.**
Решение: два разных слоя — хеш отвечает «менялся ли контейнер с момента
манифеста?»; провенанс — «законного ли происхождения элемент?».
Обоснование: атакующий, подменивший компонент И перегенерировавший манифест,
проходит чистую хеш-проверку. Валидная подпись доказывает *кто заверил*, а не что
текст родной.
Статус: `ПРИНЯТО`.

**AD-10 · Понижающее изменение требует кворума M-из-N.**
Решение: изменение компонента, способного ПОНИЗИТЬ вердикт (ERG / интегратор),
требует ≥3 различных авторизованных подписей; add-only карточки — 1.
Обоснование: одного украденного или вредоносного ключа не должно хватать, чтобы
подписать бэкдор, проходящий поведенческую батарею. Это закрывается
организационно, не криптографически.
Статус: `ПРИНЯТО`.

**AD-11 · Лог прозрачности хеш-сцеплен и берёт время у вызывающего.**
Решение: append-only лог, где каждая запись коммитит предыдущую; отметка времени
передаётся вызывающим.
Обоснование: сцепление делает тихое удаление/подмену обнаружимыми; переданное
время держит лог детерминированным и воспроизводимым, а целостность цепи от него
не зависит.
Статус: `ПРИНЯТО`.

**AD-12 · Подпись остаётся HMAC в репозитории; Ed25519 — санкционированный боевой апгрейд — ОТЛОЖЕНО.**
Решение: провенанс/кворум подписывают HMAC в этом репозитории; асимметричный
(Ed25519) апгрейд задокументирован, но не внесён.
Обоснование: из обзора NOTARIUS его `envelope_v2.py`/`trace.py` показывают
реальный асимметричный путь (автор подписывает приватным ключом; шлюз проверяет
публичным), закрывающий дефект симметрии HMAC. Здесь **отложено** по двум
конкретным причинам: (а) в этой среде нет провайдера Ed25519 (ни PyNaCl, ни
`cryptography`), поэтому внесение добавило бы незапускаемую жёсткую зависимость в
security-проект; (б) провенанс и кворум — quorum-защищённые понижающие компоненты,
и смена их примитива подписи сама по себе есть изменение M-из-N (AD-10), а не
мимоходная правка. Свойство безопасности (нельзя выпустить РОДНОЙ провенанс без
ключа автора) идентично в обоих; различается лишь управление ключами.
Статус: `ОТЛОЖЕНО` (путь апгрейда зафиксирован; принять при наличии крипто-
провайдера и под кворумом).

### Метод — как проект держит себя честным

**AD-13 · coverage_lock держит карточки и таблицы детектора в синхроне, в обе стороны, без генератора.**
Решение: регрессионный замок утверждает (A) у каждого гомоглиф-кодпоинта детектора
есть полная пара карточек EN+RU и (B) каждая карточка гомоглиф-семейства называет
кодпоинт, который детектор реально поддерживает.
Обоснование: спецификация карточек и таблицы детектора — два независимых
источника истины; без двунаправленного замка ручной контракт тихо расходится.
Генератор намеренно не заведён, чтобы ни одна сторона не стала производной.
Статус: `ПРИНЯТО` (code/tools/coverage_lock.py).

**AD-14 · Добавлен настоящий тест-слой на ассертах, взятый из обзора NOTARIUS.**
Решение: автономный раннер (code/tests/) с жёсткими ассертами на контракт каждого
детектора — включая поведенческий замок на каждый кодпоинт таблиц и регрессию
ложноотрицательного `ⅬG`.
Обоснование: репозиторий NOTARIUS нёс 109 настоящих pytest-ассертов; этот проект
гонял целые сценарии через range_*.py, но не закреплял отдельный контракт, и баг
`ⅬG` жил ровно в этой щели. Раннер не требует pytest (его в среде нет), но
остаётся собираемым pytest'ом. На момент принятия — 27 тестов / 221 проверка.
Статус: `ПРИНЯТО` (code/tests/run_tests.py).

**AD-15 · Механика NOTARIUS (custody / carrier / человеческий отпечаток) рассмотрена и НЕ взята.**
Решение: Shamir M-из-N, смертные TTL-носители, heartbeat/death-pulse и
человеческий отпечаток по PGP-словарю остаются в NOTARIUS.
Обоснование: они решают *разделение секрета и хранение ключей*. У Вахтёра нет
секрета для разделения и ключа для сверки человеком; их импорт был бы расползанием
рамок. Трихотомию сканера NOTARIUS (HIGH/MEDIUM/LIKELY_LEGITIMATE) здесь уже
превосходит слой ALARM/OK/WATCH (AD-6) плюс инсайт про Mn (AD-8), поэтому и она
записана, а не импортирована.
Статус: `ОТВЕРГНУТО` (импорт); записано для провенанса решения.

### Детекция — приоритизация и полноширинный носитель

**AD-16 · Новая работа по двойникам/носителям приоритизируется по частоте атак в реальной жизни; fullwidth сворачивается в канонизации.**
Решение: таблица конфузаблов расширяется по тому, насколько часто форму реально
эксплуатируют, а не по алфавиту. По этому правилу добавлена кириллическая к
(U+043A) → k (последний ходовой односимвольный кириллический двойник; проверка
смешения письменностей уже срабатывает, если хоть одна чужая буква — конфузабл,
поэтому реальная дыра — только токен с единственной подменой, чья буква
отсутствует в таблице). Следующий по частоте вектор — полноширинный ASCII
(U+FF01–FF5E, U+3000) — закрыт СВОРАЧИВАНИЕМ в ASCII в пре-пассе канонизации, а не
новым детектором.
Обоснование: fullwidth — это компат-НОСИТЕЛЬ, а не смесь письменностей, поэтому
его место в «двойном дне» рядом с overlong-UTF8: снять носитель, дать детекторам
судить настоящий знак (fullwidth ＜script＞ / IP / ../ теперь всплывают). Область
ограничена только блоком fullwidth ASCII — halfwidth-катакана (FF61–FF9F),
полноширинные белые скобки (FF5F–FF60) и настоящий CJK не тронуты — поэтому fold
даёт 0 ложных срабатываний. `м`/`т`/`ь` рассмотрены и ОТВЕРГНУТЫ как конфузаблы:
их нет в UTS #39, а начертание не является надёжно ASCII-двойником; security-
таблица не должна утверждать сходство, которого нет.
Статус: `ПРИНЯТО` (code/canonicalization/canonicalize.py :: fold_fullwidth;
code/tests/test_fullwidth.py).
