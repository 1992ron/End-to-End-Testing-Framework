from selenium.webdriver.common.by import By

cart_list = (By.CLASS_NAME, "cart_list")
checkout_button = (By.ID, "checkout")


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def get_cart_list(self):
        return self.driver.find_element(cart_list[0], cart_list[1])

    def get_checkout_button(self):
        return self.driver.find_element(checkout_button[0], checkout_button[1])
