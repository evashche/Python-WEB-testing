import pytest
from constants import SIGN_UP_URL, BASE_URL, LOGIN_URL
from my_driver import sel


@pytest.fixture(scope="class")
def driver_base():
    sel.connect()
    sel.driver.get(BASE_URL)
    sel.driver.implicitly_wait(10)
    yield
    sel.disconnect()

@pytest.fixture(scope="class")
def driver_sign_up():
    sel.connect()
    sel.driver.get(SIGN_UP_URL)
    sel.driver.implicitly_wait(10)
    yield
    sel.disconnect()

@pytest.fixture(scope="class")
def driver_login():
    sel.connect()
    sel.driver.get(LOGIN_URL)
    sel.driver.implicitly_wait(10)
    yield
    sel.disconnect()
