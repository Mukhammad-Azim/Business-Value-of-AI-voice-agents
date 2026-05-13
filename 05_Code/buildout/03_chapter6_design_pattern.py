"""
03_chapter6_design_pattern.py
=============================

Insert Chapter 6 \u2014 *A Voice-AI-in-Regulated-Workflow Design Pattern* \u2014
between the end of Chapter 5 and the References block in
``04_Drafts/Main_Draft.docx``. The chapter formalises the four prerequisites
identified in Chapter 5 as a transferable design pattern in the
design-science sense (Hevner et al., 2004), anchored in the Better.com /
Tinman / Betsy / ElevenLabs case and bounded for analytic generalization
(Yin, 2018).

Idempotent: running twice does not duplicate content.
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, ".")
from _helpers import (  # noqa: E402
    open_draft,
    save_draft,
    insert_paragraph_before,
    insert_picture_before,
    has_marker,
    add_marker,
    find_paragraph_with_text,
    FIG_DESIGN,
)


CONTENT = []


def H1(t): CONTENT.append(("h1", t))


def H2(t): CONTENT.append(("h2", t))


def H3(t): CONTENT.append(("h3", t))


def P(t): CONTENT.append(("p", t))


def CAP(t): CONTENT.append(("caption", t))


def FIG(path, caption): CONTENT.append(("fig", (path, caption)))


# ---------------------------------------------------------------------------
# Chapter heading
# ---------------------------------------------------------------------------

H1("6. A Voice-AI-in-Regulated-Workflow Design Pattern")

# ---------------------------------------------------------------------------
# 6.1 Introduction
# ---------------------------------------------------------------------------

H2("6.1 Introduction and Design-Science Framing")

P(
    "Chapter 5 established that Better.com\u2019s post-deployment trajectory "
    "is consistent with AI-enabled operational leverage on the "
    "financial-operational dimension and divergent across measurement "
    "instruments on the customer-experience dimension, and that this "
    "outcome is conditional on four architectural and organizational "
    "prerequisites that emerge directly from the case evidence: a "
    "process-aware operating platform, a coordination-layer scoping of the "
    "voice agent, low-latency voice infrastructure, and an auditable "
    "human-AI collaboration model with licensed-consultant escalation at "
    "the regulated boundary. This chapter formalises those four "
    "prerequisites as a transferable design pattern, in the design-science "
    "sense articulated by Hevner, March, Park, and Ram (2004): an artefact "
    "that prescribes a reusable configuration of components and rules for "
    "a recurring class of problems."
)

P(
    "Two distinctions frame the chapter. First, a design pattern is not a "
    "causal model. The pattern presented here states that, in the "
    "Better.com case, the four prerequisites are jointly observed with "
    "operational leverage and with low customer-side AI attribution; it "
    "does not state that the prerequisites caused those outcomes. The "
    "single-case revelatory design adopted in this thesis (Yin, 2018) "
    "supports analytic generalization to similar configurations rather "
    "than statistical generalization to a population of firms. Second, the "
    "design pattern is not a deployment recipe. It does not specify model "
    "size, vendor selection, dialogue system architecture, or "
    "compliance-document templates; rather, it identifies the structural "
    "conditions under which a voice LLM agent in a regulated "
    "financial-services workflow is most likely to generate measurable "
    "business value."
)

P(
    "The remainder of the chapter is organised as follows. Section 6.2 "
    "states the preconditions for value capture. Section 6.3 specifies the "
    "voice-AI architecture (illustrated in Figure 6.1). Section 6.4 "
    "describes the implementation stages observed in the case. Section 6.5 "
    "maps each prerequisite to the business-value mechanisms identified in "
    "Chapter 5. Section 6.6 states the pattern\u2019s boundary conditions. "
    "Section 6.7 outlines transferability to two adjacent regulated "
    "settings. Section 6.8 summarises the pattern."
)

# ---------------------------------------------------------------------------
# 6.2 Preconditions
# ---------------------------------------------------------------------------

H2("6.2 Preconditions for Value Capture")

P(
    "Four preconditions distinguish settings in which the voice-AI design "
    "pattern is plausible from settings in which deployment is likely to "
    "produce theatre rather than operational leverage. The first is "
    "process maturity. The receiving workflow must already be digitised "
    "and process-aware: events must be represented as discrete states with "
    "machine-readable transitions, not as opaque case-files held in "
    "individual loan officers\u2019 heads. In the Better.com case, this "
    "precondition is satisfied by the Tinman platform, whose "
    "process-state representation is the architectural prerequisite that "
    "makes Betsy\u2019s coordination layer technically meaningful (Better "
    "Home & Finance Holding Company, 2025a). The second precondition is "
    "data accessibility: the workflow state, document state, eligibility "
    "state, and timeline must be exposed to the agent through stable, "
    "permissioned interfaces. Without exposed state, even an "
    "advanced voice agent can answer general questions but cannot transact "
    "on the borrower\u2019s file."
)

P(
    "The third precondition is organizational readiness. The receiving "
    "organisation must have an existing human\u2013AI coordination "
    "structure into which the agent can be embedded: roles must be defined "
    "for routine communication, regulated-step communication, and "
    "exceptions; performance measurement must be capable of distinguishing "
    "agent-handled from human-handled interactions; and the licensing and "
    "training of human staff must already be aligned with the regulated "
    "boundary at which escalation will occur. The fourth precondition is "
    "regulatory clarity. The legal boundary between routine communication "
    "(generally permissible by an unlicensed automated agent) and "
    "regulated communication (requiring a licensed mortgage loan "
    "originator under the SAFE Act and consumer-protection oversight under "
    "the Consumer Financial Protection Bureau\u2019s UDAAP framework) must "
    "be explicit and operationalised before deployment, not after "
    "(Consumer Financial Protection Bureau, n.d.). Where regulatory "
    "clarity is absent, the agent\u2019s task scope cannot be defined and "
    "compliance risk grows with adoption."
)

# ---------------------------------------------------------------------------
# 6.3 Architecture
# ---------------------------------------------------------------------------

H2("6.3 Voice-AI Architecture: Four Prerequisites")

P(
    "Figure 6.1 presents the four-prerequisite architecture observed in "
    "the case. The design pattern consists of four components linked by "
    "dataflow and escalation paths, supported by a governance and "
    "measurement layer."
)

FIG(
    os.path.join(FIG_DESIGN, "fig_6_1_design_pattern.png"),
    "Figure 6.1. Voice-AI-in-Regulated-Workflow Design Pattern. The four "
    "prerequisites observed in the Better.com / Tinman / Betsy / ElevenLabs "
    "case are connected by the dataflow paths and the regulated-step "
    "escalation path identified in Chapter 5. The bottom panel summarises "
    "the multidimensional measurement scheme used to evaluate value capture.",
)

H3("6.3.1 Process-aware operating platform")

P(
    "The process-aware operating platform is the foundation of the design "
    "pattern. It exposes structured workflow state, document state, "
    "eligibility state, and timeline events through APIs that the voice "
    "agent can read and update under permissioning. In the Better.com "
    "case, this platform is Tinman, which is described in the company\u2019s "
    "10-K as the proprietary technology that handles a substantial share "
    "of the loan-origination workflow and supports the integration of "
    "automated agents on top of it (Better Home & Finance Holding Company, "
    "2025a). Without such a platform, an LLM voice agent reduces to a "
    "front-end conversational interface that can summarise but not "
    "advance the loan."
)

H3("6.3.2 Coordination-layer agent scope")

P(
    "The voice agent\u2019s task scope is bounded to the coordination layer: "
    "lead engagement, status updates, document collection, scheduling, "
    "and post-decision communication. It is not scoped to underwriting, "
    "credit decisioning, or the disclosure of material loan terms; those "
    "remain inside the regulated perimeter. Anchoring to the AI service "
    "hierarchy (Huang & Rust, 2018), the agent\u2019s scope sits in the "
    "mechanical and analytical layers of service work \u2014 high-volume, "
    "structured, communication-intensive activity \u2014 where AI is most "
    "consistently observed to substitute or augment human capacity. The "
    "case anchor is Betsy, described in the Betsy launch announcement and "
    "the Better\u2013ElevenLabs joint release as a 24/7 AI loan assistant "
    "supporting the loan-officer team rather than replacing it (Better "
    "Home & Finance Holding Company, 2024a; Better Home & Finance Holding "
    "Company & ElevenLabs, 2026)."
)

H3("6.3.3 Low-latency voice infrastructure")

P(
    "The voice infrastructure layer is responsible for speech-to-text, "
    "low-latency LLM response generation, and text-to-speech, returned to "
    "the borrower as a fluent voice. In the Better.com case, this layer "
    "is provided by ElevenLabs Agents (Better Home & Finance Holding "
    "Company & ElevenLabs, 2026). Two latency thresholds are operational. "
    "First, the per-turn end-to-end latency must remain below approximately "
    "four seconds; experimental evidence in human-computer interaction "
    "research shows that latency above this threshold materially degrades "
    "perceived response time and broader user-experience measures, with "
    "natural conversational fillers offsetting only part of the effect "
    "(Maslych et al., 2025). Second, voice naturalness shapes user "
    "perceptions of safety and compliance (Becker et al., 2025; Nussbaum "
    "et al., 2025). For these reasons, the voice infrastructure is not a "
    "cosmetic surface treatment but a service-design prerequisite: poor "
    "synthesis or high latency can undermine confidence in the agent even "
    "when the underlying answer is correct."
)

H3("6.3.4 Auditable human escalation")

P(
    "The fourth prerequisite is an auditable human-AI collaboration model. "
    "Routine communication is handled by the agent; regulated-step "
    "communication \u2014 disclosures under the Truth in Lending and Real "
    "Estate Settlement Procedures Acts, advice on terms requiring a "
    "licensed mortgage loan originator under the SAFE Act, and any "
    "interaction whose substance or framing is governed by the CFPB\u2019s "
    "UDAAP framework \u2014 is routed to a licensed loan consultant. The "
    "handoff is observable, logged, and auditable: each transition between "
    "the agent and the human is timestamped, attributed to an identifiable "
    "human staff member, and stored in the platform\u2019s case file. This "
    "design element discharges the regulatory clarity precondition by "
    "making the regulated boundary the natural human\u2013AI hand-off "
    "point rather than a contested edge."
)

# ---------------------------------------------------------------------------
# 6.4 Implementation stages
# ---------------------------------------------------------------------------

H2("6.4 Implementation Stages")

P(
    "The Better.com timeline supports a four-stage implementation sequence. "
    "Stage 1 is pilot deployment: the agent is introduced into a narrow, "
    "low-risk slice of the workflow. In the case, this slice was the "
    "post-decision update window beginning around the October 17, 2024 "
    "launch (Better Home & Finance Holding Company, 2024a). Stage 2 is "
    "coordination expansion: scheduling, mid-funnel status updates, and "
    "document follow-up are added as the agent\u2019s scope. Stage 3 is "
    "scaling and monitoring: call volume rises non-linearly while the "
    "human team reallocates capacity to complex and regulated cases. The "
    "Better\u2013ElevenLabs joint release reports approximately 100,000 "
    "Betsy-handled mortgage-related phone calls per month and approximately "
    "1.89 million inbound and outbound calls in 2025; these figures are "
    "vendor- and management-reported and are recorded as such in the "
    "source-reliability classification (\u00a73.7) (Better Home & Finance "
    "Holding Company & ElevenLabs, 2026). Stage 4 is performance "
    "measurement: the agent\u2019s contribution is evaluated through the "
    "multidimensional measurement scheme described in \u00a76.5 and "
    "summarised in the bottom panel of Figure 6.1. The transition between "
    "stages is governed by the same human-escalation model that operates "
    "within each stage \u2014 expanding the agent\u2019s task scope is "
    "itself a regulated-step decision."
)

# ---------------------------------------------------------------------------
# 6.5 Business value mechanisms
# ---------------------------------------------------------------------------

H2("6.5 Business-Value Mechanisms by Prerequisite")

P(
    "The four prerequisites generate value through different mechanisms. "
    "The process-aware operating platform creates value primarily through "
    "cost efficiency and labor productivity: structured workflow state "
    "permits automation of routine coordination, reduces "
    "exception-handling overhead, and shifts human capacity toward "
    "complex cases. In the Better.com case, this mechanism is consistent "
    "with the observed expense-ratio trajectory (4.79 \u2192 2.89 \u2192 "
    "2.01 between 2023 and 2025) and the revenue-per-employee trajectory "
    "($0.094M \u2192 $0.087M \u2192 $0.124M), although both trajectories "
    "remain incomplete relative to the 2021\u20132023 pre-period RPE "
    "average of $0.130M (Chapter 5, \u00a75.3.2 and \u00a75.3.4). The "
    "coordination-layer agent generates value through labor productivity "
    "and \u2014 ambiguously \u2014 through customer experience: routine "
    "coordination is handled at higher volume without proportional "
    "headcount, while customer-side perceptions of the resulting service "
    "are mediated by latency, voice naturalness, and the visibility of "
    "the agent."
)

P(
    "The voice-infrastructure layer affects customer experience directly. "
    "Speech-to-text, response-generation, and text-to-speech latency "
    "shape the per-turn experience; voice naturalness shapes perceptions "
    "of safety and compliance (Becker et al., 2025; Maslych et al., 2025). "
    "The Better.com NLP evidence in Chapter 5 is consistent with the "
    "proposition that, when the AI system operates as backend infrastructure "
    "rather than as a branded experience, customer-side AI attribution "
    "is low: explicit AI mentions in Trustpilot reviews remained at "
    "approximately 1.15 percent (pre) and 1.18 percent (post), and "
    "Cost/Rates discourse \u2014 the only keyword group whose prevalence "
    "shift survives the Bonferroni correction \u2014 shifted by \u221212.35 "
    "percentage points (Chapter 5, \u00a75.4.3). The auditable "
    "human-escalation prerequisite generates value through a different "
    "channel: it permits revenue conversion at the regulated boundary "
    "(where the agent legally cannot close) and trust at the customer "
    "boundary (where the borrower can request a human). It also produces "
    "regulatory-compliance value that is directly visible in the absence "
    "of UDAAP-level enforcement events but indirectly visible in Better\u2019s "
    "ongoing public-company status."
)

# ---------------------------------------------------------------------------
# 6.6 Boundary conditions
# ---------------------------------------------------------------------------

H2("6.6 Boundary Conditions")

P(
    "Five boundary conditions limit the design pattern. The first is "
    "regulated domain: the pattern is derived from a regulated workflow "
    "(U.S. mortgage origination) and is most plausibly applicable to "
    "other regulated, communication-intensive, high-volume workflows. In "
    "weakly regulated domains, the auditable human-escalation prerequisite "
    "loses much of its value; in heavily regulated domains with no clear "
    "boundary between routine and regulated communication, the "
    "coordination-layer agent scope cannot be defined. The second is data "
    "quality: the value of a process-aware operating platform depends on "
    "the structure and accuracy of the workflow data it exposes. Where "
    "workflow data is fragmented across legacy systems, the platform "
    "precondition cannot be satisfied without prior digital-transformation "
    "investment whose costs and timelines may exceed those of the agent "
    "itself."
)

P(
    "The third boundary condition is process standardization. The pattern "
    "fails for unstandardized processes whose state cannot be enumerated. "
    "The fourth is trust and transparency: the customer must be able to "
    "escalate the interaction to a human, and the platform must make the "
    "human\u2013AI boundary recognizable rather than opaque. The fifth is "
    "macroeconomic confounding: in the Better.com case, the operational-leverage "
    "signal in 2024 and 2025 is partially driven by the recovery of "
    "mortgage-market volume and by Better\u2019s NEO-channel restructuring "
    "(Better Home & Finance Holding Company, 2025a; Mortgage Bankers "
    "Association, 2024a). A parallel deployment in a neutral macroeconomic "
    "environment would be required to isolate the contribution of the "
    "voice agent itself, and Chapter 9 identifies this isolation as a "
    "priority for future research."
)

# ---------------------------------------------------------------------------
# 6.7 Transferability
# ---------------------------------------------------------------------------

H2("6.7 Transferability to Adjacent Regulated Settings")

P(
    "Two adjacent regulated settings illustrate the pattern\u2019s "
    "transferability without overreaching. The first is retail-banking "
    "servicing: high-volume coordination tasks (status updates, dispute "
    "initiation, document submission, scheduling) proceed inside a "
    "process-aware core-banking platform, with regulated steps (Reg E "
    "investigations, Reg Z disclosures, fraud-stop confirmations) routed "
    "to licensed staff. The voice agent\u2019s task scope, the latency "
    "constraint, and the auditable-escalation prerequisite carry across "
    "with minor adaptation; the data-accessibility precondition is the "
    "principal binding constraint, because core-banking systems are often "
    "less process-aware than Tinman. The second is insurance servicing: "
    "claim status, premium queries, and coverage updates can proceed inside "
    "a process-aware policy-administration platform, with claim-decisioning "
    "and material-misrepresentation steps routed to licensed adjusters or "
    "underwriters. Here the regulatory-clarity precondition is the "
    "principal constraint, because the legal definition of \u201cadvice\u201d "
    "in insurance servicing varies more across jurisdictions than under "
    "the U.S. SAFE Act."
)

P(
    "Beyond these two settings, the pattern\u2019s claim is bounded by the "
    "five conditions in \u00a76.6 and by the limitations articulated in "
    "Chapter 8. Transferability claims are therefore stated as working "
    "hypotheses for future research, not as established findings. In "
    "particular, the pattern\u2019s transferability to lower digital-maturity "
    "lenders \u2014 those without an analogue of Tinman \u2014 is "
    "explicitly weaker than its transferability across high-digital-maturity "
    "regulated workflows."
)

# ---------------------------------------------------------------------------
# 6.8 Summary
# ---------------------------------------------------------------------------

H2("6.8 Chapter Summary")

P(
    "Chapter 6 has formalised the four prerequisites identified in Chapter "
    "5 as a transferable design pattern: a process-aware operating "
    "platform; a coordination-layer agent scope; low-latency voice "
    "infrastructure; and an auditable human-AI collaboration model with "
    "licensed-consultant escalation at the regulated boundary. The "
    "pattern is offered in the design-science sense (Hevner et al., 2004) "
    "and bounded for analytic generalization (Yin, 2018) to other "
    "regulated, communication-intensive, high-volume financial workflows "
    "with mature digital operating platforms. The chapter has explicitly "
    "stated what the pattern is not: it is not a causal model and not a "
    "deployment recipe. The next chapter discusses how the empirical "
    "findings of Chapter 5 and the pattern formalised in Chapter 6 sit "
    "within \u2014 and contribute to \u2014 the literature reviewed in "
    "Chapter 2."
)


# ---------------------------------------------------------------------------
# Apply
# ---------------------------------------------------------------------------


def apply(doc):
    if has_marker(doc, "ch6_inserted"):
        print("[ch6_inserted] already present; skipping")
        return False
    _, anchor = find_paragraph_with_text(doc, "References")
    if anchor is None:
        raise RuntimeError("Could not find References anchor")

    is_first = True
    for kind, payload in CONTENT:
        if kind == "h1":
            p = insert_paragraph_before(anchor, "")
            p.style = doc.styles["Heading 1"]
            p.add_run(payload)
            if is_first:
                add_marker(p, "ch6_inserted")
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
        elif kind == "fig":
            path, caption = payload
            insert_picture_before(anchor, path, width_in=6.5)
            cap = insert_paragraph_before(anchor, "")
            try:
                cap.style = doc.styles["Caption"]
            except KeyError:
                pass
            run = cap.add_run(caption)
            run.bold = True
        elif kind == "caption":
            cap = insert_paragraph_before(anchor, "")
            try:
                cap.style = doc.styles["Caption"]
            except KeyError:
                pass
            cap.add_run(payload)
    print("[ch6_inserted] inserted")
    return True


def main():
    doc = open_draft()
    if apply(doc):
        save_draft(doc)
        print("Saved.")


if __name__ == "__main__":
    main()
