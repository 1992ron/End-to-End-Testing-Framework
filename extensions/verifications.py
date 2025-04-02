from selenium.webdriver.remote.webelement import WebElement


class Verifications:

    # This function checks whether two objects are equal
    @staticmethod
    def verify_object_comparison(expected, actual):
        assert expected == actual, ('Verify object comparison failed, Actual: ' + str(actual) +
                                    ' is not equal to' + str(expected))

    # This function checks whether an element is displayed
    @staticmethod
    def element_is_displayed(element: WebElement):
        assert element.is_displayed(), 'Verify element is displayed failed, element ' + element.text + ' is not displayed'
