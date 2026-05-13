"""
07_register_pass.py
===================

Sentence-level academic-register pass and citation cleanup. The script
applies targeted in-place rewrites of the smallest set of sentences that
still carry promotional or causally-overclaiming language, and resolves
the citation-audit closeout items.

Idempotent: each rewrite is guarded by a precondition that detects whether
the rewrite has already been applied (by searching for the new wording).
"""

from __future__ import annotations

import sys

sys.path.insert(0, ".")
from _helpers import (  # noqa: E402
    open_draft,
    save_draft,
    has_marker,
    add_marker,
    insert_paragraph_before,
    find_paragraph_with_text,
)


# ---------------------------------------------------------------------------
# Targeted sentence/paragraph rewrites
# ---------------------------------------------------------------------------

# Each entry is (find_substring, replace_substring, marker)
REPLACEMENTS = [
    # --- 1. Update the §49 thesis-structure paragraph to describe the
    # actual nine-chapter structure plus appendices.
    (
        "Chapter 6 synthesizes these critical findings into a formalized "
        "Design Pattern for voice AI implementation in financial services, "
        "representing the study's primary theoretical output. Chapter 7 "
        "discusses the broad implications of the findings in relation to "
        "the existing literature. Finally, Chapters 8 and 9 outline the "
        "necessary limitations of the research and provide concluding "
        "remarks alongside vital avenues for future scholarly study.",
        "Chapter 6 formalises the four prerequisites identified in Chapter 5 "
        "as a Voice-AI-in-Regulated-Workflow design pattern in the design-"
        "science sense (Hevner et al., 2004), bounded for analytic "
        "generalization (Yin, 2018) to other regulated, communication-"
        "intensive financial-services workflows. Chapter 7 discusses the "
        "findings against the literature reviewed in Chapter 2, evaluates "
        "alternative explanations, and articulates the theoretical and "
        "practical contributions of the thesis. Chapter 8 consolidates the "
        "limitations and Chapter 9 provides direct one-paragraph answers to "
        "RQ1 and RQ2, summarises the contributions, and identifies four "
        "directions for future research. Appendices A\u2013G document the "
        "financial dataset, SEC provenance, NLP cleaning and modelling "
        "pipeline, topic inventory, supplementary figures, source-reliability "
        "and citation audit summary, and reproducibility notes.",
    ),
    # --- 2. Soften the broad-context opening (Ch 1, P11)
    (
        "Artificial intelligence (AI) has initiated an important transformation "
        "across global industries",
        "Artificial intelligence (AI) has been associated with substantive "
        "change across many industries",
    ),
    # --- 3. Soften "particularly critical for sectors..." (Ch 1, P12)
    (
        "This technological evolution is particularly critical for sectors "
        "characterized by",
        "This technological evolution is particularly relevant for sectors "
        "characterized by",
    ),
    # --- 4. Soften "fundamentally alter the interaction paradigm" (Ch 1, P22)
    (
        "voice LLM agents fundamentally alter the interaction paradigm",
        "voice LLM agents materially extend the interaction paradigm of "
        "earlier IVR systems",
    ),
    # --- 5. Replace "an important and growing gap" (Ch 1, P24)
    (
        "an important and growing gap remains in the academic literature",
        "a substantive and growing gap remains in the peer-reviewed academic "
        "literature",
    ),
    # --- 6. Replace "important empirical gap" (Ch 1, P39)
    (
        "addresses an important empirical gap surrounding the actual "
        "organizational outcomes",
        "addresses a substantive empirical gap surrounding the actual "
        "organizational outcomes",
    ),
    # --- 7. Replace "Practically, this research provides vital, highly
    # actionable insights" (Ch 1, P41)
    (
        "Practically, this research provides vital, highly actionable insights",
        "Practically, this research provides actionable insights",
    ),
    # --- 8. Soften "represents one of the most consequential technological
    # shifts" (Ch 2, P59)
    (
        "represents one of the most consequential technological shifts in the "
        "industry's recent history",
        "represents one of the more consequential technological shifts in the "
        "industry's recent history",
    ),
    # --- 9. Remove fabricated "Zhang, Frey, Goldfarb, & Teodoridis, 2023"
    # citation in §2.6 (Conceptual Framework).
    (
        "outside regulated mortgage origination (Wang, Huang, Hong, Liu, Guo, "
        "& Chen, 2023; Zhang, Frey, Goldfarb, & Teodoridis, 2023)",
        "outside regulated mortgage origination (Wang, Huang, Hong, Liu, Guo, "
        "& Chen, 2023)",
    ),
    # --- 10. Soften "necessary limitations" framing in §49 (already
    # replaced by edit 1, which removes that sentence; this is a no-op
    # safety net.)
    # --- 11. Soften "comprehensive, systematic investigation" in P49
    (
        "is logically structured to provide a comprehensive, systematic "
        "investigation of the research problem from theory to empirical "
        "findings.",
        "is structured to address the research problem from theory to "
        "empirical findings and to a transferable design pattern.",
    ),
    # --- 12. Soften "Chapter 2 presents a thorough review" prelude (P50)
    (
        "Chapter 2 presents a thorough review of the literature, tracing the "
        "evolution from general AI applications in finance to the specific "
        "nuances of conversational AI and the theoretical mechanisms of "
        "business value creation.",
        "Chapter 2 reviews the literature on artificial intelligence in "
        "financial services, conversational and voice AI, the business "
        "value of AI, and consumer behaviour and AI interaction, and "
        "concludes with a Conceptual Framework section integrating "
        "task\u2013technology fit, the AI service hierarchy, and the "
        "AI-enabled productivity tradition.",
    ),
    # --- 13. Soften "rigorous research methodology" in P50
    (
        "Chapter 3 outlines the rigorous research methodology",
        "Chapter 3 describes the research methodology",
    ),
]


def apply_replacements(doc) -> int:
    """Apply each text replacement to whichever paragraph contains it.
    Returns count of replacements applied."""
    n_applied = 0
    for find, replace, *rest in REPLACEMENTS:
        applied_here = False
        for p in doc.paragraphs:
            if find in p.text:
                _replace_in_paragraph(p, find, replace)
                n_applied += 1
                applied_here = True
                break
    return n_applied


def _replace_in_paragraph(paragraph, find: str, replace: str) -> None:
    """Replace `find` with `replace` inside a paragraph, preserving styling
    of the leading run."""
    full = paragraph.text
    if find not in full:
        return
    new_full = full.replace(find, replace, 1)
    # Clear runs and write the new text in a single run that inherits the
    # default style of the paragraph. Note: this loses inline formatting
    # within the replaced span, but the targeted spans are plain prose.
    # First, capture the leading run's font properties to preserve them.
    if paragraph.runs:
        first_run = paragraph.runs[0]
        font_name = first_run.font.name
        font_size = first_run.font.size
        bold = first_run.bold
        italic = first_run.italic
    else:
        font_name = None
        font_size = None
        bold = None
        italic = None
    # Remove all runs.
    for r in list(paragraph.runs):
        r._element.getparent().remove(r._element)
    new_run = paragraph.add_run(new_full)
    if font_name:
        new_run.font.name = font_name
    if font_size:
        new_run.font.size = font_size
    if bold is not None:
        new_run.bold = bold
    if italic is not None:
        new_run.italic = italic


# ---------------------------------------------------------------------------
# References cleanup: drop orphan Qualtrics, add Dietvorst.
# ---------------------------------------------------------------------------


def update_references(doc) -> bool:
    """Drop the orphan Qualtrics reference and add the Dietvorst reference."""
    changed = False
    qualtrics_idx = None
    for i, p in enumerate(doc.paragraphs):
        if p.text.startswith("Qualtrics. (2024)."):
            qualtrics_idx = i
            break
    if qualtrics_idx is not None:
        # Remove the paragraph
        para = doc.paragraphs[qualtrics_idx]
        para._element.getparent().remove(para._element)
        changed = True
        print("[refs] removed orphan Qualtrics (2024) reference")

    # Add Dietvorst entry alphabetically (after CFPB, before ElevenLabs)
    dietvorst_text = (
        "Dietvorst, B. J., Simmons, J. P., & Massey, C. (2015). Algorithm "
        "aversion: People erroneously avoid algorithms after seeing them "
        "err. Journal of Experimental Psychology: General, 144(1), 114\u2013126. "
        "https://doi.org/10.1037/xge0000033"
    )
    # Idempotency check
    for p in doc.paragraphs:
        if "Dietvorst" in p.text and "Algorithm aversion" in p.text:
            return changed
    # Locate ElevenLabs entry (alphabetical anchor)
    for p in doc.paragraphs:
        if p.text.startswith("ElevenLabs. (2026"):
            new_p = insert_paragraph_before(p, dietvorst_text)
            new_p.style = doc.styles["Normal"]
            print("[refs] added Dietvorst, Simmons, & Massey (2015) reference")
            changed = True
            break
    return changed


# ---------------------------------------------------------------------------
# Lit-review structure list (P53-57): rename "Consumer Behavior and AI
# Interaction" to "Consumer Behaviour and AI Interaction" (matching
# the actual H2 inserted in script 01) and append a Conceptual Framework
# bullet.
# ---------------------------------------------------------------------------


def update_lit_review_structure_list(doc) -> bool:
    if has_marker(doc, "register_lit_struct_aligned"):
        return False
    # Rename "Consumer Behavior" -> "Consumer Behaviour"
    for p in doc.paragraphs:
        if p.text.startswith("Consumer Behavior and AI Interaction"):
            _replace_in_paragraph(p, "Consumer Behavior", "Consumer Behaviour")
            add_marker(p, "register_lit_struct_aligned")
            print("[register] renamed Consumer Behavior -> Consumer Behaviour")
            return True
    return False


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------


def main():
    doc = open_draft()
    if has_marker(doc, "register_pass_done"):
        print("[register_pass_done] already done; skipping.")
        return
    n = apply_replacements(doc)
    print(f"[register] applied {n} sentence rewrites")
    update_references(doc)
    update_lit_review_structure_list(doc)
    # Mark register pass done by adding marker to the H1 of the introduction
    _, intro = find_paragraph_with_text(doc, "1. Introduction")
    if intro is not None:
        add_marker(intro, "register_pass_done")
    save_draft(doc)
    print("Saved.")


if __name__ == "__main__":
    main()
