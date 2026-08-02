import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

extracted_dir = "extracted_pages_clean"
translated_dir = "translated_pages_clean"

GLOSSARY_REPLACEMENTS = [
    (r"توسط con-\s*تراست", "در مقابل"),
    (r"con-\s*تراست", "در مقابل"),
    (r"con-trast", "contrast"),
    (r"By contrast", "در مقابل"),
    (r"by contrast", "در مقابل"),
    (r"ویژگی پیوند", "انتساب هنری"),
    (r"pos-\s*سفلی", "احتمالاً"),
    (r"pos-\s*sibly", "possibly"),
    (r"attri-\s*bution", "attribution"),
    (r"under-\s*drawing", "underdrawing"),
    (r"گربه\s*(\d+)", r"اثر شماره \1"),
    (r"بیمار نه\s*(\d+)", r"تصویر شماره \1"),
    (r"پرنده Mynah", "مرغ مینا"),
    (r"Bodleian", "بودلیان"),
    (r"زاهد صوفی", "عارف صوفی"),
    (r"برس کاری", "قلم‌گیری و قلم‌زنی"),
    (r"هندلینگ", "پرداخت و ساخت‌وساز"),
]

def clean_english_page(raw_text):
    # 1. Fix line-ending hyphenation
    text = re.sub(r'(\b[A-Za-z]+)-\s*\n\s*([a-z]+\b)', r'\1\2', raw_text)
    
    # 2. Join paragraph lines
    lines = text.splitlines()
    paragraphs = []
    curr_para = []
    
    for l in lines:
        l_str = l.strip()
        if not l_str:
            if curr_para:
                paragraphs.append(" ".join(curr_para))
                curr_para = []
            continue
            
        if re.match(r'^(Cat\.|Catalogue|Fig\.|[0-9]{1,3}\b)', l_str) or len(l_str) < 32:
            if curr_para:
                paragraphs.append(" ".join(curr_para))
                curr_para = []
            paragraphs.append(l_str)
        else:
            curr_para.append(l_str)
            
    if curr_para:
        paragraphs.append(" ".join(curr_para))
        
    return "\n\n".join(paragraphs)

def fix_persian_translation_artifacts(fa_text):
    text = fa_text
    for pattern, replacement in GLOSSARY_REPLACEMENTS:
        text = re.sub(pattern, replacement, text)
    return text

print("Step 1: Cleaning English hyphenations and joining sentences across all 386 pages...")
cleaned_count = 0
for p_num in range(1, 387):
    p_str = f"{p_num:03d}"
    eng_path = os.path.join(extracted_dir, f"page_{p_str}.txt")
    if os.path.exists(eng_path):
        with open(eng_path, "r", encoding="utf-8") as f:
            raw_eng = f.read()
        clean_eng = clean_english_page(raw_eng)
        with open(eng_path, "w", encoding="utf-8") as f:
            f.write(clean_eng)
        cleaned_count += 1

print(f"Cleaned and de-hyphenated {cleaned_count} English page files.")

print("Step 2: Fixing Persian translation artifacts and line-joining across all 386 pages...")
fixed_fa_count = 0
for p_num in range(1, 387):
    p_str = f"{p_num:03d}"
    fa_path = os.path.join(translated_dir, f"page_{p_str}_fa.txt")
    if os.path.exists(fa_path):
        with open(fa_path, "r", encoding="utf-8") as f:
            raw_fa = f.read()
        fixed_fa = fix_persian_translation_artifacts(raw_fa)
        with open(fa_path, "w", encoding="utf-8") as f:
            f.write(fixed_fa)
        fixed_fa_count += 1

print(f"Fixed Persian translation artifacts for {fixed_fa_count} translated page files.")
