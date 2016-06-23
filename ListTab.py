#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time,re,Mytool

class ListTab:
	def __init__(self,driver):
		self.driver=driver
		#self.path='f:\\WorkSpace\\python\\excel\\new.csv'
	def login(self,name,password):
		self.driver.find_element_by_id("username").clear()
		self.driver.find_element_by_id("username").send_keys(name)
		self.driver.find_element_by_id("password").clear()
		self.driver.find_element_by_id("password").send_keys(password)
		time.sleep(3)
		self.driver.find_element_by_id("login_btn").click()
	def getListNo(self):
		"""获取第一行挂牌单号"""
		driver=self.driver
		firTar=driver.find_element_by_xpath("//*[@id='tbContent']/tr[1]/td[2]/ul/li[1]")
		title=firTar.get_attribute("title")
		no=title.split(u"：")[1]
		return no

	def getListAmount(self):
		"""获取第一行挂牌量"""
		driver=self.driver
		listAmount=driver.find_element_by_xpath("//*[@id='tbContent']/tr[1]/td[3]").text
		return listAmount

	def getPrice(self):
		"""获取第一行挂牌单价"""
		driver=self.driver
		price=driver.find_element_by_xpath("//*[@id='tbContent']/tr[1]/td[4]").text
		return price

	def getBidWay(self):
		"""获取第一行出价方式"""
		driver=self.driver
		bidway=driver.find_element_by_xpath("//*[@id='tbContent']/tr[1]/td[5]").text
		return bidway

	def getTurnOver(self):
		"""获取第一行成交量"""
		driver=self.driver
		turnover=driver.find_element_by_xpath("//*[@id='tbContent']/tr[1]/td[6]").text
		return turnover

	def getLimit(self):
		"""获取第一行挂牌有效期"""
		driver=self.driver
		limit=driver.find_element_by_xpath("//*[@id='tbContent']/tr[1]/td[7]").text
		return limit

	def getListDate(self):
		"""获取第一行发布日期"""
		driver=self.driver
		date=driver.find_element_by_xpath("//*[@id='tbContent']/tr[1]/td[8]").text
		return date

	def getStatue(self):
		"""获取第一行挂牌单状态"""
		driver=self.driver
		statue=driver.find_element_by_xpath("//*[@id='tbContent']/tr[1]/td[9]").text
		return statue

	def getOperate(self,op):
		driver=self.driver
		op=op.lower()
		if op=="copy":
			driver.find_element_by_xpath("//*[@id='tbContent']/tr[1]/td[10]/a[1]").click()
		elif op=="check":
			driver.find_element_by_xpath("//*[@id='tbContent']/tr[1]/td[10]/a[2]").click()
		time.sleep(2)