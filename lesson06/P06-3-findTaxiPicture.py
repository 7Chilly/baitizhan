import os
import ezexif
import shutil

sourcePath = "/Users/chilly/Desktop/python/yequ/崩溃的阿文/problem06-3"
downloadPath = os.path.join(sourcePath, "照片")
newPath = os.path.join(sourcePath, "2015年")
allItems = os.listdir(downloadPath)
for item in allItems:
    itemPath = os.path.join(downloadPath, item)
    exifInfo = ezexif.process_file(itemPath)
    takeTime = exifInfo["EXIF DateTimeOriginal"]
    DateTime = takeTime.split(" ")[0]
    DateTimeParts = DateTime.split(":")
    if DateTimeParts[0] == "2015" and DateTimeParts[1] == "10":
        itemNewPath = os.path.join(newPath, item)
        shutil.copy(itemPath, itemNewPath)

# 阿英的租车公司最近陷入一场车辆纠纷，为了找到出租前的车况照片，阿英需要快速找到2015年10月拍摄的车况照片，复制照片到2015年文件夹并发给法务。
# 所有照片路径：/Users/taxi/照片
# 找到2015年的照片复制到：/Users/taxi/2015年


#啊啊啊DateTime和DateTimeParts在切片之后得到的都是字符串啊啊啊啊！！！
#呜呜呜怎么总是忘记呢！
