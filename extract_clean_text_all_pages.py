import fitz
import os
import json

pdf_path = "Sultans_of_Deccan_India_1500_1700.pdf"
clean_dir = "extracted_pages_clean"
os.makedirs(clean_dir, exist_ok=True)

doc = fitz.open(pdf_path)
total_pages = len(doc)
print(f"Extracting clean text for all {total_pages} pages...")

page_stats = []

for i, page in enumerate(doc):
    pnum = i + 1
    text = page.get_text("text")
    
    out_path = os.path.join(clean_dir, f"page_{pnum:03d}.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        if text and text.strip():
            f.write(text.strip())
        else:
            f.write(f"[Page {pnum} contains images/artwork without text]")
            
    word_count = len(text.split()) if text else 0
    page_stats.append({
        "page": pnum,
        "words": word_count,
        "chars": len(text) if text else 0,
        "file": out_path
    })
    
    if pnum % 50 == 0 or pnum == total_pages:
        print(f"Extracted clean text for page {pnum}/{total_pages}")

with open("clean_pages_stats.json", "w", encoding="utf-8") as f:
    json.dump(page_stats, f, ensure_ascii=False, indent=2)

print("All 386 clean text files extracted successfully!")
