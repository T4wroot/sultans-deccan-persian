import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

test_html = """<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<style>
@font-face {
    font-family: 'Vazirmatn';
    src: url('c:/Projects/translate/Vazirmatn-Regular.ttf');
    font-weight: normal;
}
@font-face {
    font-family: 'Vazirmatn';
    src: url('c:/Projects/translate/Vazirmatn-Bold.ttf');
    font-weight: bold;
}
body {
    font-family: 'Vazirmatn', sans-serif;
    direction: rtl;
    text-align: right;
    font-size: 12pt;
}
</style>
</head>
<body>
<h1>سلاطین دکن هند</h1>
<p>این یک متن آزمایشی به زبان فارسی است.</p>
</body>
</html>
"""

story = fitz.Story(test_html)
writer = fitz.DocumentWriter("test_font_path_clean.pdf")
more = True
while more:
    device = writer.begin_page(fitz.Rect(0, 0, 595, 842))
    more, _ = story.place(fitz.Rect(40, 40, 555, 802))
    story.draw(device)
    writer.end_page()
writer.close()

doc_t = fitz.open("test_font_path_clean.pdf")
print("PDF Page count:", len(doc_t))
print("Extracted text:")
print(doc_t[0].get_text("text"))
