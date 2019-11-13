from selenium import webdriver
import time
import os

# start webdriver and load website from disk
driver = webdriver.Chrome()
url = 'file:///' + os.getcwd() + '/websites/mutli_line_textfields.html'
driver.get(url)
time.sleep(1)

# enter text
field1 = driver.find_element_by_id("textbox")
field1.send_keys('Selenium example text')# bu normal var olan line eklemek icin
field1.send_keys('\nAnother line\nAnother line..')# bu baska basak line eklemek icin
time.sleep(1)

# close browser
time.sleep(3)
driver.quit()

