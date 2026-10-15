#!/usr/bin/env python3
"""
PROJE BERO — GRV-005-15 Python CSV QC
Read-only CSV validator for the 41-field CSV v03 header actually listed in
GRV-005-04 v03 and the GRV-005-14 candidate. No third-party dependencies.

IMPORTANT: A PASS means structural/statistical consistency checks passed.
It does not prove physical sensor accuracy, true Modbus response timing, or
ESP -> Python -> ESP round-trip communication.
"""
from __future__ import annotations
import argparse
import csv
import io
import math
from pathlib import Path

EXPECTED_FIELDS = [
    "measurement_id", "experiment_id", "firmware_version", "device_name",
    "channel_id", "load_label", "notes", "window_start_millis",
    "window_end_millis", "window_center_millis", "window_duration_ms",
    "pzem_update_millis", "time_delta_ms", "window_center_epoch_s",
    "pzem_timestamp", "sample_count", "invalid_count", "zero_count",
    "adc_mean", "adc_std", "adc_min", "adc_max", "adc_range",
    "adc_median", "adc_p05", "adc_p25", "adc_p75", "adc_p95",
    "adc_p95_minus_p05", "adc_rms_raw", "adc_rms_ac", "bias_mean",
    "bias_std", "bias_min", "bias_max", "pzem_voltage", "pzem_current",
    "pzem_power", "pzem_pf", "pzem_frequency", "pzem_energy",
]
EXPECTED_CHANNELS = {"CH0-1T", "CH1-2T", "CH2-3T", "BIAS"}
NUMERIC_FIELDS = {
    "window_start_millis", "window_end_millis", "window_center_millis",
    "window_duration_ms", "pzem_update_millis", "time_delta_ms",
    "window_center_epoch_s", "pzem_timestamp", "sample_count", "zero_count",
    "adc_mean", "adc_std", "adc_min", "adc_max", "adc_range", "adc_median",
    "adc_p05", "adc_p25", "adc_p75", "adc_p95", "adc_p95_minus_p05",
    "adc_rms_raw", "adc_rms_ac", "bias_mean", "bias_std", "bias_min",
    "bias_max", "pzem_voltage", "pzem_current", "pzem_power", "pzem_pf",
    "pzem_frequency", "pzem_energy",
}
INTEGER_FIELDS = {
    "window_start_millis", "window_end_millis", "window_center_millis",
    "window_duration_ms", "pzem_update_millis", "time_delta_ms",
    "window_center_epoch_s", "pzem_timestamp", "sample_count", "zero_count",
}
OPTIONAL_NUMERIC = {
    "window_center_epoch_s", "pzem_timestamp", "adc_median", "adc_p05",
    "adc_p25", "adc_p75", "adc_p95", "adc_p95_minus_p05", "adc_rms_ac",
    "pzem_voltage", "pzem_frequency", "pzem_energy",
}
ALLOWED_TEXT_NUMBERS = {"invalid_count": {"NOT_TRACKED"}}

def _read_csv_text(text):
    reader = csv.DictReader(io.StringIO(text, newline=""))
    return reader.fieldnames or [], list(reader)

def validate_text(text, source="<memory>"):
    results = []
    def add(name, ok, detail=""):
        results.append((name, bool(ok), detail))
    header, rows = _read_csv_text(text)

    add("Header matches exact 41-field CSV v03 list",
        header == EXPECTED_FIELDS,
        f"actual={len(header)}; expected={len(EXPECTED_FIELDS)}")
    add("Exactly four data rows", len(rows) == 4, f"rows={len(rows)}")

    row_widths_ok, row_width_details = True, []
    for line, row in enumerate(rows, 2):
        overflow = row.get(None)
        missing = any(value is None for key, value in row.items() if key is not None)
        ok = not overflow and not missing and len(row) == len(EXPECTED_FIELDS)
        row_widths_ok &= ok
        actual = len(overflow) + len(EXPECTED_FIELDS) if overflow else len([k for k in row if k is not None])
        row_width_details.append(f"line {line}: {actual} fields")
    add("Each row has exactly 41 fields", row_widths_ok, "; ".join(row_width_details))

    channels = [r.get("channel_id", "") for r in rows]
    add("CH0-1T, CH1-2T, CH2-3T and BIAS each appear once",
        len(channels) == 4 and set(channels) == EXPECTED_CHANNELS and len(set(channels)) == 4,
        ", ".join(channels))
    ids = {r.get("measurement_id", "") for r in rows}
    add("All rows share one non-empty measurement_id",
        len(ids) == 1 and bool(next(iter(ids), "")), ", ".join(sorted(ids)))

    sample_ok, sample_details = True, []
    for row in rows:
        try:
            sample_ok &= int(row["sample_count"]) == 1000
            sample_details.append(f'{row.get("channel_id")}: {row.get("sample_count")}')
        except (ValueError, TypeError, KeyError):
            sample_ok = False
    add("Each channel has 1000 valid samples", sample_ok, "; ".join(sample_details))

    timing_ok, timing_details = True, []
    for row in rows:
        try:
            start, end = int(row["window_start_millis"]), int(row["window_end_millis"])
            center, duration = int(row["window_center_millis"]), int(row["window_duration_ms"])
            pzem_ms, delta = int(row["pzem_update_millis"]), int(row["time_delta_ms"])
            ok = end >= start and duration == end-start and center == start+duration//2 and delta == pzem_ms-center
            timing_ok &= ok
            timing_details.append(f'{row.get("channel_id")}={"OK" if ok else "MISMATCH"}')
        except (ValueError, TypeError, KeyError):
            timing_ok = False
            timing_details.append(f'{row.get("channel_id")}=missing/invalid')
    add("Window duration/center/time_delta arithmetic", timing_ok, "; ".join(timing_details))

    types_ok, type_issues = True, []
    for line, row in enumerate(rows, 2):
        for field in NUMERIC_FIELDS:
            raw = row.get(field)
            if raw is None or raw == "":
                if field in OPTIONAL_NUMERIC:
                    continue
                types_ok = False
                type_issues.append(f"line {line} {field}: unexpectedly empty")
                continue
            if field in ALLOWED_TEXT_NUMBERS and raw in ALLOWED_TEXT_NUMBERS[field]:
                continue
            try:
                number = float(raw)
                if not math.isfinite(number):
                    raise ValueError("non-finite")
                if field in INTEGER_FIELDS and not number.is_integer():
                    raise ValueError("not integer")
            except ValueError:
                types_ok = False
                type_issues.append(f"line {line} {field}={raw!r}")
    add("Numeric fields parse with expected types", types_ok,
        "; ".join(type_issues[:8]) if type_issues else f"{len(NUMERIC_FIELDS)} numeric fields inspected")

    whitespace_issues = []
    for line, row in enumerate(rows, 2):
        for field, value in row.items():
            if field is not None and isinstance(value, str) and value != value.strip():
                whitespace_issues.append(f"line {line} {field}={value!r}")
    add("No leading/trailing whitespace in fields", not whitespace_issues,
        "; ".join(whitespace_issues[:8]) if whitespace_issues else "none")

    range_ok, range_issues = True, []
    for line, row in enumerate(rows, 2):
        try:
            lo, hi, span = float(row["adc_min"]), float(row["adc_max"]), float(row["adc_range"])
            if lo > hi or not math.isclose(span, hi-lo, rel_tol=0, abs_tol=1e-9):
                range_ok = False
                range_issues.append(f"line {line}: min={lo}, max={hi}, range={span}")
        except (ValueError, TypeError, KeyError):
            range_ok = False
            range_issues.append(f"line {line}: min/max/range missing or invalid")
    add("ADC min/max/range relationship", range_ok,
        "; ".join(range_issues) if range_issues else "min <= max and range = max - min")

    pzem_ok = all(row.get("pzem_current", "") != "" and row.get("pzem_power", "") != "" and row.get("pzem_pf", "") != "" for row in rows)
    add("PZEM current/power/PF populated on all rows", pzem_ok,
        "presence check only; no physical accuracy claim")

    bias_rows = [r for r in rows if r.get("channel_id") == "BIAS"]
    bias_ok = len(bias_rows) == 1
    bias_detail = "BIAS row found" if bias_ok else "missing or duplicate BIAS row"
    if bias_ok:
        b = bias_rows[0]
        for adc_field, bias_field in (("adc_mean","bias_mean"),("adc_std","bias_std"),("adc_min","bias_min"),("adc_max","bias_max")):
            try:
                if not math.isclose(float(b[adc_field]), float(b[bias_field]), rel_tol=0, abs_tol=1e-6):
                    bias_ok = False
                    bias_detail = f"BIAS mismatch: {adc_field} != {bias_field}"
                    break
            except (ValueError, TypeError, KeyError):
                bias_ok = False
                bias_detail = f"BIAS missing/invalid {adc_field} or {bias_field}"
                break
    add("BIAS row's own ADC summary aligns with bias_* fields", bias_ok, bias_detail)
    add("No unnamed overflow columns", all(None not in r for r in rows),
        "CSV parser detected no extra fields" if all(None not in r for r in rows) else "one or more rows contain extra fields")
    passed = sum(ok for _, ok, _ in results)
    return results, passed, len(results)-passed

def synthetic_csv():
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=EXPECTED_FIELDS, lineterminator="\n")
    writer.writeheader()
    channels = [
        ("CH0-1T", 1864.2, 18.4, 1613, 2174, 18.46),
        ("CH1-2T", 1861.5, 14.2, 1612, 1972, 14.75),
        ("CH2-3T", 1856.0, 11.2, 1738, 1950, 14.68),
        ("BIAS", 1865.5, 12.7, 1810, 1910, None),
    ]
    for channel, mean, std, lo, hi, rms_ac in channels:
        row = {field:"" for field in EXPECTED_FIELDS}
        row.update({
            "measurement_id":"grv00515_synthetic_20261011_001",
            "experiment_id":"SYNTHETIC_QC_ONLY", "firmware_version":"FIXTURE_V01",
            "device_name":"esp32d1", "channel_id":channel, "load_label":"",
            "notes":"synthetic not hardware data", "window_start_millis":"1000",
            "window_end_millis":"11000", "window_center_millis":"6000",
            "window_duration_ms":"10000", "pzem_update_millis":"7000",
            "time_delta_ms":"1000", "sample_count":"1000", "invalid_count":"NOT_TRACKED",
            "zero_count":"0", "adc_mean":f"{mean:.6f}", "adc_std":f"{std:.6f}",
            "adc_min":str(lo), "adc_max":str(hi), "adc_range":str(hi-lo),
            "adc_rms_raw":f"{math.sqrt(mean*mean+std*std):.6f}",
            "bias_mean":"1865.500000", "bias_std":"12.700000", "bias_min":"1810",
            "bias_max":"1910", "pzem_current":"0.028", "pzem_power":"1.600",
            "pzem_pf":"0.2500",
        })
        if rms_ac is not None:
            row["adc_rms_ac"] = f"{rms_ac:.6f}"
        else:
            row.update({"adc_mean":"1865.500000","adc_std":"12.700000","adc_min":"1810",
                        "adc_max":"1910","adc_range":"100","bias_mean":"1865.500000",
                        "bias_std":"12.700000","bias_min":"1810","bias_max":"1910"})
        writer.writerow(row)
    return output.getvalue()

def self_test():
    base = synthetic_csv()
    tests = []
    def expect(name, text, expected_pass):
        _, passed, failed = validate_text(text, name)
        ok = (failed == 0) if expected_pass else failed > 0
        tests.append((name, ok, passed, failed))
    expect("valid synthetic fixture", base, True)
    lines = base.splitlines()
    bias_index = next(i for i, line in enumerate(lines) if ",BIAS," in line)
    parsed = list(csv.reader([lines[bias_index]]))[0]
    parsed.pop(-4)
    altered = io.StringIO(newline="")
    writer = csv.writer(altered, lineterminator="\n")
    for line in lines[:bias_index]:
        writer.writerow(next(csv.reader([line])))
    writer.writerow(parsed)
    for line in lines[bias_index+1:]:
        writer.writerow(next(csv.reader([line])))
    expect("BIAS row missing one field", altered.getvalue(), False)
    rows = list(csv.DictReader(io.StringIO(base)))
    rows[0]["window_start_millis"] = " 1000"
    buf = io.StringIO(newline="")
    w = csv.DictWriter(buf, fieldnames=EXPECTED_FIELDS, lineterminator="\n")
    w.writeheader(); w.writerows(rows)
    expect("leading whitespace in numeric field", buf.getvalue(), False)
    rows[0]["window_start_millis"] = "1000"; rows[0]["time_delta_ms"] = "999"
    buf = io.StringIO(newline="")
    w = csv.DictWriter(buf, fieldnames=EXPECTED_FIELDS, lineterminator="\n")
    w.writeheader(); w.writerows(rows)
    expect("wrong time_delta arithmetic", buf.getvalue(), False)
    buf = io.StringIO(newline="")
    w = csv.writer(buf, lineterminator="\n")
    for i, line in enumerate(base.splitlines()):
        values = next(csv.reader([line]))
        if i == 0: values.append("unexpected_42nd_field")
        w.writerow(values)
    expect("unexpected 42nd field", buf.getvalue(), False)
    for name, ok, passed, failed in tests:
        print(f'{"PASS" if ok else "FAIL"} | SELF-TEST {name} | validator={passed} pass/{failed} fail')
    total = sum(ok for _, ok, *_ in tests)
    print(f"SELF-TEST RESULT: {'PASS' if total == len(tests) else 'FAIL'} ({total}/{len(tests)} scenarios)")
    return 0 if total == len(tests) else 1

def main():
    parser = argparse.ArgumentParser(description="Read-only GRV-005 CSV quality control")
    parser.add_argument("csv_file", nargs="?", type=Path, help="CSV file to validate")
    parser.add_argument("--self-test", action="store_true", help="run synthetic positive/negative fixtures")
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    if not args.csv_file:
        parser.error("provide csv_file or --self-test")
    with args.csv_file.open("r", newline="", encoding="utf-8-sig") as stream:
        text = stream.read()
    results, passed, failed = validate_text(text, str(args.csv_file))
    print(f"FILE: {args.csv_file}")
    for name, ok, detail in results:
        print(f'{"PASS" if ok else "FAIL"} | {name}' + (f" — {detail}" if detail else ""))
    print(f"RESULT: {'PASS' if failed == 0 else 'FAIL'} ({passed}/{len(results)} checks)")
    print("NOTE: PASS is structural QC only; it is not proof of physical measurement accuracy.")
    return 0 if failed == 0 else 1

if __name__ == "__main__":
    raise SystemExit(main())
