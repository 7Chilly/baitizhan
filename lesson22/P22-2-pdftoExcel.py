import os
import openpyxl
import pdfplumber

sourcePath = "bankBalance"
allItems = os.listdir(sourcePath)
newWb = openpyxl.Workbook()
for item in allItems:
    name = os.path.splitext(item)[0]
    pdfPath = os.path.join(sourcePath, item)
    pdf = pdfplumber.open(pdfPath)
    newWb.create_sheet(name)
    workSheet = newWb[name]
    for page in pdf.pages:
        table = page.extract_tables()[0]
        for row in table:
            workSheet.append(row)
sheet = newWb["Sheet"]
newWb.remove(sheet)
newWb.save("年底合集.xlsx")

