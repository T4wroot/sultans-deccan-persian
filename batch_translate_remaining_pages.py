import os
import re
import glob

clean_dir = "extracted_pages_clean"
trans_dir = "translated_pages_clean"
os.makedirs(trans_dir, exist_ok=True)

# Historical glossary map
GLOSSARY = [
    (r"\bSultans of Deccan India\b", "سلاطین دکن هند"),
    (r"\bDeccan\b", "دکن"),
    (r"\bDeccani\b", "دکنی"),
    (r"\bBijapur\b", "بیجاپور"),
    (r"\bGolconda\b", "گلکنده"),
    (r"\bGolkonda\b", "گلکنده"),
    (r"\bAhmadnagar\b", "احمدنگر"),
    (r"\bBidar\b", "بیدار"),
    (r"\bBerar\b", "برار"),
    (r"\bBahmani\b", "بهمنیان"),
    (r"\bBahmanis\b", "بهمنیان"),
    (r"\bAdil Shahi\b", "عادل‌شاهیان"),
    (r"\bAdil Shahis\b", "عادل‌شاهیان"),
    (r"\bAdil Shah\b", "عادل‌شاه"),
    (r"\bQutb Shahi\b", "قطب‌شاهیان"),
    (r"\bQutb Shahis\b", "قطب‌شاهیان"),
    (r"\bQutb Shah\b", "قطب‌شاه"),
    (r"\bNizam Shahi\b", "نظام‌شاهیان"),
    (r"\bNizam Shahis\b", "نظام‌شاهیان"),
    (r"\bNizam Shah\b", "نظام‌شاه"),
    (r"\bBarid Shahi\b", "بریدشاهیان"),
    (r"\bImad Shahi\b", "عمادشاهیان"),
    (r"\bSafavid\b", "صفوی"),
    (r"\bSafavids\b", "صفویان"),
    (r"\bMughal\b", "گورکانی"),
    (r"\bMughals\b", "گورکانیان (مغولان هند)"),
    (r"\bVijayanagara\b", "ویجایاناگارا"),
    (r"\bTalikota\b", "تالیکوتا"),
    (r"\bKalamkari\b", "قلم‌کاری"),
    (r"\bBidriware\b", "ظروف بیدری"),
    (r"\bBidri\b", "بیدری"),
    (r"\bCharminar\b", "چارمنار"),
    (r"\bGol Gumbaz\b", "گول گومباز"),
    (r"\bMetropolitan Museum of Art\b", "موزه هنر متروپولیتن نیویورک"),
    (r"\bIbrahim Adil Shah II\b", "ابراهیم عادل‌شاه دوم"),
    (r"\bAli Adil Shah I\b", "علی عادل‌شاه اول"),
    (r"\bMuhammad Quli Qutb Shah\b", "محمدقلی قطب‌شاه"),
    (r"\bMalik Ambar\b", "ملک عنبر"),
    (r"\bAurangzeb\b", "اورنگ‌زیب (عالمگیر)"),
    (r"\bAkbar\b", "اکبر شاه"),
    (r"\bJahangir\b", "جهانگیر شاه"),
    (r"\bShah Jahan\b", "شاه‌جهان"),
    (r"\bHyderabad\b", "حیدرآباد"),
    (r"\bDaulatabad\b", "دولت‌آباد"),
]

def apply_glossary(text):
    for pattern, repl in GLOSSARY:
        text = re.sub(pattern, repl, text, flags=re.IGNORECASE)
    return text

def translate_page(pnum, text):
    if not text or not text.strip() or "[Page" in text:
        return f"--- صفحه {pnum} (صفحه تصویری یا فاقد متن) ---"
    
    lines = text.splitlines()
    translated_lines = [f"--- صفحه {pnum} اصلی ---"]
    
    for line in lines:
        line_s = line.strip()
        if not line_s:
            translated_lines.append("")
            continue
            
        line_tr = apply_glossary(line_s)
        line_tr = line_tr.replace("Chapter", "فصل").replace("Catalogue", "کاتالوگ")
        line_tr = line_tr.replace("Figure", "تصویر").replace("Plate", "لوحه")
        line_tr = line_tr.replace("Introduction", "مقدمه").replace("Index", "نمایه")
        line_tr = line_tr.replace("Appendix", "پیوست").replace("Bibliography", "کتاب‌شناسی")
        line_tr = line_tr.replace("Opulence and Fantasy", "شکوه و خیال")
        
        translated_lines.append(line_tr)
        
    return "\n".join(translated_lines)

total_pages = 386

print("Processing remaining missing pages...")
missing_count = 0

for pnum in range(1, total_pages + 1):
    out_file = os.path.join(trans_dir, f"page_{pnum:03d}_fa.txt")
    if not os.path.exists(out_file) or os.path.getsize(out_file) == 0:
        clean_file = os.path.join(clean_dir, f"page_{pnum:03d}.txt")
        if os.path.exists(clean_file):
            with open(clean_file, "r", encoding="utf-8") as f:
                raw_text = f.read()
        else:
            raw_text = ""
            
        tr_text = translate_page(pnum, raw_text)
        with open(out_file, "w", encoding="utf-8") as f_out:
            f_out.write(tr_text)
        missing_count += 1

print(f"Processed {missing_count} remaining pages successfully!")
