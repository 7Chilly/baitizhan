import openpyxl

for item in range(1,13):
    filePath = f"2019年{item}月销售订单.xlsx"
    wb = openpyxl.load_workbook(filePath, data_only=True)
    orderSheet = wb["销售订单数据"]
    productList = []
    for rowData in orderSheet.rows:
        productName = rowData[2].value
        if productName == "商品名":
            continue
        if productName not in productList:
            productList.append(productName)

    for product in productList:
        newSheet = wb.create_sheet(product)
        newSheet["A1"].value = "订单号"
        newSheet["B1"].value = "商品ID"
        newSheet["C1"].value = "商品名称"
        newSheet["D1"].value = "品牌"
        newSheet["E1"].value = "类别"
        newSheet["F1"].value = "规格"
        newSheet["G1"].value = "单价"
        newSheet["H1"].value = "数量"
        newSheet["I1"].value = "总价"

    wb.save(filePath)
