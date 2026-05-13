"""
09b_number_headings.py
=======================

Standardises the heading hierarchy across the entire thesis (supervisor
blocking issue A9). After this pass:

* H1 chapters keep their "N. Title" prefix (already standardised).
* Every H2 inside a chapter is prefixed "N.M Title" if not already prefixed.
* Every H3 inside an H2 is prefixed "N.M.K Title" if not already prefixed.
* Existing prefixes that already match the canonical scheme are kept verbatim.
* Cross-references in the body that already cite §3.10, §2.5, etc. are then
  satisfied because the corresponding headings now exist with those numbers.

The script is idempotent: it inspects the existing heading text first and
only adds the prefix if it is missing.

Title-page paragraphs and Appendix headings (Appendix A, B, ...) are never
touched.
"""

from __future__ import annotations

import re
import sys

sys.path.insert(0, ".")
from _helpers import open_draft, save_draft  # noqa: E402

H1_PREFIX_RE = re.compile(r"^\s*(\d+)\.\s+(.*)$")
H2_PREFIX_RE = re.compile(r"^\s*(\d+)\.(\d+)\s+(.*)$")
H3_PREFIX_RE = re.compile(r"^\s*(\d+)\.(\d+)\.(\d+)\s+(.*)$")


def get_chapter_number(text: str):
    m = H1_PREFIX_RE.match(text.strip())
    if m:
        return int(m.group(1))
    return None


def already_h2_numbered(text: str, chapter: int):
    m = H2_PREFIX_RE.match(text.strip())
    if m and int(m.group(1)) == chapter:
        return True
    return False


def already_h3_numbered(text: str, chapter: int, section: int):
    m = H3_PREFIX_RE.match(text.strip())
    if m and int(m.group(1)) == chapter and int(m.group(2)) == section:
        return True
    return False


def rewrite_paragraph_text(p, new_text: str) -> None:
    """Replace the paragraph's full text while preserving the run formatting
    of the first run (heading runs typically all share the same heading
    style)."""
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


def main():
    doc = open_draft()

    chapter = None
    h2_counter = 0
    h3_counter = 0
    n_h2_renamed = 0
    n_h3_renamed = 0

    for p in doc.paragraphs:
        style = p.style.name
        text = p.text.strip()
        if style == "Heading 1":
            # Reset counters when a new chapter is encountered.
            ch = get_chapter_number(text)
            if ch is not None:
                chapter = ch
                h2_counter = 0
                h3_counter = 0
            else:
                # Appendix or References — disable numbering inside.
                chapter = None
                h2_counter = 0
                h3_counter = 0
        elif style == "Heading 2" and chapter is not None:
            h2_counter += 1
            h3_counter = 0
            if not already_h2_numbered(text, chapter):
                new_text = f"{chapter}.{h2_counter} {text}"
                rewrite_paragraph_text(p, new_text)
                n_h2_renamed += 1
            else:
                # Sync our counter to whatever number is in the heading so
                # subsequent siblings continue from there.
                m = H2_PREFIX_RE.match(text)
                if m:
                    h2_counter = int(m.group(2))
        elif style == "Heading 3" and chapter is not None:
            h3_counter += 1
            if not already_h3_numbered(text, chapter, h2_counter):
                new_text = f"{chapter}.{h2_counter}.{h3_counter} {text}"
                rewrite_paragraph_text(p, new_text)
                n_h3_renamed += 1
            else:
                m = H3_PREFIX_RE.match(text)
                if m:
                    h3_counter = int(m.group(3))

    print(f"[number_headings] H2 renamed: {n_h2_renamed}; H3 renamed: {n_h3_renamed}")
    save_draft(doc)
    print("Saved.")


if __name__ == "__main__":
    main()
