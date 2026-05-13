"""
09a_strip_buildout_markers.py
=============================

Removes every visible BUILDOUT:: marker that the build-out scripts inserted as
idempotency sentinels. The markers were intended for build-script self-checks
and must not appear in the final draft (supervisor blocking issue A1).

This script is naturally idempotent: re-running it after a clean strip is a
no-op because no markers remain.
"""

from __future__ import annotations

import re
import sys

sys.path.insert(0, ".")
from _helpers import open_draft, save_draft  # noqa: E402

MARKER_RE = re.compile(r"\s*BUILDOUT::[A-Za-z0-9_]+", flags=0)


def strip_paragraph(p) -> bool:
    """Returns True if the paragraph text was changed."""
    if "BUILDOUT::" not in p.text:
        return False
    # First try in-place run edits (preserves run formatting).
    in_place_changed = False
    for r in p.runs:
        if "BUILDOUT::" in r.text:
            new = MARKER_RE.sub("", r.text).rstrip()
            if new != r.text:
                r.text = new
                in_place_changed = True
    # If still present after run-level edits (split across runs), rebuild text.
    if "BUILDOUT::" in p.text:
        new_text = MARKER_RE.sub("", p.text).rstrip()
        if p.runs:
            r0 = p.runs[0]
            font_name = r0.font.name
            font_size = r0.font.size
            bold = r0.bold
            italic = r0.italic
        else:
            font_name = font_size = bold = italic = None
        for r in list(p.runs):
            r._element.getparent().remove(r._element)
        nr = p.add_run(new_text)
        if font_name:
            nr.font.name = font_name
        if font_size:
            nr.font.size = font_size
        if bold is not None:
            nr.bold = bold
        if italic is not None:
            nr.italic = italic
        return True
    return in_place_changed


def main():
    doc = open_draft()
    n_paragraphs_changed = 0
    for p in doc.paragraphs:
        if strip_paragraph(p):
            n_paragraphs_changed += 1
    for t in doc.tables:
        for row in t.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    if strip_paragraph(p):
                        n_paragraphs_changed += 1
    print(f"[strip_buildout] paragraphs cleaned: {n_paragraphs_changed}")
    save_draft(doc)
    print("Saved.")


if __name__ == "__main__":
    main()
