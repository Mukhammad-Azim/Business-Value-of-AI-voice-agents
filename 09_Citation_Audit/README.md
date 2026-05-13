# Citation Audit & Reference Repair — Master Index

> **Scope**: Complete citation audit, source verification, deduplication, and APA 7 reconstruction of the thesis *Business Value of Voice LLM Agents in Financial Services*. Performed against `04_Drafts/Main_Draft.docx` and `09_Cleanup_Report/Chapter_5_Empirical_Findings.md`.
>
> **Goal**: One in-text citation = one exact source = one complete reference row = one traceable URL/DOI = one clearly supported claim.

---

## Deliverables Index

| File | Title | Purpose |
|---|---|---|
| [`A_Citation_Audit_Table.md`](./A_Citation_Audit_Table.md) | Citation audit table | Every unique in-text citation key (51) with location, claim, status, and corrected form |
| [`B_Rebuilt_Reference_List.md`](./B_Rebuilt_Reference_List.md) | Rebuilt APA 7 reference list | The canonical, deduplicated, alphabetized reference list (50 entries) — **replaces the entire current References chapter** |
| [`C_Same_Author_Same_Year_Mapping.md`](./C_Same_Author_Same_Year_Mapping.md) | Same-author same-year mapping | Disambiguates Better 2024a/b, 2025a/b/c, 2026, MBA 2024a/b, ElevenLabs 2026, Better×ElevenLabs 2026 |
| [`D_Better_IR_SEC_Verification.md`](./D_Better_IR_SEC_Verification.md) | Better IR / SEC verification | Direct URLs (Better IR + SEC EDGAR) for all 12 Better/ElevenLabs sources |
| [`E_Orphaned_Citation_Resolution.md`](./E_Orphaned_Citation_Resolution.md) | Orphaned-citation resolution | Per-citation resolution for 5 originally-flagged orphans + 12 additional issues |
| [`F_Source_Reliability_Table.md`](./F_Source_Reliability_Table.md) | Source-reliability classification | Reliability tier (high / medium-high / medium / low / contextual) for every source + required wording caveats |
| [`G_Exact_Text_Edits.md`](./G_Exact_Text_Edits.md) | Exact text edits | Copy-paste-ready text patches for Cost/Rates correction, NPS-Trustpilot honesty, decimal precision, vendor caveats, RPE caveat, statistical-method footnote, expense-comparability caveat, OLI treatment, reproducibility note, source-reliability paragraph, figure/caption fixes, "2022" anachronism removal |
| [`H_QC_Checklist.md`](./H_QC_Checklist.md) | Final QC checklist | 41-item auditable checklist confirming citation–reference consistency, suffix disambiguation, URL completeness, APA 7 conformance, source-reliability wording, and substantive critical-review fixes |

---

## Headline Findings

### Citation Inventory
- **305 raw in-text citation matches** across Chapters 1–5 (ref list begins at paragraph 354 of `Main_Draft.docx`)
- After filtering numerical/figure-caption false positives → **240 real citation occurrences**
- After deduplicating by author–year key → **51 unique citation keys**

### Reference List
- **Original list: 79 entries** with severe duplication — split across three sections (above the `---` divider, below the `---` divider, and a third late-appended block at paras 420–432)
- **Rebuilt list: 50 unique entries** — see Deliverable B
- **17+ duplicate sources merged** (Adam, Aggarwal, Andrade, Becker, Better Betsy, Better Q4/FY 2024, Better 10-K [3×], Better×ElevenLabs joint [3×], Blümel, Brynjolfsson, ElevenLabs, Fotheringham, Hentzen, Huang & Rust, Liu, Mogaji, Wang [truncated authors], Zhang)
- **3 broken `Retrieved from` URLs** healed (Better.com Our company; Better IR Corporate overview; Fannie Mae Selling Guide)

### Orphaned Citations
| Original Orphan | Resolution |
|---|---|
| Better Home & Finance Holding Company, 2022 (×2) | Anachronistic; replaced with Better HoldCo Inc. (2021) / (2023) or Primack (2021) by context |
| Better Home & Finance Holding Company, 2024c | Replaced with 2024b (no third 2024 Better-only source exists) |
| Heskett et al., 1994 | Added — verified at *Harvard Business Review*, March–April 1994 |
| Reddy, 2017 | Confirmed as **secondary citation only** ("as cited in Andrade & Tumelero, 2022") — no separate ref entry needed per APA 7 §8.6 |
| Yin, 2018 | Added — verified at SAGE 6th edition (OCLC 1015881135) |
| Acemoglu & Restrepo, 2019 | Added — verified at *Journal of Economic Perspectives* 33(2), DOI 10.1257/jep.33.2.3 |

### Same-Author Same-Year Suffix Disambiguation
- **Better Home & Finance Holding Company (alone)**: 2024a (Betsy launch), 2024b (Q3 2024 results); 2025a (Q4/FY 2024 results), 2025b (Q1 2025 results), 2025c (Q2 2025 results); **2026** (Form 10-K — no suffix)
- **Better Home & Finance Holding Company, & ElevenLabs (joint)**: 2026 — *no suffix needed* because this is a different author group from Better-alone (per APA 7 §8.19)
- **ElevenLabs (alone)**: 2026 — different author group again
- **Mortgage Bankers Association**: 2024a (full-year report), 2024b (Q3 IMB profits release)

### Source-Type Reassignment
The current `Main_Draft.docx` reference list cites Better Q1 2025 and Q2 2025 results via **paid S&P Global Market Intelligence transcripts** (entries 371–372 of the docx, paragraphs 354+). These are **reassigned** to **8-K Exhibit 99.1 / press release** equivalents on SEC EDGAR for traceability:
- Better (2025b, May 13) → SEC EDGAR `betrearningsrelease_2025-q.htm`
- Better (2025c, August 7) → SEC EDGAR `betrearningsrelease_2025-q2.htm`

This change preserves all underlying claims while improving citation traceability (free public access vs paid transcript service).

### APA 7 Style Standardization
- **5 narrative-vs-parenthetical inconsistencies** detected (Andrade & Tumelero; Fotheringham & Wiles; Goodhue & Thompson; Huang & Rust; Mogaji & Nguyen) — all are real source matches but use mixed "and" / "&" forms in inconsistent ways. Standardization rule: parenthetical → "&"; narrative → "and".
- **Author-list completeness**: Wang (2023) and Becker (2025) now list all authors per APA 7 §9.8 (up to 20 authors).

### Substantive (Non-Citation) Fixes from Critical Review
- **Cost/Rates pp correction** (−12.35 pp not −8.98 pp; −8.98 pp belongs to Digital/Process)
- **NPS-vs-Trustpilot divergence**: 7-reason caveat covering sampling, timing, framing, self-selection, product mix, measurement-window differences, channel of feedback collection
- **Decimal precision**: standardize to 3 decimals in chapter; full precision retained in `08_Code/nlp_project_report.md` and Appendix C
- **Statistical-method footnote**: Welch's t-test (continuous) / chi-square / Fisher's exact (binary) / Bonferroni across 7 keyword groups; only Cost/Rates survives strict Bonferroni
- **Vendor-evidence caveat**: ElevenLabs/BusinessWire metrics qualified as company- and vendor-reported, not independently audited
- **Cost-to-originate caveat**: $4,900 explicitly framed as a proxy (total expenses ÷ funded loans), not a Better-disclosed metric
- **RPE caveat**: 2024→2025 RPE recovery acknowledged but flagged as still below the 2021–2023 pre-period average
- **Total-expense comparability**: caveat covering pandemic refinance boom, post-rate-hike contraction, and changing expense composition
- **OLI treatment**: moved to Appendix B as illustrative only
- **Reproducibility note**: package-version snapshot for pandas, numpy, scipy, BERTopic, sentence-transformers, VADER, matplotlib, seaborn → `08_Code/requirements.txt`
- **Source-reliability paragraph**: drop-in text for §5.6 Discussion classifying sources into audited fact / management claim / vendor claim / self-selected UGC / academic theory

---

## How to Apply These Deliverables to the Thesis

The deliverables are organized so the author can apply changes in the following order:

1. **Open Deliverable A** to identify which in-text citations need editing.
2. **Open Deliverable G** for the exact text patches (Cost/Rates, NPS, vendor caveats, etc.) — copy-paste each "New text" into the corresponding paragraph of `09_Cleanup_Report/Chapter_5_Empirical_Findings.md` and `04_Drafts/Main_Draft.docx`.
3. **Apply Deliverable B**: delete the entire current reference list (paragraphs 354–432 of `Main_Draft.docx`) and replace with the rebuilt list. The list is alphabetized and ready for direct paste.
4. **Apply Deliverable C**: standardize same-author same-year suffixes globally (Better 2024a/b, 2025a/b/c, 2026; MBA 2024a/b).
5. **Apply Deliverable D**: confirm every Better/ElevenLabs reference URL loads in a browser before submission.
6. **Apply Deliverable E**: replace each "Better Home & Finance Holding Company, 2022" with the correct anachronism-free citation; confirm Heskett (1994), Yin (2018), and Acemoglu & Restrepo (2019) entries are added.
7. **Apply Deliverable F**: confirm wording caveats are present for NPS 39 → 64, 115k → 700k interactions, +30% conversion, $4,900 cost-to-originate, Trustpilot decline, topic-model shifts, and ElevenLabs/BusinessWire claims.
8. **Run Deliverable H** as a final check before submission.

---

## Outstanding Items Requiring Author Confirmation

| Item | Recommendation |
|---|---|
| **Qualtrics (2024) NPS benchmark** | Replace with NICE Satmetrix Net Promoter Benchmarks Study or Qualtrics XM Institute CX Trends 2024, **or** drop the explicit anchor and cite Hentzen et al. (2022) for industry NPS context |
| **Two "Better Home & Finance Holding Company, 2022" anachronisms** | Author should specify which underlying claim each citation supports; default replacements are Better HoldCo (2021) / (2023) or Primack (2021) |
| **Better IR detail page for Betsy launch (Oct 17, 2024)** | Currently uses Business Wire URL; check whether a dedicated `news-details/2024/Better.com-launches-Betsy/...` page exists on Better IR |
| **FY 2025 Form 10-K SEC EDGAR accession-number URL** | Re-check at submission; current `aurcu-20251231.htm` is the working URL |
| **Jang et al. (2021) author group** | Current ref-list entry lists Jang, Jung & Kim (2021) on Korean banking chatbots; confirm this is the actual paper being cited in Ch. 2 |
| **Maslych et al. (2025) arXiv ID** | Current ref says `2507.22352`; the verified abstract during this audit pointed to `2504.08507`; author should confirm against the paper's bibliographic record |
| **Rocket Companies, Inc. (2024) fiscal-year referenced** | The "(2024)" in-text citation could refer to either FY 2023's 10-K (filed in 2024) or FY 2024's 10-K (filed in 2025); author should confirm and adjust if needed |

---

## Document Provenance

This audit was performed against:
- `04_Drafts/Main_Draft.docx` — 433 paragraphs, Chapters 1–5 + References
- `09_Cleanup_Report/Chapter_5_Empirical_Findings.md` — 209-line empirical-findings chapter
- `08_Code/financial_metrics_project_report.md` — 543-line financial-analysis report
- `08_Code/nlp_project_report.md` — 409-line NLP-analysis report
- `Chapter5_Critical_Review.md` (provided as attachment; archived in `/home/ubuntu/critical_review_output/`) — 13-page critical review

External verifications cross-referenced (selectively):
- SEC EDGAR (https://www.sec.gov) for all Better Home & Finance / Better HoldCo / Rocket Companies filings
- Better Investor Relations (https://investors.better.com) for press releases, news details, and earnings releases
- Business Wire, HousingWire, Axios for news triangulation
- *Harvard Business Review*, *Journal of Service Research*, *Journal of the Academy of Marketing Science*, *European Journal of Marketing*, *Production and Operations Management*, *Trends in Cognitive Sciences*, *Electronic Markets*, *Journal of Service Theory and Practice*, *International Journal of Bank Marketing*, *MIS Quarterly*, *Journal of Economic Perspectives*, NBER, arXiv, AAAI, SAGE Publications, Crossref / DOI lookups for academic sources
- Federal Reserve Bank of New York, Freddie Mac, Mortgage Bankers Association, Fannie Mae, Consumer Financial Protection Bureau for institutional/government sources
- ElevenLabs Blog for vendor materials
