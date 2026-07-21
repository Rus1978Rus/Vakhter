# r > g admission filter — when to add code vs. add a card · Фильтр приёма r > g — когда писать код, а когда карточку

AUTHOR / АВТОР: Руслан Малявский · 2026-07-21

PROVENANCE / ПРОВЕНАНС: adapted (not copied) from the read-only msl_mip artifact
`foundation_layer/FOUNDATION_CONCEPT_PIKETTY_R_G_2026-07-17.md`. The r>g framing and
the §5 safeguards originate there; this note maps them onto Vakhter's per-sign cards
and two-gate tooling. msl_mip is a sibling project studied, not edited.

🇬🇧 [English](#english) · 🇷🇺 [Русский](#русский)

---

<a name="english"></a>
## English

### The filter
Piketty's inequality **r > g** repurposed as an architecture-admission rule:

- **g (growth / labour)** — hand-written IF/ELSE, hardcoded attack signatures, per-symbol
  manual review, tables that need manual sync. Linear cost that must be paid forever.
- **r (return on architectural capital)** — the ability of the *existing* structure to
  cover new, not-yet-seen threats **without new code**.

> Any new module or rule is admitted only if it raises core value (r) **without** a
> proportional rise in codebase / maintenance (g).

Vakhter is r-heavy by construction. `FORM ≠ EFFECT` is a structural invariant: one rule
("a sign's form never proves its effect") pre-covers an unbounded set of future attacks
that a signature list would have to chase one by one. Each per-sign card instantiates the
invariant for one codepoint; the *reasoning* does not grow with the *threats*.

### The §5 safeguards (the filter is not usable alone)
Without these, r>g can be turned against the discipline by declaring any module "raises r".

- **§5.1 — r is proven, not declared.** "This raises r" with no evidence is a claim
  without evidence, and is rejected like any other. In Vakhter the evidence is the
  **two gates**: `validate_per_sign` (structural) and `simulate_cards` (semantic).
- **§5.2 — safety can outweigh r>g.** Where a missed threat (false-negative) costs more
  than tech debt, completeness wins even if it raises g. Building the gates, the
  `gate_selftest`, and the control-alias table did *not* raise r — they were built anyway,
  because a gate you cannot fail is not a gate.
- **§5.3 — compute-on-demand is not an absolute.** A static artifact (an oracle in git, a
  committed card) is often *evidence and reproducibility*, not debt. Vakhter's cards are
  deliberately explicit, versioned files — that is the point.

### How this already shows up in Vakhter
- **High r:** 35 signs, one invariant, zero signature tables. New confusables/vectors are
  reasoned from `≠ EFFECT`, not enumerated.
- **§5.1 evidence:** every card passes both gates before commit; `gate_selftest.py` proves
  the gates themselves are not false greens (validator catches injected defects; simulator
  is pure, clean-on-benign, crash-free on hostile input).
- **§5.3 honesty:** SPEC_ONLY cards (no live detector yet) are compute-on-demand
  *delegated to the integrator* — and each says so in OPEN_QUESTIONS. That is an honest
  claim-pending-evidence, not a hidden gap.

### The one place to watch
The filter's failure mode is using "gates don't raise r" to avoid building safety tooling.
§5.2 forbids exactly that. Today's `gate_selftest` is the counter-example on record:
pure-g work, adopted because false-negatives are the expensive failure.

---

<a name="русский"></a>
## Русский

### Фильтр
Неравенство Пикетти **r > g** как правило приёма архитектуры:

- **g (рост / труд)** — ручные IF/ELSE, захардкоженные сигнатуры атак, ручное ревью
  каждого символа, таблицы с ручной синхронизацией. Линейная цена, которую платишь вечно.
- **r (доходность архитектурного капитала)** — способность *существующей* структуры
  перекрывать новые, ещё не виденные угрозы **без нового кода**.

> Любой новый модуль или правило принимается только если он повышает ценность ядра (r)
> **без** пропорционального роста кодовой базы / обслуживания (g).

Vakhter по построению r-тяжёлый. `FORM ≠ EFFECT` — структурный инвариант: одно правило
(«форма знака никогда не доказывает его эффект») заранее покрывает неограниченное множество
будущих атак, которые список сигнатур ловил бы поштучно. Каждая карточка знака — это
инстанс инварианта для одного кодпоинта; *рассуждение* не растёт вместе с *угрозами*.

### Предохранители §5 (фильтр нельзя применять в одиночку)
Без них r>g можно обернуть против дисциплины, объявив любой модуль «повышающим r».

- **§5.1 — r подтверждается, не декларируется.** «Это повышает r» без evidence = claim
  без evidence, отклоняется как всё остальное. В Vakhter evidence — это **два гейта**:
  `validate_per_sign` (структурный) и `simulate_cards` (семантический).
- **§5.2 — безопасность может перевешивать r>g.** Там, где пропуск угрозы (ложный
  негатив) дороже техдолга, полнота берёт верх, даже если растит g. Гейты,
  `gate_selftest`, таблица control-alias — НЕ повысили r, но сделаны, потому что гейт,
  который нельзя провалить, — не гейт.
- **§5.3 — compute-on-demand не абсолют.** Статический артефакт (oracle в git,
  закоммиченная карточка) — часто *evidence и воспроизводимость*, а не долг. Карточки
  Vakhter сознательно явные, версионированные файлы — в этом и смысл.

### Как это уже проявляется в Vakhter
- **Высокий r:** 35 знаков, один инвариант, ноль таблиц сигнатур. Новые confusables/векторы
  выводятся из `≠ EFFECT`, а не перечисляются.
- **§5.1 evidence:** каждая карточка проходит оба гейта до коммита; `gate_selftest.py`
  доказывает, что сами гейты — не ложная зелёнка (валидатор ловит инъектированные дефекты;
  симулятор чист, benign-чист, не падает на враждебном вводе).
- **§5.3 честность:** SPEC_ONLY-карточки (пока без живого детектора) — это compute-on-demand,
  *делегированный интегратору*, и каждая пишет об этом в OPEN_QUESTIONS. Это честный
  claim-в-ожидании-evidence, а не спрятанная дыра.

### Единственное место, за которым следить
Режим отказа фильтра — использовать «гейты не повышают r», чтобы не строить safety-инструмент.
§5.2 запрещает именно это. Сегодняшний `gate_selftest` — зафиксированный контрпример:
чистая-g работа, принятая потому, что ложные негативы — дорогой отказ.

---

### See also / См. также
- `code/tools/gate_selftest.py` — mutation-adequacy + robustness proof of the two gates.
- `code/tools/validate_per_sign.py`, `code/tools/simulate_cards.py` — the two gates.
- `docs/FOUNDATION_LAYER_ALIGNMENT.md` — the FO map (fail-visible, no-single-layer, etc.).
