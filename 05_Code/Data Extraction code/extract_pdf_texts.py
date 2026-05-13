"""
Full PDF Text Extractor
=======================
Extracts COMPLETE text from all annual report PDFs using pdfplumber.
Outputs one .txt file per PDF into 08_Code/extracted_text/
"""

import os
import pdfplumber

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "03_Case_Study_Data")
OUT_DIR  = os.path.join(BASE_DIR, "08_Code", "extracted_text")
os.makedirs(OUT_DIR, exist_ok=True)

# Map: (output_stem, pdf_path)
REPORTS = [
    # Better
    ("Better_Annual_2023", os.path.join(DATA_DIR, "Better", "Annual Reports", "2023.pdf")),
    ("Better_Annual_2024", os.path.join(DATA_DIR, "Better", "Annual Reports", "2024.pdf")),
    ("Better_Annual_2025", os.path.join(DATA_DIR, "Better", "Annual Reports", "2025.pdf")),
    ("Better_S1",         os.path.join(DATA_DIR, "Better", "Annual Reports", "S1.pdf")),
    # Rocket
    ("Rocket_Annual_2020", os.path.join(DATA_DIR, "Rocket Mortgage", "Annual Reports", "2020.pdf")),
    ("Rocket_Annual_2021", os.path.join(DATA_DIR, "Rocket Mortgage", "Annual Reports", "2021.pdf")),
    ("Rocket_Annual_2022", os.path.join(DATA_DIR, "Rocket Mortgage", "Annual Reports", "2022.pdf")),
    ("Rocket_Annual_2023", os.path.join(DATA_DIR, "Rocket Mortgage", "Annual Reports", "2023.pdf")),
    ("Rocket_Annual_2024", os.path.join(DATA_DIR, "Rocket Mortgage", "Annual Reports", "2024.pdf")),
    ("Rocket_Annual_2025", os.path.join(DATA_DIR, "Rocket Mortgage", "Annual Reports", "2025.pdf")),
]


def extract_pdf(pdf_path, out_path, stem):
    print(f"  Extracting: {stem} ...", end="", flush=True)
    try:
        with pdfplumber.open(pdf_path) as pdf:
            total = len(pdf.pages)
            lines = []
            for i, page in enumerate(pdf.pages, 1):
                text = page.extract_text(x_tolerance=2, y_tolerance=3)
                if text:
                    lines.append(f"\n\n{'='*60}\nPAGE {i} / {total}\n{'='*60}\n")
                    lines.append(text)
                if i % 50 == 0:
                    print(f" [{i}/{total}]", end="", flush=True)
        full_text = "".join(lines)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(full_text)
        size_kb = len(full_text) / 1024
        print(f" DONE  ({total} pages, {size_kb:.0f} KB)")
        return total, size_kb
    except Exception as e:
        print(f" ERROR: {e}")
        return 0, 0


def main():
    print("=" * 60)
    print("FULL PDF TEXT EXTRACTION PIPELINE")
    print("=" * 60)
    total_pages = 0
    total_size  = 0

    for stem, pdf_path in REPORTS:
        out_path = os.path.join(OUT_DIR, f"{stem}.txt")
        if not os.path.exists(pdf_path):
            print(f"  SKIP (not found): {pdf_path}")
            continue
        pages, size = extract_pdf(pdf_path, out_path, stem)
        total_pages += pages
        total_size  += size

    print()
    print(f"Extraction complete. {total_pages} total pages → {total_size:.0f} KB of text")
    print(f"Output directory: {OUT_DIR}")


if __name__ == "__main__":
    main()
