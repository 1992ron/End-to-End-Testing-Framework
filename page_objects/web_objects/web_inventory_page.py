from selenium.webdriver.common.by import By

inventory_container = (By.ID, "inventory_container")
menu_button = (By.ID, "react-burger-menu-btn")
logout_link = (By.ID, "logout_sidebar_link")
add_to_cart_button_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
add_to_cart_button_t_shirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
add_to_cart_button_onesie = (By.ID, "add-to-cart-sauce-labs-onesie")
add_to_cart_button_bike_light = (By.ID, "add-to-cart-sauce-labs-bike-light")
add_to_cart_button_fleece_jacket = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
add_to_cart_button_allthethings_t_shirt = (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
shopping_cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
shopping_cart_icon = (By.CLASS_NAME, "shopping_cart_link")
add_to_cart_buttons = (By.CLASS_NAME, "btn_inventory")


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def get_inventory_container(self):
        return self.driver.find_element(inventory_container[0], inventory_container[1])

    def get_menu_button(self):
        return self.driver.find_element(menu_button[0], menu_button[1])

    def get_logout_link(self):
        return self.driver.find_element(logout_link[0], logout_link[1])

    def get_add_to_cart_button_backpack(self):
        return self.driver.find_element(add_to_cart_button_backpack[0], add_to_cart_button_backpack[1])

    def get_add_to_cart_button_t_shirt(self):
        return self.driver.find_element(add_to_cart_button_t_shirt[0], add_to_cart_button_t_shirt[1])

    def get_add_to_cart_button_onesie(self):
        return self.driver.find_element(add_to_cart_button_onesie[0], add_to_cart_button_onesie[1])

    def get_add_to_cart_button_bike_light(self):
        return self.driver.find_element(add_to_cart_button_bike_light[0], add_to_cart_button_bike_light[1])

    def get_add_to_cart_button_fleece_jacket(self):
        return self.driver.find_element(add_to_cart_button_fleece_jacket[0], add_to_cart_button_fleece_jacket[1])

    def get_add_to_cart_button_allthethings_t_shirt(self):
        return self.driver.find_element(add_to_cart_button_allthethings_t_shirt[0], add_to_cart_button_allthethings_t_shirt[1])

    def get_shopping_cart_badge(self):
        return self.driver.find_element(shopping_cart_badge[0], shopping_cart_badge[1])

    def get_shopping_cart_icon(self):
        return self.driver.find_element(shopping_cart_icon[0], shopping_cart_icon[1])

    def get_add_to_cart_buttons(self):
        return self.driver.find_elements(add_to_cart_buttons[0], add_to_cart_buttons[1])

    def get_shopping_cart_badges(self):
        # returns a list; empty if no badge is present
        return self.driver.find_elements(shopping_cart_badge[0], shopping_cart_badge[1])


