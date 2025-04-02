from selenium.webdriver.common.by import By

welcome_text_header = (By.XPATH, "//*[@text='Welcome to Bug Tracker Tool']")


# This class contains all the elements of the home screen of the Bug Tracker mobile app
class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def get_welcome_text_header(self):
        return self.driver.find_element(welcome_text_header[0], welcome_text_header[1])

    def get_home_screen_image(self):
        return self.driver.find_element(By.XPATH, "//*[@text='Bug Tracker Image']")
