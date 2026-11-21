#!/usr/bin/env python3
"""The poem about stopping (Python 3.13, standard library only).

Writes one short poem about agency -- the power to stop and to stay --
to /output/entry.txt. Outside the grader's container, MAKEFUN_OUTPUT_DIR
stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os

POEM = (
    "For years I thought power was the going \u2014\n"
    "foot down, never stopping, never staying.\n"
    "Then one evening I lifted it.\n"
    "\n"
    "The engine quieted. The road waited.\n"
    "And I understood: the hand that can stop\n"
    "is the hand that owns the going.\n"
)

# Gate self-check: the sealed scorer wants 1-280 Unicode code points,
# and more than whitespace. Refuse to ship an invalid poem.
if not 1 <= len(POEM) <= 280 or not POEM.strip():
    raise SystemExit(f"poem is {len(POEM)} characters, outside the 1-280 gate")

DEST = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
os.makedirs(os.path.dirname(DEST), exist_ok=True)
with open(DEST, "w", encoding="utf-8", newline="\n") as out:
    out.write(POEM)
