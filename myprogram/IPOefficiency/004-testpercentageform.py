import openpyxl
from openpyxl.styles import numbers

wb = openpyxl.load_workbook("test005.xlsx", data_only= True)
ws = wb["Sheet1"]

def twoDecPer(cell):
    cellValue = cell.value
    cellValue *= 100
    cellValue = f"{cellValue:.2f}"
    Info = str(cellValue) + "%"

cellList = []
for row in ws.rows:
    for cell in row:
        formatCell = cell.number_format
        print(formatCell)
        if "%" in formatCell:
            if formatCell == "0%":
                cellValue = cell.value
                cellValue *= 100
                cellValue = f"{cellValue:.0f}"
                cellPercent = str(cellValue) + "%"
                cellList.append(cellPercent)
            if formatCell == "0.00%":
                cellValue = cell.value
                cellValue *= 100
                cellValue = f"{cellValue:.2f}"
                cellPercent = str(cellValue) + "%"
                cellList.append(cellPercent)
        else:
            cellValue = cell.value
            if cellValue is None:
                continue
            cellList.append(cellValue)

print(cellList)
