from selenium import webdriver
from .driver import browser_driver
# from .driver import thread_test
import unittest
import os

lists = {'http://192.168.19.102:5555/wd/hub': 'chrome', 'http://192.168.19.102:5556/wd/hub': 'chrome'}


class MyTest(unittest.TestCase):
    def setUp(self):
        # self.driver = browser_driver('http://192.168.5.125:4444/wd/hub', 'chrome') # 大坑 不要忘了/wd/hub
        self.driver = browser_driver('http://127.0.0.1:4444/wd/hub', 'chrome') # 大坑 不要忘了/wd/hub
        #self.driver = webdriver.Chrome()
        #self.driver = thread_test()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()


class Te(MyTest):
    def test(self):
        print(1)
if __name__ == "__main__":
    unittest.main(warnings='ignore')
