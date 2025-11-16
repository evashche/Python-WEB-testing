from ..base_elements import *
from ..base_web import BaseWeb

class Articles(BaseWeb):
    def __init__(self):
        self.loc = f"//article"
    
    def article_by_pos(self, pos):
        return Article(self.loc, pos)

class Article(BaseWeb):
    def __init__(self, loc, pos):
        self.loc = f"{loc}[{pos}]"
    
    def autor(self):
        return Author(self.loc)

    def content(self):
        return Content(self.loc)

    def actions(self):
        return Actions(self.loc)

class Author(BaseWeb):
    def __init__(self, loc):
        self.loc = f"{loc}/div/div[1]"

class Content(BaseWeb):
    def __init__(self, loc):
        self.loc = f"{loc}/div/div[2]"

class Actions(BaseWeb):
    def __init__(self, loc):
        self.loc = f"{loc}/div/div[3]"
    
    def like_viewer(self):
        return LikeViewer(self.loc) 
    
    def icon_panel(self):
        return IconPanel(self.loc)

class LikeViewer(BaseWeb):
    def __init__(self, loc):
        self.loc = f"{loc}//section[2]"

class IconPanel(BaseWeb):
    def __init__(self, loc):
        self.loc = f"{loc}//section[1]"

    def icon_text(self, text):
        return IconText(self.loc, text)

class PopUp(BaseWeb):
    def __init__(self):
        self.loc = f"//div[@id = 'has-finished-comet-page']/following-sibling::div[2]"
    
    def title(self):
        return Title(self.loc)


class Main():
    articles = Articles()
    pop_up = PopUp()

