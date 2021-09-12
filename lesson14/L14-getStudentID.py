# 使用import导入os模块
import os
import docx

allItems = os.listdir()

allStudentsData = []

for item in allItems:
    studentData = {}

    fileName = os.path.splitext(item)[0]
    studentData["classInfo"] = fileName.split("-")[0]
    studentData["name"] = fileName.split("-")[1]

    keyPath = item
    doc =docx.Document(keyPath)

    idPara = doc.paragraphs[3]
    idRun = idPara.runs[1]
    studentData["id"] = idRun.text

    allStudentsData.append(studentData)

print(allStudentsData)
