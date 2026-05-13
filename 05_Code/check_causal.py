import re

with open("04_Drafts/Main_Draft_Extracted.md", "r", encoding="utf-8") as f:
    text = f.read()

lines = text.split("\n")
words = ["caused", "attributed", "attributable", "caused by", "attributed to"]

for i, line in enumerate(lines):
    for w in words:
        if re.search(r'\b' + re.escape(w) + r'\b', line, re.IGNORECASE):
            print(f"Line {i+1} ({w}): {line[:120]}...")
            break
