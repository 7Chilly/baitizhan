import os
import shutil
allFormPath = os.listdir()
print(allFormPath)

for item in allFormPath:
    fileName = os.path.splitext(item)[0]
    subject = fileName.split("-")[1]
    if not os.path.exists(subject):
        os.mkdir(subject)
    shutil.move(item, subject)

allFormPath = os.listdir()
print(allFormPath)


# 夜曲支教协会负责人已经无情地将不按照要求命名的报名表全部移走了！
# 剩下的报名表依旧在 /Users/yequ/Downloads/registration 路径下。
# 现在，他将把剩下的报名表按照意愿科目进行分类，把报名表移动到对应的意愿科目文件夹中。
# 比如，"刘心逸-体育-五年级.docx"将会被移动到路径为 /Users/yequ/Downloads/registration/体育 的文件夹中。
# 请先使用print输出allFormPath路径下所有的文件名，再在分类后，使用print输出该路径下所有的文件夹名。
