import logging
import allure
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
import utilities.manage_pages as page_objects
from extensions.ui_actions import UiActions
from extensions.verifications import Verifications
from utilities.common_ops import wait, ExpectedConditions
import test_cases.conftest as conftest
import page_objects.web_objects.web_cart_page as web_cart_page
import page_objects.web_objects.web_checkout_page as web_checkout_page
import page_objects.web_objects.web_login_page as web_login_page
import page_objects.web_objects.web_inventory_page as web_inventory_page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utilities.common_ops import get_configuration_data


class WebFlows:
    # Configure logging for this class
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    @staticmethod
    @allure.step("Perform login to SauceDemo")
    def submit_login_credentials(username, password):
        # Always navigate to the login page
        conftest.driver.get(get_configuration_data('Url'))
        # Enter username
        UiActions.update_text(page_objects.web_login_page.get_username_field(), username)
        # Enter password
        UiActions.update_text(page_objects.web_login_page.get_password_field(), password)
        # Click the login button
        UiActions.click(page_objects.web_login_page.get_login_button())
        # Wait for inventory page to be visible
        wait(ExpectedConditions.ELEMENT_IS_VISIBLE, web_inventory_page.inventory_container)
        # Verify inventory container is visible
        Verifications.element_is_displayed(page_objects.web_inventory_page.get_inventory_container())
        logging.info("Login successful – inventory page is displayed")

    @staticmethod
    @allure.step("Login attempt without entering a username")
    def login_without_username():
        WebFlows.go_to_login_page()
        # Enter the password
        UiActions.update_text(page_objects.web_login_page.get_password_field(), "secret_sauce")
        # Click the login button
        UiActions.click(page_objects.web_login_page.get_login_button())
        error = page_objects.web_login_page.get_login_error_message().text
        # Verify the correct error message is displayed
        Verifications.verify_object_comparison("Epic sadface: Username is required", error)
        logging.info("Correct error message is displayed - 'Epic sadface: Username is required'")

    @staticmethod
    @allure.step("Login attempt without entering a password")
    def login_without_password():
        WebFlows.go_to_login_page()
        # Enter the username
        UiActions.update_text(page_objects.web_login_page.get_username_field(), "standard_user")
        # Click the login button
        UiActions.click(page_objects.web_login_page.get_login_button())
        error = page_objects.web_login_page.get_login_error_message().text
        # Verify the correct error message is displayed
        Verifications.verify_object_comparison("Epic sadface: Password is required", error)
        logging.info("Correct error message is displayed: 'Epic sadface - Password is required'")

    @staticmethod
    @allure.step("Login attempt with a locked out user")
    def login_locked_out_user():
        WebFlows.go_to_login_page()
        # Enter the username
        UiActions.update_text(page_objects.web_login_page.get_username_field(), "locked_out_user")
        # Enter the password
        UiActions.update_text(page_objects.web_login_page.get_password_field(), "secret_sauce")
        # Click the login button
        UiActions.click(page_objects.web_login_page.get_login_button())
        error = page_objects.web_login_page.get_login_error_message().text
        # Verify the correct error message is displayed
        Verifications.verify_object_comparison("Epic sadface: Sorry, this user has been locked out.", error)
        logging.info("Correct error message is displayed - 'Epic sadface: Sorry, this user has been locked out.'")

    @staticmethod
    @allure.step("Navigate to the login page")
    def go_to_login_page():
        conftest.driver.get(get_configuration_data("Url"))
        wait(ExpectedConditions.ELEMENT_IS_VISIBLE, web_login_page.login_button)

    @staticmethod
    @allure.step("Logout from SauceDemo")
    def logout():
        # Open the menu
        UiActions.click(page_objects.web_inventory_page.get_menu_button())
        # Click the logout link
        UiActions.click(page_objects.web_inventory_page.get_logout_link())
        # Wait for login button to be visible again
        wait(ExpectedConditions.ELEMENT_IS_VISIBLE, web_login_page.login_button)
        # Verify login button is visible again
        Verifications.element_is_displayed(page_objects.web_login_page.get_login_button())
        logging.info("Logout successful – returned to login page")

    @staticmethod
    @allure.step("Add backpack item to cart")
    def add_backpack_to_cart():
        # Click 'Add to cart' for the backpack item
        UiActions.click(page_objects.web_inventory_page.get_add_to_cart_button_backpack())
        # wait for the button to switch over to Remove
        remove_locator = (By.ID, "remove-sauce-labs-backpack")
        wait(ExpectedConditions.ELEMENT_IS_VISIBLE, remove_locator)
        # verify the "Add to cart" button changes to “Remove”
        remove_btn = conftest.driver.find_element(*remove_locator)
        Verifications.verify_object_comparison("Remove", remove_btn.text)
        logging.info("Backpack was added to cart (Remove button is now visible)")

    @staticmethod
    @allure.step("Add t-shirt item to cart")
    def add_t_shirt_to_cart():
        # Click 'Add to cart' for the t-shirt
        UiActions.click(page_objects.web_inventory_page.get_add_to_cart_button_t_shirt())
        # wait for the button to switch over to Remove
        remove_locator = (By.ID, "remove-sauce-labs-bolt-t-shirt")
        wait(ExpectedConditions.ELEMENT_IS_VISIBLE, remove_locator)
        # verify the "Add to cart" button changes to “Remove”
        remove_btn = conftest.driver.find_element(*remove_locator)
        Verifications.verify_object_comparison("Remove", remove_btn.text)
        logging.info("T-shirt was added to cart (Remove button is now visible)")

    @staticmethod
    @allure.step("Add onesie item to cart")
    def add_onesie_to_cart():
        UiActions.click(page_objects.web_inventory_page.get_add_to_cart_button_onesie())
        # wait for the button to switch over to Remove
        remove_locator = (By.ID, "remove-sauce-labs-onesie")
        wait(ExpectedConditions.ELEMENT_IS_VISIBLE, remove_locator)
        # verify the "Add to cart" button changes to “Remove”
        remove_btn = conftest.driver.find_element(*remove_locator)
        Verifications.verify_object_comparison("Remove", remove_btn.text)
        logging.info("Onesie was added to cart (Remove button is now visible)")

    @staticmethod
    @allure.step("Add bike light item to cart")
    def add_bike_light_to_cart():
        UiActions.click(page_objects.web_inventory_page.get_add_to_cart_button_bike_light())
        # wait for the button to switch over to Remove
        remove_locator = (By.ID, "remove-sauce-labs-bike-light")
        wait(ExpectedConditions.ELEMENT_IS_VISIBLE, remove_locator)
        # verify the "Add to cart" button changes to “Remove”
        remove_btn = conftest.driver.find_element(*remove_locator)
        Verifications.verify_object_comparison("Remove", remove_btn.text)
        logging.info("Backpack was added to cart (Remove button is now visible)")

    @staticmethod
    @allure.step("Add fleece jacket item to cart")
    def add_fleece_jacket_to_cart():
        UiActions.click(page_objects.web_inventory_page.get_add_to_cart_button_fleece_jacket())
        # wait for the button to switch over to Remove
        remove_locator = (By.ID, "remove-sauce-labs-fleece-jacket")
        wait(ExpectedConditions.ELEMENT_IS_VISIBLE, remove_locator)
        # verify the "Add to cart" button changes to “Remove”
        remove_btn = conftest.driver.find_element(*remove_locator)
        Verifications.verify_object_comparison("Remove", remove_btn.text)
        logging.info("Backpack was added to cart (Remove button is now visible)")

    @staticmethod
    @allure.step("Add 'All The Things' t-shirt to cart")
    def add_allthethings_t_shirt_to_cart():
        UiActions.click(page_objects.web_inventory_page.get_add_to_cart_button_allthethings_t_shirt())
        # wait for the button to switch over to Remove
        remove_locator = (By.ID, "remove-test.allthethings()-t-shirt-(red)")
        wait(ExpectedConditions.ELEMENT_IS_VISIBLE, remove_locator)
        # verify the "Add to cart" button changes to “Remove”
        remove_btn = conftest.driver.find_element(*remove_locator)
        Verifications.verify_object_comparison("Remove", remove_btn.text)
        logging.info("Backpack was added to cart (Remove button is now visible)")

    @staticmethod
    @allure.step("Remove an item from the inventory page")
    def remove_item_from_inventory():
        # Find all 'Remove' buttons (visible when items are in cart)
        remove_buttons = conftest.driver.find_elements(By.XPATH, "//button[text()='Remove']")
        if not remove_buttons:
            logging.warning("No items to remove from inventory")
            return

        # Record initial badge count
        initial_count = int(page_objects.web_inventory_page.get_shopping_cart_badge().text)
        # Click the first 'Remove' button
        UiActions.click(remove_buttons[0])

        # Wait until the badge text updates to initial_count - 1
        expected = str(initial_count - 1)
        wait(ExpectedConditions.TEXT_TO_BE_PRESENT_IN_ELEMENT,
             web_inventory_page.shopping_cart_badge,
             expected)

        # Verify the new badge count
        Verifications.verify_object_comparison(expected,
                                               page_objects.web_inventory_page.get_shopping_cart_badge().text)
        logging.info("Item successfully removed from inventory page")

    @staticmethod
    @allure.step("Navigate to cart page")
    def go_to_cart():
        # Click on the shopping cart icon
        UiActions.click(page_objects.web_inventory_page.get_shopping_cart_icon())
        # Wait for the cart list container to appear
        wait(ExpectedConditions.ELEMENT_IS_VISIBLE,
             web_cart_page.cart_list_container)
        # Verify the cart page is displayed
        Verifications.element_is_displayed(page_objects.web_cart_page.get_checkout_button())
        logging.info("Navigated to cart page")

    @staticmethod
    @allure.step("Proceed to checkout step one")
    def proceed_to_checkout():
        # Click the 'Checkout' button
        UiActions.click(page_objects.web_cart_page.get_checkout_button())
        # Wait for the checkout-info form to load
        wait(ExpectedConditions.ELEMENT_IS_VISIBLE, web_checkout_page.first_name_field)
        # Verify first name field is displayed
        Verifications.element_is_displayed(page_objects.web_checkout_page.get_first_name_field())
        logging.info("Proceeded to checkout step one")

    @staticmethod
    @allure.step("Fill all the checkout fields")
    def fill_checkout_form(first_name, last_name, postal_code):
        # Enter first name, last name, and postal code
        UiActions.update_text(page_objects.web_checkout_page.get_first_name_field(), first_name)
        UiActions.update_text(page_objects.web_checkout_page.get_last_name_field(), last_name)
        UiActions.update_text(page_objects.web_checkout_page.get_postal_code_field(), postal_code)
        logging.info("Checkout form filled: %s %s %s", first_name, last_name, postal_code)

    @staticmethod
    @allure.step("Fill the checkout form without first name")
    def checkout_without_first_name():
        UiActions.click(page_objects.web_checkout_page.get_continue_button())
        first_name_missing_error = page_objects.web_checkout_page.get_checkout_error_message().text
        Verifications.verify_object_comparison("Error: First Name is required", first_name_missing_error)

    @staticmethod
    @allure.step("Fill the checkout form without last name")
    def checkout_without_last_name():
        UiActions.update_text(page_objects.web_checkout_page.get_first_name_field(), "Jane")
        UiActions.click(page_objects.web_checkout_page.get_continue_button())
        last_name_missing_error = page_objects.web_checkout_page.get_checkout_error_message().text
        Verifications.verify_object_comparison("Error: Last Name is required",last_name_missing_error)

    @staticmethod
    @allure.step("Fill the checkout form without postal code")
    def checkout_without_postal_code():
        UiActions.update_text(page_objects.web_checkout_page.get_last_name_field(), "Doe")
        UiActions.click(page_objects.web_checkout_page.get_continue_button())
        postal_code_missing_error = page_objects.web_checkout_page.get_checkout_error_message().text
        Verifications.verify_object_comparison("Error: Postal Code is required", postal_code_missing_error)

    @staticmethod
    @allure.step("Continue to checkout overview")
    def continue_checkout():
        # Click 'Continue'
        UiActions.click(page_objects.web_checkout_page.get_continue_button())
        # Wait for the summary container
        wait(ExpectedConditions.ELEMENT_IS_VISIBLE, web_checkout_page.checkout_summary_container)
        # Verify summary is displayed
        Verifications.element_is_displayed(page_objects.web_checkout_page.get_checkout_summary_container())
        logging.info("Proceeded to checkout overview")

    @staticmethod
    @allure.step("Finish checkout process")
    def finish_checkout():
        # Click 'Finish'
        UiActions.click(page_objects.web_checkout_page.get_finish_button())
        # Wait for the complete header
        wait(ExpectedConditions.ELEMENT_IS_VISIBLE, web_checkout_page.success_message)
        # Verify thank-you message
        Verifications.verify_object_comparison(
            "Thank you for your order!",
            page_objects.web_checkout_page.get_success_message().text
        )
        logging.info("Checkout finished successfully")

    @staticmethod
    @allure.step("Remove an item from the inventory page")
    def remove_item_from_inventory():
        # pull in the badge-locator tuple just once
        badge_locator = web_inventory_page.shopping_cart_badge

        # 1) find all the Remove buttons
        remove_buttons = conftest.driver.find_elements(By.XPATH, "//button[text()='Remove']")
        if not remove_buttons:
            logging.info("Cart is already empty – nothing to remove")
            # verify the badge is gone (or hidden)
            badges = conftest.driver.find_elements(*badge_locator)
            assert not badges or not badges[0].is_displayed(), \
                "Shopping cart badge still visible on empty cart"
            return

        # 2) click the first Remove
        initial_count = int(page_objects.web_inventory_page.get_shopping_cart_badge().text)
        UiActions.click(remove_buttons[0])

        # 3) wait for the badge to update to initial_count - 1
        expected = str(initial_count - 1)
        wait(
            ExpectedConditions.TEXT_TO_BE_PRESENT_IN_ELEMENT,
            badge_locator,
            expected
        )

        # 4) final assert
        Verifications.verify_object_comparison(
            expected,
            page_objects.web_inventory_page.get_shopping_cart_badge().text
        )
        logging.info("Item successfully removed from inventory page")

    @staticmethod
    @allure.step("Remove item from checkout page")
    def remove_item_from_checkout(item_name: str):
        # Build locator for the cart_item row by product name
        item_locator = (
            By.XPATH,
            f"//div[text()='{item_name}']/ancestor::div[@class='cart_item']"
        )
        # Wait until that item is visible
        wait(ExpectedConditions.ELEMENT_IS_VISIBLE, item_locator)

        # Find and click its “Remove” button
        remove_btn = conftest.driver.find_element(
            By.XPATH,
            f"//div[text()='{item_name}']/ancestor::div[@class='cart_item']//button[text()='Remove']"
        )
        UiActions.click(remove_btn)

        # Now wait until that cart_item container disappears
        try:
            wait(ExpectedConditions.ELEMENT_IS_INVISIBLE, item_locator)
            logging.info("Item '%s' removed successfully from checkout", item_name)
        except TimeoutException:
            logging.error("Failed to remove '%s' from checkout – still visible", item_name)
            # re-find the element (it must still be there) and assert it's not displayed
            elem = conftest.driver.find_element(*item_locator)
            Verifications.verify_object_comparison(False, elem.is_displayed())

    @staticmethod
    @allure.step("Empty the shopping cart")
    def empty_cart():
        """
        Removes every item from the inventory page cart badge
        until the badge disappears (cart is empty).
        """
        # locator tuple for the little badge
        badge_locator = web_inventory_page.shopping_cart_badge

        # keep removing the first “Remove” button until none remain
        while True:
            remove_buttons = conftest.driver.find_elements(By.XPATH, "//button[text()='Remove']")
            if not remove_buttons:
                break

            # click the first remove
            UiActions.click(remove_buttons[0])

            # wait for that button to go stale
            WebDriverWait(
                conftest.driver,
                int(get_configuration_data('WaitForElement'))
            ).until(EC.staleness_of(remove_buttons[0]))

        # finally, wait for the badge itself to vanish
        try:
            wait(ExpectedConditions.ELEMENT_IS_INVISIBLE, web_inventory_page.shopping_cart_badge)
            logging.info("Cart emptied successfully – badge is gone.")
        except TimeoutException:
            logging.error("Cart badge still visible after cleanup!")
            raise
