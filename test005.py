# import os
#
# # sys.path.insert(1, os.path.join(os.getcwd(), 'geckodriver\\geckodriver.exe'))
#
# my_url = os.path.join(os.getcwd(), 'geckodriver\\geckodriver.exe')
#
# print(my_url)

my_urls = (f"https://www.in-cosmetics.com/en/exhibitor-directory/#search=startRecord%3D{pagenumber}%26rpp%3D64" for pagenumber in range(1, 531, 64))

for i in my_urls:
    print(i)