import time
import pyautogui
# import re

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


def cook_accept():
    # time.sleep(1)

    gdpr_cookie_accept_button = driver.find_element_by_id("gdpr-cookie-accept")
    gdpr_cookie_accept_button.click()


def do_calculation(name="Buneary", cp="503", hp="80", dust="1600"):
    # input_element = driver.find_element_by_name("q")
    pokemon_name = driver.find_element_by_name("search_pokemon_name")

    pokemon_name.send_keys(name)

    time.sleep(1)
    # pokemon_name = driver.find_element_by_name("search_pokemon_name")
    #
    # pokemon_name.send_keys("503")

    search_cp = driver.find_element_by_name("search_cp")

    search_cp.send_keys(cp)

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
    search_hp.send_keys(hp)

    time.sleep(1)
    search_dust = Select(driver.find_element_by_name("search_dust"))

    # search_dust = driver.find_element_by_name("search_dust")

    search_dust.select_by_value(dust)

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
    input_element = None
    try:
        input_element = driver.find_element_by_id("calculatebtn")
    except Exception as e:
        print(e)
    time.sleep(1)
    pyautogui.click(x + 75, y + 91)
    time.sleep(1)
    pyautogui.moveTo(x + 126, y + 182, 0.5)
    time.sleep(0.5)
    pyautogui.click(x + 126, y + 182)
    time.sleep(1)
    input_element.click()
    time.sleep(1)
# inputElement.submit()

# try:
#     WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))
#     print(driver.title)
#
# finally:
#     driver.quit()

# driver.quit()


cook_accept()
# do_calculation()
do_calculation("Squirtle", "390", "70", "1900")

my_value = driver.find_element_by_id("possibleCombinationsStringmax")

print(my_value.text)
# for elem in my_value:
#     print(elem.text)

max_rate = my_value.text[my_value.text.index(":")+2:]
print(my_value.text[my_value.text.index(":")+2:])
print(type(my_value.text[my_value.text.index(":")+2:]))

# print(int(my_value.text[my_value.text.index(":")+2:]))

new_max_rate = float(max_rate.strip('%'))/100.0
if new_max_rate > 0.89:
    print(new_max_rate)
else:
    pass

