from selenium import webdriver
from .driver import browser_driver
import unittest
import os


class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = browser_driver('http://127.0.0.1:5555', 'chrome')
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()
