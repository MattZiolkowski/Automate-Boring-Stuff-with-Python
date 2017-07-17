#! python3
# GmailLogIn.py - Program logs into gmail account using Selenium in Firefox browser.

from selenium import webdriver
x

import time

#Opens the browser.

browser = webdriver.Firefox()

#Opens log in website.

browser.get('http://gmail.com')

#Find email log in field by its id.

email = browser.find_element_by_id("identifierId")
email.send_keys("your email address here")  # Fills email field
# email.send_keys(u'\ue007') # Press ENTER
email.send_keys(Keys.ENTER) # Other option to hit ENTER


time.sleep(2) # Waits 2 sec for browser to load the password field

#Find password field by css_selector.

password = browser.find_element_by_css_selector("#password > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
password.send_keys("your password here") # Fills password field
password.send_keys(u'\ue007') # Press ENTER
#email.send_keys(Keys.ENTER) # Other option to hit ENTER

time.sleep(120) #Waits 2 min

browser.close()