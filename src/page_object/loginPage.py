from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from .base import Page


class Login(Page):
    '''
    用户登录
    '''

    url = '/'
    login_user_loc_xpath = (By.XPATH, '//*[@id="app"]/div[1]/form/div[1]/div/div/input')
    login_password_loc_xpath = (By.XPATH, '//*[@id="app"]/div[1]/form/div[2]/div/div/input')
    login_button_xpath = (By.XPATH, '//*[@id="app"]/div[1]/div[4]')

    def bz_login_name(self):
        self.find_element(*self.login_user_loc_xpath).click()
        sleep(1)
       # self.find_element(*self.login_password_loc_xpath).click()

    def bz_login_password(self):
        self.find_element(*self.login_password_loc_xpath).click()
        sleep(1)

    def login_username(self, username):
        self.find_element(*self.login_user_loc_xpath).send_keys(username)

    def login_password(self, password):
        self.find_element(*self.login_password_loc_xpath).send_keys(password)

    def login_button(self):
        self.find_element(*self.login_button_xpath).click()

    def user_login(self, username="chenyan", password="123456"):
        """获取用户名密码登录"""
        self.open()
        self.bz_login_name()
        self.login_username(username)
        self.bz_login_password()
        self.login_password(password)
        self.login_button()
        sleep(1)
