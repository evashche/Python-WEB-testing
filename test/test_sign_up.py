import pytest
from constants import LOGIN_FACEBOOK
from src.base_web import BaseWeb
from src.pages.sign_up import SignUp

@pytest.mark.usefixtures("driver_sign_up")
class TestSignUp(BaseWeb):

    def test_sign_up(self):
        su = SignUp()
        su.form.button_text(LOGIN_FACEBOOK).is_clickable(True)
        