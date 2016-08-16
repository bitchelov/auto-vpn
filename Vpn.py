from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
import json


while True:
	caps = DesiredCapabilities.INTERNETEXPLORER
	caps['ignoreProtectedModeSettings'] = True
	driver = webdriver.Ie(os.getcwd() + "\\IEDriverServer.exe", capabilities=caps)
	driver.implicitly_wait(10) # seconds
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
	# new version
	errors = 0
	while errors < 3:
		while (os.system("ping -n 1 " + data["hostname"]) == 0):
		    # print (data["hostname"] + 'is up!')
		    time.sleep(10)
		    errors = 0
		else:
		    # print (data["hostname"] + 'is down!')
		    #unexpected action with second window(popup)
		    # driver.switch_to_window(driver.window_handles[0])
		    # driver.close()
		    errors = errors + 1
	else:
	    driver.quit()

	# driver.find_element_by_id("overridelink").click()

	#pyinstaller --onefile Vpn.py
