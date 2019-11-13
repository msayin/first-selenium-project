from selenium import webdriver
import time

driver = webdriver.Chrome()

web = ["https://python.org",
       "https://stackoverflow.com",
       "https:pypy.org"]

for w in web:
    driver.get(w)
    print(driver.title)
time.sleep(2)
driver.quit()
