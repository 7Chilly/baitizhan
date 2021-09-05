import os
import openpyxl

path = "/Users/chilly/Desktop/python/yequ/阿珍的网店/problem07"
os.chdir(path)
allExcels = os.listdir(path)
for item in allExcels:
    wb = openpyxl.load_workbook(item)
    for sheet in wb.sheetnames:
        if sheet == "十二月销售订单数据":
            print(item)
