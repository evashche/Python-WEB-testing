import random
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import my_driver

class BaseWeb(object):
    failure_exception = AssertionError
    
    @property
    def locator(self):
        return self.loc

    @property
    def driver(self):
        return my_driver.sel.driver

    @property
    def element(self):
        return self.driver.find_element(By.XPATH, self.locator)

    @property
    def text_value(self):
        return self.value if hasattr(self, 'value') else ""
 
    def driver_wait(self, timeout=10):
        return WebDriverWait(self.driver, timeout)

    def fail(self, msg):
        raise self.failure_exception(msg)

    def click(self):
        try:
            self.element.click()
        except NoSuchElementException:
            self.fail(f"Unable to find element {type(self).__name__} {self.text_value} {self.locator}")

    def text(self):
        try:
            return self.element.text
        except NoSuchElementException:
            self.fail(f"Unable to find element {type(self).__name__}")
    

    def type(self, text):
        try:
            self.element.send_keys(text)
        except NoSuchElementException:
            self.fail(f"Unable to find element {type(self).__name__} {self.text_value} {self.locator}")
        return self

    def clear(self):
        self.element.clear()

    def wait_for_present(self, timeout=10):
        try:
            self.driver_wait().until(EC.visibility_of_element_located((By.XPATH, self.locator)))
        except TimeoutException:
            self.fail(f"Element {type(self).__name__} is not visible after {timeout} seconds {self.locator}")

    def is_text(self, value):
        self.wait_for_present(5)
        cur_text = self.text().strip()
        assert cur_text == value, f"Current text in element {type(self).__name__} '{cur_text}' does not match expected '{value}'"

    def is_disabled(self):
        assert self.element.get_attribute("disabled") is not None, f"Element {type(self).__name__} is enabled"

    def is_clickable(self, clickable: bool = True):
        try:
            el = self.driver_wait().until(EC.element_to_be_clickable((By.XPATH, self.locator))).is_displayed()
            if not clickable and not isinstance(el, str):
                self.fail(f"Element {type(self).__name__} '{self.text_value}' is clickable")
        except TimeoutException:
            if clickable:
                self.fail(f"Element {type(self).__name__} '{self.text_value}' is not clickable")
            else: pass
        return self

    def check_color(self):
        login_text_colour = Color.from_string(self.element.value_of_css_property('color'))
        assert login_text_colour.rgb == 'rgb(221, 44, 0)', "Color is not red"

    def send_keys_auto(self):
        self.wait_for_present()
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(self.element, f'autotest {random.randint(1, 100)}')
        actions.perform()

    def scroll_to(self):
        self.wait_for_present()
        actions = ActionChains(self.driver)
        actions.move_to_element(self.element).perform()

    def double_click(self):
        self.wait_for_present()
        actions = ActionChains(self.driver)
        actions.double_click(self.element).perform()

    def is_alert(self):
        self.click()
        alert = self.driver.switch_to.alert
        assert alert.text, "Alert has not raised as expected"

    def switch_window(self, num):
        self.driver.switch_to.window(self.driver.window_handles[num])
    
    def is_displayed(self, displayed: bool = True):
        if displayed:
            assert self.element.is_displayed(), f"Element {type(self).__name__} {self.text_value} is not displayed"
        else:
            assert not self.element.is_displayed(), f"Element {type(self).__name__} {self.text_value} is displayed {self.locator}"

    def is_url(self, url, timeout=10):
        assert self.driver_wait().until(EC.url_to_be(url)), f"Current url is not as expected {url}"

    def wait(self, time_seconds):
        time.sleep(time_seconds)
