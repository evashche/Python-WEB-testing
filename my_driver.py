import constants


class WebDriverRapper(object):
    def __init__(self):
        self.driver = None

    def connect(self):
        from selenium import webdriver
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(constants.HOMEPAGE)
        self.driver.implicitly_wait(10)

    def disconnect(self):
        self.driver.quit()


sel = WebDriverRapper()

