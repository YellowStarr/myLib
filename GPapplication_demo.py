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
import Mytool
from ListTab import ListTab
import HTMLTestRunner


class GPapplication(unittest.TestCase):
        
    def setUp(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.11.134:14703"
        self.verificationErrors = []
        self.accept_next_alert = True
        #self.f=open("f:/workspace/python/data.txt","w")
        self.driver.maximize_window()
        global dict

    def test_g_papplication(self):
        u"""商品挂牌测试用例"""
        driver = self.driver
        driver.delete_all_cookies()
        driver.get(self.base_url + 
            "/gzql/goods/add_goods_pay.shtml?menu_no=652121")
        li=normalList(driver)
        li.login("deadline1",888888)   
        time.sleep(3)     
        li.choose_Ganrantee(3)
        
        li.recipt_pick("47")
        #li.fund_pick(0,1)
        time.sleep(2)
        #li.Goods_attr()
      #  time.sleep(3)    
        driver.get_screenshot_as_file("f:\\workspace\\python\\normaltest\\1.png")
        js="document.documentElement.scrollTop=400"
        driver.execute_script(js)
        url=u"E:\\图片\\20150405H4118_AFk2Z.jpeg"
        #li.upload_Pic(url)
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
       # money=li.getContract()
       # li.payDeposite()

       #print li.getFreezeM()
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
        ll.login("deadline1",888888)   
        time.sleep(3)
        no=ll.getListNo()
        

        amount=ll.getListAmount()
        #amount=amount.decode("gb2312")
        price=ll.getPrice()
        priceL=re.split(r'(\d*)',price)
        priceNum=priceL[1]
        priceUnit=priceL[2]
        date=ll.getListDate()
        print no
        print amount
        print priceNum
        if priceUnit==u'元/斤':
            print "equals"
        else:
            print "wrong"
        print date
        '''try: self.assertEqual(Mytool.getDict("listNo"),no)
        except AssertionError as e: self.verificationErrors.append(str(e))
        
        try: self.assertEqual(Mytool.getDict("listAmount"),amount)
        except AssertionError as e: self.verificationErrors.append(str(e))'''
        



       
    
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
   # testunit.addTest(GPapplication("test_g_papplication"))
    testunit.addTest(GPapplication("test_l_check"))

    filename="f:\\WorkSpace\\python\\20160621\\repoter.html"
    fp=file(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='testreport',description='caseRun')
    runner.run(testunit)
