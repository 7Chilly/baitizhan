import pdfplumber
import docx

pdf = pdfplumber.open("英美短篇小说文本分析与鉴赏text.pdf")
doc = docx.Document()
for page in pdf.pages:
    doc.add_paragraph(page.extract_text())
    doc.add_page_break()

doc.save("英美短篇小说文本分析与鉴赏text.docx")

