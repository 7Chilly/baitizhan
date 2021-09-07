import openpyxl
def getOrderList(filepath, worksheet, column, exception):
    wb = openpyxl.load_workbook(filepath, data_only=True)
    orderSheet = wb[worksheet]
    orderList= []
    for rowData in orderSheet.rows:
        order = rowData[column].value
        if order == exception:
            continue
        orderList.append(order)
    return orderList

orderList1 = getOrderList("平台销售订单.xlsx", "销售订单数据", 0, "订单号")
orderList2 = getOrderList("系统数据.xlsx", "订单数据", 1, "order_id")

for item in orderList1:
    if item not in orderList2:
        print(f"订单号 {item} 不在系统数据中")
for item in orderList2:
    if item not in orderList1:
        print(f"订单号 {item} 不在商城数据中")
