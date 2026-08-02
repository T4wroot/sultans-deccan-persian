import fitz
import re
import os

pdf_path = "c:/Projects/translate/Sultans_of_Deccan_India_1500_1700.pdf"
output_dir = "extracted_pages_clean"
os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(pdf_path)
total_pages = len(doc)

def clean_block_text(text):
    # Split text into lines
    lines = [l.strip() for l in text.splitlines()]
    
    # Filter lines
    cleaned_lines = []
    for line in lines:
        if not line:
            continue
        # Skip decorative lines (consisting of only F, spaces, or hyphens)
        if re.match(r'^[F\s\-]+$', line) or "FGFG" in line:
            continue
        cleaned_lines.append(line)
        
    if not cleaned_lines:
        return ""
        
    # Merge lines, resolving hyphens
    merged_text = ""
    for line in cleaned_lines:
        if not merged_text:
            merged_text = line
        else:
            if merged_text.endswith("-"):
                merged_text = merged_text[:-1] + line
            else:
                merged_text += " " + line
                
    return merged_text

print("Extracting block-based clean text for all pages...")
for i in range(total_pages):
    pnum = i + 1
    page = doc[i]
    blocks = page.get_text("blocks")
    
    cleaned_blocks = []
    for block in blocks:
        # Ignore image blocks (block_type == 1)
        if len(block) > 6 and block[6] == 1:
            continue
            
        block_text = block[4].strip()
        if not block_text:
            continue
            
        # Clean block text (lines, hyphens, decorative Fs)
        clean_txt = clean_block_text(block_text)
        if not clean_txt:
            continue
            
        # Ignore standalone page numbers
        if re.match(r'^\d+$', clean_txt) or re.match(r'^[ivxldc]+$', clean_txt, re.IGNORECASE):
            continue
            
        # Ignore running headers/footers
        lower_txt = clean_txt.lower()
        if any(h in lower_txt for h in [
            "a history of the deccan",
            "richard m. eaton",
            "sultans of deccan india",
            "opulence and fantasy",
            "navina najat haidar",
            "marika sardar"
        ]) and len(clean_txt) < 80: # running headers are short
            continue
            
        cleaned_blocks.append(clean_txt)
        
    # Reconstruct Drop Caps
    final_blocks = []
    j = 0
    while j < len(cleaned_blocks):
        block = cleaned_blocks[j]
        # Check if block is a single uppercase letter
        if len(block) == 1 and block.isupper() and j + 1 < len(cleaned_blocks):
            next_block = cleaned_blocks[j + 1]
            # Merge them if next block starts with a lowercase letter
            if next_block and next_block[0].islower():
                block = block + next_block
                j += 1 # skip next block
        final_blocks.append(block)
        j += 1
        
    out_path = os.path.join(output_dir, f"page_{pnum:03d}.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        if final_blocks:
            f.write("\n\n".join(final_blocks))
        else:
            f.write(f"[Page {pnum} contains images/artwork without text]")
            
    if pnum % 50 == 0 or pnum == total_pages:
        print(f"Extracted clean block-based text for page {pnum}/{total_pages}")
