from selenium.webdriver.common.by import By

complete_text = (By.CLASS_NAME, "complete-text")
back_home_button = (By.ID, "back-to-products")


class CompletePage:
    def __init__(self, driver):
        self.driver = driver

    def get_complete_text(self):
        return self.driver.find_element(complete_text[0], complete_text[1])

    def get_back_home_button(self):
        return self.driver.find_element(back_home_button[0], back_home_button[1])
