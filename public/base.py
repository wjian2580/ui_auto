import time
import allure
import pytest
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from public.pages import login
from appium.webdriver.common.touch_action import TouchAction


def attch_screenshot():
	pass

def find_element():
	pass
	

class Action():

	# _instance = None

	# def __new__(cls):
	#     if not cls._instance:
	#         desired_caps = {
	#             "platformName": "Android",
	#             "platformVersion": "9",
	#             "deviceName": "vivo x27",
	#             "appPackage": "cn.xdf.woxue.student",
	#             "appActivity": ".activity.SplashActivity",
	#             "newCommandTimeout": 3000
	#         }
	#     pass

	def __init__(self):
		desired_caps = {
			"platformName": "Android",
			"platformVersion": "6.0.1",
			"deviceName": "MuMu",
			"appPackage": "cn.xdf.woxue.student",
			"appActivity": ".activity.SplashActivity",
			"newCommandTimeout": 3000,
			"autoGrantPermissions": True
		}
		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
		self.driver.implicitly_wait(30)

	def login(self):
		login_page = login.Login()
		self.click(*login_page.privacy_sure)
		self.click(*login_page.login_by_passwd_tab_loc)
		self.send_keys('13520637568', *login_page.phone_number_loc)
		self.send_keys('autotest', *login_page.password_loc)
		self.click(*login_page.login_btn_loc)
		self.click_by_text('跳过')
		self.click_by_text('知道了')


	def find_element(self, *loc):
		WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc))
		element = self.driver.find_element(*loc)
		return element

	def get_text(self, *loc):
		element = self.find_element(*loc)
		text = element.get_attribute('text')
		return text

	def click_by_partial_text(self, text):
		WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(f"//*[contains(@text, '{text}')]"))
		element = self.driver.find_element_by_xpath(f"//*[contains(@text, '{text}')]")
		element.click()


	def click_by_text(self, text):
		WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(f'//*[@text="{text}"]'))
		element = self.driver.find_element_by_xpath(f'//*[@text="{text}"]')
		element.click()

	def click_by_id(self, id):
		WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_id(id))
		element = self.driver.find_element_by_id(id)
		element.click()

	def click_by_accessibility_id(self, accessibility_id):
		WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_accessibility_id(accessibility_id))
		element = self.driver.find_element_by_accessibility_id(accessibility_id)
		element.click()

	def find_by_text(self, text):
		WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(f"//*[contains(@text, '{text}')]"))
		element = self.driver.find_element_by_xpath(f"//*[contains(@text, '{text}')]")
		return element

	def click(self, *loc):
		element = self.find_element(*loc)
		element.click()

	def send_keys(self, text, *loc):		
		element = self.find_element(*loc)
		element.clear()
		element.send_keys(text)

	def long_press(self, *loc):
		element = self.find_element(*loc)
		TouchAction(self.driver).long_press(element).perform()
		self.sleep()

	def sleep(self, sec=2):
		time.sleep(sec)

	def back(self, times=1):
		for i in range(times):
			time.sleep(0.5)
			self.driver.back()

	def swipe_Down(self, n=1):
		window_size = self.driver.get_window_size()
		width = window_size.get("width")
		height = window_size.get("height")
		# pytest.set_trace()
		for i in range(n):
			self.driver.swipe(width/2,height/4,width/2,height*3/4,500)

	def swipe_Up(self, n=1):
		window_size = self.driver.get_window_size()
		width = window_size.get("width")
		height = window_size.get("height")
		for i in range(n):
			self.driver.swipe(width/2,height*3/4,width/2,height/4,500)

	def swipe_Left(self, n=1):
		window_size = self.driver.get_window_size()
		width = window_size.get("width")
		height = window_size.get("height")
		for i in range(n):
			self.driver.swipe(width/4,height/2,width*3/4,height/2,500)

	def swipe_Rigth(self, n=1):
		window_size = self.driver.get_window_size()
		width = window_size.get("width")
		height = window_size.get("height")
		for i in range(n):
			self.driver.swipe(width*4/5,height/2,width/5,height/2,500)

	def attach_screenshot(self, name):
		self.sleep()
		allure.attach(self.driver.get_screenshot_as_png(), f'{name}.png', allure.attachment_type.PNG)
	

	def element_existed(self, *loc):
		try:
			self.find_element(*loc)
		except TimeoutException:
			return False
		return True

	def text_existed(self, text):
		try:
			self.find_by_text(text)
		except TimeoutException:
			return False
		return True
		
		

