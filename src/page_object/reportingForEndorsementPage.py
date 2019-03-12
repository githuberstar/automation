# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from .base import Page
import unittest, time, re


class Banzheng(Page):




    def test_banzheng(self):
        #driver = self.driver

        # 登录
        # driver.find_element_by_xpath('//*[@id="app"]/div[1]/form/div[1]/div/div/input').click()
        # driver.find_element_by_xpath('//*[@id="app"]/div[1]/form/div[1]/div/div/input').clear()
        # driver.find_element_by_xpath('//*[@id="app"]/div[1]/form/div[1]/div/div/input').send_keys("chenyan")
        # driver.find_element_by_xpath('//*[@id="app"]/div[1]/form/div[2]/div/div/input').click()
        # driver.find_element_by_xpath('//*[@id="app"]/div[1]/form/div[2]/div/div/input').clear()
        # driver.find_element_by_xpath('//*[@id="app"]/div[1]/form/div[2]/div/div/input').send_keys("123456")
        # driver.find_element_by_xpath('//*[@id="app"]/div[1]/form/div[2]/div/div/input').send_keys(Keys.ENTER)

        self.find_element_by_xpath('//*[@id="quickaccept"]/img').click()
        self.implicitly_wait(10)
        # 切换到iframe
        self.switch_to.frame('busAccept100000')

        # 基本信息录入
        # 公正类别
    def basic_info(self):

        self.find_element_by_xpath(self.notary_class_id).click()
        self.implicitly_wait(10)
        self.find_element_by_xpath(self.notary_class_value).click()

        # 使用地
        driver.find_element_by_xpath(use_land).click()
        driver.find_element_by_xpath(use_land).clear()
        driver.find_element_by_xpath(use_land).send_keys("567")
        driver.find_element_by_xpath(use_land_other).click()

        # 公证员
        # notaryId = '//*[@id="app"]/div[4]/div[1]/form/div[1]/div[3]/div/div/div/div/div[1]/input'

        # 公证用途
        notary_purpose_id = '//*[@id="app"]/div[4]/div[1]/form/div[1]/div[4]/div/div/div/div/div[1]/input'
        notary_purpose_value = '/html/body/div[3]/div[1]/div[1]/ul/li[4]'
        driver.find_element_by_xpath(notary_purpose_id).click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(notary_purpose_value).click()

        # 公证助理
        assist_id = '//*[@id="app"]/div[4]/div[1]/form/div[2]/div[1]/div/div/div/div/div[2]/input'
        assist_value = '/html/body/div[4]/div[1]/div[1]/ul/li[5]'
        driver.find_element_by_xpath(assist_id).click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(assist_value).click()

        # 送达方式
        # receive_class =

        # 服务类别 选择不行
        notary_service_id = '//*[@id="app"]/div[4]/div[1]/form/div[2]/div[3]/div/div/div/div/div[2]/input'
        notary_service_value = '/html/body/div[5]/div[1]/div[1]/ul/li[3]'
        driver.find_element_by_xpath(notary_service_id).click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(notary_service_value).click()
        driver.implicitly_wait(10)

        # 添加申请人
        add_applier = '//*[@id="app"]/div[4]/div[3]/div[1]/div[1]/button[2]'
        driver.find_element_by_xpath(add_applier).click()
        # 自然人
        natual_person = '//*[@id="app"]/div[4]/div[3]/div[1]/div[1]/div[1]/div[1]'
        name = '//*[@id="app"]/div[4]/div[3]/div[3]/div/div[1]/div[2]/div[2]/form/div/div[3]/div/div/div/div/input'
        id_card = '//*[@id="app"]/div[4]/div[3]/div[3]/div/div[1]/div[2]/div[2]/form/div/div[4]/div/div/div/div[2]/div/input'
        id_number = '//*[@id="app"]/div[11]/div/div[2]/div[1]/div[3]/table/tbody'
        save = '//*[@id="app"]/div[4]/div[3]/div[3]/div/div[1]/div[3]/div[2]/button'
        driver.find_element_by_xpath(natual_person).click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(name).click()
        driver.find_element_by_xpath(name).send_keys('朱继慧')
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(id_card).click()
        driver.implicitly_wait(10)
        id_number_button = driver.find_element_by_xpath(id_number)
        ActionChains(driver).double_click(id_number_button).perform()
        time.sleep(1)
        driver.find_element_by_xpath(save).click()

        # 公证事项
        gzsx = '//*[@id="app"]/div[4]/div[2]/div[3]'
        add = '//*[@id="app"]/div[4]/div[3]/div[1]/div[1]/button'
        sx = '//*[@id="app"]/div[4]/div[3]/div[2]/div[2]/div/div[3]/table/tbody/tr/td[1]'
        driver.find_element_by_xpath(gzsx).click()
        driver.find_element_by_xpath(add).click()
        driver.find_element_by_xpath(sx).click()
        time.sleep(1)

        # 公证文书
        gzws = '//*[@id="app"]/div[4]/div[2]/div[4]'
        xwbl = '//*[@id="app"]/div[4]/div[3]/div[1]/div[5]/div[1]/button[2]'
        gzs = '//*[@id="app"]/div[4]/div[3]/div[1]/div[6]/div[1]/button[2]'
        queren = '//*[@id="app"]/div[4]/div[3]/div[1]/div[5]/div[5]/div[3]/button'
        driver.find_element_by_xpath(gzws).click()
        driver.find_element_by_xpath(xwbl).click()
        driver.find_element_by_xpath(queren).click()
        time.sleep(14)

        # 手工操作

        exit = '//*[@id="app"]/div[4]/div[1]/div/div[1]/button[4]/span'
        queren2 = '//*[@id="app"]/div[4]/div[3]/div[1]/div[6]/div[4]/div[3]/button'
        driver.find_element_by_xpath(exit).click()
        driver.find_element_by_xpath(gzs).click()
        driver.find_element_by_xpath(queren2).click()
        time.sleep(8)

        # 收费
        feiyongjisuanqi = '//*[@id="laaa"]/div[2]'
        tijiaoshoufei = '//*[@id="app"]/div[6]/div[1]/div[3]'
        driver.find_element_by_xpath(feiyongjisuanqi).click()
        driver.find_element_by_xpath(tijiaoshoufei).click()

        # 卷宗资料
        juanzongziliao = '//*[@id="laaa"]/div[3]/div'
        shenqingbiao = '//*[@id="app"]/div[7]/div[2]/div[1]/div[2]/div/div/div/div[8]/span'
        upload = '//*[@id="app"]/div[7]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div/input'
        gaozhishu = '//*[@id="app"]/div[7]/div[2]/div[1]/div[2]/div/div/div/div[16]/span'
        dangshiren = '//*[@id="app"]/div[7]/div[2]/div[1]/div[2]/div/div/div/div[10]/span'
        shoulidan = '//*[@id="app"]/div[7]/div[2]/div[1]/div[2]/div/div/div/div[14]/span'

        driver.find_element_by_xpath(juanzongziliao).click()
        driver.find_element_by_xpath(shenqingbiao).click()
        driver.find_element_by_xpath(upload).send_keys("C:\\Users\\zhujihui\\Pictures\\handwriting.png")
        time.sleep(0.5)
        driver.find_element_by_xpath(dangshiren).click()
        driver.find_element_by_xpath(upload).send_keys("C:\\Users\\zhujihui\\Pictures\\handwriting.png")
        time.sleep(0.5)
        driver.find_element_by_xpath(shoulidan).click()
        driver.find_element_by_xpath(upload).send_keys("C:\\Users\\zhujihui\\Pictures\\handwriting.png")
        time.sleep(0.5)
        driver.find_element_by_xpath(gaozhishu).click()
        driver.find_element_by_xpath(upload).send_keys("C:\\Users\\zhujihui\\Pictures\\handwriting.png")

        driver.implicitly_wait(10)

        time.sleep(1)

        # 上报签批
        sbqp_button = '//*[@id="app"]/div[9]/div[1]/button'
        qianpiren = '//*[@id="app"]/div[5]/div/div/div[2]/div[2]/div/span[2]/div/div[1]/input'
        sbqp_button2 = '//*[@id="app"]/div[5]/div/div/div[3]/button[1]'
        sbqp_button3 = '/html/body/div[6]/div/div[3]/button[2]'
        qianfagao = '//*[@id="app"]/div[5]/div/div/div[2]/div[3]/span[2]/span[3]'
        qianfagao_quit = '//*[@id="app"]/div[6]/div[1]/button[3]'
        driver.find_element_by_xpath(sbqp_button).click()
        time.sleep(10)
        driver.find_element_by_xpath(qianfagao).click()
        time.sleep(5)
        driver.find_element_by_xpath(qianfagao_quit).click()
        time.sleep(2)
        driver.find_element_by_xpath(sbqp_button2).click()
        driver.find_element_by_xpath(sbqp_button3).click()
        time.sleep(1)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
