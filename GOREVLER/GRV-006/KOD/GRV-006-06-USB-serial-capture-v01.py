#!/usr/bin/env python3
"""GRV-006: capture ESPHome serial logs over USB and extract emitted CSV rows.

Usage:
  python3 -m pip install pyserial
  python3 GRV-006-06-usb-serial-capture-v01.py --list
  python3 GRV-006-06-usb-serial-capture-v01.py --port /dev/cu.usbserial-XXXX

The script preserves every received serial line in a raw .log file. When the
firmware emits CSV_HEADER_PART_1, CSV_HEADER_PART_2 and channel rows, it also
writes the reconstructed rows to a separate CSV. It does not flash firmware.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
import time
from datetime import datetime
from pathlib import Path

try:
    import serial
    from serial.tools import list_ports
except ImportError:
    print("MISSING_DEPENDENCY: install with: python3 -m pip install pyserial", file=sys.stderr)
    raise SystemExit(2)

DEFAULT_BAUD = 115200
HEADER_MARKER = re.compile(r"CSV_HEADER_PART_([12])\|(.*)$")
PAYLOAD_MARKER = re.compile(r"\]:\s?(.*)$")\nANSI_ESCAPE = re.compile(r"\x1b\[[0-?]*[ -/]*[@-~]")
DATA_START = re.compile(r"^esp32d1_\d+_\d+,")


def available_ports() -> None:
    ports = list(list_ports.comports())
    if not ports:
        print("NO_SERIAL_PORTS_FOUND")
        return
    for port in ports:
        print(f"{port.device}\t{port.description}")


def payload_of(line: str) -> str:
    match = PAYLOAD_MARKER.search(line)
    payload = match.group(1) if match else line\n    return ANSI_ESCAPE.sub("", payload).strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Capture ESPHome USB serial log and extract CSV rows.")
    parser.add_argument("--port", help="Serial port, e.g. /dev/cu.usbserial-XXXX or /dev/cu.SLAB_USBtoUART")
    parser.add_argument("--baud", type=int, default=DEFAULT_BAUD)
    parser.add_argument("--outdir", default=".", help="Output directory (default: current directory)")
    parser.add_argument("--seconds", type=float, default=0, help="Stop after N seconds; 0 means Ctrl-C to stop")
    parser.add_argument("--list", action="store_true", help="List available serial ports and exit")
    args = parser.parse_args()

    if args.list:
        available_ports()
        return 0
    if not args.port:
        parser.error("--port is required unless --list is used")

    outdir = Path(args.outdir).expanduser()
    outdir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    raw_path = outdir / f"GRV-006-06-USB-{stamp}.log"
    csv_path = outdir / f"GRV-006-06-USB-{stamp}.csv"

    header_parts: dict[int, list[str]] = {}
    csv_writer = None
    csv_file = None
    rows_written = 0
    started = time.monotonic()
    print(f"PORT: {args.port}")
    print(f"BAUD: {args.baud}")
    print(f"RAW_LOG: {raw_path}")
    print(f"CSV_OUTPUT: {csv_path}")
    print("CAPTURE: running; press Ctrl-C to stop")

    try:
        with serial.Serial(args.port, args.baud, timeout=1) as device, raw_path.open(
            "w", encoding="utf-8", newline=""
        ) as raw_file:
            # Do not toggle DTR/RTS deliberately; some ESP32 boards reset when these change.
            while True:
                if args.seconds and time.monotonic() - started >= args.seconds:
                    break
                data = device.readline()
                if not data:
                    continue
                line = data.decode("utf-8", errors="replace").rstrip("\r\n")
                raw_file.write(line + "\n")
                raw_file.flush()
                print(line, flush=True)

                payload = payload_of(line)
                marker = HEADER_MARKER.search(payload)
                if marker:
                    part = int(marker.group(1))
                    header_parts[part] = next(csv.reader([marker.group(2)]))
                    if 1 in header_parts and 2 in header_parts and csv_writer is None:
                        csv_file = csv_path.open("w", encoding="utf-8", newline="")
                        csv_writer = csv.writer(csv_file)
                        csv_writer.writerow(header_parts[1] + header_parts[2])
                        csv_file.flush()
                        print(f"CSV_HEADER: WRITTEN ({len(header_parts[1] + header_parts[2])} columns)")
                    continue

                if DATA_START.match(payload):
                    if csv_writer is None:
                        print("CSV_ROW_SKIPPED: header parts not both received yet", file=sys.stderr)
                        continue
                    row = next(csv.reader([payload]))
                    expected = len(header_parts[1]) + len(header_parts[2])
                    if len(row) != expected:
                        print(f"CSV_COLUMN_MISMATCH: expected={expected} actual={len(row)} row={payload}", file=sys.stderr)
                        continue
                    csv_writer.writerow(row)
                    csv_file.flush()
                    rows_written += 1
                    print(f"CSV_ROW_WRITTEN: {rows_written}")
    except KeyboardInterrupt:
        print("\nCAPTURE_STOPPED: keyboard interrupt")
    except serial.SerialException as exc:
        print(f"SERIAL_ERROR: {exc}", file=sys.stderr)
        return 3
    finally:
        if csv_file is not None:
            csv_file.close()

    print(f"RAW_LOG_SAVED: {raw_path}")
    if csv_writer is None:
        print("CSV_RESULT: NO_COMPLETE_HEADER — raw log preserved")
        return 4
    print(f"CSV_SAVED: {csv_path}")
    print(f"CSV_ROWS: {rows_written}")
    print("RESULT: CAPTURE_COMPLETE — inspect column mismatch warnings and validate the CSV before processing")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
