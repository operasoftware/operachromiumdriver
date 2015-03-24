from appium.webdriver.webdriver import WebDriver as AppiumDriver
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedConditions

class OperaAppiumDriver(AppiumDriver):

    def __init__(self, command_executor='http://127.0.0.1:4444/wd/hub',
                 desired_capabilities=None, browser_profile=None, proxy=None, keep_alive=False):

        capabilities = {
            'automationName' : 'Android',
            'platformName' : 'Android',
            'deviceName' : '',

            'appPackage' : 'com.opera.browser',
            'androidDeviceSocket' : 'com.opera.browser.devtools',
        }
        if desired_capabilities:
            capabilities.update(desired_capabilities)

        AppiumDriver.__init__(self, command_executor, capabilities, browser_profile, proxy, keep_alive)

        self._desired_caps = capabilities


    def swipe_left(self, duration=1):
        WebDriverWait(self, 10).until(
            ExpectedConditions.presence_of_element_located((By.ID, self.get_element_id("drag_area"))))
        pager = self.find_element_by_id('drag_area');
        flick = TouchActions(self).flick_element(pager, -1000, 0, 70);
        flick.perform();

    def get_element_id(self, el_id):
        if self._desired_caps['automationName'].lower() == 'android' and self.context == "NATIVE_APP":
            el_id = "com.opera.android.browser:id/" + el_id
        return el_id

    def find_element_by_id(self, el_id):
        el_id = self.get_element_id(el_id)
        return AppiumDriver.find_element_by_id(self, el_id)

    def skip_introduction_guide(self):
        WebDriverWait(self, 10).until(
            ExpectedConditions.visibility_of_element_located((By.ID, "continue_button"))).click()
        self.swipe_left()
        self.swipe_left()
        self.swipe_left()
        WebDriverWait(self, 20).until(ExpectedConditions.element_to_be_clickable((By.ID, "guide_finish_button"))).click()

    def open_page_in_native_context(self, url):
        url_field = WebDriverWait(self, 20).until(ExpectedConditions.element_to_be_clickable((By.ID, self.get_element_id("url_field"))))
        url_field.clear()
        url_field.send_keys(url + "\n")

    def close_native_dialog(self):
        WebDriverWait(self, 10).until(ExpectedConditions.element_to_be_clickable((By.ID, self.get_element_id("opera_dialog_button_negative")))).click()
