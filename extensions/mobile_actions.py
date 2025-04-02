from appium.webdriver.common.touch_action import TouchAction

import test_cases.conftest as conftest
from extensions.ui_actions import UiActions
import allure


class MobileActions(UiActions):

    @staticmethod
    @allure.step("Tap on element")
    def tap(elem, number_of_taps):
        conftest.action.tap(elem, number_of_taps).perform()

    @staticmethod
    @allure.step("Scroll")
    def scroll_by_coordinates(driver, start_x, start_y, end_x, end_y, duration=1000):
        actions = TouchAction(driver)
        actions.press(x=start_x, y=start_y).wait(ms=duration).move_to(x=end_x, y=end_y).release().perform()

