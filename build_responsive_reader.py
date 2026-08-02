import os
import base64

cover_img_path = os.path.join("extracted_images", "page_001_img_1.jpeg")
if os.path.exists(cover_img_path):
    with open(cover_img_path, "rb") as f:
        cover_b64 = base64.b64encode(f.read()).decode('utf-8')
    cover_img_html = f'<img src="data:image/jpeg;base64,{cover_b64}" class="cover-image" alt="جلد اصلی کتاب سلاطین دکن">'
else:
    cover_img_html = ""

# Base64 fonts
with open("Vazirmatn-Regular.ttf", "rb") as f:
    vazir_reg_b64 = base64.b64encode(f.read()).decode('utf-8')

with open("Vazirmatn-Bold.ttf", "rb") as f:
    vazir_bold_b64 = base64.b64encode(f.read()).decode('utf-8')

html_content = f"""<!DOCTYPE html>
<html lang="fa" dir="rtl" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
<title>ترجمه سلاطین دکن هند - نسخه دیجیتال توانا محمدی</title>
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

html {{
    scroll-behavior: smooth;
}}

:root {{
    --bg-main: #0f172a;
    --bg-card: #1e293b;
    --bg-sidebar: #1e293b;
    --border-color: #334155;
    --text-main: #f8fafc;
    --text-muted: #94a3b8;
    --accent-blue: #38bdf8;
    --accent-gold: #fbbf24;
    --accent-red: #f87171;
    --font-size-base: 18px;
    --content-max-width: 860px;
}}

[data-theme="light"] {{
    --bg-main: #f1f5f9;
    --bg-card: #ffffff;
    --bg-sidebar: #ffffff;
    --border-color: #cbd5e1;
    --text-main: #0f172a;
    --text-muted: #64748b;
    --accent-blue: #0284c7;
    --accent-gold: #d97706;
    --accent-red: #dc2626;
}}

[data-theme="sepia"] {{
    --bg-main: #f5e6c8;
    --bg-card: #fdf6e3;
    --bg-sidebar: #fdf6e3;
    --border-color: #e6d3a7;
    --text-main: #433422;
    --text-muted: #76634d;
    --accent-blue: #854d0e;
    --accent-gold: #b45309;
    --accent-red: #9f1239;
}}

* {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    -webkit-tap-highlight-color: transparent;
}}

body {{
    font-family: 'Vazirmatn', 'Segoe UI', Tahoma, sans-serif;
    direction: rtl;
    background-color: var(--bg-main);
    color: var(--text-main);
    font-size: var(--font-size-base);
    line-height: 2.15;
    transition: background-color 0.3s, color 0.3s;
    overflow-x: hidden;
}}

/* Top Navigation Bar */
.top-navbar {{
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 65px;
    background-color: var(--bg-sidebar);
    border-bottom: 1px solid var(--border-color);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 20px;
    z-index: 1000;
    box-shadow: 0 4px 15px rgba(0,0,0,0.12);
}}

.navbar-brand {{
    display: flex;
    align-items: center;
    gap: 12px;
    font-weight: bold;
    font-size: 1.15rem;
    color: var(--accent-blue);
}}

.navbar-actions {{
    display: flex;
    align-items: center;
    gap: 10px;
}}

.nav-btn {{
    background: rgba(56, 189, 248, 0.08);
    border: 1px solid var(--border-color);
    color: var(--text-main);
    padding: 8px 14px;
    border-radius: 8px;
    cursor: pointer;
    font-family: inherit;
    font-size: 0.92rem;
    font-weight: bold;
    display: flex;
    align-items: center;
    gap: 6px;
    transition: all 0.2s ease;
}}

.nav-btn:hover {{
    background-color: var(--accent-blue);
    color: #ffffff;
    border-color: var(--accent-blue);
}}

/* Reading Settings Modal Popup */
.settings-modal {{
    position: fixed;
    top: 75px;
    left: 20px;
    width: 320px;
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 14px;
    padding: 22px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.25);
    z-index: 1100;
    display: none;
    animation: fadeIn 0.2s ease;
}}

.settings-modal.active {{
    display: block;
}}

@keyframes fadeIn {{
    from {{ opacity: 0; transform: translateY(-10px); }}
    to {{ opacity: 1; transform: translateY(0); }}
}}

.setting-group {{
    margin-bottom: 20px;
}}

.setting-label {{
    font-size: 0.9rem;
    font-weight: bold;
    color: var(--accent-gold);
    margin-bottom: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}}

/* Theme Options Pills */
.theme-options {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 8px;
}}

.theme-pill {{
    border: 2px solid var(--border-color);
    padding: 8px;
    border-radius: 8px;
    text-align: center;
    cursor: pointer;
    font-size: 0.85rem;
    font-weight: bold;
    transition: all 0.2s;
}}

.theme-pill.active {{
    border-color: var(--accent-blue);
    background-color: rgba(56, 189, 248, 0.15);
    color: var(--accent-blue);
}}

.theme-pill-dark {{ background: #0f172a; color: #f8fafc; }}
.theme-pill-light {{ background: #ffffff; color: #0f172a; }}
.theme-pill-sepia {{ background: #fdf6e3; color: #433422; }}

/* Font Size Slider & Controls */
.font-slider-container {{
    display: flex;
    align-items: center;
    gap: 12px;
}}

.font-btn {{
    background: var(--bg-main);
    border: 1px solid var(--border-color);
    color: var(--text-main);
    width: 36px;
    height: 36px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 1.1rem;
    font-weight: bold;
    display: flex;
    align-items: center;
    justify-content: center;
}}

.font-btn:hover {{
    background-color: var(--accent-blue);
    color: #ffffff;
}}

.font-slider {{
    flex: 1;
    height: 6px;
    border-radius: 3px;
    accent-color: var(--accent-blue);
    cursor: pointer;
}}

/* Layout Container */
.app-container {{
    display: flex;
    margin-top: 65px;
    min-height: calc(100vh - 65px);
}}

/* Sidebar Drawer */
.sidebar {{
    width: 330px;
    background-color: var(--bg-sidebar);
    border-left: 1px solid var(--border-color);
    height: calc(100vh - 65px);
    position: fixed;
    top: 65px;
    right: 0;
    overflow-y: auto;
    padding: 22px;
    transition: transform 0.3s ease;
    z-index: 900;
}}

.sidebar-title {{
    font-size: 1.1rem;
    font-weight: bold;
    color: var(--accent-gold);
    margin-bottom: 15px;
    border-bottom: 2px solid var(--border-color);
    padding-bottom: 10px;
}}

.toc-item {{
    display: block;
    padding: 10px 14px;
    color: var(--text-main);
    text-decoration: none;
    border-radius: 8px;
    margin-bottom: 6px;
    font-size: 0.95rem;
    transition: background 0.2s;
}}

.toc-item:hover, .toc-item.active {{
    background-color: rgba(56, 189, 248, 0.15);
    color: var(--accent-blue);
    font-weight: bold;
}}

/* Main Content Area */
.main-content {{
    flex: 1;
    margin-right: 330px;
    padding: 35px 20px 80px 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    transition: margin-right 0.3s;
}}

.reader-card {{
    width: 100%;
    max-width: var(--content-max-width);
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 14px;
    padding: 45px;
    margin-bottom: 35px;
    box-shadow: 0 4px 25px rgba(0,0,0,0.15);
}}

/* Page Components */
.thesis-badge {{
    background-color: rgba(248, 113, 113, 0.15);
    border: 1px solid var(--accent-red);
    color: var(--accent-red);
    font-weight: bold;
    padding: 6px 18px;
    border-radius: 20px;
    display: inline-block;
    font-size: 0.95rem;
    margin-bottom: 20px;
}}

.cover-title {{
    font-size: 2.3rem;
    font-weight: bold;
    color: var(--accent-blue);
    text-align: center;
    line-height: 1.4;
    margin-bottom: 12px;
}}

.cover-subtitle {{
    font-size: 1.25rem;
    color: var(--text-muted);
    text-align: center;
    margin-bottom: 30px;
}}

.cover-image {{
    max-width: 100%;
    height: auto;
    border-radius: 12px;
    margin: 20px auto;
    display: block;
    box-shadow: 0 10px 30px rgba(0,0,0,0.35);
}}

.page-badge {{
    background-color: rgba(56, 189, 248, 0.1);
    color: var(--accent-blue);
    border-right: 4px solid var(--accent-blue);
    padding: 8px 16px;
    font-weight: bold;
    font-size: 0.95rem;
    margin-bottom: 25px;
    border-radius: 0 8px 8px 0;
}}

h1.chapter-heading {{
    font-size: 1.85rem;
    color: var(--accent-blue);
    border-bottom: 2px solid var(--accent-blue);
    padding-bottom: 10px;
    margin: 30px 0 20px 0;
}}

p {{
    margin-bottom: 18px;
    text-align: justify;
}}

/* Interactive Clickable TOC Table */
.toc-list {{
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin-top: 20px;
}}

.clickable-toc-link {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    border-bottom: 1px dashed var(--border-color);
    padding: 12px;
    text-decoration: none;
    color: var(--text-main);
    border-radius: 8px;
    transition: all 0.2s ease;
}}

.clickable-toc-link:hover {{
    background-color: rgba(56, 189, 248, 0.12);
    transform: translateX(-4px);
    color: var(--accent-blue);
}}

.toc-row-title {{
    font-weight: bold;
}}

.toc-row-page {{
    font-weight: bold;
    color: var(--accent-gold);
    font-family: monospace;
    font-size: 1.15rem;
}}

.toc-row-author {{
    font-size: 0.88rem;
    color: var(--text-muted);
    margin-top: 3px;
}}

.subtle-credit {{
    font-size: 0.88rem;
    color: var(--text-muted);
    text-align: center;
    margin-top: 25px;
    padding-top: 15px;
    border-top: 1px dashed var(--border-color);
}}

.subtle-credit b {{
    color: var(--accent-blue);
}}

/* Mobile Sticky Bottom Controls */
.mobile-controls {{
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    height: 60px;
    background-color: var(--bg-sidebar);
    border-top: 1px solid var(--border-color);
    display: flex;
    align-items: center;
    justify-content: space-around;
    padding: 0 10px;
    z-index: 1000;
}}

/* Responsive Breakpoints */
@media (max-width: 1024px) {{
    .sidebar {{
        transform: translateX(100%);
    }}
    .sidebar.open {{
        transform: translateX(0);
    }}
    .main-content {{
        margin-right: 0;
        padding: 20px 12px 75px 12px;
    }}
    .reader-card {{
        padding: 26px 16px;
        border-radius: 10px;
    }}
    .cover-title {{
        font-size: 1.75rem;
    }}
}}

@media (max-width: 480px) {{
    body {{
        font-size: 17px;
        line-height: 2.1;
    }}
    .reader-card {{
        padding: 20px 14px;
    }}
    .top-navbar {{
        padding: 0 12px;
    }}
    .navbar-brand span {{
        font-size: 0.9rem;
    }}
    .settings-modal {{
        left: 10px;
        right: 10px;
        width: auto;
    }}
}}
</style>
</head>
<body>

<!-- Top Navbar -->
<header class="top-navbar">
    <div class="navbar-brand">
        <button class="nav-btn" onclick="toggleSidebar()" title="فهرست مطالب">
            📑 فهرست
        </button>
        <span>سلاطین دکن هند (۱۵۰۰–۱۷۰۰)</span>
    </div>
    
    <div class="navbar-actions">
        <button class="nav-btn" onclick="toggleSettingsModal()" title="تنظیمات مطالعه (فونت و تم)">
            ⚙️ تنظیمات مطالعه
        </button>
    </div>
</header>

<!-- Reading Settings Modal Popup -->
<div class="settings-modal" id="settingsModal">
    <!-- Theme Selection -->
    <div class="setting-group">
        <div class="setting-label">
            <span>🎨 تم رنگی مطالعه</span>
        </div>
        <div class="theme-options">
            <div class="theme-pill theme-pill-dark active" onclick="setTheme('dark')">🌙 تاریک</div>
            <div class="theme-pill theme-pill-light" onclick="setTheme('light')">☀️ روشن</div>
            <div class="theme-pill theme-pill-sepia" onclick="setTheme('sepia')">📜 سپیا</div>
        </div>
    </div>
    
    <!-- Font Size Slider -->
    <div class="setting-group">
        <div class="setting-label">
            <span>📏 اندازه قلم (فونت)</span>
            <span id="fontSizeVal" style="color: var(--accent-blue);">18px</span>
        </div>
        <div class="font-slider-container">
            <button class="font-btn" onclick="stepFontSize(-1)">A⁻</button>
            <input type="range" class="font-slider" id="fontSlider" min="14" max="26" value="18" oninput="updateFontSize(this.value)">
            <button class="font-btn" onclick="stepFontSize(1)">A⁺</button>
        </div>
    </div>
</div>

<div class="app-container">
    <!-- Sidebar TOC Drawer -->
    <aside class="sidebar" id="sidebar">
        <div class="sidebar-title">📑 فهرست مطالب (کلیک‌پذیر)</div>
        <a href="#page-1" class="toc-item active" onclick="closeSidebar()">جلد اصلی پایان‌نامه</a>
        <a href="#page-4" class="toc-item" onclick="closeSidebar()">صفحه شناسنامه و نویسندگان</a>
        <a href="#page-5" class="toc-item" onclick="closeSidebar()">شناسنامه نشر و کپی‌رایت</a>
        <a href="#page-6" class="toc-item" onclick="closeSidebar()">فهرست مطالب کامل (Contents)</a>
        <a href="#page-8" class="toc-item" onclick="closeSidebar()">پیشگفتار مدیر موزه متروپولیتن</a>
    </aside>

    <!-- Main Content Area -->
    <main class="main-content">
        
        <!-- PAGE 1: COVER -->
        <article class="reader-card" id="page-1">
            <div style="text-align: center;">
                <div class="thesis-badge">پایان‌نامه دکترا</div>
                <h1 class="cover-title">سلاطین دکن هند (۱۵۰۰–۱۷۰۰)</h1>
                <div class="cover-subtitle">شکوه و خیال در هنر، معماری و فرهنگ اسلامی</div>
                
                {cover_img_html}
                
                <div style="background: rgba(56, 189, 248, 0.08); border: 1px solid var(--border-color); border-radius: 10px; padding: 22px; margin-top: 25px;">
                    <h3 style="color: var(--accent-blue); margin-bottom: 8px;">عنوان ترجمه و پژوهش آکادمیک:</h3>
                    <h2 style="color: var(--accent-red); margin-bottom: 12px; font-size: 1.45rem;">ترجمه انوشه طاهری - پایان‌نامه دکترا</h2>
                    <p style="text-align: center; color: var(--text-muted); font-size: 0.92rem; margin: 0;">
                        نویسندگان اصلی: ناویینا نجات حیدر و ماریکا سردار (موزه هنر متروپولیتن نیویورک)<br>
                        رشته تاریخ هنر و معماری اسلامی | سال تحصیلی ۱۴۰۵ - ۱۴۰۶
                    </p>
                </div>

                <div class="subtle-credit">
                    🖥️ آماده‌سازی سیستم تعاملی وب، زیرساخت دیجیتال و ناظر فنی: <b>توانا محمدی (Tawana Mohammadi)</b>
                </div>
            </div>
        </article>

        <!-- PAGE 4: TITLE PAGE -->
        <article class="reader-card" id="page-4">
            <div class="page-badge">صفحه ۴ از ۳۸۶ (شناسنامه اثر)</div>
            
            <h1 class="chapter-heading" style="text-align: center; border: none;">
                سلاطین دکن هند (۱۵۰۰–۱۷۰۰)<br>
                <small style="font-size: 1.15rem; color: var(--text-muted);">شکوه و خیال‌پردازی در هنر اسلامی</small>
            </h1>
            
            <p style="text-align: center; font-weight: bold; color: var(--accent-blue); font-size: 1.15rem;">
                نویسندگان اصلی: ناویینا نجات حیدر و ماریکا سردار
            </p>
            
            <div style="background-color: var(--bg-main); padding: 22px; border-radius: 10px; border: 1px solid var(--border-color); margin: 20px 0;">
                <p style="font-size: 0.95rem; color: var(--text-muted); margin: 0; text-align: center;">
                    <b>با مشارکت پژوهشگران و مورخان برجسته:</b><br>
                    جان رابرت آلدرمن، جیک بنسون، ویلیام دالریمپل، ریچارد ام. ایتون، مریم اختیار، عبدالله قوچانی، سلام کاوکجی، ترنس مک‌اینرنی، جک اوگدن، کیلان اورتون، آنامیکا پاتاک، هوارد ریکتس، کورتنی ای. استوارت، سانجی سوبرامانیام و لورا واینستین
                </p>
            </div>
            
            <div style="text-align: center; margin-top: 30px; font-weight: bold; color: var(--text-main);">
                موزه هنر متروپولیتن، نیویورک<br>
                <span style="font-weight: normal; font-size: 0.9rem; color: var(--text-muted);">توزیع توسط انتشارات دانشگاه ییل (نیوهیون و لندن)</span>
            </div>
        </article>

        <!-- PAGE 5: COPYRIGHT & METADATA -->
        <article class="reader-card" id="page-5">
            <div class="page-badge">صفحه ۵ از ۳۸۶ (اطلاعات نشر و یادداشت خواننده)</div>
            
            <p>این کاتالوگ همزمان با برگزاری نمایشگاه <b>«سلاطین دکن هند، ۱۵۰۰–۱۷۰۰: شکوه و خیال»</b> در موزه هنر متروپولیتن نیویورک (برگزار شده از ۲۰ آوریل تا ۲۶ ژوئیه ۲۰۱۵) منتشر گردیده است.</p>

            <div style="background-color: rgba(251, 191, 36, 0.1); border-right: 4px solid var(--accent-gold); padding: 18px; border-radius: 6px; margin: 20px 0;">
                <p style="margin: 0; font-size: 0.95rem;">
                    <b>حامیان مالی و برگزارکنندگان نمایشگاه:</b><br>
                    برگزاری این نمایشگاه با حمایت مالی صندوق گیل و پارکر گیلبرت، صندوق پلاچیدو آرانگو، بنیاد ای. رودز و لئونا بی. کارپنتر، موقوفه ملی هنرها، و سینتیا هازن پولسکی و لئون بی. پولسکی امکان‌پذیر شده است.
                </p>
            </div>

            <h3 style="color: var(--accent-blue); margin-top: 25px; margin-bottom: 10px;">یادداشت تخصصی برای خواننده و پژوهشگر:</h3>
            <p>واژه‌های غیرانگلیسی (شامل اصطلاحات فارسی، عربی، دکنی، هندی و ترکی) در سرتاسر کتاب به‌صورت مشخص درج شده‌اند. تمام تلاش انجام شده تا آوانگاری و ضبط اسامی خاص به همراه نشانه‌گذاری‌های علمی (مانند ضبط عین و حمزه) رعایت شود.</p>
            <p>تاریخ‌های ذکر شده در تمامی بخش‌ها بر اساس تقویم میلادی است، مگر در مواردی که کتیبه یا نسخه‌ای دارای تاریخ دقیق هجری قمری یا ویکرام ساموات باشد که در این صورت هر دو تاریخ ذکر گردیده‌اند.</p>
        </article>

        <!-- PAGE 6: INTERACTIVE CLICKABLE TABLE OF CONTENTS -->
        <article class="reader-card" id="page-6">
            <div class="page-badge">صفحه ۶ از ۳۸۶ (فهرست مطالب تعاملی و کلیک‌پذیر)</div>
            
            <h1 class="chapter-heading">فهرست مطالب (Interactive Table of Contents)</h1>
            <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 15px;">💡 روی هر بخش کلیک کنید تا مستقیماً به صفحه مربوطه منتقل شوید:</p>
            
            <div class="toc-list">
                <a href="#page-8" class="clickable-toc-link">
                    <div>
                        <div class="toc-row-title">پیشگفتار مدیر موزه متروپولیتن</div>
                        <div class="toc-row-author">توماس پی. کمپبل (Thomas P. Campbell)</div>
                    </div>
                    <span class="toc-row-page">vii</span>
                </a>

                <a href="#page-5" class="clickable-toc-link">
                    <div>
                        <div class="toc-row-title">پیشگفتار و قدردانی</div>
                        <div class="toc-row-author">ناویینا نجات حیدر (Navina Najat Haidar)</div>
                    </div>
                    <span class="toc-row-page">viii</span>
                </a>

                <a href="#page-5" class="clickable-toc-link">
                    <div class="toc-row-title">شناسنامه و فهرست موزنداران</div>
                    <span class="toc-row-page">xi</span>
                </a>

                <a href="#page-4" class="clickable-toc-link">
                    <div class="toc-row-title">۱. دکن: یک عصر طلایی</div>
                    <span class="toc-row-page">۱</span>
                </a>

                <a href="#page-8" class="clickable-toc-link">
                    <div>
                        <div class="toc-row-title">۲. تاریخ سیاسی دکن (۱۵۰۰–۱۷۰۰)</div>
                        <div class="toc-row-author">ریچارد ام. ایتون (Richard M. Eaton)</div>
                    </div>
                    <span class="toc-row-page">۳</span>
                </a>
            </div>
        </article>

        <!-- PAGE 8: DIRECTOR'S FOREWORD -->
        <article class="reader-card" id="page-8">
            <div class="page-badge">صفحه ۸ از ۳۸۶ (پیشگفتار مدیر موزه)</div>
            
            <h1 class="chapter-heading">پیشگفتار مدیر موزه (Director's Foreword)</h1>
            <p style="color: var(--accent-gold); font-weight: bold; margin-bottom: 20px;">توماس پی. کمپبل (Thomas P. Campbell)</p>
            
            <p>پایه‌های فرهنگ جهانی امروزی از دیرباز پی‌ریزی شده است. از اواخر قرن پانزدهم تا اواخر قرن هفدهم میلادی، هنگامی که اروپاییان برای کشف نقاط جدید جهان به راه افتادند، نگاه آنان بیش از هر چیز معطوف به شبه‌قاره هند بود. آنان هنگامی که به مرکز این سرزمین یعنی <b>فلات دکن</b> وارد شدند، با جهانی شگرف مواجه گشتند که در آن فرهنگ‌های گوناگون خاورمیانه، ایران و افریقا از پیش با یکدیگر پیوند خورده و در فرهنگ بومی جذب شده بودند.</p>

            <div class="subtle-credit">
                آماده‌سازی تعاملی وب و زیرساخت دیجیتال: <b>توانا محمدی (Tawana Mohammadi)</b> | ترجمه انوشه طاهری (پایان‌نامه دکترا)
            </div>
        </article>

    </main>
</div>

<!-- Mobile Sticky Controls -->
<div class="mobile-controls">
    <button class="nav-btn" onclick="toggleSidebar()">📑 فهرست</button>
    <button class="nav-btn" onclick="toggleSettingsModal()">⚙️ تنظیمات</button>
    <button class="nav-btn" onclick="window.scrollTo({{top: 0, behavior: 'smooth'}})">⬆ بالا</button>
</div>

<script>
function toggleSidebar() {{
    document.getElementById('sidebar').classList.toggle('open');
    document.getElementById('settingsModal').classList.remove('active');
}}

function closeSidebar() {{
    document.getElementById('sidebar').classList.remove('open');
}}

function toggleSettingsModal() {{
    document.getElementById('settingsModal').classList.toggle('active');
    document.getElementById('sidebar').classList.remove('open');
}}

function updateFontSize(val) {{
    document.body.style.fontSize = val + 'px';
    document.getElementById('fontSizeVal').innerText = val + 'px';
    document.getElementById('fontSlider').value = val;
}}

function stepFontSize(delta) {{
    const current = parseInt(document.getElementById('fontSlider').value);
    const next = Math.max(14, Math.min(26, current + delta));
    updateFontSize(next);
}}

function setTheme(themeName) {{
    document.documentElement.setAttribute('data-theme', themeName);
    document.querySelectorAll('.theme-pill').forEach(pill => {{
        pill.classList.remove('active');
    }});
    if (themeName === 'dark') document.querySelectorAll('.theme-pill-dark')[0].classList.add('active');
    if (themeName === 'light') document.querySelectorAll('.theme-pill-light')[0].classList.add('active');
    if (themeName === 'sepia') document.querySelectorAll('.theme-pill-sepia')[0].classList.add('active');
}}
</script>

</body>
</html>
"""

out_file = "pages_001_to_010_responsive.html"
with open(out_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Responsive Reader with Tawana Mohammadi Credit saved to: {out_file}")
