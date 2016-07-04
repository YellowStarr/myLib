#!/usr/bin/env python
# -*- coding: utf-8 -*-
#库存挂牌
import pdb
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import os,sys
from normalList import normalList
from ListCheckFactory import ListCheck
import Mytool
from ListTab import ListTab
import HTMLTestRunner


class GPapplication(unittest.TestCase):
        
    def setUp(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.10.153:8080"
        self.verificationErrors = []
        self.accept_next_alert = True
        #self.f=open("f:/workspace/python/data.txt","w")
        self.driver.maximize_window()
        global dict

    def test_garantee(self):
        """保证金信用金挂牌"""
        driver = self.driver
        driver.delete_all_cookies()
        driver.get(self.base_url + 
            "/gzql/goods/add_goods_pay.shtml?menu_no=652121")
        li=normalList(driver)
        li.login("qiuwjcom1",888888)   
        time.sleep(3)     
        li.choose_Ganrantee(1)
        li.fund_pick(0,1)
        time.sleep(2)
        li.Goods_attr()
        li.intro('C:\\Users\\Administrator.2013-20150712UD\\Desktop\\eng.txt')
        time.sleep(3)   
        js="document.documentElement.scrollTop=400"
        driver.execute_script(js)
        url=u"E:\\图片\\20150405H4118_AFk2Z.jpeg"
        li.upload_Pic(url)
        js="document.documentElement.scrollTop=1000"
        driver.execute_script(js)
    #交易信息

        li.trade_info(2,10,1,30)
        print "totalprice:%d"%li.getTotalprice()
        js="document.documentElement.scrollTop=1400"
        driver.execute_script(js)
    #交收信息
        li.set_Addr()
        js="document.documentElement.scrollTop=1600"
        driver.execute_script(js)
        li.getContract(1,20,10)
        li.payDeposite()
    #截屏
        js="document.documentElement.scrollTop=1900"
        driver.execute_script(js)
        driver.get_screenshot_as_file("f:\\workspace\\python\\1.png")
        time.sleep(5)
    #合同约定
        li.submit()
        time.sleep(5)
        li.getListNo()
        dict=li.returnDic()

    def test_wareHouse(self):
        u"""仓单库存挂牌"""
        driver = self.driver
        driver.delete_all_cookies()
        driver.get(self.base_url + 
            "/gzql/goods/add_goods_pay.shtml?menu_no=652121")
        li=normalList(driver)
        li.login("qiuwjcom1",888888)   
        time.sleep(3)     
        li.choose_Ganrantee(4)   
        li.recipt_pick("618")
        time.sleep(2) 
        #li.intro('C:\\Users\\Administrator.2013-20150712UD\\Desktop\\eng.txt','wm_intro')
        #time.sleep(3)   
        js="document.documentElement.scrollTop=400"
        driver.execute_script(js)
        url=u"E:\\图片\\20150405H4118_AFk2Z.jpeg"
        li.upload_Pic(url)
        js="document.documentElement.scrollTop=1000"
        driver.execute_script(js)
    #交易信息
        li.trade_info(2,5,1,30)
        print "totalprice:%d"%li.getTotalprice()
        js="document.documentElement.scrollTop=1600"
        driver.execute_script(js)
    #交收信息
        li.set_Addr(2)
        js="document.documentElement.scrollTop=1600"
        driver.execute_script(js)
        li.getContract(1,20,10)
    #截屏
        js="document.documentElement.scrollTop=1900"
        driver.execute_script(js)
        driver.get_screenshot_as_file("f:\\workspace\\python\\1.png")
        time.sleep(5)
    #合同约定
        li.submit()
        time.sleep(5)
        li.getListNo()
        dict=li.returnDic()
    
    def test_l_check(self):
        u"""挂牌列表测试用例"""
       # Mytool.printDict()
        driver = self.driver
        driver.delete_all_cookies()
        driver.get(self.base_url + 
            "/gzql/goods/goods_mgr.shtml?menu_no=652102#tab1")
        ll=ListTab(driver)
        ll.login("qiuwjcom1",888888)   
        Mytool.getScreen(driver)
        time.sleep(3)
        ll.getOperate("check")
        aa=ListCheck(driver) 
        ad=aa.getSuccInfo()
        for ii in ad:
            print ii
            print ad[ii]

        Mytool.verify(driver,'dddd',ad['bidway'])
        self.verificationErrors.append(str(ad['bidway']))
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
    testunit=unittest.TestSuite()
    #testunit.addTest(GPapplication("test_garantee"))
    testunit.addTest(GPapplication("test_wareHouse"))

    filename="f:\\www\\qiuLib\\repoter.html"
    fp=file(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='testreport',description='caseRun')
    runner.run(testunit)
