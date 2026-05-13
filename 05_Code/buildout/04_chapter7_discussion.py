"""
04_chapter7_discussion.py
=========================

Insert Chapter 7 \u2014 *Discussion* \u2014 between Chapter 6 and the
References block. The discussion connects the empirical findings of
Chapter 5 and the design pattern of Chapter 6 to the literature reviewed in
Chapter 2, evaluates competing explanations, and articulates the
theoretical and practical contributions of the thesis.

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
H1("7. Discussion")
# ---------------------------------------------------------------------------

H2("7.1 Introduction")

P(
    "This chapter integrates the empirical findings of Chapter 5 and the "
    "design pattern formalised in Chapter 6 with the literature reviewed "
    "in Chapter 2. It does so under three guiding constraints. First, the "
    "discussion does not exceed what the evidence supports: the case is "
    "single, observational, and dependent on a mix of audited, "
    "management-reported, vendor, and self-selected user-generated "
    "evidence; the discussion therefore privileges interpretive depth over "
    "causal identification. Second, the discussion takes alternative "
    "explanations seriously and asks where the case-study evidence is "
    "underdetermined. Third, the discussion separates the contributions "
    "that hold robustly under alternative explanations from those that "
    "depend on assumptions about the role of Betsy specifically. The "
    "chapter is organised around five questions: how the financial "
    "trajectory should be interpreted (\u00a77.2), how the divergence "
    "between management-reported NPS and independent Trustpilot discourse "
    "should be interpreted (\u00a77.3), what the case contributes to the "
    "theoretical literature (\u00a77.4), what competing explanations "
    "imply (\u00a77.5), and what the practical implications are for "
    "lenders, vendors, and regulators (\u00a77.6). Section 7.7 summarises "
    "the discussion."
)

# ---------------------------------------------------------------------------
H2("7.2 Interpreting the Financial Trajectory")
# ---------------------------------------------------------------------------

P(
    "Three financial signals from Chapter 5 anchor the discussion: the "
    "expense-ratio trajectory (4.79 \u2192 2.89 \u2192 2.01 between 2023 "
    "and 2025), the revenue-per-employee trajectory ($0.094M \u2192 "
    "$0.087M \u2192 $0.124M), and the net-loss trajectory (\u2212$536.4M "
    "\u2192 \u2212$206.3M \u2192 \u2212$165.9M). Read together, these "
    "signals are consistent with AI-enabled operational leverage of the "
    "kind anticipated in the AI-productivity literature, but they do not "
    "isolate the contribution of the voice agent. Two observations are "
    "important. First, the expense-ratio improvement is fastest in 2024, "
    "the year Betsy was launched (October 17, 2024), but it is not "
    "discontinuous at the launch date; the ratio had already begun to "
    "improve from its 2022\u20132023 trough as Better\u2019s post-IPO "
    "restructuring took effect (Better Home & Finance Holding Company, "
    "2024b, 2025a). Second, revenue-per-employee in 2025 ($0.124M) is "
    "below the 2021\u20132023 pre-period RPE average ($0.130M), although "
    "above the 2024 nadir; the trajectory is therefore better understood "
    "as a recovery toward the pre-period operating envelope than as a "
    "step-change beyond it."
)

P(
    "These observations are consistent with the AI-productivity "
    "literature\u2019s emphasis on task reallocation rather than full "
    "labor substitution (Acemoglu & Restrepo, 2019; Brynjolfsson, Li, & "
    "Raymond, 2023). They are also consistent with the operational "
    "patterns reported in voice-AI field studies in customer-service "
    "settings, where productivity gains accrue to lower-skilled or "
    "lower-tenure workers reassigned to coordination-intensive roles "
    "(Brynjolfsson et al., 2023; Wang et al., 2023). The Better.com case "
    "differs from those settings in two ways. First, the case is in a "
    "regulated workflow (mortgage origination) in which the regulated "
    "boundary itself shapes the agent\u2019s task scope; the productivity "
    "channel therefore co-exists with a regulatory-compliance channel "
    "that is largely absent in the call-center literature. Second, the "
    "voice agent operates inside a process-aware operating platform "
    "(Tinman) that is itself a precondition for the productivity gains "
    "the financial trajectory exhibits. Without Tinman, the same agent "
    "would not have the workflow-state access required to coordinate the "
    "loan."
)

P(
    "A cautious reading therefore states three reconcilable propositions. "
    "First, the financial trajectory is consistent with the design "
    "pattern\u2019s prediction that, given the four prerequisites, "
    "operational leverage is observable. Second, the trajectory cannot "
    "be attributed to Betsy in isolation; the contribution of macroeconomic "
    "recovery, restructuring, and Tinman maturity is not separable in the "
    "case data. Third, the AI-productivity literature\u2019s prediction "
    "that gains accrue through task reallocation and operational leverage "
    "is supported descriptively by the trajectory and is consistent with "
    "the Better\u2013ElevenLabs joint release\u2019s reported call-volume "
    "expansion alongside a reduced human staff (\u00a75.3). The thesis "
    "stops at \u201cconsistent with\u201d and does not claim that the "
    "trajectory empirically validates the literature."
)

# ---------------------------------------------------------------------------
H2("7.3 Interpreting the NPS \u2013 Trustpilot Divergence")
# ---------------------------------------------------------------------------

P(
    "Chapter 5 presents two customer-experience signals that point in "
    "different directions. Better\u2019s management-reported Net Promoter "
    "Score rose from 39 to 64 between 2023 and 2025 (Better Home & "
    "Finance Holding Company, 2025a), while the Trustpilot corpus shows a "
    "post-deployment decline in mean star rating (4.2806 \u2192 3.8580, p "
    "= 0.0019, d = 0.2899) and a decline in mean VADER compound sentiment "
    "(0.6416 \u2192 0.5151, p = 0.0057, d = 0.2505). The thesis treats this "
    "divergence as the most informative single finding in the empirical "
    "chapter and resists the temptation to resolve it by privileging "
    "either signal."
)

P(
    "The literature on consumer behaviour and AI interaction reviewed in "
    "\u00a72.5 suggests four reasons why these two instruments should be "
    "expected to diverge in this case rather than to converge. First, "
    "Trustpilot reviews over-sample emotionally engaged customers; the "
    "instrument over-represents the tails of the customer-experience "
    "distribution, while NPS surveys distributed at closing capture the "
    "modal customer (Filieri, 2015; Luca, 2016). Second, the post-period "
    "Trustpilot sample is small (n = 169) relative to the pre-period "
    "(n = 1,746), and self-selection therefore has more leverage on the "
    "post-period mean. Third, the AI literature on backend-AI services "
    "predicts that customer-side AI attribution will be low when the AI "
    "system is not branded to the end user (Mogaji & Nguyen, 2021; "
    "Aggarwal, Kumar, & Srivastava, 2025); the Trustpilot-explicit-AI "
    "mention rate is consistent with this prediction (\u22481.15 percent "
    "pre, \u22481.18 percent post). Fourth, an algorithm-aversion effect "
    "may further depress public-discourse evaluations of automated "
    "service even when the underlying service quality is unchanged "
    "(Dietvorst, Simmons, & Massey, 2015)."
)

P(
    "The Cost/Rates discourse shift is the most diagnostic single finding "
    "in the keyword-prevalence analysis: it shifts by \u221212.35 "
    "percentage points and is the only keyword group whose shift survives "
    "Bonferroni correction. Two interpretations are consistent with this "
    "shift. The first is that the customers reviewing Better.com after "
    "October 2024 differ in their reasons for reviewing: cost and rates "
    "are mentioned less because the post-period reviewing population is "
    "more concentrated on operational frustrations than on transactional "
    "outcomes. The second is that the broader discourse environment "
    "changed: the post-period overlaps a partial recovery of the "
    "mortgage-rate environment (Mortgage Bankers Association, 2024a), "
    "and customers are less likely to write rate-related reviews when the "
    "rate environment is less salient. The two interpretations are not "
    "mutually exclusive, and the case data cannot adjudicate between them. "
    "What they jointly imply is that public-discourse evidence on "
    "voice-AI deployment must be read alongside management-reported "
    "instruments and triangulated against operational evidence, rather "
    "than substituted for them."
)

# ---------------------------------------------------------------------------
H2("7.4 Theoretical Contributions")
# ---------------------------------------------------------------------------

P(
    "The thesis contributes to three threads of the literature. The first "
    "is the AI service hierarchy (Huang & Rust, 2018). The Better.com "
    "case extends that hierarchy by showing that mechanical and analytical "
    "service work can be substantially automated by a voice LLM agent "
    "scoped to the coordination layer of a regulated workflow, while the "
    "intuitive and empathetic layers remain inside the human-AI "
    "collaboration model. The case is also consistent with the "
    "hierarchy\u2019s prediction that AI substitution diffuses first "
    "through the lower layers of service work; what the hierarchy does "
    "not specify, and what the case contributes, is the architectural "
    "precondition (a process-aware operating platform) for the "
    "substitution to be operational rather than rhetorical."
)

P(
    "The second thread is task\u2013technology fit (Goodhue & Thompson, "
    "1995). The case operationalises the task\u2013technology-fit lens at "
    "the workflow level rather than at the individual-task level: the "
    "fit between Betsy\u2019s coordination-layer task scope and the "
    "structured workflow state exposed by Tinman is the architectural "
    "fact that the case identifies. The case extends the task\u2013"
    "technology-fit lens by showing that, in regulated workflows, "
    "task\u2013technology fit must be evaluated against the regulated "
    "boundary as well as against the task itself: the agent\u2019s scope "
    "must fit not only the task but also the licensing and disclosure "
    "constraints that govern the task."
)

P(
    "The third thread is the AI-enabled productivity literature "
    "(Acemoglu & Restrepo, 2019; Brynjolfsson, Li, & Raymond, 2023). The "
    "case is consistent with that literature\u2019s prediction that "
    "AI-related productivity gains materialise through task reallocation "
    "rather than full labor substitution and may emerge alongside "
    "ambiguous customer-perception effects when the AI system operates "
    "as backend infrastructure (Mogaji & Nguyen, 2021; Aggarwal, Kumar, & "
    "Srivastava, 2025). The case adds a regulated-workflow boundary "
    "condition that the AI-productivity literature has examined less "
    "frequently: the productivity channel and the regulatory-compliance "
    "channel are not separable in the case data, and the four-prerequisite "
    "design pattern specifies the architectural arrangement under which "
    "they are jointly observed."
)

P(
    "Read together, the three threads suggest that the Better.com case is "
    "an example of what might be called \u201cinvisible AI infrastructure\u201d: "
    "a voice-AI agent that is operationally consequential but customer-side "
    "imperceptible. This is not a new theoretical category; it is a "
    "synthesis of existing observations in the chatbot literature (Adam, "
    "Wessel, & Benlian, 2021), the backend-AI services literature "
    "(Mogaji & Nguyen, 2021), and the AI-productivity literature. What "
    "the case adds is an integrated empirical example in which the "
    "operational-financial signal, the customer-discourse signal, the "
    "vendor-architectural signal, and the management-reported signal can "
    "be read against each other on the same firm in the same time window."
)

# ---------------------------------------------------------------------------
H2("7.5 Alternative Explanations and Competing Hypotheses")
# ---------------------------------------------------------------------------

P(
    "Several alternative explanations could account for the financial "
    "trajectory of 2023\u20132025 in whole or in part. First, "
    "macroeconomic recovery: U.S. mortgage origination volume began to "
    "recover from its 2022\u20132023 trough as 30-year fixed mortgage "
    "rates eased and as the volume of refinance and purchase originations "
    "rose (Federal Reserve Bank of New York, 2024; Mortgage Bankers "
    "Association, 2024a). A neutral macroeconomic counterfactual cannot "
    "be constructed from the case data. The case therefore concedes that "
    "the recovery component of the trajectory is not separable from the "
    "AI-enabled component using single-firm evidence. Second, "
    "restructuring: Better\u2019s post-IPO restructuring (the NEO loan "
    "officer programme, the consolidation of operations, the headcount "
    "reductions reported in the 2023 and 2024 10-Ks) reduces the "
    "expense base independently of any AI-related effect (Better Home & "
    "Finance Holding Company, 2024b, 2025a). Third, mix shift: changes "
    "in the mix of refinance versus purchase originations affect both "
    "revenue per loan and operating margin, and the post-period mix is "
    "not constant. Fourth, peer-effect spillovers: a parallel benchmark "
    "lender (Rocket Companies, 2024, 2025) shows correlated trajectory "
    "changes during the same window, although Rocket\u2019s scale and "
    "vertical integration make a direct comparison only directional."
)

P(
    "How does each alternative bear on the design pattern? The "
    "macroeconomic-recovery and restructuring hypotheses do not "
    "invalidate the design pattern; they bound the share of the financial "
    "trajectory that the pattern is licensed to explain. The mix-shift "
    "hypothesis does not invalidate the design pattern either, but it "
    "does suggest that revenue-per-employee should be interpreted with "
    "care, and \u00a75.3.4 already does so. The peer-effect-spillovers "
    "hypothesis is the most challenging: if Rocket\u2019s 2024\u20132025 "
    "trajectory partially mirrors Better\u2019s, the operational-leverage "
    "signal cannot be attributed to AI deployment without further "
    "evidence. The case study\u2019s response is to treat Rocket as a "
    "directional industry benchmark and not as a counterfactual, and to "
    "treat the AI deployment as one of several mechanisms in a "
    "multi-mechanism explanation."
)

P(
    "On the customer-experience side, the principal alternative is that "
    "the post-Betsy Trustpilot decline reflects a broader reviewing-population "
    "drift rather than a deterioration in service quality: post-Betsy "
    "reviewers may differ in their reasons for reviewing, in the share of "
    "transactional versus operational complaints, and in the broader "
    "discourse environment. The thesis records this alternative explicitly "
    "and reads the Trustpilot evidence as one signal in a triangulated "
    "evidence base, rather than as a contradicting fact. Where the "
    "discourse evidence is genuinely uninformative \u2014 such as on the "
    "magnitude of the customer-experience effect \u2014 the thesis "
    "abstains from a single magnitude estimate."
)

# ---------------------------------------------------------------------------
H2("7.6 Practical Implications")
# ---------------------------------------------------------------------------

P(
    "The practical implications of the thesis are pitched at three "
    "audiences. For lender executives, the thesis argues that voice-AI "
    "deployment should be evaluated as the visible component of a longer "
    "digital-platform investment whose less visible components (process "
    "digitization, workflow-state APIs, data-quality investments, "
    "human-AI coordination structures) typically dominate the cost and "
    "the timeline. The four-prerequisite design pattern functions as a "
    "diagnostic checklist: a deployment that lacks any one of the four "
    "prerequisites is unlikely to generate the operational leverage the "
    "case exhibits, regardless of vendor selection. For voice-AI vendors, "
    "the thesis suggests that the boundary between voice-infrastructure "
    "value and integration-and-data-platform value is the principal "
    "commercial fault line: a high-quality voice-infrastructure layer is "
    "necessary but not sufficient for a productive deployment."
)

P(
    "For regulators, the thesis suggests that the most informative "
    "supervisory question may not be \u201cis the customer interacting "
    "with an AI?\u201d but \u201cis the regulated step routed to a "
    "licensed and identifiable human, and is the routing audit-logged?\u201d "
    "The pattern\u2019s auditable-escalation prerequisite renders the "
    "regulated boundary observable and supervisable, regardless of "
    "whether the customer is consciously aware of the AI in the routine "
    "communication that precedes it. This framing aligns with the "
    "Consumer Financial Protection Bureau\u2019s UDAAP framework and the "
    "SAFE Act\u2019s licensing requirements (Consumer Financial Protection "
    "Bureau, n.d.) and offers a workable supervisory primitive for "
    "voice-AI deployments in regulated financial workflows."
)

# ---------------------------------------------------------------------------
H2("7.7 Chapter Summary")
# ---------------------------------------------------------------------------

P(
    "Chapter 7 has integrated the empirical findings of Chapter 5 and the "
    "design pattern of Chapter 6 with the literature reviewed in Chapter "
    "2 across five threads: financial-trajectory interpretation, the "
    "NPS\u2013Trustpilot divergence, theoretical contributions to AI "
    "service-hierarchy / task\u2013technology-fit / AI-productivity "
    "literatures, alternative explanations and competing hypotheses, and "
    "practical implications for lenders, vendors, and regulators. The "
    "discussion has consistently respected the boundary between "
    "\u201cconsistent with\u201d and \u201ccaused by,\u201d and has stated "
    "the contribution of the case as descriptive, interpretive, and "
    "design-pattern-prescriptive rather than causal. Chapter 8 examines "
    "the limitations of the design and the evidence in detail; Chapter 9 "
    "states the answers to RQ1 and RQ2 and the priority directions for "
    "future research."
)


def apply(doc):
    if has_marker(doc, "ch7_inserted"):
        print("[ch7_inserted] already present; skipping")
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
                add_marker(p, "ch7_inserted")
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
    print("[ch7_inserted] inserted")
    return True


def main():
    doc = open_draft()
    if apply(doc):
        save_draft(doc)
        print("Saved.")


if __name__ == "__main__":
    main()
