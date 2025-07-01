import allure
import pytest
from extensions.ui_actions import UiActions
from extensions.verifications import Verifications
import utilities.manage_pages as page_objects
from workflows.web_flows import WebFlows


@pytest.mark.usefixtures("init_web_driver")
class TestErrorHandling:

    # Error handling for the login page
    @allure.title("Invalid login")
    @allure.description("Verifies the correct error messages are displayed on invalid login attempts")
    def test_invalid_login(self):
        # Login without a username
        WebFlows.login_without_username()
        # Login without a password
        WebFlows.login_without_password()
        # Login with a locked out user
        WebFlows.login_locked_out_user()

    # Error handling for the checkout page
    @allure.title("Invalid checkout")
    @allure.description("Verifies the correct error messages are displayed on invalid checkout attempts")
    def test_checkout_form_errors(self):
        # Login first
        WebFlows.submit_login_credentials("standard_user", "secret_sauce")
        # Go to cart → checkout step
        WebFlows.go_to_cart()
        # Proceed to the checkout page
        UiActions.click(page_objects.web_cart_page.get_checkout_button())
        # Attempt to check out without first name
        WebFlows.checkout_without_first_name()
        # Attempt to check out without last name
        WebFlows.checkout_without_last_name()
        # Attempt to check out without postal code
        WebFlows.checkout_without_postal_code()
        WebFlows.logout()
