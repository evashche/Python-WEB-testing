from selenium.webdriver.support.color import Color

from base_web import BaseTest


class MenuBar(BaseTest):
    def __init__(self):
        self.loc = f"//nav[@class='menu custom-site-box']"


class MainNavigationRight(BaseTest):
    def __init__(self):
        self.loc = f"//div[@class='main-navigation']/div[2]"

    def get_item_by_pos(self, pos):
        return MainItem(self.loc, pos)


class MainNavigationLeft(BaseTest):
    def __init__(self):
        self.loc = f"//div[@class='main-navigation']/div[1]"

    def get_item_by_pos(self, pos):
        return MainItem(self.loc, pos)


class MainItem(BaseTest):
    def __init__(self, loc, pos):
        self.loc = f"{loc}//li[{pos}]"

    def click(self):
        self.wait_for_present(3)
        BaseTest.click(self)


class ListNavigation(BaseTest):
    def __init__(self):
        self.loc = f"//div[@class='list-navigation']"


class AboutUsLeft(BaseTest):
    def __init__(self):
        self.loc = f"//ul[@data-content='about-us-list'][1]"

    def get_item_by_pos(self, pos):
        return AboutUsItem(self.loc, pos)


class AboutUsItem(BaseTest):
    def __init__(self, loc, pos):
        self.loc = f"{loc}/li[{pos}]/div[@class='links-box']"

    def click(self):
        self.wait_for_present(3)
        BaseTest.click(self)


class TeamButton(BaseTest):
    def __init__(self):
        self.loc = "//a[@class='tn-atom']"

    def click_item(self):
        self.wait_for_present(3)
        self.click()


class ApplyNetPeakBottom(BaseTest):
    def __init__(self):
        self.loc = "//a[@class='btn green-btn']"

    def click(self):
        self.wait_for_present(3)
        BaseTest.click(self)


class LoginForm(BaseTest):
    def __init__(self):
        self.loc = "//form[@id='loginForm']"

    def get_field_by_pos(self, pos):
        if pos == 4:
            return GDPRCheckBox()
        else:
            return LoginField(self.loc, pos)


class LoginField(BaseTest):
    def __init__(self, loc, pos):
        self.pos = pos
        self.loc = f'{loc}/div[{pos}] {"/button" if pos == 5 else ""}'

    @property
    def color(self):
        if self.pos == 1:
            return LabelColor(self.loc)


class LabelColor(BaseTest):
    def __init__(self, loc):
        self.loc = f'{loc}//label'


class GDPRCheckBox(BaseTest):
    def __init__(self):
        self.loc = f"//md-checkbox[@class='gdpr ng-pristine ng-untouched ng-valid ng-empty']"


class Notification(BaseTest):
    def __init__(self):
        self.loc = "//md-toast"


class PageLocators(BaseTest):
    main_left = MainNavigationLeft()
    main_right = MainNavigationRight()
    about_us_left = AboutUsLeft()
    team_button = TeamButton()
    apply_bottom = ApplyNetPeakBottom()
    login = LoginForm()
    notification = Notification()
