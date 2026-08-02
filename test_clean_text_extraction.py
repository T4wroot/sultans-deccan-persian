import pdfplumber
import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = "Sultans_of_Deccan_India_1500_1700.pdf"

print("--- Testing PyMuPDF (fitz) text for Page 20 ---")
doc = fitz.open(pdf_path)
page20_fitz = doc[19].get_text("text")
print("fitz text length:", len(page20_fitz))
print("fitz first 400 chars:\n", page20_fitz[:400])

print("\n--- Testing pdfplumber (layout=False) text for Page 20 ---")
with pdfplumber.open(pdf_path) as pdf:
    page20_plumber = pdf.pages[19].extract_text(layout=False)
    print("plumber text length:", len(page20_plumber))
    print("plumber first 400 chars:\n", page20_plumber[:400])
