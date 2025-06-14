import allure
import pytest
from extensions.verifications import Verifications
from workflows.desktop_flows import DesktopFlows
import utilities.manage_pages as page_objects


@pytest.mark.usefixtures('init_desktop_driver')
class TestDesktop:
    @allure.title("Test 01: Adding 2 numbers")
    @allure.description("This test adds 2 number and verify the result")
    def test_add_numbers_and_verify(self):
        DesktopFlows.open_standard_calculator()
        DesktopFlows.calculate_flow('1+7')
        Verifications.verify_object_comparison(DesktopFlows.get_result_flow(), "8")

    @allure.title("Test case 02: Arithmetic actions")
    @allure.description("This test performs arithmetic actions and verifies it")
    def test_arithmetic_actions(self):
        # Clear the calculator result for the test
        DesktopFlows.clear_calculator()
        DesktopFlows.calculate_flow('2*5+50/2-25')
        Verifications.verify_object_comparison(DesktopFlows.get_result_flow(), "5")

    @allure.title("Test 03: Change calculator type")
    @allure.description("This test change and verify calculator types")
    def test_change_and_verify_calculator_type(self):
        # Clear the calculator result for the next test
        DesktopFlows.clear_calculator()
        DesktopFlows.verify_calculator_type("scientific")
        DesktopFlows.verify_calculator_type("graphing")
        DesktopFlows.verify_calculator_type("programmer")
        DesktopFlows.verify_calculator_type("date calculation")
        DesktopFlows.verify_calculator_type("standard")

    @allure.title("Test 04: Convert temperature")
    @allure.description("This test converts the temperature from fahrenheit to celsius")
    def test_convert_fahrenheit_to_celsius(self):
        DesktopFlows.open_standard_calculator()
        DesktopFlows.open_temperature_converter()
        # Enter "104" in the Fahrenheit field
        DesktopFlows.calculator_click("1")
        DesktopFlows.calculator_click("0")
        DesktopFlows.calculator_click("4")
        expected_result_in_celsius = "Converts into 40 Celsius"
        actual_result_in_celsius = page_objects.temperature_converter_page.get_temperature_in_celsius().text
        # Verify the expected result matches the actual result
        assert expected_result_in_celsius == actual_result_in_celsius, "f(The expected result in Celsius is 40, but the actual result is: {result_in_celsius})"
