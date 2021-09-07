import os
import openpyxl
import shutil

docPath = "学生资料"
wb = openpyxl.load_workbook("学生地区.xlsx")
workSheet = wb["地区表"]
for rowData in workSheet.rows:
    name = rowData[0].value
    address = rowData[1].value
    if name == "姓名":
        continue
    nameDoc = f"{name}.docx"
    downloadPath = os.path.join(docPath, nameDoc)
    targetPath = os.path.join(docPath, address)
    if not os.path.exists(targetPath):
        os.mkdir(targetPath)
    shutil.move(downloadPath, targetPath)


# 夜曲大学招生办Wendy收到了今年来自国内各个地区的学生资料，位于路径/Users/Wendy/学生资料 下。
# 每个学生资料以他们的姓名命名，例如：毛大鹏.docx
# 现在Wendy想把这些学生资料按照他们的地区进行分类，以便于之后发给对应地区的负责人。分类的文件夹需要创建在/Users/Wendy/学生资料这个路径下，例如：/Users/Wendy/学生资料/四川
# 每个学生分别属于哪个地区的信息在/Users/Wendy/学生地区.xlsx这个Excel表格中，表格格式如下图。
# 请使用已学知识帮助Wendy完成对学生的分类，当前程序的工作目录为/Users/Wendy/
