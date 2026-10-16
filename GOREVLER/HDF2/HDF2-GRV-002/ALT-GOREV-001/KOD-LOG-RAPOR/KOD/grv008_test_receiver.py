#!/usr/bin/env python3
"""PROJE BERO GRV-008.2 candidate receiver and first-waveform plot.

Install: python3 -m pip install pyserial numpy matplotlib
Edit SERIAL_PORT before running. The ESP frame is 4040 bytes:
9 little-endian uint32 fields + 2000 uint16 samples + final uint32 marker.
"""
import csv
import struct
import time
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import serial

SERIAL_PORT = "/dev/cu.usbserial-REPLACE_ME"  # Mac Mini: edit to actual port
BAUD_RATE = 921600
SAMPLE_COUNT = 1000
MAX_FRAMES = 100
OUT_DIR = Path("grv008_capture")
START_MARKER = 0xDEADBEEF
END_MARKER = 0xCAFEBABE
START_BYTES = struct.pack("<I", START_MARKER)
# 9 x uint32 header, interleaved 1000*(SCT uint16, BIAS uint16), uint32 end marker
FRAME_FORMAT = f"<IIIIIIIII{SAMPLE_COUNT * 2}HI"
FRAME_SIZE = struct.calcsize(FRAME_FORMAT)  # 4040 bytes


def extract_frames(ser, max_frames):
    stream = bytearray()
    frames = []
    while len(frames) < max_frames:
        chunk = ser.read(max(1, min(4096, ser.in_waiting or 1)))
        if chunk:
            stream.extend(chunk)
        while len(stream) >= 4 and len(frames) < max_frames:
            start = stream.find(START_BYTES)
            if start < 0:
                # Keep final 3 bytes: marker may straddle serial-read boundaries.
                del stream[:-3]
                break
            if start:
                del stream[:start]
            if len(stream) < FRAME_SIZE:
                break
            packet = bytes(stream[:FRAME_SIZE])
            values = struct.unpack(FRAME_FORMAT, packet)
            if values[0] != START_MARKER or values[-1] != END_MARKER:
                del stream[:1]
                continue
            header = values[:9]
            raw = np.asarray(values[9:-1], dtype=np.uint16)
            frames.append({
                "start_marker": header[0], "frame_id": header[1],
                "sample_rate_hz": header[2], "sample_count": header[3],
                "start_micros": header[4], "end_micros": header[5],
                "dma_overflows": header[6], "raw_queue_overflows": header[7],
                "frame_queue_overflows": header[8],
                "sct": raw[0::2].copy(), "bias": raw[1::2].copy(),
            })
            del stream[:FRAME_SIZE]
            f = frames[-1]
            # ESP micros() is a wrapping uint32 counter; unsigned subtraction handles wrap.
            duration_us = (f["end_micros"] - f["start_micros"]) & 0xFFFFFFFF
            print(f"Frame {f['frame_id']:5d} | duration={duration_us:7d} us | "
                  f"DMA={f['dma_overflows']} rawQ={f['raw_queue_overflows']} "
                  f"frameQ={f['frame_queue_overflows']}")
    return frames


def save_and_plot(frames):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    csv_path = OUT_DIR / "grv008_raw_samples.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["frame_id", "sample_index", "sct_adc_raw", "bias_adc_raw"])
        for f in frames:
            for i, (sct, bias) in enumerate(zip(f["sct"], f["bias"])):
                writer.writerow([f["frame_id"], i, int(sct), int(bias)])

    durations = np.array([(f["end_micros"] - f["start_micros"]) & 0xFFFFFFFF for f in frames], dtype=np.uint64)
    print("\n--- GRV-008 test summary ---")
    print(f"Valid frames: {len(frames)} / {MAX_FRAMES}")
    if len(durations):
        print(f"Mean frame duration: {durations.mean():.1f} us (nominal target ~100000 us)")
        print(f"Frame-duration standard deviation: {durations.std():.1f} us")
        print("Note: frame duration does NOT prove every sample interval is 100 us.")
    last = frames[-1]
    print(f"Final cumulative counters: DMA={last['dma_overflows']}, "
          f"raw queue={last['raw_queue_overflows']}, frame queue={last['frame_queue_overflows']}")
    print(f"BIAS mean (raw ADC counts, first frame): {frames[0]['bias'].mean():.2f}")
    print(f"BIAS standard deviation (raw ADC counts, first frame): {frames[0]['bias'].std():.2f}")
    print(f"Raw CSV: {csv_path.resolve()}")

    # First 5 SCT and BIAS waveforms, raw ADC counts only; no calibration or filtering.
    fig, axes = plt.subplots(5, 1, figsize=(12, 10), sharex=True)
    for i, ax in enumerate(axes):
        if i >= len(frames):
            ax.set_visible(False)
            continue
        x = np.arange(SAMPLE_COUNT)
        ax.plot(x, frames[i]["sct"], label="SCT raw")
        ax.plot(x, frames[i]["bias"], label="BIAS raw", alpha=0.8)
        ax.set_ylabel("ADC count")
        ax.set_title(f"Frame {frames[i]['frame_id']}")
        ax.grid(True, alpha=0.25)
        ax.legend(loc="upper right")
    axes[-1].set_xlabel("Sample index (not a verified time axis yet)")
    fig.tight_layout()
    plot_path = OUT_DIR / "first_five_frames.png"
    fig.savefig(plot_path, dpi=150)
    plt.show()
    print(f"Plot: {plot_path.resolve()}")


def main():
    print(f"GRV-008.2 candidate receiver | expected frame={FRAME_SIZE} bytes")
    print(f"Port={SERIAL_PORT} baud={BAUD_RATE}; waiting for {MAX_FRAMES} valid frames")
    try:
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=0.2) as ser:
            time.sleep(1.0)
            ser.reset_input_buffer()
            frames = extract_frames(ser, MAX_FRAMES)
    except KeyboardInterrupt:
        print("Stopped by user; no claim of complete test.")
        return
    except Exception as exc:
        print(f"Serial/receiver error: {exc}")
        print("Check SERIAL_PORT, permissions, cable, baud rate and ESP serial output.")
        return
    save_and_plot(frames)


if __name__ == "__main__":
    main()