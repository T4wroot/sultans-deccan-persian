import fitz

html_file = "pages_001_to_010.html"
pdf_file = "pages_001_to_010.pdf"

with open(html_file, "r", encoding="utf-8") as f:
    html_content = f.read()

print(f"Rendering {html_file} to {pdf_file}...")

story = fitz.Story(html_content)
writer = fitz.DocumentWriter(pdf_file)
more = True
page_count = 0

while more:
    device = writer.begin_page(fitz.Rect(0, 0, 595, 842)) # A4
    more, _ = story.place(fitz.Rect(30, 30, 565, 812))
    story.draw(device)
    writer.end_page()
    page_count += 1

writer.close()

print(f"PDF generated successfully: {pdf_file} ({page_count} PDF pages)")
