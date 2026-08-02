import os
import base64

cover_img_path = os.path.join("extracted_images", "page_001_img_1.jpeg")
if os.path.exists(cover_img_path):
    with open(cover_img_path, "rb") as f:
        cover_b64 = base64.b64encode(f.read()).decode('utf-8')
    cover_img_html = f'<img src="data:image/jpeg;base64,{cover_b64}" class="cover-image">'
else:
    cover_img_html = ""

html_template = f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<title>ترجمه آکادمیک سلاطین دکن هند - صفحات ۱ تا ۱۰</title>
<style>
body {{
    font-family: 'Vazirmatn', 'Segoe UI', Tahoma, sans-serif;
    direction: rtl;
    text-align: right;
    font-size: 11pt;
    line-height: 1.9;
    color: #1f2937;
    background-color: #f3f4f6;
    margin: 0;
    padding: 20px;
}}

.paper-page {{
    background-color: #ffffff;
    width: 210mm;
    min-height: 297mm;
    margin: 20px auto;
    padding: 25mm 20mm;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    box-sizing: border-box;
    position: relative;
    page-break-after: always;
}}

.page-header {{
    border-bottom: 1px solid #cbd5e1;
    padding-bottom: 8px;
    margin-bottom: 25px;
    display: flex;
    justify-content: space-between;
    font-size: 9.5pt;
    color: #64748b;
}}

.page-footer {{
    border-top: 1px solid #cbd5e1;
    padding-top: 8px;
    margin-top: 35px;
    text-align: center;
    font-size: 9.5pt;
    color: #64748b;
}}

/* Cover Styling */
.cover-title {{
    font-size: 26pt;
    font-weight: bold;
    color: #1e3a8a;
    text-align: center;
    margin-top: 20px;
}}

.cover-subtitle {{
    font-size: 15pt;
    color: #475569;
    text-align: center;
    margin-bottom: 25px;
}}

.cover-image {{
    max-width: 80%;
    height: auto;
    border-radius: 8px;
    display: block;
    margin: 20px auto;
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
}}

.thesis-badge {{
    background-color: #fef2f2;
    border: 1px solid #fecaca;
    color: #991b1b;
    font-weight: bold;
    font-size: 15pt;
    padding: 8px 20px;
    border-radius: 6px;
    text-align: center;
    width: fit-content;
    margin: 0 auto 20px auto;
}}

.thesis-card {{
    background-color: #f8fafc;
    border: 2px solid #e2e8f0;
    border-radius: 8px;
    padding: 20px;
    margin-top: 30px;
    text-align: center;
}}

.thesis-card h3 {{
    color: #1e3a8a;
    margin-top: 0;
}}

.thesis-card h2 {{
    color: #991b1b;
    margin: 10px 0;
}}

/* TOC Table Styling */
.toc-table {{
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
}}

.toc-row {{
    margin-bottom: 12px;
    border-bottom: 1px dotted #cbd5e1;
    padding-bottom: 4px;
}}

.toc-title {{
    font-weight: bold;
    color: #1e3a8a;
}}

.toc-page {{
    float: left;
    font-weight: bold;
    color: #991b1b;
}}

.toc-author {{
    font-size: 9.5pt;
    color: #64748b;
    margin-top: 2px;
}}

h1.section-heading {{
    color: #1e3a8a;
    font-size: 18pt;
    border-bottom: 2px solid #3b82f6;
    padding-bottom: 8px;
    margin-top: 0;
}}

p {{
    text-align: justify;
    text-justify: inter-word;
    margin-bottom: 14px;
}}
</style>
</head>
<body>

<!-- PAGE 1: COVER -->
<div class="paper-page" id="page-1">
    <div class="thesis-badge">پایان‌نامه دکترا</div>
    <div class="cover-title">سلاطین دکن هند (۱۵۰۰–۱۷۰۰)</div>
    <div class="cover-subtitle">شکوه و خیال در هنر، معماری و فرهنگ اسلامی</div>
    
    {cover_img_html}
    
    <div class="thesis-card">
        <h3>عنوان ترجمه و تحقیق آکادمیک:</h3>
        <h2>ترجمه انوشه طاهری - پایان‌نامه دکترا</h2>
        <p style="text-align: center; color: #64748b; margin: 0;">
            نویسندگان اصلی: ناویینا نجات حیدر و ماریکا سردار (موزه هنر متروپولیتن نیویورک)<br>
            رشته تاریخ هنر و معماری اسلامی | سال تحصیلی ۱۴۰۵ - ۱۴۰۶
        </p>
    </div>
    
    <div class="page-footer">صفحه ۱ از ۳۸۶ (جلد اصلی)</div>
</div>

<!-- PAGE 4: TITLE PAGE -->
<div class="paper-page" id="page-4">
    <div class="page-header">
        <span>سلاطین دکن هند (۱۵۰۰-۱۷۰۰)</span>
        <span>ترجمه انوشه طاهری - پایان‌نامه دکترا</span>
    </div>
    
    <h1 class="section-heading" style="text-align: center;">سلاطین دکن هند (۱۵۰۰–۱۷۰۰)<br><small style="font-size: 14pt; color: #475569;">شکوه و خیال‌پردازی</small></h1>
    
    <p style="text-align: center; font-size: 13pt; font-weight: bold; color: #1e3a8a;">
        نویسندگان اصلی: ناویینا نجات حیدر و ماریکا سردار
    </p>
    
    <p style="text-align: center; color: #475569; font-size: 10.5pt;">
        <b>با مشارکت پژوهشگران و مورخان برجسته:</b><br>
        جان رابرت آلدرمن، جیک بنسون، ویلیام دالریمپل، ریچارد ام. ایتون، مریم اختیار، عبدالله قوچانی، سلام کاوکجی، ترنس مک‌اینرنی، جک اوگدن، کیلان اورتون، آنامیکا پاتاک، هوارد ریکتس، کورتنی ای. استوارت، سانجی سوبرامانیام و لورا واینستین
    </p>
    
    <div style="text-align: center; margin-top: 50px; font-weight: bold; color: #334155;">
        موزه هنر متروپولیتن، نیویورک<br>
        <span style="font-weight: normal; font-size: 10pt; color: #64748b;">توزیع توسط انتشارات دانشگاه ییل (نیوهیون و لندن)</span>
    </div>
    
    <div class="page-footer">صفحه ۴ از ۳۸۶</div>
</div>

<!-- PAGE 5: COPYRIGHT & PUBLICATION METADATA -->
<div class="paper-page" id="page-5">
    <div class="page-header">
        <span>شناسنامه نشر و کپی‌رایت</span>
        <span>ترجمه انوشه طاهری - پایان‌نامه دکترا</span>
    </div>
    
    <p>این کاتالوگ همزمان با برگزاری نمایشگاه <b>«سلاطین دکن هند، ۱۵۰۰–۱۷۰۰: شکوه و خیال»</b> در موزه هنر متروپولیتن نیویورک (برگزار شده از ۲۰ آوریل تا ۲۶ ژوئیه ۲۰۱۵) به چاپ رسیده است.</p>

    <p style="background-color: #f8fafc; padding: 12px; border-right: 3px solid #3b82f6; font-size: 10pt;">
        <b>حامیان مالی و برگزارکنندگان نمایشگاه:</b><br>
        برگزاری این نمایشگاه با حمایت مالی صندوق گیل و پارکر گیلبرت، صندوق پلاچیدو آرانگو، بنیاد ای. رودز و لئونا بی. کارپنتر، موقوفه ملی هنرها، و سینتیا هازن پولسکی و لئون بی. پولسکی امکان‌پذیر شده است.
    </p>

    <h3 style="color: #1e3a8a; margin-top: 25px;">یادداشت مهم برای خواننده و پژوهشگر:</h3>
    <p>واژه‌های غیرانگلیسی (شامل اصطلاحات فارسی، عربی، دکنی، هندی و ترکی) در سرتاسر کتاب به‌صورت مشخص درج شده‌اند. تمام تلاش انجام شده تا آوانگاری و ضبط اسامی خاص به همراه نشانه‌گذاری‌های علمی (مانند ضبط عین و حمزه) رعایت شود.</p>

    <div class="page-footer">صفحه ۵ از ۳۸۶</div>
</div>

<!-- PAGE 6: TABLE OF CONTENTS -->
<div class="paper-page" id="page-6">
    <div class="page-header">
        <span>فهرست مطالب کامل کتاب</span>
        <span>ترجمه انوشه طاهری - پایان‌نامه دکترا</span>
    </div>
    
    <h1 class="section-heading">فهرست مطالب (Contents)</h1>
    
    <div class="toc-row">
        <span class="toc-title">پیشگفتار مدیر موزه متروپولیتن</span>
        <span class="toc-page">vii</span>
        <div class="toc-author">توماس پی. کمپبل (Thomas P. Campbell)</div>
    </div>
    
    <div class="toc-row">
        <span class="toc-title">پیشگفتار و سپاس‌گزاری</span>
        <span class="toc-page">viii</span>
        <div class="toc-author">ناویینا نجات حیدر (Navina Najat Haidar)</div>
    </div>
    
    <div class="toc-row">
        <span class="toc-title">فهرست موزنداران و مجموعه‌داران</span>
        <span class="toc-page">xi</span>
    </div>
    
    <div class="toc-row">
        <span class="toc-title">نقشه‌ها و زمینه‌های جغرافیایی دکن</span>
        <span class="toc-page">xii</span>
    </div>
    
    <div class="toc-row" style="margin-top: 15px;">
        <span class="toc-title">۱. دکن: یک عصر طلایی</span>
        <span class="toc-page">۱</span>
    </div>
    
    <div class="toc-row">
        <span class="toc-title">۲. تاریخ سیاسی دکن (۱۵۰۰–۱۷۰۰)</span>
        <span class="toc-page">۳</span>
        <div class="toc-author">ریچارد ام. ایتون (Richard M. Eaton)</div>
    </div>
    
    <div class="toc-row">
        <span class="toc-title">۳. هنرهای دربار دکن</span>
        <span class="toc-page">۱۵</span>
        <div class="toc-author">ناویینا نجات حیدر (Navina Najat Haidar)</div>
    </div>
    
    <div class="toc-row">
        <span class="toc-title">۴. بهمنیان و میراث هنری آن‌ها</span>
        <span class="toc-page">۲۹</span>
        <div class="toc-author">ماریکا سردار (Marika Sardar)</div>
    </div>
    
    <div class="toc-row">
        <span class="toc-title">کاتالوگ آثار ۱ تا ۶</span>
        <span class="toc-page">۳۴</span>
    </div>
    
    <div class="toc-row">
        <span class="toc-title">۵. مکتب احمدنگر و برار</span>
        <span class="toc-page">۴۳</span>
    </div>
    
    <div class="toc-row">
        <span class="toc-title">کاتالوگ آثار ۷ تا ۲۱</span>
        <span class="toc-page">۵۵</span>
    </div>
    
    <div class="toc-row">
        <span class="toc-title">۶. مکتب بیجاپور</span>
        <span class="toc-page">۷۷</span>
    </div>
    
    <div class="toc-row">
        <span class="toc-title">کاتالوگ آثار ۲۲ تا ۷۱</span>
        <span class="toc-page">۸۴</span>
    </div>
    
    <div class="page-footer">صفحه ۶ از ۳۸۶</div>
</div>

<!-- PAGE 8: DIRECTOR'S FOREWORD -->
<div class="paper-page" id="page-8">
    <div class="page-header">
        <span>پیشگفتار مدیر موزه متروپولیتن</span>
        <span>ترجمه انوشه طاهری - پایان‌نامه دکترا</span>
    </div>
    
    <h1 class="section-heading">پیشگفتار مدیر موزه (Director's Foreword)</h1>
    <p style="color: #64748b; font-weight: bold; margin-bottom: 20px;">توماس پی. کمپبل (Thomas P. Campbell)</p>
    
    <p>پایه‌های فرهنگ جهانی امروزی از دیرباز پی‌ریزی شده است. از اواخر قرن پانزدهم تا اواخر قرن هفدهم میلادی، هنگامی که اروپاییان برای کشف نقاط جدید جهان به راه افتادند، نگاه آنان بیش از هر چیز معطوف به شبه‌قاره هند بود. آنان هنگامی که به مرکز این سرزمین یعنی <b>فلات دکن</b> وارد شدند، با جهانی شگرف مواجه گشتند که در آن فرهنگ‌های گوناگون خاورمیانه، ایران و افریقا از پیش با یکدیگر پیوند خورده و در فرهنگ بومی جذب شده بودند.</p>
    
    <p>سلاطین دکن که حامیان سخاوتمند هنرمندان، شاعران، معماران و دانشمندان بودند، دربارهایی با شکوه و متمایز پدید آوردند که شاهکارهای هنری آن همواره مورد تحسین جهان بوده است.</p>
    
    <div class="page-footer">صفحه ۸ از ۳۸۶</div>
</div>

</body>
</html>
"""

out_file = "pages_001_to_010.html"
with open(out_file, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"Clean HTML template document generated: {out_file}")
