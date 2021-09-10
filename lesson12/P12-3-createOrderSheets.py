import openpyxl

for i in range(1, 13):
    filePath = f"2019年{i}月销售订单.xlsx"
    wb = openpyxl.load_workbook(filePath, data_only=True)
    orderSheet = wb["销售订单数据"]
    for rowData in orderSheet.rows:
        productName = rowData[2].value
        if productName == "商品名":
            continue
        rowValue = []
        for cell in rowData:
            rowValue.append(cell.value)
        for sheet in wb.worksheets:
            if sheet.title == productName:
                sheet.append(rowValue)
    wb.save(filePath)
