import os
import sys
import glob
from googletrans import Translator
import time
import re

translator = Translator()

input_dir = r"c:\Projects\translate\extracted_pages_clean"
output_dir = r"c:\Projects\translate\translated_pages_clean"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

replacements = {
    r"\bBijapur\b": "بیجاپور",
    r"\bGolconda\b": "گلکنده",
    r"\bGolkonda\b": "گلکنده",
    r"\bAhmadnagar\b": "احمدنگر",
    r"\bBidar\b": "بیدار",
    r"\bBerar\b": "برار",
    r"\bBahmani\b": "بهمنیان",
    r"\bAdil Shah\b": "عادل‌شاه",
    r"\bAdil Shahi\b": "عادل‌شاهیان",
    r"\bQutb Shah\b": "قطب‌شاه",
    r"\bQutb Shahi\b": "قطب‌شاهیان",
    r"\bNizam Shah\b": "نظام‌شاه",
    r"\bNizam Shahi\b": "نظام‌شاهیان",
    r"\bBarid Shahi\b": "بریدشاهیان",
    r"\bImad Shahi\b": "عمادشاهیان",
    r"\bDeccani\b": "دکنی",
    r"\bDeccan\b": "دکن",
    r"\bSafavid\b": "صفوی",
    r"\bSafavids\b": "صفویان",
    r"\bMughal\b": "گورکانیان",
    r"\bMughals\b": "مغولان هند",
    r"\bMiniature\b": "مینیاتور",
    r"\bManuscript\b": "نسخه خطی",
    r"\bDeccani Painting\b": "نقاشی دکنی"
}

def translate_text(text):
    # PRE-TRANSLATION REPLACEMENTS (Optional, but let's let Google handle it, then replace in Persian)
    # Actually, it's better to translate first, then replace Persian equivalents if needed,
    # or just replace English first and let Google translate the mixed text?
    # Mixed text translation might fail or have weird grammar.
    pass

def custom_translate(text):
    if not text.strip():
        return text
    
    try:
        # Split by newlines to keep formatting
        paragraphs = text.split('\n\n')
        translated_paragraphs = []
        for p in paragraphs:
            if not p.strip():
                translated_paragraphs.append(p)
                continue
            
            # small sleep to avoid rate limit
            time.sleep(0.5)
            trans = translator.translate(p, dest='fa').text
            
            # Post-translation replacements to fix names
            # Google trans might output things like گالکوندا, etc.
            trans = re.sub(r'گولکوندا|گالکوندا', 'گلکنده', trans)
            trans = re.sub(r'بیجاپور', 'بیجاپور', trans)
            trans = re.sub(r'موگال|مغول', 'گورکانیان', trans)
            trans = re.sub(r'دکان|دکان‌ها', 'دکن', trans)
            trans = re.sub(r'صفویه', 'صفویان', trans)
            
            translated_paragraphs.append(trans)
        
        return '\n\n'.join(translated_paragraphs)
    except Exception as e:
        print(f"Error: {e}")
        return ""

for i in range(262, 331):
    filename = f"page_{i}.txt"
    filepath = os.path.join(input_dir, filename)
    out_filepath = os.path.join(output_dir, f"page_{i}_fa.txt")
    
    if not os.path.exists(filepath):
        print(f"File {filepath} not found.")
        continue
    
    print(f"Translating {filename}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple strategy: just use Google translate and apply a regex post-fix
    trans_content = custom_translate(content)
    
    # Add page marker if not present in translation
    if not trans_content.startswith(f"--- PAGE {i} ---"):
        trans_content = f"--- PAGE {i} ---\n" + trans_content
        
    with open(out_filepath, 'w', encoding='utf-8') as f:
        f.write(trans_content)
    
    print(f"Saved {out_filepath}")

print("Done!")
