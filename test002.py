import time
import pyautogui

from selenium import webdriver
from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.maximize_window()

# driver.get("https://www.google.com")
driver.get("https://pokeassistant.com/main/ivcalculator")

print(driver.title)

# inputElement = driver.find_element_by_name("q")
pokemon_name = driver.find_element_by_name("search_pokemon_name")

pokemon_name.send_keys("Buneary")

time.sleep(1)
# pokemon_name = driver.find_element_by_name("search_pokemon_name")
#
# pokemon_name.send_keys("503")

search_cp = driver.find_element_by_name("search_cp")

search_cp.send_keys("503")

time.sleep(1)

search_hp = driver.find_element_by_name("search_hp")

xy = pokemon_name.location
print(xy.keys())
print(xy.values())

print(xy['x'])
print(type(xy['x']))
print(xy['y'])
print(type(xy['y']))

x, y = xy['x'], xy['y']
search_hp.send_keys("80")

time.sleep(1)

search_dust = Select(driver.find_element_by_name("search_dust"))

# search_dust = driver.find_element_by_name("search_dust")

search_dust.select_by_value("1600")

time.sleep(1)
# search_dust = driver.find_element_by_name("search_dust")
#
# search_dust.send_keys("1600")
#
# search_dust = driver.find_element_by_name("search_dust")
#
# search_dust.send_keys("1600")
#
# pyautogui.click()
try:
    inputElement = driver.find_element_by_id("calculatebtn")
except Exception as e:
    print(e)
time.sleep(1)
pyautogui.click(x + 75, y + 91)
time.sleep(1)
pyautogui.moveTo(x + 126, y + 172, 0.5)
pyautogui.click(x + 126, y + 172)
time.sleep(1)
inputElement.click()
time.sleep(1)
# inputElement.submit()

# try:
#     WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))
#     print(driver.title)
#
# finally:
#     driver.quit()

# driver.quit()
