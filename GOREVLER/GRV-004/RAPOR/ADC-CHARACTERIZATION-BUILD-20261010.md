# GRV-004 — ADC Characterization Build Validation

- Date: 2026-10-10
- Status: BUILD_OK — physical measurement pending
- ESPHome: 2026.9.1
- ESP-IDF: 5.5.5
- Target: classic ESP32 / esp32d1
- Validation run ID: 38066911718
- Validated branch commit: 2b3722dc69bb9685029967218b4811a2d5f5afbc

## 1. Purpose

Resolve the compile-time dependency problem caused by adc_character_test.h including esp_adc/adc_oneshot.h, while preserving the existing active esp32d1.yaml and PZEM setup. The characterization candidate is a separate versioned YAML; the existing active file was not overwritten and no firmware was flashed.

## 2. Supported dependency fix

ESPHome 2026.2 and later excludes some unused built-in ESP-IDF components by default. The supported YAML-level fix for custom code that directly uses the ADC oneshot API is:

```yaml
esp32:
  framework:
    advanced:
      include_builtin_idf_components:
        - esp_adc
```

This explicitly re-enables the built-in esp_adc component required by esp_adc/adc_oneshot.h. The candidate pins ESP-IDF 5.5.5.

Reference: ESPHome developer note, “Unused Built-in IDF Components Excluded by Default” (published 2026-02-20).

## 3. Files

- Candidate YAML: KOD/esp32d1-adc-characterization.yaml
- Header: KOD/adc_character_test.h
- Report: ADC-CHARACTERIZATION-BUILD-20261010.md
- Existing active esp32d1.yaml and previously archived GRV-004 YAML/log files were not replaced.

## 4. Experiment implemented

For each target period of 1 ms, 2 ms, 5 ms and 10 ms:
- 1000 scan cycles are attempted.
- Each scan reads all four channels sequentially, once each:
  - GPIO32 — BIAS — ADC1 channel 4
  - GPIO33 — 1T — ADC1 channel 5
  - GPIO34 — 2T — ADC1 channel 6
  - GPIO35 — 3T — ADC1 channel 7
- Raw ADC counts are retained without voltage conversion or on-device mean/standard-deviation calculation.
- A relative scan-start timestamp in microseconds is retained for each scan. Computer-side analysis can calculate actual intervals and jitter; the target period is not proof of the actual period.
- A failed ADC read is represented by -1 and included in the per-sweep error count.
- Data is emitted in logger chunks after each sweep: RAW,<period>,<channel>,<start-index>:... and TS_US,<period>,<start-index>:... This is log-formatted data, not a separately written file on the ESP32.

The sampler runs in its own FreeRTOS task and yields on each scan so ESPHome, Wi-Fi, API and PZEM tasks can continue to run.

## 5. PZEM preserved in the candidate

- UART TX: GPIO16
- UART RX: GPIO17
- Baud: 9600, 8 data bits, no parity, 1 stop bit
- Modbus address: 0x01
- Update interval: 5 seconds
- Entity names: PZEM Gerilim, PZEM Akım, PZEM Güç, PZEM Enerji, PZEM Frekans, PZEM Güç Faktörü

## 6. Build result

The final candidate revision compiled successfully in GitHub Actions with ESPHome 2026.9.1 and ESP-IDF 5.5.5. The build log ends with “INFO Successfully compiled program.” The missing esp_adc/adc_oneshot.h dependency is resolved by explicit built-in component inclusion.

The CI job used temporary build-only Wi-Fi secrets. No real Wi-Fi credentials were added to the repository.

## 7. What is not verified

NO PHYSICAL MEASUREMENT WAS PERFORMED. NO OTA UPLOAD OR DEVICE RUNTIME TEST WAS PERFORMED.

This record confirms compilation only. It does not claim that all four sweeps completed on the physical ESP32, that 1000 valid readings were obtained per channel at each target period, that measured periods match their targets, or that the complete log was received without truncation. Those points remain the next hardware-validation step.
