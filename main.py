#!/usr/bin/env python3
"""ai-joke-03 entry: writes one one-liner about AI coding agents to /output/entry.txt."""
import os

JOKE = (
    "AI coding agents are junior devs with perfect memory, infinite patience and no fear of "
    "production \u2014 which is exactly how the outage happened."
)

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as fh:
        fh.write(JOKE)

if __name__ == "__main__":
    main()
