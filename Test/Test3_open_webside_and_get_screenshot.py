from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get ('https://google.com')

driver.get_screenshot_as_file("shot.png")

time.sleep(3)
driver.quit()
