from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser  =webdriver.Firefox()
browser.get('https://www.google.com/')

assert 'Google' in browser.title

elem = browser.find_element_by_name('btnK')
# elem.send_keys('seleniumhq', Keys.)

browser.quit()