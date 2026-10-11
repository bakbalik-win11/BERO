#!/usr/bin/env python3
"""GRV-006-03: send one integer through ESPHome Native API and verify echoed state.

Requires: Python 3.10+ and aioesphomeapi.
Install: python3 -m pip install aioesphomeapi
Set ESPHOME_ADDRESS, ESPHOME_NOISE_PSK if the device is configured for encryption,
and ESPHOME_PASSWORD if API password authentication is configured.
This script intentionally does not assume credentials or trigger an OTA update.
"""
import asyncio
import os
import sys
from aioesphomeapi import APIClient

ADDRESS = os.environ.get("ESPHOME_ADDRESS", "192.168.0.8")
PORT = int(os.environ.get("ESPHOME_PORT", "6053"))
VALUE = int(os.environ.get("GRV006_VALUE", "120"))
PASSWORD = os.environ.get("ESPHOME_PASSWORD", "")
NOISE_PSK = os.environ.get("ESPHOME_NOISE_PSK", "")

async def main():
    client = APIClient(
        ADDRESS, PORT,
        password=PASSWORD,
        noise_psk=NOISE_PSK or None,
    )
    try:
        await client.connect(login=True)
        print(f"CONNECTED: {ADDRESS}:{PORT}")
        states = {}
        ready = asyncio.Event()

        def on_state(state):
            states[state.key] = state
            if getattr(state, "name", "") == "GRV006 Echo Value":
                ready.set()

        client.subscribe_states(on_state)
        # API user actions are represented by the service-call API.
        # Service name is the action id declared in the candidate YAML.
        await client.execute_service(
            "grv006_set_value",
            {"value": VALUE},
        )
        try:
            await asyncio.wait_for(ready.wait(), timeout=10)
        except asyncio.TimeoutError:
            # Some API versions deliver the state before/after service response;
            # report clearly rather than claiming a pass.
            pass

        echoed = None
        for state in states.values():
            if getattr(state, "name", "") == "GRV006 Echo Value":
                echoed = getattr(state, "state", None)
                break
        if echoed is None:
            print("RESULT: INCONCLUSIVE — service called but echo state not observed")
            return 2
        print(f"SENT: {VALUE}")
        print(f"ECHOED: {echoed}")
        if int(float(echoed)) == VALUE:
            print("RESULT: PASS — sent value equals ESP echo")
            return 0
        print("RESULT: FAIL — sent value differs from ESP echo")
        return 1
    finally:
        client.disconnect()

if __name__ == "__main__":
    try:
        raise SystemExit(asyncio.run(main()))
    except Exception as exc:
        print(f"RESULT: ERROR — {type(exc).__name__}: {exc}", file=sys.stderr)
        raise
