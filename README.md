# Business Value of AI Voice Agents in Mortgage Origination

> **MSc Business Informatics Thesis** — Utrecht University  
> *A mixed-methods single-case study of Better.com's deployment of Betsy, an AI-powered voice loan assistant, built on the ElevenLabs voice platform and integrated with the proprietary Tinman mortgage operating system.*

---

## Overview

This repository contains the complete research materials, analytical code, datasets, and thesis drafts for an MSc thesis examining the **business value of large language model (LLM)-based voice agents** in regulated financial services. The study uses Better Home & Finance Holding Company (NASDAQ: BETR) as a revelatory single case and triangulates three independent evidence streams:

1. **Qualitative case-study evidence** — Better.com's operating model, Tinman platform architecture, Betsy voice agent, and ElevenLabs integration (sourced from SEC filings, press materials, and vendor case studies)
2. **Longitudinal financial analysis** — SEC-extracted annual financial metrics (2021–2025) benchmarked against Rocket Companies (NYSE: RKT)
3. **NLP customer-discourse analysis** — VADER sentiment scoring and BERTopic topic modelling of 1,915 Trustpilot reviews segmented around Betsy's 17 October 2024 launch date

The thesis is structured around two research questions:

- **RQ1:** How have voice LLM agents been integrated into Better.com's mortgage origination process, and what architectural prerequisites does this imply?
- **RQ2:** What measurable business value can be associated with Better.com's voice AI deployment across operational efficiency, labour productivity, and customer experience?

---

## Repository Structure

```
Business-Value-of-AI-voice-agents/
│
├── 01_Literature/              # Annotated bibliography and literature review sources
│
├── 02_Case_Study_Data/         # SEC filings, annual reports, vendor materials
│   ├── Better/                 # Better.com: 10-K (2023–2025), S-1, ElevenLabs case study
│   ├── Rocket Mortgage/        # Rocket Companies: 10-K (2021–2025)
│   ├── ElevenLabs/             # ElevenLabs vendor press materials
│   └── Financial_Industry/     # Mortgage Bankers Association & industry benchmarks
│
├── 03_Drafts/                  # Thesis drafts (Word format)
│   ├── Main_Draft_FULL.docx    # Complete thesis draft
│   └── Backup/                 # Version backups
│
├── 04_Notes/                   # Research notes, memos, and planning documents
│
├── 05_Code/                    # All analytical code
│   ├── requirements.txt        # Python dependencies (pinned)
│   ├── financial_metric_analysis.ipynb      # SEC financial metrics analysis (Figures 5.1–5.3)
│   ├── better_reviews_topic_modeling.ipynb  # BERTopic NLP analysis (Figures 5.4–5.6)
│   ├── cleaning_reviews.ipynb  # Trustpilot review cleaning pipeline
│   ├── apply_citation_audit.py # Citation consistency checker
│   ├── apply_thesis_cleanup.py # Thesis structural cleanup utility
│   └── Data Extraction code/   # SEC PDF extraction scripts
│       ├── extract_pdf_texts.py        # PDF text extraction from SEC filings
│       ├── build_dataset_v4.py         # Compiles financial_dataset_annual.csv
│       └── financial_dataset_documentation.md  # Dataset audit trail & provenance
│
├── 06_Data/                    # Processed, analysis-ready datasets
│   ├── financial_dataset_annual.csv    # Annual SEC-extracted financials (Better + Rocket, 2018–2025)
│   ├── dataset_viewer.html             # Interactive dataset explorer
│   └── NLP/                           # Trustpilot review data
│       ├── Better_Reviews.csv          # Raw scraped reviews (Apify)
│       └── better_trustpilot_clean.csv # Cleaned & pre-processed corpus (1,915 reviews)
│
├── 07_Outputs/figures/         # All thesis figures (PNG + interactive HTML)
│   ├── financial/              # Figures 5.1–5.3 and OLI appendix figure
│   └── NLP/                    # Figures 5.4–5.6 and appendix topic maps
│
├── 08_Cleanup_Report/          # Automated structural analysis reports
├── 09_Citation_Audit/          # Reference list audit outputs
└── 10_Thesis_Improvement_Report/  # Chapter-level critical analyses and revision notes
```

---

## Key Datasets

### `Data/financial_dataset_annual.csv`
Annual financial metrics extracted from SEC filings for both companies.

| Field | Description |
|---|---|
| `Company` | `Better` or `Rocket` |
| `Year` | Fiscal year (Better: 2021–2025; Rocket: 2018–2025) |
| `Revenue` | Total net revenue (millions USD) |
| `Total_Expenses` | Standardised total expense base (millions USD) |
| `Net_Income` | Net income / loss (millions USD) |
| `Op_Cash_Flow` | Operating cash flow (millions USD) |
| `Headcount` | Year-end employee count |
| `RPE` | Revenue per employee (millions USD) |
| `Expense_Ratio` | Total expenses / revenue |
| `Funded_Loan_Volume` | Funded mortgage volume (billions USD) |

**Sources:** Better.com S-1, 10-K filings 2023–2025; Rocket Companies 10-K filings 2020–2025. All values in millions USD. Full audit trail in `05_Code/Data Extraction code/financial_dataset_documentation.md`.

### `Data/NLP/better_trustpilot_clean.csv`
Cleaned Trustpilot review corpus used for all NLP analyses.

| Field | Description |
|---|---|
| `review_text` | Cleaned review body text |
| `rating` | Star rating (1–5) |
| `date` | Review date |
| `period` | `pre_betsy` / `post_betsy` (split at 17 October 2024) |
| `vader_compound` | VADER compound sentiment score (−1 to 1) |
| `topic_id` | BERTopic cluster assignment (−1 = noise) |

**Sample sizes:** Pre-Betsy: n = 1,746 | Post-Betsy: n = 169 | Total clean corpus: 1,915 reviews  
**Raw source:** Scraped via Apify from Better.com's public Trustpilot profile.

---

## Analytical Pipeline

```
SEC PDFs  ──►  05_Code/Data Extraction code/extract_pdf_texts.py
                             │
                             ▼
               05_Code/Data Extraction code/build_dataset_v4.py
                             │
                             ▼
               06_Data/financial_dataset_annual.csv
                             │
                             ▼
               05_Code/financial_metric_analysis.ipynb
               (Figures 5.1, 5.2, 5.3, OLI  ──►  07_Outputs/figures/financial/)

Trustpilot  ──►  06_Data/NLP/Better_Reviews.csv
                             │
                             ▼
               05_Code/cleaning_reviews.ipynb
                             │
                             ▼
               06_Data/NLP/better_trustpilot_clean.csv
                             │
                             ▼
               05_Code/better_reviews_topic_modeling.ipynb
               (Figures 5.4, 5.5, 5.6  ──►  07_Outputs/figures/NLP/)
```

---

## Generated Figures

All thesis figures are exported to `outputs/figures/` in both PNG and interactive HTML formats.

### Financial Figures (`07_Outputs/figures/financial/`)

| File | Thesis Figure | Description |
|---|---|---|
| `fig_fin_better_financial_trajectory_clean.png` | Figure 5.1 | Revenue, expense base, net income/loss 2021–2025 |
| `fig_fin_expense_ratio_cashflow_clean.png` | Figure 5.2 | Expense ratio & operating cash flow margin 2021–2025 |
| `fig_fin_headcount_productivity_clean.png` | Figure 5.3 | Headcount & RPE 2021–2025 |
| `fig_fin_benchmark_productivity_expense_ratio_clean.png` | Appendix | Better vs. Rocket benchmark comparison |
| `appendix_fig_fin_operational_leverage_index.png` | Appendix E.1 | Operational Leverage Index (OLI) |

### NLP Figures (`07_Outputs/figures/NLP/`)

| File | Thesis Figure | Description |
|---|---|---|
| `fig_nlp_sentiment_by_period_clean.png` | Figure 5.4 | VADER compound sentiment distribution pre/post Betsy |
| `fig_nlp_keyword_prevalence_clean.png` | Figure 5.5 | Keyword-group prevalence across 7 thematic categories |
| `fig_nlp_topic_shares_clean.png` | Figure 5.6 | BERTopic topic-share comparison pre/post Betsy |
| `fig_nlp_quarterly_keywords_clean.png` | Appendix | Quarterly keyword trend analysis |
| `appendix_fig_nlp_topic_map.png` | Appendix | BERTopic intertopic distance map |
| `appendix_fig_nlp_topic_word_importance.png` | Appendix | Topic-word importance heatmap |

---

## Installation & Reproduction

### Requirements

- Python 3.10–3.12
- All dependencies pinned in `08_Code/requirements.txt`

```bash
git clone https://github.com/Mukhammad-Azim/Business-Value-of-AI-voice-agents.git
cd Business-Value-of-AI-voice-agents

pip install -r 05_Code/requirements.txt
```

### Running the Analyses

**Step 1 — Financial metrics analysis:**
```bash
jupyter notebook 05_Code/financial_metric_analysis.ipynb
```

**Step 2 — NLP review cleaning:**
```bash
jupyter notebook 05_Code/cleaning_reviews.ipynb
```

**Step 3 — NLP topic modelling & sentiment:**
```bash
jupyter notebook 05_Code/better_reviews_topic_modeling.ipynb
```

All figures are automatically exported to `07_Outputs/figures/` on notebook execution.

> **Note:** The raw Trustpilot review file (`06_Data/NLP/Better_Reviews.csv`) was collected via Apify from Better.com's public Trustpilot profile. The financial PDFs in `02_Case_Study_Data/` are publicly available SEC filings and vendor press materials.

---

## Methodology Summary

| Dimension | Method | Tool / Source |
|---|---|---|
| Research design | Convergent parallel mixed methods | — |
| Case selection | Revelatory single case | Better.com (BETR) |
| Financial data | SEC filing extraction, longitudinal descriptive analysis | 10-K, S-1 filings |
| Industry benchmark | Directional comparison (not counterfactual) | Rocket Companies (RKT) |
| Customer sentiment | VADER lexicon-based sentiment scoring | `vaderSentiment` |
| Topic modelling | BERTopic with all-MiniLM-L6-v2 embeddings, UMAP, HDBSCAN | `bertopic`, `sentence-transformers` |
| Statistical tests | Welch's t-test, chi-squared / Fisher's exact, Bonferroni correction | `scipy` |
| Causal claims | None — all findings are descriptive and observational | — |

### Key Analytical Constraints
- The analysis is **observational and descriptive**. No causal claims are made.
- Betsy launched on **17 October 2024**; FY2024 therefore blends ~9.5 months pre-launch with ~2.5 months post-launch. The primary comparison window is **FY2024 → FY2025**.
- All financial improvements are attributed to the **broader Betsy/Tinman AI operating model**, not to Betsy in isolation.
- Trustpilot data is self-selected and the post-Betsy corpus (n = 169) is substantially smaller than the pre-Betsy corpus (n = 1,746).

---

## Key Findings

| Stream | Finding |
|---|---|
| **Financial** | Revenue grew ~52% (2024→2025) while expenses grew ~5.3%; expense ratio fell from 2.89 to 2.01; RPE improved ~42.9% — consistent with AI-enabled operational leverage |
| **Benchmark** | Better's relative efficiency improvement exceeded Rocket's over the same period, suggesting the trajectory is not explained solely by market recovery |
| **Customer — NPS** | Management-reported NPS rose from ~39 to ~64 (medium-reliability, unaudited) |
| **Customer — Trustpilot** | Star ratings declined 4.28 → 3.86 (p = 0.0019, d = 0.29); VADER sentiment declined 0.64 → 0.52 (p = 0.0057, d = 0.25) |
| **AI visibility** | Explicit AI mentions in Trustpilot reviews: ~1.2% pre and post Betsy (p = 1.000) — consistent with voice AI as invisible infrastructure |
| **Topic modelling** | Post-Betsy shift away from refinance topics; Closing Timeline & Process topic share rose ~+3.5 pp |

---

## Citation

If you use the dataset, code, or figures from this repository, please cite:

```
[Author], (2025). Business Value of AI Voice Agents in Mortgage Origination:
A Mixed-Methods Single-Case Study of Better.com's Betsy Deployment.
MSc Thesis, Utrecht University.
```

---

## Licence

The code in this repository is released under the **MIT Licence**.  
SEC filing data is publicly available and sourced from the U.S. Securities and Exchange Commission (SEC EDGAR).  
Trustpilot review data was collected from Better.com's public Trustpilot profile for non-commercial academic research purposes.  
Vendor materials (ElevenLabs, Better.com press releases) remain the intellectual property of their respective owners.
