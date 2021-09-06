import openpyxl
import os
import shutil

wb = openpyxl.load_workbook("长颈鹿图书馆.xlsx", data_only=True)
bookSheet = wb["长颈鹿图书馆书籍清单"]
targetBookList = []
for rowData in bookSheet.rows:
    name = rowData[1].value
    bookClass = rowData[4].value
    if bookClass == "计算机科学":
        targetBookList.append(name)

oldPath = "books"
allBooks = os.listdir(oldPath)
newPath = "计算机科学"
for book in allBooks:
    bookName = os.path.splitext(book)[0]
    if bookName in targetBookList:
        sourcePath = os.path.join(oldPath, book)
        shutil.move(sourcePath, newPath)


# 阿图来长颈鹿图书馆做志愿者，图书管理老师让他将books文件夹中的计算机科学书籍移动到“计算机科学”文件夹中，阿图之前学习过Python，决定利用Python来快速分类。
# books文件夹路径：/Users/giraffe/books
# 所有文件命名方式：书名.docx
# 根据长颈鹿图书馆中的类别进行分类，文档路径为：/Users/giraffe/长颈鹿图书馆.xlsx
# 文档中的格式如下图所示
# 分类后的文件移动到：/Users/giraffe/计算机科学
