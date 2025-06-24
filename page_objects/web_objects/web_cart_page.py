from selenium.webdriver.common.by import By

cart_list = (By.CLASS_NAME, "cart_list")
checkout_button = (By.ID, "checkout")
cart_list_container = (By.CLASS_NAME, "cart_list")


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def get_cart_list(self):
        return self.driver.find_element(cart_list[0], cart_list[1])

    def get_checkout_button(self):
        return self.driver.find_element(checkout_button[0], checkout_button[1])

    # Returns the <div class="cart_list"> element in order to wait for the cart to be visible
    def get_cart_list_container(self):
        return self.driver.find_element(cart_list_container[0], cart_list_container[1])
