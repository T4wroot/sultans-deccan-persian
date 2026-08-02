import os
import glob
import re
import json
import base64
import fitz
import time

progress_file = "processing_progress.json"
text_dir = "extracted_pages_pdfplumber"
trans_dir = "translated_pages_clean"
img_dir = "extracted_images"
out_dir = "output_pdf"

os.makedirs(out_dir, exist_ok=True)

total_pages = 386

print("Waiting for Step 1 & Step 2 to finish processing all 386 pages...")

# Wait until all 386 pages are translated
while True:
    tr_files = glob.glob(os.path.join(trans_dir, "*.txt"))
    if len(tr_files) >= total_pages:
        break
    time.sleep(2)

print(f"All {total_pages} pages translated! Starting Step 3: PDF & HTML Compilation...")

# Load Vazirmatn fonts as base64
with open("Vazirmatn-Regular.ttf", "rb") as f:
    vazir_reg_b64 = base64.b64encode(f.read()).decode('utf-8')

with open("Vazirmatn-Bold.ttf", "rb") as f:
    vazir_bold_b64 = base64.b64encode(f.read()).decode('utf-8')

# Cover image
cover_img_path = os.path.join(img_dir, "page_001_img_1.jpeg")
if os.path.exists(cover_img_path):
    with open(cover_img_path, "rb") as f:
        cover_b64 = base64.b64encode(f.read()).decode('utf-8')
    cover_img_tag = f'<img src="data:image/jpeg;base64,{cover_b64}" style="max-width: 75%; height: auto; border-radius: 8px; box-shadow: 0 10px 25px rgba(0,0,0,0.2); margin: 20px 0;">'
else:
    cover_img_tag = ""

html_header = f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<title>ترجمه کامل و دقیق کتاب سلاطین دکن هند - انوشه طاهری</title>
<style>
@font-face {{
    font-family: 'Vazirmatn';
    src: url('data:font/ttf;charset=utf-8;base64,{vazir_reg_b64}') format('truetype');
    font-weight: normal;
    font-style: normal;
}}
@font-face {{
    font-family: 'Vazirmatn';
    src: url('data:font/ttf;charset=utf-8;base64,{vazir_bold_b64}') format('truetype');
    font-weight: bold;
    font-style: normal;
}}

@page {{
    size: A4;
    margin: 20mm 15mm 20mm 15mm;
}}

body {{
    font-family: 'Vazirmatn', 'Segoe UI', Tahoma, sans-serif;
    direction: rtl;
    text-align: right;
    font-size: 11pt;
    line-height: 1.9;
    color: #1f2937;
    background-color: #f1f5f9;
    margin: 0;
    padding: 20px;
}}

/* Cover Page Styling */
.cover-container {{
    text-align: center;
    padding: 30px 20px;
    page-break-after: always;
}}

.thesis-tag {{
    color: #991b1b;
    font-weight: bold;
    font-size: 16pt;
    margin-bottom: 15px;
    padding: 8px 18px;
    background-color: #fef2f2;
    display: inline-block;
    border-radius: 6px;
    border: 1px solid #fecaca;
}}

.book-title {{
    color: #1e3a8a;
    font-weight: bold;
    font-size: 24pt;
    margin-top: 15px;
    margin-bottom: 10px;
    line-height: 1.3;
}}

.book-subtitle {{
    color: #374151;
    font-size: 13pt;
    margin-bottom: 20px;
}}

.divider-line {{
    height: 3px;
    background: linear-gradient(to right, #1e3a8a, #991b1b, #1e3a8a);
    margin: 20px auto;
    width: 75%;
    border-radius: 2px;
}}

.thesis-credits {{
    background-color: #f8fafc;
    border: 2px solid #cbd5e1;
    border-radius: 8px;
    padding: 20px;
    width: 85%;
    margin: 20px auto 0 auto;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
}}

.credit-title {{
    color: #1e3a8a;
    font-weight: bold;
    font-size: 14pt;
    margin-bottom: 8px;
}}

.credit-author {{
    color: #991b1b;
    font-weight: bold;
    font-size: 16pt;
    margin-bottom: 6px;
}}

.credit-details {{
    color: #64748b;
    font-size: 10.5pt;
}}

.page-block {{
    background: #ffffff;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    margin: 40px auto;
    padding: 50px 60px;
    max-width: 800px;
    min-height: 1000px;
    page-break-after: always;
    break-after: page;
}}

.page-marker {{
    color: #1e3a8a;
    font-weight: bold;
    font-size: 10.5pt;
    background-color: #eff6ff;
    padding: 4px 10px;
    border-radius: 4px;
    display: inline-block;
    margin: 15px 0 10px 0;
    border-right: 4px solid #3b82f6;
}}

.page-image {{
    text-align: center;
    margin: 15px 0;
}}

.page-image img {{
    max-width: 90%;
    max-height: 450px;
    height: auto;
    border-radius: 6px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}}

.catalog-page-header {{
    text-align: center;
    font-size: 10pt;
    color: #9ca3af;
    border-bottom: 1px solid #cbd5e1;
    padding-bottom: 8px;
    margin-bottom: 30px;
    font-weight: bold;
    letter-spacing: 1px;
}}

.catalog-title {{
    color: #1e3a8a;
    font-weight: bold;
    font-size: 14pt;
    margin-top: 25px;
    margin-bottom: 12px;
    border-bottom: 2px solid #3b82f6;
    padding-bottom: 6px;
}}

.catalog-meta {{
    color: #4b5563;
    font-size: 10pt;
    font-style: italic;
    line-height: 1.7;
    margin-bottom: 20px;
    background-color: #f8fafc;
    border-right: 4px solid #3b82f6;
    padding: 10px 15px;
    border-radius: 4px;
}}

h1.chapter-title {{
    color: #1e3a8a;
    font-weight: bold;
    font-size: 18pt;
    border-bottom: 2px solid #3b82f6;
    padding-bottom: 8px;
    margin-top: 30px;
    margin-bottom: 15px;
}}

p {{
    margin-bottom: 12px;
    text-align: justify;
    text-justify: inter-word;
}}

.footer-note {{
    text-align: center;
    font-size: 9pt;
    color: #9ca3af;
    margin-top: 40px;
    border-top: 1px solid #e5e7eb;
    padding-top: 10px;
}}
</style>
</head>
<body>

<div class="cover-container">
    <div class="thesis-tag">پایان‌نامه دکترا</div>
    <div class="book-title">سلاطین دکن هند (۱۵۰۰–۱۷۰۰)</div>
    <div class="book-subtitle">شکوه و خیال در هنر، معماری و فرهنگ اسلامی</div>
    
    {cover_img_tag}
    
    <div class="divider-line"></div>
    
    <div class="thesis-credits">
        <div class="credit-title">عنوان پژوهش و ترجمه کامل صفحه به صفحه:</div>
        <div class="credit-author">ترجمه انوشه طاهری - پایان‌نامه دکترا</div>
        <div class="credit-details">
            نویسندگان اصلی: ناویینا نجات حیدر و ماریکا سردار (موزه هنر متروپولیتن نیویورک)<br>
            رشته تاریخ هنر و معماری اسلامی | سال تحصیلی ۱۴۰۵ - ۱۴۰۶
        </div>
    </div>
</div>
"""

html_body = []

for pnum in range(1, total_pages + 1):
    tr_file = os.path.join(trans_dir, f"page_{pnum:03d}_fa.txt")
    if os.path.exists(tr_file):
        with open(tr_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
    else:
        lines = []
        
    html_body.append(f'<div class="page-block" id="page-{pnum}">')
    html_body.append(f'<div class="page-marker">--- صفحه {pnum} از {total_pages} ---</div>')
    
    # Images for this page
    p_imgs = sorted([f for f in os.listdir(img_dir) if f.startswith(f"page_{pnum:03d}_")])
    for img_name in p_imgs:
        img_path = os.path.join(img_dir, img_name)
        if os.path.exists(img_path):
            with open(img_path, "rb") as f_img:
                img_b64 = base64.b64encode(f_img.read()).decode('utf-8')
            ext = img_name.split('.')[-1]
            if ext.lower() == 'jpg': ext = 'jpeg'
            html_body.append(f'<div class="page-image"><img src="data:image/{ext};base64,{img_b64}"></div>')
            
    # Page text
    for line in lines:
        line_str = line.strip()
        if not line_str or line_str.startswith("--- صفحه"):
            continue
        
        is_page_hdr = re.match(r'^(کاتالوگ|Catalogue)\s+\d+$', line_str)
        is_cat_title = (re.match(r'^(\d{1,3}\s+\w+|\d{1,3}\s+|گربه\s*\d+|کاتالوگ\s*\d+)', line_str) or line_str.startswith("گربه ") or line_str.startswith("کاتالوگ ")) and len(line_str) < 90
        is_cat_meta = any(k in line_str for k in ["منسوب به", "حدود", "جوهر،", "آبرنگ", "موزه", "کتابخانه", "مجموعه", "کاغذ", "سانتی متر", "اینچ"]) and len(line_str) < 180
        
        if line_str.startswith("فصل") or line_str.startswith("سلاطین") or line_str.startswith("پیوست") or line_str.startswith("نمایه"):
            html_body.append(f'<h1 class="chapter-title">{line_str}</h1>')
        elif is_page_hdr:
            html_body.append(f'<div class="catalog-page-header">{line_str}</div>')
        elif is_cat_title:
            html_body.append(f'<h2 class="catalog-title">{line_str}</h2>')
        elif is_cat_meta:
            html_body.append(f'<div class="catalog-meta">{line_str}</div>')
        else:
            html_body.append(f'<p>{line_str}</p>')
            
    html_body.append('</div>')

html_footer = """
<div class="footer-note">
    ترجمه کامل و صفحه به صفحه کتاب سلاطین دکن هند (۱۵۰۰-۱۷۰۰) | ترجمه انوشه طاهری - پایان‌نامه دکترا
</div>
</body>
</html>
"""

full_html = html_header + "\n".join(html_body) + html_footer
html_file_path = os.path.join(out_dir, "Sultans_of_Deccan_Persian_Complete.html")
with open(html_file_path, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"HTML document saved: {html_file_path}")

pdf_output_path = os.path.join(out_dir, "Sultans_of_Deccan_India_Persian_Translation_Complete.pdf")

print("Rendering final 386-page PDF...")
story = fitz.Story(full_html)
writer = fitz.DocumentWriter(pdf_output_path)
more = True
page_count = 0
while more:
    device = writer.begin_page(fitz.Rect(0, 0, 595, 842))
    more, _ = story.place(fitz.Rect(40, 40, 555, 802))
    story.draw(device)
    writer.end_page()
    page_count += 1

writer.close()

print(f"PDF rendered successfully: {pdf_output_path} ({page_count} PDF pages)")

if os.path.exists(progress_file):
    with open(progress_file, "r", encoding="utf-8") as f_p:
        prog = json.load(f_p)
    prog["current_step"] = "تکمیل موفقیت‌آمیز پروژه"
    prog["status"] = f"پایان پروژه - فایل PDF در {page_count} صفحه تولید شد."
    with open(progress_file, "w", encoding="utf-8") as f_p:
        json.dump(prog, f_p, ensure_ascii=False, indent=2)

print("Step 3 completed successfully!")
