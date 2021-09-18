import os

allItems = os.listdir()
chapterList = []
for item in allItems:
    chapter = os.path.splitext(item)[0].split("-")[1]
    chapterList.append(chapter)
chapterList.sort(key=int)
newFileList = []

for i in chapterList:
    for item in allItems:
        newName = os.path.splitext(item)[0].split("-")[1]
        if newName == i:
            newFileList.append(item)

print(newFileList)
