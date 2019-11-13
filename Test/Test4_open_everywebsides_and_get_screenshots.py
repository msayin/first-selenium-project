from selenium import webdriver
import time

driver = webdriver.Chrome()

web = ["https://python.org",
       "https://stackoverflow.com",
       "https:pypy.org"]

for i in range(0,len(web)):
    driver.get(web[i])
    driver.get_screenshot_as_file("shot" + str(i)+ ".png")
    time.sleep(2)
driver.quit()
