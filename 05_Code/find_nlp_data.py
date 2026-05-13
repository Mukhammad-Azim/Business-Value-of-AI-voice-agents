import os

for root, dirs, files in os.walk("."):
    for file in files:
        if "review" in file.lower() or "trustpilot" in file.lower():
            print(os.path.join(root, file))
