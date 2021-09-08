import openpyxl
for item in range(1,13):
    filePath = f"2019{item:02}.xlsx"
    wb = openpyxl.load_workbook(filePath, data_only=True)
    orderSheet = wb["明细"]
    MonthData = {}
    for rowData in orderSheet.rows:
        productName = rowData[4].value
        orderPrice = rowData[5].value
        if productName == "名称":
            continue
        monthPrice = MonthData.get(productName, 0)
        MonthData[productName] = monthPrice + orderPrice
    print(MonthData)

