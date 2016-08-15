from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
import json

caps = DesiredCapabilities.INTERNETEXPLORER
caps['ignoreProtectedModeSettings'] = True
driver = webdriver.Ie(os.getcwd() + "\\IEDriverServer.exe", capabilities=caps)
#driver.implicitly_wait(10) # seconds
wait = WebDriverWait(driver, 10)


data = json.loads(open('data.json').read())
driver.get(data["url"])
wait.until(EC.title_contains("Check Point"))
userName = driver.find_element_by_id("userName")
userName.clear()
userName.send_keys(data["login_data"]["login"])
password = driver.find_element_by_id("passwordDisplayed")
password.clear()
password.send_keys(data["login_data"]["password"])
# Login
driver.find_element_by_id("LoginButton").click()
time.sleep(3)
driver.switch_to_window(driver.window_handles[1])
time.sleep(2)
connectionStatus = driver.find_element_by_id("displayStatus")
# doesnt work

# wait.until(EC.text_to_be_present_in_element(By.ID, 'displayStatus'), 'Подключено')
# wait.until(EC.text_to_be_present_in_element_value(connectionStatus, "Подключено")
# driver.close()

# new version
while(connectionStatus.text != " Подключено"):
    time.sleep(1)
print(connectionStatus.text)
driver.close()



# while (os.system("ping -n 6 " + data["hostname"]) == 0):
#     print (hostname + 'is up!')
# else:
#     print (hostname + 'is down!')
#     driver.close()
#     driver.close()
#

#
#driver.find_element_by_id("overridelink").click()


#pyinstaller --onefile Vpn.py
