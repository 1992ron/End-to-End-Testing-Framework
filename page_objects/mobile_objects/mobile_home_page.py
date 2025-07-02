from selenium.webdriver.common.by import By

welcome_text_header = (By.XPATH, "//*[@text='Welcome to Bug Tracker Tool']")
home_screen_image = (By.XPATH, "//*[@text='bug-tracker']")

# This class contains all the elements of the home screen of the Bug Tracker mobile app
class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def get_welcome_text_header(self):
        return self.driver.find_element(welcome_text_header[0], welcome_text_header[1])

    def get_home_screen_image(self):
        return self.driver.find_element(home_screen_image[0], home_screen_image[1])
