from src.pages.sign_up import SignUp
from src.constants import *

class TestSignUp():
    su = SignUp()

    def test_form_fields_content(self):
        for field in FieldsSignInLocal.EN.value:
            self.su.form.field_text(field).is_displayed()
        self.su.footer.language().option_value('de').click()
        for field in FieldsSignInLocal.DE.value:
            self.su.form.field_text(field).is_displayed()
    
    def test_form_fields_layout(self):
        for i in range(len(FieldsSignInLocal.EN.value)):
            self.su.form.field_by_pos(i + 1).is_text(FieldsSignInLocal.EN.value[i])

    def test_empty_form_buttons(self):
        self.su.form.button_text(ButtonsSignIn.LOGIN.value).is_clickable()
        self.su.form.button_text(ButtonsSignIn.SIGN_UP.value).is_clickable(False)

    def test_footer_links(self):
        for link in Links:
            self.su.footer.link_text(link.value).is_clickable()
    
    def test_form_fields_validation(self):
        self.su.form.field_text(FieldsLogin.MOBILE_OR_EMAIL.value).type(1)
        self.su.form.field_text(FieldsLogin.PASSWORD.value).type(1)
        self.su.form.field_text(FieldsLogin.MOBILE_OR_EMAIL.value).clear()
        self.su.form.field_text(FieldsLogin.FULL_NAME.value).click()
        self.su.form.field_following_error(FieldsLogin.MOBILE_OR_EMAIL.value, REQUIRED_FIELD_ERROR).is_displayed()
        self.su.form.field_following_error(FieldsLogin.PASSWORD.value, PASSWORD_ERROR).is_displayed()
        
        