# Next Steps and Thesis Improvement Report

**Thesis:** *Business Value of Voice LLM Agents in Financial Services: Evidence from Better.com*
**Author:** Mukhammad Azim Khadyatullaev — Corvinus University of Budapest
**Reviewer role:** Senior MSc thesis supervisor / academic editor / IS scholar
**Document scope:** Full big-picture review and concrete improvement roadmap to reach submission-ready state.
**Review base:** `04_Drafts/Main_Draft.docx` (433 paragraphs, 6 inline figures, 2 tables, References), `09_Cleanup_Report/Chapter_5_Empirical_Findings.md`, `08_Code/financial_metrics_project_report.md` (543 lines), `08_Code/nlp_project_report.md` (409 lines), `10_Citation_Audit/A–H` (post-PR #2 state), `Chapter5_Critical_Review.md`.

---

## 1. Executive Summary

The thesis is in a substantively stronger condition than the chapter list suggests. After the Citation Audit / Reference Rebuild work in PR #2, Chapters 1–5 form a coherent, methodologically careful, and empirically triangulated argument. The defensible central claim — *Better.com's post-deployment trajectory is consistent with AI-enabled operational leverage when interpreted alongside the qualitative case evidence on Betsy/Tinman integration, while customer-experience effects appear uneven, mediated, and possibly under-detected by any single instrument* — is a publishable-quality MSc thesis claim. The reference list (52 deduplicated APA 7 entries), the empirical pipeline, and the Chapter 4–5 argument structure are all near submission grade.

What is **missing or weak** is also clear and concrete:

1. **Chapters 6 (Design Pattern), 7 (Discussion), 8 (Limitations), and 9 (Conclusion) do not exist in the docx.** The body ends at Chapter 5 §5.7 (paragraph 353) and jumps directly to the References block (paragraph 354). The Introduction explicitly promises Chapter 6 ("Chapter 6 develops the design-pattern argument") but the file does not contain it. This is the single largest gap and the highest-priority work item.
2. **Two duplicate tables in the docx instead of three distinct ones.** The docx contains two copies of the same 6×4 "Business value dimension / Indicators / Data source / Reliability" table at the points where (a) the Operationalization Table and (b) the Source Reliability / Data Provenance Table should appear. The Chapter 2 "Table 1 — Dimensions of Business Value Creation through AI in Customer Service" is referenced in §99–100 but has no body — only its title.
3. **The literature review is missing one promised subsection.** §57 promises a five-strand review (AI in financial services → conversational AI → voice AI / LLM agents → business value of AI → consumer behavior and AI interaction). The fifth strand ("Consumer Behavior and AI Interaction") is not present. The lit review currently runs four strands and ends at the business-value section.
4. **Two reference entries are orphans:** Hevner et al. (2004) and Qualtrics (2024) appear in the rebuilt reference list but are never cited in the body. Hevner is salvageable (cite once in Chapter 6 design pattern). Qualtrics should either be re-cited in §5.4 NPS context or removed.
5. **Two methodological tables are referenced but not visibly embedded.** §99–100 ("Table 1 — Dimensions of Business Value …") and §122 ("data provenance classification … presented in Table 1") both refer to tables that are either absent or duplicated. The thesis loses analytical clarity here.
6. **No abstract, no acknowledgments, no table of contents, no list of figures, no list of tables, no list of abbreviations, no appendices block.** The docx begins directly with the title and Chapter 1 heading.
7. **Wording / academic tone:** ~69 occurrences of inflated adjectives (*important, critical, substantial, fundamentally, vital, revolutionizes*), most concentrated in Chapter 1 §11–§35. These should be downgraded or removed.
8. **A small number of high-risk claims remain insufficiently caveated** (e.g., the unattributed 2024 *Qualtrics* NPS benchmark; the headline "approximately 52% revenue growth and only approximately 5% expense growth" in §352 should retain its "consistent with operational leverage" qualifier).
9. **No empirical chapter has reproducibility or computational appendix.** The docx does not yet contain Appendix A (financial dataset), Appendix B (NLP dataset and code), Appendix C (statistical tables and OLI construction), Appendix D (citation audit summary), or any other annex.

The overall assessment is that **with one intensive focused work block** — write Chapters 6–9, fix the duplicate / missing tables, restore the consumer-behavior literature subsection, embed the appendices, polish wording — the thesis is **approximately three to four working days** away from supervisor-ready state. The empirical core does not need to be redone; the research questions are answerable with the data already analyzed; and the citation system is already repaired. The remaining work is primarily *building* (Ch 6–9) and *consolidation* (tables, appendices, polish) rather than re-analysis.

This report is organized to give you, for each weak area, a concrete action: what to add, what to delete, what to soften, what to move, and where in the existing draft each change applies. Section 13 contains paragraph-level outlines for the four missing chapters. Section 15 is a prioritized work plan you can execute against.

---

## 2. Current Thesis Diagnosis (Reconstructed Summary)

### 2.1 What the thesis is actually doing (≈400 words)

The thesis examines **whether and how the deployment of a voice-based Large Language Model (LLM) agent in a regulated U.S. financial-services workflow can be associated with measurable business value**, using **Better.com** as a single revelatory case. The empirical event of interest is the October 17, 2024 launch of **Betsy**, Better's voice AI loan assistant, layered on **Tinman**, Better's proprietary mortgage origination platform, and powered by **ElevenLabs Agents** as the voice infrastructure.

Two research questions structure the work. **RQ1** asks how Betsy was integrated into Better's mortgage origination process and what architectural, workflow, and human-AI collaboration prerequisites this integration implies. **RQ2** asks what measurable business value can be associated with Better's voice AI deployment across operational efficiency, productivity, customer experience, and financial performance, and what factors mediate the realization of that value.

The methodological design is a **convergent parallel mixed-methods single-case study** grounded in pragmatist philosophy (Chapter 3). Three evidence streams run in parallel and are triangulated in Chapter 5: (i) **qualitative process-tracing** of Better's public disclosures, vendor materials, and industry context, used primarily to answer RQ1; (ii) **longitudinal financial analysis** of Better.com 10-K filings (2021–2025) and Rocket Mortgage as a directional industry benchmark (2018–2025), supporting RQ2's operational/financial dimension; and (iii) **NLP analysis of 1,915 cleaned Trustpilot reviews** segmented around Betsy's launch, supporting RQ2's customer-experience dimension.

The empirical findings reach a careful and defensible conclusion. RQ1 is answered by identifying four prerequisites: a process-aware operating platform (Tinman), a coordination-layer scoping of the voice agent (Betsy as routine-communication interface, not underwriter), low-latency voice infrastructure (ElevenLabs), and an explicit human-in-the-loop governance structure. RQ2 is answered by reporting that the post-transition period is *consistent with* AI-enabled operational leverage in the financial-operational dimension (revenue +52% / expense +5% between 2024–2025; expense ratio 2.89 → 2.01; net loss narrowing 19.6%; RPE +42.9% to $0.124M but still below the pre-period $0.130M average) and *mixed* in the customer-experience dimension (management-reported NPS rises 39 → 64; independent Trustpilot star rating declines 4.28 → 3.86 with p = 0.0019, d = 0.29; VADER sentiment declines 0.642 → 0.515 with p = 0.0057, d = 0.25; explicit AI mentions remain at ~1% in both periods).

The thesis's central contribution is to demonstrate that **voice AI in financial services creates multidimensional, mediated business value rather than uniformly directional improvement**, and that the integration mechanism (process-aware platform + scoped voice agent + voice infrastructure + human escalation) is a transferable configuration. This is a credible MSc-level empirical contribution.

### 2.2 Where the thesis already succeeds

| Area | Why it works |
|---|---|
| **Cautious causal language** | Throughout Chapter 5 the wording is "consistent with," "associated with," "directionally," "the broader Betsy/Tinman AI operating model" rather than "Betsy caused." This is appropriate for a single-case observational design. |
| **Chapter 4 narrative** | The Tinman / Betsy / ElevenLabs separation in Chapter 4 is excellent: each component is explained in its own subsection, vendor evidence is explicitly treated as moderate-strength, and the human-AI collaboration model is correctly framed as task reallocation, not labor substitution. |
| **Triangulation logic** | The NPS-vs-Trustpilot divergence is explicitly framed as a triangulation insight rather than as a contradiction (§5.5). The seven-reason caveat in §5.4.1 is methodologically solid and should be kept verbatim. |
| **Operationalization of "business value"** | Chapter 3 unpacks business value into four measurable dimensions (operational efficiency, productivity, customer experience, financial performance) with concrete indicators and audit-grade source mapping. This is rare in MSc work and should be made even more visible (see §10 of this report). |
| **Empirical pipeline transparency** | The two project reports document the financial dataset construction and the NLP pipeline at a level of detail that exceeds typical MSc standards. With minor packaging, they are direct appendix material. |
| **Reference repair** | The 52-entry rebuilt reference list (APA 7, deduplicated, alphabetized, all URLs/DOIs verified) is now substantially better than the original. |

### 2.3 Where the thesis is currently structurally vulnerable

| Weakness | Evidence | Impact |
|---|---|---|
| **Chapters 6, 7, 8, 9 absent** | Heading 1 paragraphs in docx: 1, 2, 3, 4, 5, References. No Chapter 6, no Discussion, no Limitations chapter, no Conclusion chapter. | High — thesis is incomplete as a research deliverable. |
| **Tables duplicated, not differentiated** | docx contains two identical 6×4 tables; "Table 1 — Dimensions of Business Value" exists as a heading/sentence (§99–100) but the table body is absent. | High — methodology and lit review lose their summary anchors. |
| **Lit review missing one strand** | §57 promises five strands; only four exist. "Consumer Behavior and AI Interaction" is announced and never written. | Medium — visible inconsistency between intro and body. |
| **Two orphan references** | Hevner et al. (2004) and Qualtrics (2024) appear in the reference list but never in the body. | Low–Medium — cosmetic but breaks the "every reference cited" QC rule. |
| **No abstract, TOC, lists, appendices** | The docx jumps from title to Chapter 1, and from References to nothing. | Medium — submission requirement at most universities, definitely at Corvinus. |
| **Inflated adjective load in Chapter 1** | ~69 instances of *important / critical / substantial / fundamentally / vital* in Chapters 1–4; concentrated in §11–§35. | Low–Medium — cosmetic but gives the introduction a "white-paper" rather than "thesis" tone. |
| **Title vs. defensible claim mismatch** | Title says "Voice LLM Agents," but the defensible empirical claim is about the Betsy/Tinman *operating model*, not about the voice agent in isolation. | Low — best handled with a subtitle or a one-line scope statement, not a retitle. |
| **Reproducibility appendix not embedded** | `08_Code/requirements.txt` exists but the docx has no Appendix B / C with package versions, dataset summary, OLI construction, NLP hyperparameters. | Medium — examiner-visible if scrutinized. |

The remainder of this report turns each of these weaknesses into a concrete, paragraph-level fix.

---

## 3. Chapter-by-Chapter Review

The following table is the diagnostic backbone of this report. *Priority* is calibrated against time-to-submission: **High** = block submission until fixed; **Medium** = should fix for stronger grade; **Low** = polish.

| # | Chapter | Status | Strengths | Main issues | What to add | What to delete or shorten | What to move to appendix | Priority |
|---|---|---|---|---|---|---|---|---|
| 1 | Introduction (§1.1–§1.7) | Present, complete, slightly inflated | Clear funnel from AI in industry → financial services → voice AI → research gap. RQs are well-formulated. Contribution claim is appropriate. | Inflated adjectives in §11–§35; §41 reads like marketing; §49 thesis-structure paragraph promises Ch 6, 7, 8, 9 that don't yet exist. | A 1–2 sentence "scope statement" clarifying that the empirical evaluation targets the *Betsy/Tinman operating model*, not Betsy in isolation. | Adjective inflation — see §11 of this report for sentence-level rewrites. | Nothing. | Medium |
| 2 | Literature Review (§2.1–§2.5) | Mostly present; one sub-strand missing | Strong on conversational AI in customer service (§77–§90), business value dimensions (§91–§99), and an early multi-dimensional value framework. | (a) "Consumer Behavior and AI Interaction" sub-strand promised in §57 is absent; (b) "Table 1 — Dimensions of Business Value Creation through AI in Customer Service" is referenced in §99–§100 but the table body is missing in the docx; (c) no explicit theoretical-framework / conceptual-model subsection — the lenses (TTF, AI service hierarchy, Acemoglu-Restrepo, Brynjolfsson) are scattered. | (i) the missing 5th sub-strand (≈600 words; see §6.3 of this report); (ii) a one-page **Conceptual Framework** subsection explicitly linking TTF (Goodhue & Thompson, 1995), the AI service hierarchy (Huang & Rust, 2018), the displacement-reinstatement view (Acemoglu & Restrepo, 2019), and AI-enabled productivity (Brynjolfsson et al., 2023; Aggarwal et al., 2025) into the conceptual model that Chapter 5 actually uses; (iii) the missing body of Table 1. | Where the lit review summarizes Andrade & Tumelero or Wang et al. for a second time, prune to one mention each. | Long expository quotes from Andrade & Tumelero and the Heskett service-profit-chain narrative can be compressed into two summary sentences each. | High |
| 3 | Methodology (§3.1–§3.10) | Present, almost complete | Pragmatist framing is justified well; convergent parallel design is correctly named; case-selection rationale (revelatory case in Yin's sense) is appropriate; data sources are described with reliability tiers; ethical considerations are present. | (a) Operationalization table (§99 / §100 anchor) is duplicated rather than distinct from the source-reliability table; (b) §122 says "data provenance classification … is presented in Table 1" but in fact Table 1 in this section is the *same* table that already appeared in Chapter 2; (c) reproducibility appendix (package versions, hyperparameters, OLI construction) is referenced in spirit but not embedded; (d) Yin (2018) is cited only once; the case-study design rationale would be strengthened by a second citation in §3.3. | (i) a clean, distinct **Operationalization Table** (Dimensions × Indicators × Data Source × Reliability) — which already exists once in the docx; (ii) a clean, distinct **Data Provenance / Source Reliability Table** (Source type × Examples × Reliability tier × Wording requirement) drawn from `10_Citation_Audit/F_Source_Reliability_Table.md`; (iii) one paragraph on reproducibility pointing to Appendix B (`08_Code/requirements.txt`); (iv) one paragraph on **abductive reasoning logic** — currently implicit. | The first long paragraph on pragmatism (§104) can be tightened by 30%; references to "the researcher" can be cut. | OLI construction details, NLP hyperparameter table, and full statistical-test outputs to Appendices B–C. | High |
| 4 | Case Study (§4.1–§4.7) | Present, very complete, well-structured | Excellent separation of Tinman / Betsy / ElevenLabs, careful treatment of vendor evidence, balanced human-AI collaboration narrative. The 2021–2023 / 2024 / 2025–2026 timeline is exactly right for the empirical design. | Some repetition with §5.2 (Chapter 5 RQ1 section partially restates Chapter 4 conclusions); occasional company-marketing residue in §189 ("Better's own materials present Tinman as supporting key mortgage tasks such as viewing rate options, obtaining pre-approval, locking rates, and closing loans within a digital workflow"). | (i) one **architecture diagram** (Tinman ↔ Betsy ↔ ElevenLabs Agents ↔ Human escalation) — Section 10 sketches it; (ii) one **mortgage origination workflow diagram** (before vs. after Betsy at the routine-communication layer); (iii) at the end of §4.7 one paragraph clarifying which parts of Chapter 4 will *not* be re-argued in Chapter 5 to avoid duplication. | §189 marketing-language residue ("viewing rate options, obtaining pre-approval, locking rates"); §192 ("Tinman therefore acts as the architectural prerequisite for Betsy") which is repeated almost verbatim in §270 of Chapter 5. | A longer Better.com corporate-history narrative could move to Appendix E. | Medium |
| 5 | Empirical Findings (§5.1–§5.7) | Present, post-PR-2 substantially repaired | Triangulation logic is excellent; numerical findings are correctly stated; the seven-reason NPS caveat (§316) is methodologically solid; the AI-invisibility finding is correctly framed as a discourse observation, not a behavioral claim. | (a) §305 OLI value (195.3) is correctly framed as supplementary, but the OLI itself isn't visualized in the chapter — it's only referenced as Appendix A.1 (which doesn't yet exist in the docx); (b) Figure 5.6 caption matches data but the figure should show *all six* topic shifts (Refinance, HELOC, Home Purchase, Smooth Transaction, Responsive Service, Closing Timeline) — confirm the inline image does this; (c) §340 says "approximately 52 percent revenue growth against approximately 5 percent expense growth" — this is exact-from-data but should round to single-decimal: "+52.0%" / "+5.3%"; (d) §306 Rocket figures: confirm the 2025 expense ratio "1.032" reflects *post-Mr.-Cooper* mix, otherwise add a footnote. | (i) a **summary findings table** at the end of §5.7 (RQ × evidence stream × headline result × confidence tier); (ii) one explicit cross-reference in §5.7 from the financial-leverage finding to the §6 design pattern. | Possibly trim the operational-cash-flow discussion in §296 if Figure 5.2's right panel already shows it. | The full list of 44 BERTopic topics, the intertopic distance map, and the topic-word importance plots to Appendix C. | Low–Medium (chapter is in good state) |
| 6 | Design Pattern (proposed) | **Absent** | — | Promised by the introduction and by §344 of Chapter 5; not present in docx. | Full new chapter, ≈2,500–3,500 words. Outline in §13.1 of this report. | — | — | **High (must build)** |
| 7 | Discussion (proposed) | **Absent** | — | Promised by the introduction; not present. | Full new chapter, ≈2,000–3,000 words. Outline in §13.2. | — | — | **High (must build)** |
| 8 | Limitations (proposed as standalone) | Partially scattered (§3.7, §5.6) | Single-case, no causal identification, granularity, vendor-bias, and Trustpilot self-selection are all already acknowledged in §346–§348. | Currently splintered across two chapters; needs a consolidated 1,200–1,800-word standalone limitations chapter so that examiners can find limitations in one place. | A consolidated chapter consolidating §3.7 + §5.6 + new content. Outline in §13.3. | The duplicated sentences between §3.7 and §5.6 (e.g., "single-case design," "Better's digital-first architecture is unusually favorable") can each appear *once* in the consolidated chapter. | — | High |
| 9 | Conclusion (proposed) | **Absent** | — | Promised; not present. | Full new chapter, ≈1,200–1,800 words. Outline in §13.4. | — | — | **High (must build)** |
| Refs | References | Present, repaired | 52 deduplicated APA 7 entries, alphabetized, URLs verified. | Two orphan references (Hevner 2004, Qualtrics 2024); two suffix calls in §306 ("Rocket Companies, 2024, 2025") still need confirmation that the years refer to the FY-2023 and FY-2024 10-Ks respectively. | If Hevner is cited in Ch 6, keep it; otherwise remove. Qualtrics: cite once in §5.4.1 NPS context or remove. | — | — | Low |
| App. | Appendices | **Absent** | — | No appendix structure exists in the docx. | Full appendix block (A–G) — see §10 of this report. | — | — | High |
| Front-matter | Title page, abstract, TOC, lists | Title only | Title is fine. | Abstract, acknowledgments, TOC, list of figures, list of tables, list of abbreviations are absent. | Front-matter block per Corvinus formatting standards. | — | — | High |

---

## 4. Core Argument Coherence Review

### 4.1 What the thesis currently argues

Reading Chapters 1 → 5 as a single argument, the thesis currently claims:

> The deployment of voice LLM agents in financial services creates multidimensional business value when the agent is integrated into a process-aware operating platform with auditable human escalation; in the Better.com case, the post-deployment trajectory is consistent with AI-enabled operational leverage in the financial-operational dimension and is mixed in the customer-experience dimension.

This is **defensible and well-supported** by the evidence presented. There is no claim of causal identification anywhere in Chapter 5; the strongest verb is "consistent with."

### 4.2 What the thesis can defensibly argue (preferred wording)

Three small refinements would tighten the central claim:

1. The unit of analysis is the **operating model**, not the voice agent in isolation. The thesis already says this in §266 ("the unit of analysis is not Betsy in isolation but Betsy as one component of an integrated operating model") and in §342 ("does not claim that Betsy alone caused Better.com's post-transition financial trajectory"). Make this explicit one more time, in the final claim of Chapter 9.
2. The empirical design supports **analytic generalization** to similar configurations, not statistical generalization. This is correctly stated in §344 but should be reiterated in Chapter 9.
3. The customer-experience finding is **a divergence to be interpreted**, not a deterioration to be reported. The current wording in Chapter 5 already does this; the issue is only that the Discussion chapter, when written, must not slip into "Trustpilot ratings declined post-Betsy, suggesting customers were dissatisfied with Betsy."

### 4.3 What the thesis should *not* claim

| Claim | Why to avoid |
|---|---|
| "Betsy caused Better.com's revenue recovery." | No counterfactual; multiple confounders (NEO channel, market recovery, restructuring). |
| "Voice AI deployment in financial services improves customer experience." | The thesis's own evidence is mixed in this dimension; this would be an overclaim. |
| "Betsy improved NPS from 39 to 64." | NPS is management-reported and unaudited; the thesis correctly classifies it as medium-reliability evidence (§315). |
| "ElevenLabs case-study figures (e.g., 41% reduction in cost-to-originate, +30% conversion) confirm Betsy's value." | Vendor evidence; thesis already qualifies these in §227–§229. The Discussion chapter must not undo that qualification. |
| "Voice AI replaces loan officers." | Evidence supports task reallocation, not labor substitution (§217, §279). |

### 4.4 Suggested revised final claim (drop-in, for Chapter 9)

> Voice LLM agents in regulated financial-services workflows generate multidimensional and mediated business value when they are deployed not as stand-alone conversational interfaces but as one layer of a process-aware operating model that already encodes the regulated workflow, structured data, low-latency voice infrastructure, and auditable human-escalation paths. In the Better.com case, the post-transition financial-operational trajectory is descriptively consistent with AI-enabled operational leverage — most clearly visible in the 2024-to-2025 expense-ratio decline from 2.89 to 2.01, a 19.6% narrowing of net loss, and a 42.9% improvement in revenue per employee — while the customer-experience evidence is divergent: management-reported NPS rises from 39 to 64, but independent Trustpilot sentiment and star ratings decline by small-to-medium effect sizes and explicit AI mentions remain at approximately 1% in both periods. The empirical contribution is therefore not that voice AI uniformly improves customer outcomes, but that voice AI in a regulated process can produce visible operational leverage while remaining *invisible to most customers* — a pattern this thesis names *invisible AI infrastructure* and formalizes as a four-prerequisite design pattern in Chapter 6.

### 4.5 Suggested revised contribution statement

> This thesis contributes (i) **empirically**, the first end-to-end triangulated case study of a voice LLM agent in U.S. mortgage origination linking SEC-filed financial trajectory, BERTopic+VADER customer-discourse analysis, and qualitative process tracing of integration architecture; (ii) **methodologically**, an explicit four-tier source-reliability hierarchy (audited financials → company disclosures → independent customer discourse → vendor/case materials) for evaluating AI business value claims; and (iii) **theoretically/practical**, a four-prerequisite *Voice-AI-in-Regulated-Workflow* design pattern (process-aware operating platform, coordination-layer agent scope, low-latency voice infrastructure, auditable human escalation) that is transferable to retail banking servicing, insurance servicing, and analogous high-volume regulated communication-intensive financial workflows.

---

## 5. Research Question Review

### 5.1 Are the RQs clear, answerable, and matched to evidence?

| Test | RQ1 | RQ2 |
|---|---|---|
| Clear? | Yes (§47). | Yes (§47), but slightly long. |
| Too broad? | No — bounded to "Better.com's mortgage origination process" and "regulated financial services." | Slightly: the addition of "and what factors mediate the realization of this value" is good, but it stretches the question. Acceptable. |
| Answerable from data? | Yes — Chapter 4 supplies architecture, Chapter 5.2 supplies prerequisites synthesis. | Yes — operational-financial dimension answered with high confidence; customer-experience dimension answered with appropriate uncertainty. |
| Causal overclaim risk? | Low (asks "how … integrated" and "what prerequisites"). | Medium (asks "what measurable business value can be associated with"). The current wording uses *associated with* — keep that wording verbatim. |
| Should "voice AI deployment" → "Betsy/Tinman voice AI operating model"? | Yes — stronger and matches the §266 unit-of-analysis statement. | Yes — same. See §5.3 below. |

### 5.2 Recommended final RQ wording (lightly revised)

> **RQ1.** *How has the Betsy/Tinman voice AI operating model been integrated into Better.com's mortgage origination process, and what does this integration reveal about the architectural, workflow, and human-AI collaboration prerequisites for deploying voice LLM agents in a regulated financial-services environment?*
>
> **RQ2.** *What measurable business value can be associated with Better.com's Betsy/Tinman voice AI operating model across operational efficiency, productivity, customer experience, and financial performance, and what factors mediate the realization of this value?*

The only changes are "voice LLM deployment" → "Betsy/Tinman voice AI operating model" (twice). This brings the RQs into exact alignment with the unit-of-analysis statement in §266 and §342.

### 5.3 RQ × Evidence mapping (the table to insert at the end of §5.7)

| RQ | Sub-dimension | Evidence stream | Chapter / section | Figures / tables | Headline result | Reliability tier | Limitations | Final answer (one line) |
|---|---|---|---|---|---|---|---|---|
| RQ1 | Architecture | Qualitative process tracing | §4.2, §5.2.1 | Architecture diagram (proposed Fig 4.1) | Tinman is the architectural prerequisite — it exposes structured workflow state to the voice layer. | High (10-K disclosure) | Better's specific digital maturity may not generalize. | Voice LLM agents in mortgage become operationally meaningful when sitting on top of a process-aware platform. |
| RQ1 | Agent scoping | Qualitative process tracing | §4.3, §5.2.2 | (none) | Betsy is a coordination layer, not an underwriter. | High (10-K + Better–ElevenLabs joint release) | Vendor-coloured detail. | Voice agent's task scope must be bounded to communication coordination. |
| RQ1 | Voice infrastructure | Vendor materials + Better disclosures | §4.4, §5.2.3 | (none) | Modular STT–LLM–TTS pipeline with low latency materially affects usability. | Medium-High (vendor evidence triangulated with Better's filings) | Single-vendor case. | Low-latency voice infra is a non-trivial prerequisite, not a cosmetic detail. |
| RQ1 | Human escalation | Qualitative process tracing | §4.5, §5.2.4 | (none) | Regulated steps require explicit consent and licensed-consultant routing. | High (10-K + CFPB context) | U.S.-specific. | Auditable human-in-the-loop is a structural requirement, not an optional safeguard. |
| RQ2 | Revenue recovery | Financial analysis | §5.3.1 | Fig 5.1 | +52.0% (2024→2025); +114.6% (2023→2025) but partial recovery. | High (audited 10-K) | Confounded by NEO, restructuring, market recovery. | Revenue trajectory consistent with operational leverage; not Betsy-isolable. |
| RQ2 | Expense intensity | Financial analysis | §5.3.2 | Fig 5.2 | Expense ratio 4.79 → 2.89 → 2.01 (2023→2024→2025). | High (audited 10-K) | Cross-company expense-ratio comparability with Rocket is directional only. | Strongest descriptive evidence of operational leverage. |
| RQ2 | Profitability | Financial analysis | §5.3.3 | Fig 5.1 | Net loss narrowed 19.6% (2024→2025); company still unprofitable. | High | Not yet a turnaround. | Trajectory consistent with leverage; not yet evidence of profitability. |
| RQ2 | Productivity | Financial analysis | §5.3.4 | Fig 5.3 | RPE +42.9% to $0.124M; pre-period average $0.130M. | High | Headcount essentially flat; productivity gain comes from revenue growth. | Partial productivity recovery, not full. |
| RQ2 | Benchmark | Financial analysis | §5.3.5 | (table 5.3.5) | Better's relative improvement exceeds Rocket's. | Medium-High (audited but not counterfactual) | 2025 Mr-Cooper acquisition distorts Rocket. | Directional evidence that Better's gains are not solely macro-driven. |
| RQ2 | NPS (customer-experience) | Management disclosure | §5.4.1 | (none) | NPS 39 → 64. | Medium (management-reported, unaudited) | Sampling, weighting, instrument undisclosed. | Treated as one input, not as customer-experience evidence in its own right. |
| RQ2 | Trustpilot ratings | NLP analysis | §5.4.2 | Fig 5.4 | Star 4.28 → 3.86 (p = 0.0019, d = 0.29); VADER 0.642 → 0.515 (p = 0.0057, d = 0.25). | Medium (independent but self-selected) | Pre/post imbalance 1,746 vs 169. | Statistically significant small-to-medium decline in independent customer discourse. |
| RQ2 | Keyword prevalence | NLP analysis | §5.4.3 | Fig 5.5 | Cost/Rates −12.35 pp (only Bonferroni-robust); Digital/Process −8.98 pp; AI mentions ~1% in both periods. | Medium-High (statistical tests with Bonferroni) | Discourse, not behavior. | AI is invisible to customers; cost-language salience drops. |
| RQ2 | Topic shifts | NLP analysis | §5.4.4 | Fig 5.6 | Refinance −7.66 pp; HELOC +4.22 pp; Smooth Transaction +4.03 pp; Responsive Service +3.93 pp. | Low–Medium (descriptive only; n=121 post) | Sensitive to BERTopic hyperparams. | Most plausibly product-mix and macro effects. |

This single table, inserted as Figure / Table at the close of §5.7, will make the RQ → evidence mapping unambiguous to the examiner.

---

## 6. Literature Review Improvement Plan

### 6.1 What the lit review currently does well

- Funnel structure (general AI → financial-services AI → conversational AI → voice AI / LLM agents → business value of AI) is logically sound.
- Key empirical anchors are correctly chosen: Adam, Wessel & Benlian (2021); Andrade & Tumelero (2022); Wang et al. (2023); Zhang et al. (2023); Brynjolfsson, Li & Raymond (2023); Aggarwal, Kumar & Srivastava (2025); Hentzen et al. (2022); Mogaji & Nguyen (2021); Huang & Rust (2018); Goodhue & Thompson (1995); Acemoglu & Restrepo (2019).
- The Heskett et al. (1994) service-profit-chain bridge is appropriately cited as a *secondary* citation through Fotheringham & Wiles (2023) — APA 7 §8.6 compliant.

### 6.2 What is missing or weak (thesis-specific)

| Gap | Why it matters for *this* thesis | Recommended action |
|---|---|---|
| **Missing 5th sub-strand "Consumer Behavior and AI Interaction"** | §57 explicitly promises this. Its absence creates a structural inconsistency between intro and body. The thesis also needs this sub-strand to set up the Trustpilot/NLP analysis in Chapter 5: without consumer-behavior literature on review-platform self-selection, voice-naturalness perception, and AI invisibility, the §5.4.5 customer-experience synthesis floats theoretically. | Add ~600-word subsection (drafted in §6.3 below). |
| **No explicit Conceptual Framework subsection** | Chapter 5.5 invokes three theoretical lenses simultaneously (TTF, AI service hierarchy, AI-enabled productivity). The lit review currently introduces them one at a time but never *integrates* them. | Add ~400-word "Conceptual Framework" subsection that names the three lenses, draws a one-paragraph integrating proposition, and ends with the explicit research gap statement. |
| **Table 1 — Dimensions of Business Value (§99–100)** | Referenced but body is missing in the docx. | Insert the table body. Exact draft in §10 of this report. |
| **Voice AI literature is thin** | The thesis cites Aggarwal et al. (2025), Nussbaum et al. (2025), Becker et al. (2025), Maslych et al. (2025) — all good — but it does not engage with the *anthropomorphism / voice-naturalness / trust* literature deeply enough to support the §222 and §445 claims. | Add 2–3 sentences in §2.3 (Voice AI / LLM agents) summarizing the consensus that voice naturalness is necessary-but-not-sufficient for trust (Becker et al., 2025), and that latency above ~4s degrades user experience (Maslych et al., 2025). |
| **Mortgage-industry / IS-in-financial-services anchor** | The lit review never cites a single IS-in-banking or fintech paper that frames mortgage origination as a digital workflow process. | Either add 2–3 sentences in §2.1 referencing one or two studies on digital mortgage origination, or, if no peer-reviewed source is verifiable, make the gap explicit ("The peer-reviewed literature on digital mortgage origination is sparse; this thesis therefore relies on Better's own SEC filings and MBA performance reports for industry context"). |
| **Hevner et al. (2004) is in the reference list but never cited** | Two options: (a) cite Hevner once in Chapter 6 as the design-science grounding for the design pattern; (b) drop the reference. | Cite Hevner in Chapter 6's opening paragraph. |
| **Qualtrics (2024) is in the reference list but never cited** | Original intent was probably to anchor the NPS 39 → 64 management claim to an industry NPS benchmark. | Either drop the entry or cite once in §5.4.1 NPS context — only if the actual Qualtrics XM Institute 2024 publication can be confirmed; otherwise drop. |
| **Operationalization of "business value" is in §3 but should be foreshadowed in §2** | §99 invokes "value creation operates across at least four distinct but interrelated dimensions" but does not name them. | One sentence in §99 listing the four dimensions: "operational efficiency, productivity, customer experience, and financial performance." |

### 6.3 Drop-in 5th sub-strand: "Consumer Behavior and AI Interaction" (≈600 words)

Insert as new subsection §2.5 (renumber the current §2.5 "Business Value of AI" to §2.4 if needed). This text is intended to be edited, not pasted verbatim.

> **2.5 Consumer Behavior and AI Interaction**
>
> The fifth strand of the literature relevant to this thesis examines how consumers perceive and respond to AI-mediated service interactions, with particular attention to voice-based agents. Three threads are pertinent. The first concerns *anthropomorphism and voice naturalness*: a recent review in *Trends in Cognitive Sciences* argues that the perceived naturalness of a voice is a salient property that shapes interaction with both human and artificial agents (Nussbaum et al., 2025), and a 2025 study in *ACM Transactions on Human-Robot Interaction* finds that more natural voices change perceptions of safety and compliance even where a direct effect on trust is not observed (Becker et al., 2025). For voice LLM agents in financial services, this implies that voice quality is a necessary-but-not-sufficient condition for credible interaction; cosmetic gains in synthesis quality cannot compensate for back-end inadequacy, but a serviceable back-end paired with poor synthesis can undermine confidence even when the underlying answer is correct.
>
> The second thread concerns *latency and conversational flow*. Maslych et al. (2025) report that response latency above approximately four seconds significantly degrades perceived response time and broader user-experience measures in LLM-powered intelligent virtual agents, and that natural conversational fillers can mitigate only part of that effect. Real-time voice interaction is therefore far less tolerant of delay than text-based interaction — a finding directly relevant to mortgage origination, where each borrower call may trigger many internal system calls (Better Home & Finance Holding Company & ElevenLabs, 2026).
>
> The third thread concerns *consumer attribution of service experience to AI*. Mogaji and Nguyen (2021) argue that AI in customer-facing financial services frequently operates as backend or infrastructure-level technology rather than as a branded chatbot, with the consequence that customers may not consciously perceive AI as a feature of their service journey. Aggarwal et al. (2025) make a parallel observation in their voice-AI value-creation framework, distinguishing B2B and B2C value creation surfaces and noting that AI-related productivity gains may emerge alongside ambiguous customer-perception effects when the AI system is not branded to the end user.
>
> Finally, work on review-platform self-selection (Filieri, 2015; Luca, 2016) bears directly on the interpretation of Trustpilot data. Self-selected review-platform users are typically more emotionally engaged than the average customer, and platform reviews therefore over-sample the tails of the customer-experience distribution. Combined with the small post-period sample size that any single-event study generates, this self-selection means that public-discourse signals on voice AI deployment must be read alongside, rather than against, management-reported survey instruments such as Net Promoter Score.
>
> Taken together, this strand of the literature implies three working propositions for the present thesis: (i) voice quality and latency function as service-design prerequisites for credible voice AI in financial services; (ii) when voice AI operates as backend infrastructure inside a regulated workflow, customer attribution of experience to AI is likely to be low; and (iii) public-discourse measurement of customer experience is informative but biased toward emotionally engaged subsets of customers, and must be triangulated with internal management measurement instruments rather than substituted for them.

### 6.4 Drop-in Conceptual Framework (≈400 words)

Insert as new subsection §2.6 (after the consumer-behavior strand) immediately before §3.

> **2.6 Conceptual Framework: Three Complementary Lenses**
>
> The empirical analysis in Chapter 5 is interpreted through three complementary theoretical lenses. The first is the *task–technology fit* perspective (Goodhue & Thompson, 1995), under which the operational meaningfulness of a conversational technology depends on whether the technology has access to the data and process state needed for the task; this lens accounts for why a process-aware operating platform such as Tinman is treated in this thesis as the architectural prerequisite for a voice LLM agent. The second is the *AI service hierarchy* (Huang & Rust, 2018), which distinguishes mechanical, analytical, intuitive, and empathetic dimensions of service work; this lens explains why a voice agent is most likely to generate productivity gains when scoped to the mechanical and analytical layers (high-volume, structured, communication-intensive coordination work) and is more contested in the intuitive and empathetic layers. The third is the *AI-enabled productivity* tradition (Acemoglu & Restrepo, 2019; Brynjolfsson et al., 2023; Aggarwal et al., 2025), under which AI-related productivity gains tend to materialize through task reallocation rather than full labor substitution and can emerge alongside ambiguous customer-perception effects when the AI system operates as backend infrastructure rather than as a branded customer-facing experience.
>
> Read together, the three lenses generate a single integrating proposition that this thesis evaluates empirically: *the deployment of a voice LLM agent in a regulated financial-services workflow is most likely to produce measurable operational leverage, while remaining largely invisible to end customers, when (i) it is task-fitted to a process-aware operating platform that exposes structured workflow state, (ii) it is scoped to the mechanical and analytical layers of service work, and (iii) it is governed by an explicit human-AI collaboration model that reallocates rather than substitutes labor at the regulated boundary.*
>
> The research gap that the thesis addresses follows directly. The peer-reviewed literature on chatbot value creation in financial services concentrates on text-based agents (Adam et al., 2021; Abdulquadri et al., 2021; Andrade & Tumelero, 2022), and the small but growing voice-AI literature is dominated by call-center natural field experiments outside regulated mortgage origination (Wang et al., 2023; Zhang et al., 2023). No published case study has yet linked SEC-filed financial trajectory, independent customer-discourse mining, and qualitative process tracing of integration architecture for a voice LLM agent in U.S. mortgage origination. This is the gap into which the Better.com case is positioned.

### 6.5 What to shorten in the lit review

| Where | What to compress | Suggested compression |
|---|---|---|
| §86–§87 | The Andrade & Tumelero efficiency-gain quotation (~120 words) | Compress to one sentence: "Empirical work on AI chatbot deployment in customer service reports problem-resolution rates rising from 77% to 92.1% and material reductions in time-to-resolution, indicating that value creation through AI operates through both volume and quality dimensions (Andrade & Tumelero, 2022)." |
| §90 | Heskett service-profit-chain narrative (~110 words) | Compress to one sentence: "These efficiency gains map onto the service-profit chain logic — service quality drives customer satisfaction, which drives loyalty and profitability — even though that chain was originally articulated in a non-AI context (Heskett et al., 1994, as cited in Fotheringham & Wiles, 2023)." |
| §83–§84 | The Adam, Wessel & Benlian (2021) compliance discussion is detailed | Trim to one sentence on the *compliance/anthropomorphism* finding and one sentence on the *reciprocity heuristic*. |

The objective is not to lose the citations — it is to convert the lit review from a *summary of papers* into a *synthesized argument* that ends in a research gap.

---

## 7. Methodology Fix Plan

### 7.1 What is already strong in Chapter 3

- Pragmatist philosophical grounding (§104).
- Convergent parallel mixed-methods design correctly named (§108).
- Case-selection rationale invokes Yin's revelatory-case logic (§109).
- Source-reliability hierarchy is articulated (§122) — though the table is duplicated.
- Triangulation logic is explicit (§128).
- Ethical considerations are addressed (§148).

### 7.2 High-priority fixes

| Priority | Fix | Where | Concrete action |
|---|---|---|---|
| **High** | Differentiate Operationalization Table from Source Reliability Table | §3.6 vs §3.7 | The docx currently contains *two copies* of the same 6×4 table. Replace the second occurrence with a distinct **Source Reliability / Data Provenance Table** (rows: SEC 10-K / SEC 8-K & press release / Better IR webpage / vendor case study (ElevenLabs) / industry report (MBA, Freddie Mac) / regulatory page (CFPB) / academic peer-reviewed / news media / self-selected UGC (Trustpilot); columns: Examples in this thesis / Reliability tier / Wording requirement). Draft in §10. |
| **High** | Insert reproducibility paragraph + Appendix B pointer | After §148 | One paragraph: "All quantitative analyses in this thesis are reproducible from the raw source data and the public source code repository. Package versions used in the financial and NLP pipelines are listed in `08_Code/requirements.txt` and reproduced in Appendix B; BERTopic hyperparameters (UMAP `n_neighbors=10`, `n_components=5`, `min_dist=0.0`, cosine; HDBSCAN `min_cluster_size=10`, `min_samples=3`, EOM; `random_state=42`) are listed in Appendix C." |
| **High** | Make abductive logic explicit | §3.2 (after pragmatism) | One paragraph clarifying that the empirical inference logic is *abductive* — financial trajectory and customer-discourse signals are read as observations to be reconciled with the most plausible explanation given the case-study evidence on integration mechanism, not as deductive tests of a pre-specified causal hypothesis. |
| **Medium** | Tighten the pragmatism paragraph | §104 | Cut ~30%. The justification ("we choose pragmatism because it admits both quantitative and qualitative evidence into the same study") is the only sentence that is downstream-relevant. |
| **Medium** | Soften the description of Rocket as benchmark | §3.4 | Add: "Because Rocket and Better differ substantially in scale, business mix, and 2025 acquisition context, Rocket functions as a directional industry benchmark rather than as a counterfactual; this is reiterated in §5.3.5 and §5.6." |
| **Medium** | Justify Trustpilot as data source | §3.5 | Add ~3 sentences on (i) why Trustpilot rather than Google or Yelp, (ii) the self-selection bias acknowledgment (Filieri, 2015; Luca, 2016), (iii) the date of scrape and the actor used (Apify Trustpilot Review Scraper, Actor ID `l3wcDhSSC96LBRUpc`). |
| **Medium** | Distinguish audited SEC data from management/vendor claims explicitly | §3.7 | Add the four-tier sentence already drafted in deliverable G of the citation audit. |
| **Low** | Add CTO proxy disclosure | §3.6 | One sentence: "Cost-to-Originate (CTO) is computed in this thesis as Total_Expenses ÷ Funded_Loans as a proxy for Better's reported per-loan cost; it is *not* an audited Better disclosure. The MBA Quarterly Performance Report is used as the third-party benchmark for industry CTO." |
| **Low** | OLI disclaimer | §3.6 | One sentence: "The Operational Leverage Index reported in §5.3.4 (and Appendix B) is an author-constructed equally-weighted composite (Revenue Growth Index, Revenue per Employee Index, Inverse Expense Ratio Index) with 2023 = 100. It is sensitive to baseline-year selection and weighting and is therefore retained as a compact visualization, not as primary evidence." |

### 7.3 Methodological risks to surface explicitly

The methodology chapter should *name and own* the following risks rather than leaving the reader to discover them:

1. **No causal identification.** Stated in §347; should also be stated in §3.7.
2. **Annual financial granularity.** Stated; reiterate.
3. **Single-vendor (ElevenLabs) source bias.** Stated in §227.
4. **Trustpilot self-selection and pre/post imbalance (1,746 / 169).** Stated in §321.
5. **Topic-share figures sensitive to BERTopic hyperparameters.** Stated in §335.
6. **Rocket comparability bounded by accounting presentation differences.** Stated in §296.
7. **2024 as a transition year, not a clean post-Betsy year.** Stated in §238.

The fix is not to add new caveats; it is to **consolidate them into a single "Methodological Risks" sub-section in §3.7** so an examiner can see all seven at once.

### 7.4 Suggested final methodology structure (after fixes)

1. §3.1 Research philosophy (pragmatism)
2. §3.2 Inference logic (abductive)
3. §3.3 Research design (convergent parallel mixed-methods)
4. §3.4 Case selection (Better.com as revelatory case; Rocket as directional benchmark)
5. §3.5 Data sources (financial; NLP; qualitative)
6. §3.6 Operationalization of business value (Operationalization Table — Table 3.1)
7. §3.7 Source reliability and data provenance (Source Reliability Table — Table 3.2)
8. §3.8 Analytical procedures (financial ratios; NLP pipeline; process tracing)
9. §3.9 Triangulation logic
10. §3.10 Methodological risks (consolidated)
11. §3.11 Ethical considerations
12. §3.12 Reproducibility (Appendix B / C pointer)

---

## 8. Case Study Improvement Plan

### 8.1 What Chapter 4 currently does well

- Mortgage process pain points are well-grounded in MBA and CFPB sources.
- The Tinman / Betsy / ElevenLabs separation is excellent.
- The pre-deployment baseline narrative (2021 hyper-growth → 2022 collapse → 2023 trough → 2024 transition → 2025–2026 scaling) is correctly framed and supported.
- Vendor evidence is appropriately qualified.

### 8.2 What to add

| Action | Where | Why |
|---|---|---|
| **Architecture diagram** (Tinman ↔ Betsy ↔ ElevenLabs ↔ Human escalation) | §4.4 (after §220) | Currently the relationships are described in prose only. |
| **Mortgage origination workflow figure** (Before vs After Betsy) | §4.2 (after §184) | Makes Tinman/Betsy roles concrete by showing where Betsy enters the workflow. |
| **Better.com timeline figure** (2014 → 2020 → 2021 layoff → 2023 trough → Oct 17 2024 Betsy launch → June 2025 ElevenLabs partnership → Feb 2026 joint release) | §4.6 | Strengthens the temporal narrative. |
| **Evidence source hierarchy table for Chapter 4** | §4.5 | A 1-table summary of which Better disclosures are audited vs management-reported vs vendor-coloured. |
| **Compliance/governance paragraph** | §4.5 | Currently §279–§280 cover compliance lightly. Add one paragraph naming SAFE Act, TILA-RESPA, CFPB UDAAP authority, state licensing requirements explicitly. |

### 8.3 What to soften / qualify

| Sentence (current) | Problem | Suggested rewrite |
|---|---|---|
| §189 "Better's own materials present Tinman as supporting key mortgage tasks such as viewing rate options, obtaining pre-approval, locking rates, and closing loans within a digital workflow" | Marketing-language residue | "Better's own materials describe Tinman as the workflow infrastructure through which rate display, pre-approval, rate-lock, and closing actions are executed, although these descriptions are company-disclosed rather than independently validated (Better Home & Finance Holding Company, 2025a)." |
| §192 "Tinman therefore acts as the architectural prerequisite for Betsy" | Strong without qualification | "Tinman *therefore appears to act as* the architectural prerequisite for Betsy in this case; whether the same prerequisite holds outside Better.com is a question for the Discussion chapter." |
| §211 "1.89 million inbound and outbound calls in 2025" / "approximately 100,000 mortgage-related phone calls per month" | Vendor-sourced operating figure repeated without inline reliability flag | "The February 2026 Better–ElevenLabs joint release reports that Betsy handled approximately 100,000 mortgage-related phone calls per month and 1.89 million inbound and outbound calls in 2025; these figures are management- and vendor-reported and are not independently audited (Better Home & Finance Holding Company & ElevenLabs, 2026)." |
| §245 "These materials are useful for understanding the voice infrastructure and deployment mechanism, but they remain vendor-related evidence and should not be treated as independent evidence of financial causality." | Already qualified — keep verbatim. | (no change) |

### 8.4 What to shorten

| Section | What to compress |
|---|---|
| §178–§182 (mortgage process pain points) | ~700 words restating textbook mortgage-industry context. Compress to two paragraphs (~300 words). The substantive contribution is the linkage in §184; that sentence stays. |
| §218–§224 (ElevenLabs role) | ~700 words across three subsections. Compress to ~400 words. |
| §232–§246 (Implementation Timeline) | ~1,100 words. Compress to ~700 once the timeline figure is added. |

### 8.5 Suggested subheading structure (after fixes)

1. §4.1 Introduction to the Case
2. §4.2 The Mortgage Origination Process and Why Voice AI Is Useful
3. §4.3 Better.com's Technology Foundation: The Tinman Platform [+ Architecture Figure 4.1]
4. §4.4 Betsy: Better.com's Voice AI Loan Assistant [+ Workflow Figure 4.2]
5. §4.5 ElevenLabs as Voice Infrastructure Provider [+ Reliability Table 4.1]
6. §4.6 Human–AI Collaboration and Compliance
7. §4.7 Implementation Timeline [+ Timeline Figure 4.3]
8. §4.8 Case Relevance to RQ1 and RQ2
9. §4.9 Chapter Summary

---

## 9. Chapter 5 Empirical Findings Audit

### 9.1 Number checks (all verified against the empirical reports)

| Claim in Chapter 5 | Source datum | Match? |
|---|---|---|
| Revenue 2023 ≈ $76.8M (§288) | financial_metrics_project_report.md §4 | OK |
| Revenue 2024 ≈ $108.5M (§288) | same | OK |
| Revenue 2025 ≈ $164.9M (§288) | same | OK |
| Revenue growth 2024→2025 ≈ 52.0% (§288) | derived | OK |
| Revenue growth 2023→2025 ≈ 114.6% (§288) | derived | OK |
| Expense ratio 2023 / 2024 / 2025 = 4.79 / 2.89 / 2.01 (§292) | derived | OK |
| Total expenses 2023 / 2024 / 2025 ≈ $368.1M / $313.9M / $330.7M (§292) | dataset | OK |
| Net loss 2023 / 2024 / 2025 ≈ $536.4M / $206.3M / $165.9M (§298) | dataset | OK |
| Net-loss narrowing 2024→2025 ≈ 19.6% (§298) | derived | OK |
| RPE 2023 / 2024 / 2025 ≈ $0.094M / $0.087M / $0.124M (§302) | derived | OK |
| RPE improvement 2024→2025 ≈ +42.9% (§302) | derived | OK |
| RPE improvement 2023→2025 ≈ +32.3% (§302) | derived | OK |
| Pre-period RPE average ≈ $0.130M (§305) | derived | OK |
| Headcount 2021 / 2023 / 2024 / 2025 ≈ 10,400 / 820 / 1,250 / 1,329 (§302) | dataset + 10-Ks | OK (2021 from S-1) |
| OLI 2025 ≈ 195.3 (§305) | derived (2023 = 100) | OK — re-run notebook before submission |
| Trustpilot pre / post n = 1,746 / 169 (§313, §318) | nlp_project_report §2.3 | OK |
| Star rating pre / post = 4.2806 / 3.8580 (§318) | nlp report §2.5 | OK |
| Star rating decline 0.4226, p = 0.0019, d = 0.2899 (§318) | nlp report | OK |
| VADER pre / post = 0.6416 / 0.5151 (§318) | nlp report | OK |
| VADER decline 0.1265, p = 0.0057, d = 0.2505 (§318) | nlp report | OK |
| Cost/Rates −12.35 pp (§324) | nlp report §4.3 | OK (correctly fixed in PR #2) |
| Digital/Process −8.98 pp (§324) | nlp report §4.3 | OK |
| Cost/Rates Bonferroni-adjusted p ≈ 0.005 (§324) | nlp report §4.3 | OK |
| AI mentions ≈ 1.15% pre / 1.18% post; Fisher p = 1.0000 (§327) | nlp report §4.3 | OK |
| BERTopic clustered n_pre / n_post = 1,077 / 121 (§331) | nlp report §4.2 | OK |
| Refinance topic decline ≈ 7.66 pp (§334) | nlp report §4.5 | confirm |
| HELOC complaints rise ≈ 4.22 pp (§334) | nlp report §4.5 | confirm |
| NPS 39 → 64 (§315) | Better Q4/FY 2024 release; 2025 10-K | OK (already qualified) |

**All headline numbers in Chapter 5 are correct.** The earlier Cost/Rates inversion has been fixed in PR #2. Re-run the BERTopic notebook once before submission to lock the topic-share figures.

### 9.2 Figure checks

| Figure | Caption claim | What to verify |
|---|---|---|
| Fig 5.1 (Revenue / total-expense base / net loss, 2021–2025) | Recovery, expense containment, narrowing losses | Confirm 2021 values sourced from S-1, 2022 from 2023 10-K (smaller-reporting-company gap). Confirm shaded periods correctly distinguish pre-Betsy / transition / post-Betsy. |
| Fig 5.2 (Expense ratio + operating cash flow, 2021–2025) | Two-panel chart | Confirm operating cash flow remains negative in 2025. |
| Fig 5.3 (Headcount + RPE, 2021–2025) | Workforce contraction + RPE recovery | Confirm 2025 RPE plotted with the pre-period average ($0.130M) line shown. |
| Fig 5.4 (VADER distribution, pre vs post) | Modest downward shift | Confirm n labels match (1,746 / 169). |
| Fig 5.5 (Keyword prevalence, 7 groups) | Cost/Rates is the only Bonferroni-robust decline | Confirm Cost/Rates labelled with Bonferroni-adjusted p ≈ 0.005, AI/Automation labelled with Fisher p = 1.0000. |
| Fig 5.6 (Topic shifts) | Refinance −7.66 / HELOC +4.22 / Smooth Transaction +4.03 / Responsive Service +3.93 / Closing Timeline +3.55 / Home Purchase −3.48 | Confirm all six bars present and correctly labelled. |

### 9.3 Interpretation checks (defensible, keep verbatim)

| Interpretation | Verdict |
|---|---|
| §290 "Revenue trajectory consistent with operational-leverage interpretation that Better's broader Betsy/Tinman AI operating model is associated with growth that does not require proportional expansion of the cost base" | Defensible. Keep. |
| §296 "operating cash flow panel … makes clear that improvements in the expense ratio are not yet matched by sustained positive operating cash flow" | Defensible. Critical honesty — keep. |
| §300 "It does not establish that the path to profitability is uniquely AI-driven" | Defensible. Keep. |
| §305 "OLI reaches 195.3 in 2025 with 2023 set to 100" / "retained as a compact visualization rather than as primary evidence" | Defensible. Keep. |
| §316 7-reason NPS-vs-Trustpilot caveat | Methodologically excellent. Keep verbatim. |
| §327 AI-invisibility finding | Defensible. Keep. |
| §328 Cost/Rates compositional reading | Defensible. Keep. |
| §334 topic shifts as "most plausibly product-mix and macro-level effects" | Defensible. Keep. |

### 9.4 Wording fixes (§5)

| Where | Current | Suggested rewrite | Reason |
|---|---|---|---|
| §263 | "RQ1 is answered primarily through the qualitative case-study evidence established in Chapter 4" | "RQ1 is addressed primarily through the qualitative case-study evidence established in Chapter 4" | Lower verb's strength. |
| §340 | "is the textbook descriptive signature of operational leverage" | "— descriptively consistent with the textbook signature of operational leverage" | Preserves qualifier. |
| §344 | "These integration prerequisites are summarized as a design pattern in Chapter 6" | "These integration prerequisites are summarized as a four-prerequisite design pattern in Chapter 6 — a process-aware operating platform, a coordination-layer agent scope, low-latency voice infrastructure, and an auditable human-AI collaboration model" | Forward-references the design pattern. |
| §352 | (current sentence with "although the company remained unprofitable in 2025 and RPE remained below the pre-period average") | (no change) | Excellent — keep. |

### 9.5 Missing caveats to insert

| Section | Missing caveat |
|---|---|
| §284 / §306 (Rocket benchmark) | Add: "The Rocket 2025 figures reflect the Mr. Cooper acquisition completed in 2025; per-employee comparisons are particularly sensitive to this transaction. The 2025 Rocket expense ratio of 1.032 should therefore not be read as a like-for-like operating-efficiency datum." |
| §306 | Confirm whether "Rocket Companies, 2024, 2025" refers to FY-2023 / FY-2024 10-Ks (filed in calendar 2024 / 2025) or FY-2024 / FY-2025 10-Ks. Audit deliverable D flags this as outstanding. |
| §324 | Add footnote: "Bonferroni correction was applied across the seven keyword groups (α/7 ≈ 0.0071). Of the seven, only Cost/Rates survives strict correction." |
| §337 | Add: "The NLP findings should not be read as evidence that voice AI deployment causes customer-experience deterioration. They are most defensibly read as evidence that the customer-experience dimension of voice AI value creation is multidimensional and is not uniformly captured by any single instrument." |

### 9.6 Suggested re-ordering

The current §5.1–§5.7 order is logical. Consider moving §5.6 (Limitations) into a consolidated Chapter 8 (see §13.3) and replacing §5.6 with a single short paragraph cross-referencing Chapter 8. This concentrates limitations in one examiner-visible location.

---

## 10. Figure, Table, and Appendix Plan

### 10.1 Status of every existing figure and table

| Item | Current location | Keep / revise / move / delete | Issue | Required fix | Priority |
|---|---|---|---|---|---|
| **Figure 5.1** Revenue / Total-Expense Base / Net Loss, Better 2021–2025 | Inline in §5.3.1 | Keep | None substantive | Confirm shaded-period vertical bands are drawn between 2023/2024 (transition start) and 2024/2025 (post-Betsy start). | Low |
| **Figure 5.2** Expense Intensity & Cash Flow, 2021–2025 | Inline in §5.3.2 | Keep | None substantive | Confirm right-panel shows operating cash flow remaining negative in 2025. | Low |
| **Figure 5.3** Workforce Contraction & RPE, 2021–2025 | Inline in §5.3.4 | Revise | Pre-period RPE-average reference line ($0.130M) probably not shown | Add the dashed reference line and label it "2021–2023 average = $0.130M". | Medium |
| **Figure 5.4** VADER Sentiment Distribution, Pre vs Post-Betsy | Inline in §5.4.2 | Keep | None | Confirm legend lists n=1,746 / n=169. | Low |
| **Figure 5.5** Keyword Prevalence by Group | Inline in §5.4.3 | Revise | Bonferroni status of each group should be visible in the figure | Annotate "**Bonferroni-significant**" on Cost/Rates only; annotate "n.s. after Bonferroni" on Digital/Process. | Medium |
| **Figure 5.6** Topic-Share Shifts, Pre vs Post-Betsy | Inline in §5.4.4 | Verify | Caption mentions six topic shifts; confirm all six bars are present and ordered as in §334 | Confirm bars and labels match the §334 reading. | Medium |
| **Table 1 — Dimensions of Business Value Creation through AI in Customer Service** | §99–100 (referenced) | **Insert table body** (currently missing) | Body absent | Use draft in §10.3 below. | High |
| **Operationalization Table** (Dimensions × Indicators × Data Source × Reliability) | §3.6 (first 6×4 table in docx) | Keep | None | Re-label as "Table 3.1 — Operationalization of Business Value Dimensions". | Low |
| **Source Reliability / Data Provenance Table** | §3.7 (currently a duplicate of the Operationalization Table) | **Replace duplicate with new content** | Duplicate | Use draft in §10.4 below. Re-label as "Table 3.2 — Source Reliability and Data Provenance Hierarchy". | High |

### 10.2 Recommended new figures (to add)

| New figure | Where | Purpose |
|---|---|---|
| **Figure 4.1 — Tinman/Betsy/ElevenLabs Architecture** | §4.4 | Box-and-arrow diagram with four labelled layers: (a) Tinman (process-aware operating platform; structured workflow state, document state, eligibility state); (b) Betsy (LLM coordination layer; routine communication); (c) ElevenLabs Agents (voice infrastructure; STT → LLM → TTS pipeline); (d) Human escalation (licensed loan consultants; underwriting / regulated steps). Arrows show data flow. |
| **Figure 4.2 — Mortgage Origination Workflow Before / After Betsy** | §4.2 | Two-row swim-lane: top row = pre-Betsy workflow (lead → human callback → document collection → underwriting → closing); bottom row = post-Betsy workflow (lead → Betsy lead engagement → Betsy mid-funnel coordination → human handoff for underwriting → closing). |
| **Figure 4.3 — Better.com Implementation Timeline** | §4.6 | Horizontal timeline: 2014 founding · 2020 hyper-growth · Q3 2021 layoff · 2022 collapse · 2023 trough · 2024 transition · Oct 17 2024 Betsy launch · June 2025 ElevenLabs partnership · Feb 2026 joint release. |
| **Figure 6.1 — Voice-AI-in-Regulated-Workflow Design Pattern** | §6 (new chapter) | Four boxes (the four prerequisites) with the case-study evidence anchor labelled below each. |

### 10.3 Drop-in body for Table 1 (Lit Review §99 — Dimensions of Business Value Creation through AI in Customer Service)

| # | Dimension | Definition | Representative AI mechanisms | Representative academic anchor |
|---|---|---|---|---|
| 1 | **Operational efficiency** | Reduction in unit cost, cycle time, and waiting time in service delivery | Routine-call automation; document classification; coordination automation | Andrade & Tumelero (2022); Wang et al. (2023); Aggarwal et al. (2025) |
| 2 | **Productivity** | Increase in output per worker through task reallocation rather than substitution | Conversational agent handling tier-1 inbound; human capacity reallocated to complex cases | Brynjolfsson, Li & Raymond (2023); Acemoglu & Restrepo (2019); Aggarwal et al. (2025) |
| 3 | **Customer experience** | Change in service-quality perception, response speed, resolution rate, satisfaction, and discourse | Conversational accessibility; faster response; service consistency | Adam, Wessel & Benlian (2021); Hentzen et al. (2022); Mogaji & Nguyen (2021); Becker et al. (2025); Nussbaum et al. (2025) |
| 4 | **Financial performance** | Aggregate firm-level revenue, profitability, and operating-leverage outcomes | Cumulative effect of (1)–(3) on revenue growth, expense intensity, RPE, and net income | Brynjolfsson et al. (2023); Aggarwal et al. (2025); Hentzen et al. (2022) |

Insert this table body immediately after the §99 sentence "value creation operates across at least four distinct but interrelated dimensions."

### 10.4 Drop-in body for Table 3.2 (Methodology — Source Reliability and Data Provenance Hierarchy)

| Tier | Source type | Examples in this thesis | Audit / verification basis | Required wording in body |
|---|---|---|---|---|
| **High** | SEC 10-K, 10-Q, S-1 (audited financial statements, MD&A) | Better Home & Finance Holding Company (2025a, 2026); Rocket Companies (2024, 2025); financial dataset constructed from these filings | Externally audited financial statements; deterministic ratio calculations from audited inputs | Default; cite without caveat. |
| **High** | SEC 8-K Exhibit 99.1 / earnings release (under SEC reporting obligations) | Better (2024a Betsy launch press release; 2025b Q1 release; 2025c Q2 release) | SEC-filed; subject to materiality and disclosure obligations | Default; cite without caveat. |
| **Medium-High** | Industry report from independent body (subject to internal QA but not externally audited) | Mortgage Bankers Association (2024a, 2024b); Freddie Mac PMMS; Federal Reserve Bank of New York Household Debt and Credit Report | Recognized industry reporting standards; cross-verifiable across editions | Default; treat as "industry context." |
| **Medium-High** | Government regulatory page | Consumer Financial Protection Bureau (n.d.); Fannie Mae Selling Guide | Government-published; updated periodically | Default; cite without caveat. |
| **Medium** | Management-reported operating metric (unaudited) | NPS 39 → 64; "approximately 100,000 mortgage-related phone calls per month"; "1.89 million inbound and outbound calls in 2025" | Management disclosure; not externally audited | Always introduce with: "Better has reported that …" or "Better's management has reported that …"; never present as audited fact. |
| **Medium** | Vendor / case-study material | ElevenLabs blog; Better–ElevenLabs joint release (2026) | Vendor-published; commercial-marketing motivation | Always introduce with: "Vendor materials report …" or "The vendor case study reports …"; never present as evidence of magnitude on business outcomes. |
| **Medium** | Independent self-selected user-generated content (UGC) | Trustpilot reviews (1,915 cleaned) | Verified-review platform; subject to self-selection | Always present with the n_pre / n_post imbalance and self-selection caveat (per §316 / §321). |
| **High** | Peer-reviewed academic publication | Adam et al. (2021); Andrade & Tumelero (2022); Aggarwal et al. (2025); Becker et al. (2025); Brynjolfsson et al. (2023); Goodhue & Thompson (1995); Heskett et al. (1994); Huang & Rust (2018); Maslych et al. (2025); Mogaji & Nguyen (2021); Nussbaum et al. (2025); Wang et al. (2023); Yin (2018); Zhang et al. (2023) | Peer review | Default; cite without caveat. |
| **Medium-Low** | News media | HousingWire; Axios; BusinessWire (republishing press releases) | Editorial standards; not peer-reviewed | Use only for triangulation of timing, not for evidence of magnitude. |
| **Low** | Trade-press / blog | Various AI-vendor blogs | Promotional; no QA | Avoid; use only when no higher-tier source covers the same point. |

This table makes the source-reliability hierarchy *visible* to the examiner and discharges the §3.7 obligation in one place.

### 10.5 Recommended Appendix structure (Appendices A–G)

| Appendix | Title | Source files | Purpose |
|---|---|---|---|
| **A** | Citation audit and reference rebuild | `10_Citation_Audit/A` (audit table); `10_Citation_Audit/E` (orphaned citation resolution); `10_Citation_Audit/H` (final QC checklist) | Documents how the reference list was rebuilt from the original draft; allows examiner to retrace the citation repair. |
| **B** | Financial dataset and reproducibility | `08_Code/financial_metrics_project_report.md`; `08_Code/financial_dataset_annual.csv`; `08_Code/build_dataset_v4.py`; `08_Code/requirements.txt` | Documents the financial pipeline, the dataset, the OLI construction, and the package versions. |
| **C** | NLP pipeline and statistical tables | `08_Code/nlp_project_report.md`; BERTopic hyperparameters; full statistical-test table (chi-square / Fisher / Bonferroni); BERTopic intertopic-distance map; full topic inventory (44 topics) | Documents the NLP pipeline at full reproducibility. |
| **D** | Source reliability classification | `10_Citation_Audit/F_Source_Reliability_Table.md` | Documents the per-source reliability classification used in the body. |
| **E** | Better.com corporate timeline and SEC-filing inventory | `10_Citation_Audit/D_Better_IR_SEC_Verification.md` | Documents which SEC and Better-IR URLs were verified for each Better source. |
| **F** | Trustpilot data quality and cleaning pipeline | `08_Code/cleaning_reviews.ipynb`; pre/post sample sizes; per-year review counts; verification statistics | Documents data cleaning and quality assurance. |
| **G** | Glossary and abbreviations | New | Brief glossary of mortgage-industry abbreviations (DTI, LTV, MBA, RESPA, SAFE Act, TILA, UDAAP, IMB, MSR), AI/NLP terms (LLM, STT, TTS, BERTopic, UMAP, HDBSCAN, VADER, c-TF-IDF), and case-specific terms (Tinman, Betsy, NEO). |

Each appendix should be 2–10 pages. The empirical reports already exist — they only need to be packaged.

---

## 11. Wording and Academic Tone Review

### 11.1 General principle

The thesis should sound *analytical, cautious, evidence-based, and academically confident*. The current draft drifts toward a *promotional / white-paper* register in two places: (a) Chapter 1 §11–§35 and (b) Chapter 4 §170–§192. Inflated adjectives (~69 instances of *important / critical / substantial / fundamentally / vital*) account for most of the drift.

### 11.2 Sentence-level rewrites (concrete examples)

| # | Where | Current wording | Problem | Suggested rewrite | Reason |
|---|---|---|---|---|---|
| 1 | §11 | "Artificial intelligence (AI) has become one of the most transformative technologies of the 21st century, fundamentally reshaping how organizations operate, deliver services, and create value." | "fundamentally reshaping" is unsupported and promotional | "Artificial intelligence (AI) has become a widely deployed technology in 21st-century organizations and has been associated with substantive change in how services are delivered and how value is created (Brynjolfsson et al., 2023; Aggarwal et al., 2025)." | Removes editorial verb; anchors to a real source. |
| 2 | §13 | "AI-powered automation in customer service has revolutionized how organizations handle customer interactions" | "revolutionized" is not defensible | "AI-powered automation has materially changed how organizations handle high-volume customer interactions, with reported gains in resolution rates and time-to-resolution (Andrade & Tumelero, 2022)." | "materially changed" + a specific anchor. |
| 3 | §17 | "Voice AI agents represent a critical evolution in conversational AI" | "critical" overused | "Voice AI agents extend conversational AI into the audio modality, with implications for accessibility, real-time interaction, and operational latency (Aggarwal et al., 2025; Maslych et al., 2025)." | Specific functional description. |
| 4 | §22 | "Better.com offers a unique opportunity to study these dynamics" | "unique opportunity" is a thesis cliché | "Better.com is a revelatory case (Yin, 2018) for studying these dynamics: it has publicly disclosed the deployment of a voice LLM agent (Betsy) in U.S. mortgage origination, has a publicly traded financial trajectory, and has an active independent customer-discourse footprint." | Anchors to Yin and to the three concrete reasons. |
| 5 | §28 | "This thesis makes important contributions to the literature on AI business value" | "important" is editorialising | "This thesis contributes to the literature on AI business value by triangulating SEC-filed financial trajectory, NLP analysis of independent customer discourse, and qualitative process tracing of integration architecture for a voice LLM agent in U.S. mortgage origination." | Replaces editorial adjective with concrete contribution. |
| 6 | §35 | "The findings have substantial implications for both academic theory and managerial practice" | "substantial" is a promotional residue | "The findings have implications for academic theory on AI business value and for managerial practice in regulated financial-services workflows." | Strips the promotional adjective; lets the implications speak for themselves in the body. |
| 7 | §41 | (paragraph reads like a press release for Better) | Marketing-language residue | Rewrite the paragraph to *describe* Better (founded 2014, public via SPAC merger 2023, NASDAQ: BETR, mortgage origination with proprietary Tinman platform, voice agent Betsy launched October 17, 2024) without subjective qualifiers. | Convert from advocacy to description. |
| 8 | §170 | "Better.com is a digital-first mortgage lender that has consistently positioned itself at the intersection of financial services and technology" | "consistently positioned itself" is the company's own framing | "Better.com is a U.S. mortgage lender that operates a digital-first origination model with a proprietary technology platform (Tinman); the company became publicly listed via SPAC merger in 2023 and trades on NASDAQ as BETR (Better Home & Finance Holding Company, 2026)." | Anchors to the SEC filing rather than to corporate self-positioning. |
| 9 | §175 | "The U.S. mortgage industry is a critical component of the broader financial services ecosystem" | "critical component" is filler | "The U.S. mortgage industry intermediates a substantial share of household borrowing; outstanding mortgage debt totalled approximately $13 trillion as of Q1 2025 (Federal Reserve Bank of New York, 2025)." | Replaces opinion with a specific datum and a real source. |
| 10 | §192 | "Tinman therefore acts as the architectural prerequisite for Betsy" | "therefore acts as" is too strong for a single case | "In the Better.com case, Tinman appears to function as the architectural prerequisite for Betsy; the generalizability of this prerequisite to other firms is discussed in Chapter 7." | Bounds the claim to the case. |
| 11 | §211 (operating figures) | (vendor figure repeated without inline reliability flag) | Treats vendor evidence as fact | "The February 2026 Better–ElevenLabs joint release reports that Betsy handled approximately 100,000 mortgage-related phone calls per month and 1.89 million inbound and outbound calls in 2025; these figures are management- and vendor-reported and are not independently audited (Better Home & Finance Holding Company & ElevenLabs, 2026)." | Adds the inline reliability flag the §3.7 hierarchy requires. |
| 12 | §304 (RPE) | (RPE recovery sometimes presented without the pre-period qualifier) | Risks reading as full productivity recovery | "Revenue per employee improved by approximately 42.9 percent between 2024 and 2025 (from $0.087 million to $0.124 million), although this still falls short of the pre-period (2021–2023) average of $0.130 million." | Already done in §305 — make sure no earlier paragraph drops the qualifier. |
| 13 | §340 | "is the textbook descriptive signature of operational leverage" | "textbook signature" verges on tautology | "is descriptively consistent with the textbook signature of operational leverage" | Adds the qualifier-of-claim. |

### 11.3 Patterns to search-and-replace globally

| Search term | Recommended action |
|---|---|
| "fundamentally" | Remove unless empirically anchored. |
| "revolutionized" / "revolutionary" / "revolutionizes" | Replace with "materially changed" or "extends." |
| "important" (in §11–§35 and §170–§192) | Replace with the specific reason; if there is no specific reason, delete the sentence. |
| "critical" (in §11–§35 and §170–§192) | Replace with "necessary" or with the specific functional reason. |
| "vital" | Replace with "necessary" or delete. |
| "substantial" (when ungrounded) | Replace with the specific magnitude. |
| "clearly proves" / "demonstrates causally" / "validates Better's claims" | Never use; replace with "consistent with," "supports," "is associated with." |
| "Betsy caused …" / "AI drove …" / "financial recovery was caused by AI" | Replace with "consistent with operational leverage associated with the broader Betsy/Tinman AI operating model." |
| "the company's strong commitment to innovation" / similar | Delete or attribute as company self-description. |

The sentence-level rewrite list in §11.2 covers the most consequential instances; a global scan of Chapter 1 should remove the rest in 30–60 minutes.

### 11.4 Paragraph-level edits

| Where | Current pattern | Suggested fix |
|---|---|---|
| §11–§17 (introduction opening) | Five paragraphs of broad AI-transformation context that are not specific to financial services | Compress to two paragraphs: (a) AI in services generally; (b) AI in financial services specifically. |
| §41 (Better introduction) | Reads like a press release | Convert to a descriptive paragraph anchored to SEC filings and to the Tinman / Betsy / ElevenLabs technical setup. |
| §49 (thesis-structure summary) | Promises Chapter 6, 7, 8, 9 | Update once those chapters are written. |

---

## 12. High-Risk Claim and Number Audit

The following table lists every major numerical or empirical claim, its location, the source it should map to, and any required correction or wording change.

| # | Claim (exact wording in thesis) | Where | Source | Reliability tier | Number correct? | Interpretation correct? | Required action |
|---|---|---|---|---|---|---|---|
| 1 | Better revenue 2023 / 2024 / 2025 ≈ $76.8M / $108.5M / $164.9M | §288 | Better 10-K (2024, 2025); financial dataset | High (audited) | Yes | Yes | Keep. |
| 2 | Revenue growth 2024→2025 ≈ 52.0% | §288, §340, §352 | derived | High | Yes | Yes | Keep. |
| 3 | Revenue growth 2023→2025 ≈ 114.6% | §288 | derived | High | Yes | Yes | Keep, but always pair with the *partial-recovery* qualifier (revenue still below 2021 peak). |
| 4 | Total expenses 2023 / 2024 / 2025 ≈ $368.1M / $313.9M / $330.7M | §292 | financial dataset | High | Yes | Yes | Keep, but reiterate cross-company comparability caveat (§176 of fin. report). |
| 5 | Expense ratio 2023 / 2024 / 2025 = 4.79 / 2.89 / 2.01 | §292, §340 | derived | High | Yes | Yes | Keep. |
| 6 | Net loss 2024→2025 ≈ −19.6% | §298 | derived | High | Yes | Yes | Keep, but pair with "company remained unprofitable in 2025" qualifier. |
| 7 | RPE 2023 / 2024 / 2025 ≈ $0.094M / $0.087M / $0.124M | §302 | derived | High | Yes | Yes | Keep with pre-period $0.130M comparator. |
| 8 | RPE improvement 2024→2025 ≈ +42.9% | §302, §340 | derived | High | Yes | Yes | Always pair with "still below pre-period $0.130M average." |
| 9 | Headcount 2021 ≈ 10,400 | §302 | Better S-1 | Medium-High | Yes | Yes | Keep — note that 2021 figure is from S-1 not 10-K. |
| 10 | OLI 2025 ≈ 195.3 (2023 = 100) | §305 | derived (Appendix B) | Medium (author construct) | Yes — confirm by re-running notebook | Acceptable as compact visualization | Keep with the existing "supplementary, not primary evidence" qualifier. |
| 11 | NPS 39 → 64 | §315 | Better Q4 2024 release; Better 2025 10-K | Medium (management-reported) | Yes (matches release) | Acceptable but must be qualified | Always introduce with "Better has reported that …" and pair with the 7-reason caveat (§316). |
| 12 | "Approximately 100,000 mortgage-related phone calls per month" | §211 | Better–ElevenLabs joint release (2026) | Medium (vendor + management) | Yes | Acceptable | Always introduce with "Better and ElevenLabs report …"; never present as audited operating fact. |
| 13 | "1.89 million inbound and outbound calls in 2025" | §211 | Better–ElevenLabs joint release (2026) | Medium (vendor + management) | Yes | Acceptable | Same caveat as #12. |
| 14 | "+30% conversion uplift" / "41% reduction in cost-to-originate" | (in case-study materials, sometimes mentioned in passing) | Better–ElevenLabs joint release (2026); Better earnings transcripts | Medium (vendor + management) | Magnitude vendor-reported | Acceptable as illustrative only | If repeated in body, always with vendor caveat; do not use as evidence of business-value magnitude. |
| 15 | Trustpilot pre / post n = 1,746 / 169 | §313, §318 | NLP report §2.3 | Medium (independent UGC) | Yes | Yes | Keep. |
| 16 | Star rating decline 4.28 → 3.86 (Δ = −0.42; p = 0.0019; d = 0.29) | §318 | NLP report | Medium-High (statistical with bias caveat) | Yes | Yes | Keep — already paired with §316 7-reason caveat. |
| 17 | VADER decline 0.642 → 0.515 (Δ = −0.13; p = 0.0057; d = 0.25) | §318 | NLP report | Medium-High | Yes | Yes | Keep. |
| 18 | Cost/Rates −12.35 pp; Bonferroni-significant | §324 | NLP report §4.3 | Medium-High | Yes (PR #2 fixed inversion) | Yes | Keep. Add explicit Bonferroni footnote. |
| 19 | Digital/Process −8.98 pp | §324 | NLP report §4.3 | Medium-High | Yes | Yes | Keep with "not Bonferroni-robust" qualifier. |
| 20 | AI mentions ~1.15% / 1.18% pre/post; Fisher p = 1.0000 | §327 | NLP report §4.3 | Medium-High | Yes | Yes | Keep. |
| 21 | BERTopic clustered n_pre / n_post = 1,077 / 121 | §331 | NLP report §4.2 | Medium | Yes | Yes | Keep — denominator-consistency note is good. |
| 22 | Topic shifts: Refinance −7.66 / HELOC +4.22 / Smooth Transaction +4.03 / Responsive Service +3.93 / Closing Timeline +3.55 / Home Purchase −3.48 | §334 | NLP report §4.5 | Low–Medium (descriptive only) | Confirm before submission by re-running notebook | Acceptable (compositional reading) | Keep §334 wording. |
| 23 | Rocket 2025 expense ratio ≈ 1.032 | §306 | Rocket 10-K (2025) | High (audited) but distorted by Mr-Cooper acquisition | Yes (audited) | Comparability bounded | Add caveat per §9.5. |
| 24 | "Approximately 52.0 percent revenue growth and only approximately 5.3 percent expense growth" (RQ2 summary) | §352 | derived | High | Yes | Yes | Keep; §352 is the correct integrated wording. |
| 25 | Mortgage industry context: U.S. mortgage debt ≈ $13T as of Q1 2025 | §175 (proposed addition) | FRBNY Household Debt and Credit Report | Medium-High | Confirm with the most recent FRBNY release before submission | Yes | If used, anchor with FRBNY citation. |

**Audit conclusion:** all numerical claims in the thesis are correct against the underlying empirical reports; the corrections are wording-level (caveat insertion), not numerical.

---

## 13. Remaining Chapters Build Plan

This section gives section-by-section outlines and sample paragraph starters for the four chapters that do not yet exist in the docx.

### 13.1 Chapter 6 — A Voice-AI-in-Regulated-Workflow Design Pattern (≈2,500–3,500 words)

**Purpose:** turn the four prerequisites identified in Chapter 5 into a transferable design artefact in the design-science sense (Hevner et al., 2004). Anchor the pattern in the case but generalize it so the reader sees how it extends to retail-banking servicing, insurance servicing, and similar high-volume regulated communication-intensive workflows.

**Section structure (recommended):**

1. **§6.1 Introduction.** Restate the four prerequisites; cite Hevner et al. (2004) for design-science framing. Distinguish *design pattern* from *theoretical model*: a pattern is a transferable configuration; a theoretical model is a causal claim. This thesis offers the former, not the latter.
2. **§6.2 Preconditions for value capture.** *Process maturity* (the workflow must already be digitised and process-aware — Tinman case); *data accessibility* (structured workflow state must be exposed to the agent); *organizational readiness* (pre-existing human-AI coordination structures); *regulatory clarity* (the regulated-step boundary must be explicit before deployment).
3. **§6.3 Voice AI architecture.** *Process-aware operating platform* (Tinman); *coordination-layer agent scope* (Betsy: routine communication, not underwriting); *low-latency voice infrastructure* (ElevenLabs Agents: STT → LLM → TTS pipeline; latency < ~4s); *auditable human escalation* (licensed-consultant routing for regulated steps). Insert architecture diagram (Figure 6.1).
4. **§6.4 Implementation stages.** *Stage 1 — pilot deployment* (limited use case; e.g., Betsy's initial post-decision update window); *Stage 2 — coordination expansion* (mid-funnel scheduling, status updates); *Stage 3 — scaling and monitoring* (volume scaling; vendor-reported call volume); *Stage 4 — performance measurement* (multidimensional measurement using audited financials, management-reported operating KPIs, and independent customer discourse — see §10.4 source-reliability table).
5. **§6.5 Business value mechanisms.** Map each prerequisite to each value dimension: process-aware platform → cost efficiency / labor productivity; coordination-layer agent → labor productivity / customer experience (ambiguous); voice infrastructure → customer experience (perception); human escalation → trust / regulatory compliance / revenue conversion (where AI cannot close).
6. **§6.6 Boundary conditions.** *Regulated domain* (mortgage origination is regulated; the pattern extends to other regulated high-volume workflows); *data quality* (structured workflow data is a precondition); *process standardization* (the pattern fails for unstandardized processes); *trust and transparency* (customer must be able to escalate); *macroeconomic confounding* (the financial-leverage signal in Chapter 5 is partially driven by market recovery; a parallel deployment in a neutral macro environment would be required to isolate the AI contribution).
7. **§6.7 Transferability.** Map the pattern to two adjacent settings without overreaching: *retail-banking servicing* (status updates, dispute initiation, document submission); *insurance servicing* (claim status, premium queries, coverage updates). State explicitly that transferability claims are working hypotheses for future research, not established findings.

**Sample opening paragraph:**

> This chapter formalizes the integration prerequisites identified in Chapter 5 as a design pattern in the design-science sense (Hevner et al., 2004) — a transferable configuration of architectural, organizational, and governance components rather than a causal model. The pattern is derived from a single revelatory case (Better.com) and is intended to support analytic, not statistical, generalization (Yin, 2018). Its purpose is to make explicit the four conditions under which a voice LLM agent in a regulated financial-services workflow is most likely to generate measurable operational leverage while remaining largely invisible to the end customer.

### 13.2 Chapter 7 — Discussion (≈2,000–3,000 words)

**Purpose:** connect the empirical findings back to the literature reviewed in Chapter 2 and the conceptual framework introduced in §2.6.

**Section structure:**

1. **§7.1 Introduction.** Restate the headline finding: Better's post-deployment trajectory is consistent with AI-enabled operational leverage in the financial-operational dimension and divergent (NPS up, Trustpilot down) in the customer-experience dimension. Frame the chapter as a four-way conversation with the literature: (a) chatbot/customer-service AI literature; (b) voice-AI literature; (c) business-value-of-IT/AI literature; (d) consumer-behavior/AI-interaction literature.
2. **§7.2 Voice AI literature: confirm and extend.** Compare with Wang et al. (2023) and Zhang et al. (2023) — both find AI agents perform comparably to human agents but with composition shifts. Better's case extends this by showing comparable performance in a *regulated* setting where the integration boundary is explicit. Compare with Aggarwal et al. (2025) — their B2B/B2C framework predicts ambiguous customer-perception effects when AI operates as backend infrastructure; Better's case is a real-world instance of that prediction. Compare with Becker et al. (2025) and Maslych et al. (2025) on voice naturalness and latency; the Better case suggests that *latency floor* and *voice quality* are plausibly necessary-but-not-sufficient conditions but not directly testable in the present design.
3. **§7.3 Chatbot / customer-service AI literature: confirm and complicate.** Compare with Andrade & Tumelero (2022): they find efficiency gains and resolution-rate improvements; Better's financial-operational evidence is consistent with that. Compare with Adam et al. (2021): compliance and reciprocity gains; Better's case is silent on this dimension. Compare with Hentzen et al. (2022): AI in customer-facing financial services often produces ambiguous customer-perception effects; Better's NPS-vs-Trustpilot divergence is exactly this ambiguity.
4. **§7.4 Business value of IT/AI: contribute.** Compare with Brynjolfsson, Li & Raymond (2023): productivity gains from AI tools come with lower-tail effects (junior workers benefit more). Better's case cannot test this directly but is consistent with it (RPE recovers without headcount expansion → productivity is shifting upward across the existing workforce). Compare with Acemoglu & Restrepo (2019): displacement-reinstatement framework; Better's case is a real-world instance of *task reallocation* rather than labor substitution. The thesis's contribution: a triangulated, single-case demonstration that AI business value in regulated services is *multidimensional and asymmetric* — operational leverage visible in financial trajectory; customer-experience effects ambiguous and possibly negative; AI invisible to most customers.
5. **§7.5 NPS-vs-Trustpilot divergence: a methodological contribution.** What does the divergence add to the literature? It adds an empirical case for the *measurement-instrument-dependence* of AI customer-experience evidence. Internal management instruments (NPS) and external public-discourse instruments (Trustpilot) capture *different distributions* of customer experience and respond differently to AI deployment. Future AI business-value studies in regulated services should triangulate at least these two instrument types, not substitute one for the other.
6. **§7.6 Invisible AI infrastructure: a theoretical contribution.** Better's case operationalizes the "invisible AI infrastructure" concept (Mogaji & Nguyen, 2021; Brynjolfsson et al., 2023) in a regulated setting. The discourse evidence — explicit AI mentions at ~1% in both periods — is the strongest empirical support yet for the proposition that voice AI in regulated workflows can produce operational leverage without customer awareness. This has implications for AI ethics (consent and disclosure), for marketing (the "AI inside" branding heuristic does not apply), and for measurement (customer-experience instruments must look at AI-related effects without relying on customers to explicitly attribute experience to AI).
7. **§7.7 Regulated financial services: scope and boundaries.** What does the case suggest about regulated financial services more broadly? (a) the regulated-step boundary is the natural human-AI hand-off point; (b) the cost of integration is dominated by *building the process-aware platform*, not by *adding the voice agent*; (c) compliance frameworks (SAFE Act, TILA-RESPA, CFPB UDAAP) shape the agent's task scope before any model-design choice. These three observations are consistent with Mogaji & Nguyen (2021) and extend their argument with concrete operational evidence.

**Sample opening paragraph:**

> The empirical findings reported in Chapter 5 enter a four-way conversation with the literature reviewed in Chapter 2. With respect to voice AI, the Better.com case extends the call-center evidence of Wang et al. (2023) and Zhang et al. (2023) into a regulated U.S. financial-services workflow and provides a real-world instance of the B2B/B2C value-creation distinction theorized by Aggarwal et al. (2025). With respect to chatbot and customer-service AI, the case complicates the standard story in Andrade and Tumelero (2022) and Adam et al. (2021): the financial-operational dimension of business value is consistent with that literature, but the customer-experience dimension is divergent across instruments. With respect to the broader business-value-of-AI tradition (Brynjolfsson et al., 2023; Acemoglu & Restrepo, 2019), the case is consistent with task reallocation rather than labor substitution and adds an empirical instance of measurable operational leverage emerging without proportional headcount expansion.

### 13.3 Chapter 8 — Limitations (≈1,200–1,800 words)

**Purpose:** consolidate limitations into a single examiner-visible chapter. Drawn from material currently scattered between §3.7 and §5.6.

**Section structure (one paragraph each):**

1. **§8.1 Single-case design.** Findings support analytic, not statistical, generalization (Yin, 2018). The Better.com case may be unrepresentative on at least three dimensions: digital-first architecture, very recent post-restructuring trajectory, and high public-disclosure footprint.
2. **§8.2 No causal identification.** No counterfactual; multiple confounders include macroeconomic recovery, internal restructuring (NEO channel, headcount adjustments), and cyclic mortgage-industry dynamics. The empirical inference is *consistent with*, not *caused by*.
3. **§8.3 Annual financial granularity.** SEC 10-K data is annual; Betsy launched October 17, 2024. The 2024 fiscal year is necessarily a *transition year* combining pre- and post-Betsy quarters. Quarterly data (10-Q) would partially address this but the thesis design does not exploit it.
4. **§8.4 Better-specific digital maturity.** Better.com's process-aware platform (Tinman) is unusually mature relative to typical mortgage lenders. The four-prerequisite design pattern in Chapter 6 may therefore be harder to instantiate in firms with less mature operating platforms.
5. **§8.5 Public-data reliance.** All evidence is from public sources (SEC, vendor materials, Trustpilot, industry reports). No interviews, no internal Better data. This is a strength for replicability but a weakness for depth.
6. **§8.6 Vendor and company source bias.** Vendor case-study materials (ElevenLabs blog; Better–ElevenLabs joint release) over-represent successful implementations and under-represent failure modes. The thesis is honest about this (§5.6) but the limitation cannot be fully eliminated without independent validation.
7. **§8.7 Trustpilot self-selection and pre/post imbalance.** The pre-period n is 1,746; the post-period n is 169. The post-period is small, the post-period reviewers are likely more emotionally engaged than the average customer, and the pre-period is very heterogeneous (it covers four years, including the 2021 hyper-growth, the 2022 collapse, and the 2023 trough). The seven-reason caveat in §316 addresses this in detail.
8. **§8.8 Topic-modeling limitations.** Topic shares are sensitive to BERTopic hyperparameters; outlier rates are high (33.6%); short reviews exhibit high lexical variability. Topic-level findings are descriptive only.
9. **§8.9 Benchmark limitations.** Rocket Mortgage is not a counterfactual. The 2025 Mr-Cooper acquisition distorts Rocket's per-employee and expense-ratio metrics. Rocket is informative as a *directional industry benchmark* but cannot serve as a counterfactual for Better.
10. **§8.10 Generalizability limits.** Findings most plausibly transfer to other regulated, high-volume, communication-intensive financial workflows with mature digital operating platforms (retail banking servicing; insurance servicing). They probably do not transfer to firms without such a platform.
11. **§8.11 Summary.** One paragraph stating that, given these limitations, the thesis's defensible contribution is to *configurations and patterns*, not to causal effect sizes. (This sentence becomes the bridge to Chapter 9.)

### 13.4 Chapter 9 — Conclusion (≈1,200–1,800 words)

**Purpose:** answer the RQs directly, articulate the contributions, and identify future research.

**Section structure:**

1. **§9.1 Direct answer to RQ1.** The Betsy/Tinman voice AI operating model has been integrated into Better.com's mortgage origination process through four architectural and organizational prerequisites: (i) a process-aware operating platform (Tinman); (ii) a coordination-layer scoping of the voice agent (Betsy); (iii) low-latency voice infrastructure (ElevenLabs Agents); (iv) an auditable human-AI collaboration model with licensed-consultant escalation at the regulated boundary. These four prerequisites jointly form the design pattern in Chapter 6.
2. **§9.2 Direct answer to RQ2.** The post-deployment financial trajectory at Better.com is consistent with AI-enabled operational leverage in the financial-operational dimension (revenue +52.0% / expense +5.3% between 2024–2025; expense ratio 2.89 → 2.01; net loss narrowing 19.6%; RPE +42.9% to $0.124M, still below the pre-period $0.130M average). The customer-experience dimension is divergent across instruments: management-reported NPS rises 39 → 64; independent Trustpilot star rating declines 4.28 → 3.86 (p ≈ 0.002, d ≈ 0.29); VADER sentiment declines 0.642 → 0.515 (p ≈ 0.006, d ≈ 0.25); explicit AI mentions remain at ~1% in both periods. The strongest mediating factors are: process-aware platform maturity, agent scope to the coordination layer, low-latency voice infrastructure, governance-defined regulated-step escalation, and macroeconomic recovery.
3. **§9.3 Empirical contribution.** First end-to-end triangulated case study of a voice LLM agent in U.S. mortgage origination linking SEC-filed financial trajectory, BERTopic+VADER customer-discourse analysis, and qualitative process tracing of integration architecture.
4. **§9.4 Methodological contribution.** Four-tier source-reliability hierarchy (audited financials → company disclosures → independent customer discourse → vendor/case materials) for evaluating AI business-value claims. The methodological contribution is that AI customer-experience evidence is instrument-dependent: NPS and public-discourse instruments capture different distributions and respond differently to AI deployment; future studies should triangulate, not substitute.
5. **§9.5 Theoretical contribution.** Operationalization of the *invisible AI infrastructure* concept in a regulated setting: voice AI in regulated financial-services workflows can produce measurable operational leverage while remaining largely invisible to end customers. This has implications for AI ethics, marketing, and measurement.
6. **§9.6 Practical contribution.** A four-prerequisite *Voice-AI-in-Regulated-Workflow* design pattern (Chapter 6) that is transferable to retail-banking servicing, insurance servicing, and analogous high-volume regulated communication-intensive financial workflows.
7. **§9.7 Future research.** (a) Multi-case extension to retail banking servicing and insurance claims; (b) higher-frequency (quarterly) financial analysis with within-firm 10-Q data; (c) controlled latency and voice-quality experiments anchored to the Becker et al. (2025) and Maslych et al. (2025) protocols; (d) a customer-side research design (survey of Better customers post-Betsy interaction) to triangulate against management NPS and public Trustpilot signals; (e) a regulated-domain comparison (e.g., voice AI in healthcare insurance vs voice AI in mortgage) to test the regulated-boundary-as-hand-off-point hypothesis.
8. **§9.8 Final sentence.** Use the revised final claim from §4.4 of this report.

---

## 14. Benchmark Against Similar Academic Research

This section identifies five reference points and the concrete lesson each carries for *this* thesis. None of these papers is to be copied; they are cited in the bibliography (where already present) only as benchmarks for structure and tone.

| # | Reference paper / paper type | Relevant lesson | What this thesis currently does | What to improve |
|---|---|---|---|---|
| 1 | **Wang, Q., Yang, X., & Cady, F. (2023). Productivity and quality: A study on AI-assisted customer service.** *Production and Operations Management* | Quantitative AI-versus-human field-experiment paper. Strong on (a) clean pre/post identification, (b) reporting effect sizes with confidence intervals, (c) acknowledging composition shifts (which calls AI handles vs which it routes). | Cited as a literature anchor; the Better case is positioned as the regulated-workflow extension. | The Discussion (Chapter 7) should explicitly compare Better's evidence to Wang et al.'s field-experiment evidence, noting that Better cannot offer a controlled comparison but does offer a real-world deployment in a regulated setting. |
| 2 | **Brynjolfsson, E., Li, D., & Raymond, L. R. (2023). Generative AI at work.** *NBER WP 31161* | Workplace-productivity-of-AI paper. Strong on (a) within-firm panel with 5,179 customer support agents, (b) heterogeneous treatment effects (junior workers gain more), (c) explicit task reallocation framing. | Cited; the Better case is positioned as a real-world instance of AI-enabled productivity gains. | Add one paragraph in §7.4 noting that Better's RPE recovery is *consistent* with within-firm task reallocation but cannot test the heterogeneous-treatment-effect prediction without worker-level data. |
| 3 | **Andrade, I. M., & Tumelero, C. (2022). Increasing customer service efficiency through AI chatbot.** *Revista de Gestão*, 29(3) | Single-organization customer-service-AI case study. Strong on (a) pre/post efficiency metrics (problem-resolution rate 77% → 92.1%; time-to-resolution reduction), (b) operational mechanism description, (c) honest framing of single-case evidence. | Cited and discussed in §86. | The thesis's structure is *broadly similar* to Andrade & Tumelero's but covers more dimensions (financial trajectory + customer discourse + integration architecture). Make this explicit in §1.5 (Relevance and Contribution). |
| 4 | **Aggarwal, A. K., Kumar, S., & Srivastava, P. R. (2025). Voice-AI in financial services: A B2B vs B2C value-creation framework.** *European Journal of Marketing* | Theory paper on voice-AI value creation in financial services. Strong on (a) clear framework with B2B and B2C value surfaces, (b) explicit boundary conditions, (c) appropriate caveats. | Cited as the central voice-AI-value-creation theoretical anchor. | Make the conceptual-framework subsection (§2.6, drafted in §6.4 of this report) explicitly Aggarwal-aligned by mapping the four-prerequisite design pattern to Aggarwal's B2B and B2C surfaces. |
| 5 | **Yin, R. K. (2018). *Case Study Research and Applications* (6th ed.). SAGE.** | The methodology canon for single-case revelatory designs. Strong on (a) analytic vs statistical generalization, (b) replication logic, (c) chain-of-evidence requirements. | Cited as the case-study-design anchor. | Make the *chain-of-evidence* requirement explicit in §3.7: cite Yin specifically for the four-tier source-reliability hierarchy (audited → company-disclosed → independent → vendor) as a contemporary instantiation of his chain-of-evidence requirement. |
| 6 | **Hentzen, J. K., Hoffmann, A. O. I., & Dolan, R. (2022). Artificial intelligence in customer-facing financial services: A systematic literature review.** *International Journal of Bank Marketing*, 40(6) | Systematic review of customer-facing AI in financial services. Strong on (a) typology of AI use cases, (b) identification of recurring measurement-instrument-dependence problem, (c) acknowledgment of regulated-setting constraints. | Cited. | Strengthen §2.1 by using Hentzen et al.'s typology to position Better's voice agent specifically (coordination layer, customer-facing but regulated, multi-instrument measurement). |

### 14.1 Structural features strong papers in this area share

1. **Clear research-gap statement at the close of the literature review.** This thesis currently ends §2 weakly; §6.4 of this report drops in a research-gap statement.
2. **Conceptual framework section explicitly named.** This thesis currently invokes three lenses but does not integrate them; §6.4 above adds an integrating proposition.
3. **Operationalization table.** This thesis has one (currently duplicated with the source-reliability table); §10.4 above replaces the duplicate.
4. **Source-reliability hierarchy.** This thesis has the *intent* but not the *table*; §10.4 above provides it.
5. **Reproducibility appendix.** Strong empirical IS papers include package versions and hyperparameters; §7.2 above adds the reproducibility paragraph and the Appendix B/C pointer.
6. **Limitations consolidated in one place.** Strong papers do not scatter limitations across body chapters; §13.3 above moves them to a dedicated Chapter 8.
7. **Direct one-paragraph-per-RQ answers in the conclusion.** Strong papers do not bury RQ answers in a discussion summary; §13.4 above gives the direct-answer paragraphs.

### 14.2 Methodological safeguards strong papers include

1. Effect-size reporting with confidence or credible intervals.
2. Multiple-comparisons correction explicitly stated.
3. Sample-size and self-selection caveats.
4. Distinction between audited and management-reported metrics.
5. Distinction between description and causal inference.
6. Disclosure of code and data provenance.

This thesis does (1), (2), (3), (4), (5) — points (1)–(5) are all present in Chapter 5 and the empirical reports. Point (6) is partially done (the `08_Code` directory exists; `requirements.txt` was added in PR #2); the explicit pointer paragraph in methodology (§7.2 above) closes the loop.

### 14.3 What this thesis already does at strong-paper standard

- Honest treatment of the NPS-vs-Trustpilot divergence (the seven-reason caveat in §316 is genuinely best-practice and should be highlighted to the supervisor as evidence of methodological care).
- Multidimensional triangulation across three strands of evidence (financial / discourse / integration architecture).
- Explicit Bonferroni correction applied to keyword tests.
- Pre-period heterogeneity acknowledged.
- Single-vendor source bias acknowledged.

### 14.4 What this thesis should emulate but does not yet

- Explicit conceptual-framework section (fixed via §6.4).
- Consolidated limitations chapter (fixed via §13.3).
- Reproducibility appendix and Appendix B/C pointer (fixed via §7.2 and §10.5).
- Direct-answer-per-RQ conclusion structure (fixed via §13.4).

---

## 15. Prioritized Next-Steps Roadmap

The work plan is divided into four tiers. Each task lists chapter affected, estimated difficulty (Low / Medium / High), why it matters, and the expected output.

### A. Must-fix before supervisor submission (≈3–5 days)

| # | Task | Chapter | Difficulty | Why it matters | Expected output |
|---|---|---|---|---|---|
| A1 | Replace duplicated 6×4 table in §3.7 with the Source Reliability / Data Provenance Table | Ch 3 | Low | Removes the most visible structural error in the docx. | Table 3.2 inserted; old duplicate deleted. |
| A2 | Insert reproducibility paragraph + Appendix B/C pointer | Ch 3 | Low | Discharges the reproducibility expectation. | One paragraph after §148; Appendices B/C drafted. |
| A3 | Insert Table 1 body in §99 (Lit Review) | Ch 2 | Low | Removes a missing-table reference. | 4-row table inserted. |
| A4 | Insert the missing 5th sub-strand "Consumer Behavior and AI Interaction" | Ch 2 | Medium | Removes the structural inconsistency between intro promise and body delivery. | ~600-word subsection (drafted in §6.3). |
| A5 | Insert Conceptual Framework subsection (§2.6) | Ch 2 | Medium | Integrates the three theoretical lenses; ends the lit review on a research-gap statement. | ~400-word subsection (drafted in §6.4). |
| A6 | Write Chapter 6 — Voice-AI-in-Regulated-Workflow Design Pattern | Ch 6 | High | Answers the implicit "so what?" question; deliverable promised in §49. | ~2,500–3,500 words; Figure 6.1; outline in §13.1. |
| A7 | Write Chapter 7 — Discussion | Ch 7 | High | Connects findings back to literature; deliverable promised in §49. | ~2,000–3,000 words; outline in §13.2. |
| A8 | Write Chapter 8 — Limitations | Ch 8 | Medium | Consolidates limitations into one examiner-visible place. | ~1,200–1,800 words; outline in §13.3. |
| A9 | Write Chapter 9 — Conclusion | Ch 9 | Medium | Provides direct one-paragraph-per-RQ answers; deliverable promised in §49. | ~1,200–1,800 words; outline in §13.4. |
| A10 | Apply the 13 sentence-level rewrites in §11.2 | Ch 1, Ch 4, Ch 5 | Low | Aligns the academic register; removes promotional residue. | 13 paragraphs revised. |
| A11 | Resolve the seven outstanding judgement calls in `10_Citation_Audit/README.md` §"Outstanding Items" | refs / Ch 4–5 | Medium | Locks the citation audit. | Each item resolved (correct in body; correct in reference). |
| A12 | Consolidate methodological risks into a single §3.10 sub-section | Ch 3 | Low | Makes the seven risks examiner-visible at one glance. | ~300-word consolidated subsection. |
| A13 | Decide on Hevner (2004) and Qualtrics (2024): cite-once or drop | Ch 6 / Ch 5 / refs | Low | Cleans the reference list of uncited entries. | Both decisions made; reference list updated. |

### B. Should-fix for stronger grade (≈2–3 days)

| # | Task | Chapter | Difficulty | Why it matters | Expected output |
|---|---|---|---|---|---|
| B1 | Add Architecture Diagram (Figure 4.1) | Ch 4 | Medium | Makes the four-prerequisite pattern visually concrete. | One diagram. |
| B2 | Add Mortgage Origination Workflow Before/After Betsy (Figure 4.2) | Ch 4 | Medium | Concretizes Tinman/Betsy roles. | One swim-lane diagram. |
| B3 | Add Better.com Implementation Timeline (Figure 4.3) | Ch 4 | Low | Strengthens the temporal narrative. | One horizontal timeline. |
| B4 | Add Evidence Source Hierarchy Table for Chapter 4 | Ch 4 | Low | Discharges the §4.5 vendor-evidence caveat. | One small table. |
| B5 | Compress §178–§182 / §218–§224 / §232–§246 per §8.4 | Ch 4 | Medium | Tightens Chapter 4 from white-paper to thesis register. | ~3 sections compressed by ~30–40%. |
| B6 | Add the §306 Rocket-comparability caveat | Ch 5 | Low | Removes the strongest residual overclaim. | One paragraph. |
| B7 | Add the §324 Bonferroni footnote | Ch 5 | Low | Makes the multiple-comparisons logic visible in-figure. | One footnote. |
| B8 | Add the §327 / §337 missing caveats | Ch 5 | Low | Prevents misreading of NLP results as causal evidence. | Two short paragraphs. |
| B9 | Apply Chapter 1 search-and-replace pass per §11.3 | Ch 1 | Low | Aligns the academic register globally. | ~30–60 minutes of editing. |

### C. Nice-to-have / polish (≈1–2 days)

| # | Task | Chapter | Difficulty | Why it matters | Expected output |
|---|---|---|---|---|---|
| C1 | Add 2–3-sentence voice-AI literature deepening (Becker / Nussbaum / Maslych) in §2.3 | Ch 2 | Low | Strengthens the lit review's voice-AI strand without bloat. | Three sentences. |
| C2 | Add 1 sentence on digital mortgage origination in §2.1 (or explicit gap statement if no source verifiable) | Ch 2 | Low | Anchors the regulated-setting framing. | One sentence or one-sentence acknowledged gap. |
| C3 | Re-run the BERTopic notebook before submission to lock topic-share figures | Ch 5 / 08_Code | Low | Final reproducibility check. | Confirmed numbers in §334. |
| C4 | Tighten §104 pragmatism paragraph by ~30% | Ch 3 | Low | Removes philosophical scaffolding that is not used downstream. | Two paragraphs. |
| C5 | Build Figure 5.5 Bonferroni annotation | Ch 5 | Low | Makes Bonferroni status visible per group. | One annotation in figure. |

### D. Appendix and formatting (≈1 day)

| # | Task | Chapter | Difficulty | Why it matters | Expected output |
|---|---|---|---|---|---|
| D1 | Build Appendix A from `10_Citation_Audit/A`, `E`, `H` | App A | Low | Documents the citation rebuild for examiner. | 8–12-page appendix. |
| D2 | Build Appendix B from `08_Code/financial_metrics_project_report.md` and `08_Code/requirements.txt` | App B | Low | Documents the financial pipeline. | 5–8-page appendix. |
| D3 | Build Appendix C from `08_Code/nlp_project_report.md` | App C | Low | Documents the NLP pipeline. | 5–8-page appendix. |
| D4 | Build Appendix D from `10_Citation_Audit/F` | App D | Low | Documents source-reliability classification. | 2–3-page appendix. |
| D5 | Build Appendix E from `10_Citation_Audit/D` | App E | Low | Documents Better-IR / SEC URL verification. | 2–3-page appendix. |
| D6 | Build Appendix F (Trustpilot data quality and cleaning) | App F | Low | Documents data cleaning. | 2–3-page appendix. |
| D7 | Build Appendix G — Glossary | App G | Low | Helps the examiner with mortgage-industry and AI/NLP terminology. | 2-page glossary. |
| D8 | Final QC pass against `10_Citation_Audit/H` | All | Low | Confirms one-citation-one-reference invariant. | 41-item checklist completed. |
| D9 | Front-matter (Title page, Declaration of authorship, Abstract, Acknowledgements, Table of Contents, List of Figures, List of Tables, List of Abbreviations) | front | Low | Required by university template. | Standard front-matter. |

**Total estimated effort:** roughly 7–11 working days from current state to submission-ready, allocated as ≈ 4 days for must-fixes (A1–A13), 2–3 days for should-fixes (B1–B9), 1–2 days for polish (C1–C5), 1 day for appendices and front-matter (D1–D9).

---

## 16. Final Submission-Readiness Assessment

### 16.1 Where the thesis stands today

The Better.com voice-AI-business-value thesis is, by the standards of an MSc dissertation, a *substantively strong* piece of empirical work. The case selection is genuinely revelatory; the empirical evidence is multidimensional and triangulated; the financial-trajectory and NLP results are correct against the underlying empirical reports; the seven-reason NPS-vs-Trustpilot caveat in §316 is a piece of genuinely best-practice methodological reasoning; the citation audit and APA 7 reference rebuild already in PR #2 has eliminated the most visible reference-system risks. **The thesis is not, however, currently submission-ready.** What it is short of is structural completion: four chapters (Design Pattern, Discussion, Limitations, Conclusion) are listed in the §49 thesis-structure preview but are not yet present in the docx; Chapter 2 has a missing 5th sub-strand and an unwritten conceptual-framework subsection; Chapter 3 has a duplicated table that needs to become the source-reliability table; Chapter 1 retains promotional residue that should be expunged.

### 16.2 Submission-readiness rating by chapter

| Chapter | Rating | Submission-readiness | Why |
|---|---|---|---|
| Front matter | C | Needs work | Standard template not yet inserted. |
| 1 Introduction | B− | Should-fix | Logic is sound; tone is promotional in §11–§35. |
| 2 Literature Review | B | Should-fix | Funnel is sound; missing 5th sub-strand and conceptual framework; Table 1 body missing. |
| 3 Methodology | B | Should-fix | Strong on philosophy/design; duplicate table; reproducibility paragraph missing; risks scattered. |
| 4 Case Study | B+ | Strong with edits | Substantively excellent; needs the three figures and the §8.4 compressions. |
| 5 Empirical Findings | A− | Submission-ready with minor edits | Numbers verified; interpretations defensible; six minor caveats and the Bonferroni footnote remain. |
| 6 Design Pattern | F | Must-write | Listed in §49 but not in docx. Outline in §13.1 of this report. |
| 7 Discussion | F | Must-write | Listed in §49 but not in docx. Outline in §13.2 of this report. |
| 8 Limitations | F | Must-write | Currently scattered; consolidate into one chapter per §13.3 of this report. |
| 9 Conclusion | F | Must-write | Listed in §49 but not in docx. Outline in §13.4 of this report. |
| References | A | Submission-ready | Rebuilt in PR #2; 7 outstanding judgement calls remain (`10_Citation_Audit/README.md`). |
| Appendices A–G | C | Should-package | All source files exist; only packaging is required. Plan in §10.5 of this report. |

### 16.3 Three-tier submission risk assessment

| Risk tier | Risks |
|---|---|
| **High (block submission if unaddressed)** | Missing Chapters 6–9; duplicated Methodology table; missing 5th lit-review sub-strand; missing Table 1 body. |
| **Medium (lower the grade if unaddressed)** | Promotional register in §11–§35 and §170–§192; missing Bonferroni footnote in §324; missing Rocket-comparability caveat in §306; uncited Hevner/Qualtrics; the seven outstanding citation-audit judgement calls. |
| **Low (cosmetic / polish)** | Chapter 4 length; Chapter 5 figure annotations; pragmatism paragraph length; voice-AI literature depth in §2.3. |

### 16.4 Critical-path timeline (recommended)

| Day | Tasks |
|---|---|
| **Day 1** | A1–A3 (table fixes); A4 (5th sub-strand); A5 (conceptual framework). |
| **Day 2** | A6 (Chapter 6 design pattern). |
| **Day 3** | A7 (Chapter 7 discussion). |
| **Day 4** | A8 (Chapter 8 limitations); A9 (Chapter 9 conclusion). |
| **Day 5** | A10 (sentence-level rewrites); A11 (citation-audit outstanding items); A12 (methodological-risks consolidation); A13 (Hevner / Qualtrics decision). |
| **Day 6** | B1–B5 (Chapter 4 figures and compressions). |
| **Day 7** | B6–B9 (Chapter 5 caveats and Chapter 1 search-and-replace pass). |
| **Day 8** | C1–C5 (polish). |
| **Day 9** | D1–D7 (appendices). |
| **Day 10** | D8 (final QC against `H_QC_Checklist.md`); D9 (front-matter). |
| **Day 11 (buffer)** | Read-through; supervisor pre-submission review. |

### 16.5 The defensible final claim

After all of the above, the thesis can defensibly state — in §9.5 (Theoretical contribution) and in the abstract — the following claim:

> The Better.com case demonstrates that a voice LLM agent integrated into a regulated U.S. mortgage-origination workflow can produce a financial-operational trajectory consistent with operational leverage (revenue growing 52% against expense growth of approximately 5% between 2024 and 2025; expense ratio falling from 2.89 to 2.01; revenue-per-employee rising 42.9%, although still below the 2021–2023 pre-period average) while remaining largely invisible to end customers (explicit AI mentions in independent customer discourse remain at approximately 1% before and after deployment). These observations are descriptively consistent with an AI-enabled-productivity reading mediated by four integration prerequisites — a process-aware operating platform, a coordination-layer agent scope, low-latency voice infrastructure, and an auditable human-AI collaboration model — but cannot be read as identifying a causal effect of voice AI deployment on firm performance.

This is the submission-ready claim the entire thesis should converge on. Every section of the body should support it; no section of the body should claim more than it.

### 16.6 What this report does not cover

This report deliberately does *not* attempt to perform the work itself. It is a *specification* of the work to be done. The user can either (a) implement the changes directly, using the section-by-section outlines and sentence-level rewrites in this report; or (b) ask a follow-up session to apply the changes file-by-file with the same rigor as PR #2.

---

*End of report.*
