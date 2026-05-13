# D. Chapter 5 Writing Skeleton

This is the *skeleton* requested by the cleanup brief. It is **not** a
draft of Chapter 5 — only the section structure, the questions each
subsection must answer, the indicators / values it should cite, and the
recommended figures. Each indicator below is already standardized in
Chapters 1–4 and the analytical reports, so Chapter 5 only needs to
narrate them.

The required final-interpretation paragraph (Task 20) is reproduced
verbatim at the end of this document so that Chapter 5's closing reads
exactly as the cleanup brief specifies.

---

## 5.1 Introduction to Empirical Findings
- Restate RQ1 and RQ2 verbatim.
- Explain the convergent parallel mixed-methods triangulation across:
  qualitative case study (Chapter 4), longitudinal SEC financial
  analysis, and computational NLP of Trustpilot reviews.
- Flag the central interpretive stance: triangulated evidence
  *consistent with* AI-enabled operational leverage, not proof of
  Betsy as the sole causal driver.

## 5.2 RQ1 — Integration of Betsy into Mortgage Origination
*(Primarily qualitative; values come from Chapter 4 and the case-study
data in `03_Case_Study_Data/`.)*

- 5.2.1 Tinman as architectural prerequisite
- 5.2.2 Betsy as voice / conversational layer
- 5.2.3 ElevenLabs as low-latency voice infrastructure (June 2025
        partnership)
- 5.2.4 Human-AI collaboration and escalation pattern
- 5.2.5 Compliance and controlled workflow

*No new financial / NLP numbers belong in 5.2.*

## 5.3 RQ2 — Operational and Financial Business Value
*(Primary source: `08_Code/financial_metrics_project_report.md`,
`Data/financial_dataset_annual.csv`.)*

### 5.3.1 Revenue Recovery
- Better.com revenue: 2023 $76.8 M → 2024 $108.5 M → 2025 $164.9 M
  (+52.0 % from 2024 to 2025).
- 2025 revenue still below pre-restructuring scale, but consistent
  with a recovery trajectory.
- **Figure:** `outputs/figures/financial/fig_fin_better_financial_trajectory_clean.png`.

### 5.3.2 Expense Intensity and Operational Efficiency
- Total Expenses 2023 $368.1 M → 2024 $313.9 M → 2025 $330.7 M
  (+5.3 % from 2024 to 2025).
- Expense Ratio 4.79 → 2.89 → 2.01.
- Frame Total Expenses as a "standardized total expense base /
  broad cost-intensity indicator".
- **Figure:** `outputs/figures/financial/fig_fin_expense_ratio_cashflow_clean.png`
  (Panel A primary; Panel B with cash-flow caution).

### 5.3.3 Loss Narrowing and Profitability Trajectory
- Net loss 2023 −$536.4 M → 2024 −$206.3 M → 2025 −$165.9 M
  (−19.6 % from 2024 to 2025).
- Profit margin trajectory still negative but improving.
- Use the "consistent with AI-enabled operational leverage" register.

### 5.3.4 Productivity and Scalability
- Revenue per Employee 2023 $0.094 M → 2024 $0.087 M → 2025 $0.124 M
  (+42.9 % from 2024 to 2025).
- 2025 RPE remains slightly below the 2021–2023 pre-period average
  ($0.130 M) — partial productivity recovery.
- Note Betsy's reported call volume (>115 k customer interactions per
  month) as a management-reported operating metric.
- **Figure:** `outputs/figures/financial/fig_fin_headcount_productivity_clean.png`.

### 5.3.5 Benchmark Context with Rocket Mortgage
- Use Rocket explicitly as a directional industry benchmark, not as a
  formal counterfactual.
- Cross-company expense-ratio caveat (different accounting
  presentations, scale ~40×, Mr. Cooper acquisition).
- **Figure:** `outputs/figures/financial/fig_fin_benchmark_productivity_expense_ratio_clean.png`.

## 5.4 RQ2 — Customer Experience Evidence
*(Primary source: `08_Code/nlp_project_report.md` and figures under
`outputs/figures/NLP/`.)*

### 5.4.1 Management-Reported NPS
- NPS 39 → 64 post-Betsy.
- Tag as management-reported, unaudited, medium reliability.
- Use the user-specified divergence framing (different measurement
  instruments capturing different customer-experience dimensions).

### 5.4.2 Trustpilot Rating and Sentiment
- Star ratings: pre-Betsy 4.2806 vs post-Betsy 3.8580 (Δ −0.4226,
  Welch's t p = 0.0019, Cohen's d = 0.2899).
- VADER: pre 0.6416 vs post 0.5151 (Δ −0.1265, p = 0.0057, d = 0.2505).
- Frame the decline as a triangulation insight, not as evidence that
  Betsy harmed customer experience.
- **Figure:** `outputs/figures/NLP/fig_nlp_sentiment_by_period_clean.png`.

### 5.4.3 Keyword Prevalence and AI Invisibility
- Cost/Rates 28.92 → 16.57 % (Δ −12.35 pp, p = 0.0009, survives
  Bonferroni).
- Digital/Process 32.65 → 23.67 % (Δ −8.98 pp, p = 0.0211, fails
  Bonferroni).
- Speed/Efficiency 52.00 → 44.38 % (Δ −7.63 pp, p = 0.0698,
  suggestive only).
- Human Support / Communication / Delay/Friction not significant.
- Explicit AI / Automation 1.15 → 1.18 % (Fisher exact p = 1.0000).
- AI-invisibility wording (verbatim from Task 11):
  "The near-zero explicit AI mention rate suggests that customers do
  not usually frame their experience in AI-specific terms. This
  supports the interpretation of voice AI as invisible infrastructure,
  although the keyword analysis cannot determine whether individual
  customers interacted with Betsy."
- **Figure:** `outputs/figures/NLP/fig_nlp_keyword_prevalence_clean.png`.

### 5.4.4 Topic Modeling and Product-Mix Interpretation
- Topic-share denominator: Pre n = 1,077; Post n = 121.
- Key shifts: HELOC complaints +4.22 pp; Smooth Transaction +4.03 pp;
  Responsive Service +3.93 pp; Closing Timeline +3.55 pp; refinance
  topics combined −7.66 pp; Home Purchase −3.48 pp.
- Caveat (verbatim from Task 13): "Because the post-Betsy clustered
  non-outlier sample is only 121 reviews, topic-share changes are
  descriptive signals rather than statistically tested population-level
  changes."
- Optional figure: `outputs/figures/NLP/fig_nlp_topic_shares_clean.png`
  (label clearly as descriptive).

## 5.5 Triangulated Interpretation
- Financial metrics improve.
- Customer-review sentiment declines.
- Explicit AI mentions remain near zero.
- Business value is multidimensional.
- AI-enabled operational leverage may be financially visible while
  customer-experience effects remain mediated by product mix, market
  conditions, and service-quality variation.

## 5.6 Summary of Findings
- Direct answer to RQ1: Betsy was integrated as a voice layer on top of
  the Tinman platform, with ElevenLabs providing low-latency voice
  infrastructure and a human-AI collaboration / escalation model
  preserving compliance.
- Direct answer to RQ2: triangulated evidence is consistent with
  AI-enabled operational leverage on financial / productivity
  dimensions; customer-experience evidence is mixed (NPS up, Trustpilot
  rating and sentiment down, explicit AI mentions near zero).
- Brief statement of limitations before Chapter 6 (descriptive design,
  small post-Betsy NLP sample, single-case design, public-data
  constraints).

---

## Required closing interpretation (verbatim, Task 20)

> "The evidence does not establish that Betsy alone caused
> Better.com's financial recovery. Rather, the post-Betsy period
> displays revenue recovery, expense-intensity improvement, narrowing
> losses, and partial labor-productivity recovery that are consistent
> with AI-enabled operational leverage when interpreted alongside
> qualitative evidence on Betsy's deployment and Tinman's architectural
> role. Customer-perception evidence is more mixed: management-reported
> NPS improves, but independent Trustpilot sentiment declines and
> explicit AI mentions remain rare. This suggests that voice AI may
> create business value as invisible infrastructure, while
> customer-experience effects remain mediated by product mix, market
> conditions, and service-quality variation."

---

## Figure placement quick reference

### Main Chapter 5
- `outputs/figures/financial/fig_fin_better_financial_trajectory_clean.png`
- `outputs/figures/financial/fig_fin_headcount_productivity_clean.png`
- `outputs/figures/financial/fig_fin_expense_ratio_cashflow_clean.png`
  (Panel A primary; full two-panel figure with cash-flow caution)
- `outputs/figures/NLP/fig_nlp_sentiment_by_period_clean.png`
- `outputs/figures/NLP/fig_nlp_keyword_prevalence_clean.png`
- `outputs/figures/NLP/fig_nlp_topic_shares_clean.png`
  (optional, descriptive only)

### Appendix only
- `outputs/figures/NLP/appendix_fig_nlp_operational_leverage_index.png`
  (OLI = 195.3 in 2025; appendix-only by design)
- `outputs/figures/NLP/appendix_fig_nlp_topic_map.png`
  (intertopic distance map)
- `outputs/figures/NLP/appendix_fig_nlp_topic_word_importance.png`
- Quarterly Keyword Group Mentions Over Time (if produced)
- Profitability and Operating Cash Flow Benchmark figure (unless
  specifically needed in §5.3.5)
