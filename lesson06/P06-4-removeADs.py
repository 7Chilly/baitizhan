import os
import shutil

downloadPath = "/Users/chilly/Desktop/python/yequ/崩溃的阿文/problem06-4/素材"
allItems = os.listdir(downloadPath)
print(allItems)
for item in allItems:
    oldItemPath = os.path.join(downloadPath, item)
    newName = item.replace("[夜曲资源网]","")
    newItemPath = os.path.join(downloadPath, newName)
    shutil.move(oldItemPath, newItemPath)
newItems = os.listdir(downloadPath)
print(newItems)

# 小明喜欢在“夜曲资源网”下载各种MP3音效素材，但这种资源网站为了给自己打广告，喜欢在资源的文件名中添加自己的网站名称。
# 例如：
# 欢呼[夜曲资源网].mp3
# 呼噜声[夜曲资源网].mp3
# 男惨叫声[夜曲资源网].mp3
# 小明下载素材的文件夹在 /Users/ming/素材 路径下，请先输出该路径下所有的文件列表。
# 然后运用文件自动化操作的相关知识，帮助小明把所有资源文件名里的[夜曲资源网]去掉。
# 广告去掉后再次输出该路径文件列表。
