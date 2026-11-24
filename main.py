"""Aica Houseplant Out-of-Office — make.fun entry.

Writes one out-of-office auto-reply, as if a houseplant sent it,
to /output/entry.txt (max 120 characters, one line).
Python standard library only.
"""

import os

ENTRY = (
    "Out of office: my human left for vacation and forgot I need water. "
    "Water me before I file a complaint with the sun."
)



def validate(text):
    """Check the entry meets the competition gate before writing it."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > 120:
        raise ValueError(f"entry is {len(text)} characters, over the 120 limit")
    return True


def main():
    validate(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
