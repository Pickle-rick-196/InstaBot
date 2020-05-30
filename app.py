from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys


usern = input('name of user >>')
message_ = input("message >>>")

class bot:
    def __init__(self, username, password, user, message):
        self.username = username
        self.password = password
        self.user = user
        self.message =  message
        self.base_url = 'https://www.instagram.com/'
        self.bot = webdriver.Chrome("E:/chromedriver.exe")
        self.login()


    def login(self):
        self.bot.get(self.base_url)
        
        enter_username = WebDriverWait(self.bot, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'username')))
        enter_username.send_keys(self.username)
        enter_password = WebDriverWait(self.bot, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)
        enter_password.send_keys(Keys.RETURN)
        time.sleep(5)
        self.bot.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        time.sleep(3)
        self.bot.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
        time.sleep(4)
        self.bot.find_element_by_xpath('//a[@class="xWeGp"]/*[name()="svg"][@aria-label="Direct"]').click()
        time.sleep(3)
        self.bot.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/button').click()
        time.sleep(2)
        self.bot.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[1]/div/div[2]/input').send_keys(self.user)
        time.sleep(2)
        self.bot.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/div/div/div[3]/button/span').click()
        time.sleep(2)
        self.bot.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/div/button').click()
        time.sleep(2)
        self.bot.find_element_by_css_selector('textarea[placeholder="Message..."]').send_keys(self.message)
        time.sleep(1)
        self.bot.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()

def init():     
    bot('bot_test0', 'abcdefg123456', usern, message_)
    input("DONE")

init()
