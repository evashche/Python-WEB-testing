from src.pages.sign_up import SignUp
from src.constants import *

class TestAccountsLogin():
    su = SignUp()

    def test_form_fields_content(self):
        for field in FieldsLoginLocal.EN.value:
            self.su.form.field_text(field).is_displayed()
        self.su.footer.language().option_value('de').click()
        for field in FieldsLoginLocal.DE.value:
            self.su.form.field_text(field).is_displayed()
    
    def test_form_fields_layout(self):
        for i in range(len(FieldsLoginLocal.EN.value)):
            self.su.form.field_by_pos(i + 1).is_text(FieldsLoginLocal.EN.value[i])

    def test_empty_form_buttons(self):
        self.su.form.button_text(ButtonsLogIn.LOGIN.value).is_clickable(False)
        self.su.form.button_text(ButtonsLogIn.LOGIN_FACEBOOK.value).is_clickable(True)

    def test_footer_links(self):
        for link in Links:
            self.su.footer.link_text(link.value).is_clickable()
    
    def test_filled_form_button(self):
        self.su.form.field_text(FieldsLogin.MOBILE_OR_EMAIL.value).type(1)
        self.su.form.field_text(FieldsLogin.PASSWORD.value).type(1)
        self.su.form.button_text(ButtonsLogIn.LOGIN.value).is_clickable()
        