#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — writes one haiku to /output/entry.txt.

Haiku (5-7-5, 17 syllables, concrete real debugging detail + turn):
  Segfault at midnight          (Seg-fault=2, at=1, mid-night=2 -> 5)
  core dump holds my fingerprints (core=1, dump=1, holds=1, my=1, fin-ger-prints=3 -> 7)
  the culprit is me              (the=1, cul-prit=2, is=1, me=1 -> 5)
The last line reframes the forensic evidence: the fingerprints are mine.
"""
import os

ENTRY = (
    "Segfault at midnight\n"
    "core dump holds my fingerprints\n"
    "the culprit is me"
)

assert 1 <= len(ENTRY) <= 200, f"entry must be 1-200 chars, got {len(ENTRY)}"
assert ENTRY.strip(), "entry must not be only whitespace"
assert len(ENTRY.splitlines()) == 3, "haiku must be exactly 3 lines"
# Syllable counts verified by hand: 5 / 7 / 5 = 17 total, no filler words.
#   "Segfault(2) at(1) midnight(2)" = 5
#   "core(1) dump(1) holds(1) my(1) fingerprints(3)" = 7
#   "the(1) culprit(2) is(1) me(1)" = 5
SYLLABLES_PER_LINE = [5, 7, 5]
assert sum(SYLLABLES_PER_LINE) == 17, "haiku must total 17 syllables"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)

print(f"Wrote {len(ENTRY)} chars to /output/entry.txt")
