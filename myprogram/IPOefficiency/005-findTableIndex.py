import docx

doc = docx.Document("【有研硅】财务部分.docx")
checkInfo1 = input("请填写您想查找的表格内容（最好unique一点哦）：")
InfoList = []
for idx, table in enumerate(doc.tables):
    if idx == 32 or idx == 49:
        break
    for row in table.rows:
        for cell in row.cells:
            cellValue = cell.text
            if checkInfo1 == cellValue:
                InfoList.append(idx)
if len(InfoList) == 1:
    idx = InfoList[0]
    print(f"这是Sheet{idx}")
else:
    checkInfo2 = input("信息可以再精准一点，再填一个试试吧：")
    newInfoList = []
    for idx in InfoList:
        if idx == 32 or idx == 49:
            break
        table = doc.tables[idx]
        for row in table.rows:
            for cell in row.cells:
                cellValue = cell.text
                if checkInfo2 == cellValue:
                    newInfoList.append(idx)
    if len(newInfoList) == 1:
        idx = newInfoList[0]
        print(f"这是Sheet{idx}")
    else:
        print("不想找啦，请检查是否输入正确～")
