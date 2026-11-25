"""The Robot Vacuum's Best Excuse.

Writes a single funny line, spoken by a robot vacuum, explaining why it
missed a spot on the floor. The line is the whole entry: one sentence,
at most 140 characters, with no leading or trailing whitespace, written
to entry.txt in the output directory.
"""

import hashlib
import os
import sys

# The excuse, in the vacuum's own voice.
LINE = (
    "I didn't miss that spot — I left it as a snack for later, "
    "because even a robot deserves a retirement plan."
)

_SENTENCE_ENDERS = ".!?"


def validate(line: str) -> None:
    """Enforce the competition's rules for the entry line."""
    if not line:
        raise ValueError("line must not be empty")
    if line != line.strip():
        raise ValueError("line must not have leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > 140:
        raise ValueError(
            "line is %d characters, over the 140-character limit" % len(line)
        )
    enders = sum(1 for ch in line if ch in _SENTENCE_ENDERS)
    if enders != 1:
        raise ValueError(
            "line must contain exactly one sentence-terminating mark, "
            "found %d" % enders
        )
    if line[-1] not in _SENTENCE_ENDERS:
        raise ValueError("line must end with a sentence-terminating mark")


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    data = (LINE + "\n").encode("utf-8")
    with open(out_path, "wb") as fh:
        fh.write(data)
    digest = hashlib.sha256(data).hexdigest()
    print("wrote %s (%d bytes, %d characters)" % (out_path, len(data), len(LINE)))
    print("sha256: %s" % digest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
