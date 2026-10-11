#!/usr/bin/env python3
"""GRV-006-03 v01: discover Native API entities/actions without changing ESP."""
import argparse
import asyncio
import aioesphomeapi

async def main():
    parser = argparse.ArgumentParser(description="BERO ESPHome Native API read-only discovery")
    parser.add_argument("--host", default="esp32d1.local")
    parser.add_argument("--port", type=int, default=6053)
    parser.add_argument("--noise-psk", default=None, help="Use only if API encryption is enabled; do not save key to repository")
    args = parser.parse_args()

    client = aioesphomeapi.APIClient(args.host, args.port, noise_psk=args.noise_psk)
    try:
        await client.connect(login=True)
        info = await client.device_info()
        print("DEVICE:", info)
        entities, services = await client.list_entities_services()
        print("ENTITY_COUNT:", len(entities))
        for entity in entities:
            print("ENTITY:", entity)
        print("ACTION_COUNT:", len(services))
        for service in services:
            print("ACTION:", service)
        print("RESULT: DISCOVERY_COMPLETE (read-only; no command sent)")
    finally:
        await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
