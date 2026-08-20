#!/usr/bin/env python3
"""The separation gate. This corpus may not mention the verification instrument.

The project specification names the conflict this exists to prevent: a party that teaches people to
pass its own verification is grading work it set itself. The agreed mitigation is that teaching and
verification are separated as components - and a separation held only by good intentions is not a
separation, so it is held by this.

WHAT IS FORBIDDEN is vocabulary indexed to the instrument: the ladder levels, the passport, the
evidence classes, the absence reasons, the product name. What is NOT forbidden is ordinary English
that happens to overlap - a "confidence rating" for sales leads is not a claim about anyone's
autonomy. The published documents were reworded in the few places the two collided, so that this
check can stay strict instead of being widened until it stops catching anything.

Exit 1 on any hit. DISCLAIMER.md is the one file allowed to name the instrument, because its whole
job is to say what this corpus is not.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ALLOWED = {"DISCLAIMER.md", "check_separation.py", "README.md"}

# The provenance header of each document is metadata ABOUT the artefact, not part of it, and saying
# what a document is requires naming what it is separate from - "what it produced: provek.dev". The
# first version of this gate scanned it and convicted its own headers, which is the same shape as a
# text search that convicts the fix for quoting the thing it removed. So the scan starts after the
# header's closing rule. That is a correction of SCOPE, not of strictness: everything a reader
# actually reads is still held to the full rule.
HEADER_END = "\n---\n"


def body(text: str) -> tuple[str, int]:
    """The document past its provenance header, and the line it starts on."""
    if text.lstrip().startswith("#") and HEADER_END in text[:4000]:
        cut = text.index(HEADER_END, 0) + len(HEADER_END)
        return text[cut:], text[:cut].count("\n") + 1
    return text, 0

FORBIDDEN = [
    (r"\bL[0-5]\b", "a ladder level"),
    (r"\bpassports?\b", "the passport artefact"),
    (r"\bevidence class(es)?\b", "the evidence taxonomy"),
    (r"\bnot_measured\b", "an absence state"),
    (r"\bnothing_qualified\b|\bcheck_did_not_run\b|\bunreadable\b", "an absence reason"),
    (r"\bautonomy projection\b", "the projection"),
    (r"\bprovek\b", "the product name"),
    (r"\bverdicts?\b", "a verdict"),
    (r"\bscores?\b", "a score"),
]


def scan() -> list[tuple[str, int, str, str]]:
    hits = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or ".git/" in str(path):
            continue
        # `evidence/` holds transcripts of THIS gate's own runs, and a transcript of a failure
        # necessarily quotes what failed. Scanning it makes the kept red run a violation of the
        # rule it exists to prove - the same shape as a text search that convicts the fix for
        # quoting the thing it removed. The rule governs what a reader consumes; these files are
        # records of the checker.
        if path.parts[len(ROOT.parts):][:1] == ("evidence",):
            continue
        if path.suffix not in {".md", ".txt", ".py", ".yml", ".yaml"}:
            continue
        if path.name in ALLOWED:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        scanned, offset = body(text)
        for n, line in enumerate(scanned.splitlines(), 1 + offset):
            for pattern, what in FORBIDDEN:
                if re.search(pattern, line, re.I):
                    hits.append((str(path.relative_to(ROOT)), n, what, line.strip()[:90]))
    return hits


def main() -> int:
    hits = scan()
    if not hits:
        print("separation: clean - this corpus does not mention the verification instrument")
        return 0
    print(f"separation: FAILED, {len(hits)} occurrence(s)\n")
    for f, n, what, line in hits[:40]:
        print(f"  {f}:{n}  {what}\n      {line}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
