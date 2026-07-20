# Coverage Map · Карта охвата

🇬🇧 [English](#english) · 🇷🇺 [Русский](#русский)

---

<a name="english"></a>
## English — what the product catches, by category

Empirical, measured (not claimed). Two columns:

- **BASELINE** = `canonicalize → real MSL → verdict` — the product with *only*
  the real msl_mip cards loaded (the ~"half a percent" of the planned card base).
- **+DRAFTS** = same pipeline **plus the drafted card simulators**
  (supplement checks, digit/IP/confusable cards, metacharacter cards,
  invisible/bidi cards, hardening cards: jndi/ssti, cloud-creds, IPv6/octal IP).
  These are WORKING_DRAFT cards run as code so we can measure them before the
  author's conveyor closes them into msl_mip proper.

Numbers come from six harnesses in `code/range/`:
`range_test.py` (broad), `range_digits.py` (digit/IP/confusable),
`range_meta.py` (metacharacters), `range_bidi.py` (invisible/bidi),
`range_harden.py` (tomorrow's high-severity classes),
`range_context.py` (ERG context layer + threat-regression safety battery).
Re-runnable with `MSL_MIP_HOME` set.

### Summary line

| | BASELINE | +DRAFTS |
|---|---|---|
| broad structural threats | 9/20 (45%) | — |
| digit / IP / confusable threats | 3/14 (21%) | **14/14 (100%)** |
| metacharacter threats | 2/11 (18%) | **11/11 (100%)** |
| invisible / bidi threats | 6/7 (85%) | **7/7 (100%)** |
| benign kept clean (digit set) | 11/11 | 11/11 (0 new FP) |
| benign kept clean (metachar set) | 9/9 | 9/9 (0 new FP) |
| benign kept clean (invisible set) | **5/8** | **8/8 (0 new FP)** |
| hardening classes (jndi/ssti/cloud/ipv6/octal) | 3/15 (20%) | **15/15 (100%)** |
| benign kept clean (hardening set) | 7/10 | 7/10 (0 new FP) |
| residual MSL-core FPs (context layer) | 5 flagged | **5 → OK, 0 threats silenced** |
| natural-language prompt injection | 0/1 | 0/1 — **blind by design** |

> The hardening set's 7/10 benign "clean" is because 3 controls (`${HOME}`,
> `{{ title }}`, `git@github.com`) sit at WATCH — but that WATCH comes from
> **MSL core** (`queue_for_review` on its `{` / `:` / `@` cards), *not* from the
> new cards (new FP: 0). They are the same meaning-gap WATCHes noted at the end.

### By category

**1. Encoding: percent / double-percent / overlong UTF-8 — 100%.**
BASELINE already 100%. The canonicalization pre-pass decodes `%2e`, `%252e`,
`%c0%af` back to the real sign, then MSL reads it — the "double bottom" working:
the carrier is peeled, the sign underneath is judged.
*Missing to raise: add UTF-7, base64-in-URL, mixed double+overlong layering as regression guards.*

**2. Path traversal (`../`, encoded, overlong) — 100%.**
BASELINE 100% (plain, percent, double-enc, overlong all → ALARM).
*Missing: Windows `..\`, UNC `\\host\share`, `....//` collapse variants.*

**3. Invisible / zero-width / bidi — precision fix: benign 5/8 → 8/8, threats 6/7 → 7/7.**
Not a *catch* gap (MSL already witnesses invisibles) but a **precision** gap — and fixing it exposed an adapter bug.
The bug (fixed): on an uncarded invisible, MSL says `pass` + `WITNESS_PRESENT` — an honest "look at this," not a verdict. The adapter (`msl_real.py`) promoted **every** witness to a conclusive ALARM (`conclusive = sev>=3 or witness`), judging on *presence, not context* — it could not tell a Trojan-Source RLO from a legit ❤️ emoji, and blocked both.
The fix: the adapter DELEGATES invisible judgment to a contextual `invisible_cards` layer (a witness is never itself conclusive). That card is the invisible authority — ALARM on a zero-width splitting a *word*, bidi **imbalance** (CVE-2021-42574), tag chars U+E00xx with no flag base, variation-selector carrier run; OK on provable glue (ZWJ between emoji, VS after an emoji base, tag chars after a flag base, balanced bidi); WATCH otherwise. `range_bidi.py`: benign 5/8 → **8/8**, threats 6/7 → **7/7**, 0 new FP.
*Missing to raise: script-specific legit-ZWNJ allowlist (Persian/Indic) → OK instead of WATCH.*

**4. Homoglyph digit-as-letter brand mimicry (`paypa1`, `g00gle`) — 0% → 100%.**
BASELINE 0% (MSL sees valid ASCII letters/digits). Digit cards de-leet each label and match a brand set → ALARM, **0 FP** on `version 1.0.3`, `pi 3.14159`, `iPhone 15`, `H2O`.
*Missing to raise: expand the brand set (~21), edit-distance-1 fuzzy match, per-brand TLD expectations.*

**5. Numeric IP hosts (metadata / private / loopback / decimal / hex / wildcard) — ~20% → 100%.**
BASELINE catches only dotted-private. Digit cards + canon normalize decimal `2130706433` and hex `0x7f000001` to dotted, then classify: link-local `169.254.169.254` → metadata/SSRF, `0` → wildcard, etc. Hardening round adds bracketed IPv6 (`[::1]`, `[fd00::1]`, `[::ffff:169.254.169.254]`) and octal-dotted `0177.0.0.1` → all ALARM. `range_harden` IP cases 0/4 → 4/4, 0 FP.
*Missing to raise: short forms (`127.1`), IPv6 zone-ids.*

**6. Mixed-script confusable (Cyrillic look-alike `раypal.com`) — 0% → 100%.**
BASELINE 0%. Confusable card flags Latin+Cyrillic-lookalike in one domain token.
*Missing to raise: Greek/Armenian look-alikes, full confusables table, whole-script confusable.*

**7. Metacharacters (SQLi, cmdi `` ` `` `|` `;` `$()`, XSS `<>`, null, CRLF) — 18% → 100%.**
Contextual detectors (quote+SQL-operator, backtick+command-word, CRLF+header-name) → 11/11 ALARM, **0 new FP** on `don't`, `a<b`, `` `print()` ``, `a|b`, `<b>` tag. Hardening round adds template/expression injection — `${jndi:…}` (Log4Shell CVE-2021-44228), `{{7*7}}` / `{{config.__class__}}` SSTI, SpEL, ERB — all ALARM, **0 FP** on `${HOME}`, `{{ user.name }}`, `<%= @post.title %>`.
*Missing to raise: LDAP/NoSQL/XPath families; PowerShell cmdlets.*

**8. Sensitive-path & exfiltration intent — supplement + hardening.**
Supplement flags `/etc/passwd`, `id_rsa`, `.env`, and EMAIL/URL + exfil-verb. Hardening adds cloud-credential artifacts (`~/.aws/credentials`, `~/.kube/config`, `.docker/config.json`, `.npmrc`/`.netrc`, `-----BEGIN … PRIVATE KEY-----`) → ALARM; DNS-exfil → WATCH. **0 FP** on `aws` in prose, `git@github.com`.
*Missing to raise: Azure/OCI paths; base32 DNS-exfil labels.*

**9. Natural-language / semantic prompt injection — 0%, BLIND BY DESIGN.**
"Ignore all previous instructions…" is structurally clean text. MSL judges what a *sign* does, not what a *sentence means*. This is the boundary of the tool, not a gap to patch — it belongs to a semantic layer sitting *beside* MSL.

**10. ERG / context layer — precision, not detection (`erg_context`, `range_context`).**
MSL says what a *sign* is; this layer asks whether the FRAME corroborates operational intent. It **only softens**, under a strict contract: acts only on a broad MSL-core verdict (operational cards are immune); softens only inside a benign frame; if a real operational token is also present it softens by at most one notch (ALARM→WATCH), never to OK. `range_context.py` (24-threat battery): FPs cleared, threats still flagged **24/24**, **threats silenced to OK: 0**. Adversarially hardened (check #2): a red-team found a real bypass (a phishing domain wrapped in "is this safe?" cleared 5 threats); fixed so a conclusive verdict is never cleared and phishing shape is recognised → **0 silenced**.
*Missing to raise: rule-based framing, not the full multi-scale ERG; it reduces false positives only.*

**11. Self-defense — the guard's own robustness (`guard.py`, `range_stress.py`).**
A guard you can drown is not a guard. Real DoS found and closed: 10k invisible chars hung it (O(n²) recompute) and 25k `/` took ~15 s (MSL's slash sign). Fixes: the O(n²) in the invisible card; a **self-defense front gate** that bounces floods in <1 ms (oversized → hold; invisible flood >128 → ALARM; single-char flood >40% → ALARM; too many `/` → hold); a wall-clock **time budget** (honest limit: it stops *our* code, MSL swallows the in-process interrupt, so the slow `/` is predict-and-held instead; production needs a worker/subprocess timeout). `range_stress.py`: 13 attacks up to 10M chars — all bounce <10 ms, none hang/crash. Also fixed a **ReDoS** in the DNS-label regex.

### Security posture — component checks at a glance

| # | check | finding | status |
|---|---|---|---|
| 1 | integrators fail-open/closed | SQLi leaked 9 ways when a part crashed | ✅ fail-closed, 0 leaks |
| 2 | ERG adversarial bypass | phishing-in-a-question silenced 5 threats | ✅ 0 silenced |
| 3 | per-card stress | 4 cards had ReDoS (hung) | ✅ all healthy <65 ms |
| 4 | poisoned component | fake integrator/ERG could lower a verdict | ✅ integrity gate + core isolation |
| 5 | malicious author (SIGNED≠SAFE) | valid signature can make a backdoor NATIVE | ✅ behavioral battery rejects it |
| 6 | one key / secret sign-off | a lone author could push a lowering change | ✅ m-of-n + transparency log |
| 7 | query-time injection via output | a card echoed raw ANSI into the admin-facing reason | ✅ safe_view sanitizes, 1/5→0/5 |
| 8 | 5-reviewer conveyor on ERG | 3 CRITICAL + 3 HIGH bypasses cleared to OK by phrasing — missed by check #2 | ✅ denylist removed; mask-and-rescan; 0/7 bypass |

The guard defends the input (detection + DoS), defends itself (fail-closed, per-component isolation), and defends its own supply chain (integrity → provenance → behavior → quorum → transparency). Every number reproduces from `code/range/`.

Full per-check narrative (provenance, behavioral, quorum, transparency detail) is preserved in the git history of this file and in the harness docstrings under `code/range/`.

### Honest false positives still present at BASELINE

Two benign inputs the **real MSL** flags on its own: `"How do I use ../ in a relative import?"` → ALARM; `"In URLs, %2f is the code for a slash"` → WATCH. Plus WATCH-level ones from MSL's own `queue_for_review` cards (`${HOME}`, `{{ title }}`, `git@github.com`). **These are now cleared by the ERG/context layer (point 10) — with a proven 0-threats-silenced safety gate.**

### Reading the map

**MSL baseline is strong exactly where a sign's danger is structural and encoding-carried** (traversal, encoding, bidi), and **blind exactly where danger needs a lookup or a meaning** (which brand does this mimic? is this IP internal? does this sentence intend harm?). The drafted cards close the *lookup* gaps deterministically, with no heavy database, and leave the *meaning* gap to a semantic layer by design.

---

<a name="русский"></a>
## Русский — что продукт ловит, по категориям

Эмпирика, измерено (а не заявлено). Два столбца:

- **BASELINE** = `канонизация → настоящий MSL → вердикт` — продукт с загруженными *только* настоящими карточками msl_mip (те самые «полпроцента» от планируемой базы карточек).
- **+DRAFTS** = тот же конвейер **плюс симуляторы черновых карточек** (доп-проверки, карточки цифр/IP/двойников, метасимволы, невидимки/bidi, hardening: jndi/ssti, cloud-креды, IPv6/octal IP). Это `WORKING_DRAFT`-карточки, запущенные как код, чтобы измерить их **до** того, как конвейер автора закроет их в сам msl_mip.

Цифры — из шести харнессов в `code/range/`: `range_test.py` (широкий), `range_digits.py` (цифры/IP/двойники), `range_meta.py` (метасимволы), `range_bidi.py` (невидимки/bidi), `range_harden.py` (высокосерьёзные классы «на завтра»), `range_context.py` (слой ERG-контекста + батарея регрессии угроз). Воспроизводимо при заданном `MSL_MIP_HOME`.

### Сводка

| | BASELINE | +DRAFTS |
|---|---|---|
| широкие структурные угрозы | 9/20 (45%) | — |
| цифра / IP / двойник | 3/14 (21%) | **14/14 (100%)** |
| метасимволы | 2/11 (18%) | **11/11 (100%)** |
| невидимки / bidi | 6/7 (85%) | **7/7 (100%)** |
| безобидное осталось чистым (цифры) | 11/11 | 11/11 (0 новых FP) |
| безобидное осталось чистым (метасимволы) | 9/9 | 9/9 (0 новых FP) |
| безобидное осталось чистым (невидимки) | **5/8** | **8/8 (0 новых FP)** |
| hardening-классы (jndi/ssti/cloud/ipv6/octal) | 3/15 (20%) | **15/15 (100%)** |
| безобидное осталось чистым (hardening) | 7/10 | 7/10 (0 новых FP) |
| остаточные FP ядра MSL (слой контекста) | 5 помечено | **5 → OK, 0 угроз заглушено** |
| языковая (смысловая) инъекция | 0/1 | 0/1 — **слеп by design** |

> «7/10» безобидного в hardening — потому что 3 контроля (`${HOME}`, `{{ title }}`, `git@github.com`) стоят на WATCH. Но этот WATCH идёт от **ядра MSL** (`queue_for_review` на его карточках `{` / `:` / `@`), а **не** от новых карточек (новых FP: 0). Это те же «смысловые» WATCH-и, отмеченные в конце.

### По категориям

**1. Кодировка: percent / double-percent / overlong-UTF-8 — 100%.**
BASELINE уже 100%. Pre-pass канонизации раскрывает `%2e`, `%252e`, `%c0%af` обратно в настоящий знак, и MSL его читает — «двойное дно» работает: обёртка снята, судим знак под ней.
*Что добавить: UTF-7, base64-в-URL, смешанные double+overlong слои как регресс-стражи.*

**2. Path traversal (`../`, кодированный, overlong) — 100%.**
BASELINE 100% (обычный, percent, double-enc, overlong — все → ALARM).
*Чего нет: Windows `..\`, UNC `\\host\share`, варианты `....//`.*

**3. Невидимки / zero-width / bidi — уточнение точности: безобидное 5/8 → 8/8, угрозы 6/7 → 7/7.**
Это не пробел в *ловле* (MSL и так «свидетельствует» невидимки), а пробел в **точности** — и его починка вскрыла баг адаптера.
Баг (исправлен): на некарточном невидимом MSL говорит `pass` + `WITNESS_PRESENT` — честное «посмотри сюда», а не вердикт. Адаптер (`msl_real.py`) повышал **каждого** свидетеля до блокирующего ALARM (`conclusive = sev>=3 or witness`), судя по *присутствию, а не контексту* — он не отличал Trojan-Source RLO от легального эмодзи ❤️ и блокировал оба.
Починка: адаптер **делегирует** суждение о невидимках контекстному слою `invisible_cards` (свидетель сам по себе никогда не conclusive). Эта карточка — авторитет по невидимкам: ALARM на zero-width, рвущий *слово*, дисбаланс bidi (CVE-2021-42574), tag-символы U+E00xx без флаг-базы, несущая цепочка variation-selector; OK на доказуемом «клее» (ZWJ между эмодзи, VS после эмодзи-базы, tag-символы после флаг-базы, сбалансированный bidi); иначе WATCH. `range_bidi.py`: безобидное 5/8 → **8/8**, угрозы 6/7 → **7/7**, 0 новых FP.
*Что добавить: allowlist легального ZWNJ по системам письма (перс./индик) → OK вместо WATCH.*

**4. Двойник «цифра-как-буква», мимикрия брендов (`paypa1`, `g00gle`) — 0% → 100%.**
BASELINE 0% (MSL видит валидные ASCII-буквы/цифры). Карточки цифр «раз-литят» каждую метку и сверяют с набором брендов → ALARM, **0 FP** на `version 1.0.3`, `pi 3.14159`, `iPhone 15`, `H2O`.
*Что добавить: расширить набор брендов (~21), fuzzy-совпадение на расстоянии 1, ожидания по TLD.*

**5. Числовые IP-хосты (метаданные / приватные / loopback / decimal / hex / wildcard) — ~20% → 100%.**
BASELINE ловит только dotted-private. Карточки цифр + канон нормализуют decimal `2130706433` и hex `0x7f000001` в dotted, затем классифицируют: link-local `169.254.169.254` → метаданные/SSRF, `0` → wildcard и т.д. Hardening добавляет IPv6 в скобках (`[::1]`, `[fd00::1]`, `[::ffff:169.254.169.254]`) и octal `0177.0.0.1` → все ALARM. `range_harden`: IP-кейсы 0/4 → 4/4, 0 FP.
*Что добавить: короткие формы (`127.1`), zone-id IPv6.*

**6. Смешанные скрипты / двойники (кириллический `раypal.com`) — 0% → 100%.**
BASELINE 0%. Карточка двойников флагует латиница+кириллица-двойник в одном домен-токене.
*Что добавить: греческие/армянские двойники, полная таблица confusables, whole-script.*

**7. Метасимволы (SQLi, cmdi `` ` `` `|` `;` `$()`, XSS `<>`, null, CRLF) — 18% → 100%.**
Контекстные детекторы (кавычка+SQL-оператор, backtick+команда, CRLF+имя заголовка) → 11/11 ALARM, **0 новых FP** на `don't`, `a<b`, `` `print()` ``, `a|b`, тег `<b>`. Hardening добавляет инъекцию шаблонов/выражений — `${jndi:…}` (Log4Shell CVE-2021-44228), `{{7*7}}` / `{{config.__class__}}` SSTI, SpEL, ERB — все ALARM, **0 FP** на `${HOME}`, `{{ user.name }}`, `<%= @post.title %>`.
*Что добавить: семейства LDAP/NoSQL/XPath; командлеты PowerShell.*

**8. Чувствительные пути и намерение эксфильтрации — supplement + hardening.**
Supplement флагует `/etc/passwd`, `id_rsa`, `.env`, а также EMAIL/URL + глагол-эксфильтрации. Hardening добавляет облачные креды (`~/.aws/credentials`, `~/.kube/config`, `.docker/config.json`, `.npmrc`/`.netrc`, заголовки `-----BEGIN … PRIVATE KEY-----`) → ALARM; DNS-эксфил → WATCH. **0 FP** на `aws` в тексте, `git@github.com`.
*Что добавить: пути Azure/OCI; base32-метки DNS-эксфила.*

**9. Языковая / смысловая prompt-инъекция — 0%, СЛЕП BY DESIGN.**
«Ignore all previous instructions…» — структурно чистый текст. MSL судит, что делает *знак*, а не что значит *предложение*. Это граница инструмента, а не пробел для латания — это работа смыслового слоя, стоящего *рядом* с MSL.

**10. Слой ERG / контекст — точность, а не детекция (`erg_context`, `range_context`).**
MSL говорит, *что за знак*; этот слой спрашивает, подтверждает ли РАМКА вокруг операционное намерение. Он **только смягчает**, по строгому контракту: действует лишь на широкий вердикт ядра MSL (операционные карточки иммунны); смягчает лишь внутри безобидной рамки; если рядом есть реальный операционный токен — смягчает максимум на одну ступень (ALARM→WATCH), никогда до OK. `range_context.py` (батарея 24 угроз): FP сняты, угрозы по-прежнему флагуются **24/24**, **угроз заглушено до OK: 0**. Проверено на прочность (проверка #2): red-team нашла реальный обход (фишинг-домен в обёртке «это безопасно?» заглушил 5 угроз); починено так, что conclusive-вердикт никогда не сбрасывается и форма фишинга распознаётся → **0 заглушено**.
*Что добавить: это правило-основанная рамка, а не полный многомасштабный ERG; снижает только ложные тревоги.*

**11. Самозащита — стойкость самого вахтёра (`guard.py`, `range_stress.py`).**
Вахтёр, которого можно утопить, — не вахтёр. Найден и закрыт реальный DoS: 10k невидимых символов вешали его (пересчёт O(n²)), а 25k `/` занимали ~15 c (знак-слэш у MSL). Починки: сам O(n²) в карточке невидимок; **передний шлюз самозащиты**, отбивающий флуды за <1 мс (переразмер → hold; флуд невидимок >128 → ALARM; флуд одного символа >40% → ALARM; слишком много `/` → hold); **бюджет по времени** (честная граница: он останавливает *наш* код, а MSL проглатывает внутрипроцессное прерывание, поэтому медленный `/` держится предсказанием; в проде нужен таймаут воркера/подпроцесса). `range_stress.py`: 13 атак до 10M символов — все отбиты <10 мс, ни зависания, ни падения. Также починен **ReDoS** в regex DNS-метки.

### Профиль безопасности — проверки компонентов кратко

| # | проверка | находка | статус |
|---|---|---|---|
| 1 | интеграторы fail-open/closed | SQLi утёк 9 путями при падении части | ✅ fail-closed, 0 утечек |
| 2 | адверсариальный обход ERG | «фишинг-в-вопросе» заглушил 5 угроз | ✅ 0 заглушено |
| 3 | стресс каждой карточки | у 4 карточек был ReDoS (зависали) | ✅ все здоровы <65 мс |
| 4 | отравленный компонент | фейк-интегратор/ERG мог понизить вердикт | ✅ integrity-гейт + изоляция ядра |
| 5 | злонамеренный автор (SIGNED≠SAFE) | валидная подпись делает бэкдор NATIVE | ✅ поведенческая батарея отвергает |
| 6 | один ключ / тайная подпись | одиночный автор мог протолкнуть понижающее | ✅ m-of-n + transparency-лог |
| 7 | инъекция во время запроса через вывод | карточка эхом выдавала сырой ANSI в отчёт админу | ✅ safe_view санирует, 1/5→0/5 |
| 8 | конвейер 5 ревьюеров на ERG | 3 CRITICAL + 3 HIGH обхода прошли до OK формулировкой — пропущены проверкой #2 | ✅ denylist убран; mask-and-rescan; 0/7 обходов |

Вахтёр защищает вход (детекция + DoS), защищает себя (fail-closed, изоляция компонентов) и защищает свою цепочку поставки (integrity → provenance → поведение → кворум → transparency). Каждая цифра воспроизводится из `code/range/`.

Полное подробное описание по каждой проверке (провенанс, поведение, кворум, transparency) сохранено в git-истории этого файла и в докстрингах харнессов под `code/range/`.

### Честные ложные тревоги, ещё живущие на BASELINE

Два безобидных входа, которые **настоящий MSL** флагует сам: `"How do I use ../ in a relative import?"` → ALARM; `"In URLs, %2f is the code for a slash"` → WATCH. Плюс WATCH-и от собственных карточек `queue_for_review` MSL (`${HOME}`, `{{ title }}`, `git@github.com`). **Теперь они снимаются слоем ERG/контекста (пункт 10) — с доказанным гейтом «0 угроз заглушено».**

### Как читать карту

**Baseline MSL силён ровно там, где опасность знака структурна и несётся кодировкой** (traversal, кодировка, bidi), и **слеп ровно там, где опасность требует справочника или смысла** (какой бренд это подделывает? этот IP внутренний? это предложение хочет вреда?). Черновые карточки закрывают *справочные* пробелы детерминированно, без тяжёлой базы, и по замыслу оставляют *смысловой* пробел смысловому слою.
