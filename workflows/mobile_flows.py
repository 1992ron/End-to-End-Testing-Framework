import logging
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
import allure
import utilities.manage_pages as page_objects
from extensions.mobile_actions import MobileActions
from extensions.verifications import Verifications
import test_cases.conftest as conftest
from utilities.common_ops import wait, ExpectedConditions
import page_objects.mobile_objects.mobile_create_bug_page as create_bug
import page_objects.mobile_objects.mobile_view_bugs_page as view_bugs
import page_objects.mobile_objects.mobile_edit_bug_page as edit_bug
from enum import Enum


# Enum class for choosing a status of a bug
class BugStatuses(Enum):
    STATUS_OPEN = "Open"
    STATUS_FIXED = "Fixed"
    STATUS_CLOSED = "Closed"
    STATUS_NOT_A_BUG = "Not a Bug"
    STATUS_NOT_REPRODUCED = "Not Reproduced"


# Enum class for choosing the severity of a bug
class BugSeverity(Enum):
    CRITICAL = "Critical"
    MAJOR = "Major"
    MINOR = "Minor"
    TRIVIAL = "Trivial"
    ENHANCEMENT = "Enhancement"


# Enum class for choosing the priority of a bug
class BugPriority(Enum):
    CRITICAL = "Critical"
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"
    DEFERRED = "Deferred"


class MobileFlows:
    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    @staticmethod
    @allure.step("Open a new bug sanity")
    def open_a_new_bug_sanity(bug_id, day_open: int, bug_title: str, steps: str, expected_result: str,
                              actual_result: str, detected_by: str):
        # Tap the create bug button from the menu
        MobileActions.tap(page_objects.mobile_menu_page.get_create_bug_button(), 1)
        # Fill only the mandatory fields
        MobileActions.update_text(page_objects.mobile_create_bug_page.get_bug_id_field(), bug_id)
        MobileFlows.choose_a_date(day_open)
        MobileActions.update_text(page_objects.mobile_create_bug_page.get_bug_title_field(), bug_title)
        MobileActions.update_text(page_objects.mobile_create_bug_page.get_bug_steps_field(), steps)
        MobileActions.update_text(page_objects.mobile_create_bug_page.get_expected_result_field(), expected_result)
        MobileActions.update_text(page_objects.mobile_create_bug_page.get_actual_result_field(), actual_result)
        MobileActions.scroll_by_coordinates(conftest.driver, 129, 1905, 129, 1002, 500)
        MobileActions.update_text(page_objects.mobile_create_bug_page.get_bug_detected_by_field(), detected_by)

        # Tap the add bug button
        MobileActions.tap(page_objects.mobile_create_bug_page.get_add_bug_button(), 1)
        # Wait until the bug created successfully message is displayed
        wait(ExpectedConditions.ELEMENT_IS_VISIBLE, create_bug.bug_open_successfully_message)
        # If the message is displayed verify the bug is listed in the view bugs screen
        if page_objects.mobile_create_bug_page.get_bug_open_successfully_message().is_displayed:
            MobileActions.scroll_by_coordinates(conftest.driver, 129, 396, 129, 15665, 500)
            MobileActions.tap(page_objects.mobile_menu_page.get_view_bugs_button(), 1)
            if conftest.driver.find_element(By.XPATH, f"//*[@text='{bug_title} (ID: {bug_id})']").is_displayed:
                logging.info("The bug was created successfully and appears in the view bugs screen")
                return True
            else:
                logging.info("The bug is not displayed in the view bugs screen, the bug was not created")
                return False

    @staticmethod
    @allure.step("Open a new bug sanity")
    def open_bug_status_fixed(bug_id, day_open: int, bug_title: str, steps: str, expected_result: str,
                              actual_result: str, detected_by: str):
        # Tap the create bug button from the menu
        MobileActions.tap(page_objects.mobile_menu_page.get_create_bug_button(), 1)
        # Fill only the mandatory fields
        MobileActions.update_text(page_objects.mobile_create_bug_page.get_bug_id_field(), bug_id)
        MobileFlows.choose_a_date(day_open)
        MobileActions.update_text(page_objects.mobile_create_bug_page.get_bug_title_field(), bug_title)
        MobileActions.update_text(page_objects.mobile_create_bug_page.get_bug_steps_field(), steps)
        MobileActions.update_text(page_objects.mobile_create_bug_page.get_expected_result_field(), expected_result)
        MobileActions.update_text(page_objects.mobile_create_bug_page.get_actual_result_field(), actual_result)
        MobileActions.tap(page_objects.mobile_create_bug_page.get_bug_status_field(), 1)
        MobileActions.tap(MobileFlows.choose_bug_status(BugStatuses.STATUS_FIXED), 1)
        MobileActions.scroll_by_coordinates(conftest.driver, 129, 1905, 129, 1002, 500)
        MobileActions.update_text(page_objects.mobile_create_bug_page.get_bug_detected_by_field(), detected_by)

        # Tap the add bug button
        MobileActions.tap(page_objects.mobile_create_bug_page.get_add_bug_button(), 1)
        # Wait until the bug created successfully message is displayed
        wait(ExpectedConditions.ELEMENT_IS_VISIBLE, create_bug.bug_open_successfully_message)
        # If the message is displayed verify the bug is listed in the view bugs screen
        if page_objects.mobile_create_bug_page.get_bug_open_successfully_message().is_displayed:
            MobileActions.scroll_by_coordinates(conftest.driver, 129, 396, 129, 15665, 500)
            MobileActions.tap(page_objects.mobile_menu_page.get_view_bugs_button(), 1)
            if conftest.driver.find_element(By.XPATH, f"//*[@text='{bug_title} (ID: {bug_id})']").is_displayed:
                logging.info("The bug was created successfully and appears in the view bugs screen")
                return True
            else:
                logging.info("The bug is not displayed in the view bugs screen, the bug was not created")
                return False

    @staticmethod
    @allure.step("Open a new bug sanity")
    def open_bug_status_closed(bug_id, day_open: int, bug_title: str, steps: str, expected_result: str,
                               actual_result: str, detected_by: str):
        # Tap the create bug button from the menu
        MobileActions.tap(page_objects.mobile_menu_page.get_create_bug_button(), 1)
        # Fill only the mandatory fields
        MobileActions.update_text(page_objects.mobile_create_bug_page.get_bug_id_field(), bug_id)
        MobileFlows.choose_a_date(day_open)
        MobileActions.update_text(page_objects.mobile_create_bug_page.get_bug_title_field(), bug_title)
        MobileActions.update_text(page_objects.mobile_create_bug_page.get_bug_steps_field(), steps)
        MobileActions.update_text(page_objects.mobile_create_bug_page.get_expected_result_field(), expected_result)
        MobileActions.update_text(page_objects.mobile_create_bug_page.get_actual_result_field(), actual_result)
        MobileActions.tap(page_objects.mobile_create_bug_page.get_bug_status_field(), 1)
        MobileActions.tap(MobileFlows.choose_bug_status(BugStatuses.STATUS_CLOSED), 1)
        MobileActions.scroll_by_coordinates(conftest.driver, 129, 1905, 129, 1002, 500)
        MobileActions.update_text(page_objects.mobile_create_bug_page.get_bug_detected_by_field(), detected_by)

        # Tap the add bug button
        MobileActions.tap(page_objects.mobile_create_bug_page.get_add_bug_button(), 1)
        # Wait until the bug created successfully message is displayed
        wait(ExpectedConditions.ELEMENT_IS_VISIBLE, create_bug.bug_open_successfully_message)
        # If the message is displayed verify the bug is listed in the view bugs screen
        if page_objects.mobile_create_bug_page.get_bug_open_successfully_message().is_displayed:
            MobileActions.scroll_by_coordinates(conftest.driver, 129, 396, 129, 15665, 500)
            MobileActions.tap(page_objects.mobile_menu_page.get_view_bugs_button(), 1)
            if conftest.driver.find_element(By.XPATH, f"//*[@text='{bug_title} (ID: {bug_id})']").is_displayed:
                logging.info("The bug was created successfully and appears in the view bugs screen")
                return True
            else:
                logging.info("The bug is not displayed in the view bugs screen, the bug was not created")
                return False

    @staticmethod
    @allure.step("Open a new bug sanity")
    def open_bug_status_not_a_bug(bug_id, day_open: int, bug_title: str, steps: str, expected_result: str,
                                  actual_result: str, detected_by: str):
        # Tap the create bug button from the menu
        MobileActions.tap(page_objects.mobile_menu_page.get_create_bug_button(), 1)
        # Fill only the mandatory fields
        MobileActions.update_text(page_objects.mobile_create_bug_page.get_bug_id_field(), bug_id)
        MobileFlows.choose_a_date(day_open)
        MobileActions.update_text(page_objects.mobile_create_bug_page.get_bug_title_field(), bug_title)
        MobileActions.update_text(page_objects.mobile_create_bug_page.get_bug_steps_field(), steps)
        MobileActions.update_text(page_objects.mobile_create_bug_page.get_expected_result_field(), expected_result)
        MobileActions.update_text(page_objects.mobile_create_bug_page.get_actual_result_field(), actual_result)
        MobileActions.tap(page_objects.mobile_create_bug_page.get_bug_status_field(), 1)
        MobileActions.tap(MobileFlows.choose_bug_status(BugStatuses.STATUS_NOT_A_BUG), 1)
        MobileActions.scroll_by_coordinates(conftest.driver, 129, 1905, 129, 1002, 500)
        MobileActions.update_text(page_objects.mobile_create_bug_page.get_bug_detected_by_field(), detected_by)

        # Tap the add bug button
        MobileActions.tap(page_objects.mobile_create_bug_page.get_add_bug_button(), 1)
        # Wait until the bug created successfully message is displayed
        wait(ExpectedConditions.ELEMENT_IS_VISIBLE, create_bug.bug_open_successfully_message)
        # If the message is displayed verify the bug is listed in the view bugs screen
        if page_objects.mobile_create_bug_page.get_bug_open_successfully_message().is_displayed:
            MobileActions.scroll_by_coordinates(conftest.driver, 129, 396, 129, 15665, 500)
            MobileActions.tap(page_objects.mobile_menu_page.get_view_bugs_button(), 1)
            MobileActions.scroll_by_coordinates(conftest.driver, 543, 1680, 120, 615, 500)
            if conftest.driver.find_element(By.XPATH, f"//*[@text='{bug_title} (ID: {bug_id})']").is_displayed:
                logging.info("The bug was created successfully and appears in the view bugs screen")
                return True
            else:
                logging.info("The bug is not displayed in the view bugs screen, the bug was not created")
                return False

    @staticmethod
    @allure.step("Filter the bugs list")
    def filter_bugs_by_status(expected_status: str):
        """
        Test that filtering bugs by status correctly updates the displayed bug list.
        param expected_status: The status to filter by (e.g. "open", "fixed", "closed")
        """

        # Locate the bug list container (ensures we only look inside this section)
        bug_list_container = page_objects.mobile_view_bugs_page.get_bug_list_element()

        # Find and click the filter button corresponding to the expected status
        filter_button_xpath = f"//android.widget.Button[@text='{expected_status}']"
        filter_button = conftest.driver.find_element(By.XPATH, filter_button_xpath)
        MobileActions.tap(filter_button, 1)

        # Wait for the filtered results to load
        wait(ExpectedConditions.ELEMENT_IS_PRESENT, view_bugs.bug_list_element)

        # Get all bug titles in the list
        bug_titles = bug_list_container.find_elements(By.CLASS_NAME, "android.widget.TextView")

        # Log a message if no bugs are found, but don't fail the test because it is a normal scenario
        if not bug_titles:
            logging.info(f"No bugs found for status '{expected_status}', but this is valid.")

        # Verify that all displayed bugs match the expected status
        for title in bug_titles:
            if expected_status.lower() not in title.text.lower():
                logging.error(f"Bug with unexpected status found: {title.text}")
                return False  # Fail the test if an unexpected bug is found

        # If all bugs match the expected status, return success
        logging.info(f"Filter function is working correctly for status '{expected_status}'.")
        return True

    @staticmethod
    @allure.step("Edit bug details")
    def edit_bug(bug_name: str, bug_id, day_open: int, bug_title, steps: str, expected_result: str,
                 actual_result: str, bug_status: BugStatuses,
                 bug_severity: BugSeverity, bug_priority: BugPriority, detected_by: str, fixed_by: str,
                 day_closed: int):

        edit_button = MobileFlows.get_bug_button(bug_name, bug_id, "Edit")
        # Tap the edit button
        MobileActions.tap(edit_button, 1)
        # Wait until the edit screen is displayed
        wait(ExpectedConditions.ELEMENT_IS_CLICKABLE, edit_bug.edit_bug_date_field)
        MobileFlows.edit_date_open_field(day_open)
        MobileActions.update_text(page_objects.mobile_edit_bug_page.get_edit_bug_title_field(), bug_title)
        MobileActions.update_text(page_objects.mobile_edit_bug_page.get_edit_bug_steps_field(), steps)
        MobileActions.update_text(page_objects.mobile_edit_bug_page.get_edit_expected_result_field(), expected_result)
        MobileActions.update_text(page_objects.mobile_edit_bug_page.get_edit_actual_result_field(), actual_result)
        # Edit the dropdown fields
        MobileActions.tap(page_objects.mobile_edit_bug_page.get_edit_bug_status_field(), 1)
        MobileActions.tap(MobileFlows.choose_bug_status(bug_status), 1)
        MobileActions.tap(page_objects.mobile_edit_bug_page.get_edit_bug_severity_field(), 1)
        MobileActions.tap(MobileFlows.choose_bug_severity(bug_severity), 1)
        MobileActions.tap(page_objects.mobile_edit_bug_page.get_edit_bug_priority_field(), 1)
        MobileActions.tap(MobileFlows.choose_bug_priority(bug_priority), 1)
        # Scroll the screen to view the last fields
        MobileActions.scroll_by_coordinates(conftest.driver, 129, 1905, 129, 1002, 500)
        MobileActions.update_text(page_objects.mobile_edit_bug_page.get_edit_bug_detected_by_field(), detected_by)
        MobileActions.update_text(page_objects.mobile_edit_bug_page.get_edit_bug_fixed_by_field(), fixed_by)
        MobileFlows.edit_date_closed_field(day_closed)
        logging.info("Finished editing")
        # Save the changes after editing
        MobileActions.tap(page_objects.mobile_edit_bug_page.get_save_changes_button(), 1)
        wait(ExpectedConditions.ELEMENT_IS_VISIBLE, view_bugs.view_bugs_page)
        # Verify the new bug title is displayed after editing
        if conftest.driver.find_element(By.XPATH, f"//*[@text='{bug_title} (ID: {bug_id})']").is_displayed:
            logging.info("The new bug title is displayed, the bug was edited successfully")
            return True
        else:
            logging.info("The new bug title is not displayed, the bug was not edited")
            return False

    @staticmethod
    @allure.step("Delete a bug")
    def delete_a_bug(bug_title: str, bug_id: int):
        # Tap the delete button
        delete_button = MobileFlows.get_bug_button(bug_title, bug_id, "Delete")
        MobileActions.tap(delete_button, 1)

        # Wait for the bug to disappear from the screen
        try:
            wait(ExpectedConditions.ELEMENT_IS_INVISIBLE, (By.XPATH, f"//*[@text='{bug_title} (ID: {bug_id})']"))
            logging.info("The bug is deleted and does not appear in the view bugs screen")
            return True
        except TimeoutException:
            logging.info("The bug is not deleted and still appears in the view bugs screen")
            return False

    @staticmethod
    @allure.step("Choose a date")
    def choose_a_date(day: int):
        # Validate the input day
        if day < 1 or day > 31:
            raise ValueError("Day must be between 1 and 31")

        # Tap on the date field
        MobileActions.tap(page_objects.mobile_create_bug_page.get_bug_date_field(), 1)
        # Wait for the date picker to appear
        wait(ExpectedConditions.ELEMENT_IS_PRESENT, create_bug.date_picker_window)
        # Tap on the selected day
        MobileActions.tap(page_objects.mobile_create_bug_page.get_day_of_month(day), 1)
        # Confirm the selection
        MobileActions.tap(page_objects.mobile_create_bug_page.get_set_date_button(), 1)
        # Wait for the date picker to disappear
        wait(ExpectedConditions.ELEMENT_IS_INVISIBLE, create_bug.date_picker_window)

    @staticmethod
    @allure.step("Edit the date field")
    def edit_date_open_field(day: int):
        # Validate the input day
        if day < 1 or day > 31:
            raise ValueError("Day must be between 1 and 31")

        # Tap on the date field
        MobileActions.tap(page_objects.mobile_edit_bug_page.get_edit_bug_date_field(), 1)
        # Wait for the date picker to appear
        wait(ExpectedConditions.ELEMENT_IS_CLICKABLE, (By.XPATH, f"//*[@text='{day}']"))
        # Tap on the selected day
        MobileActions.tap(page_objects.mobile_create_bug_page.get_day_of_month(day), 1)
        # Confirm the selection
        MobileActions.tap(page_objects.mobile_create_bug_page.get_set_date_button(), 1)
        # Wait for the date picker to disappear
        wait(ExpectedConditions.ELEMENT_IS_INVISIBLE, create_bug.date_picker_window)

    @staticmethod
    @allure.step("Edit the date field")
    def edit_date_closed_field(day: int):
        # Validate the input day
        if day < 1 or day > 31:
            raise ValueError("Day must be between 1 and 31")

        # Tap on the date field
        MobileActions.tap(page_objects.mobile_edit_bug_page.get_edit_bug_date_closed_field(), 1)
        # Wait for the date picker to appear
        wait(ExpectedConditions.ELEMENT_IS_PRESENT, create_bug.date_picker_window)
        # Tap on the selected day
        MobileActions.tap(page_objects.mobile_create_bug_page.get_day_of_month(day), 1)
        # Confirm the selection
        MobileActions.tap(page_objects.mobile_create_bug_page.get_set_date_button(), 1)
        # Wait for the date picker to disappear
        wait(ExpectedConditions.ELEMENT_IS_INVISIBLE, create_bug.date_picker_window)

    @staticmethod
    @allure.step("Choose bug status")
    def choose_bug_status(bug_status: BugStatuses):
        return MobileFlows._choose_option_from_list(bug_status.value)

    @staticmethod
    @allure.step("Choose bug severity")
    def choose_bug_severity(bug_severity: BugSeverity):
        return MobileFlows._choose_option_from_list(bug_severity.value)

    @staticmethod
    @allure.step("Choose bug priority")
    def choose_bug_priority(bug_priority: BugPriority):
        return MobileFlows._choose_option_from_list(bug_priority.value)

    @staticmethod
    def _choose_option_from_list(str_option: str):
        """Dynamic private method that passes one of the enum options value to the xpath, so it can locate the desired
           option from the list of the status/severity/priority field when creating/editing a bug
        """
        option_from_list = conftest.driver.find_element(By.XPATH, f"//*[@text='{str_option}']")
        wait(ExpectedConditions.ELEMENT_IS_CLICKABLE, (By.XPATH, f"//*[@text='{str_option}']"))
        MobileActions.tap(option_from_list, 1)

    @staticmethod
    def get_bug_button(bug_title: str, bug_id: int, button_type: str):
        """
        Locates the 'Edit' or 'Delete' button for a specific bug dynamically.

        :param bug_title: The title of the bug.
        :param bug_id: The ID of the bug.
        :param button_type: 'Edit' or 'Delete'.
        :return: The mobile element of the button.
        """
        # Construct the dynamic XPath
        button_xpath = f"//*[@text='{bug_title} (ID: {bug_id})']/..//*[contains(@text, '{button_type}')]"

        # Locate and return the button element
        return conftest.driver.find_element(By.XPATH, button_xpath)

    @staticmethod
    def switch_to_create_bug_screen():
        MobileActions.tap(page_objects.mobile_menu_page.get_create_bug_button(), 1)
        expected_screen_title = page_objects.mobile_create_bug_page.get_create_bug_screen_title().text
        actual_screen_title = "Create a Bug"

        # Verify that the expected screen title matches the current screen
        Verifications.verify_object_comparison(expected_screen_title, actual_screen_title)
        logging.info("Screen title is: " + expected_screen_title + " as expected for the create bug screen")

    @staticmethod
    def switch_to_view_bugs_screen():
        MobileActions.tap(page_objects.mobile_menu_page.get_view_bugs_button(), 1)
        expected_screen_title = page_objects.mobile_view_bugs_page.get_view_bugs_screen_title().text
        actual_screen_title = "Bug List"

        # Verify that the expected screen title matches the current screen
        Verifications.verify_object_comparison(expected_screen_title, actual_screen_title)
        logging.info("Screen title is: " + expected_screen_title + " as expected for the view bug screen")

    @staticmethod
    def switch_to_home_screen():
        MobileActions.tap(page_objects.mobile_menu_page.get_home_button(), 1)
        expected_screen_title = page_objects.mobile_home_page.get_welcome_text_header().text
        actual_screen_title = "Welcome to Bug Tracker Tool"

        # Verify that the expected screen title matches the current screen
        Verifications.verify_object_comparison(expected_screen_title, actual_screen_title)
        logging.info("Screen title is: " + expected_screen_title + " as expected for the home screen")
        Verifications.element_is_displayed(page_objects.mobile_home_page.get_home_screen_image())
        logging.info("The bug tracker image is displayed as expected")
