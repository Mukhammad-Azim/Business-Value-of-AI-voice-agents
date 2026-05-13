import docx
import os

def docx_to_md(docx_path, md_path):
    doc = docx.Document(docx_path)
    with open(md_path, 'w', encoding='utf-8') as f:
        for para in doc.paragraphs:
            # Handle headers (rough estimation based on style)
            if para.style.name.startswith('Heading'):
                level = para.style.name.split(' ')[-1]
                try:
                    f.write('#' * int(level) + ' ' + para.text + '\n\n')
                except:
                    f.write('## ' + para.text + '\n\n')
            else:
                f.write(para.text + '\n\n')

if __name__ == "__main__":
    src = r"c:\Users\User\OneDrive\Рабочий стол\Thesis\04_Drafts\Main_Draft.docx"
    dst = r"c:\Users\User\OneDrive\Рабочий стол\Thesis\04_Drafts\Main_Draft.md"
    docx_to_md(src, dst)
    print(f"Converted {src} to {dst}")
