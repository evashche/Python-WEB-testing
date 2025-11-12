import constants
from selenium import webdriver


class WebDriverRapper(object):
    def __init__(self):
        self.driver = None

    def connect(self):
        self.driver = webdriver.Firefox()
        self.driver.set_window_size(1920, 1080)

    def disconnect(self):
        self.driver.quit()


sel = WebDriverRapper()

