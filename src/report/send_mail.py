import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from HTMLTestRunner import HTMLTestRunner
from email.header import Header
import unittest
import time, os


def send_mail(file_new):
    smtpserver = "smtp.exmail.qq.com"
    sender = 'zhujihui@enotary.com.cn'
    receiver = 'zhujihui_1991@163.com'
    username = 'zhujihui@enotary.com.cn'
    password = 'Zjh6578602%'
    subject = 'test'

    sendfile = open(file_new, 'rb').read()

    att = MIMEText(sendfile, 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="TestReport.html"'

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = subject
    msgRoot.attach(att)

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)  # 登录的用户名和密码
    smtp.sendmail(sender, receiver, msgRoot.as_string())  # 发送邮件
    smtp.quit()
    print('sendmail success')


if __name__ == '__main__':
    send_mail('D:\\File\\python\\bztest\\src\\test.txt')

