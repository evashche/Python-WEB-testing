import pytest
from src.constants import SIGN_UP_URL
from my_driver import sel

@pytest.fixture(autouse=True)
def driver():
    sel.connect()
    sel.driver.get(SIGN_UP_URL)
    sel.driver.implicitly_wait(10)
    yield
    sel.disconnect()

