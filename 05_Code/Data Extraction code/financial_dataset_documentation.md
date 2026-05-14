# Financial Dataset: Better.com vs Rocket Mortgage
## SEC Filing Comparative Analysis Dataset

**Dataset location:** `06_Data/financial_dataset_annual.csv`  
**Build scripts:** `05_Code/Data Extraction code/extract_pdf_texts.py`, `extract_s1.py`

---

## 1. Dataset Overview

| Property | Value |
|---|---|
| **Total rows** | 13 (Annual baseline + FY Actuals) |
| **Status** | 100% Complete (Zero-NA Integrity) |
| **Version** | V6 |
| **Companies** | Better Home & Finance (BETR), Rocket Companies (RKT) |
| **Time period** | Better: 2021–2025; Rocket: 2018–2025 |
| **Units** | All financial values in **millions USD** |
| **Source** | 10-K filings, S-1 historicals, and audited manual cross-checks. |

---

## 2. Source Documents & Data Provenance

The following annual reports have been verified and are part of the extraction corpus:

### Rocket Mortgage (Rocket Companies, Inc.)
- **2025 10-K**: Primary source for 2024-2025 actuals.
- **2024 10-K**: Primary source for 2022-2024 data.
- **2023 10-K**: Primary source for 2021-2023 data.
- **2021 10-K**: Historical context for 2018-2020.
- **2020 10-K**: IPO-era historical financials (2018-2020).

### Better.com (Better Home & Finance Holding Co.)
- **2025 10-K**: Primary source for 2024-2025.
- **2024 10-K**: Primary source for 2023-2024.
- **2023 10-K**: Post-merger financials for 2022-2023. Contains "Smaller Reporting Company" (SRC) disclosure limiting audited statements to two years.
- **2021 10-K (Aurora SPAC)**: Contains SPAC-only financials; Better.com operational history for 2021 is not present in this filing.
- **S-1/S-4 Filings**: Source for 2021 historicals, as the 2023 10-K only covers back to 2022.

---

## 3. Data Coverage Matrix

| Metric | Rocket (2018-2025) | Better (2021-2025) |
| :--- | :--- | :--- |
| **Revenue** | ✅ Complete | ✅ Complete |
| **Op_Cash_Flow** | ✅ Complete | ✅ Complete |
| **Total_Equity** | ✅ Complete | ✅ Complete |
| **Employee Count** | ✅ Complete | ✅ Complete |

---

## 4. Key Notes from the Data Collection

1. **Better.com SRC Status**: Better's transition to a public company follows "Smaller Reporting Company" rules, meaning their 10-Ks only provide 2 years of audited P&L (compared to Rocket's 3 years). This created the 2021 gap in the 2023 10-K.
2. **Employee Peak**: Better's 2021 employee peak of **10,400** was confirmed in the 2023 10-K narrative, providing a critical data point for the efficiency analysis.
3. **Rocket 2025 Scale**: Rocket's 2025 financials show significant scale-up due to the Mr. Cooper acquisition, which must be controlled for in per-employee efficiency metrics.
4. **Consistency**: All monetary values have been verified as adjusted to **Millions USD** across all sources.

---

## 5. Visualizations & Thesis Integration
This dataset supports the following thesis figures:
- **Figure 5.1**: Better.com Financial Trajectory (2021–2025)
- **Figure 5.2**: Expense Ratio & Operating Cash Flow Margin
- **Figure 5.3**: Headcount & Revenue per Employee
