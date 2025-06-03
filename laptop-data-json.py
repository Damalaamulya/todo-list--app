import csv
import json
import time

import e
import newline
from fsspec.implementations import data
from selenium import webdriver, webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://webscraper.io/test-sites/e-commerce/static/computers/laptops')
time.sleep(3)


#accept cookies  if visible
try:
    cookie_button = driver.find_element(By.XPATH,"//a[text()='accept Cookies']")
    cookie_button.click()
    time.sleep(3)
except NoSuchElementException:

    print("no cookies banner found")

products = driver.find_elements(By.CLASS_NAME,"thumbnail")
laptop_data=[]
for product in products:
    try:
         title_element = product.find_element(By.CLASS_NAME,"product-title").text
         title = title_element.text
         price = product.find_element(By.CLASS_NAME,"product-price").text
         description = product.find_element(By.CLASS_NAME,"product_description").text
         detail_url =title_element.get_attribute("href")
         laptop_data.append({"title":title,
                    "price":price,
                    "description":description,
                    "detail_url":detail_url})
    except NoSuchElementException as e:
         print(f"Error Parsing a product: {e}")
#save to json

with open("laptop-data.json", "w",encoding = "utf-8") as f:
     json.dump(laptop_data,f,ensure_ascii=False, indent=4)
     print("data saved to laptop-data.json")

#close the brows
driver.quit()



