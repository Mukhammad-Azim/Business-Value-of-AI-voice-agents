"""
14_targeted_pass.py
===================

Apply the supervisor's second-round targeted corrections.

  High-priority
  -------------
  H1 (Section 6.5): Remove the "absence of UDAAP-level enforcement events"
       claim and replace it with cautious wording that does not interpret
       absence-of-evidence as evidence-of-compliance-value.
  H2 (Section 3.7): Two references to Appendix D should point to Appendix F
       (Source Reliability and Citation Audit Summary). Appendix D is the
       Topic Inventory and Keyword Dictionary.
  H3 (Section 8.9): Update the future-research cross-reference from
       Section 9.4 to Section 9.5 (the September pass added a new
       Section 9.4 Limitations and renumbered Future Research to 9.5).
  H4 (Section 9.2): Replace "see Section 5.2 for the full numeric detail"
       with "see Section 5.3 for the financial-operational detail and
       Section 5.4 for the customer-experience evidence", and tighten the
       second parenthetical from "see Section 5.3 and Section 5.4..." to
       "see Section 5.4...".
  H5 (Section 9.2): Drop "CSAT" from "management-reported NPS and CSAT
       improved" because CSAT is not analysed anywhere in Chapters 1-8.

  Medium-priority
  ---------------
  M6  (Chapter 2):  "demonstrating customer satisfaction" -> "improving
       customer satisfaction indicators".
  M7  (Chapter 2):  "scores -those organisations" -> "scores - those
       organisations" (en-spaced em-dash). Also fix the matching
       "indicators -" to em-dash for typographic consistency.
  M8  (Chapter 2):  Wang et al. (2023) methodology sentence:
       "...creating quasi-experimental variation that allows descriptive
        benchmark comparison analysis to isolate the causal effects..."
       -> "...creating quasi-experimental variation that allows the
        authors to estimate the causal effects of AI implementation".
  M9  (Chapter 2):  Soften the categorical claim "No published case
       study has yet linked..." to "To the author's knowledge, little
       published academic work has yet linked...".
  M10 (Section 1.7): Revise the scope-boundary paragraph so it does
       not contradict the Chapter 6/7/8 SAFE Act / UDAAP / regulatory-
       boundary discussion.
  M11 (Section 6.2): Replace "produce theatre rather than operational
       leverage" with "be symbolic rather than produce measurable
       operational leverage".
  M12 (Section 6.4): Replace the unsourced "post-decision update window"
       phrase with the more cautious "borrower-communication tasks
       around the October 2024 launch".
  M13 (Chapter 5): Deduplicate "...consistent with operational leverage
       and is consistent with the AI-enabled..." to "...consistent with
       operational leverage and with the AI-enabled..." in two paragraphs.

The script is idempotent. Reference list, official source titles, URLs,
and file paths are left untouched.
"""

from __future__ import annotations

import sys

sys.path.insert(0, ".")
from _helpers import open_draft, save_draft  # noqa: E402


# ---------------------------------------------------------------------------
# Replacements: (old_substr, new_substr, label)
# ---------------------------------------------------------------------------

REPLACEMENTS = [
    # H1. Section 6.5 -- absence-of-enforcement claim. Apply to paragraph 404.
    (
        "It also produces regulatory-compliance value that is directly "
        "visible in the absence of UDAAP-level enforcement events but "
        "indirectly visible in Better\u2019s ongoing public-company status.",
        "It may also support regulatory-compliance value by making "
        "escalation boundaries auditable, although this thesis does not "
        "independently evaluate regulatory compliance outcomes.",
        "H1. \u00a76.5 'absence of UDAAP-level enforcement' rewritten",
    ),

    # H2a. Section 3.7 -- "Appendix D records the per-source reliability ..."
    (
        "Appendix D records the per-source reliability classification used "
        "in this thesis.",
        "Appendix F records the per-source reliability classification used "
        "in this thesis.",
        "H2a. \u00a73.7 'Appendix D records...' -> 'Appendix F records...'",
    ),

    # H2b. Section 3.7 -- second mention.
    (
        "and Appendix D (per-source classification).",
        "and Appendix F (per-source classification).",
        "H2b. \u00a73.7 'Appendix D (per-source classification)' -> 'Appendix F'",
    ),

    # H3. Section 8.9 -- future-research cross-reference.
    (
        "Future research is articulated more fully in \u00a79.4.",
        "Future research is articulated more fully in \u00a79.5.",
        "H3. \u00a78.9 future-research ref \u00a79.4 -> \u00a79.5",
    ),

    # H4 + H5. Section 9.2 -- replace Section 5.2 ref, drop CSAT, tighten
    # second parenthetical. Done as a single multi-substring replace.
    (
        "(see \u00a75.2 for the full numeric detail and \u00a75.6 for the "
        "macro-environment caveats). Second, the customer-experience signal "
        "is divergent across instruments: management-reported NPS and CSAT "
        "improved over the same window, while the independent Trustpilot "
        "corpus shows a post-deployment decline in mean star rating and in "
        "VADER sentiment, alongside a contraction of Cost/Rates discourse "
        "as the only keyword-prevalence shift surviving multiple-comparison "
        "correction (see \u00a75.3 and \u00a75.4 for the full statistical "
        "treatment, including Welch tests, effect sizes, and the BERTopic "
        "and keyword-prevalence diagnostics).",
        "(see \u00a75.3 for the financial-operational detail and \u00a75.6 "
        "for the macro-environment caveats). Second, the customer-experience "
        "signal is divergent across instruments: management-reported NPS "
        "improved over the same window, while the independent Trustpilot "
        "corpus shows a post-deployment decline in mean star rating and in "
        "VADER sentiment, alongside a contraction of Cost/Rates discourse "
        "as the only keyword-prevalence shift surviving multiple-comparison "
        "correction (see \u00a75.4 for the full statistical treatment, "
        "including Welch tests, effect sizes, and the BERTopic and "
        "keyword-prevalence diagnostics).",
        "H4+H5. \u00a79.2 ref \u00a75.2 -> \u00a75.3, drop CSAT, tighten 2nd parenthetical",
    ),

    # M6. Chapter 2 -- "demonstrating customer satisfaction".
    (
        "compressing approval times and demonstrating customer satisfaction.",
        "compressing approval times and improving customer satisfaction "
        "indicators.",
        "M6. Ch2 'demonstrating customer satisfaction' -> 'improving "
        "customer satisfaction indicators'",
    ),

    # M7. Chapter 2 -- punctuation. There are two ASCII hyphens around
    # the parenthetical list "performance indicators - ... - those".
    # Convert both to spaced em-dashes.
    (
        "performance indicators - conversion rates, cost per "
        "interaction, revenue per lead, customer satisfaction scores "
        "-those",
        "performance indicators \u2014 conversion rates, cost per "
        "interaction, revenue per lead, customer satisfaction scores "
        "\u2014 those",
        "M7. Ch2 hyphens -> em-dashes around 'performance indicators ... "
        "scores ... those'",
    ),

    # M8. Chapter 2 -- Wang et al. (2023) methodology sentence (paragraph 75).
    (
        "creating quasi-experimental variation that allows descriptive "
        "benchmark comparison analysis to isolate the causal effects of "
        "AI implementation.",
        "creating quasi-experimental variation that allows the authors "
        "to estimate the causal effects of AI implementation.",
        "M8. Ch2 Wang et al. methodology - 'descriptive benchmark "
        "comparison analysis to isolate' -> 'allows the authors to estimate'",
    ),

    # M9. Chapter 2 -- soften "No published case study has yet linked".
    (
        "No published case study has yet linked SEC-filed financial "
        "trajectory, independent customer-discourse mining, and qualitative "
        "process tracing of integration architecture for a voice LLM agent "
        "in U.S. mortgage origination.",
        "To the author\u2019s knowledge, little published academic work "
        "has yet linked SEC-filed financial trajectory, independent "
        "customer-discourse mining, and qualitative process tracing of "
        "integration architecture for a voice LLM agent in U.S. mortgage "
        "origination.",
        "M9. Ch2 'No published case study has yet linked...' softened",
    ),

    # M10. Section 1.7 -- revise scope boundary so it does not contradict
    # the Chapter 6/7/8 regulatory-boundary discussion. Replace only the
    # first sentence of the paragraph; keep the academic-literature
    # citation and the no-technical-AI-build sentence as-is.
    (
        "Finally, the research does not aim to analyse ethical risks, "
        "regulatory concerns, or broader societal implications of "
        "AI-generated voices. While such topics are undoubtedly important "
        "(Adam et al., 2021), they fall outside the primary objective of "
        "this thesis, which is strictly centred on business value creation "
        "and process integration.",
        "Finally, the thesis does not analyse broader ethical, societal, "
        "or legal accountability questions around AI-generated voices, "
        "but it does examine regulatory workflow boundaries where they "
        "directly affect business-value realisation, task allocation, and "
        "human escalation. While the broader normative debates around "
        "AI-generated voices are undoubtedly important (Adam et al., "
        "2021), they fall outside the primary objective of this thesis, "
        "which is strictly centred on business value creation and process "
        "integration.",
        "M10. \u00a71.7 scope-boundary paragraph rewritten to acknowledge "
        "regulatory workflow boundaries",
    ),

    # M11. Section 6.2 -- replace 'theatre' with 'symbolic'.
    (
        "deployment is likely to produce theatre rather than operational "
        "leverage.",
        "deployment is likely to be symbolic rather than to produce "
        "measurable operational leverage.",
        "M11. \u00a76.2 'produce theatre' -> 'be symbolic ... measurable "
        "operational leverage'",
    ),

    # M12. Section 6.4 -- soften unsourced "post-decision update window"
    # phrase.
    (
        "In the case, this slice was the post-decision update window "
        "beginning around the October 17, 2024 launch (Better Home & "
        "Finance Holding Company, 2024a).",
        "In the case, this slice covered borrower-communication tasks "
        "around the October 2024 launch (Better Home & Finance Holding "
        "Company, 2024a).",
        "M12. \u00a76.4 'post-decision update window' -> "
        "'borrower-communication tasks around the October 2024 launch'",
    ),

    # M13. Chapter 5 -- deduplicate "consistent with ... is consistent
    # with..." in two paragraphs.
    (
        "is a pattern consistent with operational leverage and is "
        "consistent with the AI-enabled operational-leverage hypothesis "
        "examined in this thesis.",
        "is a pattern consistent with operational leverage and with the "
        "AI-enabled operational-leverage hypothesis examined in this "
        "thesis.",
        "M13. Ch5 dedupe 'consistent with operational leverage and is "
        "consistent with' -> 'consistent with operational leverage and "
        "with'",
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

    # Find references heading so we don't touch the reference list.
    refs_start_index = None
    for idx, p in enumerate(doc.paragraphs):
        s = p.style.name if p.style else ""
        if s.startswith("Heading 1") and p.text.strip().startswith("References"):
            refs_start_index = idx
            break

    body_paragraphs = (
        doc.paragraphs[:refs_start_index]
        if refs_start_index is not None
        else list(doc.paragraphs)
    )
    appendix_paragraphs = (
        doc.paragraphs[refs_start_index + 1:] if refs_start_index is not None else []
    )
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
    print("Targeted second-round correction pass")
    print("=" * 60)
    for line in summary:
        print(line)


if __name__ == "__main__":
    main()
