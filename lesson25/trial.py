import re
def findNum(string):
    pattern = re.compile(r"\d+")
    res = re.findall(pattern, string)
    for number in res:
        lenNumber = len(number)
        if lenNumber == 11:
            print(number)

stringList = ["asiofnof 12345678911 ahahaha 12341234567  \n100 13232112332 30 13232112331", "234512342", "sdjiof", ""]
for string in stringList:
    pattern = re.compile(r"\d+")
    res = re.findall(pattern, string)
    for number in res:
        lenNumber = len(number)
        if lenNumber == 11:
            print(number)

