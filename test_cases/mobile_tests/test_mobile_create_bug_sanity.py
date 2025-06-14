import allure
import pytest
from workflows.mobile_flows import MobileFlows


@pytest.mark.usefixtures('init_mobile_driver')
class TestCreateBugSanity:

    @allure.title("Create a new bug - Sanity test")
    @allure.description("This is a sanity test for the create new bug feature")
    def test_open_a_new_bug_sanity(self):
        assert MobileFlows.open_a_new_bug_sanity(1, 10, "Login failed", "1. Open the login page."
                                                                        "2. Enter login credentials. 3. Click the login button.",
                                                 "Login is successful", "Login failed, error message is displayed",
                                                 "Dan Brown")

    @allure.title("Delete a bug")
    @allure.description("This test is to verify the delete bug feature")
    def test_delete_bug(self):
        assert MobileFlows.delete_a_bug("Login failed", 1)
