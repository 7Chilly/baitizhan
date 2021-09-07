import openpyxl
from openpyxl import utils

def getMonthlySOld(filePath):
    wb = openpyxl.load_workbook(filePath, data_only=True)
    workSheet = wb["销售订单数据"]
    gumSold = 0
    for rowData in workSheet.rows:
        productName = rowData[2].value
        if productName == "商品名":
            continue
        priceIndex = utils.cell.column_index_from_string("I")-1
        price = rowData[priceIndex].value
        if productName == "麻辣味口香糖":
            gumSold += price
    return gumSold

gumMonthlySoldList = []
for month in range(1,13):
    filePath = f"2019年{month}月销售订单.xlsx"
    gumMonthlySold = getMonthlySOld(filePath)
    gumMonthlySoldList.append(gumMonthlySold)

maxMonthlySold = max(gumMonthlySoldList)
maxMonth = gumMonthlySoldList.index(maxMonthlySold) + 1
print(f"麻辣味口香糖在{maxMonth}月份卖得最好")

