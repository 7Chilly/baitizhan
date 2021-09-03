import os
def findBigFile(Path):
    allItems = os.listdir(Path)
    for item in allItems:
        nextItemPath = os.path.join(Path, item)
        if os.path.isdir(nextItemPath):
            findBigFile(nextItemPath)
        else:
            fileSize = os.path.getsize(nextItemPath)
            if fileSize > 2000:
                print(nextItemPath)

findBigFile("/Users/Yoyo/")


#题目：
#硬盘满了！
#Yoyo的电脑可用的硬盘空间不够用了，这种情况一般最有效的方式是找出电脑里大文件。
#她隐约记得/Users/Yoyo/这个文件夹路径下有一些占用空间比较大的文件，但有的可能还在子文件夹下甚至子文件夹的子文件夹下，这样一个一个手动去找的话，比较耗时。
#请帮助Yoyo找出/Users/Yoyo/路径文件夹及其子文件夹下空间占用大于2000字节的文件并输出它们的文件路径。
