from selenium.webdriver.common.by import By

home_button = (By.XPATH, "//*[@text='Home']")
create_bug_button = (By.XPATH, "//*[@text='Create Bug']")
view_bugs_button = (By.XPATH, "//*[@text='View Bugs']")
menu_title = (By.XPATH, "//*[@text='Bug Tracker']")


# This class contains all the elements of the navigation menu of the Bug Tracker mobile app
class MenuPage:

    def __init__(self, driver):
        self.driver = driver

    def get_home_button(self):
        return self.driver.find_element(home_button[0], home_button[1])

    def get_create_bug_button(self):
        return self.driver.find_element(create_bug_button[0], create_bug_button[1])

    def get_view_bugs_button(self):
        return self.driver.find_element(view_bugs_button[0], view_bugs_button[1])

    def get_menu_title(self):
        return self.driver.find_element(menu_title[0], menu_title[1])
