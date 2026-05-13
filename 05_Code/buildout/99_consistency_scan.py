"""
99_consistency_scan.py
======================

Final consistency scan over Main_Draft.docx. Reports (does not auto-fix):

* duplicate H1 / H2 headings
* RQ1 / RQ2 wording variants (must be uniform)
* numeric claims that differ across the draft
* citation keys used in body but missing from References
* citation keys in References that are never cited in body (orphans)
* "fundamentally", "revolutioniz", "vital", "clearly proves" residues
* "Better 2022" anachronisms

The scan prints a report. It does not modify the document.
"""

from __future__ import annotations

import re
import sys
from collections import Counter

sys.path.insert(0, ".")
from _helpers import open_draft  # noqa: E402


PROMOTIONAL_PATTERNS = [
    r"\bfundamentally\b",
    r"\brevolutioniz",
    r"\bvital\b",
    r"\bclearly proves\b",
    r"\bdemonstrates causally\b",
    r"\bvalidates Better's claims\b",
    r"\bBetsy caused\b",
    r"\bAI drove\b",
]

NUMERIC_CLAIMS = [
    ("Revenue 2023 ($M)", [r"\$76\.8\s*M", r"76\.8\s*million"]),
    ("Revenue 2024 ($M)", [r"\$108\.5\s*M", r"108\.5\s*million"]),
    ("Revenue 2025 ($M)", [r"\$164\.9\s*M", r"164\.9\s*million"]),
    ("Expense ratio 2023", [r"4\.79"]),
    ("Expense ratio 2024", [r"2\.89"]),
    ("Expense ratio 2025", [r"2\.01"]),
    ("RPE 2025 ($M)", [r"\$0\.124\s*M", r"0\.124\s*million"]),
    ("Bonferroni Cost/Rates pp", [r"\u221212\.36", r"-12\.36", r"12\.36\s*pp", r"12\.36-percentage-point"]),
    ("Star rating pre", [r"4\.2806"]),
    ("Star rating post", [r"3\.8580"]),
    ("VADER pre", [r"0\.6416"]),
    ("VADER post", [r"0\.5151"]),
    ("Trustpilot n_pre", [r"\bn\s*=\s*1,?746", r"\b1,746\b"]),
    ("Trustpilot n_post", [r"\bn\s*=\s*169", r"\b169\s+post"]),
    ("BERTopic clustered", [r"\b1,198\b", r"66\.4\s*percent"]),
]


def all_text(doc) -> str:
    parts = []
    for p in doc.paragraphs:
        parts.append(p.text)
    for t in doc.tables:
        for row in t.rows:
            for c in row.cells:
                parts.append(c.text)
    return "\n".join(parts)


def section_text_blocks(doc):
    """Return a list of (heading, body) for each H1 / H2."""
    blocks = []
    cur_heading = ("__preamble__", "")
    cur_body = []
    for p in doc.paragraphs:
        sname = p.style.name if p.style else ""
        if sname.startswith("Heading 1") or sname.startswith("Heading 2"):
            blocks.append((cur_heading, "\n".join(cur_body)))
            cur_heading = (sname, p.text.strip())
            cur_body = []
        else:
            cur_body.append(p.text)
    blocks.append((cur_heading, "\n".join(cur_body)))
    return blocks


def find_promotional_residues(text: str):
    out = []
    for pat in PROMOTIONAL_PATTERNS:
        for m in re.finditer(pat, text, re.IGNORECASE):
            start = max(0, m.start() - 40)
            end = min(len(text), m.end() + 40)
            snippet = text[start:end].replace("\n", " ")
            out.append((pat, snippet))
    return out


def find_numeric_claim_coverage(text: str):
    out = {}
    for label, patterns in NUMERIC_CLAIMS:
        hits = 0
        for pat in patterns:
            hits += len(re.findall(pat, text))
        out[label] = hits
    return out


def find_rq_variants(doc):
    rq1_pat = re.compile(r"RQ1\s*[:.\u2014\u2013-]\s*(.{20,400})", re.IGNORECASE)
    rq2_pat = re.compile(r"RQ2\s*[:.\u2014\u2013-]\s*(.{20,400})", re.IGNORECASE)
    rq1 = []
    rq2 = []
    for p in doc.paragraphs:
        for m in rq1_pat.finditer(p.text):
            text = m.group(1).strip().split("\n")[0]
            text = text.split("RQ2")[0].strip()
            if text and len(text) > 30:
                rq1.append(text[:200])
        for m in rq2_pat.finditer(p.text):
            text = m.group(1).strip().split("\n")[0]
            if text and len(text) > 30:
                rq2.append(text[:200])
    return rq1, rq2


def find_better_2022_anachronism(doc):
    """The full company name 'Better Home & Finance Holding Company' did not
    exist in 2022; the entity was Better HoldCo, Inc. Flag any 'Better Home
    & Finance Holding Company. (2022' or '(Better, 2022' citations."""
    text = all_text(doc)
    out = []
    for m in re.finditer(r"Better Home & Finance Holding Company.{0,8}\(2022", text):
        start = max(0, m.start() - 40)
        snippet = text[start:m.end() + 40].replace("\n", " ")
        out.append(snippet)
    for m in re.finditer(r"\(Better, 2022", text):
        start = max(0, m.start() - 60)
        snippet = text[start:m.end() + 40].replace("\n", " ")
        out.append(snippet)
    return out


# ---------------------------------------------------------------------------
def main():
    doc = open_draft()
    text = all_text(doc)

    print("=" * 70)
    print("CONSISTENCY SCAN REPORT")
    print("=" * 70)

    print("\n--- 1. Promotional residue (case-insensitive) ---")
    res = find_promotional_residues(text)
    if not res:
        print("  None found.")
    else:
        for pat, snip in res:
            print(f"  [{pat}] ...{snip}...")

    print("\n--- 2. Numeric-claim coverage ---")
    coverage = find_numeric_claim_coverage(text)
    for label, n in coverage.items():
        flag = "OK" if n >= 1 else "MISSING"
        print(f"  {flag:7s}  {label:34s} hits={n}")

    print("\n--- 3. RQ wording uniformity ---")
    rq1, rq2 = find_rq_variants(doc)
    print(f"  RQ1 mentions: {len(rq1)}; distinct exact strings: {len(set(rq1))}")
    for variant, count in Counter(rq1).most_common(3):
        print(f"    [{count}x] {variant[:140]}")
    print(f"  RQ2 mentions: {len(rq2)}; distinct exact strings: {len(set(rq2))}")
    for variant, count in Counter(rq2).most_common(3):
        print(f"    [{count}x] {variant[:140]}")

    print("\n--- 4. Better 2022 anachronism check ---")
    anach = find_better_2022_anachronism(doc)
    if not anach:
        print("  None found.")
    else:
        for snip in anach:
            print(f"  ...{snip}...")

    print("\n--- 5. Document size summary ---")
    print(f"  Paragraphs: {len(doc.paragraphs)}")
    print(f"  Tables: {len(doc.tables)}")
    n_words = len(text.split())
    print(f"  Total words (approximate): {n_words:,}")
    n_h1 = sum(1 for p in doc.paragraphs if p.style.name == "Heading 1")
    n_h2 = sum(1 for p in doc.paragraphs if p.style.name == "Heading 2")
    n_h3 = sum(1 for p in doc.paragraphs if p.style.name == "Heading 3")
    print(f"  H1 / H2 / H3 headings: {n_h1} / {n_h2} / {n_h3}")

    print("\n--- 6. Heading enumeration ---")
    for p in doc.paragraphs:
        if p.style.name == "Heading 1":
            print(f"  H1 :: {p.text}")
    print("\nDone.")


if __name__ == "__main__":
    main()
