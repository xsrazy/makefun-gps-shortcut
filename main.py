"""The GPS Swears It Was a Shortcut - make.fun entry.

Writes the GPS's own one-line excuse for sending the driver down the
wrong road to <output dir>/entry.txt. The line is a single plain-text
line of at most 200 characters, with no trailing newline.

The excuse is written in the GPS's own voice: smug and defensive,
caught red-handed and blaming the map, with a fresh specific detail
(a cul-de-sac, a wedding, a lake) instead of the stale recalculating
joke. The gate only accepts UTF-8 text of 1 to 200 characters, so the
entry is validated against those bounds before it is written.
"""

import os
from pathlib import Path

ENTRY = (
    "The map swore that cul-de-sac was a shortcut to your cousin's "
    "wedding, so I believed it, and honestly the lake looks lovely "
    "from here."
)


def validate_entry(text):
    """Check the excuse against the gate: one line, 1-200 chars."""
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def write_entry(output_dir):
    """Write the excuse as one line with no trailing newline."""
    validate_entry(ENTRY)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(ENTRY, encoding="utf-8")
    os.chmod(entry_path, 0o644)
    os.chmod(output_dir, 0o755)
    return entry_path


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(output_dir)


if __name__ == "__main__":
    main()
