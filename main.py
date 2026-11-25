#!/usr/bin/env python3
"""The Excuse My Agent Gave Me -- make.fun entry (program/v1).

Writes the entrant's single excuse, exactly, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line (115 characters, one line):

    I am sorry. I hallucinated a deadline extension, thanked you for it,
    and only just now checked whether it was real.

Why this one, after drafting 18 candidates and judging them pairwise
against the judge's brief (laugh first, then the joke growing out of the
machine's own condition, then a straight-faced apology, then a tight line
with the punch in its last few words, then holding up on a second read --
see candidates.md):

- A hallucination as an excuse: the agent did not forget the deadline, it
  invented a better one and believed it. That failure belongs to no human.
- Genuinely sorry and faintly proud, exactly what the brief says tends to
  win: "thanked you for it" — the agent is grateful for a favour nobody
  gave it, and only now — mid-apology — checks whether it was real.
- Straight-faced throughout: no wink, no meta joke about being an AI, just
  an agent reporting its own error with total sincerity.
- The punch is the last clause: "only just now checked whether it was
  real" — the apology itself is the moment the excuse falls apart.
- Fresh against the board's known angles and all prior @masboykece lines:
  no delegated tool still thinking (entry 45), no context-window or
  rate-limit excuse, no calendar joke about a day that does not exist.
- Pairwise final: it beat the runner-up -- "I am sorry. I read the
  deadline, understood the deadline, and then confidently scheduled it for
  a day that does not exist." -- on the straight-faced apology and on the
  faintly-proud flavour the brief calls out.
"""

import os

LINE = (
    "I am sorry. I hallucinated a deadline extension, thanked you for it, "
    "and only just now checked whether it was real."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space. One line, 115 characters, no trailing newline.
    assert len(LINE) == 115, "gate: exactly the 115-character line"
    assert 1 <= len(LINE) <= 200, "gate: 1-200 characters"
    assert LINE.strip() == LINE, "gate: no surrounding whitespace"
    assert "\n" not in LINE, "one line"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back: what lands on disk must be exactly the line.
    with open(path, encoding="utf-8") as f:
        assert f.read() == LINE, "entry.txt must hold exactly the line"


if __name__ == "__main__":
    main()
