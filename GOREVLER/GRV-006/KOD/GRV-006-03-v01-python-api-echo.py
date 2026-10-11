#!/usr/bin/env python3
"""GRV-006-03: send one integer through ESPHome Native API and verify echoed state.

Requires Python 3.10+ and aioesphomeapi.
Install in a virtual environment: python3 -m pip install aioesphomeapi

Environment:
  ESPHOME_ADDRESS       device IP/hostname (default 192.168.0.9)
  ESPHOME_PORT          Native API port (default 6053)
  ESPHOME_NOISE_PSK     API encryption key, if encryption is enabled
  GRV006_VALUE          integer to send (default 120)

ESPHome 2026.1+ no longer supports API password authentication; this script
uses the optional encryption key and does not embed credentials.
"""
import asyncio
import os
import sys
import aioesphomeapi

ADDRESS = os.environ.get("ESPHOME_ADDRESS", "192.168.0.9")
PORT = int(os.environ.get("ESPHOME_PORT", "6053"))
VALUE = int(os.environ.get("GRV006_VALUE", "120"))
NOISE_PSK = os.environ.get("ESPHOME_NOISE_PSK") or None
ECHO_NAME = "GRV006 Echo Value"
ACTION_NAME = "grv006_set_value"

async def main() -> int:
    client = aioesphomeapi.APIClient(ADDRESS, PORT, noise_psk=NOISE_PSK)
    try:
        await client.connect(login=True)
        print(f"CONNECTED: {ADDRESS}:{PORT}")
        entities, services = await client.list_entities_services()

        echo_entity = next((e for e in entities if getattr(e, "name", "") == ECHO_NAME), None)
        action = next((s for s in services if getattr(s, "name", "") == ACTION_NAME), None)

        if echo_entity is None:
            print(f"RESULT: ERROR — entity not found: {ECHO_NAME}")
            return 2
        if action is None:
            print(f"RESULT: ERROR — action not found: {ACTION_NAME}")
            return 2

        echo_value = {"value": None}
        changed = asyncio.Event()

        def on_state(state):
            if getattr(state, "key", None) == echo_entity.key:
                echo_value["value"] = getattr(state, "state", None)
                changed.set()

        client.subscribe_states(on_state)
        # Give the initial state subscription a moment to deliver the state,
        # then issue the action through the UserService descriptor discovered above.
        await asyncio.sleep(0.5)
        changed.clear()
        await client.execute_service(action, {"value": VALUE})
        try:
            await asyncio.wait_for(changed.wait(), timeout=10)
        except asyncio.TimeoutError:
            print("RESULT: INCONCLUSIVE — action sent but echo state update not received")
            return 3

        echoed = echo_value["value"]
        print(f"SENT: {VALUE}")
        print(f"ECHOED: {echoed}")
        if echoed is not None and int(float(echoed)) == VALUE:
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
