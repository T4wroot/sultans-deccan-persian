import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read Page 5, 8, 20 from extracted_pages_pdfplumber
pages_to_test = [5, 8, 20]

for pnum in pages_to_test:
    fpath = f"extracted_pages_pdfplumber/page_{pnum:03d}.txt"
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        print(f"=== ORIGINAL ENGLISH PAGE {pnum} ===")
        print(content[:400])
        print("\n")
