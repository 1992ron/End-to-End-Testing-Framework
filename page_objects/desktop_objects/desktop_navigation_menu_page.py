from selenium.webdriver.common.by import By

standard_calculator = (By.NAME, "Standard Calculator")
scientific_calculator = (By.NAME, "Scientific Calculator")
graphing_calculator = (By.NAME, "Graphing Calculator")
programmer_calculator = (By.NAME, "Programmer Calculator")
date_calculation_calculator = (By.NAME, "Date calculation Calculator")
temperature_converter = (By.XPATH, "//*[@AutomationId='Temperature']")


# This class contains the elements of the navigation menu in the calculator app
class NavigationMenuPage:

    def __init__(self, driver):
        self.driver = driver

    def get_standard_calculator(self):
        return self.driver.find_element(standard_calculator[0], standard_calculator[1])

    def get_scientific_calculator(self):
        return self.driver.find_element(scientific_calculator[0], scientific_calculator[1])

    def get_programmer_calculator(self):
        return self.driver.find_element(programmer_calculator[0], programmer_calculator[1])

    def get_graphing_calculator(self):
        return self.driver.find_element(graphing_calculator[0], graphing_calculator[1])

    def get_date_calculation_calculator(self):
        return self.driver.find_element(date_calculation_calculator[0], date_calculation_calculator[1])

    def get_temperature_converter(self):
        return self.driver.find_element(temperature_converter[0], temperature_converter[1])
