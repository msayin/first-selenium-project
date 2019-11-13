from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get ('https://python.org')
print (driver.title)
time.sleep(2)
driver.quit()
