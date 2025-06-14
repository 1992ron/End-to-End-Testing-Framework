from selenium.webdriver.common.by import By

inventory_container = (By.ID, "inventory_container")
menu_button = (By.ID, "react-burger-menu-btn")
logout_link = (By.ID, "logout_sidebar_link")
add_to_cart_buttons = (By.CLASS_NAME, "btn_inventory")
shopping_cart_badge = (By.CLASS_NAME, "shopping_cart_badge")


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def get_inventory_container(self):
        return self.driver.find_element(inventory_container[0], inventory_container[1])

    def get_menu_button(self):
        return self.driver.find_element(menu_button[0], menu_button[1])

    def get_logout_link(self):
        return self.driver.find_element(logout_link[0], logout_link[1])

    def get_add_to_cart_buttons(self):
        return self.driver.find_elements(add_to_cart_buttons[0], add_to_cart_buttons[1])

    def get_shopping_cart_badge(self):
        return self.driver.find_element(shopping_cart_badge[0], shopping_cart_badge[1])
