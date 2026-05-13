"""
01_lit_review.py
================

Apply Chapter 2 (Literature Review) build-out tasks A3 + A4 + A5 from the
prior improvement report:

* **A3** insert Table 1 body in §99 (Dimensions of Business Value Creation
  through AI in Customer Service).
* **A4** insert the missing 5th sub-strand "Consumer Behaviour and AI
  Interaction" (§2.5) before the Synthesis subsection.
* **A5** insert a Conceptual Framework subsection (§2.6) immediately after
  the Synthesis subsection and before Chapter 3.

Idempotent: re-running the script does not duplicate content.
"""

from __future__ import annotations

import sys

sys.path.insert(0, ".")
from _helpers import (  # noqa: E402
    open_draft,
    save_draft,
    insert_paragraph_before,
    insert_paragraph_after,
    insert_table_before,
    has_marker,
    add_marker,
    find_paragraph_with_text,
    set_table_cell,
)


# ---------------------------------------------------------------------------
# Content
# ---------------------------------------------------------------------------

CONSUMER_BEHAVIOUR_TITLE = "Consumer Behaviour and AI Interaction"

CONSUMER_BEHAVIOUR_PARAS = [
    "The fifth strand of the literature relevant to this thesis examines how "
    "consumers perceive and respond to AI-mediated service interactions, with "
    "particular attention to voice-based agents. Three threads are pertinent to "
    "the present study. The first thread concerns anthropomorphism and voice "
    "naturalness. A recent review in Trends in Cognitive Sciences argues that "
    "perceived naturalness is a salient property of voice that shapes "
    "interaction with both human and artificial agents (Nussbaum et al., 2025), "
    "and a 2025 study in ACM Transactions on Human-Robot Interaction reports "
    "that more natural voices change perceptions of safety and compliance even "
    "where a direct effect on trust is not observed (Becker et al., 2025). For "
    "voice LLM agents in financial services, this implies that voice quality is "
    "a necessary-but-not-sufficient condition for credible interaction: cosmetic "
    "improvements in synthesis quality cannot compensate for back-end "
    "inadequacy, but a serviceable back-end paired with poor synthesis can "
    "undermine confidence even when the underlying answer is correct.",

    "The second thread concerns latency and conversational flow. Maslych et al. "
    "(2025) report that response latency above approximately four seconds "
    "significantly degrades both perceived response time and broader "
    "user-experience measures in LLM-powered intelligent virtual agents, and "
    "that natural conversational fillers can mitigate only part of that effect. "
    "Real-time voice interaction is therefore far less tolerant of delay than "
    "text-based interaction\u2014a finding directly relevant to mortgage "
    "origination, where each borrower call may trigger many internal system "
    "calls (Better Home & Finance Holding Company & ElevenLabs, 2026).",

    "The third thread concerns consumer attribution of service experience to "
    "AI. Mogaji and Nguyen (2021) argue that AI in customer-facing financial "
    "services frequently operates as backend or infrastructure-level "
    "technology rather than as a branded chatbot, with the consequence that "
    "customers may not consciously perceive AI as a feature of their service "
    "journey. Aggarwal et al. (2025) make a parallel observation in their "
    "voice-AI value-creation framework, distinguishing B2B and B2C value "
    "creation surfaces and noting that AI-related productivity gains may "
    "emerge alongside ambiguous customer-perception effects when the AI "
    "system is not branded to the end user.",

    "Two further considerations bear directly on the interpretation of the "
    "Trustpilot evidence presented in Chapter 5. Self-selected review-platform "
    "users are typically more emotionally engaged than the average customer, "
    "and platform reviews therefore over-sample the tails of the "
    "customer-experience distribution (Filieri, 2015; Luca, 2016). When "
    "combined with the small post-period sample size that any single-event "
    "study generates, this self-selection means that public-discourse signals "
    "on voice AI deployment must be read alongside, rather than against, "
    "management-reported survey instruments such as Net Promoter Score. A "
    "complementary literature on algorithm aversion suggests that consumers "
    "may discount algorithmic outputs after observing errors, even when those "
    "outputs outperform human judgement on average (Dietvorst, Simmons & "
    "Massey, 2015); this asymmetry is amplified in services where the stake "
    "of error is high, as it is in regulated financial transactions.",

    "Taken together, this strand of the literature implies three working "
    "propositions for the present thesis: (i) voice quality and latency "
    "function as service-design prerequisites for credible voice AI in "
    "financial services; (ii) when voice AI operates as backend infrastructure "
    "inside a regulated workflow, customer attribution of experience to AI is "
    "likely to be low, and the visibility of AI-related effects in "
    "review-platform discourse will be muted; (iii) public-discourse "
    "measurement of customer experience is informative but biased toward "
    "emotionally engaged subsets of customers, and must be triangulated with "
    "internal management measurement instruments rather than substituted for "
    "them.",
]

# Conceptual framework subsection
CONCEPTUAL_FRAMEWORK_TITLE = "Conceptual Framework: Three Complementary Lenses"

CONCEPTUAL_FRAMEWORK_PARAS = [
    "The empirical analysis in Chapter 5 is interpreted through three "
    "complementary theoretical lenses that together specify when a voice LLM "
    "agent is most likely to generate measurable business value in a regulated "
    "financial-services workflow. The first lens is the task\u2013technology "
    "fit perspective (Goodhue & Thompson, 1995), under which the operational "
    "meaningfulness of a conversational technology depends on whether the "
    "technology has access to the data and process state required to perform "
    "the task. This lens accounts for why a process-aware operating platform "
    "such as Tinman is treated in this thesis as the architectural "
    "prerequisite for a voice LLM agent: without exposed workflow state, even "
    "a state-of-the-art voice agent cannot plan, route, or coordinate.",

    "The second lens is the AI service hierarchy (Huang & Rust, 2018), which "
    "distinguishes mechanical, analytical, intuitive, and empathetic "
    "dimensions of service work and predicts that automation will diffuse "
    "first through the mechanical and analytical layers and only later, "
    "and partially, through the intuitive and empathetic layers. This lens "
    "explains why a voice agent is most likely to generate productivity gains "
    "when scoped to high-volume, structured, communication-intensive "
    "coordination work (status updates, scheduling, document follow-up) and "
    "is more contested when extended to advisory or relational tasks. The "
    "third lens is the AI-enabled productivity tradition (Acemoglu & "
    "Restrepo, 2019; Brynjolfsson, Li, & Raymond, 2023; Aggarwal, Kumar, & "
    "Srivastava, 2025), under which AI-related productivity gains tend to "
    "materialize through task reallocation rather than full labor "
    "substitution and can emerge alongside ambiguous customer-perception "
    "effects when the AI system operates as backend infrastructure rather "
    "than as a branded customer-facing experience.",

    "Read together, the three lenses generate a single integrating proposition "
    "that this thesis evaluates empirically: the deployment of a voice LLM "
    "agent in a regulated financial-services workflow is most likely to "
    "produce measurable operational leverage, while remaining largely "
    "invisible to end customers, when (i) the agent is task-fitted to a "
    "process-aware operating platform that exposes structured workflow "
    "state; (ii) the agent is scoped to the mechanical and analytical layers "
    "of service work; and (iii) the agent is governed by an explicit human-AI "
    "collaboration model that reallocates rather than substitutes labor at "
    "the regulated boundary.",

    "The research gap that the thesis addresses follows directly from this "
    "proposition. The peer-reviewed literature on chatbot value creation in "
    "financial services concentrates on text-based agents (Adam, Wessel, & "
    "Benlian, 2021; Abdulquadri, Mogaji, Kieu, & Nguyen, 2021; Andrade & "
    "Tumelero, 2022), and the small but growing voice-AI literature is "
    "dominated by call-center natural field experiments outside regulated "
    "mortgage origination (Wang, Huang, Hong, Liu, Guo, & Chen, 2023; Zhang, "
    "Frey, Goldfarb, & Teodoridis, 2023). No published case study has yet "
    "linked SEC-filed financial trajectory, independent customer-discourse "
    "mining, and qualitative process tracing of integration architecture for "
    "a voice LLM agent in U.S. mortgage origination. This is the gap into "
    "which the Better.com case is positioned, and the methodology presented "
    "in Chapter 3 operationalizes the three lenses through three "
    "complementary evidence streams (qualitative process tracing for "
    "task\u2013technology fit, financial-ratio analysis for AI-enabled "
    "productivity, and NLP-based discourse analysis for customer-perception "
    "outcomes).",
]


# ---------------------------------------------------------------------------
# Table 1 body
# ---------------------------------------------------------------------------

TABLE1_HEADERS = [
    "#",
    "Dimension",
    "Definition",
    "Representative AI mechanisms",
    "Representative academic anchor",
]

TABLE1_ROWS = [
    [
        "1",
        "Operational efficiency",
        "Reduction in unit cost, cycle time, and waiting time in service delivery.",
        "Routine-call automation; document classification; coordination automation.",
        "Andrade & Tumelero (2022); Wang et al. (2023); Aggarwal et al. (2025).",
    ],
    [
        "2",
        "Productivity",
        "Increase in output per worker through task reallocation rather than substitution.",
        "Conversational agent handling tier-1 inbound; human capacity reallocated to complex cases.",
        "Brynjolfsson, Li, & Raymond (2023); Acemoglu & Restrepo (2019); Aggarwal et al. (2025).",
    ],
    [
        "3",
        "Customer experience",
        "Change in service-quality perception, response speed, resolution rate, satisfaction, and discourse.",
        "Conversational accessibility; faster response; service consistency; voice naturalness.",
        "Adam, Wessel, & Benlian (2021); Hentzen et al. (2022); Mogaji & Nguyen (2021); Becker et al. (2025); Nussbaum et al. (2025).",
    ],
    [
        "4",
        "Financial performance",
        "Aggregate firm-level revenue, profitability, and operating-leverage outcomes.",
        "Cumulative effect of (1)\u2013(3) on revenue growth, expense intensity, RPE, and net income.",
        "Brynjolfsson et al. (2023); Aggarwal et al. (2025); Hentzen et al. (2022).",
    ],
]


# ---------------------------------------------------------------------------
# Apply the three insertions
# ---------------------------------------------------------------------------


def apply_table1(doc):
    if has_marker(doc, "lit_table_1"):
        print("[lit_table_1] already present; skipping")
        return False
    # Find P0100 ("Table 1 — Dimensions of Business Value Creation through AI ...")
    idx, anchor = find_paragraph_with_text(doc, "Dimensions of Business Value Creation through AI")
    if anchor is None:
        raise RuntimeError("Could not find Table 1 caption paragraph")
    # We insert the actual table BEFORE the paragraph that follows the caption
    # (i.e., before P0101 which begins "This framework informs...")
    next_idx = idx + 1
    next_para = doc.paragraphs[next_idx]
    n_rows = 1 + len(TABLE1_ROWS)
    n_cols = len(TABLE1_HEADERS)
    tbl = insert_table_before(next_para, n_rows, n_cols, style_name="Table Grid")
    # header
    for c, h in enumerate(TABLE1_HEADERS):
        set_table_cell(tbl.rows[0].cells[c], h, bold=True)
    # body rows
    for r, row in enumerate(TABLE1_ROWS, start=1):
        for c, value in enumerate(row):
            set_table_cell(tbl.rows[r].cells[c], value)

    # Convert the caption paragraph (currently a Normal stub) into a proper
    # caption-styled paragraph. We do not change its style aggressively; we
    # add a small marker run so re-runs don't duplicate.
    add_marker(anchor, "lit_table_1")
    print("[lit_table_1] inserted")
    return True


def apply_consumer_behaviour_strand(doc):
    if has_marker(doc, "lit_consumer_behaviour"):
        print("[lit_consumer_behaviour] already present; skipping")
        return False
    # Insert before the Synthesis: A Multi-Dimensional Framework heading (P98)
    idx, anchor = find_paragraph_with_text(doc, "Synthesis: A Multi-Dimensional Framework")
    if anchor is None:
        raise RuntimeError("Could not find Synthesis heading anchor")

    # Insert H2 heading
    h2 = insert_paragraph_before(anchor, "")
    h2.style = doc.styles["Heading 2"]
    h2.add_run(CONSUMER_BEHAVIOUR_TITLE)
    add_marker(h2, "lit_consumer_behaviour")

    # Insert paragraphs
    for ptext in CONSUMER_BEHAVIOUR_PARAS:
        p = insert_paragraph_before(anchor, "")
        p.style = doc.styles["Normal"]
        p.add_run(ptext)
    print("[lit_consumer_behaviour] inserted")
    return True


def apply_conceptual_framework(doc):
    if has_marker(doc, "lit_conceptual_framework"):
        print("[lit_conceptual_framework] already present; skipping")
        return False
    # Insert AFTER the Synthesis section's last paragraph and BEFORE
    # the chapter-3 H1. The last paragraph of synthesis is the "This
    # framework informs..." paragraph (currently P0101). We insert
    # immediately before the chapter 3 heading.
    idx, anchor = find_paragraph_with_text(doc, "3. Research Methodology")
    if anchor is None or not anchor.style.name.startswith("Heading"):
        raise RuntimeError("Could not find Chapter 3 heading")

    # Insert H2 heading
    h2 = insert_paragraph_before(anchor, "")
    h2.style = doc.styles["Heading 2"]
    h2.add_run(CONCEPTUAL_FRAMEWORK_TITLE)
    add_marker(h2, "lit_conceptual_framework")

    for ptext in CONCEPTUAL_FRAMEWORK_PARAS:
        p = insert_paragraph_before(anchor, "")
        p.style = doc.styles["Normal"]
        p.add_run(ptext)
    print("[lit_conceptual_framework] inserted")
    return True


def main():
    doc = open_draft()
    changed = False
    changed |= apply_table1(doc)
    changed |= apply_consumer_behaviour_strand(doc)
    changed |= apply_conceptual_framework(doc)
    if changed:
        save_draft(doc)
        print("Saved updated draft.")
    else:
        print("No changes.")


if __name__ == "__main__":
    main()
