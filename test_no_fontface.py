import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

test_html = """<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<style>
body {
    font-family: sans-serif;
    direction: rtl;
    text-align: right;
    font-size: 12pt;
}
h1 { color: #1e3a8a; }
</style>
</head>
<body>
<h1>سلاطین دکن هند</h1>
<p>این یک متن آزمایشی به زبان فارسی است که به صورت کاملاً درست و با کیفیت رندر می‌شود.</p>
</body>
</html>
"""

story = fitz.Story(test_html)
writer = fitz.DocumentWriter("test_no_fontface.pdf")
more = True
while more:
    device = writer.begin_page(fitz.Rect(0, 0, 595, 842))
    more, _ = story.place(fitz.Rect(40, 40, 555, 802))
    story.draw(device)
    writer.end_page()
writer.close()

doc_t = fitz.open("test_no_fontface.pdf")
print("PDF Page count:", len(doc_t))
print("Extracted text:")
print(doc_t[0].get_text("text"))
