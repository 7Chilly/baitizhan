import os
import docx
import openpyxl
import pdfplumber
import re

def findNum(string):
    NumList = []
    pattern = re.compile(r"\d+")
    res = re.findall(pattern, string)
    for number in res:
        lenNumber = len(number)
        if lenNumber == 11:
            NumList.append(number)
    return NumList


def getList(searchPath):
    PDFList = []
    allItems = os.listdir(searchPath)
    for item in allItems:
            itemPath = os.path.join(searchPath, item)
            if os.path.isdir(itemPath):
                getList(itemPath)

            extension = os.path.splitext(item)[1].lower()
            if extension == ".pdf":
                pdf = pdfplumber.open(itemPath)
                for page in pdf.pages:
                    pageText = page.extract_text()
                    newNum = findNum(pageText)
                    if newNum == None:
                            continue
                    PDFList += newNum
                for page in pdf.pages:
                    table = page.extract_tables()[0]
                    for row in table:
                        for cell in row:
                            cellText = str(cell)
                            newNum = findNum(cellText)
                            if newNum == None:
                                continue
                            if newNum == "15011932792":
                                print("yes")
                            PDFList += newNum
    PhoneList = PDFList
    if "13944608722" in PhoneList:
        print("haha")
    return PhoneList

PhoneList = getList("/Users/chilly/Desktop/python/yequ/再见啦/problem25")
if "13944608722" in PhoneList:
    print("ok")

phoneList = list(set(PhoneList))
print(phoneList)
if "13944608722" in phoneList:
    print("yes")
