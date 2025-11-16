import pytest
from src.constants import BASE_URL
from my_driver import sel

@pytest.fixture(autouse=True)
def driver():
    sel.connect()
    sel.driver.get(BASE_URL)
    sel.driver.implicitly_wait(10)
    yield
    sel.disconnect()

