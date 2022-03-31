from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get("https://www.facebook.com/campaign/landing.php?campaign_id=14884913640&extra_1=s%7Cc%7C589460569894%7Ce%7Cfacebook%20login%7C&placement=&creative=589460569894&keyword=facebook%20login&partner_id=googlesem&extra_2=campaignid%3D14884913640%26adgroupid%3D128696221912%26matchtype%3De%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D%26target%3D%26targetid%3Dkwd-1409285535%26loc_physical_ms%3D9040220%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=Cj0KCQjw_4-SBhCgARIsAAlegrUhdncPHJT7mJ1kFhhd49nXZtYe1zPT87QGqjRaVYS61lu5cgQHlOYaAmR3EALw_wcB")
time.sleep(1)
driver.find_element_by_name("firstname").send_keys("Leela")
driver.find_element_by_name("websubmit").click()
time.sleep(5)
driver.close()
print("Tested Successfully")
