from ..base_elements import *
from ..base_web import BaseWeb

class MainForm(BaseWeb):
    def __init__(self):
        self.loc = f"//main//form"

    def button_text(self, text):
        return ButtonText(self.loc, text)

    def field_text(self, text):
        return FieldText(self.loc, text)

    def field_by_pos(self, pos):
        return FieldPos(self.loc, pos)
    
    def link_text(self, text):
        return LinkText(self.loc, text)
    
    def field_following_error(self, text, error):
        self.loc = FieldText(self.loc, text).loc
        return FieldError(self.loc, error)

class FieldError(BaseWeb):
    def __init__(self, loc, error):
        self.loc = f"{loc}//ancestor::label//parent::div/following::div{equal_text(error)}"

class DisplayLanguage(BaseWeb):
    def __init__(self, loc):
        self.loc = f"{loc}//select[@aria-label='Switch Display Language']"

    def option_value(self, value):
        return OptionValue(self.loc, value)
    
class Footer(BaseWeb):
    def __init__(self):
        self.loc = f"//footer"

    def link_text(self, text):
        return LinkText(self.loc, text)

    def language(self):
        return DisplayLanguage(self.loc)


class SignUp():
    form = MainForm()
    footer = Footer()
