from selenium.webdriver.common.by import By

first_name_field = (By.ID, "first-name")
last_name_field = (By.ID, "last-name")
postal_code_field = (By.ID, "postal-code")
continue_button = (By.ID, "continue")
finish_button = (By.ID, "finish")
success_message = (By.CLASS_NAME, "complete-header")


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def get_first_name_field(self):
        return self.driver.find_element(first_name_field[0], first_name_field[1])

    def get_last_name_field(self):
        return self.driver.find_element(last_name_field[0], last_name_field[1])

    def get_postal_code_field(self):
        return self.driver.find_element(postal_code_field[0], postal_code_field[1])

    def get_continue_button(self):
        return self.driver.find_element(continue_button[0], continue_button[1])

    def get_finish_button(self):
        return self.driver.find_element(finish_button[0], finish_button[1])

    def get_success_message(self):
        return self.driver.find_element(success_message[0], success_message[1])
