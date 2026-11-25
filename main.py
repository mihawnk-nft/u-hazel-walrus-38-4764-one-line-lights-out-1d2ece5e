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


def validate_entry(text: str) -> str:
    """Hold the line to the sealed gate: UTF-8 text, 1-200 chars, not blank."""
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(cleaned) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(cleaned)}")
    cleaned.encode("utf-8")  # raises if not valid UTF-8 text
    return cleaned


def main() -> None:
    text = validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
