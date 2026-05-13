"""
08_register_pass2.py
====================

Second register pass that targets residues identified by 99_consistency_scan.py:

* paragraph 50 thesis-structure rewrite (uses non-breaking spaces, so the
  earlier script\u2019s find string did not match)
* P11 "fundamentally constrained" -> "structurally constrained"
* P13 "fundamentally altering customer interaction models" ->
       "materially changing customer interaction models"
* P26 "could revolutionize financial services" ->
       "could materially change financial services"
* P60 "AI has fundamentally restructured" ->
       "AI has materially restructured"
* P45  "this is fundamentally a single-company case study" ->
       "this is a single-company case study"
* P74  "toward a fundamentally different mode" ->
       "toward a materially different mode"

Idempotent.
"""

from __future__ import annotations

import re
import sys

sys.path.insert(0, ".")
from _helpers import open_draft, save_draft, has_marker, add_marker, find_paragraph_with_text  # noqa: E402


def replace_in_paragraph(paragraph, find: str, replace: str, regex: bool = False) -> bool:
    txt = paragraph.text
    if regex:
        new = re.sub(find, replace, txt)
        if new == txt:
            return False
    else:
        if find not in txt:
            return False
        new = txt.replace(find, replace, 1)
    # capture first run formatting
    if paragraph.runs:
        r0 = paragraph.runs[0]
        font_name = r0.font.name
        font_size = r0.font.size
        bold = r0.bold
        italic = r0.italic
    else:
        font_name = None
        font_size = None
        bold = None
        italic = None
    for r in list(paragraph.runs):
        r._element.getparent().remove(r._element)
    nr = paragraph.add_run(new)
    if font_name:
        nr.font.name = font_name
    if font_size:
        nr.font.size = font_size
    if bold is not None:
        nr.bold = bold
    if italic is not None:
        nr.italic = italic
    return True


# Pairs of (find, replace, regex_flag)
EDITS = [
    # P50: replace using regex that's tolerant of non-breaking spaces.
    (
        r"Chapter\s*6\s*synthesizes these critical findings into a formalized Design Pattern for voice AI implementation in financial services, representing the study's primary theoretical output\.\s*Chapter\s*7\s*discusses the broad implications of the findings in relation to the existing literature\.\s*Finally,\s*Chapters\s*8 and 9\s*outline the necessary limitations of the research and provide concluding remarks alongside vital avenues for future scholarly study\.",
        "Chapter 6 formalises the four prerequisites identified in Chapter 5 as a Voice-AI-in-Regulated-Workflow design pattern in the design-science sense (Hevner et al., 2004), bounded for analytic generalization (Yin, 2018) to other regulated, communication-intensive financial-services workflows. Chapter 7 discusses the findings against the literature reviewed in Chapter 2, evaluates alternative explanations, and articulates the theoretical and practical contributions of the thesis. Chapter 8 consolidates the limitations and Chapter 9 provides direct one-paragraph answers to RQ1 and RQ2, summarises the contributions, and identifies four directions for future research. Appendices A\u2013G document the financial dataset, SEC provenance, NLP cleaning and modelling pipeline, topic inventory, supplementary figures, source-reliability and citation audit summary, and reproducibility notes.",
        True,
    ),
    # P11
    ("they were fundamentally constrained by their inability",
     "they were structurally constrained by their inability", False),
    # P13
    ("This capability is fundamentally altering customer interaction models",
     "This capability is materially changing customer interaction models", False),
    # P26
    ("how advanced AI could revolutionize financial services",
     "how advanced AI could materially change financial services", False),
    # P60
    ("arguing that AI has fundamentally restructured how market participants",
     "arguing that AI has materially restructured how market participants", False),
    # P45
    ("While this is fundamentally a single-company case study to enable depth of analysis",
     "While this is a single-company case study selected for analytic depth",
     False),
    # P74
    ("toward a fundamentally different mode of human-machine interaction",
     "toward a materially different mode of human-machine interaction", False),
]


def main():
    doc = open_draft()
    if has_marker(doc, "register_pass2_done"):
        print("[register_pass2_done] already done; skipping")
        return
    n = 0
    for find, replace, regex in EDITS:
        applied = False
        for p in doc.paragraphs:
            if replace_in_paragraph(p, find, replace, regex=regex):
                n += 1
                applied = True
                break
        if not applied:
            print(f"[register2] no match for: {find[:80]}{'...' if len(find) > 80 else ''}")
    print(f"[register2] {n} edits applied")
    _, intro = find_paragraph_with_text(doc, "1. Introduction")
    if intro is not None:
        add_marker(intro, "register_pass2_done")
    save_draft(doc)
    print("Saved.")


if __name__ == "__main__":
    main()
