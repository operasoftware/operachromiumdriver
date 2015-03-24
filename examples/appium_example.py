import os
import time

from appium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedConditions

######## WEB DRIVER INITIALIZATION #############################
desired_caps = {}
desired_caps['automationName'] = 'selendroid'
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = ''

desired_caps['chromedriverExecutable'] = 'path/to/operadriver' #download from https://github.com/operasoftware/operachromiumdriver/releases
desired_caps['app'] = os.path.abspath('path/to/opera-browser.apk') #download it from http://www.opera.com/mobile/operabrowser/android
desired_caps['appPackage'] = 'com.opera.browser'
desired_caps['androidDeviceSocket'] = desired_caps['appPackage'] + '.devtools'


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


######## UTILITIES                 #############################
def swipe_left(duration=1):
    WebDriverWait(driver, 10).until(
        ExpectedConditions.presence_of_element_located((By.ID, get_element_id("drag_area"))))
    pager = find_element_by_id('drag_area');
    flick = TouchActions(driver).flick_element(pager, -1000, 0, 70);
    flick.perform();

def get_element_id(el_id):
    if desired_caps['automationName'].lower() == 'android':
        el_id = "com.opera.android.browser:id/" + el_id
    return el_id

def find_element_by_id(el_id):
    el_id = get_element_id(el_id)
    return driver.find_element_by_id(el_id)



######## TEST                      #############################
def skip_introduction_guide():
    WebDriverWait(driver, 10).until(
        ExpectedConditions.visibility_of_element_located((By.ID, "continue_button"))).click()
    swipe_left()
    swipe_left()
    swipe_left()
    WebDriverWait(driver, 20).until(ExpectedConditions.element_to_be_clickable((By.ID, "guide_finish_button"))).click()

def open_page_in_native_context(url):
    url_field = WebDriverWait(driver, 20).until(ExpectedConditions.element_to_be_clickable((By.ID, get_element_id("url_field"))))
    url_field.clear()
    url_field.send_keys(url + "\n")

def close_native_dialog():
    WebDriverWait(driver, 10).until(ExpectedConditions.element_to_be_clickable((By.ID, get_element_id("opera_dialog_button_negative")))).click()


skip_introduction_guide()
open_page_in_native_context("https://www.google.com/")

print "*** VIEW HANDLES: ***"
for h in driver.contexts:
    print h

if not 'CHROMIUM' in driver.contexts:
    print '\'CHROMIUM\' not in driver.contexts!'
    driver.quit()
    exit(1)

driver.switch_to.context('CHROMIUM')

driver.get("https://www.google.com/")
text_input = WebDriverWait(driver, 10).until(ExpectedConditions.element_to_be_clickable((By.NAME, "q")))
text_input.send_keys('OperaDriver\n')

driver.switch_to.context('NATIVE_APP')
close_native_dialog()

time.sleep(5) #just to see the dialog is closed
driver.quit()
