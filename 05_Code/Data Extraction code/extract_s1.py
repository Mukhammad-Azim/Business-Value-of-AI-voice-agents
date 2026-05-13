import pypdf
import os

pdf_path = r"c:\Users\User\OneDrive\Рабочий стол\Thesis\03_Case_Study_Data\Better\Annual Reports\S1.pdf"
txt_path = r"c:\Users\User\OneDrive\Рабочий стол\Thesis\08_Code\extracted_text\Better_S1.txt"

def extract_text():
    print(f"Extracting {pdf_path}...")
    try:
        reader = pypdf.PdfReader(pdf_path)
        with open(txt_path, 'w', encoding='utf-8') as f:
            for i, page in enumerate(reader.pages):
                f.write(f"--- PAGE {i+1} ---\n")
                f.write(page.extract_text() + "\n")
        print("Success.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    extract_text()
