import os
allItems = os.listdir()


def sortFile(name):
    chapter = os.path.splitext(name)[0]
    return int(chapter)


allItems.sort(key=sortFile)
print(allItems)
