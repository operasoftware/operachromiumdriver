#Appium

Using [Appium](http://appium.io/) makes the test app able to swicth between the native wne web contexts. The native contexts is the context of user interface. In this conext test app is able to dismiss some native Opera dialogs (for example the 'pass word dialog'). The web context is for web pages testing.
For now to start tests for Opera with Appium several capabilities are needed. This will change soon and you be able to use only 'opera' browserName like for other supported browsers.

Typical setup:

```python
desired_caps = {}
desired_caps['browserName'] = 'opera'
desired_caps['automationName'] = 'Android'  #or 'selendroid'

desired_caps['chromedriverExecutable'] = '/path_to_operadriver'
desired_caps['appPackage'] = 'com.opera.browser.beta'
desired_caps['androidDeviceSocket'] = 'opera_beta_devtools_remote'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
```



###Complete example with context switching:

```python
import os
import time
from appium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedConditions


######## WEB DRIVER INITIALIZATION #############################
desired_caps = {}
desired_caps['browserName'] = 'opera'

desired_caps['automationName'] = 'Android'  #or 'selendroid'

desired_caps['chromedriverExecutable'] = '/home/ela/SRC1/work/chromium/src/out_chromedriver/Release/operadriver'
desired_caps['app'] = '/home/ela/Bugs/OPPIUM-13/75916-release-beta.apk'
desired_caps['appPackage'] = 'com.opera.browser.beta'
desired_caps['androidDeviceSocket'] = 'opera_beta_devtools_remote'

desired_caps['specialChromedriverSessionArgs'] = {
  'androidDeviceSocket': 'opera_beta_devtools_remote',
}


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(3)


######## UTILITIES                 #############################
def swipe_left(duration=1):
    #pager = driver.find_element_by_tag_name("LinearLayout");
    pager = find_element_by_id('drag_area');
    flick = TouchActions(driver).flick_element(pager, -1000, 0, 70);
    flick.perform();

def find_element_by_id(el_id):
    if desired_caps['automationName'] == 'android' or desired_caps['automationName'] == 'Android':
        el_id = "com.opera.android.browser:id/" + el_id
    return driver.find_element_by_id(el_id)



######## TEST                      #############################
def skip_introduction_guide():
    driver.find_element_by_id("continue_button").click()
    time.sleep(1)
    swipe_left()
    time.sleep(1)
    swipe_left()
    time.sleep(1)
    swipe_left()
    time.sleep(1)
    guide_finish_button = WebDriverWait(driver, 20).until(ExpectedConditions.element_to_be_clickable((By.ID, "guide_finish_button")))
    guide_finish_button.click()
    time.sleep(1)
    driver.find_element_by_id("ok_button").click()
    time.sleep(1)

def open_page_in_native_context(url):
    url_field = find_element_by_id("url_field")
    url_field.click()
    url_field.send_keys(url + "\n")

def login_to_amazon():
    WebDriverWait(driver, 20).until(ExpectedConditions.element_to_be_clickable((By.XPATH, "//p[@id='who-are-you']/a[1]"))); #probably the page is still loading
    driver.find_element_by_xpath("//p[@id='who-are-you']/a[1]").click();
    driver.find_element_by_name("email").send_keys("operatester@opera.com");
    driver.find_element_by_name("password").send_keys("operasoft");
    driver.find_element_by_name("signIn").submit();

def close_password_dialog():
    negative_button = find_element_by_id("opera_dialog_button_negative")
    if negative_button:
        negative_button.click()


skip_introduction_guide()
open_page_in_native_context("http://amazon.com")
time.sleep(1)

print "*** VIEW HANDLES: ***"
for h in driver.contexts:
    print h

if not 'CHROMIUM' in driver.contexts:
  print '\'CHROMIUM\' not in driver.contexts!'
  driver.quit()
  exit(1)

driver.switch_to.context('CHROMIUM')

login_to_amazon()
time.sleep(5)
driver.switch_to.context('NATIVE_APP')
close_password_dialog()
time.sleep(5)
driver.quit()
```





###Run with selendroid instead of uiautomator:
The same setup but with:

```python
desired_caps['automationName'] = 'selendroid'
```
