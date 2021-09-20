import openpyxl
import pdfplumber
import os

pdf = pdfplumber.open("来访学生统计表.pdf")
newWb = openpyxl.Workbook()
aSheet = newWb["Sheet"]
sourcePath = "学生照片"
allItems = os.listdir(sourcePath)
for page in pdf.pages:
    table = page.extract_tables()[0]
    for row in table:
        aSheet.append(row)
        aSheet.append(row)
aSheet["D1"].value = "照片"
for rowIndex, row in enumerate(aSheet.rows):
    name = row[0].value
    for item in allItems:
        picPath = os.path.join(sourcePath, item)
        picName = os.path.splitext(item)[0]
        if name == picName:
            path = openpyxl.drawing.image.Image(picPath)
            aSheet.add_image(path, f"D{rowIndex+1}")
newWb.save("来访学生统计表.xlsx")
