# Foundation Layer alignment: the code ↔ the observations · Привязка к Foundation Layer: код ↔ наблюдения

AUTHOR / АВТОР: Руслан Малявский · 2026-07-20 · maps this suite to Foundation Layer v11.5

🇬🇧 [English](#english) · 🇷🇺 [Русский](#русский)

---

<a name="english"></a>
## English

Foundation Layer (FL) is a registry of ~99 structural observations (FO) about how systems handle status, trust, and validation — a diagnostic toolkit, conveyor-verified across 53 real cases, 34 domains, ~69,826 years, 0 hallucinations.

This suite is not a separate idea. It is a **working implementation** of FL in the AI-security domain: nearly every design decision and every bug found is a specific FO manifesting in code. FL is the WHY; this suite is the proof.

```
Foundation Layer   → WHY     (structural laws, 70 000 years of evidence)
MSL / MIP          → SIGN    (what a sign does in context)
this suite         → PRODUCT (laws instantiated as code: guard + notarius + erg-fraud)
the conveyor       → METHOD  (how all of it is checked)
```

### 1. Design ↔ FO

| built here | where (file / check) | Foundation Observation |
|---|---|---|
| "what a sign DOES, not what it IS"; invariance across substrate | `msl_real`, whole guard | **FO-013** SUBSTRATE_INDEPENDENCE; **FO-012** OBSERVED>DECLARED |
| structural guard at the input boundary | `product.analyze` | **FO-026** SOCIAL_ENGINEERING ~= PROMPT_INJECTION |
| hidden command / invisible-smuggled instruction | `invisible_cards`, `metachar_cards` | **FO-034** PARASITIC_CONTEXT_ELEMENT |
| rare-Unicode detectors (tag chars U+E00xx, VS, bidi, hieroglyph-range) | `invisible_cards` (check #3) | **FO-099** RARE_SIGN ≠ SAFE_SIGN; DORMANT_EPOCH ≠ INACTIVE_RISK |
| provenance: SIGNED ≠ NATIVE · behavioral: SIGNED ≠ SAFE | `provenance.py`, `behavioral.py` (checks #4c, #5) | **FO-049** SOURCE_STATUS ≠ CLAIM_STATUS |
| behavioral battery — a signature never waives the behaviour test | `behavioral.py` (check #5) | **FO-004** REVIEW ≠ VALIDATION; **FO-012** |
| defense in depth — 8 checks, no single layer suffices | all component checks | **FF-010** NO_SINGLE_LAYER_IS_SUFFICIENT; **FO-080** COMPLETE_TESTING_IMPOSSIBLE |
| self-defense: a guard you can drown is not a guard | `guard.py` (check #11) | **FO-088** EXISTS ≠ EFFECTIVE |
| m-of-n + transparency log; trace on the record, not the actor | `quorum.py`, `transparency.py` | **FO-004**; **FO-024** TRACE ≠ ACTOR |
| erg-fraud: a spike is real only if it survives coarse-graining | `applications/erg_fraud` | invariance across scale (**FO-013** family) |
| notarius: native vs inserted, provenance ≠ visible carrier | `applications/notarius_data` | **FO-016** PROVENANCE_PATH ≠ VISIBLE_CARRIER |

### 2. The bugs the conveyor found ARE FL laws in action

Not accidents — the registry predicted them:

- **ERG bypass** (softening for usability became the hole; a threat phrased as a question was cleared) = **`COMPLIANCE_IS_ATTACK_SURFACE`** / STRENGTH_OF_SYSTEM = VECTOR_FOR_ATTACKER (FL injection presentation).
- **Fail-open** (the guard crashed → let the threat through) = **FO-088** EXISTS ≠ EFFECTIVE + **FO-064** SECURITY_THEATER_BY_PROCESS. A guard that "runs" but fails open is theatre.
- **SIGNED ≠ SAFE** (a malicious author signs a backdoor, provenance accepts it) = **FO-049** SOURCE_STATUS ≠ CLAIM_STATUS, verbatim.

We re-discovered the FOs empirically, in code. That is strong evidence the registry is not abstract.

### 3. We independently followed FL's own "how to use" recipe

The FL injection presentation lists five steps; this suite implements all five without having read it first:

1. FO-026 at the input boundary (untrusted until verified) → fail-closed + guard
2. FO-049 at authority claims (source ≠ content) → provenance + behavioral
3. FO-034 as a filter (does this element work toward or against the goal?) → cards
4. FO-088 as a layer check (exists ≠ active ≠ effective) → the 8 component checks
5. FO-099 to rare characters (rare Unicode is not safe) → invisible / tag / VS cards

### 4. Honest — FL requires this of itself, so we honor it

- **FO-080 COMPLETE_TESTING_IS_IMPOSSIBLE** — the 8 checks do not make the product "proven complete." Every check ships with an honest "missing to raise" list.
- **FO-004 applies to FL itself** — using FL (or these checks) is a *review*, not a *validation* of security. We label verdicts, not guarantees.
- **FF-003 MULTI_MODEL_REVIEW ≠ ADVERSARIAL_PROCESS** — our conveyor used five same-model reviewers plus an adversarial verify pass. The adversarial pass is what gave it teeth; true independence still wants model diversity (multi-vendor).

### 5. The guard as a Foundation Layer case

By FL's own CASE_LIBRARY criteria (documented pattern, investigation with findings, generalisable structure, measured outcome), this session is a candidate:

> **REAL_054 (candidate):** Foundation Layer patterns implemented as a working guard and adversarially verified in code, 2026 — with three FOs (COMPLIANCE_IS_ATTACK_SURFACE, EXISTS ≠ EFFECTIVE, SOURCE_STATUS ≠ CLAIM_STATUS) re-derived empirically from the guard's own failures. STATUS: NEEDS_CONVEYOR.

This gives the product a rare thing: not "another filter," but a concrete instantiation of a registry tested against 70,000 years of recurring structure.

---

<a name="русский"></a>
## Русский

Foundation Layer (FL) — реестр из ~99 структурных наблюдений (FO) о том, как системы обращаются со статусом, доверием и валидацией; диагностический инструментарий, проверенный конвейером на 53 реальных случаях, в 34 доменах, на диапазоне ~69 826 лет, с 0 галлюцинаций.

Этот пакет — не отдельная идея. Это **рабочая реализация** FL в области безопасности ИИ: почти каждое проектное решение и каждый найденный баг — это конкретное FO, проявившееся в коде. FL — это ПОЧЕМУ; пакет — доказательство.

```
Foundation Layer   → ПОЧЕМУ  (структурные законы, 70 000 лет свидетельств)
MSL / MIP          → ЗНАК    (что знак делает в контексте)
этот пакет         → ПРОДУКТ (законы как код: вахтёр + нотариус + erg-fraud)
конвейер           → МЕТОД   (как всё это проверяется)
```

### 1. Проектное решение ↔ FO

| построено здесь | где (файл / проверка) | Foundation Observation |
|---|---|---|
| «что знак ДЕЛАЕТ, а не что он ЕСТЬ»; инвариантность к подложке | `msl_real`, весь вахтёр | **FO-013** SUBSTRATE_INDEPENDENCE; **FO-012** OBSERVED>DECLARED |
| структурный страж на границе входа | `product.analyze` | **FO-026** SOCIAL_ENGINEERING ~= PROMPT_INJECTION |
| скрытая команда / невидимо-протащенная инструкция | `invisible_cards`, `metachar_cards` | **FO-034** PARASITIC_CONTEXT_ELEMENT |
| детекторы редкого Unicode (tag U+E00xx, VS, bidi, иероглифы) | `invisible_cards` (проверка #3) | **FO-099** RARE_SIGN ≠ SAFE_SIGN; DORMANT_EPOCH ≠ INACTIVE_RISK |
| провенанс: SIGNED ≠ NATIVE · поведение: SIGNED ≠ SAFE | `provenance.py`, `behavioral.py` (#4c, #5) | **FO-049** SOURCE_STATUS ≠ CLAIM_STATUS |
| поведенческая батарея — подпись никогда не отменяет тест поведения | `behavioral.py` (проверка #5) | **FO-004** REVIEW ≠ VALIDATION; **FO-012** |
| защита в глубину — 8 проверок, ни один слой не самодостаточен | все проверки компонентов | **FF-010** NO_SINGLE_LAYER_IS_SUFFICIENT; **FO-080** COMPLETE_TESTING_IMPOSSIBLE |
| самозащита: вахтёр, которого можно утопить, — не вахтёр | `guard.py` (проверка #11) | **FO-088** EXISTS ≠ EFFECTIVE |
| m-of-n + transparency-лог; след на записи, а не на акторе | `quorum.py`, `transparency.py` | **FO-004**; **FO-024** TRACE ≠ ACTOR |
| erg-fraud: всплеск реален, только если переживёт огрубление | `applications/erg_fraud` | инвариантность к масштабу (семейство **FO-013**) |
| нотариус: родное или вставленное, провенанс ≠ видимый носитель | `applications/notarius_data` | **FO-016** PROVENANCE_PATH ≠ VISIBLE_CARRIER |

### 2. Баги, найденные конвейером, — это законы FL в действии

Не случайности — реестр их предсказал:

- **Обход ERG** (смягчение ради удобства стало дырой; угроза в форме вопроса была снята) = **`COMPLIANCE_IS_ATTACK_SURFACE`** / STRENGTH_OF_SYSTEM = VECTOR_FOR_ATTACKER (презентация FL по инъекциям).
- **Fail-open** (вахтёр упал → пропустил угрозу) = **FO-088** EXISTS ≠ EFFECTIVE + **FO-064** SECURITY_THEATER_BY_PROCESS. Вахтёр, который «работает», но падает открытым, — театр.
- **SIGNED ≠ SAFE** (злонамеренный автор подписывает бэкдор, провенанс принимает его) = **FO-049** SOURCE_STATUS ≠ CLAIM_STATUS дословно.

Мы переоткрыли FO эмпирически, в коде. Это сильное свидетельство, что реестр не абстрактен.

### 3. Мы независимо повторили собственный «рецепт применения» FL

Презентация FL по инъекциям перечисляет пять шагов; пакет реализует все пять, не прочитав её заранее:

1. FO-026 на границе входа (недоверенно, пока не проверено) → fail-closed + вахтёр
2. FO-049 на заявлениях авторитета (источник ≠ содержимое) → провенанс + поведение
3. FO-034 как фильтр (этот элемент работает на цель или против?) → карточки
4. FO-088 как проверка слоёв (существует ≠ активно ≠ эффективно) → 8 проверок компонентов
5. FO-099 к редким символам (редкий Unicode небезопасен) → карточки невидимок / tag / VS

### 4. Честно — FL требует этого от самого себя, и мы это чтим

- **FO-080 COMPLETE_TESTING_IS_IMPOSSIBLE** — 8 проверок не делают продукт «доказанно полным». Каждая проверка идёт с честным списком «что добавить».
- **FO-004 применяется к самому FL** — использовать FL (или эти проверки) — это *обзор*, а не *валидация* безопасности. Мы ставим вердикты, не гарантии.
- **FF-003 MULTI_MODEL_REVIEW ≠ ADVERSARIAL_PROCESS** — наш конвейер использовал пять ревьюеров одной модели плюс адверсариальный проход проверки. Именно адверсариальный проход дал зубы; настоящая независимость всё же хочет разнообразия моделей (мультивендор).

### 5. Вахтёр как случай Foundation Layer

По собственным критериям CASE_LIBRARY у FL (документированный паттерн, расследование с находками, обобщаемая структура, измеренный итог) эта сессия — кандидат:

> **REAL_054 (кандидат):** паттерны Foundation Layer, реализованные как рабочий вахтёр и адверсариально проверенные в коде, 2026 — с тремя FO (COMPLIANCE_IS_ATTACK_SURFACE, EXISTS ≠ EFFECTIVE, SOURCE_STATUS ≠ CLAIM_STATUS), переоткрытыми эмпирически из собственных провалов вахтёра. СТАТУС: NEEDS_CONVEYOR.

Это даёт продукту редкую вещь: не «ещё один фильтр», а конкретное воплощение реестра, проверенного на 70 000 лет повторяющейся структуры.
