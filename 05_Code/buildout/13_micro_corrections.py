"""
13_micro_corrections.py
=======================

Apply the supervisor's final micro-correction list:

  1. Fix the typo "is the an empirical pattern" -> "is a pattern".
     (Two paragraphs in Chapter 5 carry this defective wording.)
  2. Correct the wrong table reference in section 3.4.3:
     "...is presented in Table 1." -> "...is presented in Table 3.2."
  3. Soften the Chapter 1 wording about generative AI:
     "modern generative AI has effectively dismantled these historic
     constraints" -> "modern generative AI has reduced some of these
     historic constraints".
  4. Soften the section 1.6.2 ROI wording:
     "demonstrating exactly how to systematically understand and measure
      the Return on Investment (ROI) of complex voice AI initiatives"
     -> "offering a structured approach for assessing the Return on
        Investment (ROI) and business value of complex voice AI
        initiatives".
  5. Revise the Chapter 7 NPS modal-customer claim:
     "...while NPS surveys distributed at closing capture the modal
      customer (Filieri, 2015; Luca, 2016)."
     ->
     "...while management-reported NPS may capture a different,
      internally sampled customer population (Filieri, 2015; Luca, 2016)."
  6. Targeted British English on author prose only:
     "recognizable" -> "recognisable"
     "programs"      -> "programmes"  (only at paragraph 281 inside
                       "broader expense-management programs", which is
                       author prose; we leave reference titles alone
                       because they live in the reference list which is
                       not visited here).

The script is conservative and only touches paragraphs in the body
chapters (Chapters 1-9 + Discussion + Conclusion + Appendices A-G); it
does not touch the reference list. It is idempotent: a second run is a
no-op once the new wording is in place.
"""

from __future__ import annotations

import sys

sys.path.insert(0, ".")
from _helpers import open_draft, save_draft  # noqa: E402


# ---------------------------------------------------------------------------
# Replacements: (old_substr, new_substr, label)
# ---------------------------------------------------------------------------

REPLACEMENTS = [
    # 1. Typo in Chapter 5 (paragraphs 318 and 366).
    (
        "is the an empirical pattern consistent with operational leverage",
        "is a pattern consistent with operational leverage",
        "1. typo 'is the an empirical pattern' -> 'is a pattern'",
    ),

    # 2. Wrong table reference in section 3.4.3 (paragraph 135).
    (
        "is presented in Table 1.",
        "is presented in Table 3.2.",
        "2. \u00a73.4.3 'Table 1' -> 'Table 3.2'",
    ),

    # 3. Soften Chapter 1 generative-AI wording (paragraph 13).
    (
        "modern generative AI has effectively dismantled these historic constraints",
        "modern generative AI has reduced some of these historic constraints",
        "3. Chapter 1 'dismantled' -> 'reduced some'",
    ),

    # 4. Soften section 1.6.2 ROI wording (paragraph 41).
    (
        "by demonstrating exactly how to systematically understand and measure "
        "the Return on Investment (ROI) of complex voice AI initiatives",
        "by offering a structured approach for assessing the Return on "
        "Investment (ROI) and business value of complex voice AI initiatives",
        "4. \u00a71.6.2 ROI wording softened",
    ),

    # 5. Chapter 7 NPS modal-customer claim (paragraph 422).
    (
        "while NPS surveys distributed at closing capture the modal customer",
        "while management-reported NPS may capture a different, internally "
        "sampled customer population",
        "5. Chapter 7 NPS 'modal customer' replaced with cautious wording",
    ),

    # 6a. recognizable -> recognisable (paragraph 407).
    (
        "the human\u2013AI boundary recognizable",
        "the human\u2013AI boundary recognisable",
        "6a. 'recognizable' -> 'recognisable'",
    ),

    # 6b. programs -> programmes inside "expense-management programs" (paragraph 281).
    (
        "broader expense-management programs",
        "broader expense-management programmes",
        "6b. 'programs' -> 'programmes' (author prose only)",
    ),

    # 6c. AI program investments -> AI programme investments (paragraph 279).
    (
        "to AI program investments",
        "to AI programme investments",
        "6c. 'AI program investments' -> 'AI programme investments'",
    ),

    # 6d. Cover-page label "Program:" -> "Programme:" (paragraph 7).
    (
        "Program:  Master\u2019s in Business Informatics",
        "Programme:  Master\u2019s in Business Informatics",
        "6d. cover page 'Program:' -> 'Programme:' (curly apostrophe)",
    ),
    (
        "Program:  Master's in Business Informatics",
        "Programme:  Master's in Business Informatics",
        "6d. cover page 'Program:' -> 'Programme:' (straight apostrophe)",
    ),
]


def apply_replacement_to_paragraph(paragraph, old: str, new: str) -> int:
    """Replace ``old`` with ``new`` across a paragraph's runs, preserving
    the formatting of the first run that contains the match. Returns the
    number of replacements applied to this paragraph."""
    full = "".join(r.text for r in paragraph.runs)
    if old not in full:
        return 0

    new_full = full.replace(old, new)
    runs = paragraph.runs
    if runs:
        runs[0].text = new_full
        for r in runs[1:]:
            r.text = ""
    else:
        paragraph.text = new_full
    return full.count(old)


def main():
    doc = open_draft()
    summary: list[str] = []

    # Find the references heading so we don't touch the reference list.
    refs_start_index = None
    for idx, p in enumerate(doc.paragraphs):
        s = p.style.name if p.style else ""
        if s.startswith("Heading 1") and p.text.strip().startswith("References"):
            refs_start_index = idx
            break

    body_paragraphs = (
        doc.paragraphs[:refs_start_index]
        if refs_start_index is not None
        else doc.paragraphs
    )
    appendix_paragraphs = (
        doc.paragraphs[refs_start_index + 1:] if refs_start_index is not None else []
    )
    # We skip the reference list itself but include appendices that follow it.
    # Detect the next "Appendix" heading after References.
    in_appendix = False
    appendix_safe = []
    for p in appendix_paragraphs:
        s = p.style.name if p.style else ""
        if s.startswith("Heading 1") and p.text.strip().startswith("Appendix"):
            in_appendix = True
        if in_appendix:
            appendix_safe.append(p)

    target_paragraphs = list(body_paragraphs) + appendix_safe

    for old, new, label in REPLACEMENTS:
        count = 0
        for p in target_paragraphs:
            count += apply_replacement_to_paragraph(p, old, new)
        summary.append(f"  {label}: {count} replacement(s)")

    save_draft(doc)

    print("=" * 60)
    print("Micro-correction pass")
    print("=" * 60)
    for line in summary:
        print(line)


if __name__ == "__main__":
    main()
