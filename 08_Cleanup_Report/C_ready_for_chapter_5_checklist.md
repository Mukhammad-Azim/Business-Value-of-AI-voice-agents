# C. "Ready for Chapter 5" Checklist

Every box below was verified after the cleanup pass. Boxes that remain
unchecked are explicitly out of scope for this pass and are flagged at the
bottom for the user to address before submission.

## Research questions and framing
- [x] RQ1 unchanged.
- [x] RQ2 uses the final wording in `04_Drafts/Main_Draft.docx` and
      `thesis_integration_instructions.md`.
- [x] No "DiD" / "DiD-style" / "Difference-in-Differences" residue in the
      draft, financial report, NLP report, or integration notes.
- [x] Causality language register enforced ("consistent with",
      "associated with", "directionally supports", "provides descriptive
      evidence", "cannot isolate Betsy's specific contribution").
- [x] No instances of "validates the hypothesis", "definitively
      demonstrates", "transformative results achieved through AI",
      "only achievable through AI substitution", or "positive causal
      interpretation" in the draft or reports.

## Financial methodology and values
- [x] Financial dataset described as built from 10 SEC regulatory filing
      PDFs (3 Better 10-Ks + 1 S-1 + 6 Rocket 10-Ks).
- [x] Rocket 2018–2019 sourced from comparative tables in Rocket's 2020
      10-K, not from separate local PDFs.
- [x] Final dataset described as 13 rows × 15 columns, USD millions,
      employee count as headcount.
- [x] pdfplumber and pypdf identified as the extraction libraries; no
      OCR; pipeline did not parse tables automatically; final values
      manually identified and cross-verified; derived metrics computed
      deterministically.
- [x] Better revenue values standardized to $76.8 M (2023), $108.5 M
      (2024), $164.9 M (2025).
- [x] Better total expenses $368.1 M / $313.9 M / $330.7 M (2023–2025).
- [x] Better net loss −$536.4 M / −$206.3 M / −$165.9 M (2023–2025).
- [x] Expense ratio 4.79 / 2.89 / 2.01 (2023–2025).
- [x] Revenue per employee $0.094 M / $0.087 M / $0.124 M (2023–2025).
- [x] 2024→2025 framed as the primary post-transition window.
- [x] 2023→2025 retained as recovery-from-trough supporting evidence.
- [x] Pre-period-average→2025 retained as a robustness sensitivity check.
- [x] Total_Expenses now described as a "standardized total expense base"
      / "broad cost-intensity indicator".
- [x] Cross-company expense-ratio caveat added.

## Operational Leverage Index
- [x] OLI value standardized to 195.3 in 2025 (2023 = 100).
- [x] OLI labelled as author-constructed, equally weighted, sensitive to
      baseline / weighting, appendix-only, not primary evidence.
- [x] No occurrences of OLI = 679.0 anywhere in the draft, reports, or
      integration notes.

## NLP dataset and statistics
- [x] Raw Trustpilot corpus = 1,934.
- [x] Final clean dataset = 1,915 (used for sentiment, ratings, keyword).
- [x] Pre-Betsy n = 1,746; Post-Betsy n = 169; date boundary = October 17,
      2024.
- [x] CEO/scandal filter is applied only to BERTopic.
- [x] Topic-modeling input = 1,804 (not 1,805).
- [x] BERTopic clustered = 1,198; HDBSCAN noise = 606.
- [x] Topic-share denominators reported: Pre clustered non-outlier
      n = 1,077, Post clustered non-outlier n = 121.

## NLP sentiment and ratings
- [x] Star ratings: pre 4.2806 / post 3.8580, Δ = −0.4226, Welch p =
      0.0019, Cohen's d = 0.2899.
- [x] VADER sentiment: pre 0.6416 / post 0.5151, Δ = −0.1265, Welch p =
      0.0057, Cohen's d = 0.2505.
- [x] Decline framed as a triangulation insight, not as proof of harm.

## NLP keyword prevalence
- [x] Cost/Rates 28.92 → 16.57 (Δ −12.35 pp, p = 0.0009, survives
      Bonferroni).
- [x] Digital/Process 32.65 → 23.67 (Δ −8.98 pp, p = 0.0211, fails
      Bonferroni).
- [x] Human Support 43.81 → 40.83 (not significant).
- [x] Speed/Efficiency 52.00 → 44.38 (Δ −7.63 pp, p = 0.0698,
      suggestive).
- [x] Communication 32.53 → 30.77 (not significant).
- [x] Delay/Friction 13.52 → 10.06 (not significant).
- [x] Explicit AI/Automation 1.15 → 1.18 (Fisher exact p = 1.0000).
- [x] AI invisibility framed as descriptive interpretation, not as proven
      finding.

## NPS and customer experience
- [x] NPS 39 → 64 labelled management-reported, unaudited, medium
      reliability.
- [x] Divergence between NPS and Trustpilot framed as a triangulation
      insight.

## BERTopic interpretation
- [x] Topic shifts reported with the +/− pp values exactly as specified
      (HELOC +4.22; Smooth Transaction +4.03; Responsive Service +3.93;
      Closing Timeline +3.55; refinance topics combined −7.66; Home
      Purchase −3.48).
- [x] n = 121 caveat present.

## Chapter 4 readiness
- [x] Chapter 4 remains descriptive; no full Chapter 5 findings imported.
- [x] 2024 framed as a transition year; 2025 as scaling phase.

## Chapter 3 methodology readiness
- [x] Section ordering preserved; section titles cover Research
      Philosophy, Research Design, Case Selection, Data Collection,
      Financial Analysis, NLP Analysis, Operationalization,
      Triangulation Logic, Methodological Limitations, Research Rigor,
      Ethical Considerations.
- [x] Operationalization-of-business-value table inserted.
- [x] Validity / reliability / limitations content present (split across
      Methodological Limitations, Research Rigor, and Ethical
      Considerations subsections).

## Chapter 1 tone
- [x] No occurrences of "exceptionally", "glaringly", "radical departure",
      "glaring empirical void", "profound and irreversible",
      "desperately short", "massive blind spot", "incredibly powerful",
      "unprecedented", or "virtually infinite scalability" remain in the
      draft.
- [x] Second-pass softening of additional promotional phrasing in the
      Introduction ("discontinuous technological leap", "decisively
      shifted ... fundamentally redefining", "unforgiving environment",
      "core driver of competitive advantage", "early and aggressive
      adopter", "extreme margin pressures", "unique and invaluable
      opportunity", etc. — full list in B_inconsistency_table.md row 35).

## Second-pass corrections (supervisor feedback)
- [x] No occurrences of "descriptive benchmark descriptive benchmark"
      (the duplicated phrase in §3.7).
- [x] "controls for broad market recovery" replaced with
      "contextualizes ... against broad market recovery effects".
- [x] "zero risk of GDPR violation" softened to "minimizing GDPR
      exposure ...".
- [x] No occurrences of the typos `imdemonstrating` or `imindicates`
      anywhere in the draft.
- [x] Heading 1 entries carry consistent chapter numbers
      (1. Introduction; 2. Literature Review; 3. Research Methodology;
      4. Case Study Description: ...). References left without a number.
- [x] The "3. The Emergence of Voice AI and LLM Agents" line is now a
      proper Heading 2 (no stray "3." prefix).
- [x] Stale `08_Code/.ipynb_checkpoints/` files removed from version
      control; `.gitignore` excludes them going forward.

## Figure placement
- [x] Recommended main-Chapter-5 figures and appendix-only figures listed
      in `D_chapter_5_outline.md`. The corresponding PNGs already exist
      under `outputs/figures/financial/` and `outputs/figures/NLP/`.

## Chapter 5 status (third-pass update)
- [x] Chapter 5 prose drafted (≈ 7,400 words, in target range
      7,000–9,000) and inserted between Chapter 4 and References in
      `04_Drafts/Main_Draft.docx`.
- [x] All seven supervisor-plan sections present (5.1 Introduction;
      5.2 RQ1; 5.3 RQ2 financial; 5.4 RQ2 customer experience; 5.5
      Triangulated interpretation; 5.6 Limitations; 5.7 Summary).
- [x] Six figures embedded with academic captions and in-text
      references (Figures 5.1–5.6). Appendix-only figures flagged in
      prose, not embedded.
- [x] Forbidden-phrase audit clean ("proves", "caused by Betsy",
      "validates the hypothesis", "transformative results", "positive
      causal", "only achievable through AI", "DiD",
      "Difference-in-Differences", "controls for broad market",
      "imdemonstrating", "imindicates", "exceptionally", "glaring",
      "radical departure", "unprecedented").
- [x] All standardized financial and NLP values present in chapter at
      appropriate points.
- [x] Four new bibliography entries added (Filieri 2015, Grootendorst
      2022, Hutto & Gilbert 2014, Rocket Companies 2024 + 2025).

## Out of scope for this cleanup pass
- [ ] Final cross-reference / numbering of figures and tables across
      the full document (Word will renumber automatically when the TOC
      is rebuilt).
- [ ] Bibliography deduplication / style harmonization; the user has
      flagged the existing bibliography as duplicated / messy and will
      clean it after Chapter 5 is final.
- [ ] Final pandoc / Word styling pass before submission. Note that
      the Chapter-3 sub-section numbering (3.1 ... 3.8) is not
      enforced explicitly in the Heading 2 text; the existing Heading
      2 / 3 structure already covers all eight sub-sections in content
      terms.
- [ ] Chapter 6 (Discussion) — to be written next, building on the
      design-pattern argument previewed at the end of Chapter 5.

These open items are intentionally left for the user; the pre-Chapter-5
cleanup target and the Chapter-5 drafting target are otherwise
complete.
