from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from src.page_object.base import Page
import unittest


class PageSon(Page):
    path = (By.XPATH, 'www')
    path2 = (By.ID, 'kw')

    def click(self):
        try:
            self.find_element(*self.path).click()
            self.find_element(*self.path2).click()
        except Exception as mes:
            print('111')


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = Chrome()  # 大坑 不要忘了/wd/hub
        self.driver.get('http://www.baidu.com')

    def test_12(self):
        page = PageSon(self.driver)
        page.click()


if __name__ == "__main__":
    unittest.main()
