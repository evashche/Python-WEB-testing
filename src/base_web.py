import random
import time
import pytest
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import my_driver


# @pytest.mark.usefixtures("driver_base")
class BaseWeb(object):
    failure_exception = AssertionError
    
    @property
    def locator(self):
        return self.loc

    @property
    def driver(self):
        return my_driver.sel.driver

    def fail(self, msg):
        raise self.failure_exception(msg)

    def click(self):
        try:
            self.driver.find_element_by_xpath(self.locator).click()
        except NoSuchElementException:
            self.fail(f"Unable to find element {type(self).__name__}")

    def text(self):
        try:
            return self.driver.find_element_by_xpath(self.locator).text
        except NoSuchElementException:
            self.fail(f"Unable to find element {type(self).__name__}")

    def wait_for_present(self, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located((By.XPATH, self.locator)))
        except TimeoutException:
            self.fail(f"Element {type(self).__name__} is not visible after {timeout} seconds")

    def is_text(self, value):
        self.wait_for_present(3)
        cur_text = self.text.strip()
        assert cur_text == value, f"Current text in element {type(self).__name__} '{cur_text}' does not match expected '{value}'"

    def is_disabled(self):
        elem = self.driver.find_element_by_xpath(self.locator)
        assert elem.get_attribute("disabled") is not None, f"Element {type(self).__name__} is enabled"

    def is_clickable(self, value: bool):
        elem = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.locator)))
        if value:
            assert elem, f'element is not visible or not enabled'
        else:
            assert not elem, f'element is visible or enabled'

    def check_color(self):
        elem = self.driver.find_element_by_xpath(self.locator)
        login_text_colour = Color.from_string(elem.value_of_css_property('color'))
        assert login_text_colour.rgb == 'rgb(221, 44, 0)', "Color is not red"

    def send_keys_auto(self):
        self.wait_for_present()
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(self.driver.find_element_by_xpath(self.locator), f'autotest {random.randint(1, 100)}')
        actions.perform()

    def is_alert(self):
        self.click()
        alert = self.driver.switch_to.alert
        assert alert.text, "Alert has not raised as expected"

    def switch_window(self, num):
        self.driver.switch_to.window(self.driver.window_handles[num])

    def is_url(self, url, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        assert wait.until(EC.url_to_be(url)), f"Current url is not as expected {url}"

    def wait(self, time_seconds):
        time.sleep(time_seconds)
