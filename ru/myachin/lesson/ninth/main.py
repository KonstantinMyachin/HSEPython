# Selenium Library
from selenium.webdriver import Chrome

driver = Chrome(executable_path="C:\\Users\\User\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("http://okeydostavka.ru")
search = driver.find_element_by_id("SimpleSearchForm_SearchTerm")
search.send_keys("Каша")

from selenium.webdriver.common.keys import Keys

search.send_keys(Keys.ENTER)

from time import sleep

table = []
for i in range(2):
    products = driver.find_elements_by_css_selector(".product")
    for product in products:
        name = product.find_element_by_css_selector(".product_name a")
        print(name.text)

        price = product.find_element_by_css_selector(".price")
        pr = price.text.split()[0].replace(",", ".")
        print(pr)
        table.append([name.text, float(pr)])

    driver.find_element_by_class_name("right_arrow").click()
    sleep(3)

import pandas as pd

df = pd.DataFrame(table, columns=['name', 'price'])
print(df)

from pandas_datareader import wb

df = wb.download(indicator="NY.GDP.PCAP.KD", country=['US', 'RU'], start=1999, end=2017)
df.reset_index()
print(df.unstack().T)

import tabula

dfs = tabula.read_pdf("C:\\Users\\User\\Downloads\\report.pdf", page=2, multiple_tables=True, lattice=True)
print(dfs[2])
