from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()

driver.get("https://www.google.com/")
time.sleep(1)
driver.find_element_by_name("q").send_keys("Harman")
#search
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(5)
driver.close()
print("Tested successsfully")
