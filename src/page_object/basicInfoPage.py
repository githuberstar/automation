from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .base import Page
from .loginPage import Login
import time
from ..tools import remote_exe
import os

url = '/'


class Login2(Page):
    """登录"""
    new_button = (By.XPATH, '//*[@id="quickaccept"]/img')

    def __init__(self, selenium_driver, base_url=url, parent=None):
        # 用super调用父类的构造函数会报错，以后看
        Page.__init__(self, selenium_driver, base_url=base_url, parent=None)
        Login(self.driver).user_login(username='chenyan', password='123456')

    def new_business(self):
        self.find_element(*self.new_button).click()
        time.sleep(1)
        self.driver.switch_to.frame('busAccept100000')


class BasicInfo(Page):
    """基本信息录入"""

    url = '/'
    notary_class_xpath = (By.XPATH, '//*[@id="app"]/div[4]/div[1]/form/div[1]/div[1]/div/div/div/div/div[1]/input')
    notary_class_value = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[3]/span')
    useland = (By.XPATH, '//*[@id="app"]/div[4]/div[1]/form/div[1]/div[2]/div/div/div/input')
    use_land_other = (By.XPATH, '//*[@id="app"]/div[4]/div[1]/form/div[1]/div[3]/div/div/label')
    notary_purpose_id = (By.XPATH, '//*[@id="app"]/div[4]/div[1]/form/div[1]/div[4]/div/div/div/div/div[1]/input')
    notary_purpose_value = (By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[4]')
    notary_service_id = (By.XPATH, '//*[@id="app"]/div[4]/div[1]/form/div[2]/div[3]/div/div/div/div/div[2]/input')
    notary_service_value = (By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul/li[3]')
    assist_id = (By.XPATH, '//*[@id="app"]/div[4]/div[1]/form/div[2]/div[1]/div/div/div/div/div[2]/input')
    assist_value = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[5]')

    def notary_category(self):
        """公证类别"""
        self.find_element(*self.notary_class_xpath).click()
        self.find_element(*self.notary_class_value).click()

    def use_land(self):
        """使用地"""
        self.find_element(*self.useland).click()
        self.find_element(*self.useland).send_keys("567")
        self.find_element(*self.use_land_other).click()

    def notary(self):
        pass

    def notary_purpose(self):
        """公正用途"""
        self.find_element(*self.notary_purpose_id).click()
        self.find_element(*self.notary_purpose_value).click()

    def notary_assistant(self):
        """公证助理"""
        self.find_element(*self.assist_id).click()
        self.find_element(*self.assist_value).click()

    def delivery_method(self):
        pass

    def service_type(self):

        self.find_element(*self.notary_service_id).click()
        self.find_element(*self.notary_service_value).click()

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


class Applier(Page):
    """添加申请人信息"""
    add_applier_button = (By.XPATH, '//*[@id="app"]/div[4]/div[3]/div[1]/div[1]/button[2]')
    nature_person = (By.XPATH, '//*[@id="app"]/div[4]/div[3]/div[1]/div[1]/div[1]/div[1]')
    name = (By.XPATH, '//*[@id="app"]/div[4]/div[3]/div[3]/div/div[1]/div[2]/div[2]/form/div/div[3]/div/div/div/div/input')
    id_card = (By.XPATH, '//*[@id="app"]/div[4]/div[3]/div[3]/div/div[1]/div[2]/div[2]/form/div/div[4]/div/div/div/div[2]/div/input')
    id_number = (By.XPATH, '//*[@id="app"]/div[12]/div/div[2]/div[1]/div[3]/table/tbody')
    save = (By.XPATH, '//*[@id="app"]/div[4]/div[3]/div[3]/div/div[1]/div[3]/div[2]/button')

    def add_applier(self):
        # 添加申请人
        self.find_element(*self.add_applier_button).click()
        # 自然人
        self.find_element(*self.nature_person).click()
        self.find_element(*self.name).click()
        self.find_element(*self.name).send_keys('朱继慧')
        self.find_element(*self.id_card).click()
        id_number_button = self.find_element(*self.id_number)
        ActionChains(self.driver).double_click(id_number_button).perform()
        time.sleep(1)
        self.find_element(*self.save).click()
        time.sleep(1)


class NotarizationMatter(Page):
    """公证事项"""
    notarization_matter_tab = (By.XPATH, '//*[@id="app"]/div[4]/div[2]/div[3]')
    notarization_matter_add_button = (By.XPATH, '//*[@id="app"]/div[4]/div[3]/div[1]/div[1]/button')
    common_matter = (By.XPATH, '//*[@id="app"]/div[4]/div[3]/div[2]/div[2]/div/div[3]/table/tbody/tr/td[1]')

    def add_notarization_matter(self):
        # 公证事项
        self.find_element(*self.notarization_matter_tab).click()
        self.find_element(*self.notarization_matter_add_button).click()
        self.find_element(*self.common_matter).click()
        time.sleep(1)


class NotarizationDocuments(Page):
    """卷宗资料"""
    notarization_document = (By.XPATH, '//*[@id="app"]/div[4]/div[2]/div[4]')
    ask_record = (By.XPATH, '//*[@id="app"]/div[4]/div[3]/div[1]/div[5]/div[1]/button[2]')
    certificate = (By.XPATH, '//*[@id="app"]/div[4]/div[3]/div[1]/div[6]/div[1]/button[2]')
    commit = (By.XPATH, '//*[@id="app"]/div[4]/div[3]/div[1]/div[5]/div[5]/div[3]/button')

    def add_notarization_document(self):
        # 公证文书
        self.find_element(*self.notarization_document).click()
        self.find_element(*self.ask_record).click()
        self.find_element(*self.commit).click()
        time.sleep(20)

        # 手工操作
        remote_exe()
        time.sleep(20)

        exit = '//*[@id="app"]/div[4]/div[1]/div/div[1]/button[4]/span'
        queren2 = '//*[@id="app"]/div[4]/div[3]/div[1]/div[6]/div[4]/div[3]/button'
        self.find_element(exit).click()
        self.find_element(*self.certificate).click()
        self.find_element(queren2).click()
        time.sleep(8)


class ExpenseCalculator(Page):
    """费用计算器"""
    expense_calculator_button = (By.XPATH, '//*[@id="laaa"]/div[2]')
    commit = (By.XPATH, '//*[@id="app"]/div[7]/div[1]/div[3]')

    def charge_fee(self):
        # 收费
        self.find_element(*self.expense_calculator_button).click()
        self.find_element(*self.commit).click()
        time.sleep(11)


class FileInformation(Page):
    """卷宗资料"""
    pic_url = 'C:\\Users\\zhujihui\\Pictures\\handwriting.png'
    file_information_button = (By.XPATH, '//*[@id="laaa"]/div[3]/div')
    application_form = (By.XPATH, '//*[@id="app"]/div[8]/div[2]/div[1]/div[2]/div/div/div/div[8]/span')
    upload = (By.XPATH, '//*[@id="app"]/div[8]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div/input')
    notification = (By.XPATH, '//*[@id="app"]/div[8]/div[2]/div[1]/div[2]/div/div/div/div[16]/span')
    party = (By.XPATH, '//*[@id="app"]/div[8]/div[2]/div[1]/div[2]/div/div/div/div[10]/span')
    acceptance_form = (By.XPATH, '//*[@id="app"]/div[8]/div[2]/div[1]/div[2]/div/div/div/div[14]/span')

    def add_file_infomation(self):
        # 上传卷宗资料
        self.find_element(*self.file_information_button).click()
        self.find_element(*self.application_form).click()
        self.find_element(*self.upload).send_keys(*self.pic_url)
        time.sleep(0.5)
        self.find_element(*self.party).click()
        self.find_element(*self.upload).send_keys(*self.pic_url)
        time.sleep(0.5)
        self.find_element(*self.acceptance_form).click()
        self.find_element(*self.upload).send_keys(*self.pic_url)
        time.sleep(0.5)
        self.find_element(*self.notification).click()
        self.find_element(*self.upload).send_keys(*self.pic_url)

        time.sleep(1)


class Commit(Page):
    """上报签批"""
    def click_commit(self):
        # 上报签批
        sbqp_button = '//*[@id="app"]/div[9]/div[1]/button'
        qianpiren = '//*[@id="app"]/div[5]/div/div/div[2]/div[2]/div/span[2]/div/div[1]/input'
        sbqp_button2 = '//*[@id="app"]/div[5]/div/div/div[3]/button[1]'
        sbqp_button3 = '/html/body/div[6]/div/div[3]/button[2]'
        qianfagao = '//*[@id="app"]/div[5]/div/div/div[2]/div[3]/span[2]/span[3]'
        qianfagao_quit = '//*[@id="app"]/div[6]/div[1]/button[3]'
        self.find_element(sbqp_button).click()
        time.sleep(10)
        self.find_element(qianfagao).click()
        time.sleep(5)
        self.find_element(qianfagao_quit).click()
        time.sleep(2)
        self.find_element(sbqp_button2).click()
        self.find_element(sbqp_button3).click()
        time.sleep(1)
