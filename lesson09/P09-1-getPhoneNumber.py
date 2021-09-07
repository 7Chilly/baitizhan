import openpyxl
def queryPhone(queryName):
    queryList = []
    wb = openpyxl.load_workbook("电话本.xlsx")
    workSheet = wb["电话簿"]
    for rowData in workSheet.rows:
        name = rowData[0].value
        phoneNumber = rowData[1].value
        if name == queryName:
            queryList.append(phoneNumber)
    return queryList

print(queryPhone("刘进英"))


# 写一个通过姓名查询电话号码函数queryPhone，
# 函数有一个参数queryName用来传入查询的姓名，返回一个列表，列表内是所有匹配该查询姓名的电话号码。
# 如果没有匹配的电话号码，返回一个空列表。
