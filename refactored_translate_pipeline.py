import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from deep_translator import GoogleTranslator

sys.stdout.reconfigure(encoding='utf-8')

# Directory configuration
INPUT_DIR = "extracted_pages_clean"
OUTPUT_DIR = "translated_pages_clean"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Glossary for post-translation replacement
GLOSSARY = {
    # 1. English terms to Persian (in case Google Translate didn't translate them)
    r"\bSultans of Deccan India\b": "سلاطین دکن هند",
    r"\bDeccan\b": "دکن",
    r"\bDeccani\b": "دکنی",
    r"\bBijapur\b": "بیجاپور",
    r"\bGolconda\b": "گلکنده",
    r"\bGolkonda\b": "گلکنده",
    r"\bAhmadnagar\b": "احمدنگر",
    r"\bBidar\b": "بیدار",
    r"\bBerar\b": "برار",
    r"\bBahmani\b": "بهمنیان",
    r"\bBahmanis\b": "بهمنیان",
    r"\bAdil Shahi\b": "عادل‌شاهیان",
    r"\bAdil Shahis\b": "عادل‌شاهیان",
    r"\bAdil Shah\b": "عادل‌شاه",
    r"\bQutb Shahi\b": "قطب‌شاهیان",
    r"\bQutb Shahis\b": "قطب‌شاهیان",
    r"\bQutb Shah\b": "قطب‌شاه",
    r"\bNizam Shahi\b": "نظام‌شاهیان",
    r"\bNizam Shahis\b": "نظام‌شاهیان",
    r"\bNizam Shah\b": "نظام‌شاه",
    r"\bBarid Shahi\b": "بریدشاهیان",
    r"\bImad Shahi\b": "عمادشاهیان",
    r"\bSafavid\b": "صفوی",
    r"\bSafavids\b": "صفویان",
    r"\bMughal\b": "گورکانی",
    r"\bMughals\b": "گورکانیان",
    r"\bVijayanagara\b": "ویجایاناگارا",
    r"\bTalikota\b": "تالیکوتا",
    r"\bKalamkari\b": "قلم‌کاری",
    r"\bBidriware\b": "ظروف بیدری",
    r"\bBidri\b": "بیدری",
    r"\bCharminar\b": "چارمنار",
    r"\bGol Gumbaz\b": "گول گومباز",
    r"\bMetropolitan Museum of Art\b": "موزه هنر متروپولیتن نیویورک",
    r"\bIbrahim Adil Shah II\b": "ابراهیم عادل‌شاه دوم",
    r"\bAli Adil Shah I\b": "علی عادل‌شاه اول",
    r"\bMuhammad Quli Qutb Shah\b": "محمدقلی قطب‌شاه",
    r"\bMalik Ambar\b": "ملک عنبر",
    r"\bAurangzeb\b": "اورنگ‌زیب (عالمگیر)",
    r"\bAkbar\b": "اکبر شاه",
    r"\bJahangir\b": "جهانگیر شاه",
    r"\bShah Jahan\b": "شاه‌جهان",
    r"\bHyderabad\b": "حیدرآباد",
    r"\bDaulatabad\b": "دولت‌آباد",
    r"\bNew Haven\b": "نیوهیون",
    r"\bnew haven\b": "نیوهیون",
    r"\bMiniature\b": "مینیاتور",
    r"\bMiniatures\b": "مینیاتورها",
    r"\bManuscript\b": "نسخه خطی",
    r"\bManuscripts\b": "نسخه‌های خطی",
    r"\bDeccani Painting\b": "نقاشی دکنی",
    r"\bTranquebar\b": "ترانکوبار",
    r"\bChalukya\b": "چالوکیا",
    r"\bMaratha\b": "مراته",
    r"\bHabshi\b": "حبشی",
    r"\bBrahmin\b": "برهمن",
    
    # 2. Correcting common translation artifacts & misspelled terms in Persian output
    r"گولکوندا": "گلکنده",
    r"گولکونده": "گلکنده",
    r"گلکوندا": "گلکنده",
    r"بیدر": "بیدار",
    r"بهمنی": "بهمنیان",
    r"عادل شاهی": "عادل‌شاهیان",
    r"عادل شاه": "عادل‌شاه",
    r"قطب شاهی": "قطب‌شاهیان",
    r"قطب شاه": "قطب‌شاه",
    r"نظام شاهی": "نظام‌شاهیان",
    r"نظام شاه": "نظام‌شاه",
    r"برید شاهی": "بریدشاهیان",
    r"عماد شاهی": "عمادشاهیان",
    r"دکانی": "دکنی",
    r"مغولان هند": "گورکانیان",
    r"مغول ها": "گورکانیان",
    r"مغولان": "گورکانیان",
    r"مغول": "گورکانیان",
    r"نقاشی دکانی": "نقاشی دکنی",
    r"نقاشی دکن": "نقاشی دکنی",
    r"صفویs": "صفویان",
    r"ویژگی پیوند": "انتساب هنری",
    r"پرنده Mynah": "مرغ مینا",
    r"پناهگاه جدید": "نیوهیون",
    r"اشراف در Repast": "نجیب‌زاده در حال صرف غذا",
    r"اونگ آباد": "اورنگ‌آباد",
    r"شاخص": "نمایه",
    r"صلاح خمبا": "سولا خمبا (شانزده ستون)",
    r"میش \(آفتاب\)": "آفتابه",
    r"میش، گلابی شکل": "آفتابه گلابی‌شکل",
    r"پایگاه حقوقی": "پایه حقه (قلیان)",
    r"پایه حکا": "پایه حقه",
    r"پایه حوقا": "پایه حقه",
    r"ظروف رنگین محل بیداری": "ظروف بیدری",
    r"محل بیداری": "بیدار",
    r"bidri ware": "ظروف بیدری",
    r"Bidri ware": "ظروف بیدری",
    r"Bidri Ware": "ظروف بیدری",
    r"\(شانزده ستون\)\s*\(شانزده ستون\)": "(شانزده ستون)",
    r"گربه\s*(\d+)": r"کاتالوگ \1",
    r"گربه‌های\s*(\d+)": r"کاتالوگ‌های \1",
    r"زاهد صوفی": "عارف صوفی",
    r"برس کاری": "قلم‌گیری و قلم‌زنی",
    r"هندلینگ": "پرداخت و ساخت‌وساز",
    
    # Correcting Google Translate hallucinations of broken layout words
    r"بیداری ور": "ظروف بیدری",
    r"بیداری Ware": "ظروف بیدری",
    r"توسط con-\s*تراست": "در مقابل",
    r"con-\s*تراست": "در مقابل",
    r"pos-\s*سفلی": "احتمالاً",
    r"غواصی": "تنوع", # Fix "diversity" -> "diving" -> "غواصی"
}

def translate_paragraph(translator, paragraph):
    """
    Translates a single paragraph using deep-translator's GoogleTranslator.
    """
    if not paragraph.strip():
        return ""
        
    # Handle maximum length of a single request (5000 chars)
    if len(paragraph) > 4500:
        chunks = [paragraph[i:i+4000] for i in range(0, len(paragraph), 4000)]
        t_chunks = []
        for chunk in chunks:
            try:
                res = translator.translate(chunk)
                t_chunks.append(res if res else chunk)
            except Exception as e:
                print(f"Error translating chunk: {e}")
                t_chunks.append(chunk)
        return " ".join(t_chunks)
    else:
        try:
            res = translator.translate(paragraph)
            return res if res else paragraph
        except Exception as e:
            print(f"Error translating paragraph: {e}")
            return paragraph

def translate_page(p_num):
    """
    Translates a single block-separated page.
    """
    p_str = f"{p_num:03d}"
    in_path = os.path.join(INPUT_DIR, f"page_{p_str}.txt")
    out_path = os.path.join(OUTPUT_DIR, f"page_{p_str}_fa.txt")
    
    if not os.path.exists(in_path):
        return f"Page {p_num} not found."
        
    with open(in_path, "r", encoding="utf-8") as f:
        clean_eng = f.read()
        
    # Handle empty files/blank artwork pages
    if not clean_eng.strip() or "contains images/artwork" in clean_eng:
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(f"--- صفحه {p_num} (صفحه تصویری یا فاقد متن) ---")
        return f"Page {p_num} empty/artwork."

    # Step 1: Translate pure English paragraph-by-paragraph (blocks separated by \n\n)
    translator = GoogleTranslator(source='en', target='fa')
    paragraphs = clean_eng.split("\n\n")
    translated_paras = []
    
    for para in paragraphs:
        t_para = translate_paragraph(translator, para)
        translated_paras.append(t_para)
        time.sleep(0.1) # Small rate limiting buffer
        
    translated_content = "\n\n".join(translated_paras)
    
    # Step 2: Apply glossary post-translation
    for pattern, replacement in GLOSSARY.items():
        translated_content = re.sub(pattern, replacement, translated_content)
        
    # Write output
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"--- صفحه {p_num} اصلی ---\n\n" + translated_content)
        
    return f"Page {p_num} completed successfully."

def run_translation(pages):
    print(f"Starting translation pipeline for {len(pages)} pages...")
    sys.stdout.flush()
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(translate_page, p): p for p in pages}
        for future in as_completed(futures):
            p = futures[future]
            try:
                result = future.result()
                print(result)
            except Exception as e:
                print(f"Exception for page {p}: {e}")
            sys.stdout.flush()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        pages_to_run = [int(x) for x in sys.argv[1:]]
        run_translation(pages_to_run)
    else:
        all_pages = list(range(1, 387))
        run_translation(all_pages)
