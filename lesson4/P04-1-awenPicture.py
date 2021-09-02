import os
import shutil
sourcePath = "/Users/chilly/Desktop/python/yequ/爱整理的阿文/awen/source"
targetPath = "/Users/chilly/Desktop/python/yequ/爱整理的阿文/awen/animal"

targetItems = ['东北虎.jpg', '非洲最美猎豹.jpg', '非洲最美长颈鹿.jpg', '几维鸟.jpg']

for item in targetItems:
    beforePath = os.path.join(sourcePath, item)
    shutil.move(beforePath, targetPath)
