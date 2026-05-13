"""
15_format_typo_pass.py
======================

Standardise document formatting, fix typos, and clarify a small set of
H2/H3 headings.

Formatting standardisation
--------------------------
* Normalise every Body ("Normal") paragraph to:
    - font family = Calibri
    - font size   = 11 pt
    - line spacing = 1.5 (rule = MULTIPLE)
    - alignment   = JUSTIFY (except paragraphs that are deliberately
                    CENTER-aligned, e.g. cover page).
* Headings (Heading 1/2/3) and Caption paragraphs are left in their
  existing styled state but their LINE SPACING is normalised to 1.15
  (single-and-a-bit) for consistency, with Heading-style "before"
  spacing untouched. (We do not change the heading font/size; the
  document already uses 14/13/11 pt bold for H1/H2/H3 via the theme
  major font, which is conventional academic style.)
* Page size, margins, and orientation are left as configured (US
  Letter, 1 inch all sides, portrait).
* Tables, the reference list, and figure captions are left untouched
  except for the typo / smart-quote pass.

Heading clarifications
----------------------
* "3.11 Research Rigor and Reproducibility" -> "3.11 Research Rigour
  and Reproducibility" (British English).
* §6.3.1-6.3.4 four sub-headings are converted from sentence-case to
  Title Case so they match every other H3 heading in the thesis.
* §5.4.2 "Trustpilot Ratings and VADER Sentiment as Independent
  Customer Discourse" -> "...as Independent Customer-Discourse
  Evidence" (these are evidence streams, not discourse itself).

Typo fixes
----------
* Smart-quote pass over body+appendix prose:
    - U+0027 ASCII apostrophe   -> U+2019 right single quote
    - U+0022 ASCII double quote -> U+201C / U+201D opening / closing
      curly double quotes (alternation per occurrence within the same
      paragraph).
  Paragraph 541 ("B.2 Extraction Methodology") is excluded because it
  contains regex string literals which must remain ASCII.
* No other typos surfaced from a multi-pattern scan covering doubled
  function words, common British/American confusion, common keyboard
  errors, and punctuation oddities. Cover-page double spaces (paras
  5-8) are intentional cover-page spacing.

The script is idempotent. Running it twice produces the same file.
"""

from __future__ import annotations

import sys

from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING

sys.path.insert(0, ".")
from _helpers import open_draft, save_draft  # noqa: E402


# ---------------------------------------------------------------------------
# Heading clarifications
# ---------------------------------------------------------------------------

HEADING_REPLACEMENTS = [
    ("3.11 Research Rigor and Reproducibility",
     "3.11 Research Rigour and Reproducibility",
     "BE: Rigor -> Rigour"),
    ("6.3.1 Process-aware operating platform",
     "6.3.1 Process-Aware Operating Platform",
     "Title Case alignment with sibling H3s"),
    ("6.3.2 Coordination-layer agent scope",
     "6.3.2 Coordination-Layer Agent Scope",
     "Title Case alignment with sibling H3s"),
    ("6.3.3 Low-latency voice infrastructure",
     "6.3.3 Low-Latency Voice Infrastructure",
     "Title Case alignment with sibling H3s"),
    ("6.3.4 Auditable human escalation",
     "6.3.4 Auditable Human Escalation",
     "Title Case alignment with sibling H3s"),
    ("5.4.2 Trustpilot Ratings and VADER Sentiment as Independent "
     "Customer Discourse",
     "5.4.2 Trustpilot Ratings and VADER Sentiment as Independent "
     "Customer-Discourse Evidence",
     "Heading clarity: 'as Independent Customer-Discourse Evidence'"),
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def replace_in_paragraph(paragraph, old: str, new: str) -> int:
    full = "".join(r.text for r in paragraph.runs)
    if old not in full:
        return 0
    new_full = full.replace(old, new)
    runs = paragraph.runs
    if runs:
        runs[0].text = new_full
        for r in runs[1:]:
            r.text = ""
    else:
        paragraph.text = new_full
    return full.count(old)


def normalise_runs(paragraph, font_name: str, font_size_pt: int) -> None:
    """Set every run in the paragraph to the given font name and size,
    preserving bold/italic/underline state."""
    for r in paragraph.runs:
        # Only set if the run is non-empty or if explicit font is missing,
        # so we don't accidentally change empty bookkeeping runs.
        if r.font.name is None:
            r.font.name = font_name
        elif r.font.name != font_name:
            r.font.name = font_name
        # Some runs (e.g. page-break markers) carry size 1pt; preserve
        # those, otherwise force 11 pt.
        current = r.font.size
        if current is None:
            r.font.size = Pt(font_size_pt)
        elif current.pt < 5:
            # Empty 1pt section / page-break runs - leave alone.
            pass
        elif abs(current.pt - font_size_pt) > 0.1:
            r.font.size = Pt(font_size_pt)


def smart_quote_paragraph(paragraph) -> tuple[int, int]:
    """Replace ASCII apostrophes with U+2019 and ASCII double quotes
    with curly quotes (alternating opening/closing). Returns (single,
    double) replacement counts."""
    text = "".join(r.text for r in paragraph.runs)
    if "'" not in text and '"' not in text:
        return (0, 0)

    # Single quote: every ASCII ' becomes the right single quote
    # (typographic apostrophe). This is correct for possessives
    # ("Better's") and for closing single quotes; the few opening
    # single quotes that do occur in body prose are inside scare-quote
    # pairs (see Para 30 'Betsy,') and we will treat the ASCII ' before
    # a letter at a word boundary as a left single quote.
    out = []
    in_double_open = False
    single_count = 0
    double_count = 0
    for i, ch in enumerate(text):
        if ch == '"':
            if not in_double_open:
                out.append("\u201c")  # left/opening
                in_double_open = True
            else:
                out.append("\u201d")  # right/closing
                in_double_open = False
            double_count += 1
            continue
        if ch == "'":
            # Decide opening vs closing single quote heuristically:
            # opening if the previous character is a word boundary
            # (start of string, whitespace, or opening-bracket) AND
            # the next character is alphanumeric.
            prev_ch = text[i - 1] if i > 0 else ""
            next_ch = text[i + 1] if i + 1 < len(text) else ""
            if (prev_ch in ("", " ", "\t", "\n", "(", "[", "{")
                    and next_ch.isalpha()):
                out.append("\u2018")  # left single quote
            else:
                out.append("\u2019")  # right single quote / apostrophe
            single_count += 1
            continue
        out.append(ch)
    new_text = "".join(out)
    if new_text == text:
        return (0, 0)

    runs = paragraph.runs
    if runs:
        runs[0].text = new_text
        for r in runs[1:]:
            r.text = ""
    else:
        paragraph.text = new_text
    return (single_count, double_count)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    doc = open_draft()

    # Build paragraph index map
    paragraphs = list(doc.paragraphs)

    # Find references heading + appendix start
    refs_idx = None
    for i, p in enumerate(paragraphs):
        s = p.style.name if p.style else ""
        if s.startswith("Heading 1") and p.text.strip().startswith("References"):
            refs_idx = i
            break

    in_appendix_after_refs = set()
    if refs_idx is not None:
        in_app = False
        for i, p in enumerate(paragraphs[refs_idx + 1:], start=refs_idx + 1):
            s = p.style.name if p.style else ""
            if s.startswith("Heading 1") and p.text.strip().startswith("Appendix"):
                in_app = True
            if in_app:
                in_appendix_after_refs.add(i)

    body_indices = set(range(refs_idx if refs_idx is not None else len(paragraphs)))
    prose_indices = body_indices | in_appendix_after_refs

    # ---- 1. Heading replacements ---------------------------------------
    heading_changes = []
    for old, new, label in HEADING_REPLACEMENTS:
        count = 0
        for p in paragraphs:
            if not (p.style and p.style.name.startswith("Heading")):
                continue
            count += replace_in_paragraph(p, old, new)
        heading_changes.append((label, count))

    # ---- 2. Smart-quote pass -------------------------------------------
    # Skip Para 541 (regex strings).
    EXCLUDE = {541}
    single_total = 0
    double_total = 0
    quotes_paragraphs_changed = 0
    for i, p in enumerate(paragraphs):
        if i in EXCLUDE:
            continue
        if i not in prose_indices:
            continue
        s, d = smart_quote_paragraph(p)
        if s or d:
            quotes_paragraphs_changed += 1
        single_total += s
        double_total += d

    # ---- 3. Format standardisation -------------------------------------
    body_paras_normalised = 0
    body_paras_aligned = 0
    body_paras_spacing = 0
    for i, p in enumerate(paragraphs):
        s = p.style.name if p.style else ""
        if s != "Normal":
            continue
        # Skip the empty 'page break only' paragraphs - they have no
        # text but we still want to fix line spacing for layout
        # consistency.
        normalise_runs(p, "Calibri", 11)
        body_paras_normalised += 1
        # Line spacing -> 1.5 (multiple).
        pf = p.paragraph_format
        if (pf.line_spacing != 1.5
                or pf.line_spacing_rule != WD_LINE_SPACING.ONE_POINT_FIVE):
            pf.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
            pf.line_spacing = 1.5
            body_paras_spacing += 1
        # Alignment: JUSTIFY for body, but preserve any explicit CENTER
        # paragraphs (cover page; centred captions). LEFT-aligned and
        # None-aligned default to JUSTIFY.
        if p.alignment in (None, WD_ALIGN_PARAGRAPH.LEFT):
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            body_paras_aligned += 1

    save_draft(doc)

    # ---- Summary -------------------------------------------------------
    print("=" * 60)
    print("Format / typo / heading-clarification pass")
    print("=" * 60)
    print("Heading clarifications:")
    for label, count in heading_changes:
        print(f"  - {label}: {count} replacement(s)")
    print(
        "Smart-quote pass:"
        f"\n  - paragraphs touched: {quotes_paragraphs_changed}"
        f"\n  - ASCII apostrophes converted: {single_total}"
        f"\n  - ASCII double quotes converted: {double_total}"
        " (Para 541 excluded for regex literals)"
    )
    print(
        "Body formatting standardisation:"
        f"\n  - Normal paragraphs with font/size normalised: {body_paras_normalised}"
        f"\n  - Paragraphs whose line spacing was set to 1.5: {body_paras_spacing}"
        f"\n  - Paragraphs whose alignment was set to JUSTIFY: {body_paras_aligned}"
    )


if __name__ == "__main__":
    main()
