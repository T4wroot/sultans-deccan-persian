import pdfplumber
import json
import os

pdf_path = "Sultans_of_Deccan_India_1500_1700.pdf"
output_txt = "english_pages_1_to_10_pdfplumber.txt"
output_json = "english_pages_1_to_10_structured.json"

structured_pages = []

with pdfplumber.open(pdf_path) as pdf:
    with open(output_txt, "w", encoding="utf-8") as f_out:
        for pnum in range(1, 11): # Pages 1 to 10
            page = pdf.pages[pnum - 1]
            
            # Extract words with layout information
            words = page.extract_words(
                x_tolerance=3,
                y_tolerance=3,
                keep_blank_chars=True,
                use_text_flow=True
            )
            
            # Extract plain layout text
            layout_text = page.extract_text(
                layout=True,
                x_tolerance=3,
                y_tolerance=3
            )
            
            # Extract tables if any
            tables = page.extract_tables()
            
            page_data = {
                "page_number": pnum,
                "width": float(page.width),
                "height": float(page.height),
                "layout_text": layout_text if layout_text else "[No text on this page]",
                "word_count": len(words),
                "tables_count": len(tables),
                "words_sample": words[:10] if words else []
            }
            structured_pages.append(page_data)
            
            # Write to formatted text file
            f_out.write(f"==================== PAGE {pnum} (Width: {page.width:.1f}, Height: {page.height:.1f}) ====================\n")
            if layout_text and layout_text.strip():
                f_out.write(layout_text.strip())
            else:
                f_out.write(f"[Page {pnum} contains images/artwork without text]")
            f_out.write("\n\n")
            
            print(f"Extracted Page {pnum}: {len(words)} words, {len(tables)} tables")

with open(output_json, "w", encoding="utf-8") as f_json:
    json.dump(structured_pages, f_json, ensure_ascii=False, indent=2)

print(f"Extraction completed! Text saved to {output_txt} and JSON saved to {output_json}")
