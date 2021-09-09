import pytest
import constants
from my_driver import sel


@pytest.fixture(scope="class")
def driver_init():
    sel.connect()
    yield
    sel.disconnect()
