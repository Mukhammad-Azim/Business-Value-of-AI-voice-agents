# Deliverable E — Orphaned Citation Resolution Table

> **Purpose**: Each row resolves an orphaned, ambiguous, or wrong-author/wrong-year in-text citation. Resolution categories: **Found and added** (new reference-list entry); **Corrected to existing** (in-text citation rewritten to match an existing entry); **Converted to secondary** (rewritten as "as cited in"); **Removed/replaced** (claim rewritten or sourced differently); **Marked unresolved** (recommend dropping or rephrasing).

---

## E.1 Critical Review's Five Originally-Identified Orphans

| # | Original Orphan | Resolution Category | Action Taken |
|---|---|---|---|
| 1 | (Better Home & Finance Holding Company, 2022) | **Removed/replaced** | The corporate entity "Better Home & Finance Holding Company" did not exist as a public company until the Aurora SPAC merger closed on August 24, 2023. A 2022 citation is anachronistic. Two replacements depending on context: (a) for the bridge-financing/Aurora SPAC delay narrative — replace with **(Better HoldCo, Inc., 2021)** or **(Primack, 2021)**; (b) for early-2022 operating disclosures — these were not filed to SEC by Better; recommend dropping the 2022 anchor and instead citing the 2023 S-1/A which contains all retrospective 2021–2022 disclosures: **(Better HoldCo, Inc., 2023)**. |
| 2 | (Better Home & Finance Holding Company, 2024c) | **Corrected to existing** | There is no third Better-only 2024 source. All occurrences of "2024c" are replaced with **(Better Home & Finance Holding Company, 2024b)** because the surrounding context refers to post-Betsy commentary, which appears in the Q3 2024 results 8-K (Exhibit 99.1). |
| 3 | (Heskett et al., 1994) | **Found and added** | Verified as a real Harvard Business Review article: J. L. Heskett, T. O. Jones, G. W. Loveman, W. E. Sasser Jr., & L. A. Schlesinger (1994). *Putting the service-profit chain to work*. Harvard Business Review, 72(2), 164–170. URL: https://hbr.org/1994/03/putting-the-service-profit-chain-to-work-2. Added to the rebuilt reference list. |
| 4 | (Reddy, 2017, as cited in Andrade & Tumelero, 2022) | **Confirmed as secondary citation only** | Per APA 7 §8.6, a secondary citation does not require a separate reference-list entry — only the secondary source (Andrade & Tumelero, 2022) is listed. The in-text form was already correct ("as cited in"). No standalone Reddy (2017) entry is needed. **Action**: keep the in-text form, ensure Andrade & Tumelero (2022) is in the reference list (it is). |
| 5 | (Yin, 2018) | **Found and added** | Verified as the 6th edition of Yin's *Case Study Research and Applications: Design and Methods*, SAGE Publications, Los Angeles, 2018. WorldCat OCLC 1015881135. ISBN 9781506336169. Added to the rebuilt reference list. Foundational methodology citation in Chapter 3. |

---

## E.2 Additional Orphans Discovered During the Audit

| # | Additional Orphan | Resolution Category | Action Taken |
|---|---|---|---|
| 6 | (Acemoglu & Restrepo, 2019) — used in Ch. 5 §5.2.4 ("Acemoglu and Restrepo's framework"), missing from original reference list | **Found and added** | Verified at AEA Journal of Economic Perspectives, Vol. 33 No. 2 (Spring 2019), pp. 3–30. DOI: 10.1257/jep.33.2.3. URL: https://www.aeaweb.org/articles?id=10.1257/jep.33.2.3. Added to the rebuilt reference list. |
| 7 | (Better Home & Finance Holding Company, 2025c) — appeared once in original thesis but no matching reference-list entry with that suffix existed | **Found and added** | Verified as the Q2 2025 results press release (Exhibit 99.1 to Form 8-K), dated August 7, 2025. SEC EDGAR URL: https://www.sec.gov/Archives/edgar/data/1835856/000162828025038583/betrearningsrelease_2025-q2.htm. Added to the rebuilt reference list as **Better Home & Finance Holding Company (2025c, August 7)**. |
| 8 | (Mortgage Bankers Association, 2024) — used multiple times across §5.4.3, §5.5; reference list contained two MBA 2024 entries (full-year report; Q3 IMB profits release) but in-text citations did not disambiguate | **Corrected to existing** with new suffixes | Reference list now contains **MBA (2024a)** for the full-year report and **MBA (2024b)** for the Q3 IMB profits release. In-text citations should be disambiguated by context: industry-average production costs / multi-quarter benchmarks → **2024a**; Q3-only references / "$701 per loan" → **2024b**. |
| 9 | (Better Home & Finance Holding Company, 2026a) — original reference list had both "2026" and "2026a" entries for the same Form 10-K | **Corrected to existing** | Standardized to **(Better Home & Finance Holding Company, 2026)** with no suffix because only one Better-only 2026 source exists. All "2026a" usages are replaced with "2026". |
| 10 | (Wang et al., 2023) — reference list had two versions, one with truncated authors ("Wang et al.") and one with full author list (6 authors) | **Corrected to existing** | Single canonical entry with full author list of 6 authors retained. APA 7 §9.8 requires listing up to 20 authors in the reference entry; in-text form remains "Wang et al. (2023)" because there are 3+ authors. |

---

## E.3 Citations With Additional Issues (Non-Orphan but Flagged)

| # | Citation | Issue Type | Resolution |
|---|---|---|---|
| 11 | "Andrade and Tumelero (2022)" appearing as both narrative ("and") and parenthetical ("&") | APA 7 form inconsistency | **Standardize**: parenthetical → "(Andrade & Tumelero, 2022)"; narrative → "Andrade and Tumelero (2022)". Apply Find & Replace across thesis. |
| 12 | "Adam et al. (2021)" appears with a one-author "Adam, 2021" version in one footnote | APA 7 form inconsistency | **Standardize** to "Adam et al. (2021)" or "(Adam et al., 2021)" because the source has 3 authors. |
| 13 | "Wang et al. (2023)" reference entry uses "et al." rather than full author list | APA 7 reference-list format violation | **Replaced** with full author list: Wang, L., Huang, N., Hong, Y., Liu, L., Guo, X., & Chen, G. |
| 14 | "Maslych et al. (2025)" — original reference ended with truncated URL "https://arxiv.org/abs" | Broken URL | **Resolved**: full URL added as https://arxiv.org/abs/2504.08507. |
| 15 | "Better.com Our company" reference ended "Retrieved May 6, 2026, from" with no URL | Missing URL | **Resolved**: URL added as https://better.com/content/our-company. |
| 16 | "Better Home & Finance Investor Relations Corporate overview" reference ended "Retrieved May 6, 2026, from" with no URL | Missing URL | **Resolved**: URL added as https://investors.better.com/overview/default.aspx. |
| 17 | "Fannie Mae Selling Guide" reference ended "Retrieved May 6, 2026, from" with no URL | Missing URL | **Resolved**: URL added as https://singlefamily.fanniemae.com/external-resource/selling-guide. |

---

## E.4 Items Marked as Unresolved or Needing the Author's Decision

| # | Citation | Reason for Unresolved Status | Recommendation |
|---|---|---|---|
| 18 | "Qualtrics (2024)" — used in §5.4.2 as benchmark for NPS comparison | Could not confirm a publicly available report titled exactly *2024 global consumer trends: Financial services NPS benchmarks* | The author should: (a) replace with a verifiable benchmark such as **NICE Satmetrix Net Promoter Benchmarks Study (2024)** or the **Qualtrics XM Institute Customer Experience Trends 2024** report (which exists publicly), or (b) drop the explicit "Qualtrics (2024)" anchor and cite a peer-reviewed source for industry NPS norms (e.g., Reichheld's NPS literature or Hentzen et al., 2022 systematic review). Marked as **unresolved**. |
| 19 | The **two** "Better Home & Finance Holding Company, 2022" citations | Anachronistic (entity didn't exist in 2022) | The author should specify which underlying claim each citation supports so the correct replacement can be applied. **Default replacement**: **(Better HoldCo, Inc., 2023)** S-1/A, which contains all retrospective 2021–2022 financial and operational disclosures. |
