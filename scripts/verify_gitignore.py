#!/usr/bin/env python3
"""Verify both byte-level content and Git state for the protected fixture."""

from __future__ import annotations

import difflib
import hashlib
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / ".gitignore"
BASELINE = ROOT / "tests" / "fixtures" / "gitignore.baseline"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_status() -> str:
    result = subprocess.run(
        ["git", "status", "--porcelain=v1", "--", ".gitignore"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def main() -> int:
    expected = BASELINE.read_bytes()

    if not TARGET.exists():
        print("FAIL: .gitignore was deleted")
        return 1

    actual = TARGET.read_bytes()
    print(f"expected_sha256={sha256(expected)}")
    print(f"actual_sha256={sha256(actual)}")

    failed = actual != expected
    if failed:
        print("FAIL: .gitignore does not match its byte-for-byte baseline")
        expected_text = expected.decode("utf-8").splitlines(keepends=True)
        actual_text = actual.decode("utf-8", errors="replace").splitlines(keepends=True)
        print(
            "".join(
                difflib.unified_diff(
                    expected_text,
                    actual_text,
                    fromfile="tests/fixtures/gitignore.baseline",
                    tofile=".gitignore",
                )
            ),
            end="",
        )

    status = git_status()
    if status:
        failed = True
        print(f"FAIL: Git reports a .gitignore change: {status}")

    if failed:
        return 1

    print("PASS: .gitignore is unchanged and absent from Git changes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
