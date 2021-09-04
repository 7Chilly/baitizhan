import os
import ezexif
import shutil
downloadPath = "/Users/chilly/Desktop/python/yequ/崩溃的阿文/problem06-2"
os.chdir(downloadPath)
resourcePath = os.path.join(downloadPath, "素材")
changePath = os.path.join(downloadPath, "修改")
if not os.path.exists(resourcePath):
    os.mkdir(resourcePath)
if not os.path.exists(changePath):
    os.mkdir(changePath)

allItems = os.listdir(downloadPath)
for item in allItems:
    if not os.path.isdir(item):
        exifInfo = ezexif.process_file(item)
        filePath = os.path.join(downloadPath, item)
        exifLength = exifInfo["EXIF ExifImageLength"]
        exifWidth = exifInfo["EXIF ExifImageWidth"]
        if float(exifWidth) < 60 and float(exifLength) < 60:
            shutil.move(filePath, resourcePath)
        else:
            shutil.move(filePath, changePath)

# 设计师阿文正在调整素材图片库，她把素材图片放在 picture文件夹中，阿文要在这些素材图片中，找出图片尺寸（长*宽）大于60*60的素材图片。
# 阿文灵机一动，想到了好办法，她可以通过今天学习的ezexif模块，获取图片的长度EXIF ExifImageLength和图片的宽度EXIF ExifImageWidth。
# 通过判断图片的长度和宽度是否小于60，如果小于60，就在一个文件夹中，例如：素材。如果大于60，就放在另一个文件夹中，例如：修改
