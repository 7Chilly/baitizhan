import pdfplumber
import docx

pdf = pdfplumber.open("名单.pdf")
nameList = []
for page in pdf.pages:
    table = page.extract_tables()[0]
    for row in table:
        name = row[0]
        if name == "姓名":
            continue
        nameList.append(name)
doc = docx.Document("优秀教师.docx")
nameList2 = " ".join(nameList)
doc.add_paragraph(nameList2)
doc.save("优秀教师.docx")
