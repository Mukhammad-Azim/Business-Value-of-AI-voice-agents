import os

def finalize_draft():
    md_path = r"c:\Users\User\OneDrive\Рабочий стол\Thesis\04_Drafts\Main_Draft.md"
    final_path = r"c:\Users\User\OneDrive\Рабочий стол\Thesis\04_Drafts\Main_Draft_Final.md"
    
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    appendix = """
### 10. Appendix: Primary Empirical Data Sources (SEC Filings Corpus)

The longitudinal financial dataset utilized in this research was constructed using the following primary regulatory filings, processed via automated textual extraction and data engineering pipelines.

**Better Home & Finance Holding Company (BETR) / Aurora Acquisition Corp:**
*   **Annual Reports (Form 10-K):** 2021, 2022, 2023, 2024, 2025.

**Rocket Companies, Inc. (RKT):**
*   **Annual Reports (Form 10-K):** 2020, 2021, 2022, 2023, 2024, 2025.

*Note: All filings were accessed via the SEC EDGAR database and processed locally within the research workspace to ensure high-fidelity longitudinal alignment and cross-verification.*
"""
    
    with open(final_path, 'w', encoding='utf-8') as f:
        f.write(content + "\n\n" + appendix)
    print(f"Finalized draft at {final_path}")

if __name__ == "__main__":
    finalize_draft()
