import os
from deep_translator import GoogleTranslator
import time
import sys

def translate_text(text):
    if not text.strip():
        return text
    
    # deep_translator has a limit of 5000 chars per request. We will chunk by paragraphs or sentences if needed.
    translator = GoogleTranslator(source='en', target='fa')
    
    chunks = []
    current_chunk = ""
    # sometimes lines are very long, we might need a finer split if len(line) > 4000, but let's assume it's normal text
    for line in text.split('\n'):
        if len(current_chunk) + len(line) + 1 < 4000:
            current_chunk += line + "\n"
        else:
            chunks.append(current_chunk)
            current_chunk = line + "\n"
    if current_chunk:
        chunks.append(current_chunk)
        
    translated_text = ""
    for chunk in chunks:
        if chunk.strip():
            try:
                res = translator.translate(chunk)
                if res:
                    translated_text += res + "\n"
            except Exception as e:
                print(f"Error translating chunk: {e}")
                translated_text += chunk + "\n"
        else:
            translated_text += "\n"
            
    # Terminology replacements (mostly English terms translated directly, or fix Persian outputs)
    replacements = {
        "Bijapur": "بیجاپور",
        "Golconda": "گلکنده",
        "Golkonda": "گلکنده",
        "Ahmadnagar": "احمدنگر",
        "Bidar": "بیدار",
        "Berar": "برار",
        "Bahmani": "بهمنیان",
        "Adil Shah": "عادل‌شاه",
        "Adil Shahi": "عادل‌شاهیان",
        "Qutb Shah": "قطب‌شاه",
        "Qutb Shahi": "قطب‌شاهیان",
        "Nizam Shah": "نظام‌شاه",
        "Nizam Shahi": "نظام‌شاهیان",
        "Barid Shahi": "بریدشاهیان",
        "Imad Shahi": "عمادشاهیان",
        "Deccani": "دکنی",
        "Safavid": "صفوی",
        "Mughal": "گورکانیان",
        "Miniature": "مینیاتور",
        "Manuscript": "نسخه خطی",
        "Deccani Painting": "نقاشی دکنی",
        "بیجاپور": "بیجاپور",
        "گولکوندا": "گلکنده",
        "گولکونده": "گلکنده",
        "گلکوندا": "گلکنده",
        "بیدر": "بیدار",
        "بهمنی": "بهمنیان",
        "عادل شاهی": "عادل‌شاهیان",
        "عادل شاه": "عادل‌شاه",
        "قطب شاهی": "قطب‌شاهیان",
        "قطب شاه": "قطب‌شاه",
        "نظام شاهی": "نظام‌شاهیان",
        "نظام شاه": "نظام‌شاه",
        "برید شاهی": "بریدشاهیان",
        "عماد شاهی": "عمادشاهیان",
        "دکانی": "دکنی",
        "مغولان هند": "گورکانیان",
        "مغول": "گورکانیان",
        "نقاشی دکانی": "نقاشی دکنی",
    }
    
    for k, v in replacements.items():
        translated_text = translated_text.replace(k, v)
        
    return translated_text

def main():
    input_dir = 'extracted_pages_clean'
    output_dir = 'translated_pages_clean'
    
    os.makedirs(output_dir, exist_ok=True)
    
    for i in range(331, 387):
        in_path = os.path.join(input_dir, f'page_{i}.txt')
        out_path = os.path.join(output_dir, f'page_{i}_fa.txt')
        
        if not os.path.exists(in_path):
            print(f"File {in_path} not found.")
            sys.stdout.flush()
            continue
            
        print(f"Translating {in_path}...")
        sys.stdout.flush()
        with open(in_path, 'r', encoding='utf-8') as f:
            text = f.read()
            
        translated = translate_text(text)
        
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(translated)
        
        time.sleep(0.5)

if __name__ == "__main__":
    main()
