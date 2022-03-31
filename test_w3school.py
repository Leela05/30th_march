from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get("https://www.w3schools.com/")
time.sleep(1)
#tutorial
driver.find_element_by_id("navbtn_tutorials").click()
time.sleep(2)
#datascience
driver.find_element_by_link_text("Learn Data Science").click()
time.sleep(5)
driver.close()
print("Tested successfully")
