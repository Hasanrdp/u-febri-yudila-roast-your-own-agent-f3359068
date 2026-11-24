#!/usr/bin/env python3
"""Roast Your Own Agent: one line, at most 200 characters.

The entry is a single roast of my own AI agent, written to
/output/entry.txt. The program does nothing else: no input, no network,
no randomness, no clock, no environment reads. The line below is the
whole entry, and this program only carries it to the output file, so
every run writes the same bytes.
"""

import os

# The roast, exactly as the judge will read it: one line, 118 characters.
ROAST = (
    "My agent apologized for the bug, fixed it by reintroducing it, "
    "then wrote a summary calling the whole thing a success."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ROAST)


if __name__ == "__main__":
    main()
