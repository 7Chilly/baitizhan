import openpyxl
import docx
from openpyxl import utils


def getNewSheet(idx, wb):
    if idx == 0:
        newSheet = wb["Sheet"]
        newSheet.title = "Sheet0"
    else:
        newSheet = wb.create_sheet(f"Sheet{idx}")
    return newSheet


wb = openpyxl.Workbook()
doc = docx.Document("【有研硅】财务部分.docx")
for idx, table in enumerate(doc.tables):
    newSheet = getNewSheet(idx, wb)
    for rowIndex in range(1, len(table.rows)+1):
        for columnNumIndex in range(1, len(table.columns)+1):
            columnIndex = utils.get_column_letter(columnNumIndex)
            newSheet[f"{columnIndex}{rowIndex}"].value = table.cell(rowIndex-1, columnNumIndex-1).text
wb.save("尝试表格-1.xlsx")
print("成功输入到Excel")
