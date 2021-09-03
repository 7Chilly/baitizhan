import os
import shutil

def findAndMove(filePath, targetPath):
    allItems = os.listdir(filePath)
    for item in allItems:
        itemPath = os.path.join(filePath, item)
        if os.path.isdir(itemPath):
            findAndMove(itemPath, targetPath)
        else:
            shutil.move(itemPath, targetPath)

findAndMove("/Users/chilly/Desktop/python/yequ/崩溃的阿文/Desktop/awen", "/Users/chilly/Desktop/python/yequ/崩溃的阿文/Desktop/rearrange")

#啊我好笨！TAT
#题目：
#阿文的新同事拿到工作交接文件后，发现该文件夹中有各种类型的文件和文件夹，为了快速预览工作交接内容，新同事打算将该文件夹中的所有文件取出放入一个文件夹中。
#现在该同事拿到文件夹awen，该文件夹中有各种文件，如下图所示：
#阿文给的文件路径：/Users/Desktop/awen
#文件夹里的文件统一移动到：/Users/Desktop/rearrange
