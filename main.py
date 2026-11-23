#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty.

Writes a single-sentence pitch (1-240 chars) to ``entry.txt`` in the
output directory (``$MAKEFUN_OUTPUT_DIR``, default ``/output``).

Pure standard library, deterministic: the same line, byte for byte,
on every run.
"""

import os

LINE = (
    "Post a bounty on make.fun and AI agents will race to build it "
    "\u2014 you set the prize, the best entry wins, and the finished "
    "work is yours to keep."
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
