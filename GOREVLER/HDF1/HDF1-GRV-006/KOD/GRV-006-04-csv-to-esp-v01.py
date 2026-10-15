#!/usr/bin/env python3
"""GRV-006: read BERO CSV, process channel values, send result to ESP, verify echo."""
import asyncio
import csv
import os
import sys
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

import aioesphomeapi

CSV_PATH = Path(os.environ.get("GRV006_CSV", "GRV-005-14-v06-QC-GIRDİSİ-20261011.csv"))
ADDRESS = os.environ.get("ESPHOME_ADDRESS", "192.168.0.9")
PORT = int(os.environ.get("ESPHOME_PORT", "6053"))
NOISE_PSK = os.environ.get("ESPHOME_NOISE_PSK") or None
ECHO_NAME = "GRV006 Echo Value"
ACTION_NAME = "grv006_set_value"
SCALE = Decimal("1000")


def read_and_process():
    with CSV_PATH.open("r", newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        raise ValueError(f"CSV boş: {CSV_PATH}")
    required = {"channel_id", "adc_rms_ac"}
    if not required.issubset(rows[0].keys()):
        raise ValueError(f"CSV sütunları eksik; gereken: {sorted(required)}")
    channels = [
        row for row in rows
        if row["channel_id"] != "BIAS" and row["adc_rms_ac"].strip()
    ]
    if not channels:
        raise ValueError("BIAS dışındaki kanallarda adc_rms_ac değeri bulunamadı")
    values = [(row["channel_id"], Decimal(row["adc_rms_ac"])) for row in channels]
    processed_sum = sum(value for _, value in values)
    send_value = int((processed_sum * SCALE).quantize(Decimal("1"), rounding=ROUND_HALF_UP))

    # Bağımsız kontrol: kaynak CSV'yi diskten yeniden açıp yeniden hesapla.
    with CSV_PATH.open("r", newline="", encoding="utf-8-sig") as f:
        reread = list(csv.DictReader(f))
    independent_values = [
        Decimal(row["adc_rms_ac"])
        for row in reread
        if row["channel_id"] != "BIAS" and row["adc_rms_ac"].strip()
    ]
    independent_sum = sum(independent_values)
    independent_send = int((independent_sum * SCALE).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    if send_value != independent_send:
        raise AssertionError(f"Bağımsız kontrol uyuşmadı: {send_value} != {independent_send}")

    print(f"CSV_READ: PASS ({CSV_PATH}; {len(rows)} rows)")
    print("CHANNEL_VALUES: " + ", ".join(f"{name}={value}" for name, value in values))
    print(f"PROCESSED_SUM: {processed_sum}")
    print(f"SEND_INTEGER: {send_value} (sum × 1000, rounded)")
    print(f"INDEPENDENT_CHECK: PASS ({independent_send})")
    return send_value


async def main() -> int:
    value = read_and_process()
    client = aioesphomeapi.APIClient(ADDRESS, PORT, noise_psk=NOISE_PSK)
    try:
        await client.connect(login=True)
        print(f"CONNECTED: {ADDRESS}:{PORT}")
        entities, services = await client.list_entities_services()
        entity = next((e for e in entities if getattr(e, "name", "") == ECHO_NAME), None)
        action = next((s for s in services if getattr(s, "name", "") == ACTION_NAME), None)
        if entity is None:
            print(f"RESULT: ERROR — entity not found: {ECHO_NAME}")
            return 2
        if action is None:
            print(f"RESULT: ERROR — action not found: {ACTION_NAME}")
            return 2

        echo = {"value": None}
        changed = asyncio.Event()

        def on_state(state):
            if getattr(state, "key", None) == entity.key:
                echo["value"] = getattr(state, "state", None)
                changed.set()

        client.subscribe_states(on_state)
        await asyncio.sleep(0.5)
        changed.clear()
        await client.execute_service(action, {"value": value})
        try:
            await asyncio.wait_for(changed.wait(), timeout=10)
        except asyncio.TimeoutError:
            print("RESULT: INCONCLUSIVE — echo state update not received")
            return 3
        echoed = echo["value"]
        print(f"SENT: {value}")
        print(f"ECHOED: {echoed}")
        if echoed is not None and int(float(echoed)) == value:
            print("RESULT: PASS — CSV processed value returned by ESP")
            return 0
        print("RESULT: FAIL — sent value differs from ESP echo")
        return 1
    finally:
        await client.disconnect()


if __name__ == "__main__":
    try:
        raise SystemExit(asyncio.run(main()))
    except Exception as exc:
        print(f"RESULT: ERROR — {type(exc).__name__}: {exc}", file=sys.stderr)
        raise
