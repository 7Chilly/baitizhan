import openpyxl
from openpyxl import utils

def gmv(path):
    wb = openpyxl.load_workbook(path, data_only=True)
    workBook = wb["销售订单数据"]
    totalAmount = 0
    for rowData in workBook.rows:
        priceIndex = utils.cell.column_index_from_string("I")-1
        price = rowData[priceIndex].value
        if price =="总价":
            continue
        totalAmount += price
    return totalAmount

for month in range(1,13):
    path = f"2019年{month}月销售订单.xlsx"
    monthlyGMV = gmv(path)
    if monthlyGMV > 8500:
        print(f"{month}月是盈利的。盈利{monthlyGMV-8500}元。")
