"""One Line, Big Laugh — a single hilarious line, on its own.

The entry is one line of at most 200 characters. This program validates
the line (single line, within the limit) and writes it, byte for byte,
to entry.txt inside MAKEFUN_OUTPUT_DIR, so the grader can read exactly
what the judge will read. No network, no randomness, no clock: the same
input always produces the same output file.
"""

import os
import sys

LINE = (
    "My grandma joined a group chat and ended a three-year family feud "
    "with one voice note that just said: 'I can see all of you. Behave.'"
)

MAX_CHARS = 200


def main() -> int:
    if len(LINE) > MAX_CHARS:
        print(f"line is {len(LINE)} chars, over the {MAX_CHARS} limit", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("line must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Round-trip check: what the grader reads must be exactly the line.
    with open(out_path, encoding="utf-8", newline="") as f:
        if f.read() != LINE:
            print("entry.txt does not match the line", file=sys.stderr)
            return 1
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
