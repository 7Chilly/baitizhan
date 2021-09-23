import os
import shutil
import openpyxl
wb = openpyxl.load_workbook("汇总.xlsx")
bSheet = wb["面试教师名单"]
path = "teacher"
allItems = os.listdir(path)
for item in allItems:
    extension = os.path.splitext(item)[1]
    if extension != ".docx":
        continue
    info = os.path.splitext(item)[0]
    name = info.split("-")[0]
    for row in bSheet.rows:
        if row[0].value == name:
            job = row[8].value
            jobPath = os.path.join(path, job)
            if not os.path.exists(jobPath):
                os.mkdir(jobPath)
            sourcePath = os.path.join(path, item)
            if not os.path.isdir(sourcePath):
                shutil.move(sourcePath, jobPath)
