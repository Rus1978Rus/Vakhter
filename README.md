# INVARIANT ENGINE SUITE

**ЧАСТНЫЙ АВТОРСКИЙ ПРОЕКТ / COMMERCIAL USE PROHIBITED**
Автор: Руслан Малявский · Собрано: 2026-07-20 · Статус: WORKING_DRAFT

Сводный пакет наработок одной рабочей сессии вокруг общей идеи:

> **Реальное/осмысленное — это структура, инвариантная к преобразованию
> (подложка / масштаб / время / кодировка), а не локальный поверхностный знак.**

Один движок, две оси, много подложек: **MSL** (структура, ось подложки) +
**ERG** (устойчивость, ось масштаба/времени). Сигнал, текст, промпт, код —
адаптеры на одном ядре. Плюс слой канонизации, закрывающий кодировочные обходы.

---

## Что здесь РАБОТАЕТ (запускаемый код)

| Модуль | Что делает | Статус |
|---|---|---|
| `code/erg_cad_mvp/` | ERG-детектор «intensity ≠ objectivity» (спайк→шум, устойчивый→сигнал) | ✅ 6/6 тестов |
| `code/invariant_engine/` | общее ядро + адаптеры (сигнал/текст/код), **настоящий MSL** встроен | ✅ 11/11 + 8/8 |
| `code/canonicalization/` | pre-pass: percent / HTML-entity / escapes / **overlong-UTF-8** | ✅ доказано на MSL |
| `code/eval/` | prompt-injection eval (MSL vs keyword), dataset-pluggable | ✅ индикативно |
| `code/range/` | before/after охват: широкий + цифры/IP + метасимволы | ✅ бежит на MSL |

Запуск (для настоящего MSL нужен репозиторий `msl_mip` рядом):
```bash
python code/erg_cad_mvp/demo.py
python code/erg_cad_mvp/tests/test_detector.py
MSL_MIP_HOME=/path/to/msl_mip python code/invariant_engine/demo_real.py
MSL_MIP_HOME=/path/to/msl_mip python code/canonicalization/demo_overlong.py
MSL_MIP_HOME=/path/to/msl_mip python code/eval/eval.py
MSL_MIP_HOME=/path/to/msl_mip python code/range/range_meta.py     # 18% -> 100%, 0 new FP
MSL_MIP_HOME=/path/to/msl_mip python code/range/range_digits.py   # 3/14 -> 14/14, 0 new FP
```

Измеренный охват по категориям — см. **`COVERAGE_MAP.md`** (before/after,
проценты, и что ещё нужно, чтобы поднять каждый пункт).

## Что здесь ЗАГОТОВКИ (карточки знаков — на вход в конвейер)

`sign_cards/` — прочерновлено ВСЁ пространство percent-кодирования `%00..%FF`:

- `DIGIT_CLASS_0-9_DRAFT.md` — классовая карточка цифр (двойное дно: SURFACE + CARRIER).
- `DIGIT_0-9_DRAFT.md` — per-digit карточки 0–9 (несущий слой по полосам `%Nx`).
- `HEX_A-F_DRAFT.md` — hex-полосы A–F (вердикт по сегодня + риски на завтра).
- `HEX_BANDS_A-F_MAP_DRAFT.md` — карта полос (справочно).

Все карточки — `WORKING_DRAFT`, **не прогнаны через конвейер, автором не закрыты.**
Стратегия: черновить по максимуму (угроза завтра готовится сегодня), закрывать
конвейером по приоритету риска.

## Главная идея одной таблицей

| Проект | инвариант через… | статус |
|---|---|---|
| MSL/MIP | смену **подложки** | внешний репозиторий (ядро) |
| ERG-CAD | смену **масштаба** | здесь, ✅ бежит |
| E-Continuity | смену **времени** | концепт |
| canonicalization | смену **кодировки** | здесь, ✅ бежит |

---

## Честные границы

- **Настоящий MSL — отдельный репозиторий** (`msl_mip`), а не часть пакета: адаптер
  `msl_real.py` подключается к нему (`MSL_MIP_HOME`). Заглушка `msl.py` работает
  автономно, но она беднее.
- **Карточки — заготовки**, не рабочие детекторы. Их закрывает конвейер автора.
- **Eval не на публичном бенчмарке** (сеть была закрыта) — набор рукотворный,
  цифры индикативные; харнесс принимает реальный датасет одной строкой.
- **MSL слеп к языковым (смысловым) атакам** by design — это ось «языкового»
  охранника, не структурного.

## Структура

```
README.md                 — этот файл
COVERAGE_MAP.md            — измеренный охват по категориям (before/after, %)
MASTER_PROJECT_MAP.md      — карта всей экосистемы проектов автора
code/
  erg_cad_mvp/             — ERG-детектор (standalone)
  invariant_engine/        — общее ядро + адаптеры + настоящий MSL
  canonicalization/        — pre-pass (двойное дно цифр в коде)
  eval/                    — prompt-injection eval harness
  range/                   — before/after харнессы охвата (+ симуляторы карточек)
sign_cards/                — заготовки карточек 0–9 + A–F (всё %00..%FF)
```

## Лицензия / статус
Частный авторский проект. Коммерческое использование запрещено.
NOT A FINAL STANDARD · NOT A SECURITY CERTIFICATE · NOT A PRODUCTION VALIDATOR.
Готово к переносу в отдельный GitHub-репозиторий как пакет.
