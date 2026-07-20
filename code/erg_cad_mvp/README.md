# ERG-CAD — Objective Anomaly Detector (runnable MVP)

🇬🇧 [English](#english) · 🇷🇺 [Русский](#русский)

---

<a name="english"></a>
## English

The first **executable** node of family 1 (ERG-CAD → ACDM-ST). It proves the founding principle in code, not in words:

> **INTENSITY ≠ OBJECTIVITY** — a strong signal ≠ an objective signal.

Pure Python, standard library only (in the `msl_mip` house style). No dependencies.

### The idea
A signal = a field of activation over a grid of `time × nodes`. The detector applies RG coarse-graining (repeated 2×2 averaging = a renormalization step) and measures **how much of the signal survives** the change of scale:

| Scenario | intensity | objectivity (survival) | verdict |
|---|---|---|---|
| A. single strong spike (0.9) | 0.90 | **0.016** | `NOISE` |
| B. weak persistent (0.4) | 0.40 | **0.56** | `WATCH` |
| C. strong persistent (0.9) | 0.90 | 0.56 | `CRITICAL` |
| D. B under high social_stress | 0.40 | 0.56 | `NOISE` (thresholds raised) |

**The point:** A is **stronger** than B by intensity, yet is **cut off**, while B passes. That is "intensity ≠ objectivity", demonstrated.

### Run
```bash
python demo.py                  # A/B/C/D demo + self-check (asserts)
python tests/test_detector.py   # 6 tests, no pytest
pytest                          # if pytest is installed
```

### What's inside
```
erg_cad/
  detector.py   RG pipeline (coarse_grain, rg_filter_pipeline), ERGDetector,
                adaptive_weight_update (plasticity), mask_api_output (public/private)
  signals.py    synthetic "golden traces" (spike / weak / strong persistent)
demo.py         scenarios A–D
tests/          acceptance criteria A/B/C + plasticity + API masking
```

### How it fits the architecture
- **ERG-CAD** is the entry point of the ACDM-ST pipeline (`Telemetry → ERG-CAD → …`). This code is its first working node.
- **Public/Private boundary** honoured: `analyze()` returns a private `Reading` (intensity, objectivity, level_peaks); `mask_api_output()` gives the client only `risk_level / explanation / confidence_band / recommended_action` — no raw numbers (verified by `test_api_masking_hides_internals`).
- **Adaptive Aerodynamic Plasticity** implemented: as `social_stress` rises, thresholds rise, and a weakly-persistent signal (D) is reclassified as NOISE.
- **The tests are golden traces** for ACDM-ST Module 15 (verification, not simulation).

### Honest boundaries (what it is NOT)
- A **prototype of the principle**, not a production detector. The objectivity metric here is peak survival under 2×2 averaging; a real ERG-CAD may be richer (Scale_Stability / Temporal_Persistence / Source_Redundancy as separate axes).
- Thresholds (0.35 / 0.60) are demo values, not calibrated on real data.
- Written to the BioRG-CAD spec (criteria A/B/C). The formulas can be refined against the current ERG-CAD canon in the THICK archive.

Status: `WORKING` · v0.1 · the principle carried into code and verified.

---

<a name="русский"></a>
## Русский

Первый **исполняемый** узел семьи 1 (ERG-CAD → ACDM-ST). Доказывает главный принцип программно, а не словами:

> **INTENSITY ≠ OBJECTIVITY** — сильный сигнал ≠ объективный сигнал.

Чистый Python, только стандартная библиотека (в духе `msl_mip`). Зависимостей нет.

### Идея
Сигнал = поле активации на сетке `время × узлы`. Детектор применяет RG-огрубление (повторное 2×2 усреднение = шаг ренормализации) и меряет, **сколько сигнала выживает** при смене масштаба:

| Сценарий | intensity | objectivity (выживание) | вердикт |
|---|---|---|---|
| A. одиночный сильный спайк (0.9) | 0.90 | **0.016** | `NOISE` |
| B. слабый устойчивый (0.4) | 0.40 | **0.56** | `WATCH` |
| C. сильный устойчивый (0.9) | 0.90 | 0.56 | `CRITICAL` |
| D. B под высоким social_stress | 0.40 | 0.56 | `NOISE` (пороги подняты) |

**Главное:** A **сильнее** B по интенсивности, но **отсекается**, а B проходит. Это и есть доказанное «intensity ≠ objectivity».

### Запуск
```bash
python demo.py                  # демонстрация A/B/C/D + самопроверка (asserts)
python tests/test_detector.py   # 6 тестов без pytest
pytest                          # если pytest установлен
```

### Что внутри
```
erg_cad/
  detector.py   RG-конвейер (coarse_grain, rg_filter_pipeline), ERGDetector,
                adaptive_weight_update (пластичность), mask_api_output (public/private)
  signals.py    синтетические «золотые трассы» (spike / weak / strong persistent)
demo.py         сценарии A–D
tests/          критерии приёмки A/B/C + пластичность + маскировка API
```

### Как это ложится в архитектуру
- **ERG-CAD** — точка входа пайплайна ACDM-ST (`Telemetry → ERG-CAD → …`). Этот код — его первый рабочий узел.
- **Public/Private boundary** соблюдён: `analyze()` возвращает приватную `Reading` (intensity, objectivity, level_peaks); `mask_api_output()` отдаёт клиенту только `risk_level / explanation / confidence_band / recommended_action` — без сырых чисел (тест `test_api_masking_hides_internals` это проверяет).
- **Adaptive Aerodynamic Plasticity** реализована: при росте `social_stress` пороги поднимаются, и слабо-устойчивый сигнал (D) переклассифицируется в NOISE.
- **Тесты = golden traces** для Module 15 ACDM-ST (верификация, не симуляция).

### Честные границы (что это НЕ)
- Это **прототип принципа**, не production-детектор. Метрика objectivity здесь — выживание пика при 2×2-усреднении; в реальном ERG-CAD может быть богаче (Scale_Stability / Temporal_Persistence / Source_Redundancy как отдельные оси).
- Пороги (0.35 / 0.60) — демонстрационные, не откалиброваны на реальных данных.
- Написано по спеке BioRG-CAD (критерии A/B/C). При сверке с текущим каноном ERG-CAD из THICK-архива формулы можно уточнить.

Статус: `WORKING` · v0.1 · перенос принципа в код выполнен и проверен.
