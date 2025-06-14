import allure
import pytest
from workflows.mobile_flows import MobileFlows, BugStatuses, BugSeverity, BugPriority


@pytest.mark.usefixtures('init_mobile_driver')
class TestEditBug:

    @allure.title("Open a new bug")
    @allure.description("Open a new bug so it can be edited")
    def test_open_a_new_bug_sanity(self):
        assert MobileFlows.open_a_new_bug_sanity(1, 10, "Login failed", "1. Open the login page."
                                                                        "2. Enter login credentials. 3. Click the login button.",
                                                 "Login is successful", "Login failed, error message is displayed",
                                                 "Dan Brown")

    @allure.title("Edit a bug")
    @allure.description("Edit the bug details")
    def test_edit_bug_details(self):
        assert MobileFlows.edit_bug("Login failed", 1, 14, "Web app crashes on login page", "1. Open the login page.",
                                    "Login page is displayed with login and password fields.",
                                    "Web app crashes, API returns 500.", BugStatuses.STATUS_NOT_REPRODUCED,
                                    BugSeverity.MAJOR, BugPriority.HIGH, "Voldemort", "Harry Potter", 16)

    @allure.title("Delete a bug")
    @allure.description("Delete the bug after editing")
    def test_delete_bug(self):
        assert MobileFlows.delete_a_bug("Web app crashes on login page", 1)
