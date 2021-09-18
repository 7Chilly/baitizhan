import os
allItems = os.listdir()


def sortFile(fileName):
    chapter = os.path.splitext(fileName)[0].split("-")[1]
    return int(chapter)


allItems.sort(key=sortFile)
print(allItems)

