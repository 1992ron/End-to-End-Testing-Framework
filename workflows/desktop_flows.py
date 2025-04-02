import logging

import allure

from extensions.ui_actions import UiActions
import utilities.manage_pages as page_objects


class DesktopFlows:

    @staticmethod
    @allure.step("Calculate equation")
    def calculate_flow(equation):
        for number in equation:
            DesktopFlows.calculator_click(number)
        UiActions.click(page_objects.standard_page.get_equals_button())

    @staticmethod
    def calculator_click(value):
        if value == '0':
            UiActions.click(page_objects.standard_page.get_number_zero())
        elif value == '1':
            UiActions.click(page_objects.standard_page.get_number_one())
        elif value == '2':
            UiActions.click(page_objects.standard_page.get_number_two())
        elif value == '3':
            UiActions.click(page_objects.standard_page.get_number_three())
        elif value == '4':
            UiActions.click(page_objects.standard_page.get_number_four())
        elif value == '5':
            UiActions.click(page_objects.standard_page.get_number_five())
        elif value == '6':
            UiActions.click(page_objects.standard_page.get_number_six())
        elif value == '7':
            UiActions.click(page_objects.standard_page.get_number_seven())
        elif value == '8':
            UiActions.click(page_objects.standard_page.get_number_eight())
        elif value == '9':
            UiActions.click(page_objects.standard_page.get_number_nine())
        elif value == '+':
            UiActions.click(page_objects.standard_page.get_plus_button())
        elif value == '-':
            UiActions.click(page_objects.standard_page.get_minus_button())
        elif value == '*':
            UiActions.click(page_objects.standard_page.get_multiply_button())
        elif value == '/':
            UiActions.click(page_objects.standard_page.get_divide_button())
        else:
            raise Exception('Invalid input: ' + value)

    @staticmethod
    @allure.step("Gets calculator result")
    def get_result_flow():
        result = page_objects.standard_page.get_result().text.replace("Display is", "").strip()
        return result

    @staticmethod
    @allure.step("Clear calculator page")
    def clear_calculator():
        UiActions.click(page_objects.standard_page.get_clear_button())

    @staticmethod
    @allure.step("Verifies calculator type")
    def verify_calculator_type(calculator_type: str):
        if calculator_type == "standard":
            UiActions.click(page_objects.standard_page.get_navigation_menu())
            UiActions.click(page_objects.navigation_menu_page.get_standard_calculator())
            assert page_objects.standard_page.get_calculator_header().text == "Standard"
            logging.info("For standard type the header is: 'Standard', as expected")
        elif calculator_type == "scientific":
            UiActions.click(page_objects.standard_page.get_navigation_menu())
            UiActions.click(page_objects.navigation_menu_page.get_scientific_calculator())
            assert page_objects.standard_page.get_calculator_header().text == "Scientific"
            logging.info("For scientific type the header is: 'Scientific', as expected")
        elif calculator_type == "graphing":
            UiActions.click(page_objects.standard_page.get_navigation_menu())
            UiActions.click(page_objects.navigation_menu_page.get_graphing_calculator())
            assert page_objects.standard_page.get_calculator_header().text == "Graphing"
            logging.info("For graphing type the header is: 'Graphing', as expected")
        elif calculator_type == "programmer":
            UiActions.click(page_objects.standard_page.get_navigation_menu())
            UiActions.click(page_objects.navigation_menu_page.get_programmer_calculator())
            assert page_objects.standard_page.get_calculator_header().text == "Programmer"
            logging.info("For programmer type the header is: 'Programmer', as expected")
        elif calculator_type == "date calculation":
            UiActions.click(page_objects.standard_page.get_navigation_menu())
            UiActions.click(page_objects.navigation_menu_page.get_date_calculation_calculator())
            assert page_objects.standard_page.get_calculator_header().text == "Date calculation"
            logging.info("For date calculation type the header is: 'Date calculation', as expected")


    @staticmethod
    @allure.step("Open the temperature converter calculator")
    def open_temperature_converter():
        UiActions.click(page_objects.standard_page.get_navigation_menu())
        UiActions.click(page_objects.navigation_menu_page.get_temperature_converter())
        assert page_objects.standard_page.get_calculator_header().text == "Temperature"

    @staticmethod
    @allure.step("Open the standard calculator")
    def open_standard_calculator():
        UiActions.click(page_objects.standard_page.get_navigation_menu())
        UiActions.click(page_objects.navigation_menu_page.get_standard_calculator())
        assert page_objects.standard_page.get_calculator_header().text == "Standard"
