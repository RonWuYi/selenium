import logging

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from func.mylog import config_basic

# # log_config()
# browser = webdriver.Firefox()
# browser.get('https://www.google.com/')
#
# assert 'Google' in browser.title
#
# elem = browser.find_element_by_name('btnK')
# # elem.send_keys('seleniumhq', Keys.)
# logging.debug('nomal debug message')
# browser.quit()


class Mini:
    def __init__(self):
        config_basic()

    # @staticmethod
    def for_log(self):
        logging.debug("this is debug log")
        logging.critical("add critical")
        print("create debug log")


if __name__ == '__main__':
    app = Mini()
    app.for_log()




