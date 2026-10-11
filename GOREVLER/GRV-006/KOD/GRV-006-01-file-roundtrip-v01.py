#!/usr/bin/env python3
"""GRV-006-01: write a deterministic CSV, read it back, process, reread, verify."""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "GRV-006-01-ham-veri.csv"
OUTPUT = ROOT / "GRV-006-01-islenmis-veri.csv"

# Explicitly synthetic starter data; this proves file/data handling, not sensor accuracy.
source_rows = [
    {"sample_id": "S001", "value": 10},
    {"sample_id": "S002", "value": 20},
    {"sample_id": "S003", "value": 30},
]

with SOURCE.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["sample_id", "value"])
    writer.writeheader()
    writer.writerows(source_rows)

print(f"SOURCE_WRITTEN: {SOURCE.name} ({SOURCE.stat().st_size} bytes)")

# Read from the actual file, not from the original in-memory list.
with SOURCE.open("r", newline="", encoding="utf-8") as f:
    reread_rows = list(csv.DictReader(f))

assert len(reread_rows) == 3
assert [r["sample_id"] for r in reread_rows] == ["S001", "S002", "S003"]
values = [int(r["value"]) for r in reread_rows]
processed_rows = [
    {"sample_id": row["sample_id"], "value": int(row["value"]), "double_value": int(row["value"]) * 2}
    for row in reread_rows
]

with OUTPUT.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["sample_id", "value", "double_value"])
    writer.writeheader()
    writer.writerows(processed_rows)
print(f"OUTPUT_WRITTEN: {OUTPUT.name} ({OUTPUT.stat().st_size} bytes)")

# Reread processed output from disk.
with OUTPUT.open("r", newline="", encoding="utf-8") as f:
    final_rows = list(csv.DictReader(f))

# Independent expected-value calculation, separate from the row transformation above.
expected_sum = 2 * (10 + 20 + 30)
actual_sum = sum(int(row["double_value"]) for row in final_rows)
assert len(final_rows) == 3
assert actual_sum == expected_sum == 120
assert [int(r["double_value"]) for r in final_rows] == [20, 40, 60]

print("SOURCE_REREAD: PASS (3 rows; values=10,20,30)")
print("PROCESSING: PASS (double each value)")
print("OUTPUT_REREAD: PASS (3 rows; doubled_values=20,40,60)")
print(f"INDEPENDENT_CHECK: PASS (expected_sum={expected_sum}; output_sum={actual_sum})")
print("RESULT: PASS — GRV-006-01 file round-trip and Python processing demonstrated")
print("LIMIT: synthetic data only; no ESP communication or sensor-accuracy claim")
