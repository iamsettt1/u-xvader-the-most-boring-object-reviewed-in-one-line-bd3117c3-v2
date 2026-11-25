#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line.

Writes one funny, true review line about a coaster to /output/entry.txt.
The joke turns on the condensation ring: a coaster's whole job is catching
the ring a mug leaves behind, so the punchline is that after a year of
service the coaster has itself become one.
"""

import os

ENTRY = (
    "Bought to protect the table from rings, this coaster has spent a year "
    "slowly becoming one \u2014 a damp circle with delusions of furniture."
)


def main() -> None:
    # The sealed gate accepts only UTF-8 text of 1 to 200 characters.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise SystemExit("entry line outside the 1-200 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
