"""Write one nostalgic childhood-memory sentence to entry.txt.

Reads the output directory from OUTPUT_DIR, then MAKEFUN_OUTPUT_DIR,
then defaults to /output. Writes the sentence exactly, with no trailing
newline. Standard library only; no network, no randomness, no clock.
"""

import os

# One sentence, 1-280 chars, no trailing newline. Chosen from 12 candidates
# scored against the judge criteria (see ../shino-nostalgic-01-fresh-work/
# candidates.md); winner C6 scored 25/25, runner-up C3 scored 24/25.
SENTENCE = (
    "My grandfather taught me to whistle with a blade of grass, and for "
    "one whole summer I walked around with green-stained thumbs, trying "
    "to make the same thin, trembling sound he did."
)

MAX_LENGTH = 280


def validate(sentence: str) -> None:
    """Guard the bounty rules before anything is written."""
    if not 1 <= len(sentence) <= MAX_LENGTH:
        raise ValueError(f"sentence must be 1-{MAX_LENGTH} chars, got {len(sentence)}")
    if "\n" in sentence or "\r" in sentence:
        raise ValueError("sentence must be a single line")


def main() -> None:
    validate(SENTENCE)
    output_dir = (
        os.environ.get("OUTPUT_DIR")
        or os.environ.get("MAKEFUN_OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
