from selenium.webdriver.common.by import By

view_bugs_screen_title = (By.XPATH, "//*[@text='Bug List']")
view_bugs_page = (By.ID, "viewBugsPage")
search_bugs_field = (By.ID, "searchinput")
show_all_bugs_filter = (By.XPATH, "//*[@text='All']")
show_fixed_bugs_filter = (By.XPATH, "//*[@text='Fixed']")
show_opened_bugs_filter = (By.XPATH, "//*[@text='Open']")
show_closed_bugs_filter = (By.XPATH, "//*[@text='Closed']")
show_not_a_bug_filter = (By.XPATH, "//*[@text='Not a Bug']")
bug_list_element = (By.ID, "bugList")


# This class contains all the elements of the view bugs screen of the Bug Tracker mobile app
class ViewBugsPage:

    def __init__(self, driver):
        self.driver = driver

    def get_view_bugs_screen_title(self):
        return self.driver.find_element(view_bugs_screen_title[0], view_bugs_screen_title[1])

    def get_view_bugs_page(self):
        return self.driver.find_element(view_bugs_page[0], view_bugs_page[1])

    def get_search_bugs_field(self):
        return self.driver.find_element(search_bugs_field[0], search_bugs_field[1])

    def get_show_all_bugs_filter(self):
        return self.driver.find_element(show_all_bugs_filter[0], show_all_bugs_filter[1])

    def get_show_opened_bugs_filter(self):
        return self.driver.find_element(show_opened_bugs_filter[0], show_opened_bugs_filter[1])

    def get_show_closed_bugs_filter(self):
        return self.driver.find_element(show_closed_bugs_filter[0], show_closed_bugs_filter[1])

    def get_show_not_a_bug_filter(self):
        return self.driver.find_element(show_not_a_bug_filter[0], show_not_a_bug_filter[1])

    def get_bug_list_element(self):
        return self.driver.find_element(bug_list_element[0], bug_list_element[1])
