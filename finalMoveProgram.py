import os
import shutil

#遍历downloads文件夹里的文件（夹）名
downloadPath = "/Users/chilly/Desktop/python/yequ/爱整理的阿文/Downloads"
allItems = os.listdir(downloadPath)
for item in allItems:
    #获取文件名后缀小写
    extension = os.path.splitext(item)[1].lower()

    targetPath = []
    if extension in [".jpg", ".jpeg", ".gif", ".png", ".bmp"]:
        targetPath = os.path.join(downloadPath, "图片文件")

    elif extension in [".avi", ".mp4", ".wmv", ".mov", ".flv"]:
        targetPath = os.path.join(downloadPath, "视频文件")

    elif extension in [".wav", ".mp3", ".mid", ".ape", ".flac"]:
        targetPath = os.path.join(downloadPath, "音频文件")

    elif extension in [".pdf"]:
        targetPath = os.path.join(downloadPath, "PDF文件")

    elif extension in [".docx", ".doc"]:
        targetPath = os.path.join(downloadPath, "Word文件")

    elif extension in [".xlsx", ".xls"]:
        targetPath = os.path.join(downloadPath, "Excel文件")

    elif extension in [".pptx", ".ppt"]:
        targetPath = os.path.join(downloadPath, "PPT文件")

    else:
        targetPath = os.path.join(downloadPath, "其他文件")

    if not os.path.exists(targetPath):
        os.mkdir(targetPath)

    itemPath = os.path.join(downloadPath, item)
    if not os.path.isdir(itemPath):
        shutil.move(itemPath, targetPath)

