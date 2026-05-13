# NLP Analysis of Customer Perception: Trustpilot Review Mining for Better.com

## Comprehensive Methodological and Findings Report

**Research Context:** MSc Thesis — *Business Value of Voice LLM Agents in Financial Services*
**Author:** Mukhammad Azim Khadyatullaev | Corvinus University of Budapest
**Date:** May 2026

---

## 1. Purpose and Research Alignment

This report documents the complete Natural Language Processing (NLP) analysis pipeline conducted as an empirical complement to the thesis's primary quantitative analysis of Better.com's financial performance. While Chapters 5.2–5.4 of the thesis evaluate business value through SEC filings, cost-to-originate metrics, and operational KPIs, the NLP analysis addresses the **customer experience dimension** of RQ2 — specifically, how the deployment of Betsy (the voice AI agent, launched October 17, 2024) is reflected in public customer discourse.

The NLP analysis is positioned as **triangulation evidence**, not as an independent causal test. It provides an external customer-discourse perspective that complements the financial metrics analysis and the qualitative case study, but it does not independently establish causality or validate management-reported metrics. Crucially, the NLP findings serve to complicate, rather than simply validate or invalidate, the company-reported customer-experience narrative.

The analysis directly supports the revised **Research Question 2** (RQ2):

> *"What measurable business value can be associated with Better.com’s voice AI deployment across operational efficiency, productivity, customer experience, and financial performance, and what factors mediate the realization of this value?"*

The thesis's quantitative evidence demonstrates a 25-point NPS improvement (39 → 64) reported by management. The NLP analysis triangulates this self-reported metric with independent, unsolicited customer feedback from Trustpilot — providing an external customer-discourse perspective that adds depth and friction to management-reported metrics rather than serving as direct validation.

### 1.1 Specific Analytical Objectives

1. **Keyword prevalence analysis:** Measure whether customer discourse about AI/automation, speed, cost, communication, and service quality changed after Betsy's launch, with statistical significance testing.
2. **Unsupervised topic modeling:** Discover latent thematic structure in customer reviews using BERTopic (Grootendorst, 2022) and compare topic distributions between pre- and post-Betsy periods.
3. **Sentiment analysis:** Quantify sentiment polarity across periods as a complementary customer experience indicator.
4. **AI visibility assessment:** Test whether customers explicitly reference AI, automation, or chatbot technology — or whether AI functions as invisible infrastructure.

---

## 2. Dataset Construction

### 2.1 Data Source and Collection Method

Customer reviews were collected from **Trustpilot** (https://www.trustpilot.com/review/better.com), a third-party consumer review platform widely used in academic research on service quality and customer experience (Filieri, 2015; Luca, 2016). Trustpilot was selected because it provides independently verified, publicly accessible reviews with structured metadata (date, rating, verification status, language), and because Better.com maintains an active presence on the platform.

Data extraction was performed using the **Apify platform** (https://apify.com), a cloud-based web scraping infrastructure, and specifically the **Trustpilot Review Scraper** actor (Actor ID: `l3wcDhSSC96LBRUpc`). The scraper was configured to extract all available reviews for the Better.com Trustpilot profile. The scraper collected the following fields per review:

| Field | Description |
|---|---|
| `reviewId` | Unique Trustpilot review identifier |
| `reviewDate` | ISO 8601 timestamp of review publication |
| `reviewText` | Full text body of the customer review |
| `rating` | Star rating (1–5 scale) |
| `country` | Reviewer's self-reported country |
| `language` | Detected review language |
| `verified` | Whether Trustpilot verified the review |

The raw dataset was exported as CSV and subjected to **manual quality assurance**: multiple rows were inspected to confirm absence of HTML artifacts, encoding errors, duplicate entries, or scraping failures. This manual verification step ensures dataset integrity beyond what automated validation alone can guarantee.

**Total raw reviews collected: 1,934**

### 2.2 Data Cleaning Pipeline (`cleaning_reviews.ipynb`)

A dedicated Jupyter Notebook implements the cleaning pipeline with full reproducibility. The pipeline applies the following sequential filters:

| Step | Operation | Rows Before | Rows After | Removed |
|---|---|---|---|---|
| 1 | Column renaming and standardization | 1,934 | 1,934 | 0 |
| 2 | Date parsing (`pd.to_datetime`) and timezone removal | 1,934 | 1,934 | 0 |
| 3 | Drop rows with missing `review_text`, `rating`, or `review_date` | 1,934 | 1,934 | 0 |
| 4 | Remove exact duplicates by `review_id` | 1,934 | 1,934 | 0 |
| 5 | Remove short reviews (≤20 characters) | 1,934 | 1,916 | 18 |
| 6 | Retain English-language reviews only | 1,916 | 1,915 | 1 |

**Final clean dataset: 1,915 reviews** spanning August 22, 2020 to April 25, 2026.

### 2.3 Temporal Segmentation

Reviews are segmented into two analytical periods using Betsy's official launch date (October 17, 2024) as the temporal boundary:

| Period | Date Range | n | Share |
|---|---|---|---|
| **Pre-Betsy** | 2020-08-22 → 2024-10-15 | 1,746 | 91.2% |
| **Post-Betsy** | 2024-10-22 → 2026-04-25 | 169 | 8.8% |

> **Methodological note:** The severe class imbalance (10.3:1 ratio) is an inherent feature of the temporal design — Betsy (the voice AI agent) has been operational for approximately 18 months versus 4+ years of pre-Betsy reviews. All statistical tests account for this imbalance, and percentage-based comparisons (rather than raw counts) are used throughout. Observed Post-Betsy percentages carry wider confidence intervals; each individual review represents approximately 0.59 percentage points. Because the data uses annual aggregation, the analysis cannot isolate effects arising specifically from Q4 2024 (Betsy's launch quarter) from effects in subsequent quarters.
>
> **Figure Standardization Note:** Across all figures, a consistent categorical ordering is enforced (**Pre-Betsy first, Post-Betsy second**) along with a consistent color mapping (**Pre-Betsy is a muted blue `#3a86c8`, Post-Betsy is a muted orange/red `#e07a5f`**). This avoids automated Plotly color shifting and ensures reader clarity.

### 2.4 Sentiment Scoring

During the cleaning phase, each review was scored using the **VADER (Valence Aware Dictionary and sEntiment Reasoner)** sentiment analyzer (Hutto & Gilbert, 2014), a lexicon and rule-based tool validated for social media and review text. VADER produces a compound sentiment score ranging from −1.0 (most negative) to +1.0 (most positive).

The sentiment column was exported in the clean CSV with European comma-decimal formatting. In the analysis notebook, this is re-parsed to float and validated (1,915 valid scores, range −0.984 to +0.998).

### 2.5 Exploratory Data Quality Statistics (from `cleaning_reviews.ipynb`)

| Metric | Value |
|---|---|
| Mean rating | 4.24 / 5.0 |
| Rating distribution | 75.3% 5-star, 14.9% 1-star (bimodal) |
| Pre-Betsy mean rating | 4.28 |
| Post-Betsy mean rating | 3.86 |
| Welch's t-test (rating) | t = 3.15, p = 0.002 ** |
| Pre-Betsy mean sentiment | 0.642 |
| Post-Betsy mean sentiment | 0.515 |
| Welch's t-test (sentiment) | t = 2.80, p = 0.006 ** |

The statistically significant decline in both rating and sentiment is noteworthy and is discussed in Section 5.

### 2.6 Annual Review Volume

| Year | Reviews |
|---|---|
| 2020 | 221 |
| 2021 | 817 |
| 2022 | 453 |
| 2023 | 76 |
| 2024 | 214 |
| 2025 | 60 |
| 2026 (partial) | 74 |

The 2021 peak aligns with the pandemic-era refinancing boom; the 2023 trough reflects the post-rate-hike market contraction. The 2024 recovery coincides with Better's renewed marketing and Betsy's launch.

---

## 3. Analysis Pipeline (`better_reviews_topic_modeling.ipynb`)

### 3.1 Text Preprocessing

Each review undergoes a two-stage text transformation:

**Stage 1 — `clean_text_raw`:** Lowercasing, removal of URLs, email addresses, phone numbers, non-alphabetic characters, and extra whitespace. This preserves the full lexical content for keyword analysis.

**Stage 2 — `topic_text`:** Additional removal of a curated stopword list (423 terms) combining NLTK English stopwords with domain-specific terms (e.g., "better", "com", "mortgage", "loan", "company", "review", "experience") that are ubiquitous across all reviews and would dominate topic representations without contributing thematic discrimination. This stage is used exclusively as input to BERTopic.

### 3.2 Keyword-Based Prevalence Analysis

Seven keyword groups were defined a priori based on the thesis's business value framework and the specific capabilities claimed for Betsy:

| Keyword Group | Representative Terms | Rationale |
|---|---|---|
| **Explicit AI/Automation** | "ai", "artificial intelligence", "chatbot", "automated", "bot", "machine learning", "virtual assistant" | Directly measures AI visibility in customer discourse |
| **Speed/Efficiency** | "fast", "quick", "efficient", "smooth", "seamless", "timely" | Core value proposition of voice AI |
| **Human Support** | "team", "staff", "agent", "advisor", "helped me", "person" | Complementary dimension; AI may shift human mentions |
| **Communication** | "responsive", "communication", "answered", "explained", "clear" | Service quality indicator |
| **Delay/Friction** | "delay", "slow", "waiting", "frustrated", "stuck", "problem" | Negative experience indicator |
| **Cost/Rates** | "rate", "rates", "cost", "fees", "expensive", "affordable", "pricing" | Financial value dimension |
| **Digital/Process** | "online", "digital", "portal", "dashboard", "app", "upload", "website" | Technology-mediated process experience |

Keyword matching uses **word-boundary regular expressions** (`\b...\b`) via a utility function `contains_any_phrase()` to prevent false positives (e.g., "rates" matching within "celebrates"). Each review is binary-coded (1/0) for each group, and group prevalence is calculated as the percentage of reviews mentioning at least one term in the group.

### 3.3 CEO Outlier Filtering

During the 2020–2022 period, Better.com received significant negative press coverage related to a mass layoff event conducted via Zoom, which generated a cluster of reviews focused on the CEO and corporate culture rather than the mortgage product or service. To prevent these outlier reviews from distorting the topic model, reviews containing CEO/scandal-related terms ("vishal", "garg", "ceo", "zoom", "fired", "firing", "layoff", "layoffs", "employees") were filtered using the same word-boundary matching logic.

**Rows removed by CEO and outlier filter: 111** (reducing corpus from 1,915 to 1,804)

This filter is applied only to the topic modeling input — rating, sentiment, and keyword prevalence analyses retain all 1,915 reviews to preserve the full temporal signal of customer discourse.

### 3.4 BERTopic Configuration

The topic model uses **BERTopic** (Grootendorst, 2022), a neural topic modeling framework that combines transformer-based document embeddings with class-based TF-IDF to produce interpretable topic representations. The pipeline components:

| Component | Configuration | Rationale |
|---|---|---|
| **Embedding model** | `all-MiniLM-L6-v2` (Sentence-Transformers) | Balanced performance/speed for short texts |
| **UMAP** | `n_neighbors=10, n_components=5, min_dist=0.0, metric="cosine", random_state=42` | Dimensionality reduction with fixed seed for reproducibility |
| **HDBSCAN** | `min_cluster_size=10, min_samples=3, metric="euclidean", cluster_selection_method="eom"` | Density-based clustering allowing variable-density topics |
| **CountVectorizer** | `ngram_range=(1,2), min_df=5, max_df=0.85, stop_words=custom_stopwords` | `min_df=5` filters noise from hapax legomena; `max_df=0.85` excludes universally common terms |

### 3.5 Topic Labeling Methodology

Following standard practice in qualitative topic model interpretation (Blei, Ng, & Jordan, 2003; Grootendorst, 2022), each topic was assigned a descriptive label by the researcher through manual inspection of (a) the top 10 c-TF-IDF keywords per topic, and (b) a minimum of five representative documents per topic. Labels were registered in the BERTopic model via `set_topic_labels()` and are used in all visualizations.

---

## 4. Results

### 4.1 Topic Model Output

The BERTopic model produced **44 topics** (Topic 0 through Topic 43), with Topic −1 representing the noise/outlier class.

| Metric | Value |
|---|---|
| Documents input to BERTopic | 1,804 |
| Topics discovered | 44 |
| Clustered documents | 1,198 (66.4%) |
| Outlier documents (Topic −1) | 606 (33.6%) |
| Largest topic share | 7.26% (Topic 0: First-Time Home Purchase) |

The outlier rate of 33.6% is within the expected range for HDBSCAN-based clustering of short, heterogeneous review text. Short customer reviews exhibit high lexical variability and idiosyncratic expression, which means many documents do not conform to recurring thematic patterns detectable by density-based clustering. This is a known characteristic of HDBSCAN applied to short-text corpora rather than a sign of model failure (McInnes et al., 2017). The topic model should therefore be understood as capturing the **most recurring thematic clusters** rather than providing complete thematic coverage of all customer concerns. Topic-level findings are descriptive and should not be interpreted as representing the full distribution of customer sentiment.

### 4.2 Topic Inventory

**Positive Experience Topics (majority):**

| ID | Label | n |
|---|---|---|
| 0 | First-Time Home Purchase | 87 |
| 1 | Online Refinance — Positive | 79 |
| 2 | Efficient Refinance & Advocacy | 53 |
| 3 | Competitive Rates & Fees | 52 |
| 7 | Portal Task Management | 37 |
| 8 | Communication Quality | 35 |
| 9 | Responsive Q&A Support | 35 |
| 15 | Responsive Professional Service | 27 |
| 16 | Excellent General Service | 24 |
| 17 | Stress-Free Experience | 22 |

**Negative/Friction Topics:**

| ID | Label | n | Concern |
|---|---|---|---|
| 18 | Income & Closing Disputes | 26 | Underwriting disagreements |
| 19 | Poor Phone/Email Contact | 24 | Failed outreach |
| 31 | Appraisal Disputes | 17 | Value conflicts |
| 36 | HELOC Complaints | 14 | Product-specific problems |
| 37 | Staff Treatment Concerns | 13 | Internal culture perception |
| 43 | Worst Experience — Very Negative | 11 | Severe dissatisfaction |

Negative topics together account for approximately 105 of 1,198 clustered documents (~8.8% of clustered reviews, or ~5.8% of total documents including outliers). This represents a meaningful minority of identifiable friction areas that automation has not resolved. The denominator used throughout this report for topic share percentages is **clustered documents** (n=1,198), excluding the 606 outlier documents assigned to Topic −1.
Specifically, **percentages are calculated among clustered non-outlier BERTopic assignments, and denominators are non-outlier clustered reviews only.** In the updated topic shares figure, the Pre-Betsy clustered non-outlier n = 1,077 and Post-Betsy clustered non-outlier n = 121, ensuring denominator consistency between the displayed percentages and reported sample sizes. Topic-level shifts are descriptive only because the post-Betsy sample is small, capturing recurring thematic clusters rather than the full distribution of all customer reviews.

### 4.3 Statistical Tests: Keyword Prevalence Pre vs Post-Betsy

Below is the updated keyword prevalence analysis using 95% Wilson score confidence intervals, Pearson's Chi-squared tests, and Fisher's exact tests to evaluate the significance of changes in customer discourse before and after Betsy's launch across the full clean dataset (n_pre = 1,746; n_post = 169):

| Keyword Group | Pre % (95% CI) | Post % (95% CI) | Δ (pp) | χ² p-value | Fisher p-value | Odds Ratio | Significance (Bonferroni) |
|---|---|---|---|---|---|---|---|
| **Cost/Rates** | 28.92% (26.84%–31.09%) | 16.57% (11.72%–22.90%) | −12.35% | 0.0009 | 0.0004 | 2.0492 | **Highly Significant** |
| **Digital/Process** | 32.65% (30.49%–34.88%) | 23.67% (17.89%–30.62%) | −8.98% | 0.0211 | 0.0193 | 1.5631 | **Significant** (α=0.05) |
| **Human Support** | 43.81% (41.50%–46.15%) | 40.83% (33.70%–48.36%) | −2.98% | 0.5052 | 0.4659 | 1.1302 | Not Significant |
| **Speed/Efficiency** | 52.00% (49.66%–54.34%) | 44.38% (37.10%–51.91%) | −7.63% | 0.0698 | 0.0638 | 1.3580 | Suggestive (α=0.10) |
| **Communication** | 32.53% (30.37%–34.77%) | 30.77% (24.30%–38.09%) | −1.76% | 0.7029 | 0.6678 | 1.0849 | Not Significant |
| **Delay/Friction** | 13.52% (11.99%–15.20%) | 10.06% (6.38%–15.52%) | −3.46% | 0.2508 | 0.2346 | 1.3974 | Not Significant |
| **Explicit AI/Automation** | 1.15% (0.74%–1.76%) | 1.18% (0.33%–4.21%) | +0.04% | 1.0000 | 1.0000 | 0.9676 | Not Significant |

> [!NOTE]
> **Multiple Comparisons & Bonferroni Correction:** Seven keyword groups were tested simultaneously, which raises the risk of Type I error. Under a strict Bonferroni correction (adjusted α = 0.05/7 ≈ 0.0071), only **Cost/Rates** (p = 0.0009) remains fully statistically significant. Digital/Process (p = 0.0211) is significant under standard unadjusted threshold but suggestive under multiple-comparison correction.
>
> **Low-Frequency AI/Automation Note:** Because explicit AI mentions occur in only ~1.15% of reviews, cell counts are extremely small. Under Fisher's exact test, which is mathematically exact for low-frequency cells, the difference remains highly non-significant (p = 1.0000), supporting the **AI Invisibility hypothesis** (i.e. Betsy operates seamlessly as background infrastructure rather than being actively described in AI-specific terms by customers).

### 4.4 Star Rating and Sentiment by Period

To examine whether operational efficiency gains coincided with changes in customer sentiment and discourse across the full clean dataset, we conducted Welch's t-tests (which accommodate unequal sample sizes and variances) and calculated Cohen's d effect sizes:

*   **Star Ratings (1–5 scale):**
    *   **Pre-Betsy Mean:** 4.2806 (std: 1.4336, n = 1,746)
    *   **Post-Betsy Mean:** 3.8580 (std: 1.6878, n = 169)
    *   **Welch's t-test:** t = 3.1473, p-value = 0.0019
    *   **Mean Difference (Post − Pre):** −0.4226 [95% CI: −0.6865 to −0.1587]
    *   **Effect Size (Cohen's d):** 0.2899 (small-medium effect size)
*   **VADER Sentiment Score (−1.0 to +1.0 scale):**
    *   **Pre-Betsy Mean:** 0.6416 (std: 0.4986, n = 1,746)
    *   **Post-Betsy Mean:** 0.5151 (std: 0.5671, n = 169)
    *   **Welch's t-test:** t = 2.7976, p-value = 0.0057
    *   **Mean Difference (Post − Pre):** −0.1265 [95% CI: −0.2152 to −0.0378]
    *   **Effect Size (Cohen's d):** 0.2505 (small effect size)

Both ratings and sentiment exhibit statistically significant declines post-Betsy, representing a key point of divergence from the company-reported NPS improvement. This indicates that while voice AI may drive backend operational leverage, it does not automatically translate into a uniformly improved independent customer discourse.

### 4.5 Pre/Post Topic Shifts

| Topic | Pre % | Post % | Δ (pp) | Direction |
|---|---|---|---|---|
| 36 – HELOC Complaints | 0.74 | 4.96 | +4.22 | ↑ |
| 33 – Smooth Transaction | 0.93 | 4.96 | +4.03 | ↑ |
| 15 – Responsive Service | 1.86 | 5.79 | +3.93 | ↑ |
| 5 – Closing Timeline | 3.06 | 6.61 | +3.55 | ↑ |
| 1+2 – Refinance topics | 11.79 | 4.13 | −7.66 | ↓ |
| 0 – Home Purchase | 7.61 | 4.13 | −3.48 | ↓ |

> **Caveat:** With n=121 Post-Betsy clustered non-outlier reviews, topic-level shifts are descriptive only — each review represents approximately 0.83 pp of the clustered sample. No inferential claims are made from these proportions.

---

## 5. Interpretation and Discussion

### 5.1 The AI Invisibility Finding

The most thesis-relevant result is the **null finding on explicit AI mentions**: only 1.15–1.18% of reviews reference AI, automation, chatbots, or related technology in either period, with zero statistically discernible change (χ² ≈ 0, p ≈ 1.00).

This does not indicate Betsy had no effect. It suggests that **customers do not cognitively frame their mortgage experience in technological terms**. They evaluate outcomes — speed, ease, cost, communication quality — rather than the mechanisms producing them. This is consistent with Mogaji and Nguyen's (2021) finding that consequential AI applications in financial services often operate "invisibly within backend infrastructure" rather than as customer-facing branded features.

This null result should be interpreted cautiously. Explicit AI references may be under-detected due to **vocabulary limitations** (the keyword list may not capture all ways customers describe AI interactions), **indirect phrasing** (e.g., "the system" or "automated voice" without using AI-specific terms), or the **low base rate** (~1%) which limits statistical power to detect small changes. The near-zero explicit AI mention rate suggests that customers do not usually frame their experience in AI-specific terms. This supports the interpretation of voice AI as **invisible infrastructure**, although the keyword analysis cannot determine whether individual customers interacted with Betsy. The finding is therefore best read as a descriptive observation about customer discourse rather than as a measurement of customer exposure to the AI agent.

### 5.2 Cost/Rates Decline (−12.35 pp, p = 0.0009)

The statistically significant reduction in cost/rates mentions is the strongest individual signal (and the only result surviving Bonferroni correction). Three non-exclusive interpretations:

1. **Pricing competitiveness:** Better.com may have improved rate transparency post-Betsy, reducing cost salience.
2. **Macroeconomic confound:** Federal Reserve rate cuts began in late 2024, potentially reducing rate-sensitivity across the mortgage industry — a confound that cannot be controlled without a comparison group.
3. **Selection effect:** Post-Betsy customers who proceeded to close may have already pre-screened Better's rates as competitive.
4. **Product mix shift:** Growth in HELOC products (reflected in Topic 36) may have shifted customer discourse away from traditional rate concerns.

Importantly, this decline does not necessarily indicate improved pricing perception; it may reflect **reduced salience of rates** in customer discourse due to macroeconomic or product-mix factors. The finding is consistent with, but not uniquely explained by, the thesis's quantitative evidence of a declining cost-to-originate ($8,500 → $4,900).

### 5.3 Speed/Efficiency Marginal Decline (−7.63 pp, p = 0.070)

The trend-level reduction in speed mentions admits two readings:

- **Ceiling effect (positive):** Speed has been normalized — customers take it for granted and no longer praise it explicitly. This is consistent with AI-driven automation establishing fast processing as a baseline.
- **Actual decline (negative):** Betsy's introduction may have added verification steps or document requests that marginally slowed perceived processing.

The ambiguity should be acknowledged in the thesis discussion.

### 5.4 Sentiment Decline — Compositional and Methodological Considerations

The lower Post-Betsy mean sentiment (0.515 vs 0.642, p = 0.006) appears to contradict the NPS improvement. One plausible explanation is **compositional**: the Post-Betsy review sample includes a higher proportion of HELOC complaints (Topic 36: +4.22 pp) and closing disputes, which are product-specific issues unrelated to AI deployment. Trustpilot reviewers also skew toward extreme experiences. The NPS metric (internal, survey-based) captures a broader population than self-selected Trustpilot reviewers.

However, this compositional explanation is suggestive rather than conclusive. Without product-level controls or a matched comparison group, the analysis cannot isolate whether the sentiment decline reflects (a) changing review composition, (b) genuine experience deterioration for some customer segments, (c) platform selection effects, or (d) random variation amplified by the small post-period sample. The divergence between sentiment and NPS should be characterized as a **triangulation insight** — different measurement instruments capture different facets of customer experience — rather than as evidence that one metric is "correct" and the other misleading.

### 5.5 Topic Shifts — Macro vs Technology Effects

The decline in refinance topics (−7.66 pp combined) most plausibly reflects the macroeconomic environment (elevated rates reducing refinancing demand) rather than any technology effect. The growth in "Responsive Professional Service" (+3.93 pp) and "Smooth Transaction" (+4.03 pp) is **directionally consistent** with AI-driven operational improvements but cannot be associated solely with Betsy given the small sample, absence of controls, and the fact that these shifts occurred around the same period as multiple other changes at Better.com (product mix, staffing, market conditions).

The rise in HELOC Complaints (+4.22 pp) likely reflects product mix expansion at Better.com rather than service quality decline.

### 5.6 Alternative Explanations

The following alternative explanations should be considered when interpreting the NLP findings:

1. **Mortgage market cycle:** The pre-Betsy period (2020–2024) spans the pandemic refinancing boom and post-rate-hike bust. Changes in keyword prevalence and topic distribution may reflect macroeconomic demand shifts rather than technology effects.
2. **Product mix changes:** Better.com expanded into HELOC products during 2024–2025. The rise in HELOC-related complaints and the decline in refinance topics are plausibly driven by product strategy rather than AI deployment.
3. **Platform selection bias:** Trustpilot reviewers are self-selected and tend to over-represent extreme experiences (very positive or very negative). The review population may not be representative of Better.com's full customer base.
4. **Review self-selection bias:** Customers who interact with Betsy but have unremarkable experiences may be less likely to write reviews, biasing the post-period sample toward outlier experiences.
5. **Temporal sample imbalance:** The post-Betsy sample (n=169) is small relative to pre-Betsy (n=1,746). Small-sample instability means that a few atypical reviews can substantially shift post-period percentages and topic distributions.

These alternative explanations do not invalidate the findings but underscore that all NLP results should be interpreted as **indicative rather than causal**.

### 5.7 Triangulation with Financial Analysis

The NLP findings should be read alongside the companion financial metrics analysis (`financial_metrics_project_report.md`). The financial analysis shows improvements in operational efficiency (Expense Ratio declining 30.6% from 2024 to 2025), revenue recovery (+52.0%), and labor productivity gains (RPE +42.9%) in the post-Betsy period. However, the NLP analysis does not show a corresponding improvement in customer sentiment — in fact, both mean rating and VADER sentiment declined significantly post-Betsy.

This divergence is an important analytical finding. It suggests that **AI-driven operational gains do not necessarily translate into uniformly improved perceived customer experience**, at least as measured through unsolicited third-party reviews. The operational and financial dimensions of business value may improve faster and more visibly than the customer experience dimension, which is mediated by product-specific issues (HELOC complaints), platform selection effects, and the inherent invisibility of AI infrastructure to end users.

This cross-analysis reinforces the thesis argument that business value should be evaluated across **multiple dimensions** (RQ2) rather than reduced to a single metric, and that different measurement instruments — audited financial data, management-reported NPS, and independent customer discourse — may yield complementary but non-identical signals.

---

## 6. Figures and Outputs

### 6.1 Clean, Thesis-Ready Figures (`outputs/figures/NLP/`)

A consistent categorical ordering (**Pre-Betsy first, Post-Betsy second**) and color mapping (**Pre-Betsy is a muted blue `#3a86c8`, Post-Betsy is a muted orange/red `#e07a5f`**) are applied across all charts. Figures have been updated to remove any hard-coded local paths, use project-relative directories, and exclude figure numbering from titles (which is handled by thesis captions).

| File Name | Title | Description | Selection / Placement |
|---|---|---|---|
| `fig_nlp_sentiment_by_period_clean.png` | Sentiment Score Distribution: Pre-Betsy vs Post-Betsy | Box plot of VADER sentiment scores. Includes mean markers and Welch's t-test significance note (p=0.006). Pre-Betsy is displayed first. | **Main Text (Chapter 5)** |
| `fig_nlp_keyword_prevalence_clean.png` | Keyword Group Mentions Before and After Betsy | Grouped bar chart of keyword group mentions with Pre-Betsy displayed first and a significance annotation specifically for Cost/Rates (which survives Bonferroni correction). AI/Automation remains shown at ~1.1% to support "AI invisibility". | **Main Text (Chapter 5)** |
| `fig_nlp_topic_shares_clean.png` | Top Customer Experience Topics: Pre vs Post-Betsy | Grouped bar chart of top topic shares. Solves the denominator issue by using exact clustered non-outlier reviews (Pre-Betsy n=1,077, Post-Betsy n=121). | **Main Text (Chapter 5)** |
| `fig_nlp_quarterly_keywords_clean.png` | Quarterly Keyword Group Mentions Over Time | Two-panel subplot showing quarterly keyword group prevalence (Line) and review volume (Bar). Solves the noisy monthly data issue and marks low-volume quarters (<10 reviews) as unstable. | **Appendix / Supplementary** |
| `appendix_fig_nlp_topic_map.png` | Intertopic Distance Map — Better.com Customer Reviews (Appendix) | 2D UMAP projection of the topic space. Used for model diagnostic and topic distance visualization. | **Appendix / Supplementary** |
| `appendix_fig_nlp_topic_word_importance.png` | Top Customer Experience Topics — Word Importance Scores (Appendix) | Word-importance score bar chart for the top 12 topics. Used to validate topic labeling. | **Appendix / Supplementary** |

### 6.2 Saved CSVs

| File | Contents |
|---|---|
| `better_trustpilot_keyword_analysis.csv` | Full dataset with keyword flags and topic assignments |
| `better_trustpilot_with_topics.csv` | Reviews with topic IDs and human-readable labels |
| `better_keyword_summary.csv` | Keyword prevalence percentages by period |
| `better_topic_summary.csv` | Topic info with document counts and top words |
| `better_topic_period_comparison.csv` | Topic share percentages by Pre/Post-Betsy period |

---

## 7. Methodological Limitations

| Limitation | Mitigation |
|---|---|
| **Sample imbalance** (Pre=1,746 vs Post=169) | Chi-squared tests account for group sizes; percentage-based comparisons used; confidence interval caveat stated |
| **Outlier rate** (33.6% assigned to Topic −1) | Expected for HDBSCAN on short heterogeneous text (McInnes et al., 2017); topic findings describe recurring clusters, not full thematic coverage |
| **No causal identification** | Pre/post design without control group cannot isolate Betsy's effect from macro, product-mix, and platform factors; all interpretations framed as associative |
| **Platform selection bias** | Trustpilot reviewers self-select; findings may not represent all Better.com customers |
| **Multiple comparisons** | Seven keyword groups tested; only Cost/Rates survives Bonferroni correction; others are suggestive |
| **Low-frequency AI detection** | ~1% prevalence limits chi-square validity; Fisher's exact test would be more appropriate; null result interpreted directionally |
| **HDBSCAN non-determinism** | UMAP seeded with `random_state=42`; topic assignments saved to CSV for reference stability |
| **Researcher-assigned topic labels** | Labels based on systematic inspection of top words + representative documents; process documented in code |

---

## 8. Contribution to the Thesis

This NLP analysis provides the thesis with three distinct contributions:

**First**, it supplies **triangulation evidence** for the customer experience dimension of RQ2. The management-disclosed NPS improvement (39 → 64) is a self-reported metric that may reflect promotional framing. The Trustpilot analysis provides an independent, externally sourced perspective that partially complements (topic shifts toward positive service themes) and partially complicates (lower raw sentiment) the NPS narrative. This divergence is itself analytically valuable: it suggests that AI-driven operational gains (documented in the financial analysis) do not automatically translate into uniformly improved customer perception as captured by unsolicited third-party reviews. This finding reinforces the thesis argument that business value must be evaluated across multiple dimensions rather than reduced to any single metric.

**Second**, the **AI invisibility finding** is a substantive insight in its own right, despite its limitations. The consistently near-zero rate of explicit AI mentions (~1%) across both periods provides indicative evidence that voice AI can transform customer-facing operations without customers perceiving or describing the interaction in technological terms. This is consistent with the thesis's conceptual framing of Betsy as "invisible infrastructure" and has implications for how financial services organizations communicate about AI to customers. However, this null result should be qualified by vocabulary limitations and the low statistical power associated with rare-event detection.

**Third**, the analysis demonstrates **multi-method triangulation** — combining quantitative financial analysis (SEC filings), qualitative document analysis (earnings transcripts), and computational text analysis (NLP) to evaluate the same research question from multiple evidence streams. The fact that these methods produce **complementary but non-identical signals** (financial improvement alongside sentiment decline) strengthens the overall analytical rigor of the thesis by preventing over-reliance on any single data source (Flick, 2018).

---

## References

Blei, D. M., Ng, A. Y., & Jordan, M. I. (2003). Latent Dirichlet allocation. *Journal of Machine Learning Research*, 3, 993–1022.

Filieri, R. (2015). What makes online reviews helpful? A diagnosticity-adoption framework to explain informational and normative influences in e-WOM. *Journal of Business Research*, 68(6), 1261–1270. https://doi.org/10.1016/j.jbusres.2014.11.006

Flick, U. (2018). *An introduction to qualitative research* (6th ed.). SAGE Publications.

Grootendorst, M. (2022). BERTopic: Neural topic modeling with a class-based TF-IDF procedure. *arXiv preprint arXiv:2203.05794*.

Hutto, C. J., & Gilbert, E. (2014). VADER: A parsimonious rule-based model for sentiment analysis of social media text. *Proceedings of the International AAAI Conference on Web and Social Media*, 8(1), 216–225.

Luca, M. (2016). Reviews, reputation, and revenue: The case of Yelp.com. *Harvard Business School Working Paper*, No. 12-016.

Mogaji, E., & Nguyen, N. P. (2021). Managers' understanding of artificial intelligence in relation to marketing financial services. *International Journal of Bank Marketing*, 39(6), 1544–1565. https://doi.org/10.1108/IJBM-10-2020-0527

McInnes, L., Healy, J., & Astels, S. (2017). hdbscan: Hierarchical density based clustering. *Journal of Open Source Software*, 2(11), 205. https://doi.org/10.21105/joss.00205

---

*This report documents the full NLP analysis pipeline for integration into Chapter 5 (Data Analysis and Empirical Findings) of the thesis. The NLP analysis provides triangulation evidence for the customer experience dimension of RQ2 and should be read alongside the companion financial metrics analysis (`financial_metrics_project_report.md`). All code is available in `better_reviews_topic_modeling.ipynb` and `cleaning_reviews.ipynb` within the `08_Code` directory.*
