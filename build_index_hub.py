import os

output_dir = "responsive_chunks"
chunk_files = sorted(os.listdir(output_dir))
grid_items = []

# First item: Pages 001 to 010
grid_items.append("""
<a href="pages_001_to_010_responsive.html" class="hub-card">
    <div class="hub-badge">جلد و مقدمه</div>
    <div class="hub-title">صفحات ۱ تا ۱۰</div>
    <div class="hub-subtitle">جلد اصلی، شناسنامه، فهرست مطالب و پیشگفتار مدیر موزه</div>
</a>
""")

for f in chunk_files:
    if f.endswith(".html"):
        parts = f.replace("pages_", "").replace("_responsive.html", "").split("_to_")
        start_p = int(parts[0])
        end_p = int(parts[1])
        rel_path = f"responsive_chunks/{f}"
        grid_items.append(f"""
        <a href="{rel_path}" class="hub-card">
            <div class="hub-badge">بسته ۱۰ صفحه‌ای</div>
            <div class="hub-title">صفحات {start_p} تا {end_p}</div>
            <div class="hub-subtitle">متن کامل فارسی آکادمیک و مینیاتورهای مربوطه</div>
        </a>
        """)

orcid_badge = """<a href="https://orcid.org/0009-0005-6825-6728" target="_blank" rel="noopener noreferrer" class="orcid-badge">
<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 256 256">
<path fill="#A6CE39" d="M256 128c0 70.7-57.3 128-128 128S0 198.7 0 128 57.3 0 128 0s128 57.3 128 128z"/>
<path fill="#FFF" d="M86.3 186.2H70.9V79.1h15.4v107.1zM108.9 79.1h41.6c39.6 0 57 28.3 57 53.6 0 27.5-21.5 53.5-56.8 53.5h-41.8V79.1zm15.4 93.3h24.5c34.9 0 41.4-28.9 41.4-39.7 0-16.6-10.7-39.6-41.4-39.6h-24.5v79.3zM78.6 60.1c-5.4 0-9.8-4.4-9.8-9.8s4.4-9.8 9.8-9.8 9.8 4.4 9.8 9.8-4.4 9.8-9.8 9.8z"/>
</svg>
ORCID: 0009-0005-6825-6728
</a>"""

hub_html = f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
<title>سلاطین دکن هند - سامانه مطالعه آکادمیک توانا محمدی</title>
<style>
@font-face {{
    font-family: 'Vazirmatn';
    src: url('Vazirmatn-Regular.ttf') format('truetype');
    font-weight: normal;
}}

:root {{
    --deccan-navy: #0b1329;
    --deccan-card: #152238;
    --deccan-gold: #d97706;
    --deccan-gold-light: #fef3c7;
    --deccan-blue: #38bdf8;
    --deccan-crimson: #9f1239;
    --text-main: #f8fafc;
    --text-muted: #94a3b8;
    --border-color: #27374d;
}}

* {{ box-sizing: border-box; margin: 0; padding: 0; }}

body {{
    font-family: 'Vazirmatn', 'Segoe UI', Tahoma, sans-serif;
    direction: rtl;
    background-color: var(--deccan-navy);
    background-image: 
        radial-gradient(at 0% 0%, rgba(217, 119, 6, 0.12) 0px, transparent 50%),
        radial-gradient(at 100% 100%, rgba(56, 189, 248, 0.12) 0px, transparent 50%);
    color: var(--text-main);
    line-height: 1.8;
    padding: 40px 20px;
    min-height: 100vh;
}}

.container {{
    max-width: 1150px;
    margin: 0 auto;
}}

/* Header Banner - Royal Deccan Museum Style */
.header-box {{
    text-align: center;
    margin-bottom: 45px;
    background: linear-gradient(135deg, rgba(21, 34, 56, 0.9), rgba(11, 19, 41, 0.95));
    border: 2px solid var(--deccan-gold);
    border-radius: 20px;
    padding: 45px 30px;
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.4), inset 0 0 15px rgba(217, 119, 6, 0.15);
    position: relative;
    overflow: hidden;
}}

.header-box::before {{
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0; height: 4px;
    background: linear-gradient(90deg, #d97706, #fbbf24, #38bdf8, #d97706);
}}

.header-title {{
    font-size: 2.4rem;
    font-weight: bold;
    color: #fbbf24;
    text-shadow: 0 2px 10px rgba(251, 191, 36, 0.3);
    margin-bottom: 12px;
}}

.header-subtitle {{
    font-size: 1.35rem;
    color: #f87171;
    font-weight: bold;
    margin-bottom: 18px;
}}

.header-desc {{
    color: var(--text-muted);
    font-size: 1rem;
    max-width: 800px;
    margin: 0 auto 25px auto;
}}

/* Academic Credit Banner */
.academic-credit-card {{
    background: rgba(11, 19, 41, 0.7);
    border: 1px solid rgba(56, 189, 248, 0.3);
    border-radius: 12px;
    padding: 14px 24px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    flex-wrap: wrap;
}}

.academic-credit-card span {{
    font-size: 0.95rem;
    color: var(--text-main);
}}

.academic-credit-card b {{
    color: var(--deccan-blue);
}}

.orcid-badge {{
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    color: #a6ce39;
    font-weight: bold;
    background: rgba(166, 206, 57, 0.15);
    padding: 4px 12px;
    border-radius: 16px;
    border: 1px solid rgba(166, 206, 57, 0.4);
    font-size: 0.88rem;
    transition: all 0.2s ease;
}}

.orcid-badge:hover {{
    background: rgba(166, 206, 57, 0.25);
    transform: scale(1.04);
}}

/* Grid Layout */
.grid-container {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(290px, 1fr));
    gap: 22px;
}}

.hub-card {{
    background: linear-gradient(145deg, #152238, #0e182b);
    border: 1px solid var(--border-color);
    border-radius: 14px;
    padding: 24px;
    text-decoration: none;
    color: var(--text-main);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}}

.hub-card:hover {{
    transform: translateY(-6px);
    border-color: var(--deccan-gold);
    box-shadow: 0 12px 30px rgba(217, 119, 6, 0.25);
}}

.hub-badge {{
    background: rgba(217, 119, 6, 0.15);
    color: #fbbf24;
    font-size: 0.82rem;
    font-weight: bold;
    padding: 4px 12px;
    border-radius: 12px;
    border: 1px solid rgba(217, 119, 6, 0.3);
    width: fit-content;
    margin-bottom: 14px;
}}

.hub-title {{
    font-size: 1.25rem;
    font-weight: bold;
    color: var(--deccan-blue);
    margin-bottom: 8px;
}}

.hub-subtitle {{
    font-size: 0.9rem;
    color: var(--text-muted);
}}

.footer-credit {{
    text-align: center;
    margin-top: 60px;
    padding-top: 25px;
    border-top: 1px dashed var(--border-color);
    color: var(--text-muted);
    font-size: 0.95rem;
}}
</style>
</head>
<body>
<div class="container">
    <div class="header-box">
        <h1 class="header-title">سلاطین دکن هند (۱۵۰۰–۱۷۰۰)</h1>
        <div class="header-subtitle">شکوه و خیال در هنر، معماری و فرهنگ اسلامی</div>
        <p class="header-desc">
            سامانه مطالعه آکادمیک، تعاملی و ریسپانسیو موزه هنر متروپولیتن نیویورک<br>
            شامل ۳۸۶ صفحه کامل، ۳۸۴ مینیاتور و شاهکار هنری دوره دکن
        </p>
        
        <div class="academic-credit-card">
            <span>ترجمه پایان‌نامه دکترا: <b>انوشه طاهری</b></span>
            <span style="opacity: 0.4;">|</span>
            <span>آماده‌سازی سیستم دیجیتال و ناظر فنی: <b>توانا محمدی (Tawana Mohammadi)</b></span>
            {orcid_badge}
        </div>
    </div>
    
    <div class="grid-container">
        {''.join(grid_items)}
    </div>
    
    <div class="footer-credit">
        دیجیتال‌سازی و مهندسی سیستم تعاملی وب: <b>توانا محمدی</b> {orcid_badge}
    </div>
</div>
</body>
</html>
"""

hub_file = "index_reader.html"
with open(hub_file, "w", encoding="utf-8") as f:
    f.write(hub_html)

print("Royal Deccan Theme applied to index_reader.html successfully.")
