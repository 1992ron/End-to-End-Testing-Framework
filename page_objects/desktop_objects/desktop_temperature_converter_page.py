from selenium.webdriver.common.by import By

temperature_in_fahrenheit = (By.XPATH, "//*[@AutomationId='Value1']")
temperature_in_celsius = (By.XPATH, "//*[@AutomationId='Value2']")


# This clas contains the elements of the temperature converter type calculator
class TemperatureConverterPage:

    def __init__(self, driver):
        self.driver = driver

    def get_temperature_in_fahrenheit(self):
        return self.driver.find_element(temperature_in_fahrenheit[0], temperature_in_fahrenheit[1])

    def get_temperature_in_celsius(self):
        return self.driver.find_element(temperature_in_celsius[0], temperature_in_celsius[1])
