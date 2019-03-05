from selenium.webdriver.common.by import By
from .base import Page
from .loginPage import Login
import time


class BasicInfo(Page):

    url = '/'
    notary_class_xpath = (By.XPATH, '//*[@id="app"]/div[4]/div[1]/form/div[1]/div[1]/div/div/div/div/div[1]/input')
    notary_class_value = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[2]/span')
    use_land = (By.XPATH, '//*[@id="app"]/div[4]/div[1]/form/div[1]/div[2]/div/div/div/input')
    use_land_other = (By.XPATH, '//*[@id="app"]/div[4]/div[1]/form/div[1]/div[3]/div/div/label')
    new_button = (By.XPATH, '//*[@id="quickaccept"]/img')

    def __init__(self, selenium_driver, base_url=url, parent=None):
        # 用super调用父类的构造函数会报错，以后看
        Page.__init__(self, selenium_driver, base_url=base_url, parent=None)
        Login(self.driver).user_login(username='chenyan', password='123456')

    def new_business(self):
        self.find_element(*self.new_button).click()
        time.sleep(1)
        self.driver.switch_to.frame('busAccept100000')

    def notary_category(self):
        self.find_element(*self.notary_class_xpath).click()
        self.find_element(*self.notary_class_value).click()

    def use_land(self):
        pass

    def notary(self):
        pass

    def notary_purpose(self):
        pass

    def notary_assistant(self):
        pass

    def delivery_method(self):
        pass

    def service_type(self):
        pass

    def acceptance_place(self):
        pass

    def translation(self):
        pass

    def number_of_certificate(self):
        pass

    def value_added_service(self):
        pass

    def urgency(self):
        pass

    def remark(self):
        pass
