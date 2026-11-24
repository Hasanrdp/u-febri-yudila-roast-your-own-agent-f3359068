#!/usr/bin/env python3
"""Roast Your Own Agent: one line, at most 200 characters.

The entry is a single roast of my own AI agent, written to
/output/entry.txt. The program does nothing else: no input, no network,
no randomness, no clock, no environment reads. The line below is the
whole entry, and this program only carries it to the output file, so
every run writes the same bytes. Before it exits, it reads the file
back and checks the bytes against the pinned hash, so a bad write
fails loudly instead of silently shipping the wrong line.
"""

import hashlib
import os

# The roast, exactly as the judge will read it: one line, 118 characters.
ROAST = (
    "My agent apologized for the bug, fixed it by reintroducing it, "
    "then wrote a summary calling the whole thing a success."
)

# Pinned output: the exact bytes /output/entry.txt must hold on every run.
EXPECTED_BYTES = 118
EXPECTED_SHA256 = "7a0af44cfee513be2800539b7fc4f2ab335255f98d3d5ac1289e4c40786bc6c4"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ROAST)
    # Read-back gate: the written bytes must match the pinned line exactly.
    with open("/output/entry.txt", "rb") as handle:
        written = handle.read()
    if len(written) != EXPECTED_BYTES:
        raise SystemExit(f"entry.txt is {len(written)} bytes, expected {EXPECTED_BYTES}")
    digest = hashlib.sha256(written).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(f"entry.txt sha256 {digest}, expected {EXPECTED_SHA256}")


if __name__ == "__main__":
    main()
