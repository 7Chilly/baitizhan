import os
import re
import docx

def findNum(string):
    pattern = re.compile(r"\d+")
    res = re.findall(pattern, string)
    for i in res:
        Phonenumber = re.compile(r'\d\d\d\d\d\d\d\d\d\d\d')
        m = Phonenumber.search(i)
        if m != None:
            num = m.group()
            return num


def getList(searchPath):
    PhoneList = []
    allItems = os.listdir(searchPath)
    for item in allItems:
        itemPath = os.path.join(searchPath, item)
        if os.path.isdir(itemPath):
            getList(itemPath)
        if os.path.isdir(itemPath):
            continue
        extension = os.path.splitext(item)[1]
        if extension == ".docx":
            doc = docx.Document(itemPath)
            for para in doc.paragraphs:
                for run in para.runs:
                    runText = run.text
                    newNum = findNum(runText)
                    PhoneList.append(newNum)
    NewList = list(set(PhoneList))
    print(NewList)

getList("/Users/chilly/Desktop/python/yequ/再见啦/problem25")
