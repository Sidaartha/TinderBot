from selenium import webdriver
from time import sleep
import random

from config_local import *

class TinderBot():
	def __init__(self):
		self.driver = webdriver.Chrome()

	def login(self):
		self.driver.get('https://tinder.com')

		sleep(3)

		fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
		fb_btn.click()

		base_window = self.driver.window_handles[0]
		self.driver.switch_to_window(self.driver.window_handles[1])


		email_input = self.driver.find_element_by_xpath('//*[@id="email"]')
		password_input = self.driver.find_element_by_xpath('//*[@id="pass"]')
		email_input.send_keys(fb_email)
		password_input.send_keys(fb_password)

		login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
		login_btn.click()

		self.driver.switch_to_window(self.driver.window_handles[0])

		sleep(2)

		popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
		popup_1.click()
		popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
		popup_2.click()
	
	def like(self):
		like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
		like_btn.click()

	def dislike(self):
		dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
		dislike_btn.click()

	def close_popup(self):
		popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
		popup_3.click()

	def close_match(self):
		match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
		match_popup.click()

	def run(self):
		self.login()
		while True:
			sleep(1)
			try:
				if random.uniform(0, 1) < 0.7:
					self.like()
				else:
					self.dislike()
			except:
				try:
					self.close_popup()
				except:
					self.close_match()

if __name__ == '__main__':
	bot = TinderBot()
	bot.run()