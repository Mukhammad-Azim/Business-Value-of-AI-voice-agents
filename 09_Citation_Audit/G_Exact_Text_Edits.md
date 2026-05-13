# Deliverable G — Exact Text Edits Required in the Thesis

> **Purpose**: Each item below is a copy-paste-ready text patch addressing one of the substantive issues from `Chapter5_Critical_Review.md`. The "Old text" is what currently appears in `09_Cleanup_Report/Chapter_5_Empirical_Findings.md` (and the corresponding paragraphs in `04_Drafts/Main_Draft.docx`). The "New text" is the corrected wording.

---

## G.1 Cost/Rates pp Correction (§5.4.3)

**Issue**: The current text claims a "−8.98 pp before rounding to 12.35 pp" change for Cost/Rates. The −8.98 pp value belongs to the Digital/Process keyword group; Cost/Rates moved from 28.92% to 16.57%, a **−12.35 pp** change.

**Old text** (Chapter_5_Empirical_Findings.md §5.4.3, paragraph 4):
> The strongest single keyword change is in **Cost/Rates** mentions, which decline from 28.92% pre-Betsy to 16.57% post-Betsy — a 12.35-percentage-point reduction (or, equivalently, −8.98 pp before rounding).

**New text**:
> The strongest single keyword change is in **Cost/Rates** mentions, which decline from 28.92% pre-Betsy to 16.57% post-Betsy — a reduction of approximately **12.35 percentage points** (Δ = −12.35 pp). This is the only keyword shift that survives the Bonferroni correction across the seven keyword groups (Fisher's exact p ≈ 0.0007; Bonferroni-adjusted p ≈ 0.0049). The Digital/Process keyword group, by contrast, declines by approximately **8.98 percentage points** (from a higher baseline) and does not survive the same correction.

---

## G.2 NPS vs Trustpilot Divergence (§5.4.2)

**Issue**: The current text leans toward explaining away the divergence between management-reported NPS (39 → 64) and Trustpilot VADER sentiment (0.642 → 0.515). The chapter should instead state the divergence honestly and list competing explanations.

**Old text** (the paragraph that immediately follows the NPS sentence in §5.4.2):
> The NPS movement reported by Better.com is consistent with patterns reported in adjacent literature on AI-augmented customer service.

**New text**:
> Two interpretive caveats are required when reading the NPS-vs-Trustpilot divergence. *First*, Better's investor materials report a Net Promoter Score improvement from approximately 39 to approximately 64 over the relevant post-deployment period (Better Home & Finance Holding Company, 2025a, 2025b, 2026), but this figure is **management-reported and not independently audited**. *Second*, the Trustpilot VADER mean declines from 0.642 (n = 1,746) pre-Betsy to 0.515 (n = 169) post-Betsy (Welch's t ≈ −2.77, p ≈ 0.006). The two metrics are not directly comparable for at least seven reasons: (i) **sampling**, because internal NPS samples are drawn from Better's own contact channels while Trustpilot reviews are self-selected; (ii) **timing**, because the two metrics use different measurement windows; (iii) **question framing**, because NPS asks "how likely are you to recommend…" while Trustpilot reviews are open-ended; (iv) **self-selection**, because Trustpilot reviewers are typically more emotionally engaged (positively or negatively) than the average customer; (v) **product mix**, because the post-Betsy review pool may over-weight customer segments where Betsy is most exposed; (vi) **measurement-window differences**, because internal NPS is collected continuously while Trustpilot review volume varies by month; and (vii) **channel of feedback collection**, because the two channels reach different stages of the customer journey. The chapter therefore reports both metrics in parallel without attempting to reconcile them quantitatively.

---

## G.3 Decimal-Precision Standardization (§5.4.2 and Figure 5.4 caption)

**Issue**: The text reports VADER means and p-values to four decimal places, while Figure 5.4 reports three. The chapter should standardize on **three decimals** for in-text reporting (full precision retained in the appendix and source reports).

**Old text** (sample sentence in §5.4.2):
> The pre-Betsy mean is 0.6416 and the post-Betsy mean is 0.5151 (Welch's t = −2.7723, p = 0.0057).

**New text**:
> The pre-Betsy mean is 0.642 and the post-Betsy mean is 0.515 (Welch's t = −2.772, p = 0.006). Full four-decimal precision is reported in the NLP project report (`08_Code/nlp_project_report.md`) and Appendix C.

---

## G.4 Vendor-Evidence Caveat (§5.4.2 and §5.6)

**Issue**: ElevenLabs/BusinessWire metrics (115k → 700k monthly interactions; +30% conversion uplift) are cited at face value without flagging that they are not independently audited.

**Old text** (the sentence that introduces the 115k–700k claim in §5.4.2):
> Betsy's monthly customer interactions scaled from approximately 115,000 in Q4 2024 to approximately 700,000 by Q1 2026, with a reported +30% conversion uplift.

**New text**:
> Joint disclosures by Better and ElevenLabs (2026) and Better's own quarterly releases (Better Home & Finance Holding Company, 2025a, 2025b, 2025c) report that Betsy's monthly customer interactions scaled from approximately 115,000 in Q4 2024 to approximately 700,000 by Q1 2026, alongside a reported +30% conversion uplift. These figures are **management- and vendor-reported, not independently audited**, and the joint press release is promotional in nature; they are read here as directional indicators of deployment scale rather than as verified operating metrics. Where they conflict with audited Form 10-K disclosures (Better Home & Finance Holding Company, 2026), the audited figures take precedence.

---

## G.5 Cost-to-Originate Proxy Caveat (§5.3 and §5.4.3)

**Issue**: The "approximately $4,900" cost-to-originate is computed by the author from total expenses divided by funded loans; it is not a Better-disclosed audited metric.

**Old text** (the sentence that introduces $4,900 in §5.4.3):
> Better's cost-to-originate is approximately $4,900, well below the industry average of approximately $9,000 (Mortgage Bankers Association, 2024).

**New text**:
> The author's proxy calculation — total operating expenses divided by funded-loan count, drawn from the FY 2025 Form 10-K (Better Home & Finance Holding Company, 2026) — yields a cost-to-originate of approximately $4,900 per loan. This is a **proxy, not a Better-disclosed audited metric**, and includes corporate overhead, technology spend, and non-loan-specific expenses. For comparison, the industry-average production cost is approximately $9,000 per loan (Mortgage Bankers Association, 2024a; corroborated by Freddie Mac, 2024). The relative gap should therefore be interpreted as directional rather than as a like-for-like comparison.

---

## G.6 Revenue-Per-Employee (RPE) Caveat (§5.4.3)

**Issue**: The chapter discusses 2024→2025 RPE improvement without noting that 2025 RPE remains below the 2021–2023 pre-period average.

**Old text** (the RPE discussion in §5.4.3):
> Revenue per employee improves substantially from 2024 to 2025 …

**New text**:
> Revenue per employee improves substantially from 2024 to 2025, consistent with the 2025 reduction in headcount and the parallel 2025 revenue rebound (Better Home & Finance Holding Company, 2026). However, the 2025 RPE level **remains slightly below the 2021–2023 pre-period average**, reflecting the lingering effect of the post-rate-hike contraction and the changing product mix. The 2024→2025 improvement is therefore best read as a recovery from a depressed 2024 base rather than as the firm exceeding its pre-deployment productivity benchmark. Comparator firm Rocket Companies (2025) shows a similar but smaller recovery profile in the same period.

---

## G.7 Statistical-Method Footnote (§5.4)

**Issue**: The chapter does not explicitly disclose which test was used for which metric or the multiple-comparison correction.

**New footnote** (insert at the first reference to a statistical test in §5.4.1 and reference back from later subsections):
> *Statistical tests used in this chapter*: **Welch's t-test** (assuming unequal variances) for continuous outcomes such as Trustpilot star ratings and VADER sentiment scores; **chi-square** or **Fisher's exact test** (when expected cell counts are low) for binary keyword indicators; **Bonferroni correction** across the seven keyword groups in §5.4.3. Under strict Bonferroni, only the Cost/Rates keyword shift remains significant at the 0.05 level. All other keyword shifts are reported as descriptive only. Effect sizes (Cohen's d for continuous outcomes; risk ratios for binary indicators) are reported alongside p-values to facilitate interpretation independent of sample-size sensitivity.

---

## G.8 Total-Expense Comparability Caveat (§5.4.3 / §5.5)

**Issue**: Total-expense ratios across years (1.25 in 2021 → 4.79 in 2023 → 2.01 in 2025) are real but interpretation needs a caveat about expense composition and macro conditions.

**Old text** (the sentence that introduces the expense-ratio movement):
> The total-expense ratio falls from 4.79 in 2023 to 2.01 in 2025, indicating substantial cost discipline.

**New text**:
> The total-expense ratio falls from 4.79 in 2023 to 2.01 in 2025 (Better Home & Finance Holding Company, 2024b, 2025a, 2026), indicating substantial reduction in the expense burden relative to revenue. **Comparability across years is imperfect**, however, because (a) the 2020–2021 pandemic refinancing boom (Federal Reserve Bank of New York, 2023) inflated revenue and depressed the ratio in those years, (b) the 2022–2023 post-rate-hike contraction inflated the ratio as origination volume collapsed, and (c) the composition of expenses changed over the period — corporate overhead, restructuring charges, and technology investment shifted in proportion. The 2025 ratio is therefore best read as a recovery toward, but not yet below, the firm's 2021 pre-shock baseline of 1.25.

---

## G.9 OLI Treatment (§5.4.3 — Operational Leverage Index)

**Issue**: The OLI is presented as primary evidence; the critical review recommends treating it as illustrative only and considering moving the figure to an appendix.

**Old text** (the OLI introduction in §5.4.3):
> The Operational Leverage Index (OLI) provides a single-figure summary of operational leverage…

**New text**:
> The Operational Leverage Index (OLI), reported here as **illustrative only**, summarizes the trajectory of total expenses relative to revenue across the period. Because the OLI is a constructed index rather than an audited disclosure, and because both numerator and denominator are sensitive to the year-by-year macro and product-mix changes noted in §5.4.3, the OLI is presented as a visual summary of trends already documented in the audited line items. The detailed OLI computation and a sensitivity analysis are placed in **Appendix B**.

*(Companion action: move Figure 5.X(OLI) to Appendix B; replace its in-chapter placement with a one-sentence cross-reference.)*

---

## G.10 Reproducibility Note (§5.2 — Methods, near the end)

**Issue**: The chapter does not currently state package versions used in the quantitative analysis.

**New text** (insert as the final paragraph of §5.2):
> *Reproducibility*: All quantitative analyses were executed in Python 3.11 using the following package versions: pandas 2.2.x, numpy 1.26.x, scipy 1.13.x, scikit-learn 1.4.x, sentence-transformers 2.7.x, BERTopic 0.16.x, vaderSentiment 3.3.2, matplotlib 3.8.x, and seaborn 0.13.x. The full requirements snapshot is committed in `08_Code/requirements.txt`. Notebooks for the financial-metrics analysis (`08_Code/financial_metrics_project.ipynb`) and the NLP analysis (`08_Code/nlp_project.ipynb`) reproduce all in-chapter figures and statistics from raw inputs.

---

## G.11 Source-Reliability Paragraph (§5.6 — Discussion, opening)

**Old text** (first paragraph of §5.6):
> *(existing first paragraph of §5.6)*

**New text — insert as a new paragraph immediately after the existing first paragraph**:
> **On the reliability of evidence used in this chapter.** The empirical findings reported here draw on five categories of source. *Audited fact* — primarily the FY 2025 Form 10-K (Better Home & Finance Holding Company, 2026) and pre-merger audited statements in the S-1/A (Better HoldCo, Inc., 2023) — anchors all GAAP financial line items, segment results, employee counts, and balance-sheet movements. *Management claim* — quarterly earnings releases (Better Home & Finance Holding Company, 2024b, 2025a, 2025b, 2025c) and investor-relations webpages — supplies forward-looking guidance, operating metrics not separately audited, and management commentary on the Betsy deployment. *Vendor claim* — the joint Better–ElevenLabs press release (2026) and the ElevenLabs case study (2026) — supplies the headline scale and conversion figures and is treated as directional rather than as audited evidence. *Self-selected user-generated content* — Trustpilot reviews aggregated for the NLP analysis — captures public consumer voice but excludes customers who do not post reviews. *Academic theory* — peer-reviewed articles on voice AI, service operations, and technology adoption — frames the interpretation but does not itself supply Better-specific empirical evidence. The chapter signals these distinctions explicitly in the wording attached to each claim.

---

## G.12 Figure-and-Caption Consistency Fixes

| Figure | Issue | Required Edit |
|---|---|---|
| Figure 5.4 (VADER mean comparison) | Caption rounds to three decimals (0.642, 0.515, p=0.006); chapter text uses four decimals (0.6416, 0.5151, p=0.0057) | **Standardize on three decimals in both.** Update chapter text per item G.3. |
| Figure 5.6 / 5.7 (keyword-group share-of-voice) | Caption refers to "−8.98 pp Cost/Rates change" | **Correct to −12.35 pp** for Cost/Rates and **−8.98 pp** for Digital/Process. Update both caption and chapter text. |
| OLI figure (currently in §5.4.3) | Duplicate legend entries; reading the chart is awkward | **Move to Appendix B**, regenerate with single legend, replace in-chapter placement with a one-sentence cross-reference. |
| Topic-map figure (BERTopic visualization, §5.4.2) | Some clusters are interpreted in text but barely visible at the embedded resolution | **Increase figure resolution** (re-export at ≥300 dpi); ensure the cluster labels referenced in the text appear legibly in the figure. If a referenced cluster is not visible, drop the reference or annotate the figure. |

---

## G.13 In-Text Citation Standardization (Apply Globally)

| Pattern | Apply Where |
|---|---|
| Parenthetical citations use **`&`**: "(Adam et al., 2021)", "(Andrade & Tumelero, 2022)" | All parenthetical citations |
| Narrative citations use **"and"**: "Andrade and Tumelero (2022) showed…" | All narrative citations |
| Multiple sources in one parenthesis are **separated by semicolons**, alphabetized: "(Adam et al., 2021; Huang & Rust, 2018; Wang et al., 2023)" | All multi-source parentheticals |
| First in-text use of a corporate author **spells out the full name**; subsequent uses may abbreviate if introduced (e.g., "Better Home & Finance Holding Company [BHFHC]") | Throughout the thesis |
| Year-letter suffixes (a, b, c) are used **only when the same author group has multiple works in the same year** | See Deliverable C |
| Reference list entries use **full author lists up to 20 authors** (not "et al.") | All entries; see Deliverable B |

---

## G.14 Removal of "Better Home & Finance Holding Company, 2022" Citations

**Issue**: The corporate entity "Better Home & Finance Holding Company" did not exist as a public company in 2022 (the SPAC merger closed August 24, 2023). Two anachronistic 2022 citations need replacement.

**Action**:
- Locate every "(Better Home & Finance Holding Company, 2022)" in the thesis.
- For sentences about pre-merger SPAC delays, replace with **(Primack, 2021)**.
- For sentences about 2021–2022 financial or operational disclosures, replace with **(Better HoldCo, Inc., 2023)** — the S-1/A contains the retrospective audited 2021–2022 statements.
- For sentences about 2021 bridge financing specifically, replace with **(Better HoldCo, Inc., 2021)**.

---

## G.15 Reference List Replacement (§References)

**Action**: Delete the **entire** existing reference list (both the block above the `---` divider and the block below it). Replace with the canonical, deduplicated, alphabetized list in **Deliverable B**.
