import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = "Sultans_of_Deccan_India_1500_1700.pdf"
doc = fitz.open(pdf_path)

page20_text = doc[19].get_text("text")

print("=== ORIGINAL ENGLISH PAGE 20 ===")
print(page20_text[:600])

# Save clean extracted text to page_020_raw.txt
with open("page_020_raw.txt", "w", encoding="utf-8") as f:
    f.write(page20_text)

print("\nSaved page_020_raw.txt successfully!")
