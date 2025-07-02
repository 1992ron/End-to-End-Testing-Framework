import allure
import pytest
import utilities.manage_pages as page_objects
from extensions.verifications import Verifications
from workflows.web_flows import WebFlows
import test_cases.conftest as conftest


@pytest.mark.usefixtures('init_web_driver')
class TestWebFunctionality:

    @allure.title("Login and logout")
    @allure.description("Verify that a user can log in and then log out successfully")
    def test_login_logout(self):
        # Log in with valid credentials
        WebFlows.submit_login_credentials(conftest.get_configuration_data("username"), conftest.get_configuration_data("password"))
        # Then log out
        WebFlows.logout()

    @allure.title("Add 2 items then remove one")
    @allure.description("Add two items to the cart, remove one via inventory page, and verify badge count")
    def test_add_two_and_remove_one_inventory(self):
        WebFlows.submit_login_credentials(conftest.get_configuration_data("username"), conftest.get_configuration_data("password"))

        # Add two distinct items
        WebFlows.add_backpack_to_cart()
        WebFlows.add_t_shirt_to_cart()

        # Remove one item and verify cart count decreased by 1
        WebFlows.remove_item_from_inventory()
        # Clean the cart before the next test
        WebFlows.empty_cart()
        WebFlows.logout()

    @allure.title("Add three items and verify cart count")
    @allure.description("Add three items to the cart and assert that the badge shows '3'")
    def test_add_three_and_verify_cart_count(self):
        WebFlows.submit_login_credentials(conftest.get_configuration_data("username"), conftest.get_configuration_data("password"))

        # Add three items
        WebFlows.add_backpack_to_cart()
        WebFlows.add_t_shirt_to_cart()
        WebFlows.add_bike_light_to_cart()

        # Verify the badge reads "3"
        badge_text = page_objects.web_inventory_page.get_shopping_cart_badge().text
        Verifications.verify_object_comparison("3", badge_text)
        # Clean the cart before the next test
        WebFlows.empty_cart()

        WebFlows.logout()

    @allure.title("Complete single item purchase flow")
    @allure.description("""
    1) Add one item  
    2) Go to cart → Checkout → Fill form → Continue → Finish  
    3) Verify final thank-you message  
    """)
    def test_complete_single_item_purchase_flow(self):
        WebFlows.submit_login_credentials(conftest.get_configuration_data("username"), conftest.get_configuration_data("password"))
        # Add single item
        WebFlows.add_backpack_to_cart()
        # Go through the checkout flow
        WebFlows.go_to_cart()
        WebFlows.proceed_to_checkout()
        WebFlows.fill_checkout_form("Alice", "Doe", "12345")
        WebFlows.continue_checkout()
        WebFlows.finish_checkout()
        WebFlows.logout()

    @allure.title("Remove item from checkout page")
    @allure.description("Add an item, navigate to checkout, remove it there and verify it’s gone")
    def test_remove_item_from_checkout(self):
        WebFlows.submit_login_credentials(conftest.get_configuration_data("username"), conftest.get_configuration_data("password"))
        # Add and navigate to checkout
        WebFlows.add_backpack_to_cart()
        WebFlows.go_to_cart()
        # Remove in checkout
        WebFlows.remove_item_from_checkout("Sauce Labs Backpack")
        WebFlows.logout()

    @allure.title("Attempt remove without items (Edge Case)")
    @allure.description("Calling remove on an empty cart should not error and should leave badge hidden")
    def test_remove_without_items_inventory(self):
        WebFlows.submit_login_credentials(conftest.get_configuration_data("username"), conftest.get_configuration_data("password"))

        # Cart is empty - attempt removal
        WebFlows.remove_item_from_inventory()

        badges = page_objects.web_inventory_page.get_shopping_cart_badges()
        assert len(badges) == 0, "Shopping cart badge still visible on empty cart"

        WebFlows.logout()
