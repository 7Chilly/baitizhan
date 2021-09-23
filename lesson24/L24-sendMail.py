import smtplib
from email.mime.text import MIMEText
from email.header import Header
import openpyxl

mailHost = "smtp.qq.com"
mailUser = "xixihaha@qq.com"
mailPass = "dididada"

wb = openpyxl.load_workbook("汇总.xlsx")
nameSheet = wb["教师信息登记表"]
teacherMail = {}
for row in nameSheet.rows:
    name = row[0].value
    mail = row[10].value
    teacherMail[name] = mail
smtpObj = smtplib.SMTP_SSL(mailHost, 465)
smtpObj.login(mailUser, mailPass)
sender = mailUser
receiverList = teacherMail.items()
for item in receiverList:
    name = item[0]
    receiver = item[1]
    if name == "姓名":
        continue
    message = MIMEText(f"{name}老师您好，恭喜您通过夜曲大学的筛选，现邀请您参加面试", "plain", "utf-8")
    message["Subject"] = Header("夜曲大学面试邀请通知")
    message["From"] = Header(f"夜曲大学教务处 <{sender}>")
    message["To"] = Header(f"{name}老师 <{receiver}>")
    smtpObj.sendmail(sender, receiver, message.as_string())
    print(f"{name}邮件发送成功")
