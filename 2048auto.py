#! python3
# 2048auto.py - Program automatically plays the 2048 game for you by opening the site and hitting 100 times up, right, down and left.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time


browser = webdriver.Firefox()

browser.get('http:2048game.com')  # Game's website.

time.sleep(2)  # Allows browser to open a game.

board = browser.find_element_by_css_selector('body')
#Find email log in field by its id.

for i in range(100):
    board.send_keys(Keys.ARROW_UP)
    board.send_keys(Keys.ARROW_RIGHT)
    board.send_keys(Keys.ARROW_DOWN)
    board.send_keys(Keys.ARROW_LEFT)
    time.sleep(0.2)
