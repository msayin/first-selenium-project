from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:/Users/fmsay/PycharmProjects"
                          "/FirstSeleniumTest/drivers/chromedriver.exe")

driver.set_page_load_timeout("10")
driver.get("https://google.com")
driver.find_element_by_name("q").send_keys("Automation Step by Step")
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
driver.maximize_window()
driver.refresh()
time.sleep(5)
driver.quit()
print ("Test completed succesfully")


# Not:Kaynak
# driver = webdriver.Chrome("C:/Users/fmsay/PycharmProjects/FirstSeleniumTest/drivers/chromedriver.exe")
# yukaridaki sekilde veya asagidaki sekilde yazilabilir ancak slash işaretlerini
# ya (\\) ikili back yazmak gerekiyor yada birli(/) slash yazmak gerekiyor.
# driver = webdriver.Chrome ("C:\\Users\\fmsay\\PycharmProjects\\FirstSeleniumTest\\drivers\\chromedriver.exe")

# test automation selenium python
# https://www.youtube.com/watch?v=FFDDN1C1MEQ&t=1260s