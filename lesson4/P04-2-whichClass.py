import os
import shutil

downloadPath = "/Users/chilly/Desktop/python/yequ/爱整理的阿文/exam"
allItems = os.listdir(downloadPath)
for item in allItems:
    sourcePath = os.path.join(downloadPath, item)
    targetClass = item.split("-")[0]
    targetPath = os.path.join(downloadPath, targetClass)
    if not os.path.exists(targetPath):
        os.mkdir(targetPath)
    if not os.path.isdir(sourcePath):
        shutil.move(sourcePath, targetPath)
