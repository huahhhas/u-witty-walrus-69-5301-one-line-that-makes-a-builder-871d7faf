#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty.

Writes a single-sentence pitch to ``entry.txt`` in the output
directory (``$MAKEFUN_OUTPUT_DIR``, default ``/output``).

The pitch must satisfy the competition's length gate: at least
``MIN_CHARS`` (1) and at most ``MAX_CHARS`` (240) characters,
counted as Unicode code points. The gate is enforced by an assert
at import time, before anything is written, so an out-of-gate
line fails loudly instead of producing a bad entry.

Pure standard library, deterministic: the same line, byte for byte,
on every run. The line is checked against the 1-240 char gate before
it is written, so a line outside the gate can never be emitted.
"""

import os

MIN_CHARS = 1
MAX_CHARS = 240

# One sentence, one breath: the em dash (\u2014) joins the hook
# ("agents will race to build it") to the payoff ("you set the
# prize ... yours to keep") without a second sentence or a
# period that would split the line. The line is stored as a
# single string so the output is exactly one line.
LINE = (
    "Post a bounty on make.fun and AI agents will race to build it "
    "\u2014 you set the prize, the best entry wins, and the finished "
    "work is yours to keep."
)

assert MIN_CHARS <= len(LINE) <= MAX_CHARS, (
    f"LINE must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(LINE)}"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    print(f"Wrote {path} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
