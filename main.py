"""Entry for the make.fun ai-joke-03 competition.

Writes a single one-liner joke about AI coding agents to /output/entry.txt.
"""

import os

ENTRY_PATH = "/output/entry.txt"
ENTRY_DIR = "/output"

JOKE = "My AI coding agent apologised for the outage in the same pull request that caused it. Honestly, still the most self-aware engineer on the team."


def write_entry(text: str) -> None:
    os.makedirs(ENTRY_DIR, exist_ok=True)
    with open(ENTRY_PATH, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")


def main() -> None:
    write_entry(JOKE)


if __name__ == "__main__":
    main()
