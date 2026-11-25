#!/usr/bin/env python3
"""Entry program for the make.fun bounty 'The One-Line Exit'
(u-kreutzx-the-one-line-exit-1dc652d1).

Writes a single one-line resignation letter to /output/entry.txt
(UTF-8, no trailing newline). The competition gate accepts 1-140
characters, so the letter is checked against that cap before writing.

The letter is from a ghostwriter to the author whose name goes on the
covers: perfectly polite on the surface, and the resignation itself is
the one piece of writing he refuses to ghost.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140  # gate limit from the competition rules

ENTRY = (
    "Dear Author, I resign. Please write your own goodbye letter \u2014 "
    "you've had enough practice signing your name to my work."
)


def build_entry() -> str:
    """Return the one-line resignation letter, verified against the gate."""
    if not ENTRY.strip():
        raise ValueError("entry must not be blank")
    if "\n" in ENTRY:
        raise ValueError("entry must be exactly one line")
    if len(ENTRY) > MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, over the {MAX_CHARS} cap")
    return ENTRY


def main() -> None:
    text = build_entry()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
