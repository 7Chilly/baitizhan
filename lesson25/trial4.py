import os
import docx
import re
import pdfplumber

def findNum(string):
    NumList = []
    pattern = re.compile(r"\d+")
    res = re.findall(pattern, string)
    for number in res:
        lenNumber = len(number)
        if lenNumber == 11:
            NumList.append(number)
    return NumList

searchPath = "/Users/chilly/Desktop/python/yequ/再见啦/problem25/开卡信息/天府五街银行"
PhoneList = []
allItems = os.listdir(searchPath)
for item in allItems:
        itemPath = os.path.join(searchPath, item)
        if os.path.isdir(itemPath):
            continue
        extension = os.path.splitext(item)[1].lower()
        if extension == ".pdf":
            pdf = pdfplumber.open(itemPath)
            for page in pdf.pages:
                pageText = page.extract_text()
                NumList = findNum(pageText)
                PhoneList += NumList
            for page in pdf.pages:
                table = page.extract_tables()
                for row in table:
                    for cell in row:
                        cellText = str(cell)
                        newNum = findNum(cellText)
                        if newNum == None:
                            continue
                        PhoneList += newNum

NewList = list(set(PhoneList))
print(NewList)
if "18044993236" not in NewList:
    print("no")
