import allure
import pytest
from workflows.mobile_flows import MobileFlows


@pytest.mark.usefixtures('init_mobile_driver')
class TestFilterBugList:

    @allure.title("Create bugs for all the statuses")
    @allure.description("Create a new bug for each status")
    def test_open_bugs_for_all_statuses(self):
        assert MobileFlows.open_a_new_bug_sanity(1, 10, "Status open", "Test status open",
                                                 "Bug is filtered correctly", "Bug is filtered correctly",
                                                 "Dan")
        assert MobileFlows.open_bug_status_fixed(2, 10, "Status fixed", "Test status fixed",
                                                 "Bug is filtered correctly", "Bug is filtered correctly",
                                                 "Ragnar")
        assert MobileFlows.open_bug_status_closed(3, 10, "Status closed", "Test status closed",
                                                  "Bug is filtered correctly", "Bug is filtered correctly",
                                                  "Bjorn")

        assert MobileFlows.open_bug_status_not_a_bug(4, 10, "Status not a bug", "Test status not a bug",
                                                     "Bug is filtered correctly", "Bug is filtered correctly",
                                                     "Ivar")

    @allure.title("Filter bug list by status 'Open'")
    @allure.description("Verify the bug list is filtered by status 'Open'")
    def test_filter_list_by_status_open(self):
        MobileFlows.filter_bugs_by_status("Open")

    @allure.title("Filter bug list by status 'Fixed'")
    @allure.description("Verify the bug list is filtered by status 'Fixed'")
    def test_filter_list_by_status_fixed(self):
        MobileFlows.filter_bugs_by_status("Fixed")

    @allure.title("Filter bug list by status 'Closed'")
    @allure.description("Verify the bug list is filtered by status 'Closed'")
    def test_filter_list_by_status_closed(self):
        MobileFlows.filter_bugs_by_status("Closed")

    @allure.title("Filter bug list by status 'Not a bug'")
    @allure.description("Verify the bug list is filtered by status 'Not a bug'")
    def test_filter_list_by_status_not_a_bug(self):
        MobileFlows.filter_bugs_by_status("Not a Bug")
