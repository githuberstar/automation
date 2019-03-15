from selenium.webdriver import Remote
from threading import Thread
from selenium import webdriver


lists = {'http://192.168.19.102:5555/wd/hub': 'chrome', 'http://192.168.19.102:5556/wd/hub': 'chrome'}
option = webdriver.ChromeOptions()
# option.add_argument(r"--user-data-dir=D:\\Selenium\\chrome_user_data")
option.add_argument(r"--user-data-dir=D:\\File\\chrome_user_data")
# option.experimental_options('--user-data-dir', 'D:\\Selenium\\chrome_user_data')
# option.add_experimental_option('--user-data-dir', 'D:\\Selenium\\chrome_user_data')


def browser_driver(host, browser_name):
    driver = Remote(command_executor=host,
                    desired_capabilities={'platform': 'ANY',
                                          'browserName': browser_name,
                                          'version': '',
                                          'javascriptEnabled': True
                                         },
                    options=option
                    )
    return driver


