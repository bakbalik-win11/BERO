#!/usr/bin/env python3
"""Require PREBERO STATUS and a structured session closeout on PRs."""

from __future__ import annotations

import os
import re
import subprocess
import sys

PROJECT = "PROJELER/PREBERO/"
STATUS = PROJECT + "STATUS.md"
LOG = PROJECT + "HISTORY/SESSION_LOG.md"
REQUIRED_LABELS = (
    "**Durum:**",
    "**Hedef ve kabul ölçütü:**",
    "**Yapılan:**",
    "**Doğrulama:**",
    "**Açık kalanlar:**",
    "**Sonraki adım:**",
    "**Kanıt:**",
)


def git(*args: str) -> str:
    result = subprocess.run(["git", *args], check=False, capture_output=True, text=True)
    if result.returncode:
        sys.stderr.write(result.stderr)
        raise SystemExit(result.returncode)
    return result.stdout


def main() -> int:
    base = os.environ.get("BASE_SHA", "").strip()
    if not base or base == "null":
        print("ERROR: BASE_SHA is missing; cannot compare the PR base.")
        return 2

    changed = set(git("diff", "--name-only", f"{base}...HEAD").splitlines())
    project_changes = sorted(p for p in changed if p.startswith(PROJECT))
    if not project_changes:
        print("No PREBERO files changed; session-close check is not applicable.")
        return 0

    missing = [p for p in (STATUS, LOG) if p not in changed]
    if missing:
        print("FAIL: A PR touching PREBERO must update:")
        for path in missing:
            print(f"  - {path}")
        return 1

    added_diff = git("diff", "--unified=0", f"{base}...HEAD", "--", LOG)
    added_lines = [line[1:] for line in added_diff.splitlines() if line.startswith("+") and not line.startswith("+++")]
    added_text = "\n".join(added_lines)
    sections = list(re.finditer(r"(?m)^## \d{4}-\d{2}-\d{2} — .+$", added_text))
    if not sections:
        print("FAIL: SESSION_LOG.md must include a new dated heading in this PR.")
        return 1

    latest_start = sections[-1].end()
    next_heading = re.search(r"(?m)^## ", added_text[latest_start:])
    latest_entry = added_text[latest_start:latest_start + next_heading.start()] if next_heading else added_text[latest_start:]
    absent = [label for label in REQUIRED_LABELS if label not in latest_entry]
    if absent:
        print("FAIL: The new session-log entry is missing required fields:")
        for label in absent:
            print(f"  - {label}")
        return 1

    with open(STATUS, encoding="utf-8") as status_file:
        status_content = status_file.read()
    if len(status_content.strip()) < 100:
        print("FAIL: STATUS.md is unexpectedly empty or too short.")
        return 1

    print("PASS: PREBERO STATUS.md and dated session closeout are present.")
    print(f"PREBERO files changed: {len(project_changes)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
