import os
import shutil

files_to_remove = [
    "analyze_and_extract.py",
    "build_complete_386page_pdf.py",
    "build_pdf_document.py",
    "extract_all_pages_and_images.py",
    "extract_pages_1_to_10_exact.py",
    "generate_final_persian_pdf.py",
    "generate_persian_pdf.py",
    "inspect_pages_1_to_5.py",
    "process_and_save_translations.py",
    "test_b64_pdf.pdf",
    "test_base64_font.py",
    "test_doc.html",
    "test_pdf_rendering.py",
    "test_pymupdf.pdf",
    "test_reportlab_reshaper.py",
    "test_rl_reshaper.pdf",
    "translate_all_386_pages.py",
    "Sultans_of_Deccan_India_Persian_Translation.pdf",
    "Sultans_of_Deccan_India_Persian_Translation_Complete.pdf",
    "Sultans_of_Deccan_Persian_Complete.html",
    "Sultans_of_Deccan_Persian_Thesis.html",
    "all_pages_stats.json",
    "extraction_stats.json",
    "english_pages_1_to_5.txt",
    "english_pages_1_to_10.txt"
]

dirs_to_remove = [
    "extracted_chapters",
    "translated_chapters",
    "pages_raw",
    "pages_translated",
    "pages_images"
]

for f in files_to_remove:
    if os.path.exists(f):
        try:
            os.remove(f)
            print(f"Removed file: {f}")
        except Exception as e:
            print(f"Failed to remove {f}: {e}")

for d in dirs_to_remove:
    if os.path.exists(d):
        try:
            shutil.rmtree(d)
            print(f"Removed dir: {d}")
        except Exception as e:
            print(f"Failed to remove {d}: {e}")

# Create new clean directories
new_dirs = [
    "extracted_pages_pdfplumber",
    "extracted_images",
    "translated_pages",
    "output_pdf"
]

for d in new_dirs:
    os.makedirs(d, exist_ok=True)
    print(f"Created clean dir: {d}")

print("Workspace cleanup completed successfully!")
