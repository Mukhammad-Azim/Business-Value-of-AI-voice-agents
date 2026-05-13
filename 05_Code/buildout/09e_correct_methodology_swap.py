"""
09e_correct_methodology_swap.py
================================

Corrective patch.

In 09c, fix_appendix_c_extraction() matched the first paragraph in the
document containing both 'Apify' and 'extracted' — that turned out to be the
Trustpilot justification paragraph in §3.4.2 (P0132), not Appendix C.1.

The result:
* §3.4.2 P0132 was overwritten with the extraction-date text (correct words,
  but it now duplicates the original P0131 raw-extraction paragraph and
  lost the Trustpilot-justification reasoning).
* Appendix C.1 P0544 still contains the stale 'May 6, 2026' / '2020-05 to
  2026-05' wording.

This script:
1. Restores the methodology Trustpilot-justification paragraph at P0132.
2. Updates Appendix C.1 with the correct extraction date (26 April 2026)
   and a clean repository-path reference.
"""

from __future__ import annotations

import sys

sys.path.insert(0, ".")
from _helpers import open_draft, save_draft  # noqa: E402


METHODOLOGY_TRUSTPILOT_JUSTIFICATION = (
    "Trustpilot is selected over Google Reviews and Yelp for three reasons. "
    "First, Trustpilot operates a verified-purchase model with domain-level "
    "authentication and an internal review-flagging system that materially "
    "reduces (although does not eliminate) the share of fraudulent or paid "
    "reviews relative to general-purpose review platforms (Filieri, 2015; "
    "Luca, 2016). Second, Trustpilot is the platform on which Better.com has "
    "the largest publicly available review corpus during the 2020–2026 "
    "observation window, providing both pre-period density and a non-trivial "
    "post-period sample. Third, the Trustpilot review-page schema is stable "
    "across the observation window, which simplifies reproducibility: the "
    "corpus used in this thesis was extracted on a single date (26 April "
    "2026) using the Apify Trustpilot Review Scraper (Actor ID "
    "l3wcDhSSC96LBRUpc) and is archived as a static CSV in "
    "Data/NLP/Better_Reviews.csv. The empirical cut-off is therefore the "
    "latest review date in the extraction (25 April 2026), and the title-"
    "page date and the empirical cut-off both fall in April 2026. The self-"
    "selection bias inherent to any review platform is acknowledged here and "
    "reiterated as a limitation in §3.10 and §8.7."
)

APPENDIX_C1_TEXT = (
    "The Trustpilot review corpus was extracted on a single date "
    "(26 April 2026, between 17:03 and 17:15 UTC) using the Apify Trustpilot "
    "Review Scraper (Actor ID l3wcDhSSC96LBRUpc), targeting the better.com "
    "domain. The raw extraction returned 1,934 reviews spanning the experience"
    "-date period 22 August 2020 to 25 April 2026 and is archived as a static "
    "CSV at Data/NLP/Better_Reviews.csv. The thesis title-page date "
    "(April 2026) and the empirical cut-off (the latest review date, 25 April "
    "2026) are therefore in the same calendar month."
)


def rewrite_paragraph_text(p, new_text: str) -> None:
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

    # 1. Restore the methodology Trustpilot-justification paragraph.
    target = None
    for i, p in enumerate(doc.paragraphs):
        if (p.style.name == "Heading 3" and
                "3.4.2" in p.text and "Trustpilot" in p.text):
            # The justification paragraph sits two paragraphs below the
            # heading (heading -> raw-extraction paragraph -> justification
            # / extraction-date paragraph -> cleaning paragraph).
            target = doc.paragraphs[i + 2]
            break
    if target is None:
        print("[09e] could not locate methodology paragraph slot")
    else:
        rewrite_paragraph_text(target, METHODOLOGY_TRUSTPILOT_JUSTIFICATION)
        print("[09e] §3.4.2 Trustpilot justification paragraph restored")

    # 2. Update Appendix C.1 paragraph.
    target_app = None
    in_app = False
    for i, p in enumerate(doc.paragraphs):
        if p.style.name == "Heading 1" and "Appendix C" in p.text:
            in_app = True
            continue
        if in_app and p.style.name == "Heading 1":
            break
        if in_app and "May 6, 2026" in p.text:
            target_app = p
            break
        if in_app and (p.style.name == "Heading 2" and "C.1" in p.text):
            # The paragraph after the C.1 heading is the extraction text.
            if i + 1 < len(doc.paragraphs):
                target_app = doc.paragraphs[i + 1]
                break
    if target_app is None:
        print("[09e] could not locate Appendix C.1 paragraph")
    else:
        rewrite_paragraph_text(target_app, APPENDIX_C1_TEXT)
        print("[09e] Appendix C.1 extraction paragraph updated (26 April 2026)")

    save_draft(doc)
    print("Saved.")


if __name__ == "__main__":
    main()
