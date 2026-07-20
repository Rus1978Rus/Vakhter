# ERG-CAD — Objective Anomaly Detector (runnable MVP)

Первый **исполняемый** узел семьи 1 (ERG-CAD → ACDM-ST). Доказывает главный
принцип программно, а не словами:

> **INTENSITY ≠ OBJECTIVITY** — сильный сигнал ≠ объективный сигнал.

Чистый Python, только стандартная библиотека (в духе `msl_mip`). Зависимостей нет.

## Идея

Сигнал = поле активации на сетке `время × узлы`. Детектор применяет
RG-огрубление (повторное 2×2 усреднение = шаг ренормализации) и меряет,
**сколько сигнала выживает** при смене масштаба:

| Сценарий | intensity | objectivity (выживание) | вердикт |
|---|---|---|---|
| A. Одиночный сильный спайк (0.9) | 0.90 | **0.016** | `NOISE` |
| B. Слабый устойчивый (0.4) | 0.40 | **0.56** | `WATCH` |
| C. Сильный устойчивый (0.9) | 0.90 | 0.56 | `CRITICAL` |
| D. B под высоким social_stress | 0.40 | 0.56 | `NOISE` (пороги подняты) |

**Главное:** A **сильнее** B по интенсивности, но **отсекается**, а B проходит.
Это и есть доказанное «intensity ≠ objectivity».

## Запуск

```bash
python demo.py            # демонстрация A/B/C/D + самопроверка (asserts)
python tests/test_detector.py   # 6 тестов без pytest
pytest                    # если pytest установлен
```

## Что внутри

```
erg_cad/
  detector.py   RG-конвейер (coarse_grain, rg_filter_pipeline), ERGDetector,
                adaptive_weight_update (пластичность), mask_api_output (public/private)
  signals.py    синтетические «золотые трассы» (spike / weak / strong persistent)
demo.py         сценарии A–D
tests/          критерии приёмки A/B/C + пластичность + маскировка API
```

## Как это ложится в вашу архитектуру

- **ERG-CAD** — точка входа пайплайна ACDM-ST (`Telemetry → ERG-CAD → …`). Этот
  код — его первый рабочий узел.
- **Public/Private boundary** соблюдён: `analyze()` возвращает приватную
  `Reading` (intensity, objectivity, level_peaks); `mask_api_output()` отдаёт
  клиенту только `risk_level / explanation / confidence_band / recommended_action`
  — без сырых чисел (тест `test_api_masking_hides_internals` это проверяет).
- **Adaptive Aerodynamic Plasticity** реализована: при росте `social_stress`
  пороги поднимаются, и слабо-устойчивый сигнал (D) переклассифицируется в NOISE.
- **Тесты = golden traces** для Module 15 ACDM-ST (верификация, не симуляция).

## Честные границы (что это НЕ)

- Это **прототип принципа**, не production-детектор. Метрика objectivity здесь —
  выживание пика при 2×2-усреднении; в реальном ERG-CAD может быть богаче
  (Scale_Stability / Temporal_Persistence / Source_Redundancy как отдельные оси).
- Пороги (0.35 / 0.60) — демонстрационные, не откалиброваны на реальных данных.
- Написано по спеке BioRG-CAD (критерии A/B/C). При сверке с текущим
  каноном ERG-CAD из THICK-архива формулы можно уточнить.

Статус: `WORKING` · v0.1 · перенос принципа в код выполнен и проверен.
