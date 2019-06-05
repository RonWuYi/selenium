import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

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
try:
    inputElement = driver.find_element_by_id("calculatebtn")
except Exception as e:
    print(e)

inputElement.click()
# inputElement.submit()

# try:
#     WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))
#     print(driver.title)
#
# finally:
#     driver.quit()
