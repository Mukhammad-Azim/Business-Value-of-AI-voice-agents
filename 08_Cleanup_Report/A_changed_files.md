# A. Changed Sections and Files

This document lists every file and section touched during the pre-Chapter-5
quality-control and consistency cleanup. The cleanup was deliberately
conservative: edits focused on (i) academic-tone softening, (ii) RQ2
re-wording, (iii) removal of "DiD-style" language, (iv) financial-methodology
clarifications, (v) standardization of the finalized financial and NLP
values, (vi) Operational Leverage Index restricted to the appendix, (vii)
NPS / AI-invisibility / topic-modeling caveats, and (viii) figure-placement
guidance. No new analyses were added.

## Files modified

### `04_Drafts/Main_Draft.docx`
The whole-paragraph rewrites and run-level substitutions applied to the
draft are encoded in
[`08_Code/apply_thesis_cleanup.py`](../08_Code/apply_thesis_cleanup.py).
Sections affected:

- **Chapter 1 — Introduction**
  - Broad Context: paragraphs softened to remove "exceptionally",
    "glaringly", "radical departure", and "glaring empirical void".
  - Research Aim and Questions: RQ2 updated verbatim to the final wording.
  - Methodological Contribution: dramatic phrasing replaced with academic
    register; "ensures a validity" rewritten.

- **Chapter 3 — Methodology**
  - 3.2 Research Design: "test the hypothesis of AI-driven operational
    leverage" replaced with "examine evidence consistent with AI-enabled
    operational leverage". Rocket Mortgage explicitly described as a
    directional industry benchmark.
  - 3.4 Data Sources / SEC Financial Filings: rewritten to make explicit
    that the dataset is built from 10 SEC regulatory filing PDFs (Better
    2023, 2024, 2025 10-Ks plus S-1, Rocket 2020–2025 10-Ks with 2018–2019
    coming from historical comparative tables in Rocket's 2020 10-K). The
    extraction paragraph now states explicitly that pdfplumber and pypdf
    were used for text extraction/navigation, no OCR was used, the pipeline
    did not automatically parse tables into final numeric data, final
    values were manually identified and standardized to USD millions, and
    derived metrics were calculated deterministically in Python. The
    final dataset is 13 rows × 15 columns; employee count is headcount.
  - 3.4 Trustpilot Customer Reviews: cleaned to state Pre-Betsy n = 1,746,
    Post-Betsy n = 169, and that the CEO/scandal filter is applied only
    to BERTopic topic modeling, producing a 1,804-document topic-modeling
    input (not 1,805). Rating, sentiment, and keyword analyses use the
    full 1,915-review dataset.
  - 3.5 Financial Ratio and Operational Leverage Analysis (renamed in
    spirit): rewritten to use "broad cost-intensity indicator" and
    "standardized total expense base" language for `Total_Expenses`,
    with an explicit caveat that cross-company expense-ratio comparisons
    are directional rather than precise like-for-like measurements.
    "Difference-in-Differences (DiD) style" replaced with "descriptive
    benchmark comparison against Rocket Mortgage". Three baseline checks
    explicitly named: 2024–2025 (primary), 2023–2025 (recovery from
    trough), and pre-period-average vs 2025 (robustness).
  - 3.6 NLP Text Mining: rewritten to describe sentiment, keyword, and
    BERTopic as complementary techniques. Keyword section now reports
    Cost/Rates 28.92 % → 16.57 % (p = 0.0009, survives Bonferroni),
    Digital/Process 32.65 % → 23.67 % (p = 0.0211, fails Bonferroni),
    Speed/Efficiency 52.00 % → 44.38 % (p = 0.0698, suggestive),
    Human Support / Communication / Delay/Friction not significant,
    and Explicit AI 1.15 % → 1.18 % (Fisher's exact p = 1.0000). The
    "AI invisibility" wording was softened to a descriptive
    interpretation rather than a proven finding. BERTopic section now
    explicitly states 1,804 input documents, 1,198 clustered, 606 noise,
    and clustered non-outlier subsamples Pre n = 1,077 / Post n = 121.
  - 3.7 Operationalization of Business Value: rewritten as a clean section
    introduction followed by a new five-row operationalization table
    mapping operational efficiency, productivity / scalability, financial
    performance, customer experience, and integration to indicators, data
    sources, and reliability levels. NPS (39 → 64) labelled as
    management-reported and medium-reliability. The Operational Leverage
    Index is now described as 195.3 in 2025 (2023 = 100), author-
    constructed, equally weighted, sensitive to baseline / weighting,
    appendix-only, not primary evidence.
  - 3.8 Triangulation Logic: rewritten to use the full-precision finalized
    values: ratings 4.2806 → 3.8580 (Welch's t p = 0.0019, Cohen's d =
    0.2899); VADER 0.6416 → 0.5151 (p = 0.0057, d = 0.2505); BERTopic
    shifts (HELOC +4.22 pp, Smooth Transaction +4.03 pp, Responsive
    Service +3.93 pp, Closing Timeline +3.55 pp, refinance topics
    combined −7.66 pp, Home Purchase −3.48 pp); and the n = 121 caveat.
  - Methodological Limitations: NLP-imbalance paragraph updated to use
    the new clustered-non-outlier denominators.
  - Research Rigor and Reproducibility: "exceptionally high" softened.

- **Chapter 4 — Case Study Description**
  - Pre-Deployment Baseline (2021–2023): 2023 reported revenue aligned to
    $76.8 million (was $77 million in the body text).
  - Transition Year (2024): full-year 2024 revenue $108.5 million,
    net loss $206.3 million, with 2023 comparatives $76.8 million and
    $536.4 million; explicit caveat that improvements cannot be isolated
    to Betsy because most of 2024 preceded the launch.
  - Chapter 4 remains descriptive — financial / NLP findings are flagged
    as belonging in Chapter 5.

- **Cross-cutting substitutions** (every paragraph was scanned for):
  - "Difference-in-Differences (DiD)", "DiD", "DiD-style"
    → "descriptive benchmark comparison against Rocket Mortgage"
  - "validates the hypothesis", "definitively demonstrates",
    "transformative results achieved through AI",
    "only achievable through AI substitution",
    "positive causal interpretation"
    → softened to "consistent with", "associative", "provides
    descriptive evidence consistent with"
  - "exceptionally", "glaring", "radical departure" → softened
  - "AI Invisibility hypothesis" → "AI invisibility interpretation"
  - "test the operational leverage hypothesis" /
    "test the hypothesis of AI-driven operational leverage"
    → "examine evidence consistent with AI-enabled operational leverage"

### `08_Code/financial_metrics_project_report.md`
- All "DiD-style" / "DiD" headings, list items, and prose replaced with
  "descriptive benchmark comparison against Rocket Mortgage".
- Section 6.7 retitled "Descriptive Benchmark Comparison Against Rocket
  Mortgage".
- 2025 attribution sentence ("should be attributed to") softened to
  "should be associated with" and amended to acknowledge that Betsy's
  specific contribution cannot be isolated.

### `08_Code/nlp_project_report.md`
- AI-invisibility paragraph rewritten to remove "Betsy's contribution is
  experienced as faster responses, smoother transactions, and better
  availability — not as 'talking to an AI'", which had read as a proven
  finding. The new wording uses the user-specified register ("the
  near-zero explicit AI mention rate suggests …"; "the keyword analysis
  cannot determine whether individual customers interacted with Betsy").
- Topic-shift sentence ("cannot be causally attributed to Betsy")
  softened to "cannot be associated solely with Betsy".

### `thesis_integration_instructions.md`
- RQ2 paragraph (line 16) updated to use the final RQ2 wording.

### `08_Code/apply_thesis_cleanup.py` (new)
- Reproducible Python pipeline used to apply all run-level
  substitutions, paragraph rewrites, and the operationalization table
  insertion to `04_Drafts/Main_Draft.docx`.

### `09_Cleanup_Report/` (new)
- `A_changed_files.md` (this file).
- `B_inconsistency_table.md` — table mapping each detected
  inconsistency to its old wording / value, corrected wording / value,
  and the file/section where it was changed.
- `C_ready_for_chapter_5_checklist.md` — the final go / no-go checklist
  for Chapter 5.
- `D_chapter_5_outline.md` — the Chapter 5 writing skeleton.
- `E_supervisor_note.md` — short supervisor-style note on readiness.

### `.gitignore` (new, second pass)
- Excludes `.ipynb_checkpoints/` and other Jupyter / Python /
  editor cache directories so stale autosaves cannot drift back into
  the repo. Until this commit, `08_Code/.ipynb_checkpoints/` was
  tracked and contained an out-of-date copy of `nlp_project_report.md`
  with the pre-cleanup RQ2 wording.

## Second-pass changes (supervisor feedback)

A second cleanup pass was applied after the initial PR was opened,
covering eight additional inconsistencies that were not caught in the
first pass.

- **Repeated phrase**: "descriptive benchmark descriptive benchmark
  comparison" in §3.7 (P147) corrected to "descriptive benchmark
  comparison". The duplication arose because the underlying paragraph
  contained both "DiD-style" and "descriptive benchmark"
  formulations, and the first-pass substitution mapped both into
  "descriptive benchmark".
- **"controls for broad market recovery"** (§3.7, P147) replaced with
  "contextualizes Better.com's trajectory against broad market
  recovery effects" so the Rocket-Mortgage benchmark is consistently
  framed as a descriptive context rather than a formal econometric
  control.
- **GDPR phrasing**: "ensuring zero risk of GDPR violation or data
  privacy misuse" (§3.9 ethics paragraph, P150) softened to
  "minimizing GDPR exposure because no personal data was collected,
  linked to identifiable individuals, or stored locally beyond the
  public review text".
- **Typos** `imdemonstrating` and `imindicates` replaced with
  `demonstrating` / `indicates` everywhere in the draft (multiple
  paragraphs in Chapter 1 and Chapter 2 literature review).
- **Chapter 1 promotional tone** softened in P011, P013, P016, P020,
  P024, P025, P026, P027, P030 (full list in B_inconsistency_table.md
  row 35). Examples: "discontinuous technological leap" →
  "substantial technological advance"; "decisively shifted ...
  fundamentally redefining" → "shifted ... reshaping"; "core driver
  of competitive advantage" → "important driver of competitive
  position"; "extreme margin pressures" → "significant macroeconomic
  headwinds and margin pressures".
- **Chapter heading numbering** added to all Heading 1 entries:
  "1. Introduction", "2. Literature Review", "3. Research
  Methodology", "4. Case Study Description: Better.com and the
  Deployment of Voice AI in Mortgage Origination". The References
  heading is intentionally left unnumbered. The misformatted Normal
  paragraph "3. The Emergence of Voice AI and LLM Agents" in
  Chapter 1 was promoted to a Heading 2 with the stray "3." prefix
  removed.
- **Stale Jupyter checkpoints** untracked: `08_Code/.ipynb_checkpoints/`
  (10 files, including `nlp_project_report-checkpoint.md` which
  contained the pre-cleanup RQ2) is removed from version control via
  `git rm --cached`. The new `.gitignore` prevents these files from
  being re-committed. Files remain on disk for the user's local
  Jupyter session.

The second-pass edits are encoded in the same
[`08_Code/apply_thesis_cleanup.py`](../08_Code/apply_thesis_cleanup.py)
script (look for the "Second-pass corrections" comment block in the
SUBSTITUTIONS list, and the new `normalize_chapter_headings()`
function), so the cleanup pipeline remains a single, idempotent
script.

## Third-pass change (Chapter 5 prose)

After the user reviewed the second-pass cleanup, an additional pass was
performed to draft and integrate Chapter 5. This pass added genuinely
new content rather than rewriting existing material.

### `04_Drafts/Main_Draft.docx`
- Chapter 5 inserted between Chapter 4 (Case Study Description) and the
  References section. Length ≈ 7,400 words (excluding figure captions),
  inside the supervisor-plan target of 7,000–9,000 words. Structure:
  - 5.1 Introduction to Empirical Findings
  - 5.2 RQ1: Integration of Voice LLM Agents into Mortgage Origination
    (5.2.1–5.2.5)
  - 5.3 RQ2: Operational and Financial Business Value (5.3.1–5.3.6)
  - 5.4 RQ2: Customer Experience and NLP Evidence (5.4.1–5.4.5)
  - 5.5 Triangulated Interpretation
  - 5.6 Limitations and Boundary Conditions of the Empirical Findings
  - 5.7 Summary of Empirical Findings
- Six figures embedded with academic-style captions (Figure 5.1: core
  financial trajectory; Figure 5.2: expense ratio + operating cash flow;
  Figure 5.3: headcount + RPE; Figure 5.4: VADER sentiment by period;
  Figure 5.5: keyword group prevalence; Figure 5.6: topic-share
  changes). Appendix-only figures (OLI composite index, intertopic
  distance map, topic-word importance, quarterly keyword trends,
  profitability/cash-flow benchmark) are flagged in the prose but not
  embedded in Chapter 5.
- Bibliography extended with four new references required by the new
  prose: Filieri (2015), Grootendorst (2022), Hutto & Gilbert (2014),
  and Rocket Companies, Inc. (2024) and (2025). Existing entries were
  not modified; bibliography deduplication remains deferred per the
  original brief.

### `08_Code/insert_chapter5.py` (new file)
- Idempotent script that inserts the Chapter 5 prose, figures, and
  captions immediately before the References Heading 1 in
  `04_Drafts/Main_Draft.docx`. Re-running the script on a draft that
  already contains Chapter 5 is a no-op.

### `08_Code/extend_chapter5.py` (new file)
- Idempotent companion script that inserts additional paragraphs
  anchored on unique substrings within the existing Chapter 5. Used to
  bring section word-counts within the supervisor-plan ranges. Each
  new paragraph is fingerprinted to make re-runs idempotent.

### `09_Cleanup_Report/Chapter_5_Empirical_Findings.docx` (new file)
- Standalone Word document containing only Chapter 5 (with figures and
  captions). Provided so the user can review the chapter independently
  of the full thesis draft.

### `09_Cleanup_Report/Chapter_5_Empirical_Findings.md` (new file)
- Markdown rendering of Chapter 5 prose (figures rendered as italic
  caption blocks). Provided as a quick-read preview; not the canonical
  artifact.

The Chapter 5 prose was audited end-to-end against the forbidden-phrase
list from the original 20-point brief. No occurrences of "proves",
"caused by Betsy", "definitively demonstrates", "validates the
hypothesis", "transformative results", "positive causal", "only
achievable through AI", "DiD" / "Difference-in-Differences", "controls
for broad market", or any of the Chapter 1 dramatic phrasings were
found in the inserted text. All standardized financial values
($76.8 / $108.5 / $164.9 M revenue, $368.1 / $313.9 / $330.7 M expense
base, expense ratio 4.79 / 2.89 / 2.01, RPE $0.094 / $0.087 / $0.124 M,
net loss −$536.4 / −$206.3 / −$165.9 M, OLI = 195.3 in appendix
context) and standardized NLP values (4.2806 → 3.8580, p = 0.0019,
d = 0.2899; 0.6416 → 0.5151, p = 0.0057, d = 0.2505; Cost/Rates
28.92 → 16.57 %, p = 0.0009 surviving Bonferroni; Digital/Process
32.65 → 23.67 %, p = 0.0211; Explicit AI 1.15 → 1.18 %, Fisher
p = 1.0000; Pre n = 1,746 / Post n = 169; clustered non-outlier
denominators 1,077 / 121) appear in the chapter at the appropriate
points.

## Files explicitly NOT changed (and why)

- `04_Drafts/Backup/Main_Draft.docx` — backup snapshot, left intact.
- `04_Drafts/Thesis-Structure.docx` — high-level structural document, not
  in scope of this cleanup pass.
- `05_Notes/Note-TDK-April.docx`, `05_Notes/Notes.docx`,
  `05_Notes/2025_Earnings_AI_Findings.md` — author working notes; not
  part of the chapter narrative.
- `08_Code/cleaning_reviews.ipynb`,
  `08_Code/better_reviews_topic_modeling.ipynb`,
  `08_Code/financial_metric_analysis.ipynb` — the analytical pipelines
  themselves were not re-run; only the human-language reports next to
  them were edited.
- All CSV / JSON outputs and figure PNGs under `outputs/` — finalized
  values were already correct in the upstream data; no re-export needed.
