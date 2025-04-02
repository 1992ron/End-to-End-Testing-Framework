import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
import test_cases.conftest as conftest


class UiActions:

    @staticmethod
    @allure.step("Click on a web element")
    def click(elem: WebElement):
        elem.click()

    @staticmethod
    @allure.step("Updating the text of an input field")
    def update_text(elem: WebElement, value):
        elem.clear()
        if value is None:
            elem.send_keys("")
        else:
            elem.send_keys(f"{value}")

    @staticmethod
    @allure.step("Mouse hover over one element and click it")
    def mouse_hover_on_tooltip(elem: WebElement):
        ActionChains(conftest.driver).move_to_element(elem).click().perform()

    @staticmethod
    @allure.step("Mouse hover over two elements and click the second one")
    def mouse_hover(elem1: WebElement, elem2: WebElement):
        ActionChains(conftest.driver).move_to_element(elem1).move_to_element(elem2).click().perform()

    @staticmethod
    @allure.step("Drag and drop")
    def drag_and_drop(elem1: WebElement, elem2: WebElement):
        ActionChains(conftest.driver).drag_and_drop(elem1, elem2).perform()

    @staticmethod
    @allure.step("Clear a text field")
    def clear(elem: WebElement):
        elem.clear()
