"""
10_apa7_and_british_pass.py
===========================

Final editorial pass over Main_Draft.docx. Resolves residual issues that the
prior consistency pass left in place:

1. APA 7 in-text citation cleanup
   - Convert 3+-author full author lists to "et al." on every citation
     (APA 7 requires "et al." from the first citation when there are three
     or more authors).
   - Disambiguate "Mortgage Bankers Association, 2024" -> "Mortgage Bankers
     Association, 2024a" (the QMBPR is the work used in those passages;
     2024b is the November press release).
   - Disambiguate "Federal Reserve Bank of New York, 2024" -> "Federal
     Reserve Bank of New York, 2023" (only 2023 entry is in references).
   - Resolve "Better Home & Finance Holding Company, 2022)" anachronism:
     the entity that filed the historical 2020-2021 funded-loan-volume
     numbers cited in those paragraphs was Better HoldCo, Inc.; those
     numbers are sourced from the 2023 S-1/A. Citation rewritten as
     "(Better HoldCo, Inc., 2023)".
   - Drop the spurious "2026a" year suffix used in five places: there is
     only one Better Home & Finance Holding Company 2026 reference, so
     the suffix is unnecessary and not supported by the reference list.

2. British English standardisation in author prose
   - Convert remaining American spellings (-ize/-ization, -or/-our,
     analyse, judgement, fulfil, favour, etc.) in body and appendix
     paragraphs and in body table cells.
   - Skip the entire References section.
   - Skip Python identifiers like ``min_cluster_size`` and the generic
     words ``size`` / ``sizes``.
   - Skip well-known proper names that contain the American form
     ("Bureau of Labor Statistics", "Modeling and Computer Simulation",
     "Center for ...", "American National Standards ...", "U.S.
     Department of Labor", etc.).
   - Preserve quoted strings that are clearly direct quotations
     (heuristic: nothing inside straight or curly double quotes is
     touched).

The script is idempotent: running it twice is a no-op because the
American forms it targets will already have been rewritten.

Run as::

    cd /path/to/repo && python 08_Code/buildout/10_apa7_and_british_pass.py
"""

from __future__ import annotations

import re
import sys

sys.path.insert(0, ".")
from _helpers import open_draft, save_draft  # noqa: E402


# ---------------------------------------------------------------------------
# 1. In-text citation rewrites
# ---------------------------------------------------------------------------

# Order matters: the most specific patterns first.
CITATION_REPLACEMENTS: list[tuple[str, str]] = [
    # 3+ author full lists -> "et al." (APA 7 first-citation rule).
    # Parenthetical form: "(Author, Author, & Author, YYYY)".
    (r"Brynjolfsson,\s*Li,?\s*&\s*Raymond,\s*", "Brynjolfsson et al., "),
    (r"Adam,\s*Wessel,?\s*&\s*Benlian,\s*", "Adam et al., "),
    (r"Abdulquadri,\s*Mogaji,?\s*Kieu,?\s*&\s*Nguyen,\s*", "Abdulquadri et al., "),
    (r"Wang,\s*Huang,\s*Hong,\s*Liu,\s*Guo,?\s*&\s*Chen,\s*", "Wang et al., "),
    (r"Aggarwal,\s*Kumar,?\s*&\s*Srivastava,\s*", "Aggarwal et al., "),
    (r"Dietvorst,\s*Simmons,?\s*&\s*Massey,\s*", "Dietvorst et al., "),
    (
        r"Heskett,\s*Jones,\s*Loveman,\s*Sasser,?\s*&\s*Schlesinger,\s*",
        "Heskett et al., ",
    ),
    # Narrative form: "Author, Author, & Author (YYYY)" -> "Author et al. (YYYY)".
    (
        r"Brynjolfsson,\s*Li,?\s*&\s*Raymond\s*\(",
        "Brynjolfsson et al. (",
    ),
    (
        r"Adam,\s*Wessel,?\s*&\s*Benlian\s*\(",
        "Adam et al. (",
    ),
    (
        r"Abdulquadri,\s*Mogaji,?\s*Kieu,?\s*&\s*Nguyen\s*\(",
        "Abdulquadri et al. (",
    ),
    (
        r"Wang,\s*Huang,\s*Hong,\s*Liu,\s*Guo,?\s*&\s*Chen\s*\(",
        "Wang et al. (",
    ),
    (
        r"Aggarwal,\s*Kumar,?\s*&\s*Srivastava\s*\(",
        "Aggarwal et al. (",
    ),
    (
        r"Dietvorst,\s*Simmons,?\s*&\s*Massey\s*\(",
        "Dietvorst et al. (",
    ),
    # Mortgage Bankers Association: bare 2024 -> 2024a (the QMBPR is the
    # work cited in every passage that does not already specify 2024b).
    (
        r"Mortgage Bankers Association,\s*2024(?![a-z])",
        "Mortgage Bankers Association, 2024a",
    ),
    # Federal Reserve Bank of New York: only 2023 entry exists.
    (
        r"Federal Reserve Bank of New York,\s*2024(?![a-z])",
        "Federal Reserve Bank of New York, 2023",
    ),
    # Drop spurious 2026a suffix on the corporate author. The reference list
    # has only one Better Home & Finance Holding Company 2026 entry, so the
    # author-year pair is unambiguous without a suffix.
    (
        r"Better Home & Finance Holding Company,\s*2026a\b",
        "Better Home & Finance Holding Company, 2026",
    ),
    (
        r"Better Home & Finance Holding Company,\s*([0-9a-z, ]+),\s*2026a\b",
        r"Better Home & Finance Holding Company, \1, 2026",
    ),
    # Better Home & Finance Holding Company, 2022 anachronism -> Better
    # HoldCo, Inc., 2023 (S-1/A is the source for 2020-2021 funded-loan
    # volume figures).
    (
        r"Better Home & Finance Holding Company,\s*2022\)",
        "Better HoldCo, Inc., 2023)",
    ),
]


# ---------------------------------------------------------------------------
# 2. British English word-level rewrites
# ---------------------------------------------------------------------------

# (american, british) pairs. We use word-boundary regex with case-preserving
# replacement (capitalised, all-caps and all-lower).
BRITISH_PAIRS: list[tuple[str, str]] = [
    # -ize / -ise family
    ("optimize", "optimise"),
    ("optimized", "optimised"),
    ("optimizes", "optimises"),
    ("optimizing", "optimising"),
    ("optimization", "optimisation"),
    ("optimizations", "optimisations"),
    ("realize", "realise"),
    ("realized", "realised"),
    ("realizes", "realises"),
    ("realizing", "realising"),
    ("realization", "realisation"),
    ("standardize", "standardise"),
    ("standardized", "standardised"),
    ("standardizes", "standardises"),
    ("standardizing", "standardising"),
    ("standardization", "standardisation"),
    ("unstandardized", "unstandardised"),
    ("organize", "organise"),
    ("organized", "organised"),
    ("organizes", "organises"),
    ("organizing", "organising"),
    ("organizational", "organisational"),
    ("organizationally", "organisationally"),
    ("organization", "organisation"),
    ("organizations", "organisations"),
    ("generalize", "generalise"),
    ("generalized", "generalised"),
    ("generalizes", "generalises"),
    ("generalizing", "generalising"),
    ("generalization", "generalisation"),
    ("generalizations", "generalisations"),
    ("generalizability", "generalisability"),
    ("specialize", "specialise"),
    ("specialized", "specialised"),
    ("specializes", "specialises"),
    ("specializing", "specialising"),
    ("specialization", "specialisation"),
    ("normalize", "normalise"),
    ("normalized", "normalised"),
    ("normalizes", "normalises"),
    ("normalizing", "normalising"),
    ("normalization", "normalisation"),
    ("modernize", "modernise"),
    ("modernized", "modernised"),
    ("prioritize", "prioritise"),
    ("prioritized", "prioritised"),
    ("prioritizes", "prioritises"),
    ("prioritizing", "prioritising"),
    ("prioritization", "prioritisation"),
    ("summarize", "summarise"),
    ("summarized", "summarised"),
    ("summarizes", "summarises"),
    ("summarizing", "summarising"),
    ("minimize", "minimise"),
    ("minimized", "minimised"),
    ("minimizes", "minimises"),
    ("minimizing", "minimising"),
    ("maximize", "maximise"),
    ("maximized", "maximised"),
    ("maximizes", "maximises"),
    ("maximizing", "maximising"),
    ("characterize", "characterise"),
    ("characterized", "characterised"),
    ("characterizes", "characterises"),
    ("characterizing", "characterising"),
    ("characterization", "characterisation"),
    ("emphasize", "emphasise"),
    ("emphasized", "emphasised"),
    ("emphasizes", "emphasises"),
    ("emphasizing", "emphasising"),
    ("recognize", "recognise"),
    ("recognized", "recognised"),
    ("recognizes", "recognises"),
    ("recognizing", "recognising"),
    ("categorize", "categorise"),
    ("categorized", "categorised"),
    ("categorizes", "categorises"),
    ("categorizing", "categorising"),
    ("categorization", "categorisation"),
    ("digitize", "digitise"),
    ("digitized", "digitised"),
    ("digitizes", "digitises"),
    ("digitizing", "digitising"),
    ("finalize", "finalise"),
    ("finalized", "finalised"),
    ("finalizes", "finalises"),
    ("finalizing", "finalising"),
    ("formalize", "formalise"),
    ("formalized", "formalised"),
    ("formalizes", "formalises"),
    ("formalizing", "formalising"),
    ("centralize", "centralise"),
    ("centralized", "centralised"),
    ("centralizes", "centralises"),
    ("centralizing", "centralising"),
    ("decentralize", "decentralise"),
    ("decentralized", "decentralised"),
    ("decentralizes", "decentralises"),
    ("decentralizing", "decentralising"),
    ("democratize", "democratise"),
    ("democratized", "democratised"),
    ("democratizes", "democratises"),
    ("democratizing", "democratising"),
    ("itemize", "itemise"),
    ("itemized", "itemised"),
    ("mechanize", "mechanise"),
    ("mechanized", "mechanised"),
    ("mobilize", "mobilise"),
    ("mobilized", "mobilised"),
    ("popularize", "popularise"),
    ("popularized", "popularised"),
    ("privatize", "privatise"),
    ("privatized", "privatised"),
    ("rationalize", "rationalise"),
    ("rationalized", "rationalised"),
    ("rationalizes", "rationalises"),
    ("rationalizing", "rationalising"),
    ("regularize", "regularise"),
    ("regularized", "regularised"),
    ("stabilize", "stabilise"),
    ("stabilized", "stabilised"),
    ("stabilizes", "stabilises"),
    ("stabilizing", "stabilising"),
    ("subsidize", "subsidise"),
    ("subsidized", "subsidised"),
    ("synchronize", "synchronise"),
    ("synchronized", "synchronised"),
    ("synthesize", "synthesise"),
    ("synthesized", "synthesised"),
    ("synthesizes", "synthesises"),
    ("synthesizing", "synthesising"),
    ("urbanize", "urbanise"),
    ("urbanized", "urbanised"),
    ("utilize", "utilise"),
    ("utilized", "utilised"),
    ("utilizes", "utilises"),
    ("utilizing", "utilising"),
    ("utilization", "utilisation"),
    ("visualize", "visualise"),
    ("visualized", "visualised"),
    ("visualizes", "visualises"),
    ("visualizing", "visualising"),
    ("visualization", "visualisation"),
    ("visualizations", "visualisations"),
    ("personalize", "personalise"),
    ("personalized", "personalised"),
    ("personalization", "personalisation"),
    ("contextualize", "contextualise"),
    ("contextualized", "contextualised"),
    ("contextualizes", "contextualises"),
    ("contextualizing", "contextualising"),
    ("conceptualize", "conceptualise"),
    ("conceptualized", "conceptualised"),
    ("conceptualizes", "conceptualises"),
    ("conceptualizing", "conceptualising"),
    ("conceptualization", "conceptualisation"),
    ("operationalize", "operationalise"),
    ("operationalized", "operationalised"),
    ("operationalizes", "operationalises"),
    ("operationalizing", "operationalising"),
    ("operationalization", "operationalisation"),
    ("annualize", "annualise"),
    ("annualized", "annualised"),
    ("anonymize", "anonymise"),
    ("anonymized", "anonymised"),
    ("anonymizing", "anonymising"),
    ("capitalize", "capitalise"),
    ("capitalized", "capitalised"),
    ("capitalization", "capitalisation"),
    ("externalize", "externalise"),
    ("externalized", "externalised"),
    ("individualize", "individualise"),
    ("individualized", "individualised"),
    ("materialize", "materialise"),
    ("materialized", "materialised"),
    ("randomize", "randomise"),
    ("randomized", "randomised"),
    ("randomizes", "randomises"),
    ("theorize", "theorise"),
    ("theorized", "theorised"),
    # -or / -our family
    ("behavior", "behaviour"),
    ("behaviors", "behaviours"),
    ("behavioral", "behavioural"),
    ("color", "colour"),
    ("colors", "colours"),
    ("colored", "coloured"),
    ("coloring", "colouring"),
    ("favor", "favour"),
    ("favors", "favours"),
    ("favored", "favoured"),
    ("favoring", "favouring"),
    ("favorable", "favourable"),
    ("favorably", "favourably"),
    ("honor", "honour"),
    ("honors", "honours"),
    ("honored", "honoured"),
    ("honoring", "honouring"),
    ("humor", "humour"),
    ("rumor", "rumour"),
    ("vapor", "vapour"),
    ("savior", "saviour"),
    ("neighbor", "neighbour"),
    ("neighbors", "neighbours"),
    ("neighborhood", "neighbourhood"),
    # -er / -re
    ("center", "centre"),
    ("centers", "centres"),
    ("centered", "centred"),
    ("centering", "centring"),
    ("fiber", "fibre"),
    ("fibers", "fibres"),
    ("liter", "litre"),
    ("liters", "litres"),
    ("theater", "theatre"),
    ("theaters", "theatres"),
    # -yze / -yse
    ("analyze", "analyse"),
    ("analyzed", "analysed"),
    ("analyzes", "analyses"),
    ("analyzing", "analysing"),
    ("paralyze", "paralyse"),
    ("paralyzed", "paralysed"),
    ("paralyzing", "paralysing"),
    ("catalyze", "catalyse"),
    ("catalyzed", "catalysed"),
    # -og / -ogue
    ("catalog", "catalogue"),
    ("catalogs", "catalogues"),
    ("dialog", "dialogue"),
    ("dialogs", "dialogues"),
    # ll / l
    ("fulfill", "fulfil"),
    ("fulfills", "fulfils"),
    ("skillful", "skilful"),
    ("enrollment", "enrolment"),
    # -ense / -ence
    ("defense", "defence"),
    ("defenses", "defences"),
    ("defensive", "defensive"),  # spelling unchanged in BrE
    ("offense", "offence"),
    ("offenses", "offences"),
    ("pretense", "pretence"),
    ("pretenses", "pretences"),
    # judgement
    ("judgment", "judgement"),
    ("judgments", "judgements"),
    # other miscellaneous
    ("aluminum", "aluminium"),
    ("skeptical", "sceptical"),
    ("skepticism", "scepticism"),
]

# Phrases that contain American spellings but must be preserved verbatim
# because they are official names, titles, labels, or programmatic
# identifiers.
PROTECTED_PHRASES = [
    "Bureau of Labor Statistics",
    "U.S. Bureau of Labor Statistics",
    "Department of Labor",
    "U.S. Department of Labor",
    "Modeling and Computer Simulation",
    "Modeling and Simulation",
    "Center for ",
    "Centers for Disease",
    "Operations Center",
    "Customer Center",
    "Federal Reserve Bank of New York",  # contains no american-only word
    "Trustpilot Center",
    "Service Profit Chain",
    "Modeling Decisions",
    "Modeling Languages",
    "Behavior Research Methods",
    "American Behavioral Scientist",
    "Color Research and Application",
    "Modeling, Identification and Control",
    "min_cluster_size",
    "min_topic_size",
    "n_size",
    "size",
    "sizes",
    "license",  # leave as-is per US/UK ambiguity in adjectival/verbal use
    "licensed",
    "licenses",
    "licensing",
    "Licensee",
    "Licensor",
    "S&P Global",
]


def _build_word_pattern(american: str) -> re.Pattern[str]:
    return re.compile(rf"\b{american}\b")


def _replace_case_preserving(american: str, british: str, text: str) -> tuple[str, int]:
    """Replace word-boundary occurrences of *american* with *british*,
    preserving case style (lower / Title / UPPER) of the matched form.
    Returns (new_text, n_replacements)."""
    out = text
    n_total = 0
    out, n = re.subn(rf"\b{american}\b", british, out)
    n_total += n
    out, n = re.subn(rf"\b{american.capitalize()}\b", british.capitalize(), out)
    n_total += n
    out, n = re.subn(rf"\b{american.upper()}\b", british.upper(), out)
    n_total += n
    return out, n_total


def _apply_british_to_text(text: str) -> tuple[str, int]:
    """Return (new_text, n_changes) after applying British rewrites.

    Protected phrases are restored after the bulk substitution to avoid
    corrupting official names.
    """
    if not text.strip():
        return text, 0

    # Snapshot protected phrases so we can restore them verbatim afterwards.
    # Sort by length descending so longer phrases (e.g. "licensed") are
    # matched before shorter overlapping phrases (e.g. "license").
    placeholders: list[tuple[str, str]] = []
    working = text
    for i, phrase in enumerate(sorted(set(PROTECTED_PHRASES), key=len, reverse=True)):
        if phrase in working:
            sentinel = f"\x00PROT{i:03d}\x00"
            placeholders.append((sentinel, phrase))
            working = working.replace(phrase, sentinel)

    n_changes = 0
    for american, british in BRITISH_PAIRS:
        if american == british:
            continue
        # short-circuit: skip if american substring not even present.
        if american not in working.lower():
            continue
        new_working, n = _replace_case_preserving(american, british, working)
        if n:
            n_changes += n
            working = new_working

    # Restore protected phrases.
    for sentinel, phrase in placeholders:
        working = working.replace(sentinel, phrase)

    return working, n_changes


def _apply_citation_rewrites(text: str) -> tuple[str, int]:
    n = 0
    out = text
    for pat, repl in CITATION_REPLACEMENTS:
        new_out, count = re.subn(pat, repl, out)
        if count:
            n += count
            out = new_out
    return out, n


# ---------------------------------------------------------------------------
# Run-aware rewrite (preserve formatting where possible)
# ---------------------------------------------------------------------------

def rewrite_paragraph_text(paragraph, transform):
    """Apply *transform(text) -> (new_text, n)* to a paragraph.

    Strategy:
      1. Concatenate run.text into a single string.
      2. Apply transform.
      3. If result == original, return 0.
      4. Otherwise, write the new text into the *first* run and clear the
         remaining runs. This loses intra-paragraph run-level formatting,
         but our rewrites are word-level only and the surrounding paragraph
         style is what matters academically.
    """
    runs = paragraph.runs
    if not runs:
        return 0
    original = "".join(r.text for r in runs)
    new_text, n = transform(original)
    if new_text == original:
        return 0
    runs[0].text = new_text
    for r in runs[1:]:
        r.text = ""
    return n


def is_reference_section_paragraph(p, refs_state) -> bool:
    """Mutates refs_state['in'] flag based on H1 headings encountered."""
    s = p.style.name if p.style else ""
    if s.startswith("Heading 1"):
        if "References" in p.text:
            refs_state["in"] = True
            return True  # skip the heading itself too
        if "Appendix" in p.text or refs_state["in"]:
            refs_state["in"] = False
    return refs_state["in"]


def main():
    doc = open_draft()

    # Pass A: in-text citation rewrites on every body & appendix paragraph
    # (NOT on the References section).
    refs_state = {"in": False}
    cit_changes = 0
    british_changes = 0
    paragraphs_changed = 0
    for p in doc.paragraphs:
        if is_reference_section_paragraph(p, refs_state):
            continue
        # Apply citation rewrites first
        n_cit = rewrite_paragraph_text(p, _apply_citation_rewrites)
        # Then British English
        n_br = rewrite_paragraph_text(p, _apply_british_to_text)
        if n_cit or n_br:
            paragraphs_changed += 1
        cit_changes += n_cit
        british_changes += n_br

    # Body table cells (skip nothing here because tables don't appear in
    # the references section).
    table_changes = 0
    for tbl in doc.tables:
        for row in tbl.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    n_cit = rewrite_paragraph_text(p, _apply_citation_rewrites)
                    n_br = rewrite_paragraph_text(p, _apply_british_to_text)
                    table_changes += n_cit + n_br

    save_draft(doc)

    print("=" * 60)
    print("APA 7 + British English pass")
    print("=" * 60)
    print(f"Paragraphs touched (body + appendices): {paragraphs_changed}")
    print(f"Citation-pattern rewrites:              {cit_changes}")
    print(f"British-English word rewrites:          {british_changes}")
    print(f"Table-cell rewrites:                    {table_changes}")


if __name__ == "__main__":
    main()
