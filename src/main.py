from src.test_case_1.reportingForEndorsement_sta import ReportingForEndorsementTest
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium.webdriver import Remote
from threading import Thread
import smtplib
import unittest
import time
import os
import sys

sys.path.append( 'D:\\File\\python\\bztest\\src')
print(sys.path)

testreport = 'D:\\File\\python\\bztest\\src\\report\\reports'


def new_report(report):
    lists = os.listdir(report)
    lists.sort(key=lambda fn: os.path.getatime(report+"\\"+fn))
    file_new = os.path.join(report, lists[-1])
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


def browser_driver(host, browser_name):
    driver = Remote(command_executor=host,
                    desired_capabilities={'platform': 'ANY',
                                          'browserName': browser_name,
                                          'version': '',
                                          'javascriptEnabled': True
                                        }
                    )
    return driver


if __name__ == "__main__":
    test_suit = unittest.TestSuite()  # 创建测试用例集，unittest.main()是找出所有的test开头的测试用例
    test_suit.addTest(ReportingForEndorsementTest("test_notarization_documents"))  # 向测试用例集添加测试用例
    now = time.strftime("%Y%m%d_%H%M%S")
    filename = './report/reports/'+'办证系统自动化测试报告'+now+'.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='办证系统自动化测试报告',
                            description='模块的用例执行情况：')
    runner.run(test_suit)
    fp.close()
    newreport1 = new_report(testreport)
    send_mail(newreport1)

# 以后再弄多线程
# if __name__ == "__main__":
#     lists = {'http://127.0.0.1:4444/wd/hub': 'chrome',
#              'http://192.168.5.125:4444/wd/hub': 'chrome'}
#     threads = []
#     files = range(len(lists))
#
#     for host, browser in lists.items():
#         t = Thread(target=multithread, args=(host, browser))
#         threads.append(t)
#
#     for i in files:
#         threads[i].start()
#     for i in files:
#         threads[i].join()

