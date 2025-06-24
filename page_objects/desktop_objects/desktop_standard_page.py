from selenium.webdriver.common.by import By

number_zero = (By.NAME, "Zero")
number_one = (By.NAME, "One")
number_two = (By.NAME, "Two")
number_three = (By.NAME, "Three")
number_four = (By.NAME, "Four")
number_five = (By.NAME, "Five")
number_six = (By.NAME, "Six")
number_seven = (By.NAME, "Seven")
number_eight = (By.NAME, "Eight")
number_nine = (By.NAME, "Nine")
plus_button = (By.NAME, "Plus")
minus_button = (By.NAME, "Minus")
multiply_button = (By.NAME, "Multiply by")
divide_button = (By.NAME, "Divide by")
equals_button = (By.NAME, "Equals")
result = (By.XPATH, "//*[@AutomationId='CalculatorResults']")
clear_button = (By.NAME, "Clear")
navigation_menu = (By.XPATH, "//*[@AutomationId='TogglePaneButton']")
calculator_header = (By.XPATH, "//*[@AutomationId='Header']")


# This class contains the elements of the Standard type calculator
class StandardPage:

    def __init__(self, driver):
        self.driver = driver

    def get_number_zero(self):
        return self.driver.find_element(number_zero[0], number_zero[1])

    def get_number_one(self):
        return self.driver.find_element(number_one[0], number_one[1])

    def get_number_two(self):
        return self.driver.find_element(number_two[0], number_two[1])

    def get_number_three(self):
        return self.driver.find_element(number_three[0], number_three[1])

    def get_number_four(self):
        return self.driver.find_element(number_four[0], number_four[1])

    def get_number_five(self):
        return self.driver.find_element(number_five[0], number_five[1])

    def get_number_six(self):
        return self.driver.find_element(number_six[0], number_six[1])

    def get_number_seven(self):
        return self.driver.find_element(number_seven[0], number_seven[1])

    def get_number_eight(self):
        return self.driver.find_element(number_eight[0], number_eight[1])

    def get_number_nine(self):
        return self.driver.find_element(number_nine[0], number_nine[1])

    def get_plus_button(self):
        return self.driver.find_element(plus_button[0], plus_button[1])

    def get_minus_button(self):
        return self.driver.find_element(minus_button[0], minus_button[1])

    def get_multiply_button(self):
        return self.driver.find_element(multiply_button[0], multiply_button[1])

    def get_divide_button(self):
        return self.driver.find_element(divide_button[0], divide_button[1])

    def get_equals_button(self):
        return self.driver.find_element(equals_button[0], equals_button[1])

    def get_result(self):
        return self.driver.find_element(result[0], result[1])

    def get_clear_button(self):
        return self.driver.find_element(clear_button[0], clear_button[1])

    def get_navigation_menu(self):
        return self.driver.find_element(navigation_menu[0], navigation_menu[1])

    def get_calculator_header(self):
        return self.driver.find_element(calculator_header[0], calculator_header[1])
