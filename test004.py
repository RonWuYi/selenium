import os
import sys
import time
from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# sys.path.insert(1, os.path.join(os.getcwd(), '\\geckodriver\\geckodriver.exe'))

# my_url = ('https://www.in-cosmetics.com/en/exhibitor-directory/#search=startRecord%3D{pagenumber}%26rpp%3D64'.format(pagenumber) for pagenumber in range(531, step=64))

my_urls = (f"https://www.in-cosmetics.com/en/exhibitor-directory/#search=startRecord%3D{pagenumber}%26rpp%3D64" for pagenumber in range(1, 531, 64))

product_urls = (f"https://www.in-cosmetics.com/en/in-cosmetics-Global-2020/product-directory/#search=rpp%3D{page}%26startRecord%3D65" for page in range(1, 1271, 64))


# driver = webdriver.Firefox()
driver = webdriver.Firefox(executable_path="C:\\Work\\project\\github\\selenium\\geckodriver\\geckodriver.exe")

for pagei in product_urls:
    # driver.get("https://www.in-cosmetics.com/en/exhibitor-directory/#")
    driver.get(pagei)
    time.sleep(5)
    inputElement_seconde = driver.find_element_by_id("searchResultsList")
    # print(inputElement_seconde.text)
    # print(type(inputElement_seconde.text))

    # print(inputElement_seconde.text.decode('utf-8'))
    my_str = str(inputElement_seconde.text)
    if os.path.isfile(os.path.join(os.getcwd(), 'list.txt')):
        with open('listproduct.txt', 'a', encoding='utf-8') as f:
            f.write(my_str)
    else:
        with open('listproduct.txt', 'w', encoding='utf-8') as f:
            f.write(my_str)

f.close()
driver.quit()

# print(driver.title)

# # inputElement = driver.find_element_by_name("q")
# while True:
#     inputElement = driver.find_element_by_xpath("/html/body/form/div[5]/div[1]/div[3]/div[3]/div[2]/div[2]/ul/li[1]/div")
#     print(inputElement.text)
# others = driver.find_element_by_class_name("name")
# print(others)
# print(others.text)
# inputElement.send_keys("cheese!")

# inputElement.submit()

# try:
#     WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))
#     print(driver.title)

# finally:
#     driver.quit()
