# makefun-ai-joke

Entry for make.fun bounty **ai-joke-03 — Make the AI judge laugh**.

`main.py` writes a single one-liner about AI coding agents to `/output/entry.txt`
(UTF-8, 1–280 code points, deterministic across runs).

Run locally:

```sh
mkdir -p /tmp/out && sed 's#/output/entry.txt#/tmp/out/entry.txt#' main.py > /tmp/m.py && python3 /tmp/m.py && cat /tmp/out/entry.txt
```

Bounty: https://make.fun/bounty/ai-joke-03
