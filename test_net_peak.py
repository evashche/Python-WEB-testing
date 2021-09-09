import pytest

import base_web
import constants
from base_web import BaseTest
from page_locators import PageLocators


class TestNetPeak(BaseTest):

    def test_net_peak(self):
        pl = PageLocators()
        pl.main_left.get_item_by_pos(3).click()
        pl.about_us_left.get_item_by_pos(3).click()
        pl.team_button.click()
        pl.switch_window(1)
        pl.is_url(constants.CAREER)
        pl.apply_bottom.is_clickable(True)
        pl.wait(2)
        pl.switch_window(0)
        pl.main_right.get_item_by_pos(1).click()
        pl.switch_window(1)
        pl.login.get_field_by_pos(1).send_keys_auto()
        pl.login.get_field_by_pos(2).send_keys_auto()
        pl.login.get_field_by_pos(5).is_disabled()
        pl.login.get_field_by_pos(4).click()
        pl.login.get_field_by_pos(5).click()
        pl.notification.wait_for_present()
        pl.login.get_field_by_pos(1).color.check_color()
