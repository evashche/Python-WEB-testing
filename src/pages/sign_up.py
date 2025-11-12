from ..equal_text import equal_text
from ..base_web import BaseWeb

class MainForm(BaseWeb):
    def __init__(self):
        self.loc = f"//form"

    def button_text(self, text):
        return ButtonWithText(self.loc, text)
    
class ButtonWithText(BaseWeb):
    def __init__(self, loc, text):
        self.loc = f'{loc}{equal_text(text)}'


# class MainItem(BaseWeb):
#     def __init__(self, loc, pos):
#         self.loc = f"{loc}//li[{pos}]"
#
#     def click(self):
#         self.wait_for_present(3)
#         BaseWeb.click(self)
#
# class ListNavigation(BaseWeb):
#     def __init__(self):
#         self.loc = f"//div[@class='list-navigation']"
#
#
# class AboutUsLeft(BaseWeb):
#     def __init__(self):
#         self.loc = f"//ul[@data-content='about-us-list'][1]"
#
#     def get_item_by_pos(self, pos):
#         return AboutUsItem(self.loc, pos)
#
#
# class AboutUsItem(BaseWeb):
#     def __init__(self, loc, pos):
#         self.loc = f"{loc}/li[{pos}]/div[@class='links-box']"
#
#     def click(self):
#         self.wait_for_present(3)
#         BaseWeb.click(self)
#
#
# class TeamButton(BaseWeb):
#     def __init__(self):
#         self.loc = "//a[@class='tn-atom']"
#
#     def click_item(self):
#         self.wait_for_present(3)
#         self.click()
#
#
# class ApplyNetPeakBottom(BaseWeb):
#     def __init__(self):
#         self.loc = "//a[@class='btn green-btn']"
#
#     def click(self):
#         self.wait_for_present(3)
#         BaseWeb.click(self)
#
#
# class LoginForm(BaseWeb):
#     def __init__(self):
#         self.loc = "//form[@id='loginForm']"
#
#     def get_field_by_pos(self, pos):
#         if pos == 4:
#             return GDPRCheckBox()
#         else:
#             return LoginField(self.loc, pos)
#
#
# class LoginField(BaseWeb):
#     def __init__(self, loc, pos):
#         self.pos = pos
#         self.loc = f'{loc}/div[{pos}] {"/button" if pos == 5 else ""}'
#
#     @property
#     def color(self):
#         if self.pos == 1:
#             return LabelColor(self.loc)
#
#
# class LabelColor(BaseWeb):
#     def __init__(self, loc):
#         self.loc = f'{loc}//label'
#
#
# class GDPRCheckBox(BaseWeb):
#     def __init__(self):
#         self.loc = f"//md-checkbox[@class='gdpr ng-pristine ng-untouched ng-valid ng-empty']"
#
#
# class Notification(BaseWeb):
#     def __init__(self):
#         self.loc = "//md-toast"


class SignUp():
    form = MainForm()
    # about_us_left = AboutUsLeft()
    # team_button = TeamButton()
    # apply_bottom = ApplyNetPeakBottom()
    # login = LoginForm()
    # notification = Notification()
