# Deliverable A — Citation Audit Table

> **Scope**: This table audits every unique in-text citation key found in `04_Drafts/Main_Draft.docx`, covering Chapters 1–5 (paragraphs 0–353; reference list begins at paragraph 354). The thesis contains **305 raw citation matches** which deduplicate to **51 unique citation keys** after filtering numerical/figure-caption false positives (e.g., "p = 0.0009", "Q3 2023", "$76.8 million in 2023").
>
> **Columns**:
> 1. **Citation key (as written)** — the exact form found in the thesis, including narrative ("Andrade and Tumelero, 2022") vs parenthetical ("Andrade & Tumelero, 2022") variants
> 2. **Count** — number of in-text occurrences
> 3. **Primary location(s)** — chapter / section where most occurrences appear
> 4. **Claim being supported** — the substantive claim the citation backs
> 5. **Current reference-list match** — whether a clear matching entry exists in the current (pre-rebuild) reference list
> 6. **Status** — matched / orphaned / ambiguous / duplicate / wrong-year / wrong-author / incomplete / unreliable / needs-rewording
> 7. **Required action**
> 8. **Corrected in-text citation** — APA 7-conformant final form
> 9. **Corrected reference key** — matches Deliverable B
>
> **Caveat on extraction**: Citation occurrences embedded inside figure captions, table cells, and footnotes are tied to their parent paragraph. When a paragraph contains both a real citation and a numerical figure (e.g., "p = 0.0009"), the latter has been filtered out manually.

---

## A.1 Academic / Peer-Reviewed Sources

| # | Citation Key (as written) | Count | Primary Location(s) | Claim Supported | Current Ref Match? | Status | Required Action | Corrected In-Text | Corrected Reference Key |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Abdulquadri et al., 2021 | 1 | Ch. 2 (literature review) | Chatbot adoption in Nigerian financial services | Yes | matched | None | (Abdulquadri et al., 2021) | Abdulquadri, A., Mogaji, E., Kieu, T. A., & Nguyen, N. P. (2021) |
| 2 | Adam et al., 2021 | 4 | Ch. 2 + Front matter | Chatbot-compliance experimental findings | Yes (duplicate above + below `---`) | duplicate-in-reflist | Merge duplicate ref entries | (Adam et al., 2021) | Adam, M., Wessel, M., & Benlian, A. (2021) |
| 3 | Aggarwal et al., 2025 | 12 | §5.1, §5.5, Ch. 2 | Voice-AI value-creation/appropriation framework | Yes (duplicate above + below `---`) | duplicate-in-reflist | Merge duplicate ref entries | (Aggarwal et al., 2025) | Aggarwal, A., Kumar, V., & Srivastava, R. K. (2025) |
| 4 | Andrade & Tumelero, 2022 | 2 | Ch. 2 + Front matter | AI chatbot customer-service efficiency | Yes (duplicate above + below `---`) | duplicate-in-reflist | Merge duplicate ref entries | (Andrade & Tumelero, 2022) | Andrade, I. M. D., & Tumelero, C. (2022) |
| 5 | Andrade and Tumelero, 2022 | 8 | Ch. 2 + Front matter | (same source, narrative form) | Yes | needs-rewording (APA 7 narrative is OK; check usage) | Confirm "and" only used in narrative form; convert to "&" inside parentheses | "Andrade and Tumelero (2022)" (narrative) / "(Andrade & Tumelero, 2022)" (parenthetical) | Andrade, I. M. D., & Tumelero, C. (2022) |
| 6 | Becker et al., 2025 | 1 | Ch. 2 (voice naturalness) | Robot-voice naturalness/trust findings | Yes (duplicate as separate entries) | duplicate-in-reflist | Merge duplicate ref entries | (Becker et al., 2025) | Becker, D., Braach, L., Clasmeier, L., Kaufmann, T., Ong, O., Ahrens, K., Gäde, C., Strahl, E., Fu, D., & Wermter, S. (2025) |
| 7 | Blümel et al., 2024 | 4 | §5.5 + Ch. 2 | Relational personalization framework | Yes (duplicate above + below `---`) | duplicate-in-reflist | Merge duplicate ref entries | (Blümel et al., 2024) | Blümel, J. H., Zaki, M., & Bohné, T. (2024) |
| 8 | Brynjolfsson et al., 2023 | 4 | §5.1, §5.4.1, Ch. 2 | Generative-AI productivity findings | Yes (duplicate above + below `---`) | duplicate-in-reflist | Merge duplicate ref entries | (Brynjolfsson et al., 2023) | Brynjolfsson, E., Li, D., & Raymond, L. R. (2023) |
| 9 | Filieri, 2015 | 2 | §5.4.2 + Ch. 2 | UGC trust antecedents | Yes | matched | None | (Filieri, 2015) | Filieri, R. (2015) |
| 10 | Fotheringham and Wiles, 2023 | 4 | Ch. 2 + Front matter | Stock-return event-study on chatbot adoption | Yes (duplicate above + below `---`); narrative form used in parenthetical context | needs-rewording + duplicate-in-reflist | Merge duplicate ref entries; convert parenthetical "and" → "&" | "Fotheringham and Wiles (2023)" (narrative) / "(Fotheringham & Wiles, 2023)" (parenthetical) | Fotheringham, D., & Wiles, M. A. (2023) |
| 11 | Goodhue & Thompson, 1995 | 2 | §5.2.5, §5.5 | Task-technology fit framework | Yes | matched | None | (Goodhue & Thompson, 1995) | Goodhue, D. L., & Thompson, R. L. (1995) |
| 12 | Goodhue and Thompson, 1995 | 1 | §5.2.1 (narrative) | Same source, narrative form | Yes | matched | None | "Goodhue and Thompson (1995)" (narrative form) | Goodhue, D. L., & Thompson, R. L. (1995) |
| 13 | Grootendorst, 2022 | 3 | §5.4.4 + Ch. 2 | BERTopic methodology | Yes | matched | None | (Grootendorst, 2022) | Grootendorst, M. (2022) |
| 14 | Hentzen et al., 2022 | 6 | §5.2.1, §5.2.5, Ch. 2 | AI-in-financial-services SLR | Yes (duplicate above + below `---`) | duplicate-in-reflist | Merge duplicate ref entries | (Hentzen et al., 2022) | Hentzen, J. K., Hoffmann, A., Dolan, R., & Pala, E. (2022) |
| 15 | Heskett et al., 1994 | 1 | Ch. 2 / §5.4.2 | Service-profit-chain framework | **No** — orphaned | **orphaned** | Add full reference (verified at HBR March–April 1994) | (Heskett et al., 1994) | Heskett, J. L., Jones, T. O., Loveman, G. W., Sasser, W. E., Jr., & Schlesinger, L. A. (1994) |
| 16 | Huang & Rust, 2018 | 2 | §5.2.5 + Front matter | AI-in-service typology | Yes (duplicate above + below `---`) | duplicate-in-reflist | Merge duplicate ref entries | (Huang & Rust, 2018) | Huang, M.-H., & Rust, R. T. (2018) |
| 17 | Huang and Rust, 2018 | 3 | §5.5 + Ch. 2 | Same source, narrative form | Yes | matched | None | "Huang and Rust (2018)" (narrative form) | Huang, M.-H., & Rust, R. T. (2018) |
| 18 | Hutto & Gilbert, 2014 | 2 | §5.4.2 + Ch. 2 | VADER methodology | Yes | matched | None | (Hutto & Gilbert, 2014) | Hutto, C. J., & Gilbert, E. (2014) |
| 19 | Jang et al., 2021 | 1 | Ch. 2 | Manager understanding of chatbots in Korean banking | Yes (current entry: Jang, M., Jung, Y., & Kim, S., 2021 — different from author originally cited) | wrong-author **(needs author confirmation)** | Confirm author group; the existing reference-list entry has different authors than the prior session may have referenced (Jang, Jung, & Kim 2021 ≠ Jang, Kim, & Baek 2021). Recommend keeping the existing entry as Jang et al. (2021) and verifying the underlying paper is the one cited | (Jang et al., 2021) | Jang, M., Jung, Y., & Kim, S. (2021) — **author confirmation needed** |
| 20 | Liu et al., 2024 | 7 | §5.2.3 + Ch. 2 | AI in investment efficiency | Yes (duplicate above + below `---`) | duplicate-in-reflist | Merge duplicate ref entries | (Liu et al., 2024) | Liu, Z., Zhang, K., & Zhang, H. (2024) |
| 21 | Luca, 2016 | 2 | §5.4.2 + Ch. 2 | Yelp-rating economic impact | Yes | matched | None | (Luca, 2016) | Luca, M. (2016) |
| 22 | Maslych et al., 2025 | 2 | Ch. 2 (latency mitigation) | LLM-IVA latency findings | Yes (URL needs minor verification — current ref shows arxiv.org/abs/2507.22352 vs the verified abs/2504.08507) | needs-verification | Confirm correct arXiv ID against the paper's bibliographic record | (Maslych et al., 2025) | Maslych, M., Katebi, M., Lee, C., Hmaiti, Y., Ghasemaghaei, A., Pumarada, C., Palmer, J., Martinez, E. S., Emporio, M., Snipes, W., McMahan, R. P., & LaViola, J. J. (2025) |
| 23 | Mogaji & Nguyen, 2021 | 4 | §5.2.5, §5.4.3 | Manager-AI cross-country study | Yes (duplicate above + below `---`) | duplicate-in-reflist | Merge duplicate ref entries | (Mogaji & Nguyen, 2021) | Mogaji, E., & Nguyen, N. P. (2021) |
| 24 | Mogaji and Nguyen, 2021 | 4 | §5.2.1 + Ch. 2 | Same source, narrative form | Yes | matched | None | "Mogaji and Nguyen (2021)" (narrative form) | Mogaji, E., & Nguyen, N. P. (2021) |
| 25 | Nussbaum et al., 2025 | 1 | Ch. 2 | Voice-naturalness perception | Yes | matched | None | (Nussbaum et al., 2025) | Nussbaum, C., Frühholz, S., & Schweinberger, S. R. (2025) |
| 26 | Reddy, 2017 | 1 | Ch. 2 ("as cited in Andrade & Tumelero, 2022") | Innovation-activity mediation | **Secondary citation only** — per APA 7 §8.6 only the secondary source needs a reference-list entry | matched (as secondary) | Keep the in-text "as cited in" form; no Reddy (2017) entry in reference list | (Reddy, 2017, as cited in Andrade & Tumelero, 2022) | (no separate entry — secondary only) |
| 27 | Wang et al., 2023 | 9 | §5.2.2, §5.4.1, Ch. 2 | Voice-AI call-center field experiment | Yes (one entry uses "Wang, L., et al." truncated; another lists 6 full authors) | duplicate-in-reflist + incomplete | Replace the truncated "Wang et al." entry with the full 6-author entry per APA 7 §9.8 | (Wang et al., 2023) | Wang, L., Huang, N., Hong, Y., Liu, L., Guo, X., & Chen, G. (2023) |
| 28 | Xu et al., 2020 | 1 | Ch. 2 | AI customer-service task complexity | Yes | matched | None | (Xu et al., 2020) | Xu, Y., Shieh, C.-H., van Esch, P., & Ling, I.-L. (2020) |
| 29 | Yin, 2018 | 1 | Ch. 3 (case-study methodology) | Case-study research methodology | **No** — orphaned | **orphaned** | Add full reference (verified at SAGE 6th ed.) | (Yin, 2018) | Yin, R. K. (2018) |
| 30 | Zhang et al., 2023 | 7 | §5.2.2, §5.4.1, Ch. 2 | AI conversational-agent operational performance | Yes (duplicate above + below `---`) | duplicate-in-reflist | Merge duplicate ref entries | (Zhang et al., 2023) | Zhang, Z., Li, B., & Liu, L. (2023) |
| 31 | (Acemoglu & Restrepo, 2019) | inferred from §5.2.4 narrative ("Acemoglu and Restrepo's framework") | §5.2.4 | Automation/displacement framework | Yes (now in current ref list) | matched (after adding) | Confirm in-text citation form is added | (Acemoglu & Restrepo, 2019) / "Acemoglu and Restrepo (2019)" | Acemoglu, D., & Restrepo, P. (2019) |

---

## A.2 Better-Related Corporate Sources

| # | Citation Key (as written) | Count | Primary Location(s) | Claim Supported | Current Ref Match? | Status | Required Action | Corrected In-Text | Corrected Reference Key |
|---|---|---|---|---|---|---|---|---|---|
| 32 | Better HoldCo, Inc., 2021 | 1 | Ch. 2 / Ch. 4 (pre-merger context) | $1.5B bridge financing + SoftBank/SPAC context | Yes | matched | None | (Better HoldCo, Inc., 2021) | Better HoldCo, Inc. (2021, November 30) |
| 33 | Better HoldCo, Inc., 2023 | 1 | Ch. 4 + §5.3 (pre-period audited financials) | S-1 disclosures, Tinman platform | Yes | matched | None | (Better HoldCo, Inc., 2023) | Better HoldCo, Inc. (2023, December 20) |
| 34 | Better Home & Finance Holding Company, 2022 | 2 | Ch. 4 / §5.1 (pre-merger context) | Pre-merger statements | **No** — anachronistic (entity didn't exist in 2022 as a public company) | **orphaned + wrong-year** | Replace with **(Better HoldCo, Inc., 2021)** for SPAC/bridge-financing claims; with **(Better HoldCo, Inc., 2023)** for retrospective 2021–2022 audited statements; or with **(Primack, 2021)** for SPAC-delay context | (depends on context — see Deliverable G §G.14) | (Better HoldCo, Inc., 2021/2023) or (Primack, 2021) |
| 35 | Better Home & Finance Holding Company, 2024a | 12 | §5.1, §5.2.2, §5.4.2 (Betsy launch context) | Betsy launch press release; "≥35% reduction" claim; $9k industry baseline; vendor-side framing | Yes | matched | None | (Better Home & Finance Holding Company, 2024a) | Better Home & Finance Holding Company (2024a, October 17) |
| 36 | Better Home & Finance Holding Company, 2024b | 6 | §5.3.1, §5.3.3 (Q3 2024 financials) | Q3 2024 quarterly numbers; first post-Betsy disclosures | Yes | matched | None | (Better Home & Finance Holding Company, 2024b) | Better Home & Finance Holding Company (2024b, November 12) |
| 37 | Better Home & Finance Holding Company, 2024c | 1 | Ch. 2 / §5 | (no third 2024 Better-only source) | **No** — orphan | **orphaned** | Replace with **2024b** (only post-Betsy 2024 source available) | (Better Home & Finance Holding Company, 2024b) | Better Home & Finance Holding Company (2024b, November 12) |
| 38 | Better Home & Finance Holding Company, 2025 | 5 | Ch. 2 (no suffix used) | Various 2025 management claims | Yes (ambiguous) | **ambiguous** — three Better-only 2025 sources exist (2025a/b/c) | Disambiguate by context to **2025a** (Q4/FY 2024), **2025b** (Q1 2025), or **2025c** (Q2 2025) | (Better Home & Finance Holding Company, 2025a / 2025b / 2025c) | (depends on context) |
| 39 | Better Home & Finance Holding Company, 2025a | 6 | §5.3.6 + Ch. 2 | FY 2024 results / NPS / "115k interactions" baseline / "$2,000 sales-labor savings" | Yes (current ref says "First quarter 2025 earnings call transcript [S&P Global]") | **wrong-source-type-mapping** | Reassign **2025a** to **Q4/FY 2024 results press release** (date March 18, 2025); reassign Q1 2025 transcript reference to **2025b**; current "2025a, May 13" should be relabeled. Use SEC EDGAR URL for Q1 2025 results 8-K Exhibit 99.1 instead of paid S&P Global transcript for traceability. | (Better Home & Finance Holding Company, 2025a) | Better Home & Finance Holding Company (2025a, March 18) — Q4/FY 2024 results press release |
| 40 | Better Home & Finance Holding Company, 2025b | 4 | §5.4.1 + Ch. 2 | Q1 2025 results / NPS update | Yes (current ref says "Second quarter 2025 earnings call transcript [S&P Global]") | **wrong-source-type-mapping** | Reassign **2025b** to **Q1 2025 results press release** (May 13, 2025; SEC EDGAR Exhibit 99.1) | (Better Home & Finance Holding Company, 2025b) | Better Home & Finance Holding Company (2025b, May 13) — Q1 2025 results 8-K Exhibit 99.1 |
| 41 | Better Home & Finance Holding Company, 2026 | 10 | §5.2.1 + multiple §5 sections | FY 2025 audited financials | Yes (also appears as "2026a" in 4 occurrences for the same 10-K) | matched + duplicate-suffix | Standardize all "2026a" → "2026" because only one Better-only 2026 source exists | (Better Home & Finance Holding Company, 2026) | Better Home & Finance Holding Company (2026) — Form 10-K FY 2025 |
| 42 | Better Home & Finance Holding Company, 2026a | 4 | Ch. 2 (same Form 10-K, different suffix) | (same as #41) | Yes | duplicate-suffix | Replace all "2026a" → "2026" | (Better Home & Finance Holding Company, 2026) | (same as #41) |
| 43 | Better Home & Finance Holding Company & ElevenLabs, 2026 | 19 | §5.2.3, §5.2.4 + multiple | "115k → 700k interactions"; "+30% conversion uplift"; deployment scale | Yes (duplicate entries — appears 3x in current ref list) | duplicate-in-reflist | Merge duplicate ref entries | (Better Home & Finance Holding Company & ElevenLabs, 2026) | Better Home & Finance Holding Company, & ElevenLabs (2026, February 25) |
| 44 | ElevenLabs, 2026 | 12 | §5.1, §5.2.2 + multiple | Voice-engine implementation; latency targets | Yes (duplicate entries — appears 2x in current ref list with different metadata) | duplicate-in-reflist + incomplete-metadata | Merge entries; canonical is the ElevenLabs case-study blog post | (ElevenLabs, 2026) | ElevenLabs (2026, February 9) |

---

## A.3 Industry / Government / News Sources

| # | Citation Key (as written) | Count | Primary Location(s) | Claim Supported | Current Ref Match? | Status | Required Action | Corrected In-Text | Corrected Reference Key |
|---|---|---|---|---|---|---|---|---|---|
| 45 | Consumer Financial Protection Bureau, 2024 | 3 | §5.2.4 + Ch. 2 | Mortgage-closing process and consumer disclosures | Yes | matched | None | (Consumer Financial Protection Bureau, 2024) | Consumer Financial Protection Bureau (2024, May 28) |
| 46 | Federal Reserve Bank of New York, 2023 | 1 | Ch. 2 / §5.4.3 | Pandemic refinance-boom context | Yes | matched | None | (Federal Reserve Bank of New York, 2023) | Federal Reserve Bank of New York (2023, May 15) |
| 47 | Freddie Mac, 2021 | 1 | Ch. 2 | 2020 refinance trends | Yes | matched | None | (Freddie Mac, 2021) | Freddie Mac (2021, March 5) |
| 48 | Freddie Mac, 2024 | 2 | Ch. 2 / §5.4.3 | Cost-to-originate study | Yes | matched | None | (Freddie Mac, 2024) | Freddie Mac (2024, May 13) |
| 49 | Mortgage Bankers Association, 2024 | 6 | §5.3.1, §5.3.6 (industry benchmarks) | Industry-average production cost; quarterly IMB profitability | Yes (current ref list has TWO MBA 2024 entries — full-year report at para 379 and Q3 IMB profits release at para 408 — but in-text uses single "2024" key without suffix) | **ambiguous** | Disambiguate to **2024a** (full-year report) for industry-average / benchmark uses; **2024b** (Q3 IMB profits release) for "$701 per loan" / Q3-specific uses | (Mortgage Bankers Association, 2024a) / (Mortgage Bankers Association, 2024b) | Mortgage Bankers Association (2024a) / (2024b, November 14) |
| 50 | Nunes, 2024 | 2 | Ch. 2 / §5.4.2 | News reportage of Betsy launch | Yes | matched | None | (Nunes, 2024) | Nunes, F. F. (2024, October 17) |
| 51 | Primack, 2021 | 1 | Ch. 2 / Ch. 4 (SPAC-delay context) | Better.com SPAC delay reportage | Yes | matched | None | (Primack, 2021) | Primack, D. (2021, December 8) |
| 52 | Rocket Companies, 2024 | 2 | §5.3.2, §5.3.5 (comparator firm) | Rocket comparator financials | Yes (current ref list has TWO Rocket entries — 2024 [10-K for FY 2024] and 2025 [10-K for FY 2025]) | matched | None | (Rocket Companies, Inc., 2024) | Rocket Companies, Inc. (2024) — Form 10-K FY 2023 (or FY 2024 — author should confirm which fiscal year is being referenced; the in-text "2024" suggests FY 2023's 10-K filed in 2024) |

---

## A.4 Summary Statistics

| Metric | Count |
|---|---|
| Raw citation matches (regex) | 305 |
| After filtering false positives | 240 |
| Unique citation keys (after deduplication) | **51** |
| Citations with matched reference entries | 41 |
| **Orphaned citations** | **5** (Better 2022 ×2; Better 2024c; Heskett et al., 1994; Yin, 2018) — **all resolved** in Deliverable E |
| Ambiguous suffix citations needing disambiguation | **3 keys** (Better 2025 [no suffix]; Better 2026/2026a; MBA 2024 [no suffix]) |
| Citations with narrative/parenthetical "&" vs "and" inconsistency | **5 keys** (Andrade & Tumelero; Fotheringham & Wiles; Goodhue & Thompson; Huang & Rust; Mogaji & Nguyen) |
| Citation keys requiring author/source-type confirmation | **3** (Jang et al. 2021; Maslych et al. 2025 arXiv ID; Rocket Companies 2024 fiscal year) |
| Reference-list entries with duplicates | **11+** (see Deliverable B "Notes on Removed Duplicates") |
| Reference-list entries with missing URLs ("Retrieved from [BLANK]") | 3 — **all resolved** in Deliverable B |

---

## A.5 Action-Summary by Citation

The required actions across all 51 unique keys are:

| Action Category | Count | Examples |
|---|---|---|
| **None — already matched and APA 7-conformant** | 19 | Abdulquadri 2021; Filieri 2015; Goodhue & Thompson (paren); Grootendorst 2022; Hutto & Gilbert 2014; Luca 2016; Nussbaum 2025; Xu 2020; CFPB 2024; FRBNY 2023; Freddie Mac 2021/2024; Nunes 2024; Primack 2021; Rocket 2024; Better HoldCo 2021/2023; Better 2024a/2024b |
| **Merge duplicates in reference list** | 12 | Adam 2021; Aggarwal 2025; Andrade 2022; Becker 2025; Blümel 2024; Brynjolfsson 2023; Hentzen 2022; Huang & Rust 2018 (paren); Liu 2024; Mogaji & Nguyen 2021 (paren); Wang 2023; Zhang 2023; Better×ElevenLabs 2026; ElevenLabs 2026 |
| **Convert narrative-form parenthetical "and" to "&"** (no change to ref entry) | 5 | Andrade and Tumelero (paren only); Fotheringham and Wiles (paren only); Goodhue and Thompson (paren only); Huang and Rust (paren only); Mogaji and Nguyen (paren only) |
| **Add new reference-list entry (orphan resolution)** | 3 | Heskett et al. 1994; Yin 2018; Acemoglu & Restrepo 2019 (inferred) |
| **Replace orphan with corrected citation** | 3 | Better 2022 (×2 occurrences); Better 2024c |
| **Disambiguate ambiguous suffix** | 3 | Better 2025 (no suffix); Better 2026 ↔ 2026a; MBA 2024 (no suffix) |
| **Reassign source-type/date** | 2 | Better 2025a / 2025b: switch from "earnings call transcript [S&P Global]" to **8-K Exhibit 99.1 / press release** for traceability |
| **Confirm author group / fiscal year / arXiv ID** | 3 | Jang et al. 2021; Maslych et al. 2025; Rocket Companies 2024 |
| **Total unique keys audited** | **51** | |

---

## A.6 Cross-Reference to Other Deliverables

| Issue Type | See Deliverable |
|---|---|
| Rebuilt canonical reference list | **B** |
| Same-author same-year suffix mapping | **C** |
| Better/ElevenLabs URL verification | **D** |
| Orphaned-citation resolution detail | **E** |
| Source-reliability classification | **F** |
| Substantive text patches (Cost/Rates, NPS, etc.) | **G** |
| Final QC checklist | **H** |
