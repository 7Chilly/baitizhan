import os
import pdfplumber
import docx

file = docx.Document()
folderPath = "manuscript"
allItems = os.listdir(folderPath)
chapterList = []

for item in allItems:
    chapter = os.path.splitext(item)[0]
    chapterList.append(chapter)
chapterList.sort(key=int)

for i in chapterList:
    newName = i + ".pdf"
    newPDFPath = os.path.join(folderPath, newName)
    pdf = pdfplumber.open(newPDFPath)
    for page in pdf.pages:
        text = page.extract_text()
        text = text.replace("PYTHON", "Python")
        file.add_paragraph(text)
    print(f"{newName}提取完成")
    file.add_page_break()

file.save("Python文稿.docx")
