import os
import openpyxl

allItems = os.listdir()
for item in allItems:
    wb = openpyxl.load_workbook(item)
    for sheet in wb.worksheets:
        for row in sheet.rows:
            article = row[0].value
            name = row[1].value
            email = row[3].value
            if article == "索引" and name == "小夜" and email == "16798429@yequ.com":
                print(f"{item}", row)
