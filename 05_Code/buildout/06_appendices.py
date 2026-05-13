"""
06_appendices.py
================

Insert the Appendix block (A through G) at the end of the thesis.

Modern professional structure adopted from research-paper appendix
conventions: each appendix has a single H1 title (\u201cAppendix X \u2014
title\u201d), enumerated H2 sub-sections, and supporting tables/figures.

Idempotent.
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, ".")
from _helpers import (  # noqa: E402
    open_draft,
    save_draft,
    insert_paragraph_before,
    insert_paragraph_at_end,
    insert_picture_at_end,
    insert_table_at_end,
    has_marker,
    add_marker,
    set_table_cell,
    FIG_FIN,
    FIG_NLP,
    FIG_DESIGN,
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


CONTENT = []  # ordered list of (kind, payload)


def H1(t): CONTENT.append(("h1", t))


def H2(t): CONTENT.append(("h2", t))


def H3(t): CONTENT.append(("h3", t))


def P(t): CONTENT.append(("p", t))


def CAP(t): CONTENT.append(("caption", t))


def TBL(headers, rows, caption=None):
    if caption:
        CONTENT.append(("caption", caption))
    CONTENT.append(("table", (headers, rows)))


def FIG(path, caption):
    CONTENT.append(("figure", (path, caption)))


# ===========================================================================
# Appendix A \u2014 Financial Dataset and Metric Definitions
# ===========================================================================

H1("Appendix A. Financial Dataset and Metric Definitions")

H2("A.1 Dataset Overview")

P(
    "The financial dataset analysed in Chapter 5 contains thirteen annual "
    "observations spanning fiscal years 2020\u20132025: five for Better "
    "Home & Finance Holding Company (formerly Better HoldCo, Inc.) and "
    "six for Rocket Companies, Inc., used as a directional industry "
    "benchmark. Each observation was extracted from a single SEC filing "
    "(10-K, S-1, or S-1/A) and stored as a single row in a normalised "
    "long-format table indexed by company\u2009\u00d7\u2009fiscal year. The "
    "dataset is reproducible from the public source-code repository: the "
    "raw filings are stored in 02_Raw_Data/, the extraction scripts under "
    "08_Code/financial_extract*.py, and the normalised CSV under "
    "08_Code/financial_dataset.csv."
)

H2("A.2 Variable Definitions")

TBL(
    ["#", "Variable", "Definition", "Unit", "Computed from"],
    [
        ["1", "Revenue", "Total net revenue from mortgage and related operations.", "USD millions",
         "10-K Consolidated Statements of Operations \u2014 \u201cTotal net revenues\u201d line."],
        ["2", "Total Expenses", "Sum of all operating expenses including compensation and benefits, marketing, technology, general and administrative, and other expenses.",
         "USD millions",
         "10-K Consolidated Statements of Operations \u2014 \u201cTotal expenses\u201d line."],
        ["3", "Net Loss / Net Income", "Bottom-line profit or loss after taxes and non-operating items.", "USD millions",
         "10-K Consolidated Statements of Operations."],
        ["4", "Headcount (year-end)", "Total full-time-equivalent employees at fiscal year-end.", "Persons",
         "10-K Item 1 (Business) \u2014 \u201cHuman Capital\u201d disclosure."],
        ["5", "Funded Loans", "Total dollar value of mortgage loans funded during the fiscal year.",
         "USD millions",
         "10-K Item 7 (MD&A) \u2014 \u201cKey performance indicators\u201d."],
        ["6", "Expense Ratio", "Total Expenses \u00f7 Revenue.", "Ratio (\u00d7)",
         "Computed: row 2 \u00f7 row 1."],
        ["7", "Revenue per Employee (RPE)", "Revenue \u00f7 Headcount.", "USD millions / employee",
         "Computed: row 1 \u00f7 row 4."],
        ["8", "Cost-to-Originate (proxy)", "Total Expenses \u00f7 Funded Loans (author-constructed proxy).",
         "USD per $ of funded loans", "Computed: row 2 \u00f7 row 5."],
        ["9", "Operational Leverage Index (OLI)",
         "Equally-weighted composite of Revenue Growth Index, RPE Index, and Inverse Expense Ratio Index, with 2023 = 100.",
         "Index (2023 = 100)",
         "Computed in 08_Code/financial_metrics_project.ipynb."],
    ],
    caption="Table A.1. Variable definitions for the audited financial dataset used in Chapter 5.",
)

H2("A.3 Annual Observations")

TBL(
    ["Company", "FY", "Revenue (USDm)", "Total Expenses (USDm)", "Net Loss (USDm)",
     "Headcount", "Expense Ratio", "RPE (USDm)"],
    [
        ["Better.com", "2020", "874.9", "807.0", "+172.5", "n/a", "0.92", "n/a"],
        ["Better.com", "2021", "858.9", "1,406.5", "\u2212302.4", "9,170", "1.64", "0.094"],
        ["Better.com", "2022", "383.4", "1,266.8", "\u2212876.4", "950", "3.30", "0.404"],
        ["Better.com", "2023", "76.8", "368.1", "\u2212536.4", "819", "4.79", "0.094"],
        ["Better.com", "2024", "108.5", "313.9", "\u2212206.3", "1,242", "2.89", "0.087"],
        ["Better.com", "2025", "164.9", "330.7", "\u2212165.9", "1,335", "2.01", "0.124"],
        ["Rocket Companies", "2023", "4,032.9", "4,160.4", "+13.7", "13,800", "1.03", "0.292"],
        ["Rocket Companies", "2024", "5,096.4", "4,798.5", "+30.4", "13,500", "0.94", "0.378"],
    ],
    caption=(
        "Table A.2. Audited annual observations for Better Home & Finance "
        "Holding Company (formerly Better HoldCo, Inc.) and Rocket "
        "Companies, Inc. Sources: Better Home & Finance Holding Company "
        "(2024b, 2025a, 2026); Rocket Companies (2024, 2025); Better "
        "HoldCo, Inc. (2023). All figures rounded to the disclosed precision "
        "in the underlying 10-K filings."
    ),
)

H2("A.4 Calculation Methodology")

P(
    "All ratios in Table A.2 are computed deterministically from the "
    "audited line items in the 10-K filings; no judgement-based "
    "adjustments are applied. Where the 10-K reports headcount as a range "
    "or an approximation, the lower bound is taken (this convention is "
    "documented in 08_Code/financial_metrics_project.ipynb). Net loss is "
    "reported with a leading minus sign; net income is reported with a "
    "leading plus sign. The Operational Leverage Index is computed in "
    "Appendix E and is treated in this thesis as an illustrative composite "
    "rather than as a primary inferential anchor (see \u00a73.6, OLI "
    "disclaimer)."
)


# ===========================================================================
# Appendix B \u2014 SEC Filing Provenance
# ===========================================================================

H1("Appendix B. SEC Filing Provenance")

H2("B.1 Filings List")

TBL(
    ["#", "Filer", "Form", "Filed", "Reporting period", "Accession / URL anchor"],
    [
        ["1", "Better HoldCo, Inc.", "S-1/A",
         "2023-12-20", "FY 2020\u20132022 (audited)",
         "SEC EDGAR (filer CIK 0001870348)."],
        ["2", "Better Home & Finance Holding Company", "10-K",
         "2024-03-29", "FY 2023",
         "SEC EDGAR (filer CIK 0001835416)."],
        ["3", "Better Home & Finance Holding Company", "10-Q",
         "2024-11-12", "Q3 2024",
         "SEC EDGAR (filer CIK 0001835416)."],
        ["4", "Better Home & Finance Holding Company", "8-K (Ex 99.1)",
         "2024-10-17", "Betsy launch press release",
         "SEC EDGAR (filer CIK 0001835416)."],
        ["5", "Better Home & Finance Holding Company", "10-K",
         "2025-03-18", "FY 2024",
         "SEC EDGAR (filer CIK 0001835416)."],
        ["6", "Better Home & Finance Holding Company", "8-K (Ex 99.1)",
         "2025-05-13", "Q1 2025 release",
         "SEC EDGAR (filer CIK 0001835416)."],
        ["7", "Better Home & Finance Holding Company", "8-K (Ex 99.1)",
         "2025-08-07", "Q2 2025 release",
         "SEC EDGAR (filer CIK 0001835416)."],
        ["8", "Better Home & Finance Holding Company", "10-K",
         "2026-03 (filed Q1 2026)", "FY 2025",
         "SEC EDGAR (filer CIK 0001835416)."],
        ["9", "Rocket Companies, Inc.", "10-K",
         "2024-02-29", "FY 2023",
         "SEC EDGAR (filer CIK 0001805284)."],
        ["10", "Rocket Companies, Inc.", "10-K",
         "2025-02-26", "FY 2024",
         "SEC EDGAR (filer CIK 0001805284)."],
    ],
    caption=(
        "Table B.1. SEC filings used for the financial-trajectory analysis "
        "in Chapter 5. Accession numbers and full URLs are recorded in "
        "08_Code/sec_filings_provenance.csv."
    ),
)

H2("B.2 Extraction Methodology")

P(
    "Each filing PDF was downloaded from SEC EDGAR to 02_Raw_Data/ and "
    "text-extracted using the Python libraries pdfplumber (script: "
    "08_Code/extract_pdf_texts.py) and pypdf (script: "
    "08_Code/parse_filings.py). For each filing, the relevant Statements "
    "of Operations and Item-1 Human-Capital pages were located by "
    "regex-anchored navigation (e.g., r\"Total\\s+net\\s+revenues\", "
    "r\"Human\\s+Capital\"). The extracted line items were entered into "
    "a normalised long-format CSV (08_Code/financial_dataset.csv) with "
    "columns (filer, fiscal_year, item, value, source_filing). Where a "
    "10-K disclosed restated prior-year figures, the most recent "
    "restatement was used and the prior figure was retained in a separate "
    "audit log (08_Code/restatements.csv)."
)

H2("B.3 Validation and Cross-Checks")

P(
    "Three validation checks were applied. First, every numeric line item "
    "extracted by pdfplumber was re-extracted by pypdf, and disagreements "
    "were flagged for manual review. Second, the computed expense ratios "
    "were cross-checked against the management-reported \u201ckey "
    "performance indicators\u201d disclosure in each 10-K Item 7 (MD&A) "
    "where available. Third, the headcount-based revenue-per-employee "
    "values were cross-checked against the press-release figures cited in "
    "the corresponding earnings 8-K. All disagreements within rounding "
    "tolerance were resolved in favour of the 10-K Statements of "
    "Operations."
)


# ===========================================================================
# Appendix C \u2014 NLP Pipeline
# ===========================================================================

H1("Appendix C. NLP Cleaning and Modelling Pipeline")

H2("C.1 Trustpilot Extraction")

P(
    "The Trustpilot review corpus was extracted on a single date (May 6, "
    "2026) using the Apify Trustpilot Review Scraper (Actor ID "
    "l3wcDhSSC96LBRUpc), targeting the better.com domain. The raw "
    "extraction returned 1,934 reviews spanning the period 2020\u201305 to "
    "2026\u201305. The raw extraction is archived as "
    "02_Raw_Data/trustpilot_better_com_raw.json."
)

H2("C.2 Cleaning Pipeline")

P(
    "Cleaning steps applied in 08_Code/nlp_project.ipynb: (i) removal of "
    "exact-duplicate review text (n = 6 dropped); (ii) removal of empty "
    "or single-character review text (n = 4 dropped); (iii) removal of "
    "reviews authored by accounts associated with Better-controlled "
    "domains as inferred from the reviewer-profile metadata (n = 9 "
    "dropped); (iv) language detection via langdetect with English-only "
    "retention (n = 0 dropped). The cleaned corpus contains 1,915 "
    "reviews. The pre/post split is anchored to the Betsy launch date "
    "(October 17, 2024): 1,746 reviews pre-Betsy, 169 reviews post-Betsy."
)

H2("C.3 VADER Configuration")

P(
    "VADER sentiment scoring was applied using nltk.sentiment.vader "
    "(VADER v3.3.2). The compound score is the normalised, weighted "
    "composite valence used as the primary sentiment signal. No domain "
    "lexicon adaptation was applied; all four VADER scores (compound, "
    "positive, negative, neutral) are recorded in the per-review output."
)

H2("C.4 BERTopic Hyperparameters")

P(
    "BERTopic was applied using the configuration documented in "
    "08_Code/nlp_project.ipynb: (i) embedding model "
    "all-MiniLM-L6-v2 (Hugging Face); (ii) UMAP dimensionality reduction "
    "with n_neighbors = 10, n_components = 5, min_dist = 0.0, metric = "
    "\u201ccosine\u201d; (iii) HDBSCAN density-based clustering with "
    "min_cluster_size = 10, min_samples = 3, cluster_selection_method = "
    "\u201ceom\u201d; (iv) c-TF-IDF topic representation with the default "
    "ClassTfidfTransformer; (v) random_state = 42 for reproducibility. The "
    "fitted model returned 44 topics; 1,198 reviews (66.4 percent of the "
    "cleaned corpus) were clustered to a non-noise topic and 606 reviews "
    "were classified as noise (topic = \u22121). Topic-share figures are "
    "treated as descriptive and not as inferential evidence (see "
    "\u00a73.10, Risk 5)."
)

H2("C.5 Statistical Test Parameters")

P(
    "Sentiment and rating differences between the pre-Betsy and "
    "post-Betsy periods were tested using Welch\u2019s t-test (two-sided), "
    "with Cohen\u2019s d as the effect-size measure. Keyword-prevalence "
    "differences were tested using two-sided chi-square tests with the "
    "Yates correction; where any expected cell count fell below 5, "
    "Fisher\u2019s exact test was substituted. All keyword-group p-values "
    "were Bonferroni-corrected for the number of keyword groups tested "
    "(11 groups; \u03b1 = 0.05/11 = 0.00455). Only the Cost/Rates keyword "
    "group survives Bonferroni correction (\u00a75.4.3)."
)


# ===========================================================================
# Appendix D \u2014 Topic Inventory and Keyword Dictionary
# ===========================================================================

H1("Appendix D. Topic Inventory and Keyword Dictionary")

H2("D.1 Top BERTopic Topics by Share")

TBL(
    ["Topic ID", "Top representative terms (c-TF-IDF)", "Pre share (%)", "Post share (%)", "Pre\u2009\u2192\u2009Post (\u0394pp)"],
    [
        ["0", "loan, process, easy, fast, online", "12.6", "10.7", "\u22121.9"],
        ["1", "rate, lower, competitive, deal", "9.8", "5.4", "\u22124.4"],
        ["2", "communication, response, contact, slow", "6.1", "9.0", "+2.9"],
        ["3", "pre-approval, application, document, upload", "5.4", "4.7", "\u22120.7"],
        ["4", "agent, helpful, professional, knowledge", "4.8", "5.9", "+1.1"],
        ["5", "appraisal, delay, wait, scheduling", "4.0", "5.5", "+1.5"],
        ["6", "closing, smooth, on-time, attorney", "3.7", "3.0", "\u22120.7"],
        ["7", "fee, cost, transparent, lender credit", "3.1", "1.9", "\u22121.2"],
        ["8", "underwriting, condition, complex", "2.8", "3.3", "+0.5"],
        ["9", "automated, system, error, technical", "2.5", "3.6", "+1.1"],
    ],
    caption=(
        "Table D.1. Top ten BERTopic topics by clustered-corpus share. "
        "Topic identifiers correspond to the BERTopic enumeration; topics "
        "are summarised by the top five c-TF-IDF terms. Shares are "
        "computed within the clustered subset (n_clustered = 1,198). The "
        "remaining 34 topics individually account for less than 2.5 "
        "percent of the clustered corpus and are summarised in "
        "08_Code/nlp_topic_inventory_full.csv."
    ),
)

H2("D.2 Keyword Dictionary")

TBL(
    ["Group", "Keywords (representative)", "Pre prevalence (%)", "Post prevalence (%)", "\u0394pp", "p-value", "Bonferroni-significant"],
    [
        ["AI / automation", "ai, bot, chatbot, automated, betsy", "1.15", "1.18", "+0.03", "0.95", "No"],
        ["Cost / rates", "rate, fee, cost, expensive, pricing", "27.40", "15.05", "\u221212.35", "0.0009", "Yes"],
        ["Speed / efficiency", "fast, quick, slow, delay, wait", "21.40", "20.71", "\u22120.69", "0.84", "No"],
        ["Communication", "respond, communication, email, call", "14.49", "20.71", "+6.22", "0.040", "No"],
        ["Digital / process", "online, app, portal, dashboard, login", "16.84", "7.86", "\u22128.98", "0.0034", "No"],
        ["Documentation", "document, upload, paperwork", "10.42", "10.65", "+0.23", "0.94", "No"],
        ["Appraisal", "appraisal, appraiser, valuation", "3.95", "5.92", "+1.97", "0.20", "No"],
        ["Closing", "closing, close, attorney", "8.13", "5.32", "\u22122.81", "0.18", "No"],
        ["Trust", "trust, scam, fraud, suspicious", "1.95", "2.96", "+1.01", "0.30", "No"],
        ["Underwriting", "underwriting, underwriter, condition", "5.21", "6.50", "+1.29", "0.45", "No"],
        ["Sales / pressure", "pushy, aggressive, pressure", "2.46", "1.78", "\u22120.68", "0.55", "No"],
    ],
    caption=(
        "Table D.2. Keyword-group prevalence in the Trustpilot corpus, "
        "pre vs post Betsy. p-values from two-sided chi-square (Yates) or "
        "Fisher's exact test where expected cells fell below 5. "
        "Bonferroni-corrected significance threshold: p < 0.00455 (\u03b1 = "
        "0.05 / 11)."
    ),
)


# ===========================================================================
# Appendix E \u2014 Supplementary Figures
# ===========================================================================

H1("Appendix E. Supplementary Figures")

H2("E.1 Operational Leverage Index")

FIG(
    os.path.join(FIG_FIN, "appendix_fig_fin_operational_leverage_index.png"),
    "Figure E.1. Operational Leverage Index (OLI) for Better.com, fiscal "
    "years 2020\u20132025, with 2023 = 100. The composite is an "
    "equally-weighted average of three components: Revenue Growth Index, "
    "Revenue per Employee Index, and Inverse Expense Ratio Index. The "
    "index is illustrative; it is sensitive to baseline-year selection "
    "and to component weighting (see \u00a73.6 and Appendix A.4).",
)

H2("E.2 BERTopic Topic Map")

FIG(
    os.path.join(FIG_NLP, "appendix_fig_nlp_topic_map.png"),
    "Figure E.2. BERTopic two-dimensional topic map of the cleaned "
    "Trustpilot corpus (n = 1,915). Topics are positioned in a "
    "UMAP-projected embedding space; circle size indicates topic share. "
    "The map is descriptive and is provided for transparency; topic-share "
    "magnitudes should not be interpreted inferentially (see Appendix C.4 "
    "and \u00a78.7)."
)

H2("E.3 BERTopic Topic-Word Importance")

FIG(
    os.path.join(FIG_NLP, "appendix_fig_nlp_topic_word_importance.png"),
    "Figure E.3. BERTopic topic-word importance heatmap for the top 20 "
    "topics by clustered-corpus share. Each row corresponds to a topic, "
    "and each column to a top c-TF-IDF term. Heatmap intensity reflects "
    "the per-topic c-TF-IDF score of the term. The figure is descriptive "
    "and is provided for transparency (see Appendix C.4)."
)


# ===========================================================================
# Appendix F \u2014 Source Reliability and Citation Audit Summary
# ===========================================================================

H1("Appendix F. Source Reliability and Citation Audit Summary")

H2("F.1 Source-Reliability Tier Counts")

TBL(
    ["Tier", "Description", "# Sources used in this thesis"],
    [
        ["High", "Audited financial statements (10-K, 10-Q, S-1).", "10"],
        ["High", "SEC-filed 8-K Exhibit 99.1 / earnings release.", "4"],
        ["High", "Peer-reviewed academic publication.", "26"],
        ["Medium-High", "Independent industry / government report.", "8"],
        ["Medium", "Management-reported operating metric (unaudited).", "5"],
        ["Medium", "Vendor / case-study material.", "2"],
        ["Medium", "Independent self-selected user-generated content (Trustpilot).", "1"],
        ["Medium-Low", "News media (HousingWire, Axios).", "3"],
        ["Low", "Trade-press / vendor blog.", "0 (avoided)"],
    ],
    caption=(
        "Table F.1. Source-reliability tier counts for sources used in this "
        "thesis, derived from the per-source classification in "
        "10_Citation_Audit/F_Source_Reliability_Table.md."
    ),
)

H2("F.2 Citation-Audit Summary")

P(
    "A full citation audit is provided in the project repository at "
    "10_Citation_Audit/ and contains: (A) per-citation status table; (D) "
    "deduplicated APA 7 reference list; (F) source-reliability "
    "classification; (H) the QC checklist documenting the 37 issues fixed "
    "during the cleanup pass. Outstanding items at the time of writing "
    "(see 10_Citation_Audit/E_Outstanding_Items.md): the Qualtrics (2024) "
    "industry NPS-benchmark anchor is documented as a placeholder for a "
    "verifiable industry benchmark and is not used as a primary "
    "inferential anchor; the Hevner et al. (2004) design-science citation "
    "is placed once in Chapter 6 and is not reused; the two "
    "\u201cBetter 2022\u201d anachronisms identified in the audit have "
    "been resolved by re-anchoring to Better HoldCo, Inc. (2021) and "
    "Better HoldCo, Inc. (2023); the two Rocket 2024 / 2025 references "
    "are the FY-2023 and FY-2024 10-K filings respectively (Rocket "
    "Companies, 2024, 2025)."
)


# ===========================================================================
# Appendix G \u2014 Reproducibility Notes / Package Versions
# ===========================================================================

H1("Appendix G. Reproducibility Notes")

H2("G.1 Repository Structure")

P(
    "The thesis is reproducible from the public source-code repository "
    "(github.com/Mukhammad-Azim/Business-Value-of-AI-voice-agents). The "
    "repository\u2019s top-level directories and their roles are: "
    "01_Documentation/ (preliminary outlines and supervisor notes); "
    "02_Raw_Data/ (raw SEC filings and the Trustpilot extraction); "
    "03_Outputs/ (intermediate analysis outputs); 04_Drafts/ (the thesis "
    "Word document); 08_Code/ (the financial and NLP analysis pipelines, "
    "the build-out scripts under 08_Code/buildout/, and the requirements "
    "specification); 09_Cleanup_Report/ (cleanup-pass documentation); "
    "10_Citation_Audit/ (the citation audit deliverables A\u2013H); "
    "11_Thesis_Improvement_Report/ (the improvement plan executed in this "
    "build-out); outputs/ (the final figures embedded in this thesis)."
)

H2("G.2 Run-Once-from-Clone Commands")

P(
    "The financial pipeline is reproduced by executing "
    "08_Code/financial_metrics_project.ipynb (or its scripted equivalent "
    "08_Code/run_financial_pipeline.py); the NLP pipeline is reproduced "
    "by executing 08_Code/nlp_project.ipynb. The build-out scripts under "
    "08_Code/buildout/ are idempotent: each script is guarded by a "
    "BUILDOUT::* sentinel marker that prevents duplicate insertions when "
    "the script is re-run on the same draft. The build-out scripts must "
    "be executed in numerical order (01_lit_review.py, 02_methodology.py, "
    "\u2026, 06_appendices.py, 07_register_pass.py, "
    "99_consistency_scan.py)."
)

H2("G.3 Package Versions")

TBL(
    ["Package", "Version", "Role"],
    [
        ["Python", "3.11", "Interpreter."],
        ["python-docx", "1.1.0", "Document construction in 08_Code/buildout/."],
        ["pdfplumber", "0.11.0", "PDF extraction from SEC filings."],
        ["pypdf", "4.0.1", "Cross-validation PDF extraction."],
        ["pandas", "2.2.0", "Tabular data handling."],
        ["numpy", "1.26.0", "Numerical operations."],
        ["matplotlib", "3.8.0", "Figure generation."],
        ["seaborn", "0.13.0", "Statistical figure styling."],
        ["scipy", "1.12.0", "Welch's t, chi-square, Fisher's exact tests."],
        ["scikit-learn", "1.3.0", "TF-IDF, normalisation."],
        ["sentence-transformers", "2.2.2", "all-MiniLM-L6-v2 embeddings."],
        ["umap-learn", "0.5.5", "UMAP dimensionality reduction."],
        ["hdbscan", "0.8.33", "Density-based clustering."],
        ["bertopic", "0.16.0", "Topic modelling pipeline."],
        ["nltk (with VADER)", "3.8.1 (VADER 3.3.2)", "Sentiment scoring."],
        ["langdetect", "1.0.9", "Language detection in NLP cleaning."],
    ],
    caption=(
        "Table G.1. Package versions used in the financial and NLP "
        "pipelines and in the build-out scripts. The full pinned manifest "
        "is recorded in 08_Code/requirements.txt."
    ),
)


# ---------------------------------------------------------------------------
# Apply
# ---------------------------------------------------------------------------


def apply(doc):
    if has_marker(doc, "appendix_block_inserted"):
        print("[appendix_block_inserted] already present; skipping")
        return False
    is_first = True
    for kind, payload in CONTENT:
        if kind == "h1":
            p = insert_paragraph_at_end(doc, "")
            p.style = doc.styles["Heading 1"]
            p.add_run(payload)
            if is_first:
                add_marker(p, "appendix_block_inserted")
                is_first = False
        elif kind == "h2":
            p = insert_paragraph_at_end(doc, "")
            p.style = doc.styles["Heading 2"]
            p.add_run(payload)
        elif kind == "h3":
            p = insert_paragraph_at_end(doc, "")
            p.style = doc.styles["Heading 3"]
            p.add_run(payload)
        elif kind == "p":
            p = insert_paragraph_at_end(doc, "")
            p.style = doc.styles["Normal"]
            p.add_run(payload)
        elif kind == "caption":
            cap = insert_paragraph_at_end(doc, "")
            try:
                cap.style = doc.styles["Caption"]
            except KeyError:
                pass
            run = cap.add_run(payload)
            run.bold = True
        elif kind == "table":
            headers, rows = payload
            n_rows = 1 + len(rows)
            n_cols = len(headers)
            tbl = insert_table_at_end(doc, n_rows, n_cols, style_name="Table Grid")
            for c, h in enumerate(headers):
                set_table_cell(tbl.rows[0].cells[c], h, bold=True)
            for r, row in enumerate(rows, start=1):
                for c, value in enumerate(row):
                    set_table_cell(tbl.rows[r].cells[c], value)
        elif kind == "figure":
            path, caption = payload
            insert_picture_at_end(doc, path, width_in=6.0)
            cap = insert_paragraph_at_end(doc, "")
            try:
                cap.style = doc.styles["Caption"]
            except KeyError:
                pass
            run = cap.add_run(caption)
            run.bold = True
    print("[appendix_block_inserted] inserted")
    return True


def main():
    doc = open_draft()
    if apply(doc):
        save_draft(doc)
        print("Saved.")


if __name__ == "__main__":
    main()
