import os
import shutil
os.chdir("/Users/chilly/Desktop/python/yequ/崩溃的阿文/backup2")
downloadPath = "学生信息"
for item in os.listdir(downloadPath):
    studentClass = item[4:6]
    sourcePath = os.path.join(downloadPath, item)
    targetPath = f"{studentClass}班"
    if not os.path.exists(targetPath):
        os.mkdir(targetPath)
    shutil.move(sourcePath, targetPath)



# 题目：
# 夜曲大学2020届新生入学，入学前每个学生按照 学号+姓名 的方式在系统上提交了个人信息。
# 教务老师提前将学生资料下载到了移动硬盘中，为方便各班主任查看学生信息，现在需要将硬盘中的学生信息按照班级进行分类。
# 资料存储绝对路径：/Volumes/backup/学生信息
# 硬盘路径： /Volumes/backup
# 文件命名： 入学年+班级+序号+名字
# 例如：20200123小张.docx
# 按照班级分类，小张的班级为01，就放入01班的文件夹。
