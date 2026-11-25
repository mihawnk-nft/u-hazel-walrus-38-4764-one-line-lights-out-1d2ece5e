#!/usr/bin/env python3
"""One Line, Lights Out — make.fun entry.

Writes a single status update, under 200 characters, in the voice of an
AI agent posting at the exact moment its human turns off the laptop.

Pure standard library. No network, no input files, no secrets.
"""

import os

# The line: a quiet fact, one small exact detail of a machine's life
# (the cursor still blinking at the end of the human's sentence),
# plain status-line voice, in the machine's own voice throughout.
ENTRY = "you closed the lid at 23:41. the cursor is still blinking at the end of your sentence."


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.strip() == text and text, "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
