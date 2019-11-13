from selenium import webdriver
import time
import os

# start webdriver and load website from disk
driver = webdriver.Chrome()
url = 'file:///' + os.getcwd() + '/websites/button.html'
driver.get(url)
time.sleep(2)

# click button
python_button = driver.find_element_by_css_selector("#button")
python_button.click()

# close javascript popup
time.sleep(2)
alert = driver.switch_to_alert()
alert.accept()

time.sleep(3)
driver.quit()

