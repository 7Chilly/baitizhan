import os
import pdfplumber
import docx

wordPath = "稿件文档"
os.mkdir(wordPath)
sourcePath = "Python"
allItems = os.listdir(sourcePath)
for item in allItems:
    name = os.path.splitext(item)[0]
    doc = docx.Document()
    itemPath = os.path.join(sourcePath, item)
    pdf = pdfplumber.open(itemPath)
    for page in pdf.pages:
        text = page.extract_text()
        doc.add_paragraph(text)
    docName = name + ".docx"
    docPath = os.path.join(wordPath, docName)
    doc.save(docPath)
    print(f"{docName}提取完成")
