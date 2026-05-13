"""
09f_register_pass3.py
=====================

Final register pass: tighten the small set of remaining promotional or
quasi-causal phrasings flagged by the consistency scan and the supervisor's
critical-action register.

Targets:
* "textbook descriptive signature of operational leverage" -> "an empirical
  pattern consistent with operational leverage" (two occurrences in §5.3.x).
* "demonstrates that Better's operating model is designed around partial
  human escalation" -> "indicates that ..." (case-study chapter).
* British/American English standardisation: convert American spellings of
  the few mixed terms ("modeling", "behavior", "labor", "organization",
  "operationalize", "synthesize", "summarize", "analyze") to British
  spellings, while keeping verbatim quotations from external sources
  unchanged. The spellings inside SEC filings (proper-noun titles such as
  'Bureau of Labor Statistics', 'U.S. Department of Labor', 'OPERATIONS
  REPORT', etc.) are protected.
"""

from __future__ import annotations

import re
import sys

sys.path.insert(0, ".")
from _helpers import open_draft, save_draft  # noqa: E402


def replace_in_paragraph(p, old: str, new: str) -> int:
    if old not in p.text:
        return 0
    n = p.text.count(old)
    changed = False
    for r in p.runs:
        if old in r.text:
            r.text = r.text.replace(old, new)
            changed = True
    if changed and old not in p.text:
        return n
    new_full = p.text.replace(old, new)
    # Rebuild
    if p.runs:
        r0 = p.runs[0]
        font_name = r0.font.name
        font_size = r0.font.size
        bold = r0.bold
        italic = r0.italic
    else:
        font_name = font_size = bold = italic = None
    for r in list(p.runs):
        r._element.getparent().remove(r._element)
    nr = p.add_run(new_full)
    if font_name:
        nr.font.name = font_name
    if font_size:
        nr.font.size = font_size
    if bold is not None:
        nr.bold = bold
    if italic is not None:
        nr.italic = italic
    return n


# ---------------------------------------------------------------------------
# Phrase-level fixes
# ---------------------------------------------------------------------------

PHRASE_REPLACEMENTS = [
    ("textbook descriptive signature of operational leverage",
     "an empirical pattern consistent with operational leverage"),
    ("textbook descriptive signature",
     "an empirical pattern consistent with operational leverage"),
    ("demonstrates that Better's operating model is designed around partial human escalation",
     "indicates that Better's operating model is designed around partial human escalation"),
    ("demonstrates that Better\u2019s operating model is designed around partial human escalation",
     "indicates that Better\u2019s operating model is designed around partial human escalation"),
]


# ---------------------------------------------------------------------------
# British / American English normalisation
# ---------------------------------------------------------------------------

# We treat the following American spellings as the variant to convert. The
# pairs are chosen so that the resulting British forms do not introduce new
# inconsistencies (e.g. we do *not* touch -ize verbs that are universally
# accepted in British academic English, such as 'organize').
#
# We protect three contexts:
#   1. References / bibliography paragraphs (style 'Normal' but starting with
#      an author name and year).
#   2. Quoted strings (anything inside double quotes).
#   3. Filing / institutional proper nouns (whitelist).

US_TO_UK = [
    (r"\bmodeling\b", "modelling"),
    (r"\bModeling\b", "Modelling"),
    (r"\bmodeled\b", "modelled"),
    (r"\bModeled\b", "Modelled"),
    (r"\bbehavior\b", "behaviour"),
    (r"\bBehavior\b", "Behaviour"),
    (r"\bbehaviors\b", "behaviours"),
    (r"\bbehavioral\b", "behavioural"),
    (r"\bBehavioral\b", "Behavioural"),
    (r"\blabor\b", "labour"),
    (r"\bLabor\b", "Labour"),
    (r"\blabor productivity\b", "labour productivity"),
    (r"\borganization\b", "organisation"),
    (r"\bOrganization\b", "Organisation"),
    (r"\borganizations\b", "organisations"),
    (r"\borganizational\b", "organisational"),
    (r"\bOrganizational\b", "Organisational"),
    (r"\bsummarize\b", "summarise"),
    (r"\bsummarized\b", "summarised"),
    (r"\bsummarizes\b", "summarises"),
    (r"\bsynthesize\b", "synthesise"),
    (r"\bsynthesized\b", "synthesised"),
    (r"\bsynthesizes\b", "synthesises"),
    (r"\banalyze\b", "analyse"),
    (r"\banalyzed\b", "analysed"),
    (r"\banalyzes\b", "analyses"),
    (r"\bcharacterize\b", "characterise"),
    (r"\bcharacterized\b", "characterised"),
    (r"\bcharacterizes\b", "characterises"),
    (r"\bgeneralize\b", "generalise"),
    (r"\bgeneralizable\b", "generalisable"),
    (r"\bgeneralization\b", "generalisation"),
    (r"\boperationalize\b", "operationalise"),
    (r"\boperationalized\b", "operationalised"),
    (r"\boperationalization\b", "operationalisation"),
    (r"\bemphasize\b", "emphasise"),
    (r"\bemphasized\b", "emphasised"),
    (r"\bemphasizes\b", "emphasises"),
    (r"\bcategorize\b", "categorise"),
    (r"\bcategorized\b", "categorised"),
    (r"\bcategorizes\b", "categorises"),
    (r"\brecognize\b", "recognise"),
    (r"\brecognized\b", "recognised"),
    (r"\brecognizes\b", "recognises"),
    (r"\butilize\b", "utilise"),
    (r"\butilized\b", "utilised"),
    (r"\butilizes\b", "utilises"),
    (r"\bpersonalize\b", "personalise"),
    (r"\bpersonalized\b", "personalised"),
    (r"\bcustomize\b", "customise"),
    (r"\bcustomized\b", "customised"),
    (r"\bcustomization\b", "customisation"),
    (r"\bspecialize\b", "specialise"),
    (r"\bspecialized\b", "specialised"),
    (r"\bspecializes\b", "specialises"),
    (r"\bdigitization\b", "digitisation"),
    (r"\bdigitize\b", "digitise"),
    (r"\bdigitized\b", "digitised"),
    (r"\bcenter\b", "centre"),
    (r"\bCenter\b", "Centre"),
    (r"\bcenters\b", "centres"),
    (r"\bcentered\b", "centred"),
    (r"\bcatalog\b", "catalogue"),
    (r"\bcatalogs\b", "catalogues"),
    (r"\bdialog\b", "dialogue"),
    (r"\bdialogs\b", "dialogues"),
]

# Phrases that should remain American because they are proper nouns.
PROTECTED_PHRASES = [
    "Bureau of Labor Statistics",
    "U.S. Department of Labor",
    "Department of Labor",
    "Center for ",
    "Behavioral Decision Making",
    "Modeling and Computer Simulation",
    "Behavior Analyst",
    "Customer Behavior",  # only if it appears as a proper title
    "Business Information Systems",  # safe but not US/UK divergent
]


def is_reference_paragraph(text: str) -> bool:
    """Heuristic: paragraphs in the References block typically start with a
    surname and year, e.g. 'Smith, J. (2024). Title …'. We do not modify
    these because reference titles must remain verbatim."""
    return bool(
        re.match(r"^\s*[A-Z][\w\u2019'-]+(?:,\s*[A-Z]\.|,\s*[A-Z][\w'-]+)?(?:,\s*[A-Z]\.|\s*&|\s+et al\.).*\(\d{4}", text)
        or re.match(r"^\s*[A-Z][\w\u2019'-]+,\s*[A-Z]\..*\(\d{4}", text)
        or re.match(r"^\s*Better\s*\.com.*\(.*\)\.", text)
    )


def normalise_us_to_uk(p) -> int:
    text = p.text
    if not text.strip():
        return 0
    if is_reference_paragraph(text):
        return 0
    # Don't modify quoted strings — replace each protected segment with a
    # placeholder, run replacements, then restore.
    placeholders = []

    def _stash(match):
        placeholders.append(match.group(0))
        return f"\u0001{len(placeholders) - 1}\u0001"

    # Stash double-quoted strings.
    masked = re.sub(r"\".*?\"", _stash, text)
    # Stash protected proper nouns.
    for ph in PROTECTED_PHRASES:
        if ph in masked:
            placeholders.append(ph)
            masked = masked.replace(ph, f"\u0001{len(placeholders) - 1}\u0001")

    new_text = masked
    for pat, repl in US_TO_UK:
        new_text = re.sub(pat, repl, new_text)

    if new_text == masked:
        return 0

    # Restore placeholders.
    def _unstash(match):
        idx = int(match.group(1))
        return placeholders[idx]

    new_text = re.sub(r"\u0001(\d+)\u0001", _unstash, new_text)
    if new_text == text:
        return 0
    # Count how many tokens changed; we use a heuristic of word-level diff.
    n = sum(1 for a, b in zip(text.split(), new_text.split()) if a != b)
    # Rebuild paragraph.
    if p.runs:
        r0 = p.runs[0]
        font_name = r0.font.name
        font_size = r0.font.size
        bold = r0.bold
        italic = r0.italic
    else:
        font_name = font_size = bold = italic = None
    for r in list(p.runs):
        r._element.getparent().remove(r._element)
    nr = p.add_run(new_text)
    if font_name:
        nr.font.name = font_name
    if font_size:
        nr.font.size = font_size
    if bold is not None:
        nr.bold = bold
    if italic is not None:
        nr.italic = italic
    return n


def main():
    doc = open_draft()

    # Phrase-level
    n_phrase = 0
    for p in doc.paragraphs:
        for old, new in PHRASE_REPLACEMENTS:
            n_phrase += replace_in_paragraph(p, old, new)
    print(f"[09f] phrase fixes: {n_phrase}")

    # British/American
    n_words = 0
    for p in doc.paragraphs:
        n_words += normalise_us_to_uk(p)
    # Walk tables too (cells contain paragraphs).
    for t in doc.tables:
        for row in t.rows:
            for c in row.cells:
                for p in c.paragraphs:
                    n_words += normalise_us_to_uk(p)
    print(f"[09f] US->UK word-level changes: {n_words}")

    save_draft(doc)
    print("Saved.")


if __name__ == "__main__":
    main()
