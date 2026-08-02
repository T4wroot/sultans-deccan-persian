import os
import re
import sys
from refactored_translate_pipeline import GLOSSARY

sys.stdout.reconfigure(encoding='utf-8')

translated_dir = "translated_pages_clean"
files = sorted(os.listdir(translated_dir))

updated_count = 0
for filename in files:
    if not filename.endswith("_fa.txt"):
        continue
        
    filepath = os.path.join(translated_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    original_content = content
    
    # Apply glossary
    for pattern, replacement in GLOSSARY.items():
        content = re.sub(pattern, replacement, content)
        
    # Clean up recursive suffix accumulations
    content = re.sub(r"(بهمن|عادل‌شاه|قطب‌شاه|نظام‌شاه|بریدشاه|عمادشاه|صفو|گورکانی)یان(ان)+", r"\1یان", content)
    content = re.sub(r"\(شانزده ستون\)\s*\(شانزده ستون\)", "(شانزده ستون)", content)
    
    if content != original_content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        updated_count += 1

print(f"Glossary and recursion cleanup applied. Updated {updated_count} translation files locally!")
