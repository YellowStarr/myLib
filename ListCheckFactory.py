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


class ListCheck:
	def __init__(self,driver):
		self.driver=driver
		#self.path='f:\\WorkSpace\\python\\excel\\new.csv'	

	def getGoodsBasic(self):
		"""商品基本信息 单号no，品种veriety，品名trade_name，规格standard 型号specification 产地origin 说明description 编码code 
		返回一个字典"""
		driver=self.driver
		no=driver.find_element_by_xpath("//*[@class='view_detail']/div[2]/form/fieldset/div[1]/div/div/div").text
		veriety=driver.find_element_by_xpath("//*[@class='view_detail']/div[2]/form/fieldset/div[2]/div/div/div").text
		trade_name=driver.find_element_by_xpath("//*[@class='view_detail']/div[2]/form/fieldset/div[3]/div/div/div").text
		standard=driver.find_element_by_xpath("//*[@class='view_detail']/div[2]/form/fieldset/div[4]/div/div/div").text
		specification=driver.find_element_by_xpath("//*[@class='view_detail']/div[2]/form/fieldset/div[5]/div/div/div").text
		origin=driver.find_element_by_xpath("//*[@class='view_detail']/div[2]/form/fieldset/div[6]/div/div/div").text
		description=driver.find_element_by_xpath("//*[@class='view_detail']/div[2]/form/fieldset/div[7]/div/div/div").text
		code=driver.find_element_by_xpath("//*[@class='view_detail']/div[2]/form/fieldset/div[8]/div/div/div").text

		dict={"no":no,"veriety":veriety,"trade_name":trade_name,"standard":standard,"specification":specification,
					"origin":origin,"description":description,"code":code}
		return dict

	def extraAttr(self):
		"""获取商品附加属性，商品描述"""
		driver=self.driver
		try:
			driver.find_element_by_xpath("//*[@id='view_info']/div/div[2]/form/fieldset/div/div/div/div/div")
			att1=driver.find_element_by_xpath("//*[@id='view_info']/div/div[2]/form/fieldset/div/div/div/div/div").text
			att2=driver.find_element_by_xpath("//*[@id='view_info']/div/div[3]/div/form/fieldset/div/textarea").text
			dict={'att1':att1,'att2':att2}
		except:
			att2=driver.find_element_by_xpath(".//*[@id='view_info']/div/div[3]/div/form/fieldset/div/textarea").text
			dict={'att2':att2}
		return dict

	def getPic(self):
		driver=self.driver
		hasPic=driver.find_element_by_id("attachid")
		if not hasPic.get_attribute("value"):
			src=driver.find_element_by_css_selector("img").get_attribute('src')
		else:
			src=""
		return src

	def getSuccInfo(self):
		print "call getSuccInfo"
		driver=self.driver
		bidway=driver.find_element_by_xpath("//*[@id='view_info']/div/div[7]/div[1]/form/fieldset/div[1]/div/div").text
		listAmount=driver.find_element_by_xpath("//*[@id='view_info']/div/div[7]/div[2]/form/fieldset/div[1]/div/div").text
		turnOver=driver.find_element_by_id("weight_csg").text
		minAmount=driver.find_element_by_xpath("//*[@id='view_info']/div/div[7]/div[1]/form/fieldset/div[2]/div/div").text
		unit=driver.find_element_by_xpath("//*[@id='view_info']/div/div[7]/div[2]/form/fieldset/div[2]/div/div").text
		price=driver.find_element_by_xpath("//*[@id='view_info']/div/div[7]/div[3]/form/fieldset/div[2]/div/div").text
		addr=driver.find_element_by_xpath("//*[@id='view_info']/div/div[8]/form/fieldset/div/div/div").text
		#addr=addr.encode('utf-8')
		addr=addr.replace(' ','')
		dict={"bidway":bidway,"listAmount":listAmount,"turnOver":turnOver,"minAmount":minAmount,"unit":unit,"price":price,"addr":addr}
		return dict

	def getConInfo(self):
		driver=self.driver
		lineOff=driver.find_element_by_xpath("//*[@id='view_info']/div/div[10]/div[1]/form/fieldset/div[1]/div/div").text
		deliver=driver.find_element_by_xpath("//*[@id='view_info']/div/div[10]/div[2]/form/fieldset/div[1]/div/div").text
		garanway=driver.find_element_by_xpath("//*[@id='a1']/div").text
		limit=driver.find_element_by_xpath("//*[@id='view_info']/div/div[10]/div[1]/form/fieldset/div[3]/div/div").text
		payFir=driver.find_element_by_id("att62").text
		paySec=driver.find_element_by_id("att63").text
		garenS=driver.find_element_by_id("is_deposit1").text
		garenB=driver.find_element_by_id("is_deposit1_2").text
		dict={"lineOff":lineOff,"deliver":deliver,"garanway":garanway,"limit":limit,"payFir":payFir,"paySec":paySec,"garenS":garenS,"garenB":garenB}
		return dict
	
	def getDeadline(self):
		"""截止日数据：保证金garan 付款pay 发货ship 验货comm 验票tic"""
		driver=self.driver
		garan=driver.find_element_by_xpath("//*[@id='allup']/div[1]/form/fieldset/div[1]/div/div").text
		pay=driver.find_element_by_xpath("//*[@id='allup']/div[2]/form/fieldset/div[1]/div/div").text
		ship=driver.find_element_by_xpath("//*[@id='allup']/div[1]/form/fieldset/div[2]/div/div").text
		comm=driver.find_element_by_xpath("//*[@id='allup']/div[2]/form/fieldset/div[2]/div/div").text
		tic=driver.find_element_by_xpath("//*[@id='allup']/div[1]/form/fieldset/div[3]/div/div").text
		dict={"garan":garan,"pay":pay,"ship":ship,"limit":limit,"comm":comm,"tic":tic}
		return dict
#submit
	def goBack(self):
		self.driver.find_element_by_id("id").click()
		time.sleep(1)
				
	

