"""
05_chapters_8_9.py
==================

Insert Chapter 8 (Limitations) and Chapter 9 (Conclusion) between
Chapter 7 and the References block.

Idempotent.
"""

from __future__ import annotations

import sys

sys.path.insert(0, ".")
from _helpers import (  # noqa: E402
    open_draft,
    save_draft,
    insert_paragraph_before,
    has_marker,
    add_marker,
    find_paragraph_with_text,
)

CONTENT = []


def H1(t): CONTENT.append(("h1", t))


def H2(t): CONTENT.append(("h2", t))


def H3(t): CONTENT.append(("h3", t))


def P(t): CONTENT.append(("p", t))


# ---------------------------------------------------------------------------
H1("8. Limitations")
# ---------------------------------------------------------------------------

H2("8.1 Introduction")

P(
    "Chapter 3 stated the principal methodological limitations as a "
    "consolidated table (\u00a73.10, Table 3.3); this chapter examines them "
    "in greater depth. Each limitation is described in terms of (a) the "
    "specific class of inferences it bounds, (b) the mitigation adopted "
    "in this thesis, and (c) the residual interpretive risk that survives "
    "after mitigation. The limitations are presented in the same order as "
    "Table 3.3 and connect to the alternative explanations examined in "
    "\u00a77.5."
)

# ---------------------------------------------------------------------------
H2("8.2 No Causal Identification")
# ---------------------------------------------------------------------------

P(
    "The most consequential limitation is the absence of a causal "
    "identification strategy. The thesis is observational and "
    "single-firm; no randomized assignment, no instrumental variable, "
    "and no clean quasi-experimental discontinuity is available in the "
    "case data. Consequently, no claim in the thesis is licensed to "
    "state that Betsy caused Better\u2019s expense-ratio improvement, "
    "revenue-per-employee recovery, or net-loss compression. The "
    "mitigation adopted is consistent: the thesis uses \u201cconsistent "
    "with,\u201d \u201cassociated with,\u201d \u201csuggests,\u201d and "
    "\u201cprovides directional evidence\u201d throughout, and the "
    "discussion in \u00a77.5 explicitly treats macroeconomic recovery, "
    "restructuring, mix shift, and peer effects as alternative "
    "explanations. The residual risk is that examiners or readers may "
    "import a causal interpretation that the thesis does not state; "
    "the design-pattern framing in Chapter 6 is intended in part to "
    "preclude this misreading by treating the four prerequisites as "
    "joint conditions for an observable outcome rather than as causes "
    "of it."
)

# ---------------------------------------------------------------------------
H2("8.3 Annual Financial Granularity")
# ---------------------------------------------------------------------------

P(
    "The audited financial data in this thesis is annual (10-K) and "
    "quarterly (10-Q). Betsy launched on October 17, 2024; consequently, "
    "fiscal year 2024 contains both a pre-Betsy and a post-Betsy "
    "operating period, and 2024 figures must be interpreted as a "
    "transition year. The mitigation adopted is twofold. First, the "
    "thesis privileges 2025 figures (the first full post-Betsy fiscal "
    "year) and the 2023 baseline (the last full pre-Betsy fiscal year) "
    "for the operational-leverage interpretation (Chapter 5, \u00a75.3). "
    "Second, the thesis does not run a within-2024 difference-in-means "
    "test on the financial data, because annual reporting cannot support "
    "such a test. The residual risk is that the magnitude of the "
    "transition signal is sensitive to the precise fiscal boundaries "
    "available in the SEC filings; this sensitivity is unrecoverable "
    "without quarterly disclosures with sufficient operational granularity."
)

# ---------------------------------------------------------------------------
H2("8.4 Reliance on Public-Data and Single-Vendor Sources")
# ---------------------------------------------------------------------------

P(
    "The thesis relies on Better\u2019s SEC disclosures, the joint "
    "Better\u2013ElevenLabs press release, the ElevenLabs vendor materials, "
    "and the Mortgage Bankers Association industry reports for its "
    "operating evidence. Two interpretive risks follow. First, "
    "vendor-reported metrics (call volumes, conversion-rate changes, "
    "agent-handled-call counts) are subject to commercial-marketing "
    "incentives. The mitigation adopted is to introduce every vendor "
    "metric with the flag \u201cVendor materials report \u2026\u201d and "
    "to triangulate against Better\u2019s SEC disclosures wherever "
    "possible. Second, Better\u2019s management-reported operating "
    "metrics (Net Promoter Score; \u201capproximately 100,000 mortgage-related "
    "calls per month\u201d; \u201capproximately 1.89 million inbound and "
    "outbound calls in 2025\u201d) are not externally audited. The "
    "mitigation is to introduce them with \u201cBetter has reported "
    "that \u2026\u201d and to keep them separate from the audited "
    "financial trajectory. The residual risk is that an examiner who "
    "skim-reads the discussion may conflate the audited and unaudited "
    "channels; the source-reliability hierarchy in \u00a73.7 (Table 3.2) "
    "and the explicit wording requirements are intended to preclude this."
)

# ---------------------------------------------------------------------------
H2("8.5 Single-Case Generalizability")
# ---------------------------------------------------------------------------

P(
    "The case is a single, revelatory, and extreme case (Yin, 2018). "
    "Statistical generalization to a population of mortgage lenders is "
    "not licensed; the design supports only analytic generalization to "
    "configurations that satisfy the four prerequisites of \u00a76.2. "
    "Better.com is also unusual on the digital-maturity dimension: the "
    "Tinman platform represents an atypically advanced operating-platform "
    "starting point for a U.S. mortgage lender, and the company\u2019s "
    "willingness to disclose and brand its AI deployment "
    "publicly is itself unusual. These dimensions of unusualness mean "
    "that the case is informative about the upper envelope of voice-AI "
    "value capture in regulated financial workflows; it is less "
    "informative about the median deployment. Chapter 9 identifies "
    "multi-firm replication as a priority for future research."
)

# ---------------------------------------------------------------------------
H2("8.6 Trustpilot Self-Selection and Pre/Post Imbalance")
# ---------------------------------------------------------------------------

P(
    "The Trustpilot corpus contains 1,915 cleaned reviews split into "
    "1,746 pre-Betsy and 169 post-Betsy observations. The post-period "
    "sample is small in absolute terms and is self-selected: Trustpilot "
    "reviewers are typically more emotionally engaged than the average "
    "customer, and the platform over-samples the tails of the customer-"
    "experience distribution (Filieri, 2015; Luca, 2016). The "
    "post-period sample is also more concentrated on operational "
    "frustrations than the pre-period (Chapter 5, \u00a75.4.5). Two "
    "mitigations are adopted. First, the discussion presents the "
    "Trustpilot evidence with the seven-reason caveat list of \u00a75.4 "
    "in every comparison with NPS. Second, magnitude claims based on the "
    "Trustpilot post-period are avoided; only directional claims are "
    "made, with the explicit reservation that the post-period sample is "
    "small. The residual risk is that the Trustpilot signal may be "
    "interpreted as more informative about underlying service quality "
    "than it actually is; \u00a77.3 argues that the divergence between "
    "NPS and Trustpilot is itself the most informative single finding."
)

# ---------------------------------------------------------------------------
H2("8.7 Topic-Modeling Sensitivity")
# ---------------------------------------------------------------------------

P(
    "BERTopic results are sensitive to UMAP and HDBSCAN hyperparameters, "
    "to the embedding model, and to the random seed. Chapter 5 reports "
    "44 topics with 1,198 reviews clustered (66.4 percent) and 606 "
    "reviews classified as noise. The topic-share figures are descriptive "
    "and are not used as inferential evidence in the thesis. The "
    "keyword-prevalence analysis, by contrast, is conducted on a "
    "researcher-defined keyword dictionary that is invariant to "
    "hyperparameter selection; only Cost/Rates discourse survives "
    "Bonferroni correction, and that finding is the only "
    "keyword-prevalence finding cited as inferentially supported in the "
    "thesis (Chapter 5, \u00a75.4.3). The residual risk is that examiners "
    "may interpret the topic-share visualizations as supporting "
    "claims they were not designed to support; \u00a78.7 (this section) "
    "and \u00a73.10 (the consolidated risks table) state explicitly that "
    "topic-share figures are descriptive only."
)

# ---------------------------------------------------------------------------
H2("8.8 Rocket Comparability")
# ---------------------------------------------------------------------------

P(
    "Rocket Companies is the largest U.S. retail mortgage lender and is "
    "used in this thesis as a directional industry benchmark, not as a "
    "counterfactual (Rocket Companies, 2024, 2025). Rocket\u2019s scale, "
    "vertical integration, capital structure, and product mix differ "
    "materially from Better\u2019s, and audited-line items are not "
    "directly comparable without normalization. The thesis therefore "
    "uses Rocket only for directional benchmarking of expense intensity "
    "and revenue-per-employee. The residual risk is that a stricter "
    "examiner may regard any cross-firm comparison as overreaching; "
    "\u00a77.5 acknowledges this by treating the peer-effect-spillovers "
    "hypothesis as the most challenging alternative explanation."
)

# ---------------------------------------------------------------------------
H2("8.9 Implications for Future Research")
# ---------------------------------------------------------------------------

P(
    "The limitations enumerated above suggest a coherent future-research "
    "agenda. Multi-firm replication on a panel of digital-first lenders "
    "would address single-case generalizability. Quarterly-disclosure "
    "data or proprietary loan-level data would relax the annual-granularity "
    "constraint. Quasi-experimental designs that exploit deployment-cohort "
    "variation across teams or geographies inside a single firm would "
    "reduce reliance on external counterfactuals. Independent customer-"
    "experience instruments \u2014 administered surveys with controlled "
    "samples, audited service-quality records, randomized voice-versus-text "
    "comparisons \u2014 would relax the Trustpilot self-selection "
    "constraint. Future research is articulated more fully in \u00a79.4."
)


# ---------------------------------------------------------------------------
H1("9. Conclusion")
# ---------------------------------------------------------------------------

H2("9.1 Direct Answer to RQ1")

P(
    "RQ1 asked how voice LLM agents have been integrated into "
    "Better.com\u2019s mortgage origination processes and what this "
    "integration reveals about the technical and organizational "
    "prerequisites for deploying conversational AI in a regulated "
    "financial-services environment. The case study supports a four-part "
    "answer. First, the integration is anchored in a process-aware "
    "operating platform (Tinman) that exposes structured workflow state, "
    "document state, eligibility state, and timeline events through "
    "permissioned interfaces. Second, the voice agent (Betsy) is scoped "
    "to the coordination layer of the workflow \u2014 lead engagement, "
    "scheduling, status updates, document collection, post-decision "
    "communication \u2014 and is not scoped to underwriting, credit "
    "decisioning, or the disclosure of material loan terms. Third, the "
    "voice infrastructure (ElevenLabs Agents) supplies low-latency "
    "speech-to-text, response generation, and text-to-speech, with the "
    "operational latency target consistent with the latency thresholds "
    "documented in the human-computer interaction literature (Maslych et "
    "al., 2025). Fourth, the regulated boundary is operationalised "
    "through an auditable human-AI collaboration model in which licensed "
    "loan consultants handle regulated steps and the agent\u2013human "
    "transitions are timestamped and audit-logged. Read together, these "
    "four prerequisites are the technical and organizational conditions "
    "the case identifies for deploying conversational AI in a regulated "
    "financial-services environment."
)

H2("9.2 Direct Answer to RQ2")

P(
    "RQ2 asked what measurable business value can be associated with "
    "Better.com\u2019s voice-AI deployment across operational efficiency, "
    "productivity, customer experience, and financial performance, and "
    "what factors mediate the realization of that value. The empirical "
    "evidence in Chapter 5 supports a three-part answer. First, the "
    "post-deployment trajectory is consistent with operational leverage: "
    "the expense ratio fell from 4.79 in 2023 to 2.01 in 2025, "
    "revenue-per-employee recovered from a 2024 trough of $0.087M to "
    "$0.124M in 2025 (still below the pre-period $0.130M average), and "
    "net loss narrowed from \u2212$536.4M to \u2212$165.9M over the same "
    "window (Better Home & Finance Holding Company, 2024b, 2025a). "
    "Second, the customer-experience signal is divergent across "
    "instruments: management-reported NPS rose from 39 to 64, while the "
    "independent Trustpilot corpus shows a post-deployment decline in "
    "mean star rating (4.2806 \u2192 3.8580, p = 0.0019, d = 0.2899) and "
    "in VADER sentiment (0.6416 \u2192 0.5151, p = 0.0057, d = 0.2505); "
    "Cost/Rates discourse fell by 12.35 percentage points (the only "
    "keyword-prevalence shift surviving Bonferroni correction). Third, "
    "the value-realisation factors are the four prerequisites of the "
    "design pattern: process-aware platform, coordination-layer scope, "
    "low-latency voice infrastructure, and auditable human escalation. "
    "The thesis maintains that the financial trajectory is consistent "
    "with AI-enabled operational leverage but cannot be attributed to "
    "Betsy in isolation; the contributions of macroeconomic recovery, "
    "restructuring, and Tinman maturity are not separable from the "
    "voice-AI contribution in the case data."
)

H2("9.3 Contributions")

H3("9.3.1 Empirical Contribution")

P(
    "The thesis is the first published case study, to the author\u2019s "
    "knowledge, to triangulate audited SEC-filed financial trajectory, "
    "independent customer-discourse mining, and qualitative process "
    "tracing of integration architecture for a voice LLM agent in U.S. "
    "mortgage origination. The single-case design is deliberately "
    "revelatory rather than statistical, and the thesis records the "
    "trajectory and the discourse signal in a form that is reproducible "
    "from public sources."
)

H3("9.3.2 Methodological Contribution")

P(
    "The thesis contributes a mixed-methods triangulation protocol "
    "in which audited financial data, management-reported KPIs, "
    "vendor materials, and self-selected user-generated reviews are "
    "explicitly classified by source-reliability tier (\u00a73.7) and "
    "in which each evidence stream is paired with a wording requirement "
    "that prevents inadvertent magnitude transfer between tiers. The "
    "design-pattern artefact in Chapter 6 is offered as a reusable "
    "analytical primitive for examining future voice-AI deployments in "
    "regulated workflows."
)

H3("9.3.3 Practical Contribution")

P(
    "For lender executives, the four-prerequisite design pattern "
    "functions as a diagnostic checklist: a deployment that lacks any one "
    "of the four prerequisites is unlikely to generate the operational "
    "leverage observed in the case. For voice-AI vendors, the thesis "
    "argues that integration-and-data-platform value typically dominates "
    "voice-infrastructure value in commercial outcomes. For regulators, "
    "the thesis argues that the supervisory primitive should be the "
    "audit-logged routing of regulated communication to a licensed and "
    "identifiable human, rather than the customer\u2019s conscious "
    "awareness of the AI in the routine communication that precedes it."
)

H2("9.4 Future Research")

P(
    "Four directions for future research are most natural extensions of "
    "this thesis. First, multi-firm replication on a panel of digital-first "
    "lenders \u2014 ideally with quarterly disclosure data and consistent "
    "deployment-cohort information \u2014 would address the single-case "
    "generalizability constraint. Second, quasi-experimental designs that "
    "exploit cohort variation across teams or geographies inside a single "
    "firm would reduce reliance on external counterfactuals and permit "
    "tighter inference on the productivity channel. Third, voice-AI-specific "
    "consumer-perception research is needed in regulated financial "
    "services: latency, voice naturalness, and AI-attribution salience "
    "interact with trust and willingness to escalate, and the existing "
    "literature is dominated by laboratory and call-center studies "
    "(Becker et al., 2025; Nussbaum et al., 2025; Maslych et al., 2025). "
    "Fourth, regulatory-supervisory research is needed on the audit-log "
    "primitive for routing regulated steps: the empirical question is "
    "whether audit-logged routing reduces UDAAP-class enforcement risk "
    "in practice and whether the supervisor-side cost of monitoring "
    "such logs is bounded."
)

H2("9.5 Closing Statement")

P(
    "The Better.com case is informative because it is unusual: a "
    "publicly listed, branded voice-AI deployment in a regulated "
    "high-stakes financial workflow, with audited financial disclosures "
    "for both pre- and post-deployment fiscal years. The thesis has "
    "treated the case as a single, revelatory observation rather than as "
    "a representative one, and has argued that the value of the case "
    "lies in the configuration of conditions it documents \u2014 not in "
    "the magnitude of the outcome it generates. That configuration, "
    "formalised as the four-prerequisite design pattern of Chapter 6, "
    "is the central transferable contribution of this thesis."
)


def apply(doc):
    if has_marker(doc, "ch8_9_inserted"):
        print("[ch8_9_inserted] already present; skipping")
        return False
    _, anchor = find_paragraph_with_text(doc, "References")
    if anchor is None:
        raise RuntimeError("References anchor not found")
    is_first = True
    for kind, payload in CONTENT:
        if kind == "h1":
            p = insert_paragraph_before(anchor, "")
            p.style = doc.styles["Heading 1"]
            p.add_run(payload)
            if is_first:
                add_marker(p, "ch8_9_inserted")
                is_first = False
        elif kind == "h2":
            p = insert_paragraph_before(anchor, "")
            p.style = doc.styles["Heading 2"]
            p.add_run(payload)
        elif kind == "h3":
            p = insert_paragraph_before(anchor, "")
            p.style = doc.styles["Heading 3"]
            p.add_run(payload)
        elif kind == "p":
            p = insert_paragraph_before(anchor, "")
            p.style = doc.styles["Normal"]
            p.add_run(payload)
    print("[ch8_9_inserted] inserted")
    return True


def main():
    doc = open_draft()
    if apply(doc):
        save_draft(doc)
        print("Saved.")


if __name__ == "__main__":
    main()
