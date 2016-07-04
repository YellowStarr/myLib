# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from goodsPub import goodsPub

class GoodsPublish(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.base_url = "http://192.168.10.153:8080"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.maximize_window()
    
    def test_goods_publish(self):
        driver = self.driver
        driver.delete_all_cookies()
        driver.get(self.base_url + "/ctcshop/index.shtml")
        gp=goodsPub(driver)
        gp.goLink(u'请登录')

        gp.login("qiuwjcom1",888888)
        gp.goLink(u'卖家中心')
        driver.get(self.base_url + "/ctcshop/sell/goods/goodsPublish.shtml")
        gp.gdPub()
        #js="document.documentElement.scrollTop=1600"
       # driver.execute_script(js)
        time.sleep(5)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
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
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
