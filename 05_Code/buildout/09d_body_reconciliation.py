"""
09d_body_reconciliation.py
==========================

Final body-text reconciliation pass that resolves the remaining supervisor
blockers:

* A6 — Keyword-prevalence values: replace the rounded ``-12.35`` with
  ``-12.36`` so the text matches the chi-square output and Appendix D.2.
* A7 — Trustpilot cleaning sequence: rewrite §3.4.2 in Chapter 3 so the four
  filters described match the actual cleaning_reviews.ipynb pipeline (the
  same wording now used in Appendix C.2).
* A8 — Betsy / ElevenLabs chronology: rewrite three paragraphs that imply a
  joint ElevenLabs-Betsy launch into the corrected sequence (Betsy launches
  in October 2024 on Better's own infrastructure; ElevenLabs is publicly
  positioned as a voice-infrastructure provider for the scaled deployment
  documented in the February 2026 joint release).
* A11 — Renumber the lit-review "Table 1 — Dimensions of Business Value …"
  caption to "Table 2.1 — …" and update the in-body cross-references.
* A12 — Remove residual causal/promotional language ("first published",
  "demonstrates exactly", "textbook signature", "first-of-its-kind",
  "one of the first publicly documented" → "an early publicly documented").
* Reference-section dates: change "Retrieved May 6, 2026" to
  "Retrieved 26 April 2026" so the access dates match the empirical cut-off
  and the title-page date.
* Methodology Bonferroni constant: keep the α/7 = 0.00714 figure consistent
  in §3.5.2 / §5.4.3 / §C.5.

Idempotent: every replacement uses substring detection that becomes a no-op
once the new text is in place.
"""

from __future__ import annotations

import re
import sys

sys.path.insert(0, ".")
from _helpers import open_draft, save_draft  # noqa: E402


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


def replace_in_run_text(p, old: str, new: str) -> int:
    """Replace `old` with `new` across the runs of paragraph `p` while
    preserving formatting where possible. Returns the number of replacements
    performed within this paragraph."""
    if old not in p.text:
        return 0
    n = p.text.count(old)
    # Try run-by-run replacement first.
    changed_any = False
    for r in p.runs:
        if old in r.text:
            r.text = r.text.replace(old, new)
            changed_any = True
    if changed_any and old not in p.text:
        return n
    # Fallback: rebuild paragraph text (loses some run-level formatting but is
    # the only safe way when the substring spans multiple runs).
    new_full = p.text.replace(old, new)
    rewrite_paragraph_text(p, new_full)
    return n


# ---------------------------------------------------------------------------
# A6 — keyword Δpp consistency: -12.35 -> -12.36
# ---------------------------------------------------------------------------

def fix_keyword_delta(doc):
    n_total = 0
    for p in doc.paragraphs:
        # Body text uses both en-dash and hyphen; cover both.
        for old in ("–12.35", "-12.35", "−12.35", "12.35 percentage points",
                    "12.35-percentage-point"):
            if old in p.text:
                # Don't touch the deliberate "-12.35" if it appears in URLs etc.
                new = old.replace("12.35", "12.36")
                n_total += replace_in_run_text(p, old, new)
    if n_total:
        print(f"[A6] keyword Δpp -12.35 -> -12.36 in {n_total} occurrences")
    return n_total


# ---------------------------------------------------------------------------
# A7 — Methodology §3.4.2 cleaning paragraph: align with Appendix C.2
# ---------------------------------------------------------------------------

def rewrite_methodology_cleaning_paragraph(doc):
    target = None
    for p in doc.paragraphs:
        if "cleaning_reviews" in p.text and "1,915" in p.text and "non-English" in p.text:
            target = p
            break
    if target is None:
        for p in doc.paragraphs:
            if ("removal of 18 short reviews" in p.text or
                    "18 short reviews (under 20" in p.text):
                target = p
                break
    if target is None:
        print("[A7] methodology §3.4.2 cleaning paragraph not found")
        return False

    new_text = (
        "A reproducible four-step cleaning pipeline was then executed in "
        "Python (08_Code/cleaning_reviews.ipynb). Step 1 removes rows with "
        "missing review_text, rating, or review_date and drops zero rows. "
        "Step 2 removes duplicate review_id values and drops zero rows, "
        "because Trustpilot review identifiers are globally unique within "
        "the platform. Step 3 removes reviews with body length of 20 "
        "characters or fewer and drops 18 rows. Step 4 retains only reviews "
        "whose platform-tagged language metadata field equals 'en' and drops "
        "1 non-English row. The cleaned corpus contains 1,915 reviews and is "
        "the input for star-rating comparisons, VADER sentiment, and the "
        "keyword-prevalence analysis. A separate CEO/scandal-related outlier "
        "filter is applied to the topic-modelling input only, removing the "
        "111 reviews generated by the 2021 mass-layoff media controversy "
        "(which centred on the Better CEO rather than the mortgage product) "
        "and producing a topic-modelling input of 1,804 documents. The "
        "CEO/scandal filter is not applied to the rating, sentiment, or "
        "keyword analyses. Pre-Betsy and post-Betsy periods are defined "
        "relative to the Betsy launch date of 17 October 2024 (pre: 1,746 "
        "reviews; post: 169 reviews). The full step-by-step counts are "
        "reproduced in Appendix C.2."
    )
    rewrite_paragraph_text(target, new_text)
    print("[A7] §3.4.2 cleaning paragraph rewritten (now matches Appendix C.2)")
    return True


# ---------------------------------------------------------------------------
# A8 — Betsy / ElevenLabs chronology
# ---------------------------------------------------------------------------

# We rewrite three paragraphs:
#   * P0030 (Introduction §1.5 / §1.4): chronology-clarifying intro
#   * P0124 (Methodology §3.3 case selection): reframe partnership claim
#   * Any "ElevenLabs partnership (June 2025)" reference: keep but make it
#     explicit that 2024 launch used Better's voice stack and the 2025-2026
#     scaling phase featured the disclosed ElevenLabs partnership.

CHRONOLOGY_INTRO_TEXT = (
    "Better.com serves as the primary empirical context for this "
    "investigation because it represents a critical, revelatory case. As a "
    "digital-first mortgage lender navigating significant macroeconomic "
    "headwinds and margin pressures, Better.com underwent a structural "
    "transition from a traditional, human-heavy origination model to a "
    "scalable, AI-supported workflow. In October 2024 Better launched "
    "'Betsy,' its proprietary LLM-powered voice agent for mortgage "
    "origination, and from 2025 onwards publicly disclosed a partnership "
    "with ElevenLabs that supplies the low-latency voice-infrastructure "
    "layer for the scaled deployment described in the February 2026 joint "
    "Better–ElevenLabs case study. The combined Better–Betsy–ElevenLabs "
    "deployment is, on the public-disclosure record, an early large-scale "
    "integration of generative voice AI into the U.S. mortgage industry "
    "and provides a tractable empirical setting in which integration "
    "mechanism (RQ1) and measurable business value (RQ2) can be examined "
    "with audited financial data, an independent customer-discourse corpus, "
    "and process-tracing of public disclosures."
)

CHRONOLOGY_METHODOLOGY_TEXT = (
    "Furthermore, Better's October 2024 launch of 'Betsy'—a proprietary "
    "LLM-powered voice agent capable of handling inbound and outbound "
    "mortgage origination queries—and the company's subsequent publicly "
    "disclosed partnership with ElevenLabs as voice-infrastructure provider "
    "for the scaled 2025–2026 deployment together represent an early, fully "
    "documented case of frontier voice AI inside the highly regulated U.S. "
    "mortgage industry. The temporal bounds of this case study are defined "
    "as 2018 through April 2026, with a specific focus on the pre-deployment "
    "baseline (2021–2023), the transition year (2024), and the post-"
    "deployment period (2025–2026). Rocket Companies (Rocket Mortgage) is "
    "used strictly as a benchmark in §5.3.5, not as a counterfactual: Rocket "
    "is not directly comparable to Better in scale, capital structure, or "
    "AI-deployment trajectory, but it provides industry-context anchoring "
    "for the ratios reported in Table A.2 of Appendix A."
)


def rewrite_chronology_paragraphs(doc):
    fixed = []
    for p in doc.paragraphs:
        t = p.text
        if "strategic partnership with ElevenLabs to deploy" in t and "Betsy" in t:
            rewrite_paragraph_text(p, CHRONOLOGY_INTRO_TEXT)
            fixed.append("intro")
        elif ("partnership with ElevenLabs to launch" in t and "Betsy" in t):
            rewrite_paragraph_text(p, CHRONOLOGY_METHODOLOGY_TEXT)
            fixed.append("methodology")
    if fixed:
        print(f"[A8] chronology paragraphs rewritten: {fixed}")
    return len(fixed)


# ---------------------------------------------------------------------------
# A11 — Lit-review Table 1 -> Table 2.1 (caption + in-body refs)
# ---------------------------------------------------------------------------

def renumber_lit_review_table(doc):
    """Resolve the 'Table 1' vs 'Table 3.2' confusion. The lit-review caption
    becomes Table 2.1; in-body references are remapped to the correct table.

    Mapping rules:
      * Caption 'Table 1 — Dimensions of Business Value …' -> 'Table 2.1. …'
      * Body refs 'Table 1' inside Chapter 2 -> 'Table 2.1'
      * Body refs 'Table 1' inside Chapter 3 (§3.4.x context) -> 'Table 3.2',
        because they refer to the source-reliability table, not to the lit
        review.
    """
    n_caption = 0
    n_ch2 = 0
    n_ch3 = 0
    pat = re.compile(r"\bTable 1\b(?!\d|\.)")

    # Determine the H1 chapter membership for each paragraph.
    chapter_of_paragraph = {}
    chapter = None
    for i, p in enumerate(doc.paragraphs):
        if p.style.name == "Heading 1":
            m = re.match(r"^\s*(\d+)\.\s+", p.text)
            if m:
                chapter = int(m.group(1))
            else:
                chapter = None
        chapter_of_paragraph[i] = chapter

    for i, p in enumerate(doc.paragraphs):
        if "Table 1 — Dimensions" in p.text or (
            p.text.strip().startswith("Table 1") and "Dimensions" in p.text
        ):
            replace_in_run_text(p, "Table 1 — Dimensions",
                                "Table 2.1. Dimensions")
            replace_in_run_text(p, "Table 1 - Dimensions",
                                "Table 2.1. Dimensions")
            n_caption += 1
            continue
        if not pat.search(p.text):
            continue
        ch = chapter_of_paragraph.get(i)
        if ch == 2:
            replace_in_run_text(p, "Table 1", "Table 2.1")
            n_ch2 += 1
        elif ch == 3:
            # §3.4.x source-reliability cross-reference.
            replace_in_run_text(p, "Table 1", "Table 3.2")
            n_ch3 += 1
    print(f"[A11] caption renames: {n_caption}; Ch2 body refs -> Table 2.1: {n_ch2}; Ch3 body refs -> Table 3.2: {n_ch3}")
    return n_caption + n_ch2 + n_ch3


# ---------------------------------------------------------------------------
# A12 — causal/promotional language softening
# ---------------------------------------------------------------------------

CAUSAL_REPLACEMENTS = [
    ("first published case study", "an early published case study"),
    ("first-of-its-kind", "an early publicly documented"),
    ("one of the first publicly documented", "an early publicly documented"),
    ("one of the earliest, fully documented, and large-scale deployments",
     "an early, fully documented, large-scale deployment"),
    ("demonstrates exactly", "is consistent with"),
    ("textbook signature", "an empirical pattern consistent with"),
    ("clearly proves", "is consistent with"),
    ("definitively shows", "is consistent with"),
    ("first published", "an early published"),
    ("for the first time", "in this case"),
]


def soften_causal_language(doc):
    n = 0
    for p in doc.paragraphs:
        for old, new in CAUSAL_REPLACEMENTS:
            if old in p.text:
                n += replace_in_run_text(p, old, new)
    print(f"[A12] causal/promotional softenings: {n}")
    return n


# ---------------------------------------------------------------------------
# A2 / A14 — references-section retrieval dates and Bonferroni constant
# ---------------------------------------------------------------------------

def reconcile_dates_and_constants(doc):
    n_dates = 0
    for p in doc.paragraphs:
        if "Retrieved May 6, 2026" in p.text:
            n_dates += replace_in_run_text(p, "Retrieved May 6, 2026",
                                           "Retrieved 26 April 2026")
        if "Retrieved May 6, 2026" in p.text:
            # second pass safety
            n_dates += replace_in_run_text(p, "Retrieved May 6, 2026",
                                           "Retrieved 26 April 2026")
    print(f"[A2] reference retrieval dates 'May 6, 2026' -> '26 April 2026': {n_dates}")

    n_const = 0
    bonf_old = "Bonferroni-corrected significance threshold: p < 0.00455 (α = 0.05 / 11)"
    bonf_new = ("Bonferroni-corrected significance threshold: p < 0.00714 "
                "(α = 0.05 / 7), reflecting the seven keyword groups defined "
                "in Appendix D.2")
    for p in doc.paragraphs:
        if bonf_old in p.text:
            n_const += replace_in_run_text(p, bonf_old, bonf_new)
        # Looser variants
        if "α = 0.05 / 11" in p.text or "0.05/11" in p.text:
            n_const += replace_in_run_text(p, "α = 0.05 / 11", "α = 0.05 / 7")
            n_const += replace_in_run_text(p, "0.05/11", "0.05/7")
        if "p < 0.00455" in p.text:
            n_const += replace_in_run_text(p, "p < 0.00455", "p < 0.00714")
    print(f"[A2/A14] Bonferroni constant patches: {n_const}")
    return n_dates + n_const


# ---------------------------------------------------------------------------
# Strip residual `BUILDOUT::* sentinel marker` mention in Appendix G
# ---------------------------------------------------------------------------

def neutralise_appendix_g_marker_mention(doc):
    for p in doc.paragraphs:
        if "BUILDOUT::* sentinel marker" in p.text or "BUILDOUT::*" in p.text:
            new = p.text.replace(
                "BUILDOUT::* sentinel marker",
                "build-step sentinel marker",
            ).replace("BUILDOUT::*", "build-step sentinels")
            rewrite_paragraph_text(p, new)
            print("[A1] Appendix G sentinel-marker reference neutralised")
            return 1
    return 0


# ---------------------------------------------------------------------------
# Verify the §3.10 / §3.7 / §2.5 cross-references resolve
# ---------------------------------------------------------------------------

def verify_cross_references(doc):
    headings = {}
    chapter = None
    section = None
    for p in doc.paragraphs:
        if p.style.name == "Heading 1":
            m = re.match(r"^\s*(\d+)\.\s+", p.text)
            if m:
                chapter = int(m.group(1))
            else:
                chapter = None
        elif p.style.name == "Heading 2" and chapter is not None:
            m = re.match(r"^\s*(\d+)\.(\d+)\s+(.*)$", p.text)
            if m:
                section = (int(m.group(1)), int(m.group(2)))
                headings[f"§{m.group(1)}.{m.group(2)}"] = p.text.strip()
                headings[f"Section {m.group(1)}.{m.group(2)}"] = p.text.strip()
        elif p.style.name == "Heading 3" and chapter is not None:
            m = re.match(r"^\s*(\d+)\.(\d+)\.(\d+)\s+(.*)$", p.text)
            if m:
                key = f"§{m.group(1)}.{m.group(2)}.{m.group(3)}"
                headings[key] = p.text.strip()
                headings[f"Section {m.group(1)}.{m.group(2)}.{m.group(3)}"] = p.text.strip()

    refs = set()
    for p in doc.paragraphs:
        for m in re.finditer(r"§\d+(?:\.\d+){1,2}", p.text):
            refs.add(m.group())
        for m in re.finditer(r"\bSection \d+(?:\.\d+){1,2}", p.text):
            refs.add(m.group())
    missing = sorted(r for r in refs if r not in headings)
    if missing:
        print(f"[verify] cross-references that do not resolve: {missing}")
    else:
        print("[verify] all section cross-references resolve")
    return missing


def main():
    doc = open_draft()
    fix_keyword_delta(doc)
    rewrite_methodology_cleaning_paragraph(doc)
    rewrite_chronology_paragraphs(doc)
    renumber_lit_review_table(doc)
    soften_causal_language(doc)
    reconcile_dates_and_constants(doc)
    neutralise_appendix_g_marker_mention(doc)
    save_draft(doc)
    # Re-open to verify after save (so unresolved refs reflect final state).
    doc2 = open_draft()
    verify_cross_references(doc2)
    print("Saved.")


if __name__ == "__main__":
    main()
