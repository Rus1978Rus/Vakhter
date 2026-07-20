# Architecture: the card library and its two faces · Архитектура: библиотека карточек и два её лица

AUTHOR / АВТОР: Руслан Малявский · STATUS / СТАТУС: `WORKING FRAME` · 2026-07-20

🇬🇧 [English](#english) · 🇷🇺 [Русский](#русский)

---

<a name="english"></a>
## English

### The framing (fixed)

Sign cards are **records in a library**, queried like SQL.

| SQL world | here |
|---|---|
| table / rows | the sign-card library |
| `SELECT` | MSL reads a sign → fetches its card → "what does this sign do here" |
| query engine | the MSL engine |
| **admin plane** (INSERT/UPDATE, permissions, audit, constraints) | the governance layer: signing, m-of-n quorum, transparency log, integrity + provenance gates |

A database has **two faces**:
- **User face** — read-only queries. The user sends text and asks "is this sign dangerous?". They READ the library; they never change it.
- **Admin face** — add / change / close a card, permissions, change log. Rare, privileged, locked down. Everything built in component checks #1–#6 is this face.

The admin face is deliberately heavy: changing the library is more dangerous than reading it. The ordinary user never sees it.

### Security note — injection at query time (to think about / not yet built)

Concern (Руслан): at the moment of a QUERY, can a threat be injected? This is the SAME injection family the tool itself detects — now aimed at our OWN lookup path. The attacker controls the input (the signs being looked up).

Principle: **at the boundary where attacker input meets the library, keep DATA as DATA.** Never let input choose or alter the query STRUCTURE.

Vectors to watch:

1. **Lookup key built from input (classic injection).** If the card is fetched by building a query string from the input sign, an attacker crafts input that changes the query — SQL injection against our own card store.
   - Defense: parameterize. Key cards by **exact codepoint** (a number, not a string). A codepoint cannot carry query structure.
   - Status: the current runtime looks cards up by codepoint in a dict → naturally safe. The risk appears only if the library becomes a real SQL store and queries are string-built. Keep it parameterized then.

2. **File/path lookup (traversal).** If a card were a file named after the sign, `../` or NUL in the key → traversal / wrong-card fetch.
   - Defense: never use raw input as a filename; key by codepoint-hex; validate charset.

3. **Output echo (present — TESTED & MITIGATED, check #7).** The guard's own finding reason echoes snippets of attacker input. Confirmed empirically: the confusable card echoed **raw ANSI escapes** into the reason (would hijack an admin terminal). Fixed: `report.safe_view()` sanitizes at the display boundary — control chars (incl. ANSI ESC) → visible inert escapes, HTML metacharacters → entities, length capped. `range_query_injection.py`: live payload in RAW output 1/5 → in SAFE output **0/5**. Rule: never show or log `finding.reason` raw; always pass it through `safe_view()` first.

4. **Second-order.** Input stored (transparency log, cache) then re-read and processed unsafely later.
   - Defense: stored input is DATA on write AND on read; never executed.

What already protects the query path:
- cards are **author-signed** (provenance) → an attacker cannot inject a card at query time;
- **fail-closed** → a lookup error blocks, never passes;
- **DoS gate** → a flood at query time is bounced before lookup.

One-liner: don't let the input pick or shape the query, and treat the guard's own answer as untrusted too.

---

<a name="русский"></a>
## Русский

### Рамка (зафиксирована)

Карточки знаков — это **записи в библиотеке**, к которым обращаются как к SQL.

| мир SQL | здесь |
|---|---|
| таблица / строки | библиотека карточек знаков |
| `SELECT` | MSL читает знак → достаёт его карточку → «что этот знак делает здесь» |
| движок запросов | движок MSL |
| **админ-плоскость** (INSERT/UPDATE, права, аудит, ограничения) | слой управления: подпись, кворум m-of-n, transparency-лог, воротца integrity + provenance |

У базы данных **два лица**:
- **Лицо пользователя** — только чтение. Пользователь присылает текст и спрашивает «опасен ли этот знак?». Он ЧИТАЕТ библиотеку; он её не меняет.
- **Лицо администратора** — добавить / изменить / закрыть карточку, права, журнал изменений. Редко, привилегированно, под замком. Всё, что построено в проверках компонентов #1–#6, — это оно.

Админ-лицо намеренно тяжёлое: менять библиотеку опаснее, чем читать. Обычный пользователь его никогда не видит.

### Заметка по безопасности — инъекция во время запроса (обдумать / ещё не построено)

Опасение (Руслан): в момент ЗАПРОСА можно ли вставить угрозу? Это ТО ЖЕ семейство инъекций, которое инструмент сам детектирует, — теперь нацеленное на наш СОБСТВЕННЫЙ путь поиска. Атакующий контролирует вход (знаки, которые ищутся).

Принцип: **на границе, где вход атакующего встречает библиотеку, держи ДАННЫЕ как ДАННЫЕ.** Никогда не позволяй входу выбирать или менять СТРУКТУРУ запроса.

Векторы под наблюдение:

1. **Ключ поиска, построенный из входа (классическая инъекция).** Если карточка достаётся сборкой строки-запроса из входного знака, атакующий подбирает вход, меняющий запрос, — SQL-инъекция против нашего же хранилища карточек.
   - Защита: параметризуй. Ключуй карточки по **точному кодпоинту** (число, не строка). Кодпоинт не может нести структуру запроса.
   - Статус: текущий рантайм ищет карточки по кодпоинту в словаре → безопасно по природе. Риск появляется только если библиотека станет настоящим SQL-хранилищем со строковой сборкой запросов. Тогда — держать параметризацию.

2. **Поиск по файлу/пути (traversal).** Если бы карточка была файлом с именем-знаком, `../` или NUL в ключе → traversal / выборка не той карточки.
   - Защита: никогда не использовать сырой вход как имя файла; ключевать по codepoint-hex; валидировать набор символов.

3. **Эхо вывода (есть — ПРОВЕРЕНО И СНЯТО, проверка #7).** Собственный `finding.reason` вахтёра эхом выдаёт куски входа атакующего. Подтверждено эмпирически: карточка двойников выдавала в отчёт **сырые ANSI-escape** (захватили бы терминал админа). Починка: `report.safe_view()` санирует на границе показа — управляющие символы (вкл. ANSI ESC) → видимые инертные escape, HTML-метасимволы → entities, длина ограничена. `range_query_injection.py`: живой payload в СЫРОМ выводе 1/5 → в БЕЗОПАСНОМ выводе **0/5**. Правило: никогда не показывать и не логировать `finding.reason` сырым; всегда сперва через `safe_view()`.

4. **Второго порядка.** Вход сохранён (transparency-лог, кэш), затем перечитан и небезопасно обработан позже.
   - Защита: сохранённый вход — это ДАННЫЕ и на запись, И на чтение; никогда не исполняется.

Что уже защищает путь запроса:
- карточки **подписаны автором** (провенанс) → атакующий не может вставить карточку во время запроса;
- **fail-closed** → ошибка поиска блокирует, никогда не пропускает;
- **DoS-гейт** → флуд во время запроса отбивается до поиска.

Одной строкой: не давай входу выбирать или формировать запрос — и считай собственный ответ вахтёра тоже недоверенным.
