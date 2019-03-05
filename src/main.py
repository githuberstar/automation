from src.test_case_1.reportingForEndorsement_sta import ReportingForEndorsementTest
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import unittest
import time
import os
import sys

sys.path.append( 'D:\\File\\python\\bztest\\src')
print(sys.path)


def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getatime(testreport+"\\"+fn))
    file_new = os.path.join(testreport, lists[-1])
    return file_new


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


if __name__ == "__main__":
    testreport = 'D:\\File\\python\\bztest\\src\\report\\reports'
    test_suit = unittest.TestSuite()
    test_suit.addTest(ReportingForEndorsementTest("test_basic"))

    now = time.strftime("%Y%m%d_%H%M%S")
    filename = './report/reports/'+'办证系统自动化测试报告'+now+'.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='办证系统自动化测试报告',
                            description='模块的用例执行情况：')
    runner.run(test_suit)
    fp.close()
    new_report = new_report(testreport)
    send_mail(new_report)
