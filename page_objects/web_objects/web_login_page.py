from selenium.webdriver.common.by import By

# Locator tuples
username_field = (By.ID, "user-name")
password_field = (By.ID, "password")
login_button = (By.ID, "login-button")
login_error_message = (By.CSS_SELECTOR, "[data-test='error']")


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def get_username_field(self):
        return self.driver.find_element(username_field[0], username_field[1])

    def get_password_field(self):
        return self.driver.find_element(password_field[0], password_field[1])

    def get_login_button(self):
        return self.driver.find_element(login_button[0], login_button[1])

    def get_login_error_message(self):
        return self.driver.find_element(login_error_message[0], login_error_message[1])
