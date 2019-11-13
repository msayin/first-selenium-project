from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://stackoverflow.com')
print(driver.page_source)
time.sleep(2)

driver.get('https://python.org')
print (driver.page_source)
time.sleep(2)
driver.quit()