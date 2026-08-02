import os
import re
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='en', target='fa')

terms = {
    r'\bBijapur\b': 'بیجاپور',
    r'\bGolkonda\b': 'گلکنده',
    r'\bGolconda\b': 'گلکنده',
    r'\bAhmadnagar\b': 'احمدنگر',
    r'\bBidar\b': 'بیدار',
    r'\bBerar\b': 'برار',
    r'\bBahmanis\b': 'بهمنیان',
    r'\bBahmani\b': 'بهمنیان',
    r'\bAdil Shahi\b': 'عادل‌شاهیان',
    r'\bAdil Shah\b': 'عادل‌شاه',
    r'\bQutb Shahi\b': 'قطب‌شاهیان',
    r'\bQutb Shah\b': 'قطب‌شاه',
    r'\bNizam Shahi\b': 'نظام‌شاهیان',
    r'\bNizam Shah\b': 'نظام‌شاه',
    r'\bBarid Shahi\b': 'بریدشاهیان',
    r'\bImad Shahi\b': 'عمادشاهیان',
    r'\bDeccani Painting\b': 'نقاشی دکنی',
    r'\bDeccani\b': 'دکنی',
    r'\bSafavids\b': 'صفویان',
    r'\bSafavid\b': 'صفوی',
    r'\bMughals\b': 'گورکانیان',
    r'\bMughal\b': 'گورکانیان',
    r'\bMiniatures\b': 'مینیاتورها',
    r'\bMiniature\b': 'مینیاتور',
    r'\bManuscripts\b': 'نسخه‌های خطی',
    r'\bManuscript\b': 'نسخه خطی',
}

def replace_terms(text):
    for pattern, replacement in terms.items():
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    return text

def translate_chunked(text):
    paragraphs = text.split('\n')
    translated = []
    for p in paragraphs:
        if not p.strip():
            translated.append('')
            continue
        if len(p) > 4000:
            chunks = [p[i:i+4000] for i in range(0, len(p), 4000)]
            t_p = ""
            for chunk in chunks:
                try:
                    t_p += translator.translate(chunk) + " "
                except Exception as e:
                    t_p += chunk + " "
            translated.append(t_p.strip())
        else:
            try:
                t = translator.translate(p)
                translated.append(t if t else p)
            except Exception as e:
                translated.append(p)
    return '\n'.join(translated)

in_dir = 'c:/Projects/translate/extracted_pages_clean'
out_dir = 'c:/Projects/translate/translated_pages_clean'
os.makedirs(out_dir, exist_ok=True)

for i in range(66, 131):
    filename = f'page_{i:03d}.txt'
    in_path = os.path.join(in_dir, filename)
    out_path = os.path.join(out_dir, f'page_{i:03d}_fa.txt')
    
    if os.path.exists(in_path):
        if os.path.exists(out_path):
            continue
        with open(in_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if not content.strip():
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(content)
            continue
            
        print(f"Translating {filename}...")
        mixed_content = replace_terms(content)
        persian_content = translate_chunked(mixed_content)
        
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(persian_content)
            
print("Translation complete!")
