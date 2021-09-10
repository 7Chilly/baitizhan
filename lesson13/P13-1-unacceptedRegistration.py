import os
import shutil

downloadPath = "Downloads/registration"
allItems = os.listdir(downloadPath)
print(len(allItems))
os.mkdir("不合格")

for item in allItems:
    filePath = os.path.join(downloadPath, item)
    fileName = os.path.splitext(item)[0]
    InfoList = fileName.split("-")
    if len(InfoList) != 3:
        shutil.move(filePath, "不合格")
        continue

    subjectList = ["语文", "数学", "英语", "体育", "音乐", "安全教育", "美术"]
    if InfoList[1] not in subjectList:
        shutil.move(filePath, "不合格")
        continue

    gradeList = ["一年级", "二年级", "三年级", "四年级", "五年级", "六年级"]
    if InfoList[2] not in gradeList:
        shutil.move(filePath, "不合格")
        continue

allItems = os.listdir(downloadPath)
print(len(allItems))

# 最近，夜曲支教协会举办了一场2020年“最美心灵”大学生暑期支教志愿者招募活动。
# 可竞选科目有：语文、数学、英语、体育、音乐、安全教育、美术
# 可竞选年级有：一年级、二年级、三年级、四年级、五年级、六年级
# 同学们在线上填写完报名表后，需按照“姓名-意愿科目-意愿年级.docx”的格式来进行命名，未按要求命名的报名表会被负责人无情地移动到路径为 /Users/yequ/不合格 文件夹中！
# 支教协会负责人将报名表全部下载到了 /Users/yequ/Downloads/registration 路径下。
# 请先使用print输出最开始的报名表总数量，再在移动了不按要求命名的报名表后，使用print输出移动后的总数量。
