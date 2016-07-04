#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException 
import time,re,Mytool
import os,sys


class goodsPub:
	def __init__(self,driver):
		self.driver=driver
		#self.path='f:\\WorkSpace\\python\\excel\\new.csv'
		
	def login(self,name,password):
		driver=self.driver
		Mytool.findName(driver,"username").send_keys(name)
		Mytool.findName(driver,"password").send_keys(password)
		time.sleep(3)
		Mytool.findId(driver,"login_bt").click()

	def goLink(self,text):
		driver=self.driver
		print text
		Mytool.findLink(driver,text).click()

	def gdPub(self):
		driver=self.driver
		Mytool.findXpath(driver,"//*[@id='1001']/a").click()
		Mytool.findId(driver,'qsNo','123456789111')
		Mytool.findId(driver,'pdtStdNo','123456')
		Mytool.findId(driver,'factoryName',u'天津食品厂')
		Mytool.findId(driver,'factoryAddr',u'天津塘沽区')
		Mytool.scroll(driver,1600)
		Mytool.findId(driver,'factoryLink',u'4000001234')
		Mytool.findId(driver,'burden',u'what ever i dont know')
		Mytool.findId(driver,'storeMeans',u'真空冷藏')
		Mytool.findId(driver,'storeLife',1)
		Mytool.findId(driver,'foodAdditive',u'二氧化硅，甘油酯')
		Mytool.selectList(driver,'storeLife','//option[@value="2"]')
		Mytool.selectList(driver,'hasSugar','//option[@value="2"]')
		Mytool.chooseDate(driver,'producingDate','2016-01-01')
		Mytool.chooseDate(driver,'purchaseDate','2016-05-28')
		Mytool.findId(driver,'supplier',u'阿富汗')
		Mytool.findId(driver,'goodsName',u'title')
		Mytool.findId(driver,'sellPoint',u'物美价廉')
		Mytool.scroll(driver,2200)
		Mytool.findId(driver,'goodsNo',2567)
		Mytool.findId(driver,'orderPrice',25)
		Mytool.findId(driver,'netWeight',25)
		Mytool.selectList(driver,'netWeightUnitId','//option[@value="2"]')
		Mytool.findId(driver,'providedQtt',10)
		Mytool.selectList(driver,'packingId','//option[@value="1"]')
		Mytool.selectList(driver,'breedId','//option[@value="1"]')
		Mytool.selectList(driver,'pdtProvId','//option[@value="157"]')
		Mytool.selectList(driver,'pdtCityId','//option[@value="96"]')
		Mytool.findId(driver,'SWFUpload_0').click()
		time.sleep(5)
		Mytool.scroll(driver,2500)

		body="eWebEditor1.setHTML('<b>Hello My World!</b>')"
		driver.execute_script(body)
		
		Mytool.scroll(driver,3100)
		Mytool.findId(driver,'freePostage').click()
		Mytool.findId(driver,'upTimeSetTime').click()
		time.sleep(1)
		Mytool.chooseDate(driver,'planUpTimeDay','2016-07-01')
		#Mytool.selectList(driver,'planUpTimeHour','//option[@value="16"]')
		driver.find_element_by_id('planUpTimeHour').send_keys('16')
		time.sleep(3)
		driver.find_element_by_id('planUpTimeMinute').send_keys('10')
		#Mytool.selectList(driver,'planUpTimeMinute','//option[@value="10"]')
		time.sleep(10)
		Mytool.findId(driver,'btnSubmit').click()