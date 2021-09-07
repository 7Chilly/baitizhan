import openpyxl
from openpyxl import utils

wb = openpyxl.load_workbook("2019年1月销售订单.xlsx",data_only=True)
salesSheet = wb["销售订单数据"]
productData = {}
for rowData in salesSheet.rows:
    productName = rowData[2].value
    if productName == "商品名":
        continue
    salesAmountIndex = utils.cell.column_index_from_string("I") - 1
    salesAmount = rowData[salesAmountIndex].value
    if productName not in productData.keys():
        productData[productName] = salesAmount
    else:
        productData[productName] += salesAmount

maxAmount = 0
starProduct = ""
for item in productData.keys():
    totalAmount = productData[item]
    if totalAmount > maxAmount:
        maxAmount = totalAmount
        starProduct = item

print(f"明星产品是：{starProduct}，一月总共销售出{maxAmount}元")

# 为了知道消费者季节性消费习惯，阿珍想要统计一月份卖的最好的明星产品，可是一个一个商品统计实在是很麻烦，这该怎么办呢？
# 聪明的阿珍想要的好办法，可以通过Python读取“2019年1月销售订单.xlsx”工作薄，获取“销售订单数据”工作表，计算得出工作表内每个商品当月的销售额
# 接着从所有商品销售额中，找到当月销售额最高的商品，最后输出销售额最高商品品名和销售额。
# 例如：明星产品是：XXX，一月总共销售出XXX元
