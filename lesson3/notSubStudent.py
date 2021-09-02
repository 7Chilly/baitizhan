import os

itemsPath = "/Users/chilly/Desktop/python/yequ/爱整理的阿文/day3/project"
allItems = os.listdir(itemsPath)
for item in allItems:
    targetPath = os.path.join(itemsPath, item)
    allDocuments = os.listdir(targetPath)
    document1 = (f"开题报告_{item}.docx")
    document2 = (f"中期报告_{item}.docx")
    document3 = (f"任务书_{item}.docx")
    document4 = (f"指导记录表_{item}.docx")
    if document1 not in allDocuments:
        print(f"{item}没有交开题报告")
    elif document2 not in allDocuments:
        print(f"{item}没有交中期报告")
    elif document3 not in allDocuments:
        print(f"{item}没有交任务书")
    elif document4 not in allDocuments:
        print(f"{item}没有交指导记录表")
