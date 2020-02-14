from selenium import webdriver
from time import sleep

from config_local import *

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')

bot = TinderBot()
bot.login()