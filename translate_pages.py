import os
import re
import sys
from deep_translator import GoogleTranslator

def translate_text(text):
    if not text.strip():
        return ""
    
    translator = GoogleTranslator(source='en', target='fa')
    
    # Pre-process text to avoid translation issues for specific names
    text = text.replace("Bijapur", "بیجاپور")
    text = text.replace("Golconda", "گلکنده")
    text = text.replace("Golkonda", "گلکنده")
    text = text.replace("Ahmadnagar", "احمدنگر")
    text = text.replace("Bidar", "بیدار")
    text = text.replace("Berar", "برار")
    text = text.replace("Bahmani", "بهمنیان")
    text = text.replace("Adil Shah", "عادل‌شاه")
    text = text.replace("Adil Shahi", "عادل‌شاهیان")
    text = text.replace("Qutb Shah", "قطب‌شاه")
    text = text.replace("Qutb Shahi", "قطب‌شاهیان")
    text = text.replace("Nizam Shah", "نظام‌شاه")
    text = text.replace("Nizam Shahi", "نظام‌شاهیان")
    text = text.replace("Barid Shahi", "بریدشاهیان")
    text = text.replace("Imad Shahi", "عمادشاهیان")
    text = text.replace("Deccani", "دکنی")
    text = text.replace("Safavid", "صفوی")
    text = text.replace("Safavids", "صفویان")
    text = text.replace("Mughal", "گورکانیان")
    text = text.replace("Mughals", "مغولان هند")
    text = text.replace("Miniature", "مینیاتور")
    text = text.replace("Manuscript", "نسخه خطی")
    text = text.replace("Deccani Painting", "نقاشی دکنی")
    
    # Send the whole file to Google Translate (up to 5000 chars)
    # The max file length is ~3000 chars, so this is safe.
    try:
        final_text = translator.translate(text)
    except Exception as e:
        print(f"Error translating: {e}")
        return text
    
    # Fix any remaining translation artifacts
    replacements = {
        'مغول': 'گورکانیان',
        'مغول ها': 'گورکانیان',
        'مغولان': 'گورکانیان',
        'عادل شاهی': 'عادل‌شاهیان',
        'قطب شاهی': 'قطب‌شاهیان',
        'نظام شاهی': 'نظام‌شاهیان',
        'برید شاهی': 'بریدشاهیان',
        'عماد شاهی': 'عمادشاهیان',
        'نقاشی دکن': 'نقاشی دکنی',
        'صفویs': 'صفویان'
    }
    for k, v in replacements.items():
        final_text = final_text.replace(k, v)
        
    return final_text

def main():
    in_dir = "extracted_pages_clean"
    out_dir = "translated_pages_clean"
    os.makedirs(out_dir, exist_ok=True)
    
    for i in range(131, 191):
        filename = f"page_{i}.txt"
        in_path = os.path.join(in_dir, filename)
        out_path = os.path.join(out_dir, f"page_{i}_fa.txt")
        
        if not os.path.exists(in_path):
            continue
            
        with open(in_path, 'r', encoding='utf-8') as f:
            text = f.read()
            
        # Avoid char limit issue by splitting in half if extremely large, but they are all < 5000
        if len(text) > 4900:
            part1 = translate_text(text[:4500])
            part2 = translate_text(text[4500:])
            translated = part1 + part2
        else:
            translated = translate_text(text)
        
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(translated)
            
        print(f"Translated {filename} -> {out_path}")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
