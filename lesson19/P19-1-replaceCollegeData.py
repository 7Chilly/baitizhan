import openpyxl

wb = openpyxl.load_workbook("夜曲大学英语考试成绩.xlsx")
ws = wb["汇总"]
for row in ws.rows:
    college = row[2].value
    college = college.replace("计算机学院", "计算机科学与技术学院")
    college = college.replace("机械科学与技术学院", "机械制造科学与技术学院")
    row[2].value = college
wb.save("新-夜曲大学英语考试成绩.xlsx")
