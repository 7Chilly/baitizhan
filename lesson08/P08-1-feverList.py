import openpyxl
wb = openpyxl.load_workbook("进楼登记.xlsx", data_only=True)
tempSheet = wb["体温表"]
feverList = []
for rowData in tempSheet.rows:
    name = rowData[0].value
    temp = rowData[1].value
    if temp == "测量体温":
        continue
    if temp > 37:
        feverList.append(name)
print(feverList)

# 当前工作目录有一个文件名为“进楼登记.xlsx”的Excel表格，结构如下图：
# 定义一个变量名为feverList的列表（List），将工作表“体温表”中所有体温高于37度的姓名添加进列表，最后使用print输出这个列表。
