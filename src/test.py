from selenium.webdriver import Remote
from selenium.webdriver import Chrome
from selenium import webdriver


driver = Remote(command_executor='http://192.168.5.127:4444',
                desired_capabilities={'platform': 'ANY',
                                      'browserName': 'chrome',
                                      'version': '', 'javascriptEnabled': True})
driver.get('http://www.baidu.com')
