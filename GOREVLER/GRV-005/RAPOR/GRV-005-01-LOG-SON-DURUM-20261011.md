# GRV-005 — PZEM timestamp log, latest snapshot

- Date: 2026-10-11
- Source: user-provided ESPHome log, 3,529 lines, 297,393 characters.
- Captured runtime shown in log: 09:26:41.231–09:52:32.028 (about 25 min 51 s).
- Raw source archived in the user's ChatGPT Library at `/BERO/GRV-005/LOG/esp32d1-logs-20261011-0926-0952.txt`.
- This report is an observation summary; it does not replace the raw log.
- Device/config shown: `esp32d1`, ESPHome 2026.9.1, ESP32 rev3.1, PZEM UART TX GPIO16 / RX GPIO17, 9600 baud, `pzemac` update interval 5s.

## Observations supported by this log

1. The ESPHome log connects to `esp32d1` at `192.168.0.8`; Wi-Fi is connected. Local network identifiers are intentionally not copied into this repository report.
2. At startup, wall clock is not synchronized. The log reports SNTP synchronization at 09:27:09.786. The template sensor continues reporting `CLOCK_NOT_SYNCED` briefly and starts reporting `epoch_s` at 09:27:10.901.
3. The current sensor publishes `0.028 A` repeatedly at roughly five-second intervals in the shown period. This is the observed practical baseline for this powered prototype, not a true 0 A test.
4. Voltage varies around 229.1–230.8 V in the visible log; power around 1.5–1.8 W; frequency around 49.9–50.0 Hz; power factor around 0.23–0.28.
5. PZEM energy is shown in the ESPHome component configuration as `Wh`; the visible value changes from `10522 Wh` to `10523 Wh` during this log.
6. `pzem_update_millis` changes with current sensor publications, while `age_ms` increases between them and returns to about 0.8 s after an update. This supports that the `on_value` marker is refreshed periodically even when displayed current remains 0.028 A.
7. This log does not independently prove a one-to-one relationship between every successful Modbus response and the ESPHome `on_value` callback. The marker remains a callback-time marker, not a verified exact Modbus response timestamp.
8. The log is PZEM/timing telemetry. It does not contain the GRV-005-05 1000-sample ADC statistics, statistical self-test, or final CSV rows.

## GRV-005-05 relevance

Keep this log as a historical reference before starting the controlled mathematical self-test. It confirms the earlier PZEM timestamp behavior and the SNTP startup delay. It must not be treated as evidence that ADC statistics have been implemented or validated.

## Status

- Raw log archived without modifying its contents in the user's Library.
- This summary is a new additive record.
- No existing firmware, ALT09/ALT10 record, or historical report was overwritten.
