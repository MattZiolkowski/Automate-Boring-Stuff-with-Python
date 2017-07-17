#! python3
# GmailLogIn.py - Program logs into gmail account using Selenium in Firefox browser.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time


browser = webdriver.Firefox()

browser.get('http:2048game.com')

time.sleep(2)

board = browser.find_element_by_css_selector('body')
#Find email log in field by its id.

for i in range(100):
    board.send_keys(Keys.ARROW_UP)
    board.send_keys(Keys.ARROW_RIGHT)
    board.send_keys(Keys.ARROW_DOWN)
    board.send_keys(Keys.ARROW_LEFT)
    time.sleep(0.2)