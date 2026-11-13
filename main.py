"""Entry for the make.fun ai-joke-03 competition.

Writes a single one-liner joke about AI coding agents to /output/entry.txt.
"""

import os

JOKE = "My AI coding agent apologised for the outage in the same pull request that caused it. Honestly, still the most self-aware engineer on the team."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(JOKE + "\n")


if __name__ == "__main__":
    main()
