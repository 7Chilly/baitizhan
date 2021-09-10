import os
import openpyxl

studentName = ['吕婷婷', '肖槐', '魏皖怡', '胡轶轩', '包印雪', '谭彦', '周宇', '吴琪', '龚静雯', '张思思', '潘婷', '夏乐群', '朱佩玉', '隋胜男', '朱薇', '唐梅', '罗勇', '林贸然', '张丽', '张可馨', '汪洋', '韩明希', '杜宇琳', '胡连群', '岳海洋', '李雅梦', '蔡林芮', '孟轩', '项文彦', '苏培坤', '惠红', '顾洪彬', '卡欣', '陶振英', '子顺', '成洛', '邹德浩', '王思亮', '叶家有', '王德滋', '杨少帆', '谢福顺', '刘军', '李多钰']

allItems = os.listdir()
handinNameList = []
for item in allItems:
    fileName = os.path.splitext(item)[0]
    name = fileName.split("-")[1]
    handinNameList.append(name)

wb = openpyxl.Workbook()
workSheet = wb["Sheet"]
workSheet.title = "七年级六班"
for student in studentName:
    if student in handinNameList:
        workSheet.append([student])
    else:
        workSheet.append([student, "x"])
wb.save("夜曲中学七年级六班回执提交情况.xlsx")



# 今年夜曲中学端午节的放假通知是一份Word文档，家长们阅读签字后需将文件名改为"学生班级-学生姓名-端午节放假通知回执.docx"发回给班主任。
# 乔老师是七年级六班的班主任，班上一共有44名学生，所有学生的姓名都已经存储在了studentName列表中。
# 乔老师把已交的回执下载到了路径为 /Users/qiao/回执 的文件夹下。

# 目前还有一些同学没有交回执，乔老师需要先创建一个有全班同学姓名的工作簿，里面有一张工作表，名称为“七年级六班”，然后将这些未交回执的学生后面的单元格内标上“x”（小写字母x)
# 最后，别忘记将Excel表格保存到 /Users/qiao/回执/夜曲中学七年级六班回执提交情况.xlsx 路径下哦。
