from selenium.webdriver.common.by import By

create_task = (By.XPATH, "//input[@placeholder='Create a task']")
delete_task_buttons = (By.XPATH, "//div[@class='view_2Ow90']/*[name()='svg']")
all_tasks_completed_button = (By.CLASS_NAME, "allCompletedWrapper_wdM4q")
visibility_panel = (By.XPATH, "//div[contains(@class, 'toggleVisibilityPanel_hNPyc')]")
filter_all_tasks = (By.XPATH, "/html/body//div[3]/button[1]")
filter_todo_tasks = (By.XPATH, "/html/body//div[3]/button[2]")
filter_completed_tasks = (By.XPATH, "/html/body//div[3]/button[3]")
task_labels = (By.CSS_SELECTOR, "[class^='label_']")
color_picker = (By.XPATH, "//div[@class='topWrapper_2caNE']")
mark_task_in_red = (By.XPATH, "/html/body//div/div[2]/span[2]")
red_filter = (By.XPATH, "/html/body//div[2]//div[1]/span[2]")
mark_task_in_orange = (By.XPATH, "/html/body//div/div[2]/span[3]")
orange_filter = (By.XPATH, "/html/body//div[2]//div[1]/span[3]")
mark_task_in_yellow = (By.XPATH, "/html/body//div/div[2]/span[4]")
yellow_filter = (By.XPATH, "/html/body//div[2]//div[1]/span[4]")
display_all_colors_filter = (By.CLASS_NAME, "tag_21fhY hasNoTag_3ftX1")


# This class contains the elements from the main screen of the To_do List app
class TaskPage:
    def __init__(self, driver):
        self.driver = driver

    def get_create_task(self):
        return self.driver.find_element(create_task[0], create_task[1])

    def get_delete_task_buttons(self):
        return self.driver.find_elements(delete_task_buttons[0], delete_task_buttons[1])

    def get_all_tasks_completed_button(self):
        return self.driver.find_element(all_tasks_completed_button[0], all_tasks_completed_button[1])

    def get_visibility_panel(self):
        return self.driver.find_element(visibility_panel[0], visibility_panel[1])

    def get_filter_all_tasks(self):
        return self.driver.find_element(filter_all_tasks[0], filter_all_tasks[1])

    def get_filter_todo_tasks(self):
        return self.driver.find_element(filter_todo_tasks[0], filter_todo_tasks[1])

    def get_filter_completed_tasks(self):
        return self.driver.find_element(filter_completed_tasks[0], filter_completed_tasks[1])

    def get_task_labels(self):
        return self.driver.find_elements(task_labels[0], task_labels[1])

    def get_color_picker(self):
        return self.driver.find_element(color_picker[0], color_picker[1])

    def get_mark_task_in_red(self):
        return self.driver.find_element(mark_task_in_red[0], mark_task_in_red[1])

    def get_red_filter(self):
        return self.driver.find_element(red_filter[0], red_filter[1])

    def get_orange_filter(self):
        return self.driver.find_element(orange_filter[0], orange_filter[1])

    def get_mark_task_in_orange(self):
        return self.driver.find_element(mark_task_in_orange[0], mark_task_in_orange[1])

    def get_mark_task_in_yellow(self):
        return self.driver.find_element(mark_task_in_yellow[0], mark_task_in_yellow[1])

    def get_yellow_filter(self):
        return self.driver.find_element(yellow_filter[0], yellow_filter[1])

    def get_display_all_colors_filter(self):
        self.driver.find_element(display_all_colors_filter[0], display_all_colors_filter[1])




