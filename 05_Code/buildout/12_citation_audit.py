"""
12_citation_audit.py
====================

Run a citation-integrity audit on the thesis:

* extract every in-text citation key from Chapters 1-9 + appendices,
* extract every reference-list key,
* report:
    - in-text citations missing from the reference list,
    - reference-list entries not cited anywhere in the body,
    - obvious year mismatches (same author, different year body vs ref).

This is a heuristic audit; it does not parse APA grammar but it catches
the common citation-integrity bugs.
"""

from __future__ import annotations

import re
import sys
from collections import Counter

sys.path.insert(0, ".")
from _helpers import open_draft  # noqa: E402


# ---------------------------------------------------------------------------
# Citation extractors
# ---------------------------------------------------------------------------

# Parenthetical: (Author, 2024) or (Author & Author, 2024) or (Org, 2024a)
PAREN_CITE = re.compile(
    r"\(([^()]*?\b[12][0-9]{3}[a-z]?)\)"
)

# Narrative: Author (2024), Author and Author (2024), Author et al. (2024)
NARR_CITE = re.compile(
    r"\b([A-Z][A-Za-z\u2019'\-\.]+(?:\s*(?:&|and|,|et\s*al\.?)\s*[A-Z][A-Za-z\u2019'\-\.]+)*?)\s*\(([12][0-9]{3}[a-z]?)\)"
)

# Reference-list entry pattern (Author/Org, YYYY...)  - a paragraph that
# starts with capitalised author(s) and contains a 4-digit year before the
# title. We pull the first author surname + year as the key.
REF_KEY = re.compile(
    r"^\s*([A-Z][A-Za-z\u2019'\-\.]+)(?:[,\u2014][^()]*?)?\(([12][0-9]{3}[a-z]?)\)\."
)


def _normalise_first_author(name: str) -> str:
    """Reduce 'Brynjolfsson, E., Li, S., & Raymond, L.' to 'Brynjolfsson'."""
    name = name.strip()
    # Drop initials and trailing comma-separated authors.
    return re.split(r"[,\s]", name, maxsplit=1)[0].strip().rstrip(".")


def parse_intext_keys(text: str) -> set[tuple[str, str]]:
    """Extract (FirstAuthor, Year) keys from a body of text. Multiple
    citations inside one parenthetical are split on ';'."""
    keys: set[tuple[str, str]] = set()

    # Parenthetical
    for m in PAREN_CITE.finditer(text):
        inner = m.group(1)
        for chunk in inner.split(";"):
            chunk = chunk.strip()
            mm = re.match(
                r"([^,]+?)(?:,|\s+et\s*al\.?,)\s*([12][0-9]{3}[a-z]?)\b",
                chunk,
            )
            if mm:
                first = _normalise_first_author(mm.group(1))
                year = mm.group(2)
                keys.add((first, year))

    # Narrative
    for m in NARR_CITE.finditer(text):
        first_chunk = m.group(1)
        year = m.group(2)
        first = _normalise_first_author(first_chunk)
        keys.add((first, year))

    return keys


def parse_reference_keys(ref_paragraphs) -> set[tuple[str, str]]:
    keys: set[tuple[str, str]] = set()
    for p in ref_paragraphs:
        text = p.text.strip()
        if not text:
            continue
        m = REF_KEY.match(text)
        if m:
            first = _normalise_first_author(m.group(1))
            year = m.group(2)
            keys.add((first, year))
    return keys


def main():
    doc = open_draft()

    # Find paragraph indices for body vs references.
    body_text = []
    ref_paragraphs = []
    in_refs = False
    in_appendix_g_audit = False

    for p in doc.paragraphs:
        s = p.style.name if p.style else ""
        text = p.text
        if s.startswith("Heading 1") and text.strip().startswith("References"):
            in_refs = True
            continue
        # The next H1 after References ends the reference list.
        if in_refs and s.startswith("Heading 1") and not text.strip().startswith(
            "References"
        ):
            in_refs = False

        if in_refs:
            ref_paragraphs.append(p)
        else:
            body_text.append(text)

    body_blob = "\n".join(body_text)

    intext_keys = parse_intext_keys(body_blob)
    ref_keys = parse_reference_keys(ref_paragraphs)

    # Reports
    print("=" * 70)
    print("CITATION INTEGRITY AUDIT")
    print("=" * 70)
    print(f"Body in-text citations (unique keys): {len(intext_keys)}")
    print(f"Reference-list entries (unique keys): {len(ref_keys)}")
    print()

    missing_refs = sorted(intext_keys - ref_keys)
    if missing_refs:
        print(f"** {len(missing_refs)} in-text citations missing from reference list **")
        for first, year in missing_refs:
            print(f"   - ({first}, {year})")
    else:
        print("OK: every in-text citation has a reference-list entry.")
    print()

    uncited = sorted(ref_keys - intext_keys)
    if uncited:
        print(f"** {len(uncited)} reference-list entries not cited in the body **")
        for first, year in uncited:
            print(f"   - ({first}, {year})")
    else:
        print("OK: every reference-list entry is cited.")
    print()

    # Author-year mismatch detection: same first-author surname appears in
    # both body and ref but with different years.
    body_authors = {a: years for a, years in _group_by_author(intext_keys).items()}
    ref_authors = {a: years for a, years in _group_by_author(ref_keys).items()}

    for a, body_years in body_authors.items():
        if a in ref_authors:
            mismatches = body_years - ref_authors[a]
            if mismatches:
                print(
                    f"   MAYBE MISMATCH: {a} cited as {sorted(mismatches)} in body, "
                    f"but reference list has {sorted(ref_authors[a])}"
                )


def _group_by_author(keys: set[tuple[str, str]]) -> dict[str, set[str]]:
    out: dict[str, set[str]] = {}
    for first, year in keys:
        out.setdefault(first, set()).add(year)
    return out


if __name__ == "__main__":
    main()
