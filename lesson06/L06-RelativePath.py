import os
import ezexif
import shutil

os.chdir("/Users/chilly/Desktop/python/yequ/崩溃的阿文/lesson06")
downloadPath = "照片"
photoList = os.listdir(downloadPath)

for photo in downloadPath:
    photoPath = os.path.join(downloadPath, photo)
    exifInfo = ezexif.process_file(photoPath)
    # 获取拍摄时间
    takeTime = exifInfo["EXIF DateTimeOriginal"]
    # 通过空格分隔成拍摄日期和拍摄时间
    takeTimeParts = takeTime.split(" ")
    # 分隔后的字符串列表第一个元素就是拍摄日期，赋值给变量photoDate
    photoDate = takeTimeParts[0]
    # 再把拍摄日期通过冒号分隔，分成年、月、日三部分，赋值给变量photoDateParts
    photoDateParts = photoDate.split(":")

    targetFolderName = f"{photoDateParts[0]}年{photoDateParts[1]}月"
    photoTargetPath = os.path.join(downloadPath, targetFolderName)

    if not os.path.exists(photoTargetPath):
        os.mkdir(photoTargetPath)
    shutil.move(photoPath,targetFolderName)
