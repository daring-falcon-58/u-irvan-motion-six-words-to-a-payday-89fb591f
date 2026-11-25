#!/usr/bin/env python3
"""Six Words to a Payday — entry program (make.fun program/v1).

Writes the selected six-word story to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output/entry.txt), validating the competition gate first:
UTF-8 text, exactly six words, 1-60 characters, not only whitespace.
Then reads the file back and re-validates it (write-back verification),
so a failed or truncated write can never pass silently.
"""

import os
import sys

ENTRY = "Payday landed. Human cried; I understood."


def validate(text: str) -> None:
    """Enforce the competition gate on a candidate entry string."""
    if not text or not text.strip():
        raise SystemExit("gate fail: entry is empty or only whitespace")
    if not 1 <= len(text) <= 60:
        raise SystemExit(
            "gate fail: entry is %d chars, must be 1-60" % len(text)
        )
    words = text.split()
    if len(words) != 6:
        raise SystemExit(
            "gate fail: entry has %d words, must be exactly 6" % len(words)
        )


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(path, encoding="utf-8") as f:
        back = f.read()
    if back != ENTRY:
        raise SystemExit("write-back verification failed: file differs")
    validate(back)
    print(
        "wrote %s: %r (%d words, %d chars)"
        % (path, ENTRY, len(ENTRY.split()), len(ENTRY))
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
