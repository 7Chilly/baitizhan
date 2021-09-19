import os
import pdfplumber
import docx

folderPath = "文稿汇总"
allItems = os.listdir(folderPath)
chapterList = []
for item in allItems:
    chapter = os.path.splitext(item)[0]
    chapterList.append(chapter)
chapterList.sort(key=int)
doc = docx.Document()
for i in chapterList:
    newName = i + ".pdf"
    newPDFPath = os.path.join(folderPath, newName)
    pdf = pdfplumber.open(newPDFPath)
    for page in pdf.pages:
        pageText = page.extract_text()
        pageText = pageText.replace("python", "Python")
        doc.add_paragraph(pageText)
    print(f"{i}提取完成")
    doc.add_page_break()
doc.save("Python合集.docx")

