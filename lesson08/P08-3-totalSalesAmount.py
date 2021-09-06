import openpyxl
import rmbTrans

wb = openpyxl.load_workbook("开口哭牌供货列表.xlsx",data_only=True)
salesSheet = wb["6月供货"]
totalAmount = 0
for rowData in salesSheet:
    rmbsalesAmount = rowData[6].value
    salesAmount = rmbTrans.trans(rmbsalesAmount)
    totalAmount += salesAmount
print(f"开口哭牌供应商6月采购总金额为{totalAmount}元。")


# 阿珍会收到来自开口哭牌供应商的供货信息表。由于供应商的原因，发来的Excel里，金额是用中文大写来表达的，阿珍无法直接进行计算。
# 我们需要将中文大写的金额，转化为小写阿拉伯数字，来计算总额，并且将计算结果输出。
# Excel文档"开口哭牌供货列表.xlsx"在工作目录下，工作表名为"6月供货"。
# 我们要读取Excel第7列的"总金额"。计算所有金额的总数，并最后用格式化输出：
# "开口哭牌供应商6月采购总金额为xxxx元。"

# wow 原来rmbTrans这个module可以自动跳过不是大写金额的字符串！！！好聪明！
