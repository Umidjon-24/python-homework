from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json

url = "https://www.demoblaze.com/"
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

data = list()
# Click on the "Laptops" category
try:
    laptops = driver.find_element(By.LINK_TEXT, "Laptops")
    laptops.click()
    time.sleep(3)

    contents = driver.find_elements(By.CLASS_NAME, "card-block")
    while True:
        for content in contents:
            name = content.find_element(By.CLASS_NAME, "card-title").text
            price = content.find_element(By.TAG_NAME, "h5").text
            description = content.find_element(By.CLASS_NAME, "card-text").text
            data.append({"name": name, "price": price, "description": description})
        next_button = driver.find_element(By.ID, "next2")
        next_button.click()
        time.sleep(3)
except Exception as e:
    print("Error extracting laptop details:", e)
finally:
    driver.quit()

print(data)