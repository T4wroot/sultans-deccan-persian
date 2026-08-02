import pdfplumber
import fitz
import json
import os

pdf_path = "Sultans_of_Deccan_India_1500_1700.pdf"
text_dir = "extracted_pages_pdfplumber"
img_dir = "extracted_images"

os.makedirs(text_dir, exist_ok=True)
os.makedirs(img_dir, exist_ok=True)

progress_file = "processing_progress.json"

progress = {
    "total_pages": 386,
    "extracted_pages": 0,
    "extracted_images": 0,
    "translated_pages": 0,
    "current_step": "استخراج متون با pdfplumber و استخراج تصاویر",
    "status": "در حال اجرای فاز ۱"
}

with open(progress_file, "w", encoding="utf-8") as f:
    json.dump(progress, f, ensure_ascii=False, indent=2)

print("Starting Step 1: Layout-preserved PDF extraction using pdfplumber & PyMuPDF...")

doc = fitz.open(pdf_path)
total_pages = len(doc)
total_extracted_images = 0

# 1. Extract Images via PyMuPDF
for i, page in enumerate(doc):
    pnum = i + 1
    image_list = page.get_images(full=True)
    for img_index, img in enumerate(image_list):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        img_name = f"page_{pnum:03d}_img_{img_index + 1}.{image_ext}"
        img_path = os.path.join(img_dir, img_name)
        with open(img_path, "wb") as f_img:
            f_img.write(image_bytes)
        total_extracted_images += 1

print(f"Extracted all {total_extracted_images} images successfully.")

# 2. Extract Exact Text Layout via pdfplumber
with pdfplumber.open(pdf_path) as pdf:
    for pnum in range(1, total_pages + 1):
        page = pdf.pages[pnum - 1]
        
        layout_text = page.extract_text(
            layout=True,
            x_tolerance=3,
            y_tolerance=3
        )
        
        words = page.extract_words(x_tolerance=3, y_tolerance=3)
        
        txt_path = os.path.join(text_dir, f"page_{pnum:03d}.txt")
        with open(txt_path, "w", encoding="utf-8") as f_txt:
            f_txt.write(layout_text if layout_text else f"[Page {pnum} contains images/artwork without text]")
            
        json_path = os.path.join(text_dir, f"page_{pnum:03d}.json")
        with open(json_path, "w", encoding="utf-8") as f_js:
            json.dump({
                "page": pnum,
                "word_count": len(words),
                "width": float(page.width),
                "height": float(page.height)
            }, f_js, ensure_ascii=False, indent=2)
            
        progress["extracted_pages"] = pnum
        progress["extracted_images"] = total_extracted_images
        
        if pnum % 10 == 0 or pnum == total_pages:
            with open(progress_file, "w", encoding="utf-8") as f_p:
                json.dump(progress, f_p, ensure_ascii=False, indent=2)
            print(f"Extracted text layout for page {pnum}/{total_pages}")

progress["current_step"] = "تکمیل فاز ۱ - آماده برای فاز ۲ (ترجمه)"
progress["status"] = "فاز ۱ با موفقیت پایان یافت"

with open(progress_file, "w", encoding="utf-8") as f_p:
    json.dump(progress, f_p, ensure_ascii=False, indent=2)

print("Step 1 completed successfully!")
