import os
import shutil

downloadPath = "/Users/chilly/Desktop/python/yequ/爱整理的阿文/project"
allItems = os.listdir(downloadPath)
for item in allItems:
    name = os.path.splitext(item)[0].split("_")[1]
    sourcePath = os.path.join(downloadPath, item)
    targetPath = os.path.join(downloadPath, name)
    if not os.path.exists(targetPath):
        os.mkdir(targetPath)
    if not os.path.isdir(sourcePath):
        shutil.move(sourcePath, targetPath)
