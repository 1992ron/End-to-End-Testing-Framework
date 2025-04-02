from selenium.webdriver.common.by import By

edit_bug_date_field = (By.ID, "editBugDate")
edit_bug_title_field = (By.ID, "editBugTitle")
edit_bug_steps_field = (By.ID, "editBugSteps")
edit_expected_result_field = (By.ID, "editBugExpectedResult")
edit_actual_result_field = (By.ID, "editBugActualResult")
edit_bug_status_field = (By.ID, "editBugStatus")
edit_bug_severity_field = (By.ID, "editBugSeverity")
edit_bug_priority_field = (By.ID, "editBugPriority")
edit_bug_detected_by_field = (By.ID, "editBugDetectedBy")
edit_bug_fixed_by_field = (By.ID, "editBugFixedBy")
edit_bug_date_closed_field = (By.ID, "editBugDateClosed")
save_changes_button = (By.XPATH, "//*[@text='Save Changes' and @class='android.widget.Button']")
cancel_editing_button = (By.XPATH, "//*[@text='Cancel Editing' and @class='android.widget.Button']")
edit_bug_page = (By.ID, "editBugPage")


# This class contains all the elements of the edit bug screen of the Bug Tracker mobile app
class EditBugPage:

    def __init__(self, driver):
        self.driver = driver

    def get_edit_bug_date_field(self):
        return self.driver.find_element(edit_bug_date_field[0], edit_bug_date_field[1])

    def get_edit_bug_title_field(self):
        return self.driver.find_element(edit_bug_title_field[0], edit_bug_title_field[1])

    def get_edit_bug_steps_field(self):
        return self.driver.find_element(edit_bug_steps_field[0], edit_bug_steps_field[1])

    def get_edit_expected_result_field(self):
        return self.driver.find_element(edit_expected_result_field[0], edit_expected_result_field[1])

    def get_edit_actual_result_field(self):
        return self.driver.find_element(edit_actual_result_field[0], edit_actual_result_field[1])

    def get_edit_bug_status_field(self):
        return self.driver.find_element(edit_bug_status_field[0], edit_bug_status_field[1])

    def get_edit_bug_severity_field(self):
        return self.driver.find_element(edit_bug_severity_field[0], edit_bug_severity_field[1])

    def get_edit_bug_priority_field(self):
        return self.driver.find_element(edit_bug_priority_field[0], edit_bug_priority_field[1])

    def get_edit_bug_detected_by_field(self):
        return self.driver.find_element(edit_bug_detected_by_field[0], edit_bug_detected_by_field[1])

    def get_edit_bug_fixed_by_field(self):
        return self.driver.find_element(edit_bug_fixed_by_field[0], edit_bug_fixed_by_field[1])

    def get_edit_bug_date_closed_field(self):
        return self.driver.find_element(edit_bug_date_closed_field[0], edit_bug_date_closed_field[1])

    def get_save_changes_button(self):
        return self.driver.find_element(save_changes_button[0], save_changes_button[1])

    def get_cancel_editing_button(self):
        return self.driver.find_element(cancel_editing_button[0], cancel_editing_button[1])

    def get_edit_bug_page(self):
        return self.driver.find_element(edit_bug_page[0], edit_bug_page[1])
