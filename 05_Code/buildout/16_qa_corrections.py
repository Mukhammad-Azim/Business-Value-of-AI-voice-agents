"""
16_qa_corrections.py
====================

Final QA-only correction pass on Main_Draft (7).docx.

Three correctness issues found and fixed; no other changes.

1. Para 149 (§3.6 Operationalisation of Business Value):
   The text states "the Operational Leverage Index reported in §5.3.4
   and Appendix B is an author-constructed equally-weighted composite
   of ...". Appendix B is "SEC Filing Provenance"; the Operational
   Leverage Index (Figure E.1) is in Appendix E, not Appendix B. Para
   536 already correctly says "The Operational Leverage Index is
   computed in Appendix E ...". Fix: "Appendix B" -> "Appendix E"
   in para 149 only.

2. Para 174 (§3.11 Research Rigour and Reproducibility):
   The text states "Package versions used in the financial and NLP
   pipelines are listed in 08_Code/requirements.txt and reproduced in
   Appendix B". Appendix B is "SEC Filing Provenance" and contains
   no package-versions table. Package versions are in Appendix G.3
   ("G.3 Package Versions", with Table G.1 "Package versions used in
   the financial and NLP pipelines and in the build-out scripts").
   Fix: "Appendix B" -> "Appendix G" in para 174 only.

3. Para 554 (Appendix C.5 Statistical Test Parameters):
   The sentence reads "All keyword-group p-values were Bonferroni-
   corrected for the number of keyword groups tested (11 groups; alpha
   = 0.05/7 = 0.00455). Only the Cost/Rates keyword group survives
   Bonferroni correction (§5.4.3)." This is internally contradictory
   and inconsistent with the rest of the thesis:
     - 0.05 / 7 = 0.007142..., NOT 0.00455.
     - 0.05 / 11 = 0.004545..., which matches "0.00455".
     - The thesis body and §3.5.2 (para 144), §5.4.3 (para 350), and
       Appendix D.2 (para 559) all explicitly use SEVEN keyword
       groups (Explicit AI/Automation, Speed/Efficiency, Human
       Support, Communication, Delay/Friction, Cost/Rates,
       Digital/Process), with the Bonferroni threshold reported as
       alpha/7 ~= 0.00714 in para 559.
   Fix: replace "(11 groups; alpha = 0.05/7 = 0.00455)" with
   "(seven groups; alpha = 0.05/7 \u2248 0.00714)" in para 554, so
   that the appendix matches every other mention in the thesis.

The script is idempotent.
"""

from __future__ import annotations

import sys

sys.path.insert(0, ".")
from _helpers import open_draft, save_draft  # noqa: E402


CORRECTIONS = [
    # (paragraph index, old, new, label)
    (
        149,
        "Operational Leverage Index reported in \u00a75.3.4 and Appendix B",
        "Operational Leverage Index reported in \u00a75.3.4 and Appendix E",
        "\u00a73.6 OLI appendix ref: Appendix B \u2192 Appendix E",
    ),
    (
        174,
        "Package versions used in the financial and NLP pipelines are listed in 08_Code/requirements.txt and reproduced in Appendix B",
        "Package versions used in the financial and NLP pipelines are listed in 08_Code/requirements.txt and reproduced in Appendix G",
        "\u00a73.11 Package-versions appendix ref: Appendix B \u2192 Appendix G",
    ),
    (
        554,
        "Bonferroni-corrected for the number of keyword groups tested (11 groups; \u03b1 = 0.05/7 = 0.00455)",
        "Bonferroni-corrected for the number of keyword groups tested (seven groups; \u03b1 = 0.05/7 \u2248 0.00714)",
        "Appendix C.5 Bonferroni divisor: 11 groups / 0.00455 \u2192 seven groups / 0.00714",
    ),
]


def replace_in_paragraph(paragraph, old: str, new: str) -> int:
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
    paragraphs = list(doc.paragraphs)

    for idx, old, new, label in CORRECTIONS:
        if idx >= len(paragraphs):
            print(f"  [SKIP idx OOB] {label}")
            continue
        p = paragraphs[idx]
        before = p.text
        if old not in before and new in before:
            print(f"  [already applied] {label}")
            continue
        if old not in before:
            print(f"  [NOT FOUND] {label}")
            continue
        n = replace_in_paragraph(p, old, new)
        print(f"  [OK x{n}] {label}")

    save_draft(doc)


if __name__ == "__main__":
    main()
