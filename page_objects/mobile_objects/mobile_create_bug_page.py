from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

bug_id_field = (By.ID, "bugId")
bug_date_field = (By.ID, "bugDate")
bug_title_field = (By.ID, "bugTitle")
bug_steps_field = (By.ID, "bugSteps")
expected_result_field = (By.ID, "bugExpectedResult")
actual_result_field = (By.ID, "bugActualResult")
create_bug_screen_title = (By.XPATH, "//*[@text='Create a Bug']")
bug_status_field = (By.ID, "bugStatus")
bug_severity_field = (By.ID, "bugSeverity")
bug_priority_field = (By.ID, "bugPriority")
bug_detected_by_field = (By.ID, "bugDetectedBy")
attach_file_button = (By.ID, "bugFile")
add_bug_button = (By.XPATH, "//*[@text='Add Bug']")
bug_date_closed_field = (By.ID, "bugDateClosed")
bug_fixed_by_field = (By.ID, "bugFixedBy")
set_date_button = (By.XPATH, "//*[@text='SET']")
cancel_date_button = (By.XPATH, "//*[@text='CANCEL']")
clear_date_button = (By.XPATH, "//*[@text='CLEAR']")
date_picker_window = (By.ID, 'month_view')
bug_open_successfully_message = (By.ID, 'statusMessage')
create_bug_page = (By.ID, "createBugPage")


# This class contains all the elements of the create bug screen of the Bug Tracker mobile app
class CreateBugPage:

    def __init__(self, driver):
        self.driver = driver

    def get_bug_id_field(self):
        return self.driver.find_element(bug_id_field[0], bug_id_field[1])

    def get_bug_date_field(self):
        return self.driver.find_element(bug_date_field[0], bug_date_field[1])

    def get_bug_title_field(self):
        return self.driver.find_element(bug_title_field[0], bug_title_field[1])

    def get_bug_steps_field(self):
        return self.driver.find_element(bug_steps_field[0], bug_steps_field[1])

    def get_expected_result_field(self):
        return self.driver.find_element(expected_result_field[0], expected_result_field[1])

    def get_actual_result_field(self):
        return self.driver.find_element(actual_result_field[0], actual_result_field[1])

    def get_create_bug_screen_title(self):
        return self.driver.find_element(create_bug_screen_title[0], create_bug_screen_title[1])

    def get_bug_status_field(self):
        return self.driver.find_element(bug_status_field[0], bug_status_field[1])

    def get_bug_severity_field(self):
        return self.driver.find_element(bug_severity_field[0], bug_severity_field[1])

    def get_bug_priority_field(self):
        return self.driver.find_element(bug_priority_field[0], bug_priority_field[1])

    def get_bug_date_closed_field(self):
        return self.driver.find_element(bug_date_closed_field[0], bug_date_closed_field[1])

    def get_bug_detected_by_field(self):
        return self.driver.find_element(bug_detected_by_field[0], bug_detected_by_field[1])

    def get_bug_fixed_by_field(self):
        return self.driver.find_element(bug_fixed_by_field[0], bug_fixed_by_field[1])

    def get_attach_file_button(self):
        self.driver.find_element(attach_file_button[0], attach_file_button[1])

    def get_add_bug_button(self):
        return self.driver.find_element(add_bug_button[0], add_bug_button[1])

    def get_set_date_button(self):
        return self.driver.find_element(set_date_button[0], set_date_button[1])

    def get_cancel_date_button(self):
        return self.driver.find_element(cancel_date_button[0], cancel_date_button[1])

    def get_clear_date_button(self):
        return self.driver.find_element(clear_date_button[0], clear_date_button[1])

    def get_date_picker_window(self):
        return self.driver.find_element(date_picker_window[0], date_picker_window[1])

    def get_bug_open_successfully_message(self):
        return self.driver.find_element(bug_open_successfully_message[0], bug_open_successfully_message[1])

    def get_day_of_month(self, day: int):
        try:
            return self.driver.find_element(By.XPATH, f"//*[@text='{day}']")
        except NoSuchElementException:
            raise Exception(f"Day '{day}' not found in the date picker.")

    def get_create_bug_page(self):
        return self.driver.find_element(create_bug_page[0], create_bug_page[1])


