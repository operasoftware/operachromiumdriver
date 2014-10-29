#This an example with typical setup
#Some Opera specific functionality was extracted to appium_helper.py
#If you need a custom setup, please a look at https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/caps.md

import time

from appium_helper import OperaAppiumDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedConditions

######## WEB DRIVER INITIALIZATION #############################
desired_caps = {
    'chromedriverExecutable' : '/home/ela/WEBDRIVER/bin/operadriver', #download from https://github.com/operasoftware/operachromiumdriver/releases
    'app' : '/home/ela/WEBDRIVER/test/opera-browser.apk', #download it from http://www.opera.com/mobile/operabrowser/android
}

driver = OperaAppiumDriver('http://localhost:4723/wd/hub', desired_caps)


######## TEST ##################################################
driver.skip_introduction_guide()
driver.open_page_in_native_context("http://www.google.pl")

driver.switch_to.context('CHROMIUM')

driver.get("http://www.google.pl")
text_input = WebDriverWait(driver, 10).until(ExpectedConditions.element_to_be_clickable((By.NAME, "q")))
text_input.send_keys('OperaDriver\n')

driver.switch_to.context('NATIVE_APP')
driver.close_native_dialog() # close the 'Allow location access?' dialog

time.sleep(5) #just to see the dialog is closed
driver.quit()

