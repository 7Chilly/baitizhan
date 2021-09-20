import os
import pdfplumber
import openpyxl

sourcePath = "银行账单"
allItems = os.listdir(sourcePath)
newWb = openpyxl.Workbook()
sheet = newWb["Sheet"]
for item in allItems:
    pdfPath = os.path.join(sourcePath, item)
    pdf = pdfplumber.open(pdfPath)
    for page in pdf.pages:
        tableData = page.extract_tables()[0]
        for row in tableData:
            sheet.append(row)
    print(f"{item}提取完成")
newWb.save("账单合集.xlsx")

# 在这里，每个PDF文档中，只有一个表格哦~
