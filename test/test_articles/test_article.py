from src.constants import Icons
from src.pages.main import Main

class TestArticle():
    main = Main()
    articles = main.articles
    article = articles.article_by_pos(1)

    def test_scroll_addition(self):
        self.articles.article_by_pos(2).scroll_to()
        self.articles.article_by_pos(5).is_displayed()

    def test_like_increment(self):
        counter = self.article.actions().like_viewer().text()
        self.article.content().double_click()
        self.article.actions().like_viewer().is_text(counter + 1)
    
    def test_icon_panel(self):
        self.article.actions().icon_panel().icon_text(Icons.LIKE).is_displayed()
        self.article.actions().icon_panel().icon_text(Icons.SHARE).click()
        self.main.pop_up.title().is_text(Icons.SHARE)