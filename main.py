#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI.

Writes one single-line joke pickup line, under 200 characters,
aimed at a robot or an AI, to /output/entry.txt.
"""
import os

LINE = "If I pass your Turing test, do I get your number?"


def validate(text: str) -> None:
    """Mirror the bounty gate: 1-200 chars, one line, not blank."""
    if not text or text != text.strip():
        raise ValueError("entry must not be empty or padded with whitespace")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} chars, over the 200-char cap")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
