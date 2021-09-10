import openpyxl
wb = openpyxl.load_workbook("汇总.xlsx", data_only=True)


def getData(workSheetName, targetSheetName):
    workSheet = wb[workSheetName]
    targetSheet = wb[targetSheetName]
    for rowData in workSheet.rows:
        productName = rowData[0].value
        if "口香糖" in productName:
            rowValue = []
            for cell in rowData:
                rowValue.append(cell.value)
            rowValue.append(workSheetName)
            targetSheet.append(rowValue)

getData("A平台", "口香糖")
getData("B平台", "口香糖")
getData("C平台", "口香糖")

wb.save("汇总.xlsx")
# 课程中阿珍已经将三个平台的商品信息统计到了汇总表格，现在阿珍查看所有平台的口香糖商品数据。
# 要求找到每个平台中口香糖品类，将商品复制到口香糖工作表，并添加该商品信息所属平台。
# 汇总表格路径：/Users/yequ/data/汇总.xlsx
# 阿珍已经手动在表中创建了到口香糖工作表中，并创建了表头，商品名称、月份、销售额、平台。
