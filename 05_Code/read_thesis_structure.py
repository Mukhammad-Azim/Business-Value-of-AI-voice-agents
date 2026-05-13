import docx

doc = docx.Document("04_Drafts/Thesis-Structure.docx")
with open("04_Drafts/Thesis_Structure_Extracted.txt", "w", encoding="utf-8") as f:
    for i, p in enumerate(doc.paragraphs):
        text = p.text.strip()
        if text:
            f.write(f"Line {i+1}: {text}\n")
print("Extracted structure guidelines successfully!")
