import os
def searchfile(sourcePath):
    allItems = os.listdir(sourcePath)
    for item in allItems:
        itemPath = os.path.join(sourcePath, item)
        if os.path.isdir(itemPath):
            searchfile(itemPath)
        else:
            fileSize = os.path.getsize(itemPath)
            if fileSize == 96592:
                print(itemPath)

searchfile("/Users/chilly/Desktop/python/yequ/崩溃的阿文/problem06-1")

# 阿唐是一家便利店的店员，明天她将离开这家店去另一家分店了。
# 现在有这么一件事让她苦恼，她之前存了一张自己的自拍照到便利店的电脑里，她要在今晚最后在这家店上班的时间把照片找出来，不然别人看到了一定会觉得她很自恋，但问题是她不记得放在什么路径了。
# 好在阿唐的手机里还有这张自拍照，文件名相同的文件没有找到，现在还有一个办法是找一找文件大小（字节数）相同的文件。
# 照片的大小是：96592字节
# 查询路径为：/Users/y11
# 文件找到后输出文件的绝对路径。
