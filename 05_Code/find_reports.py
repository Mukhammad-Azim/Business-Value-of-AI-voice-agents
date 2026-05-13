import os

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".md") or file.endswith(".docx") or file.endswith(".txt"):
            if "report" in file.lower() or "draft" in file.lower() or "thesis" in file.lower() or "structure" in file.lower():
                print(os.path.join(root, file))
