"""One Star, Written in Sap.

Writes a one-line, one-star review from a houseplant about its human
owner to /output/entry.txt, then validates the result.

The entry is built from three named beats so the joke's structure stays
visible in the code: the setup (where the plant got put), the grievance
(what the placement actually does to it), and the punch (the concrete
image the reader is left with).
"""

import os

# Beat 1 — setup: the owner moved the plant for "good light".
SETUP = 'He stuck me above the radiator for \'good light\''

# Beat 2 — grievance: the placement slow-roasts the plant.
GRIEVANCE = 'so now I slow-roast like a rotisserie chicken'

# Beat 3 — punch: the concrete image, in its terracotta pot, while the
# owner waters the wrong plant.
PUNCH = 'in a terracotta pot while he waters the cactus'

OUTPUT_PATH = "/output/entry.txt"
MIN_LENGTH = 1
MAX_LENGTH = 279


def build_entry() -> str:
    """Assemble the single-line review from its three beats."""
    return "One star. " + SETUP + ", " + GRIEVANCE + " " + PUNCH + "."


def validate(text: str) -> None:
    """Enforce the competition gate: one line, 1-279 chars, not blank."""
    if not text.strip():
        raise ValueError("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (MIN_LENGTH, MAX_LENGTH, len(text))
        )


def main() -> None:
    entry = build_entry()
    validate(entry)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(entry)
    print("wrote %s (%d chars)" % (OUTPUT_PATH, len(entry)))


if __name__ == "__main__":
    main()
