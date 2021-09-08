import os
import openpyxl

sourcePath = "doc"
allItems = os.listdir(sourcePath)
for item in allItems:
    filePath = os.path.join(sourcePath, item)
    wb = openpyxl.load_workbook(filePath, data_only=True)
    for sheet in wb.worksheets:
        for rowData in sheet.rows:
            if rowData[2].value == "有点酸可乐":
                rowData[2].value = "有点酸甜可乐"
    wb.save(f"revise/{item}")

# 阿珍的网店有两种口味的可乐，19年的销售数据中将商品ID700014的“有点酸甜可乐”，登记成“有点酸可乐”。
# 需要将12个月份中所有的“有点酸可乐”改成“有点酸甜可乐”
# 修改后存储到：/Users/zhener/revise
# 注意：“销售商品”和“销售订单数据”两个工作表中“有点酸可乐”都需要替换
