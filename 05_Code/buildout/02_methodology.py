"""
02_methodology.py
=================

Apply Chapter 3 (Methodology) build-out tasks from the prior improvement
report:

* **A1** delete the duplicate 6\u00d74 Operationalization Table and insert
  a new "Source Reliability and Data Provenance" H2 subsection with the
  proper tier table (Table 3.2).
* **A2** add a reproducibility paragraph and an Appendix B / C pointer
  (after the existing reproducibility paragraph).
* **A12** consolidate methodological risks into a single tabular subsection.
* Add an abductive-logic short paragraph after the pragmatism paragraph.
* Add Trustpilot data-source justification in \u00a73.5 (Data Collection).
* Add CTO proxy and OLI disclaimer to \u00a73.6 (Operationalization).
* Caption the surviving 6\u00d74 table as "Table 3.1 \u2014 Operationalization
  of Business Value Dimensions".

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
    list_tables_in_doc,
    delete_table,
)


# ---------------------------------------------------------------------------
# Source Reliability / Data Provenance Table (Table 3.2)
# ---------------------------------------------------------------------------

T32_HEADERS = [
    "Tier",
    "Source type",
    "Examples in this thesis",
    "Audit / verification basis",
    "Required wording in body",
]

T32_ROWS = [
    [
        "High",
        "SEC 10-K, 10-Q, S-1 (audited financial statements)",
        "Better Home & Finance Holding Company (2025a, 2026); Rocket Companies (2024, 2025); financial dataset constructed from these filings.",
        "Externally audited financial statements; deterministic ratio calculations from audited inputs.",
        "Default; cite without caveat.",
    ],
    [
        "High",
        "SEC 8-K Exhibit 99.1 / earnings release",
        "Better (2024a Betsy launch press release; 2025b Q1 release; 2025c Q2 release).",
        "SEC-filed; subject to materiality and disclosure obligations.",
        "Default; cite without caveat.",
    ],
    [
        "Medium-High",
        "Industry report from independent body",
        "Mortgage Bankers Association (2024a, 2024b); Freddie Mac PMMS; Federal Reserve Bank of New York Household Debt and Credit Report.",
        "Recognized industry reporting standards; cross-verifiable across editions.",
        "Treat as industry context.",
    ],
    [
        "Medium-High",
        "Government regulatory page",
        "Consumer Financial Protection Bureau (n.d.); Fannie Mae Selling Guide.",
        "Government-published; updated periodically.",
        "Default; cite without caveat.",
    ],
    [
        "Medium",
        "Management-reported operating metric (unaudited)",
        "NPS 39 \u2192 64; \u201capproximately 100,000 mortgage-related phone calls per month\u201d; \u201c1.89 million inbound and outbound calls in 2025\u201d.",
        "Management disclosure; not externally audited.",
        "Always introduce with: \u201cBetter has reported that \u2026\u201d; never present as audited fact.",
    ],
    [
        "Medium",
        "Vendor / case-study material",
        "ElevenLabs blog; Better\u2013ElevenLabs joint release (2026).",
        "Vendor-published; commercial-marketing motivation.",
        "Always introduce with: \u201cVendor materials report \u2026\u201d; never present as evidence of magnitude on business outcomes.",
    ],
    [
        "Medium",
        "Independent self-selected user-generated content (UGC)",
        "Trustpilot reviews (1,915 cleaned).",
        "Verified-review platform; subject to self-selection.",
        "Always present with the n_pre / n_post imbalance and self-selection caveat.",
    ],
    [
        "High",
        "Peer-reviewed academic publication",
        "Adam, Wessel, & Benlian (2021); Andrade & Tumelero (2022); Aggarwal et al. (2025); Becker et al. (2025); Brynjolfsson et al. (2023); Goodhue & Thompson (1995); Heskett et al. (1994); Huang & Rust (2018); Maslych et al. (2025); Mogaji & Nguyen (2021); Nussbaum et al. (2025); Wang et al. (2023); Yin (2018); Zhang et al. (2023).",
        "Peer review.",
        "Default; cite without caveat.",
    ],
    [
        "Medium-Low",
        "News media (HousingWire, Axios, BusinessWire republishing press releases)",
        "Used only for triangulating timing.",
        "Editorial standards; not peer-reviewed.",
        "Use only for triangulation of timing, not for evidence of magnitude.",
    ],
    [
        "Low",
        "Trade-press / vendor blog",
        "Various AI-vendor blogs.",
        "Promotional; no QA.",
        "Avoid; use only when no higher-tier source covers the same point.",
    ],
]


# ---------------------------------------------------------------------------
# Methodological Risks consolidated table (\u00a73.10)
# ---------------------------------------------------------------------------

RISKS_HEADERS = [
    "#",
    "Risk",
    "Where surfaced in this thesis",
    "Mitigation",
]

RISKS_ROWS = [
    [
        "1",
        "No causal identification",
        "\u00a73.7 (Source Reliability), \u00a75.6, \u00a78.2.",
        "Adopt \u201cconsistent with\u201d / \u201cassociated with\u201d wording throughout; restrict claims to descriptive interpretation supported by triangulated case evidence.",
    ],
    [
        "2",
        "Annual financial granularity",
        "\u00a73.5 (SEC Filings), \u00a75.6, \u00a78.3.",
        "Treat 2024 as a transition year combining pre- and post-Betsy quarters; flag explicitly when interpreting 2024 figures.",
    ],
    [
        "3",
        "Single-vendor (ElevenLabs) source bias",
        "\u00a74.4 (ElevenLabs as Voice Infrastructure), \u00a75.6.",
        "Triangulate vendor-reported figures with Better\u2019s 10-K disclosures and the SEC-filed 8-K press releases; flag vendor evidence inline (\u201cVendor materials report \u2026\u201d).",
    ],
    [
        "4",
        "Trustpilot self-selection and pre/post imbalance (n=1,746 / 169)",
        "\u00a73.5 (Trustpilot Customer Reviews), \u00a75.4.5, \u00a78.7.",
        "Apply the seven-reason caveat from \u00a75.4 to every NPS-vs-Trustpilot comparison; require triangulation across the two instrument types.",
    ],
    [
        "5",
        "Topic-share figures sensitive to BERTopic hyperparameters",
        "\u00a73.6 (NLP Text Mining), \u00a75.4.4, \u00a78.8.",
        "Document hyperparameters in Appendix C; describe topic-share results as descriptive, not inferential.",
    ],
    [
        "6",
        "Rocket comparability bounded by accounting and scale differences",
        "\u00a73.4 (Case Selection), \u00a75.3.5, \u00a78.9.",
        "Treat Rocket as a directional industry benchmark, not a counterfactual; isolate audited expense and revenue lines for comparison.",
    ],
    [
        "7",
        "Better-specific digital maturity may bound generalizability",
        "\u00a74 (Tinman platform), \u00a75.2.5, \u00a76, \u00a78.4.",
        "Use analytic generalization to similar configurations only (Yin, 2018); state the four-prerequisite design pattern as a transferability hypothesis, not a confirmed cross-case finding.",
    ],
]


# ---------------------------------------------------------------------------
# Helper: caption-styled paragraph
# ---------------------------------------------------------------------------


def _add_caption_before(anchor, text, marker):
    p = insert_paragraph_before(anchor, "")
    try:
        p.style = anchor.part.document.styles["Caption"]
    except KeyError:
        pass
    run = p.add_run(text)
    run.bold = True
    add_marker(p, marker)
    return p


# ---------------------------------------------------------------------------
# Operations
# ---------------------------------------------------------------------------


def remove_duplicate_table(doc):
    """Remove the 2nd copy of the 6\u00d74 Operationalization table."""
    if has_marker(doc, "method_dup_table_removed"):
        print("[method_dup_table_removed] already done; skipping")
        return False
    tables = doc.tables
    if len(tables) < 2:
        print("[method_dup_table_removed] no duplicate found; skipping")
        return False
    # Identify the two 6x4 tables whose first cell starts with
    # "Business value dimension"
    candidates = []
    for ti, t in enumerate(tables):
        if len(t.rows) >= 1 and len(t.rows[0].cells) >= 4:
            head0 = t.rows[0].cells[0].text.strip().lower()
            if "business value" in head0:
                candidates.append(ti)
    if len(candidates) < 2:
        print(f"[method_dup_table_removed] only {len(candidates)} 6x4 found; skipping")
        return False
    # Delete the SECOND candidate
    second_idx = candidates[1]
    delete_table(tables[second_idx])
    # Add an idempotency marker. Use the Operationalization heading anchor.
    _, op_heading = find_paragraph_with_text(doc, "Operationalization of Business Value")
    if op_heading is not None:
        add_marker(op_heading, "method_dup_table_removed")
    print("[method_dup_table_removed] removed duplicate Operationalization table")
    return True


def add_table_3_1_caption(doc):
    """Add a Table 3.1 caption immediately after the Operationalization
    paragraph (which precedes the surviving table)."""
    if has_marker(doc, "method_table_3_1_caption"):
        return False
    _, op_heading = find_paragraph_with_text(doc, "Operationalization of Business Value")
    if op_heading is None:
        raise RuntimeError("Operationalization heading not found")

    # The next normal paragraph is P0146 (the prose). Insert the caption
    # AFTER that paragraph but BEFORE the surviving table (which currently
    # follows immediately).
    para_idx = next(
        (i for i, p in enumerate(doc.paragraphs)
         if p._p is op_heading._p), None)
    if para_idx is None:
        raise RuntimeError("Could not locate operationalization heading index")
    # The prose paragraph is at para_idx + 1
    prose = doc.paragraphs[para_idx + 1]
    cap = insert_paragraph_after(prose, "")
    try:
        cap.style = doc.styles["Caption"]
    except KeyError:
        pass
    run = cap.add_run(
        "Table 3.1. Operationalization of Business Value Dimensions across "
        "Operational Efficiency, Productivity, Customer Experience, and "
        "Financial Performance."
    )
    run.bold = True
    add_marker(cap, "method_table_3_1_caption")
    print("[method_table_3_1_caption] added")
    return True


def insert_source_reliability_subsection(doc):
    """Insert §3.7 'Source Reliability and Data Provenance' subsection
    immediately before the existing 'Triangulation Logic' H2."""
    if has_marker(doc, "method_source_reliability"):
        print("[method_source_reliability] already present; skipping")
        return False
    _, anchor = find_paragraph_with_text(doc, "Triangulation Logic")
    if anchor is None:
        raise RuntimeError("Triangulation Logic heading not found")

    # Heading
    h2 = insert_paragraph_before(anchor, "")
    h2.style = doc.styles["Heading 2"]
    h2.add_run("Source Reliability and Data Provenance")
    add_marker(h2, "method_source_reliability")

    intro_paras = [
        "Because the empirical strategy of this thesis combines audited "
        "financial statements, management-reported operating metrics, "
        "vendor case-study materials, government and industry reports, "
        "self-selected customer reviews, and peer-reviewed academic "
        "literature, a single-tier treatment of evidence would obscure the "
        "asymmetry of reliability across these sources. To make this "
        "asymmetry explicit, the thesis adopts a four-tier source-reliability "
        "hierarchy that classifies every empirical anchor used in Chapters 4 "
        "and 5 against an audit or verification basis and prescribes a "
        "minimum wording requirement when the source is invoked in the body.",

        "The hierarchy is presented in Table 3.2. Audited 10-K and 10-Q "
        "financial statements (and the deterministic ratio calculations "
        "derived from them) are treated as the baseline of high-reliability "
        "evidence. SEC-filed press releases and earnings releases are also "
        "treated as high-reliability for descriptive facts (timing, "
        "headcount, capital structure) but not for forward-looking or "
        "performance-implying claims, which are flagged as "
        "management-reported. Independent industry reports (Mortgage Bankers "
        "Association, Freddie Mac, Federal Reserve Bank of New York) and "
        "government regulatory pages (CFPB, Fannie Mae) are classified as "
        "medium-high context evidence. Vendor materials\u2014including the "
        "ElevenLabs blog and the joint Better\u2013ElevenLabs press "
        "release\u2014are classified as medium reliability and are required "
        "to be introduced with a vendor flag (\u201cVendor materials report "
        "\u2026\u201d). Trustpilot reviews are treated as independent but "
        "self-selected user-generated content and are required to be "
        "presented with the n_pre / n_post imbalance and the self-selection "
        "caveat. Peer-reviewed academic publications are classified as high "
        "reliability for the constructs and propositions they support. News "
        "media that republish press releases without independent reporting "
        "are used only to triangulate timing, never to establish magnitude. "
        "Trade-press and vendor blog posts are avoided unless no "
        "higher-tier source covers the same point.",

        "This hierarchy is operationalized in two ways. First, every "
        "empirical claim in Chapters 4 and 5 is matched against the "
        "wording requirements in Table 3.2 (e.g., management-reported "
        "operating metrics are introduced with \u201cBetter has reported "
        "that \u2026\u201d; vendor metrics are introduced with \u201cVendor "
        "materials report \u2026\u201d). Second, where two sources at "
        "different tiers cover the same magnitude, the lower-tier source is "
        "used for triangulation of timing and direction only and is not "
        "permitted to override the higher-tier source on the magnitude. "
        "Appendix D records the per-source reliability classification used in "
        "this thesis.",
    ]
    for ptext in intro_paras:
        p = insert_paragraph_before(anchor, "")
        p.style = doc.styles["Normal"]
        p.add_run(ptext)

    # Table 3.2 caption
    cap = insert_paragraph_before(anchor, "")
    try:
        cap.style = doc.styles["Caption"]
    except KeyError:
        pass
    cap_run = cap.add_run(
        "Table 3.2. Source Reliability and Data Provenance Hierarchy used to "
        "evaluate empirical evidence in Chapters 4 and 5."
    )
    cap_run.bold = True

    # Table 3.2 itself
    n_rows = 1 + len(T32_ROWS)
    n_cols = len(T32_HEADERS)
    tbl = insert_table_before(anchor, n_rows, n_cols, style_name="Table Grid")
    for c, h in enumerate(T32_HEADERS):
        set_table_cell(tbl.rows[0].cells[c], h, bold=True)
    for r, row in enumerate(T32_ROWS, start=1):
        for c, value in enumerate(row):
            set_table_cell(tbl.rows[r].cells[c], value)

    # Closing pointer
    p = insert_paragraph_before(anchor, "")
    p.style = doc.styles["Normal"]
    p.add_run(
        "The four-tier hierarchy is referenced again in \u00a75.4.1 (NPS as "
        "medium-reliability evidence), \u00a75.4.5 (Trustpilot self-selection "
        "boundaries), \u00a75.6 (interpretive boundaries), and Appendix D "
        "(per-source classification)."
    )

    print("[method_source_reliability] inserted")
    return True


def add_abductive_logic_paragraph(doc):
    """Insert one paragraph after the Pragmatism narrative explaining
    the abductive inference logic."""
    if has_marker(doc, "method_abductive"):
        return False
    # Anchor: paragraph that begins with "Pragmatism bypasses this dichotomy"
    _, anchor = find_paragraph_with_text(doc, "Pragmatism bypasses this dichotomy")
    if anchor is None:
        # fallback to general pragmatism paragraph
        _, anchor = find_paragraph_with_text(doc, "philosophical paradigm of Pragmatism")
    if anchor is None:
        raise RuntimeError("Pragmatism anchor not found")
    p = insert_paragraph_after(anchor, "")
    p.style = doc.styles["Normal"]
    p.add_run(
        "Within this pragmatist orientation, the inference logic is explicitly "
        "abductive rather than purely deductive or inductive. Financial "
        "trajectory and customer-discourse signals are read as observations to "
        "be reconciled with the most plausible explanation given the "
        "case-study evidence on integration mechanism, rather than as "
        "deductive tests of a pre-specified causal hypothesis. This abductive "
        "stance is consistent with critical-case study research in "
        "information systems (Yin, 2018) and matches the convergent parallel "
        "mixed-methods design described in the next section."
    )
    add_marker(p, "method_abductive")
    print("[method_abductive] inserted")
    return True


def add_trustpilot_justification(doc):
    """Add ~3 sentences justifying Trustpilot as a data source."""
    if has_marker(doc, "method_trustpilot_justification"):
        return False
    _, anchor = find_paragraph_with_text(doc, "Trustpilot Customer Reviews")
    if anchor is None:
        raise RuntimeError("Trustpilot heading not found")
    # Find the immediately following normal paragraph; we insert
    # justification AFTER it so the existing paragraph still leads.
    para_idx = next(
        (i for i, p in enumerate(doc.paragraphs)
         if p._p is anchor._p), None)
    if para_idx is None:
        raise RuntimeError("Could not locate Trustpilot heading index")
    target = doc.paragraphs[para_idx + 1]
    p = insert_paragraph_after(target, "")
    p.style = doc.styles["Normal"]
    p.add_run(
        "Trustpilot is selected over Google reviews and Yelp for three "
        "reasons. First, Trustpilot operates a verified-purchase model with "
        "domain-level authentication and an internal review-flagging system "
        "that materially reduces (although does not eliminate) the share of "
        "fraudulent or paid reviews relative to general-purpose review "
        "platforms (Filieri, 2015; Luca, 2016). Second, Trustpilot is the "
        "platform on which Better.com has the largest publicly available "
        "review corpus during the 2020\u20132026 observation window, "
        "providing both pre-period density and a non-trivial post-period "
        "sample. Third, the Trustpilot API and review-page schema are "
        "stable across the observation window, which simplifies "
        "reproducibility: the corpus used in this thesis was extracted on a "
        "single date using the Apify Trustpilot Review Scraper "
        "(Actor ID l3wcDhSSC96LBRUpc) and is archived as a static dataset "
        "in the project repository. The self-selection bias inherent to any "
        "review platform is acknowledged explicitly here and reiterated "
        "as a limitation in \u00a73.10 and \u00a78.7."
    )
    add_marker(p, "method_trustpilot_justification")
    print("[method_trustpilot_justification] inserted")
    return True


def add_cto_oli_disclaimer(doc):
    """Append a CTO + OLI disclaimer to the Operationalization paragraph."""
    if has_marker(doc, "method_cto_oli"):
        return False
    _, anchor = find_paragraph_with_text(doc, "Operationalization of Business Value")
    if anchor is None:
        raise RuntimeError("Operationalization heading not found")
    para_idx = next(
        (i for i, p in enumerate(doc.paragraphs)
         if p._p is anchor._p), None)
    target = doc.paragraphs[para_idx + 1]  # the prose paragraph
    p = insert_paragraph_after(target, "")
    p.style = doc.styles["Normal"]
    p.add_run(
        "Two operationalization choices warrant explicit disclosure. First, "
        "Cost-to-Originate (CTO) is computed in this thesis as Total "
        "Expenses divided by Funded Loans as a proxy for Better\u2019s "
        "reported per-loan cost; CTO so defined is not an audited Better "
        "disclosure but an author-constructed proxy, and the Mortgage "
        "Bankers Association Quarterly Performance Report is used as the "
        "third-party benchmark for industry CTO. Second, the Operational "
        "Leverage Index reported in \u00a75.3.4 and Appendix B is an "
        "author-constructed equally-weighted composite of a Revenue Growth "
        "Index, a Revenue per Employee Index, and an Inverse Expense Ratio "
        "Index, with 2023 = 100. The composite is sensitive to baseline-year "
        "selection and weighting; it is therefore retained as a compact "
        "visualization of operational leverage, not as primary evidence."
    )
    add_marker(p, "method_cto_oli")
    print("[method_cto_oli] inserted")
    return True


def add_methodological_risks_subsection(doc):
    """Insert a consolidated 'Methodological Risks' subsection (§3.10)
    after Methodological Limitations, before Research Rigor.

    This complements the existing prose-form Methodological Limitations
    by adding a tabular bird's-eye view of the seven core risks.
    """
    if has_marker(doc, "method_risks_consolidated"):
        return False
    _, anchor = find_paragraph_with_text(doc, "Research Rigor and Reproducibility")
    if anchor is None:
        raise RuntimeError("Research Rigor heading not found")

    h2 = insert_paragraph_before(anchor, "")
    h2.style = doc.styles["Heading 2"]
    h2.add_run("Methodological Risks: Consolidated View")
    add_marker(h2, "method_risks_consolidated")

    intro = insert_paragraph_before(anchor, "")
    intro.style = doc.styles["Normal"]
    intro.add_run(
        "The methodological limitations enumerated above are interrelated. "
        "Table 3.3 consolidates them into a single examiner-visible view, "
        "labelling each risk with its current location in the thesis and the "
        "specific mitigation adopted. The same risks are revisited in "
        "Chapter 8."
    )

    cap = insert_paragraph_before(anchor, "")
    try:
        cap.style = doc.styles["Caption"]
    except KeyError:
        pass
    cap_run = cap.add_run(
        "Table 3.3. Consolidated view of the seven principal methodological "
        "risks of this thesis, with mitigation actions."
    )
    cap_run.bold = True

    n_rows = 1 + len(RISKS_ROWS)
    n_cols = len(RISKS_HEADERS)
    tbl = insert_table_before(anchor, n_rows, n_cols, style_name="Table Grid")
    for c, h in enumerate(RISKS_HEADERS):
        set_table_cell(tbl.rows[0].cells[c], h, bold=True)
    for r, row in enumerate(RISKS_ROWS, start=1):
        for c, value in enumerate(row):
            set_table_cell(tbl.rows[r].cells[c], value)

    closing = insert_paragraph_before(anchor, "")
    closing.style = doc.styles["Normal"]
    closing.add_run(
        "The mitigation column anticipates the consolidated limitations "
        "chapter (Chapter 8); each row in Table 3.3 is mapped to a "
        "subsection there."
    )

    print("[method_risks_consolidated] inserted")
    return True


def add_reproducibility_appendix_pointer(doc):
    """Add a pointer to Appendices B and C immediately after the existing
    reproducibility paragraph."""
    if has_marker(doc, "method_repro_pointer"):
        return False
    _, anchor = find_paragraph_with_text(doc, "Computational reliability and reproducibility")
    if anchor is None:
        return False
    p = insert_paragraph_after(anchor, "")
    p.style = doc.styles["Normal"]
    p.add_run(
        "All quantitative analyses in this thesis are reproducible from the "
        "raw source data and the public source-code repository. Package "
        "versions used in the financial and NLP pipelines are listed in "
        "08_Code/requirements.txt and reproduced in Appendix B; BERTopic "
        "hyperparameters (UMAP n_neighbors = 10, n_components = 5, "
        "min_dist = 0.0, cosine; HDBSCAN min_cluster_size = 10, "
        "min_samples = 3, EOM cluster selection; random_state = 42) and "
        "the c-TF-IDF topic-labelling configuration are listed in Appendix "
        "C, together with the Welch\u2019s t, chi-square / Fisher exact, "
        "and Bonferroni-correction parameters used for the keyword-prevalence "
        "and sentiment tests in \u00a75.4."
    )
    add_marker(p, "method_repro_pointer")
    print("[method_repro_pointer] inserted")
    return True


def main():
    doc = open_draft()
    changed = False
    changed |= remove_duplicate_table(doc)
    changed |= add_table_3_1_caption(doc)
    changed |= insert_source_reliability_subsection(doc)
    changed |= add_abductive_logic_paragraph(doc)
    changed |= add_trustpilot_justification(doc)
    changed |= add_cto_oli_disclaimer(doc)
    changed |= add_methodological_risks_subsection(doc)
    changed |= add_reproducibility_appendix_pointer(doc)
    if changed:
        save_draft(doc)
        print("Saved updated draft.")
    else:
        print("No changes.")


if __name__ == "__main__":
    main()
