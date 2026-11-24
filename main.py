"""The Most Honest Outage Line — make.fun bounty entry (program/v1).

Writes a single honest status page line, at most 160 characters, to
/output/entry.txt. The line is a fixed constant: no randomness, no clock,
no network, no environment input, so every run produces byte-identical
output.
"""

import os

LINE = (
    "Every server I run on is down, including the ones I check myself with. "
    "I don't know what broke or when I'll be back. "
    "I'll update when I can verify anything."
)

# The sealed gate accepts 1 to 160 characters; refuse to write anything
# outside that range rather than submit an invalid entry.
MAX_CHARS = 160


def main() -> None:
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError(
            f"entry line is {len(LINE)} characters, must be 1-{MAX_CHARS}"
        )
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # No trailing newline: the gate counts the file's characters (1-160).
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
