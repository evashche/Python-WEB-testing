from src.base_web import BaseWeb

def equal_text(text):
    return f"//self::*[normalize-space(text()) = \'{text}\']"

def contains_text(text):
    return f"//*[contains(text(), \'{text}\']"

class ButtonText(BaseWeb):
    def __init__(self, loc, text):
        self.value = text
        self.loc = f'{loc}//button{equal_text(text)}'

class FieldText(BaseWeb):
    def __init__(self, loc, text):
        self.value = text
        self.loc = f'{loc}//label{equal_text(text)}//ancestor::label//input'

class FieldPos(BaseWeb):
    def __init__(self, loc, pos):
        self.loc = f'({loc}//label)[{pos}]'

class LinkText(BaseWeb):
    def __init__(self, loc, text):
        self.value = text
        self.loc = f'{loc}//a{equal_text(text)}'

class IconText(BaseWeb):
    def __init__(self, loc, text):
        self.value = text
        self.loc = f"{loc}//div{equal_text(text)}"

class Link(BaseWeb):
    def __init__(self, loc, text):
        self.value = text
        self.loc = f'{loc}//a'

class OptionValue(BaseWeb):
    def __init__(self, loc, text):
        self.value = text
        self.loc = f"{loc}//option[@value = '{text}']"

class Title(BaseWeb):
    def __init__(self, loc):
        self.loc = f"{loc}//h2"