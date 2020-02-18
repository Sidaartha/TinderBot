from selenium import webdriver
from time import sleep
import random
import re

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

		sleep(3)

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

	def report(self):
		expand_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[6]/button')
		expand_btn.click()
		report_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/button')
		report_btn.click()
		option_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/ul/li[2]/button/div[2]')
		option_btn.click()
		report = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button')
		report.click()

	def run(self):
		self.login()
		likes = 0
		dislikes = 0
		reports = 0
		while True:
			sleep(1)
			try:
				try:
					images = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[2]')
					child_elements = images.find_elements_by_tag_name('button')
					images_no = len(child_elements)
				except:
					images_no = 0
				try:
					description = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[6]/div/div[2]/div/span[1]')
					child_elements = description.find_elements_by_tag_name('span')
					description_spans = len(child_elements)

					neg_re_exp = r"\b" + negitive_filter[0] + r"\b "
					for word in negitive_filter[1:]:
						neg_re_exp += r"| \b" + word + r"\b "
					pos_re_exp = r"\b" + positive_filter[0] + r"\b "
					for word in positive_filter[1:]:
						pos_re_exp += r"| \b" + word + r"\b "
					neg_r = re.compile(neg_re_exp, flags=re.I | re.X)
					pos_r = re.compile(pos_re_exp, flags=re.I | re.X)

					spam_words = []
					matched_words = []
					for span in child_elements:
						spam_words.extend(neg_r.findall(span.text))
						matched_words.extend(pos_r.findall(span.text))
					spam_flag = True if spam_words else False
					description_flag = True
					try:
						match_score = len(matched_words)/len(positive_filter)
					except:
						match_score = 0

				except:
					description_flag = False
					spam_flag = False
					match_score = 0
				if not spam_flag:
					try:
						if images_no > 1 and match_score > 0.3:
							self.like()
							print("Liked!\tImgs: {0}; Match: {1}".format(images_no, match_score))
							likes+=1
						elif images_no > 1:
							if description_flag: threshold = 0.8
							else: threshold = 0.6
							if random.uniform(0, 1) < threshold:
								self.like()
								print("Liked!\tImgs: {0}; Desc: {1}; Threshold: {2}".format(images_no, description_flag, threshold))
								likes+=1
							else:
								self.dislike()
								print("Disliked!\tImgs: {0}; Desc: {1}; Threshold: {2}".format(images_no, description_flag, threshold))
								dislikes+=1
						else:
							self.dislike()
							print("Disliked!\tImgs: 0; Desc: False;")
							dislikes+=1
					except:
						try:
							self.close_popup()
						except:
							self.close_match()
				else:
					report()
					print("Reported!\tSpam words: {0}".format(spam_words))
					reports+=1
					dislikes+=1
			except:
				pass
			print("Likes:\t{0}; Dislikes:\t{1}; Reports:\t{2}".format(likes, dislikes, reports))

if __name__ == '__main__':
	bot = TinderBot()
	bot.run()