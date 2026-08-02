import os
import glob
import base64
import re

trans_dir = "translated_pages_clean"
output_dir = "responsive_chunks"
os.makedirs(output_dir, exist_ok=True)

# Base64 fonts
with open("Vazirmatn-Regular.ttf", "rb") as f:
    vazir_reg_b64 = base64.b64encode(f.read()).decode('utf-8')

with open("Vazirmatn-Bold.ttf", "rb") as f:
    vazir_bold_b64 = base64.b64encode(f.read()).decode('utf-8')

orcid_svg = """<a href="https://orcid.org/0009-0005-6825-6728" target="_blank" rel="noopener noreferrer" style="text-decoration: none; display: inline-flex; align-items: center; gap: 4px; color: #a6ce39; font-weight: bold; background: rgba(166, 206, 57, 0.1); padding: 2px 8px; border-radius: 12px; border: 1px solid rgba(166, 206, 57, 0.3); font-size: 0.82rem; margin-right: 6px;">
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 256 256">
<path fill="#A6CE39" d="M256 128c0 70.7-57.3 128-128 128S0 198.7 0 128 57.3 0 128 0s128 57.3 128 128z"/>
<path fill="#FFF" d="M86.3 186.2H70.9V79.1h15.4v107.1zM108.9 79.1h41.6c39.6 0 57 28.3 57 53.6 0 27.5-21.5 53.5-56.8 53.5h-41.8V79.1zm15.4 93.3h24.5c34.9 0 41.4-28.9 41.4-39.7 0-16.6-10.7-39.6-41.4-39.6h-24.5v79.3zM78.6 60.1c-5.4 0-9.8-4.4-9.8-9.8s4.4-9.8 9.8-9.8 9.8 4.4 9.8 9.8-4.4 9.8-9.8-9.8z"/>
</svg>
ORCID: 0009-0005-6825-6728
</a>"""

def parse_lines_to_html(lines):
    # Step 1: Join fragmented lines into coherent blocks
    blocks = []
    curr_block = []
    
    for l in lines:
        l_str = l.strip()
        if not l_str or l_str.startswith("---") or l_str.startswith("صفحه"):
            if curr_block:
                blocks.append(" ".join(curr_block))
                curr_block = []
            continue
            
        is_cat_hdr = re.match(r"^(\d{1,3}\s+|گربه\s*\d+|کاتالوگ\s*\d+)", l_str) and len(l_str) < 65
        is_meta = any(k in l_str for k in ["منسوب به", "حدود", "جوهر،", "آبرنگ", "موزه", "کتابخانه", "مجموعه", "کاغذ", "سانتی متر", "اینچ"]) and (len(l_str) < 130 or "موزه" in l_str or "اینچ" in l_str)
        is_heading = len(l_str) < 35 and not l_str.endswith(".") and not any(c.isdigit() for c in l_str[:4])
        
        if is_cat_hdr or is_meta or is_heading:
            if curr_block:
                blocks.append(" ".join(curr_block))
                curr_block = []
            blocks.append(l_str)
        else:
            curr_block.append(l_str)
            
    if curr_block:
        blocks.append(" ".join(curr_block))

    # Step 2: Convert blocks to clean HTML elements
    body_html = ""
    for block in blocks:
        block_str = block.strip()
        if not block_str:
            continue
            
        if re.match(r"^(\d{1,3}\s+|گربه\s*\d+|کاتالوگ\s*\d+)", block_str) and len(block_str) < 65:
            body_html += f'<div class="catalog-header"><span class="cat-num-badge">شناسه اثر</span> <span class="cat-title">{block_str}</span></div>\n'
        elif any(k in block_str for k in ["منسوب به", "حدود", "جوهر،", "آبرنگ", "موزه", "کتابخانه", "مجموعه", "کاغذ", "سانتی متر", "اینچ"]) and (len(block_str) < 130 or "موزه" in block_str or "اینچ" in block_str):
            body_html += f'<div class="catalog-meta">{block_str}</div>\n'
        elif len(block_str) < 35 and not block_str.endswith(".") and not any(char.isdigit() for char in block_str[:4]):
            body_html += f'<h2 class="chapter-heading">{block_str}</h2>\n'
        else:
            body_html += f'<p>{block_str}</p>\n'
            
    return body_html

def build_chunk(start_pg, end_pg):
    cards_html = []
    toc_items = []
    
    for p_num in range(start_pg, end_pg + 1):
        p_str = f"{p_num:03d}"
        txt_path = os.path.join(trans_dir, f"page_{p_str}_fa.txt")
        if not os.path.exists(txt_path):
            continue
            
        with open(txt_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            
        img_pattern = os.path.join("extracted_images", f"page_{p_str}_img_*.jpeg")
        imgs = glob.glob(img_pattern)
        img_html_str = ""
        for img_path in imgs:
            with open(img_path, "rb") as img_f:
                b64 = base64.b64encode(img_f.read()).decode('utf-8')
                img_html_str += f'<img src="data:image/jpeg;base64,{b64}" class="cover-image" alt="تصویر صفحه {p_num}">\n'
                
        body_html = parse_lines_to_html(lines)
                
        card_content = f"""
        <article class="reader-card" id="page-{p_num}">
            <div class="page-badge">صفحه {p_num} از ۳۸۶</div>
            {img_html_str}
            {body_html}
        </article>
        """
        cards_html.append(card_content)
        toc_items.append(f'<a href="#page-{p_num}" class="toc-item" onclick="closeSidebar()">صفحه {p_num}</a>')
        
    chunk_html = f"""<!DOCTYPE html>
<html lang="fa" dir="rtl" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
<title>ترجمه سلاطین دکن هند - صفحات {start_pg} تا {end_pg}</title>
<style>
@font-face {{
    font-family: 'Vazirmatn';
    src: url('data:font/ttf;charset=utf-8;base64,{vazir_reg_b64}') format('truetype');
    font-weight: normal;
}}
@font-face {{
    font-family: 'Vazirmatn';
    src: url('data:font/ttf;charset=utf-8;base64,{vazir_bold_b64}') format('truetype');
    font-weight: bold;
}}
html {{ scroll-behavior: smooth; }}
:root {{
    --bg-main: #0f172a; --bg-card: #1e293b; --bg-sidebar: #1e293b; --border-color: #334155;
    --text-main: #f8fafc; --text-muted: #94a3b8; --accent-blue: #38bdf8; --accent-gold: #fbbf24;
    --accent-red: #f87171; --font-size-base: 18px; --content-max-width: 860px;
}}
[data-theme="light"] {{
    --bg-main: #f1f5f9; --bg-card: #ffffff; --bg-sidebar: #ffffff; --border-color: #cbd5e1;
    --text-main: #0f172a; --text-muted: #64748b; --accent-blue: #0284c7; --accent-gold: #d97706; --accent-red: #dc2626;
}}
[data-theme="sepia"] {{
    --bg-main: #f5e6c8; --bg-card: #fdf6e3; --bg-sidebar: #fdf6e3; --border-color: #e6d3a7;
    --text-main: #433422; --text-muted: #76634d; --accent-blue: #854d0e; --accent-gold: #b45309; --accent-red: #9f1239;
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }}
body {{
    font-family: 'Vazirmatn', 'Segoe UI', Tahoma, sans-serif; direction: rtl;
    background-color: var(--bg-main); color: var(--text-main); font-size: var(--font-size-base);
    line-height: 2.15; transition: background-color 0.3s, color 0.3s; overflow-x: hidden;
}}
.top-navbar {{
    position: fixed; top: 0; left: 0; right: 0; height: 65px; background-color: var(--bg-sidebar);
    border-bottom: 1px solid var(--border-color); display: flex; align-items: center; justify-content: space-between;
    padding: 0 20px; z-index: 1000; box-shadow: 0 4px 15px rgba(0,0,0,0.12);
}}
.navbar-brand {{ display: flex; align-items: center; gap: 12px; font-weight: bold; font-size: 1.15rem; color: var(--accent-blue); }}
.nav-btn {{
    background: rgba(56, 189, 248, 0.08); border: 1px solid var(--border-color); color: var(--text-main);
    padding: 8px 14px; border-radius: 8px; cursor: pointer; font-family: inherit; font-size: 0.92rem; font-weight: bold;
    display: flex; align-items: center; gap: 6px; transition: all 0.2s ease;
}}
.nav-btn:hover {{ background-color: var(--accent-blue); color: #ffffff; border-color: var(--accent-blue); }}
.settings-modal {{
    position: fixed; top: 75px; left: 20px; width: 320px; background-color: var(--bg-card);
    border: 1px solid var(--border-color); border-radius: 14px; padding: 22px; box-shadow: 0 15px 35px rgba(0,0,0,0.25);
    z-index: 1100; display: none; animation: fadeIn 0.2s ease;
}}
.settings-modal.active {{ display: block; }}
@keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(-10px); }} to {{ opacity: 1; transform: translateY(0); }} }}
.setting-group {{ margin-bottom: 20px; }}
.setting-label {{ font-size: 0.9rem; font-weight: bold; color: var(--accent-gold); margin-bottom: 10px; display: flex; justify-content: space-between; align-items: center; }}
.theme-options {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; }}
.theme-pill {{ border: 2px solid var(--border-color); padding: 8px; border-radius: 8px; text-align: center; cursor: pointer; font-size: 0.85rem; font-weight: bold; transition: all 0.2s; }}
.theme-pill.active {{ border-color: var(--accent-blue); background-color: rgba(56, 189, 248, 0.15); color: var(--accent-blue); }}
.theme-pill-dark {{ background: #0f172a; color: #f8fafc; }}
.theme-pill-light {{ background: #ffffff; color: #0f172a; }}
.theme-pill-sepia {{ background: #fdf6e3; color: #433422; }}
.font-slider-container {{ display: flex; align-items: center; gap: 12px; }}
.font-btn {{ background: var(--bg-main); border: 1px solid var(--border-color); color: var(--text-main); width: 36px; height: 36px; border-radius: 8px; cursor: pointer; font-size: 1.1rem; font-weight: bold; display: flex; align-items: center; justify-content: center; }}
.font-slider {{ flex: 1; height: 6px; border-radius: 3px; accent-color: var(--accent-blue); cursor: pointer; }}
.app-container {{ display: flex; margin-top: 65px; min-height: calc(100vh - 65px); }}
.sidebar {{
    width: 330px; background-color: var(--bg-sidebar); border-left: 1px solid var(--border-color);
    height: calc(100vh - 65px); position: fixed; top: 65px; right: 0; overflow-y: auto; padding: 22px;
    transition: transform 0.3s ease; z-index: 900;
}}
.sidebar-title {{ font-size: 1.1rem; font-weight: bold; color: var(--accent-gold); margin-bottom: 15px; border-bottom: 2px solid var(--border-color); padding-bottom: 10px; }}
.toc-item {{ display: block; padding: 10px 14px; color: var(--text-main); text-decoration: none; border-radius: 8px; margin-bottom: 6px; font-size: 0.95rem; transition: background 0.2s; }}
.toc-item:hover, .toc-item.active {{ background-color: rgba(56, 189, 248, 0.15); color: var(--accent-blue); font-weight: bold; }}
.main-content {{ flex: 1; margin-right: 330px; padding: 35px 20px 80px 20px; display: flex; flex-direction: column; align-items: center; transition: margin-right 0.3s; }}
.reader-card {{ width: 100%; max-width: var(--content-max-width); background-color: var(--bg-card); border: 1px solid var(--border-color); border-radius: 14px; padding: 45px; margin-bottom: 35px; box-shadow: 0 4px 25px rgba(0,0,0,0.15); }}
.cover-image {{ max-width: 100%; height: auto; border-radius: 12px; margin: 20px auto; display: block; box-shadow: 0 10px 30px rgba(0,0,0,0.35); }}
.page-badge {{ background-color: rgba(56, 189, 248, 0.1); color: var(--accent-blue); border-right: 4px solid var(--accent-blue); padding: 8px 16px; font-weight: bold; font-size: 0.95rem; margin-bottom: 25px; border-radius: 0 8px 8px 0; }}

/* Museum Catalog Entry Formatting */
.catalog-header {{
    background: linear-gradient(90deg, rgba(217, 119, 6, 0.18), rgba(56, 189, 248, 0.05));
    border-right: 4px solid var(--accent-gold);
    padding: 10px 16px;
    border-radius: 8px;
    margin: 25px 0 12px 0;
    display: flex;
    align-items: center;
    gap: 10px;
}}
.cat-num-badge {{
    background: var(--accent-gold);
    color: #0f172a;
    font-weight: bold;
    font-size: 0.85rem;
    padding: 3px 10px;
    border-radius: 6px;
}}
.cat-title {{
    font-size: 1.2rem;
    font-weight: bold;
    color: var(--accent-blue);
}}
.catalog-meta {{
    font-size: 0.92rem;
    color: var(--text-muted);
    background: rgba(15, 23, 42, 0.4);
    border-right: 2px solid var(--border-color);
    padding: 6px 14px;
    margin-bottom: 8px;
    border-radius: 0 6px 6px 0;
    line-height: 1.7;
}}

h2.chapter-heading {{ font-size: 1.5rem; color: var(--accent-blue); border-bottom: 1px solid var(--border-color); padding-bottom: 8px; margin: 25px 0 15px 0; }}
p {{ margin-bottom: 18px; text-align: justify; line-height: 2.1; }}
.subtle-credit {{ font-size: 0.88rem; color: var(--text-muted); text-align: center; margin-top: 25px; padding-top: 15px; border-top: 1px dashed var(--border-color); }}
.subtle-credit b {{ color: var(--accent-blue); }}
.mobile-controls {{ position: fixed; bottom: 0; left: 0; right: 0; height: 60px; background-color: var(--bg-sidebar); border-top: 1px solid var(--border-color); display: flex; align-items: center; justify-content: space-around; padding: 0 10px; z-index: 1000; }}
@media (max-width: 1024px) {{
    .sidebar {{ transform: translateX(100%); }}
    .sidebar.open {{ transform: translateX(0); }}
    .main-content {{ margin-right: 0; padding: 20px 12px 75px 12px; }}
    .reader-card {{ padding: 26px 16px; border-radius: 10px; }}
}}
@media (max-width: 480px) {{
    body {{ font-size: 17px; line-height: 2.1; }}
    .reader-card {{ padding: 20px 14px; }}
    .top-navbar {{ padding: 0 12px; }}
    .settings-modal {{ left: 10px; right: 10px; width: auto; }}
}}
</style>
</head>
<body>
<header class="top-navbar">
    <div class="navbar-brand">
        <button class="nav-btn" onclick="toggleSidebar()" title="فهرست">📑 فهرست</button>
        <span>سلاطین دکن هند (صفحات {start_pg} تا {end_pg})</span>
    </div>
    <div class="navbar-actions">
        <button class="nav-btn" onclick="toggleSettingsModal()" title="تنظیمات مطالعه">⚙️ تنظیمات مطالعه</button>
    </div>
</header>
<div class="settings-modal" id="settingsModal">
    <div class="setting-group">
        <div class="setting-label"><span>🎨 تم رنگی مطالعه</span></div>
        <div class="theme-options">
            <div class="theme-pill theme-pill-dark active" onclick="setTheme('dark')">🌙 تاریک</div>
            <div class="theme-pill theme-pill-light" onclick="setTheme('light')">☀️ روشن</div>
            <div class="theme-pill theme-pill-sepia" onclick="setTheme('sepia')">📜 سپیا</div>
        </div>
    </div>
    <div class="setting-group">
        <div class="setting-label"><span>📏 اندازه قلم (فونت)</span><span id="fontSizeVal" style="color: var(--accent-blue);">18px</span></div>
        <div class="font-slider-container">
            <button class="font-btn" onclick="stepFontSize(-1)">A⁻</button>
            <input type="range" class="font-slider" id="fontSlider" min="14" max="26" value="18" oninput="updateFontSize(this.value)">
            <button class="font-btn" onclick="stepFontSize(1)">A⁺</button>
        </div>
    </div>
</div>
<div class="app-container">
    <aside class="sidebar" id="sidebar">
        <div class="sidebar-title">📑 فهرست صفحات ({start_pg} تا {end_pg})</div>
        {''.join(toc_items)}
    </aside>
    <main class="main-content">
        {''.join(cards_html)}
        <div class="subtle-credit">
            آماده‌سازی سیستم تعاملی وب، زیرساخت دیجیتال و ناظر فنی: <b>توانا محمدی (Tawana Mohammadi)</b> {orcid_svg} | ترجمه انوشه طاهری (پایان‌نامه دکترا)
        </div>
    </main>
</div>
<div class="mobile-controls">
    <button class="nav-btn" onclick="toggleSidebar()">📑 فهرست</button>
    <button class="nav-btn" onclick="toggleSettingsModal()">⚙️ تنظیمات</button>
    <button class="nav-btn" onclick="window.scrollTo({{top: 0, behavior: 'smooth'}})">⬆ بالا</button>
</div>
<script>
function toggleSidebar() {{ document.getElementById('sidebar').classList.toggle('open'); document.getElementById('settingsModal').classList.remove('active'); }}
function closeSidebar() {{ document.getElementById('sidebar').classList.remove('open'); }}
function toggleSettingsModal() {{ document.getElementById('settingsModal').classList.toggle('active'); document.getElementById('sidebar').classList.remove('open'); }}
function updateFontSize(val) {{ document.body.style.fontSize = val + 'px'; document.getElementById('fontSizeVal').innerText = val + 'px'; document.getElementById('fontSlider').value = val; }}
function stepFontSize(delta) {{ const current = parseInt(document.getElementById('fontSlider').value); const next = Math.max(14, Math.min(26, current + delta)); updateFontSize(next); }}
function setTheme(themeName) {{
    document.documentElement.setAttribute('data-theme', themeName);
    document.querySelectorAll('.theme-pill').forEach(pill => pill.classList.remove('active'));
    if (themeName === 'dark') document.querySelectorAll('.theme-pill-dark')[0].classList.add('active');
    if (themeName === 'light') document.querySelectorAll('.theme-pill-light')[0].classList.add('active');
    if (themeName === 'sepia') document.querySelectorAll('.theme-pill-sepia')[0].classList.add('active');
}}
</script>
</body>
</html>
"""
    out_file = os.path.join(output_dir, f"pages_{start_pg:03d}_to_{end_pg:03d}_responsive.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(chunk_html)
    return out_file

for start_pg in range(11, 387, 10):
    end_pg = min(start_pg + 9, 386)
    build_chunk(start_pg, end_pg)

print("Joined all paragraph lines and updated all 38 chunks successfully.")
