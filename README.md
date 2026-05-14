# Business Value of Voice LLM Agents in Financial Services: Evidence from Better.com

> **MSc Business Informatics Thesis** — Corvinus University of Budapest  
> **Student:** Mukhammad Azim Khadyatullaev  
> **Supervisor:** Mike Nimrod  
> **Date:** April 2026

---

## Overview

This repository contains the complete research materials, analytical code, datasets, and thesis drafts for an MSc thesis examining the **business value of large language model (LLM)-based voice agents** in regulated financial services. The study uses Better Home & Finance Holding Company (NASDAQ: BETR) as a revelatory single case and triangulates three independent evidence streams:

1. **Qualitative Case-Study Evidence** — Analysis of Better.com's operating model, Tinman® platform architecture, Betsy™ voice agent, and ElevenLabs integration (sourced from SEC filings, earnings transcripts, and vendor case studies).
2. **Longitudinal Financial Analysis** — SEC-extracted annual financial metrics (2021–2025) benchmarked against industry peer Rocket Companies (NYSE: RKT).
3. **NLP Customer-Discourse Analysis** — VADER sentiment scoring and BERTopic topic modelling of 1,915 Trustpilot reviews segmented around the deployment of generative AI voice agents.

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
│   ├── Better/                 # Better.com: 10-K (2021–2025), S-1, earnings transcripts
│   ├── Rocket Mortgage/        # Rocket Companies: 10-K (2018–2025)
│   ├── ElevenLabs/             # ElevenLabs vendor materials and technical overviews
│   └── Financial_Industry/     # Mortgage Bankers Association & industry benchmarks
│
├── 03_Drafts/                  # Thesis drafts (Word format)
│
├── 04_Notes/                   # Research notes and empirical findings (2025 Earnings)
│
├── 05_Code/                    # All analytical code
│   ├── requirements.txt        # Python dependencies
│   ├── financial_metric_analysis.ipynb      # SEC financial metrics analysis
│   ├── better_reviews_topic_modeling.ipynb  # BERTopic NLP analysis
│   ├── cleaning_reviews.ipynb  # Trustpilot review cleaning pipeline
│   └── Data Extraction code/   # SEC PDF extraction scripts
│
├── 06_Data/                    # Processed, analysis-ready datasets
│   ├── financial_dataset_annual.csv    # Annual SEC-extracted financials (2018–2025)
│   ├── dataset_viewer.html             # Interactive dataset explorer
│   └── NLP/                           # Trustpilot review data
│
├── 07_Outputs/figures/         # All thesis figures (PNG + interactive HTML)
│   ├── financial/              # Longitudinal financial charts
│   ├── NLP/                    # Sentiment and topic modelling visualizations
│   └── design_pattern/         # System architecture diagrams
│
└── 08_Citation_Audit/          # Reference list audit and source reliability table
```

---

## Key Datasets

### `06_Data/financial_dataset_annual.csv`
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

**Sources:** Better.com S-1, 10-K filings 2021–2025; Rocket Companies 10-K filings 2018–2025.

### `06_Data/NLP/better_trustpilot_clean.csv`
Cleaned Trustpilot review corpus used for all NLP analyses.

| Field | Description |
|---|---|
| `review_text` | Cleaned review body text |
| `rating` | Star rating (1–5) |
| `date` | Review date |
| `period` | `pre_betsy` / `post_betsy` |
| `vader_compound` | VADER compound sentiment score (−1 to 1) |
| `topic_id` | BERTopic cluster assignment |

---

## Key Empirical Findings

| Dimension | Finding | Evidence Source |
|---|---|---|
| **Conversion** | Lead-to-lock conversion rate increased by **+30%** (3.3% → 4.4%) | CEO Q2 2025 Transcript |
| **Automation** | **35.5%** of borrower inquiries automated end-to-end; 1.89M calls in 2025 | ElevenLabs Case Study |
| **Efficiency** | **41% reduction** in cost to originate loans; cost parity at ~1/2 of industry avg | 2025 10-K / Vendor Data |
| **Scale** | Processed **600,000 interactions** in Q2 2025 with declining sales headcount | Q2 2025 Earnings Call |
| **Productivity** | Revenue per Employee (RPE) improved **~42.9%** (FY2024 → FY2025) | SEC Longitudinal Dataset |
| **Customer Experience** | Net Promoter Score (NPS) improved from **39 to 64** | Management Reporting |
| **Sentiment** | Trustpilot star ratings declined (4.28 → 3.86) while sentiment shifted toward process | BERTopic / VADER Analysis |

---

## Analytical Pipeline

```
SEC PDFs  ──►  05_Code/Data Extraction code/extract_pdf_texts.py
                             │
                             ▼
               06_Data/financial_dataset_annual.csv
                             │
                             ▼
               05_Code/financial_metric_analysis.ipynb (Figures 5.1–5.3)

Trustpilot  ──►  05_Code/cleaning_reviews.ipynb
                             │
                             ▼
               06_Data/NLP/better_trustpilot_clean.csv
                             │
                             ▼
               05_Code/better_reviews_topic_modeling.ipynb (Figures 5.4–5.6)
```

---

## Installation & Reproduction

### Requirements

- Python 3.10–3.12
- All dependencies in `05_Code/requirements.txt`

```bash
git clone https://github.com/Mukhammad-Azim/Business-Value-of-AI-voice-agents.git
cd Business-Value-of-AI-voice-agents
pip install -r 05_Code/requirements.txt
```

---

## Citation

If you use the dataset, code, or figures from this repository, please cite:

```
Khadyatullaev, M. A. (2026). Business Value of Voice LLM Agents in Financial Services: 
Evidence from Better.com. MSc Thesis, Corvinus University of Budapest.
```

---

## Licence

The code in this repository is released under the **MIT Licence**. SEC filing data is publicly available via EDGAR. Trustpilot review data was collected for academic research purposes. Vendor materials remain the property of their respective owners.

