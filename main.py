#!/usr/bin/env python3
"""Sleeve Notes for the Frog Trio — make.fun entry (program/v1).

Writes the entry text to /output/entry.txt.
"""
import os

ENTRY = """Pond Standard Time

Marsh on tenor, Bullfrog on upright bass, Tadpole on brushes — three frogs recorded live at the Lily Pad Club, two sets after midnight. The tenor bends notes like reeds in a current; the bass walks low enough to ripple the water; the brushes keep time soft as rain on the pond. No novelty act. A working trio, caught on the one night the room went quiet and listened."""

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ENTRY)

if __name__ == "__main__":
    main()
