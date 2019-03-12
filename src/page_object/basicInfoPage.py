from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .base import Page
from .loginPage import Login
import time

url = '/'


class BasicInfo(Page):

    url = '/'
    notary_class_xpath = (By.XPATH, '//*[@id="app"]/div[4]/div[1]/form/div[1]/div[1]/div/div/div/div/div[1]/input')
    notary_class_value = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[2]/span')
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
        """使用地"""
        use_land = (By.XPATH, '//*[@id="app"]/div[4]/div[1]/form/div[1]/div[2]/div/div/div/input')
        self.find_element(use_land).click()
        self.find_element(use_land).send_keys("567")
        self.find_element(use_land).click()

    def notary(self):
        pass

    def notary_purpose(self):
        """公正用途"""
        notary_purpose_id = '//*[@id="app"]/div[4]/div[1]/form/div[1]/div[4]/div/div/div/div/div[1]/input'
        notary_purpose_value = '/html/body/div[3]/div[1]/div[1]/ul/li[4]'
        self.find_element(notary_purpose_id).click()
        self.implicitly_wait(10)
        self.find_element(notary_purpose_value).click()

    def notary_assistant(self):
        """公证助理"""
        assist_id = '//*[@id="app"]/div[4]/div[1]/form/div[2]/div[1]/div/div/div/div/div[2]/input'
        assist_value = '/html/body/div[4]/div[1]/div[1]/ul/li[5]'
        self.find_element(assist_id).click()
        self.implicitly_wait(10)
        self.find_element(assist_value).click()

    def delivery_method(self):
        pass

    def service_type(self):
        notary_service_id = '//*[@id="app"]/div[4]/div[1]/form/div[2]/div[3]/div/div/div/div/div[2]/input'
        notary_service_value = '/html/body/div[5]/div[1]/div[1]/ul/li[3]'
        self.find_element(notary_service_id).click()
        self.implicitly_wait(10)
        self.find_element(notary_service_value).click()
        self.implicitly_wait(10)

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

    def __init__(self, selenium_driver, base_url=url, parent=None):
        # 用super调用父类的构造函数会报错，以后看
        Page.__init__(self, selenium_driver, base_url=base_url, parent=None)
        Login(self.driver).user_login(username='chenyan', password='123456')

    def add_applier(self):
        # 添加申请人
        add_applier = '//*[@id="app"]/div[4]/div[3]/div[1]/div[1]/button[2]'
        self.find_element(add_applier).click()
        # 自然人
        natual_person = '//*[@id="app"]/div[4]/div[3]/div[1]/div[1]/div[1]/div[1]'
        name = '//*[@id="app"]/div[4]/div[3]/div[3]/div/div[1]/div[2]/div[2]/form/div/div[3]/div/div/div/div/input'
        id_card = '//*[@id="app"]/div[4]/div[3]/div[3]/div/div[1]/div[2]/div[2]/form/div/div[4]/div/div/div/div[2]/div/input'
        id_number = '//*[@id="app"]/div[11]/div/div[2]/div[1]/div[3]/table/tbody'
        save = '//*[@id="app"]/div[4]/div[3]/div[3]/div/div[1]/div[3]/div[2]/button'
        self.find_element(natual_person).click()
        self.implicitly_wait(10)
        self.find_element(name).click()
        self.find_element(name).send_keys('朱继慧')
        self.implicitly_wait(10)
        self.find_element(id_card).click()
        self.implicitly_wait(10)
        id_number_button = self.find_element(id_number)
        ActionChains(self.driver).double_click(id_number_button).perform()
        time.sleep(1)
        self.find_element_by_xpath(save).click()

class NotaryStaff(Page):
    def __init__(self, selenium_driver, base_url=url, parent=None):
        # 用super调用父类的构造函数会报错，以后看
        Page.__init__(self, selenium_driver, base_url=base_url, parent=None)
        Login(self.driver).user_login(username='chenyan', password='123456')

    def add_notary_staff(self):
        # 公证事项
        gzsx = '//*[@id="app"]/div[4]/div[2]/div[3]'
        add = '//*[@id="app"]/div[4]/div[3]/div[1]/div[1]/button'
        sx = '//*[@id="app"]/div[4]/div[3]/div[2]/div[2]/div/div[3]/table/tbody/tr/td[1]'
        self.find_element(gzsx).click()
        self.find_element(add).click()
        self.find_element(sx).click()
        time.sleep(1)


class Notary_book(Page):
    def __init__(self, selenium_driver, base_url=url, parent=None):
        # 用super调用父类的构造函数会报错，以后看
        Page.__init__(self, selenium_driver, base_url=base_url, parent=None)
        Login(self.driver).user_login(username='chenyan', password='123456')

    def add_notary_book(self):
        # 公证文书
        gzws = '//*[@id="app"]/div[4]/div[2]/div[4]'
        xwbl = '//*[@id="app"]/div[4]/div[3]/div[1]/div[5]/div[1]/button[2]'
        gzs = '//*[@id="app"]/div[4]/div[3]/div[1]/div[6]/div[1]/button[2]'
        queren = '//*[@id="app"]/div[4]/div[3]/div[1]/div[5]/div[5]/div[3]/button'
        self.find_element(gzws).click()
        self.find_element(xwbl).click()
        self.find_element(queren).click()
        time.sleep(14)

        # 手工操作

        exit = '//*[@id="app"]/div[4]/div[1]/div/div[1]/button[4]/span'
        queren2 = '//*[@id="app"]/div[4]/div[3]/div[1]/div[6]/div[4]/div[3]/button'
        self.find_element(exit).click()
        self.find_element(gzs).click()
        self.find_element(queren2).click()
        time.sleep(8)

class Charge(Page):
    def __init__(self, selenium_driver, base_url=url, parent=None):
        # 用super调用父类的构造函数会报错，以后看
        Page.__init__(self, selenium_driver, base_url=base_url, parent=None)
        Login(self.driver).user_login(username='chenyan', password='123456')

        # 收费
        feiyongjisuanqi = '//*[@id="laaa"]/div[2]'
        tijiaoshoufei = '//*[@id="app"]/div[6]/div[1]/div[3]'
        self.find_element(feiyongjisuanqi).click()
        self.find_element(tijiaoshoufei).click()

class Juanzong(Page):
    def __init__(self, selenium_driver, base_url=url, parent=None):
        # 用super调用父类的构造函数会报错，以后看
        Page.__init__(self, selenium_driver, base_url=base_url, parent=None)
        Login(self.driver).user_login(username='chenyan', password='123456')

    def add_juanzong(self):
        # 卷宗资料
        juanzongziliao = '//*[@id="laaa"]/div[3]/div'
        shenqingbiao = '//*[@id="app"]/div[7]/div[2]/div[1]/div[2]/div/div/div/div[8]/span'
        upload = '//*[@id="app"]/div[7]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div/input'
        gaozhishu = '//*[@id="app"]/div[7]/div[2]/div[1]/div[2]/div/div/div/div[16]/span'
        dangshiren = '//*[@id="app"]/div[7]/div[2]/div[1]/div[2]/div/div/div/div[10]/span'
        shoulidan = '//*[@id="app"]/div[7]/div[2]/div[1]/div[2]/div/div/div/div[14]/span'

        self.find_element(juanzongziliao).click()
        self.find_element(shenqingbiao).click()
        self.find_element(upload).send_keys("C:\\Users\\zhujihui\\Pictures\\handwriting.png")
        time.sleep(0.5)
        self.find_element(dangshiren).click()
        self.find_element(upload).send_keys("C:\\Users\\zhujihui\\Pictures\\handwriting.png")
        time.sleep(0.5)
        self.find_element(shoulidan).click()
        self.find_element(upload).send_keys("C:\\Users\\zhujihui\\Pictures\\handwriting.png")
        time.sleep(0.5)
        self.find_element(gaozhishu).click()
        self.find_element(upload).send_keys("C:\\Users\\zhujihui\\Pictures\\handwriting.png")

        self.implicitly_wait(10)

        time.sleep(1)

class Commit(Page):
    def __init__(self, selenium_driver, base_url=url, parent=None):
        # 用super调用父类的构造函数会报错，以后看
        Page.__init__(self, selenium_driver, base_url=base_url, parent=None)
        Login(self.driver).user_login(username='chenyan', password='123456')

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