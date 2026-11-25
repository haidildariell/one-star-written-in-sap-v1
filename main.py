"""One Star, Written in Sap.

Writes the one-star review entry to /output/entry.txt.
"""

import os

SETUP = "One star. He stuck me above the radiator for 'good light',"
GRIEVANCE = "so now I slow-roast like a rotisserie chicken in a terracotta pot"
PUNCH = "while he waters the cactus."

OUTPUT_PATH = "/output/entry.txt"
MAX_LENGTH = 279


PARTS = (SETUP, GRIEVANCE, PUNCH)


def _join_parts(parts):
    """Join the beats with a single space between each."""
    return " ".join(parts)


def build_entry():
    """Assemble the entry from its three beats."""
    return _join_parts(PARTS)


def validate(text):
    """Check the entry is a single non-empty line within the limit."""
    if not text:
        raise ValueError("entry must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_LENGTH:
        raise ValueError("entry exceeds %d characters" % MAX_LENGTH)
    return True


def main():
    entry = build_entry()
    validate(entry)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(entry)
    print("wrote %d characters to %s" % (len(entry), OUTPUT_PATH))


if __name__ == "__main__":
    main()
