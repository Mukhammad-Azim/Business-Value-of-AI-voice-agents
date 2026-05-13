# Financial Metrics Analysis: SEC Filing Comparative Study of Better.com

## Comprehensive Methodological and Findings Report

**Research Context:** MSc Thesis — *Business Value of Voice LLM Agents in Financial Services*
**Author:** Mukhammad Azim Khadyatullaev | Corvinus University of Budapest
**Date:** May 2026

---

## 1. Purpose and Research Alignment

This report documents the complete financial metrics analysis pipeline conducted as the primary quantitative empirical component of the thesis. While the companion NLP analysis (`nlp_project_report.md`) evaluates the customer experience dimension through Trustpilot review mining, this financial analysis addresses the **operational efficiency, productivity, and financial performance dimensions** of business value — using longitudinal SEC filing data from Better.com and the industry benchmark Rocket Mortgage.

The analysis directly supports the revised **Research Question 2** (RQ2):

> *"What measurable business value can be associated with Better.com’s voice AI deployment across operational efficiency, productivity, customer experience, and financial performance, and what factors mediate the realization of this value?"*

It also provides indirect structural context for **Research Question 1** (RQ1):

> *"How have voice LLM agents been integrated into Better.com's mortgage origination processes, and what does this integration reveal about the technical and organizational prerequisites for deploying conversational AI in a regulated financial services environment?"*

The financial analysis is strongest for RQ2. Its contribution to RQ1 is indirect: it contextualizes the financial trajectory and organizational restructuring that preceded Betsy's deployment, but evidence for Tinman as Betsy's architectural prerequisite comes primarily from management disclosures and the qualitative case study (Chapter 4), not from financial ratios.

The analysis quantitatively tests whether Better.com's post-Betsy financial trajectory is **consistent with AI-enabled operational leverage** — the hypothesis that voice AI deployment, as part of Better's broader Betsy/Tinman AI operating model, is associated with revenue recovery and productivity gains without proportional expense growth.

### 1.1 Specific Analytical Objectives

1. **Revenue recovery assessment:** Determine whether Better's revenue recovered after the Betsy launch window (2024–2025) relative to the pre-Betsy nadir (2023).
2. **Expense intensity analysis:** Test whether expense ratios improved simultaneously with revenue recovery — the signature of operational leverage.
3. **Labor productivity measurement:** Track revenue per employee and related ratios across the pre/post-Betsy timeline.
4. **Benchmark comparison:** Compare Better's trajectory against Rocket Mortgage using a benchmark comparison to contextualize whether improvements are consistent with broader market recovery or reflect idiosyncratic operational shifts.
5. **Alternative baseline checks:** Compare 2023→2025, 2024→2025, and pre-period-average→2025 to ensure findings are not artifacts of trough-year baseline selection.

### 1.2 Temporal Scope and Betsy Timeline Alignment

Betsy launched on **October 17, 2024**. The ElevenLabs voice infrastructure partnership was announced later, in **June 2025**. Because this analysis uses annual SEC data, it cannot isolate Q4 2024 effects from earlier 2024 performance. The annual SEC analysis should therefore be interpreted as **audited background evidence for the broader financial trajectory**, while quarterly operating metrics discussed in the thesis (Chapters 4–5) provide the more launch-aligned view of Betsy's deployment and scaling.

The 2025 post-Betsy period captures Better's use and scaling of Betsy, but only part of 2025 reflects the ElevenLabs-enabled voice infrastructure. Therefore, 2025 financial changes should be associated with **Better's broader Betsy/Tinman AI operating model** rather than specifically to ElevenLabs, and the analysis cannot isolate Betsy's specific contribution from the broader operating-model and macroeconomic context.

---

## 2. Source Documents and Data Collection

### 2.1 Primary Source Documents

The financial dataset was constructed from a corpus of **10 SEC regulatory filing PDFs**: three Better.com annual reports (10-K), one Better.com S-1 registration statement, and six Rocket Companies annual reports (10-K). All were downloaded and stored locally in the research workspace.

#### Better Home & Finance Holding Company (NASDAQ: BETR)

| Document | File Path | Size | Source |
|---|---|---|---|
| 2023 10-K (FY ended Dec 31, 2023) | `03_Case_Study_Data/Better/Annual Reports/2023.pdf` | 2.0 MB | SEC EDGAR |
| 2024 10-K (FY ended Dec 31, 2024) | `03_Case_Study_Data/Better/Annual Reports/2024.pdf` | 1.6 MB | SEC EDGAR |
| 2025 10-K (FY ended Dec 31, 2025) | `03_Case_Study_Data/Better/Annual Reports/2025.pdf` | 2.2 MB | SEC EDGAR |
| S-1 Registration Statement | `03_Case_Study_Data/Better/Annual Reports/S1.pdf` | 1.2 MB | SEC EDGAR |

#### Rocket Companies, Inc. (NYSE: RKT)

| Document | File Path | Size | Source |
|---|---|---|---|
| 2020 10-K (FY ended Dec 31, 2020) | `03_Case_Study_Data/Rocket Mortgage/Annual Reports/2020.pdf` | 2.0 MB | SEC EDGAR |
| 2021 10-K (FY ended Dec 31, 2021) | `03_Case_Study_Data/Rocket Mortgage/Annual Reports/2021.pdf` | 15.5 MB | SEC EDGAR |
| 2022 10-K (FY ended Dec 31, 2022) | `03_Case_Study_Data/Rocket Mortgage/Annual Reports/2022.pdf` | 2.5 MB | SEC EDGAR |
| 2023 10-K (FY ended Dec 31, 2023) | `03_Case_Study_Data/Rocket Mortgage/Annual Reports/2023.pdf` | 1.8 MB | SEC EDGAR |
| 2024 10-K (FY ended Dec 31, 2024) | `03_Case_Study_Data/Rocket Mortgage/Annual Reports/2024.pdf` | 2.4 MB | SEC EDGAR |
| 2025 10-K (FY ended Dec 31, 2025) | `03_Case_Study_Data/Rocket Mortgage/Annual Reports/2025.pdf` | 1.9 MB | SEC EDGAR |

### 2.2 How Documents Were Accessed

All filings were accessed via the **SEC EDGAR** system at `https://www.sec.gov/cgi-bin/browse-edgar`. The 10-K filings are mandatory annual disclosures containing audited financial statements, MD&A, and operational metrics. The S-1 filing is Better.com's pre-merger registration statement containing historical financial data predating the public listing.

### 2.3 The 2021 Data Gap Problem

Better.com files as a **Smaller Reporting Company (SRC)**, meaning its 10-Ks provide only **two years** of audited P&L data (versus three years for larger filers like Rocket). The 2023 10-K covers only 2022–2023. The **S-1 registration statement** was used to obtain 2021 figures, including the employee peak of 10,400. As documented in `financial_dataset_documentation.md`:

> *"Better's transition to a public company follows 'Smaller Reporting Company' rules, meaning their 10-Ks only provide 2 years of audited P&L. This created the 2021 gap in the 2023 10-K."*

### 2.4 Rocket 2018–2019 Data Provenance

Although separate Rocket 2018 and 2019 annual-report PDFs were not included in the local source corpus, the dataset includes Rocket 2018–2019 historical values. The `build_dataset_v4.py` script marks the 2018 row with a `# Baseline` comment, and the dataset documentation references the 2020 10-K as the source for 2018–2020 historical data. Rocket's 2020 Form 10-K contains comparative historical financial tables covering prior fiscal years. These prior-year values were therefore sourced from the 2020 10-K rather than from separate 2018 or 2019 filings. The exact extraction path should be verified against the source PDF before final thesis submission.

### 2.5 Supplementary Sources (Not in the Annual Dataset)

The following sources provide context in the thesis but are **not** part of `financial_dataset_annual.csv`:

- **Better.com Earnings Call Transcripts (2024–2025):** Via S&P Global Market Intelligence. Used for qualitative management commentary on Betsy performance, NPS, and cost-to-originate claims.
- **MBA Quarterly Performance Reports:** Industry benchmark cost-to-originate data. Third-party source.
- **ElevenLabs/BusinessWire Case Study (February 2026):** Technical partnership documentation.
- **Better.com Press Releases:** Betsy launch announcement (October 17, 2024).

### 2.6 Data Provenance Classification

| Data Type | Method | Reliability |
|---|---|---|
| Revenue, Expenses, Net Income | Extracted from audited 10-K statements | High — externally audited |
| Operating Cash Flow | Extracted from 10-K cash flow statements | High — audited |
| Total Assets, Liabilities, Equity | Extracted from 10-K balance sheets | High — audited |
| Employee Count | Extracted from 10-K Item 1 disclosures | Medium-High — self-reported, unaudited |
| Derived ratios (Profit Margin, etc.) | Calculated in `build_dataset_v4.py` | High — deterministic from audited inputs |
| Better 2021 data | Extracted from S-1 historical financials | Medium-High — audited pre-merger filing |
| Rocket 2018–2019 data | From comparative tables in Rocket 2020 10-K | Medium-High — audited historical comparatives |
| NPS (39→64) | Better earnings transcript (2025) | Medium — management-reported, unaudited |
| Cost-to-originate ($4,900) | Author-estimated from Total Expenses / Funded Loans | Medium — proxy calculation |
| MBA industry CTO benchmark | MBA Quarterly Performance Report | High — third-party industry report |

---

## 3. PDF and Text Extraction Pipeline

### 3.1 Primary Script: `extract_pdf_texts.py`

**Location:** `08_Code/Data Extraction code/extract_pdf_texts.py`
**Library:** `pdfplumber` (Python)
**Output:** `08_Code/extracted_text/` (one `.txt` per PDF)

The script processes all 10 source PDFs through page-level text extraction:

```python
def extract_pdf(pdf_path, out_path, stem):
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, 1):
            text = page.extract_text(x_tolerance=2, y_tolerance=3)
            # writes page-delimited text to output file
```

**Parameters:** `x_tolerance=2` (character grouping), `y_tolerance=3` (line grouping). No OCR — SEC filings contain embedded text layers.

### 3.2 Auxiliary Script: `extract_s1.py`

**Library:** `pypdf` — alternative parser used specifically for the S-1 filing, reflecting that different PDF internal structures may respond better to different parsing engines.

### 3.3 Extraction Limitations

1. **No table-to-dataframe conversion:** `pdfplumber`'s `extract_text()` produces raw text in reading order but does not preserve tabular structure. Financial figures were manually identified and transcribed.
2. **Unit variance:** Some filings report in thousands ($000s), others in millions ($M). Manual standardization to millions was required.
3. **Final values were manually cross-verified** against source PDFs to ensure accuracy.

---

## 4. Dataset Construction and Metric Definitions

### 4.1 Builder Script: `build_dataset_v4.py`

**Output:** `financial_dataset_annual.csv` (13 rows, 15 columns)

Financial values are **hardcoded into the script** as a Python list of dictionaries. The final dataset was assembled through manual transcription and cross-verification of audited financial figures from the source PDFs against the original SEC tables to guarantee absolute mathematical fidelity and academic rigor. This manual verification step ensures dataset integrity beyond what automated validation alone can guarantee.

### 4.2 Raw Fields (from SEC filings)

| Field | Description | Source Location in 10-K |
|---|---|---|
| `Company` | "Better" or "Rocket" | — |
| `Year` | Fiscal year (2018–2025) | — |
| `Revenue` | Total net revenue ($M) | Consolidated Statements of Operations |
| `Total_Expenses` | Standardized total expense base ($M) | Consolidated Statements of Operations (see §4.4) |
| `Net_Income` | Net income/loss ($M) | Consolidated Statements of Operations |
| `Op_Cash_Flow` | Net cash from operating activities ($M) | Consolidated Statements of Cash Flows |
| `Total_Assets` | Total assets ($M) | Consolidated Balance Sheet |
| `Total_Liabilities` | Total liabilities ($M) | Consolidated Balance Sheet |
| `Total_Equity` | Total stockholders' equity ($M) | Consolidated Balance Sheet |
| `Employees` | Approximate headcount (count) | Item 1 (Business) |

### 4.3 Derived Fields (calculated in script)

| Metric | Formula | Interpretation |
|---|---|---|
| `Profit_Margin` | Net_Income / Revenue | Profitability; negative = losses |
| `Expense_Ratio` | Total_Expenses / Revenue | Cost intensity; >1 = expenses exceed revenue |
| `Revenue_per_Employee` | Revenue / Employees ($M per person) | Labor productivity proxy |
| `Equity_Ratio` | Total_Equity / Total_Assets | Financial health |
| `Rev_Growth` | YoY % change in Revenue (by company) | Revenue momentum |

### 4.4 Definition of `Total_Expenses`

`Total_Expenses` is used as a standardized expense-base variable for cross-year comparison. Where a directly comparable "total costs and expenses" line item was available in the filing's income statement, it was extracted. Where filing presentation differed between companies or years, the value was standardized manually during dataset construction. Because the precise composition of expense categories may vary across Better and Rocket (e.g., Better reports gain-on-sale and servicing income/expenses differently from Rocket's diversified model), the resulting `Expense_Ratio` should be interpreted as a **broad cost-intensity indicator** rather than a strict operating-expense ratio. Cross-company comparisons of this metric should be treated with particular caution.

### 4.5 Period Definitions

| Period | Years | Rationale |
|---|---|---|
| **Pre-Betsy** | 2021–2023 | Before voice AI deployment |
| **Transition** | 2024 | Betsy launched Q4 2024; mixed year |
| **Post-Betsy** | 2025 | First full fiscal year with Betsy |

Because Betsy launched on October 17, 2024, annual data cannot isolate Q4 2024 effects from earlier 2024 performance. The entire fiscal year 2024 is therefore conservatively treated as a "Transition" period.

### 4.6 Dataset Audit and Reconciliation

| Property | Value |
|---|---|
| **Total rows** | 13 (5 Better + 8 Rocket) |
| **Total columns** | 15 (10 raw + 5 derived) |
| **Better coverage** | 2021–2025 (5 years) |
| **Rocket coverage** | 2018–2025 (8 years) |
| **Units** | All financial values in millions USD ($M); Employees in headcount |
| **Missing values** | Rev_Growth is NaN for first year of each company (no prior year); zero NaN values otherwise |
| **Better 2021 source** | S-1 registration statement (SRC gap in 10-K series) |
| **Rocket 2018–2019 source** | Historical comparative tables in Rocket 2020 10-K |
| **Derived metric validation** | All derived ratios are deterministic calculations from audited inputs |
| **Cross-company comparability** | Limited for `Total_Expenses` due to different accounting presentations |

---

## 5. Analysis Pipeline in `financial_metric_Analysis.ipynb`

### 5.1 Purpose

The notebook is explicitly framed as an **"RQ2 Empirical Support Notebook"** testing whether Better's post-Betsy trajectory is consistent with AI-enabled operational leverage. It states: *"This notebook is designed as an empirical support chapter for the thesis rather than a generic exploratory analysis."*

### 5.2 Libraries

`pandas`, `numpy`, `matplotlib`, `seaborn`, `IPython.display.Markdown`

### 5.3 Workflow Summary

| Cell | Content | Output |
|---|---|---|
| 1 | Setup, project root detection, helper functions | Configuration |
| 2 | Data loading, validation, period assignment | Dataset display |
| 3 | **Figure 1:** Revenue & Expense trajectories (Better vs Rocket) | Dual-panel line chart |
| 4 | **Figure 2:** Revenue per Employee comparison | Line chart |
| 5 | **Figure 3:** Structural break dashboard (2×2 grid) | Multi-panel with vertical break line at 2024 |
| 6 | **Figure 4:** Profit Margin comparison | Bar chart |
| 7 | **Figure 5:** Revenue Growth rates | Bar chart |
| 8 | Operational Leverage Index (2023=100) | Composite index calculation |
| 9 | Period summary tables and descriptive benchmark comparison against Rocket Mortgage | Summary DataFrames |
| 10 | **Figure 6:** Expense Intensity & Cash Flow dynamics | Dual-axis chart |
| 11 | RQ2 Findings Summary | Markdown-formatted thesis-ready text |

### 5.4 Key Analytical Constructs

**Operational Leverage Index (supplementary):** Custom composite (2023=100) averaging three equally-weighted normalized components: Revenue Growth Index, RPE Index, and Inverse Expense Ratio Index. This index is retained as a compact visualization of multiple normalized trends but is **not used as primary evidence** because it is author-constructed, equally weighted, and sensitive to the 2023 baseline.

**Descriptive benchmark comparison:** Compares Better's Pre→Post metric changes against Rocket's. This is a descriptive comparison against Rocket Mortgage as a directional industry benchmark, **not a formal econometric counterfactual research design**. Rocket and Better differ substantially in scale, business model, and 2025 acquisition context, so Rocket functions as a directional industry benchmark rather than a valid untreated counterfactual.

---

## 6. Results and Findings

### 6.1 Finding 1: Revenue Recovery (Primary 2024→2025)

Better's revenue increased from **$108.5M** (2024) to **$164.9M** (2025) = **+52.0%** (primary post-transition finding).
- *Supporting finding (2023→2025):* Revenue grew from **$76.8M** (2023) to **$164.9M** (2025) = **+114.6%** recovery.
- *Baseline caveat:* The 2023→2025 recovery is heavily amplified by the depressed market-trough year following the post-2021 mortgage rate shock. The 2024→2025 comparison provides a cleaner, more conservative view of post-Betsy revenue momentum.

### 6.2 Finding 2: Controlled Expense Growth (Primary 2024→2025)

Better's total operating expenses increased from **$313.9M** (2024) to **$330.7M** (2025) = **+5.3%**, representing a highly disciplined **10:1 ratio** of revenue-to-expense growth during scaling.
- *Supporting finding (2023→2025):* Total expenses showed an absolute decline of **-10.2%** (from **$368.1M** to **$330.7M**).
- *Confounder:* Prior massive workforce reductions (10,400→820 between 2021–2023) already lowered the expense base before Betsy's launch.

### 6.3 Finding 3: Expense Ratio Improvement (Primary 2024→2025)

Better's expense ratio declined from **2.89** (2024) to **2.01** (2025) = **-30.6%**, signifying strong post-transition operational leverage.
- *Supporting finding (2023→2025):* Expense ratio declined from **4.79** to **2.01** = **-58.0%**. Better spent $4.79 per $1 revenue in 2023; $2.01 by 2025.
- *Baseline caveat:* While the rate of improvement is consistent with AI-driven efficiency, the magnitude in the 2023→2025 window is heavily amplified by the depressed 2023 revenue baseline.

### 6.4 Finding 4: Narrowing Losses (Primary 2024→2025)

Better's net losses improved from **-$206.3M** (2024) to **-$165.9M** (2025) = **19.6% loss reduction**.
- *Supporting finding (2023→2025):* Net losses improved from **-$536.4M** to **-$165.9M** = **69.1% loss reduction**.
- *Unprofitability Note:* Although the trajectory is positive, Better remained unprofitable in 2025. Improvements reflect a combination of market recovery, prior restructuring, and operational gains.

### 6.5 Finding 5: Labor Productivity Recovery (Primary 2024→2025)

Revenue per employee increased from **$0.087M** (2024) to **$0.124M** (2025) = **+42.9%** (the strongest single-year productivity gain in the dataset).
- *Supporting finding (2023→2025):* Revenue per employee increased from **$0.094M** to **$0.124M** = **+32.4%**.
- *Pre-Period Average Check:* Relative to the full 2021–2023 pre-period average (**$0.130M**), the 2025 RPE (**$0.124M**) remains slightly lower (-4.3%) because 2021–2022 included unusually high pandemic-era refinancing activity and different workforce dynamics. The productivity evidence should therefore be characterized as **recovery from the 2023 trough and strong post-transition improvement**, rather than a complete restoration to peak historical levels.

### 6.6 Finding 6: Composite Index (Supplementary)

The Operational Leverage Index reaches **195.3** by 2025 (2023=100). This is retained as a compact summary visualization in the appendix but is **illustrative only** — it is author-constructed, equally weighted (comprising Revenue Growth, Revenue per Employee Growth, and Inverse Expense Ratio Indices), sensitive to the 2023 baseline, and not statistically validated. It is not used as primary evidence.

### 6.7 Finding 7: Descriptive Benchmark Comparison Against Rocket Mortgage

| Metric | Better Change | Rocket Change | Descriptive Differential |
|---|---|---|---|
| Expense Ratio | -1.099 | +0.199 | **-1.298** (Better improved more) |
| Profit Margin | +2.179 | -0.197 | **+2.376** (Better improved more) |
| Revenue per Employee | -0.006 | -0.072 | **+0.066** (Better declined less) |

Better's trajectory is directionally superior across all metrics. *Critical limitation:* This is a descriptive benchmark comparison rather than a formal counterfactual. Rocket is substantially larger (~40× revenue), has a diversified business model (servicing portfolio), and its 2025 data reflects the Mr. Cooper acquisition which distorts per-employee metrics.

### 6.8 Alternative Baseline Checks

To ensure findings are not artifacts of trough-year baseline selection, three baseline comparisons are provided:

#### 2023 → 2025 (Trough-to-Post Recovery)

| Metric | 2023 | 2025 | Change |
|---|---|---|---|
| Revenue | $76.8M | $164.9M | +114.6% |
| Total Expenses | $368.1M | $330.7M | -10.2% |
| Expense Ratio | 4.79 | 2.01 | -58.0% |
| RPE | $0.094M | $0.124M | +32.4% |
| Net Income | -$536.4M | -$165.9M | 69.1% loss reduction |

This captures recovery from Better's post-rate-hike trough. Improvements appear largest here due to the depressed 2023 starting point.

#### 2024 → 2025 (Post-Transition Comparison)

| Metric | 2024 | 2025 | Change |
|---|---|---|---|
| Revenue | $108.5M | $164.9M | +52.0% |
| Total Expenses | $313.9M | $330.7M | +5.3% |
| Expense Ratio | 2.89 | 2.01 | -30.6% |
| RPE | $0.087M | $0.124M | +42.9% |
| Net Income | -$206.3M | -$165.9M | 19.6% loss reduction |

This comparison is especially relevant because 2024 is the Betsy transition year and 2025 is the first full post-Betsy year. Revenue grew 52.0% while expenses grew only 5.3% — a ratio of approximately 10:1, which is directionally consistent with operational leverage. RPE improved 42.9%, the strongest single-year productivity gain in the dataset. This comparison reduces, but does not eliminate, the base-effect problem of using 2023.

#### 2021–2023 Pre-Period Average → 2025

| Metric | Pre-Avg | 2025 | Change |
|---|---|---|---|
| Revenue | $551.6M | $164.9M | -70.1% |
| Total Expenses | $1,035.4M | $330.7M | -68.1% |
| Expense Ratio | 3.10 | 2.01 | -35.4% |
| RPE | $0.130M | $0.124M | -4.3% |
| Net Income | -$571.6M | -$165.9M | 71.0% loss reduction |

This reveals that 2025 revenue remains well below the pre-period average, which was inflated by 2021 pandemic-era levels ($1,200M). However, the Expense Ratio improved substantially from the pre-period average (3.10→2.01), and net losses narrowed by 71%. RPE is slightly below the pre-period average, confirming that the +32.4% improvement is a recovery-from-trough effect.

---

## 7. Interpretation in Relation to Research Questions

### 7.1 Contribution to RQ1 (Indirect)

The financial analysis contributes only **indirectly** to RQ1. It mainly supports RQ2. For RQ1:

1. **Restructuring context:** The financial data shows the 2022–2023 workforce reduction (10,400→820) and the severe financial pressure that made AI deployment both necessary and possible. This contextualizes the organizational prerequisites discussed in the qualitative case study.
2. **Scale of technology investment:** The financial data contextualizes the scale and cost of Better's technology-heavy operating model, but it does not directly quantify Tinman-specific investment. Cumulative losses include market losses, restructuring costs, compensation, marketing, SPAC-related expenses, and many other items beyond platform development. Evidence for Tinman as Betsy's architectural prerequisite should come primarily from management disclosures, case documentation, and the qualitative case study rather than from cumulative losses alone.
3. **Scalability evidence:** Post-Betsy, headcount grew 62% while revenue grew 114.6% — consistent with the thesis argument that the Tinman + Betsy architecture enables scaling without proportional human capital investment.

### 7.2 Contribution to RQ2 (Primary)

| Dimension | Evidence | Strength | Notes |
|---|---|---|---|
| Operational Efficiency | Expense Ratio -58% (2023→2025); -30.6% (2024→2025) | **Strong** | Strongest using 2024→2025 comparison |
| Revenue/Growth | +114.6% recovery (2023→2025); +52.0% (2024→2025) | **Strong** | Confounded by market recovery |
| Productivity/Scalability | RPE +42.9% (2024→2025); but -4.3% vs pre-avg | **Moderate** | Recovery from trough, not full restoration |
| Financial Performance | Losses reduced 69.1%; still unprofitable | **Moderate** | Multiple factors; trajectory is positive |
| Customer Experience | Not directly measured here; see NLP report | **Indirect** | NPS (39→64) is management-reported |

### 7.3 The Attribution Challenge

The data cannot isolate Betsy's specific contribution from: (1) macroeconomic mortgage market recovery, (2) prior workforce restructuring (2022–2023), (3) product mix changes (NEO channel launched January 2025), (4) Tinman platform improvements beyond Betsy, (5) base effects from the 2023 trough. The thesis addresses this via a counterfactual argument: if improvements were solely from cost-cutting, we would expect stagnant or declining revenue — but revenue grew 52.0% in the 2024→2025 window alongside efficiency gains, suggesting partial labor-output decoupling. This reasoning provides **associative support** but does not constitute causal proof.

---

## 8. Figures, Tables, and Outputs

### 8.1 Generated Figures

| Figure Filename | Title | Type | What It Shows | Key Takeaway |
|---|---|---|---|---|
| **[fig_fin_better_financial_trajectory_clean.png](file:///outputs/figures/financial/fig_fin_better_financial_trajectory_clean.png)** | Better.com Core Financial Trajectory, 2021–2025 | Three-panel line chart | Better's Revenue, Total Expenses, and Net Income with period shading and data labels | Better's revenue recovery and expense containment are visible; 2021 is highlighted as a pandemic-inflated peak |
| **[fig_fin_headcount_productivity_clean.png](file:///outputs/figures/financial/fig_fin_headcount_productivity_clean.png)** | Better.com Headcount and Revenue per Employee, 2021–2025 | Two-panel line chart | Better's headcount and labor productivity over time, with period shading and annotations | Headcount compression is managed; RPE recovers in 2025 but remains below the pre-period average |
| **[fig_fin_expense_ratio_cashflow_clean.png](file:///outputs/figures/financial/fig_fin_expense_ratio_cashflow_clean.png)** | Better.com Expense Intensity and Operating Cash Flow Margin, 2021–2025 | Two-panel chart (Panel A: Bar, Panel B: Line) | Expense Ratio bars and Operating Cash Flow Margin line without dual-axis clipping | Simultaneous expense ratio improvement post-transition; cash flow margin remains highly volatile |
| **[fig_fin_benchmark_productivity_expense_ratio_clean.png](file:///outputs/figures/financial/fig_fin_benchmark_productivity_expense_ratio_clean.png)** | Benchmark Comparison: Revenue per Employee and Expense Ratio | Two-panel line chart | Better vs Rocket productivity and expense ratio over time with scaling cautions | Better improves post-2023; Rocket's per-employee metrics are distorted in 2025 by scale acquisitions |
| **[fig_fin_profitability_cashflow_benchmark_clean.png](file:///outputs/figures/financial/fig_fin_profitability_cashflow_benchmark_clean.png)** | Profitability and Operating Cash Flow Margins: Better.com vs Rocket Mortgage | Two-panel line chart | Profit margins and cash flow margins benchmarked against Rocket with zero reference lines | Better's margins narrow toward breakeven; Rocket remains a descriptive, scaled benchmark |
| **[appendix_fig_fin_operational_leverage_index.png](file:///outputs/figures/financial/appendix_fig_fin_operational_leverage_index.png)** | Supplementary Operational Leverage Composite Index, 2022–2025 (Appendix Only) | Dual-axis line chart | Revenue Index and equally-weighted custom Operational Leverage Index (2023=100) | Illustrative composite metric indicating post-2023 leverage; moved to appendix due to baseline sensitivity |

### 8.2 Figure Interpretation Notes

**Better.com Core Financial Trajectory (fig_fin_better_financial_trajectory_clean.png)** presents the primary financial evidence. It highlights the massive post-2021 contraction and the subsequent 2023→2025 recovery. Shading defines the Pre-Betsy, Transition, and Post-Betsy periods, demonstrating that expense discipline was maintained during the 2025 revenue scaling.

**Better.com Expense Intensity and Operating Cash Flow Margin (fig_fin_expense_ratio_cashflow_clean.png)** replaces previous dual-axis charts with a clean, two-panel layout to prevent clipping or visual confusion. Panel A shows that Better's expense ratio declined substantially post-transition, indicating efficiency gains. Panel B shows that while operating cash flow margin improved, it remains volatile and sensitive to working capital timing.

### 8.3 Generated Tables

| Table | Content | Purpose |
|---|---|---|
| Period Summary | Pre-Average, Transition, Post values with changes | Core pre/post comparison |
| Descriptive benchmark comparison | Better vs Rocket Pre→Post differences | Benchmark-adjusted descriptive evidence |
| RQ2 Findings | Programmatically generated thesis-ready findings | Direct thesis integration |

### 8.4 Saved Output Files

All cleaned, thesis-ready figures are saved with high DPI (300) to the relative output directory:
`outputs/figures/financial/`

These files are fully generated and ready for direct insertion into Chapter 5 of the thesis.

---

## 9. Metric Traceability and Evidence Strength

| Metric | Value / Period | Source Document | Data Method | Line-Item Definition | Role in Thesis | Reliability |
|---|---|---|---|---|---|---|
| Revenue $76.8M (2023) | Better 2024 10-K | Reported/audited | "Total net revenue" from Statements of Operations | RQ2: Revenue baseline | High |
| Revenue $108.5M (2024) | Better 2025 10-K | Reported/audited | "Total net revenue" | RQ2: Transition year | High |
| Revenue $164.9M (2025) | Better 2025 10-K | Reported/audited | "Total net revenue" | RQ2: Post-Betsy revenue | High |
| Total Expenses $368.1M (2023) | Better 2024 10-K | Reported/audited | Standardized total expense base (see §4.4) | RQ2: Expense baseline | High (comparability caveat) |
| Total Expenses $330.7M (2025) | Better 2025 10-K | Reported/audited | Standardized total expense base | RQ2: Post-Betsy expenses | High (comparability caveat) |
| Net Income -$536.4M (2023) | Better 2024 10-K | Reported/audited | "Net loss" from Statements of Operations | RQ2: Loss baseline | High |
| Net Income -$165.9M (2025) | Better 2025 10-K | Reported/audited | "Net loss" | RQ2: Post-Betsy losses | High |
| Employees 820 (2023) | Better 2024 10-K Item 1 | Self-reported | Approximate headcount from Item 1 | RQ2: Headcount baseline | Medium-High (unaudited) |
| Employees 1,329 (2025) | Better 2025 10-K Item 1 | Self-reported | Approximate headcount | RQ2: Post-Betsy headcount | Medium-High (unaudited) |
| Employees 10,400 (2021) | Better S-1 filing | Self-reported | Historical headcount | RQ1: Pre-restructuring context | Medium-High (unaudited) |
| Expense Ratio 4.79→2.01 | Calculated | Author-calculated | Total_Expenses / Revenue | RQ2: Cost intensity | High (deterministic) |
| Expense Ratio 2.89→2.01 | Calculated (2024→2025) | Author-calculated | Total_Expenses / Revenue | RQ2: Post-transition efficiency | High (deterministic) |
| RPE $0.094→$0.124M | Calculated (2023→2025) | Author-calculated | Revenue / Employees | RQ2: Labor productivity | High (deterministic) |
| RPE $0.087→$0.124M | Calculated (2024→2025) | Author-calculated | Revenue / Employees | RQ2: Post-transition productivity | High (deterministic) |
| RPE $0.130→$0.124M | Calculated (pre-avg→2025) | Author-calculated | Revenue / Employees | RQ2: Full-period comparison | High (deterministic) |
| Profit Margin -6.98→-1.01 | Calculated | Author-calculated | Net Income / Revenue | RQ2: Profitability trajectory | High (deterministic) |
| OLI 195.3 (2025) | Composite | Author-constructed | Average of 3 normalized indices (2023=100) | Supplementary visualization | **Low** (illustrative only) |
| NPS 39→64 | Better earnings transcript | Management-reported | Not in annual dataset; from earnings call | RQ2: Customer experience | Medium (unaudited, self-reported) |
| CTO ~$4,900 | Author estimate | Author-estimated | Total Expenses / estimated funded loans | RQ2: Unit economics | Medium (proxy; depends on loan count) |
| MBA industry CTO $11,250 | MBA Quarterly Report | Third-party reported | Industry benchmark | RQ2: External benchmark | High |
| All Rocket financials | Rocket 10-K filings | Reported/audited | Various income/balance sheet lines | Benchmark comparison | High |

---

## 10. Thesis Integration Map

| Finding | Evidence Strength | Relevant RQ | Thesis Section | Suggested Use | Causal Caution |
|---|---|---|---|---|---|
| Revenue recovery +114.6% (2023→2025) | Strong (audited) | RQ2 | §5.4.1 | Primary revenue evidence | Confounded by market recovery and base effects; present with 2024→2025 alongside |
| Revenue growth +52.0% (2024→2025) | Strong (audited) | RQ2 | §5.4.1 | Post-transition revenue growth | Cleaner but still not isolating Betsy from other factors |
| Expense decline -10.2% (2023→2025) | Strong (audited) | RQ2 | §5.4.1 | Cost discipline during growth | Pre-existing restructuring contributed |
| Expense Ratio -30.6% (2024→2025) | Strong (calculated) | RQ2 | §5.4.2 | Core operational leverage indicator | Revenue-driven; cross-company comparability limited |
| Net loss reduction 69.1% | Strong (audited) | RQ2 | §5.4.1 | Trajectory toward profitability | Multiple factors; AI is one of several drivers |
| RPE +42.9% (2024→2025) | Moderate-Strong | RQ2 | §5.4.1 | Strongest single-year productivity gain | Recovery from trough; RPE still below pre-period avg |
| RPE -4.3% vs pre-period avg | Moderate (sobering) | RQ2 | §5.4.1 | Honest qualification of productivity claim | Pandemic-era baseline was unusually high |
| Descriptive benchmark: Better > Rocket | Moderate (descriptive) | RQ2 | §5.4.3 | Directional evidence beyond market recovery | Not a formal counterfactual; Rocket is a directional benchmark, not a counterfactual |
| OLI reaches 195.3 | **Illustrative only** | RQ2 | §5.4.4 | Supplementary composite visualization | Not statistically weighted; sensitive to baseline |
| Headcount +62% vs Revenue +114.6% | Moderate-Strong | RQ2 | §5.4.5 | Scalability evidence | Hiring reflects multiple strategic decisions |
| Workforce reduction 10,400→820 | Strong (audited) | RQ1 (indirect) | §7.1 | Organizational restructuring context | Not a measure of AI impact; contextual only |
| NPS 39→64 | Medium (management) | RQ2 | §5.3.3 | Customer experience; triangulate with NLP | Unaudited, self-reported; potential bias |
| CTO ~$4,900 vs MBA $11,250 | Medium (estimated) | RQ2 | §5.3.1 | Unit economics; industry comparison | Author-estimated proxy; dependent on loan count |

---

## 11. Methodological Limitations

### 11.1 Sample Size and Statistical Power

The dataset contains **5 annual observations for Better** and **8 for Rocket**. This is insufficient for formal statistical inference. All comparisons are descriptive. Pearson correlations, if computed, would have n≤5 and are **statistically non-inferential**.

### 11.2 Annual Granularity vs. Quarterly Thesis Timeline

Betsy launched on October 17, 2024 — late Q4. Annual data cannot distinguish between pre-Betsy and post-Betsy effects within 2024. The thesis draft uses quarterly operating metrics (Q3 2023–Q2 2025) for launch-aligned analysis. The annual SEC analysis provides audited background evidence for the broader financial trajectory, while quarterly metrics provide the more precise Betsy-aligned view.

### 11.3 Causal Identification

The study design is observational and retrospective. No randomization, natural experiment, or formal quasi-experimental identification strategy is employed. The descriptive benchmark comparison against Rocket Mortgage provides directional evidence but does not constitute formal causal identification because:
- Better and Rocket differ in scale (~40× revenue difference)
- Business models differ (Better is digital-first; Rocket has diversified servicing and the Mr. Cooper acquisition)
- Treatment timing is imprecise at annual granularity
- Multiple concurrent changes at Better prevent isolation of Betsy's effect

### 11.4 Self-Reporting Bias

Employee counts, NPS scores, and management commentary on Betsy's performance derive from Better.com's own disclosures. Financial figures are externally audited, but operational metrics and AI-specific claims are not independently verified.

### 11.5 Attribution Problem

Better's financial improvements reflect **multiple simultaneous changes**: workforce reduction (2022–2023), market recovery, Tinman platform maturation, Betsy deployment, NEO channel launch (January 2025), ElevenLabs partnership (June 2025), and product mix evolution. Disentangling Betsy's specific contribution from public annual data alone is not possible.

### 11.6 Cross-Company Comparability

`Total_Expenses` composition differs between Better and Rocket. Cross-company ratio comparisons (Expense Ratio, RPE) should be interpreted directionally rather than as precise like-for-like comparisons.

### 11.7 Baseline Sensitivity

Results vary substantially depending on baseline choice. The 2023 trough baseline produces the most dramatic improvement figures. The 2024→2025 comparison is more conservative and more defensible for post-Betsy claims. The pre-period average comparison reveals that RPE has not yet recovered to its 2021–2022 levels.

### 11.8 Survivorship and Selection Bias

Better.com is selected as a case study precisely because it represents an advanced AI implementation — this creates positive selection bias. Findings may not generalize.

---

## 12. Contribution to the Thesis

### 12.1 Empirical Foundation

This financial analysis provides the **quantitative empirical backbone** of the thesis's RQ2 argument. It establishes, through audited SEC data, that Better.com's post-Betsy period exhibits financial characteristics consistent with AI-enabled operational leverage: simultaneous revenue recovery, expense control, and productivity improvement.

### 12.2 Triangulation Role

Together with the NLP analysis (`nlp_project_report.md`), this creates a **multi-method triangulation**:
- **Financial analysis** → operational efficiency, cost, revenue, and productivity dimensions
- **NLP analysis** → customer experience dimension through independent review data
- **Case study qualitative evidence** (Chapter 4) → integration process, organizational context, and Betsy deployment details

### 12.3 Design Pattern Grounding

The financial data informs the VoiceAI-Finance (VAF) Design Pattern (Chapter 6) by providing outcome evidence for the pattern's Phase 5 (Performance Measurement) KPIs.

---

## 13. Draft Thesis Integration Paragraphs

### 13.1 Operational Leverage Evidence

The longitudinal financial analysis of Better.com's SEC filings from 2021 to 2025 provides descriptive evidence consistent with AI-enabled operational leverage in the post-Betsy period. Total revenue increased from $76.8M in 2023 to $164.9M in 2025, representing a 114.6% recovery, while total operating expenses simultaneously declined from $368.1M to $330.7M — a reduction of 10.2% in absolute terms. This pattern, in which revenue growth substantially outpaces expense growth, is consistent with operational leverage. The Expense Ratio declined from 4.79 to 2.01 over this period, indicating that each dollar of revenue requires significantly less operational expenditure to generate. However, 2023 was a depressed market-trough year, and some of this improvement reflects recovery from an abnormally low base. The more conservative 2024-to-2025 comparison — where revenue grew 52.0% while expenses grew only 5.3% — provides cleaner post-transition evidence, reducing though not eliminating the base-effect concern.

### 13.2 Labor Productivity and Scalability

The revenue-per-employee metric offers partial evidence for the productivity dimension of business value. Revenue per employee increased from $0.087M in 2024 to $0.124M in 2025, a gain of 42.9% — the strongest single-year productivity improvement in the dataset. This occurred while headcount grew modestly from 1,250 to 1,329 employees (+6.3%), compared to revenue growth of 52.0%, an asymmetry that is directionally consistent with AI-driven labor substitution for routine tasks. However, relative to the full 2021–2023 pre-period average of $0.130M, the 2025 RPE of $0.124M remains slightly lower because 2021–2022 included unusually high pandemic-era refinancing activity and different workforce dynamics. The productivity evidence should therefore be characterized as **recovery from the 2023 trough and strong post-transition improvement**, rather than a full restoration to peak historical productivity.

### 13.3 Benchmark Comparison

A descriptive benchmark comparison against Rocket Mortgage provides directional evidence that Better's improvements exceed general market recovery effects. Better's Expense Ratio improved by 1.099 points compared to a 0.199-point deterioration at Rocket, yielding a descriptive differential of -1.298 in Better's favor. Similarly, Better's Profit Margin improved by 2.179 points compared to Rocket's 0.197-point decline. These differentials suggest that factors specific to Better — including but not limited to the Betsy/Tinman AI operating model — contributed to a structurally different cost trajectory. However, this comparison is descriptive rather than causal: Rocket and Better differ substantially in scale, business model, and strategic context, and Rocket's 2025 data reflects the Mr. Cooper acquisition, which distorts per-employee comparisons. The benchmark comparison should therefore be interpreted as providing **directional support** rather than controlled causal evidence.

### 13.4 Interpretation Boundaries and Synthesis

The annual SEC-based financial analysis shows that Better.com's post-Betsy period is characterized by revenue recovery, improved expense intensity, narrowing losses, and partial labor-productivity recovery. These patterns are directionally consistent with AI-enabled operational leverage, especially when triangulated with quarterly management disclosures on Betsy's interaction volume (115,000–700,000 monthly calls) and conversion impact (+30%). However, because the evidence is annual, observational, and affected by market recovery, prior restructuring, product mix changes, and platform improvements beyond Betsy, the findings should be interpreted as **associative support rather than causal proof**. The financial findings are strongest for RQ2's operational efficiency and revenue dimensions, moderate for the productivity dimension, and indirect for customer experience (which is addressed by the companion NLP analysis). Formal causal identification would require granular sub-annual data and econometric methods that are beyond the scope of this study.

---

## References

### Primary SEC Filings
- Better Home & Finance Holding Company. (2024). Annual Report on Form 10-K for fiscal year ended December 31, 2023. SEC EDGAR.
- Better Home & Finance Holding Company. (2025). Annual Report on Form 10-K for fiscal year ended December 31, 2024. SEC EDGAR.
- Better Home & Finance Holding Company. (2026). Annual Report on Form 10-K for fiscal year ended December 31, 2025. SEC EDGAR.
- Better Home & Finance Holding Company. (2021). Registration Statement on Form S-1. SEC EDGAR.
- Rocket Companies, Inc. (2021). Annual Report on Form 10-K for fiscal year ended December 31, 2020. SEC EDGAR. (Also source for 2018–2019 historical comparatives.)
- Rocket Companies, Inc. (2022). Annual Report on Form 10-K for fiscal year ended December 31, 2021. SEC EDGAR.
- Rocket Companies, Inc. (2023). Annual Report on Form 10-K for fiscal year ended December 31, 2022. SEC EDGAR.
- Rocket Companies, Inc. (2024). Annual Report on Form 10-K for fiscal year ended December 31, 2023. SEC EDGAR.
- Rocket Companies, Inc. (2025). Annual Report on Form 10-K for fiscal year ended December 31, 2024. SEC EDGAR.
- Rocket Companies, Inc. (2026). Annual Report on Form 10-K for fiscal year ended December 31, 2025. SEC EDGAR.

### Supplementary Sources
- Better Home & Finance Holding Company. (2024, October 17). Better launches Betsy™, the first voice-based AI Loan Assistant for the U.S. mortgage industry [Press release]. https://ir.better.com
- Better Home & Finance Holding Company. (2025). Earnings call transcripts, Q1–Q4 2025. S&P Global Market Intelligence.
- ElevenLabs. (2026, February). Better Home & Finance: Automating mortgage origination with AI voice agents [Case study via BusinessWire].
- Mortgage Bankers Association. (2024). Quarterly Mortgage Bankers Performance Report. MBA Publications.

### Project Files Referenced
- `08_Code/Data Extraction code/extract_pdf_texts.py` — PDF text extraction pipeline (pdfplumber)
- `08_Code/Data Extraction code/extract_s1.py` — S-1 auxiliary extraction script (pypdf)
- `08_Code/Data Extraction code/build_dataset_v4.py` — Dataset construction script (v6)
- `08_Code/Data Extraction code/financial_dataset_documentation.md` — Dataset audit documentation
- `Data/financial_dataset_annual.csv` — Final longitudinal dataset (13 rows, 15 columns)
- `08_Code/financial_metric_Analysis.ipynb` — RQ2 Empirical Support Notebook
