import time
from enum import Enum
from selenium.webdriver.support.wait import WebDriverWait
import test_cases.conftest as conftest
from selenium.webdriver.support import expected_conditions as EC
import xml.etree.ElementTree as ET


# This Enum class is for choosing an expected condition, the 'wait' method uses this class
class ExpectedConditions(Enum):
    ELEMENT_IS_PRESENT = "element_is_present"
    ELEMENT_IS_VISIBLE = "element_is_visible"
    ELEMENT_IS_INVISIBLE = "element_is_invisible"
    URL_CHANGES = "url_changes"
    ELEMENT_IS_CLICKABLE = "element_is_clickable"
    TEXT_TO_BE_PRESENT_IN_ELEMENT = "text_to_be_present_in_element"


# This function determines which wait condition will be used
def wait(condition: ExpectedConditions, elem, *args):
    if condition.value == ExpectedConditions.ELEMENT_IS_PRESENT.value:
        WebDriverWait(conftest.driver, int(get_configuration_data('WaitForElement'))).until(
            EC.presence_of_element_located((elem[0], elem[1])))
    elif condition.value == ExpectedConditions.ELEMENT_IS_VISIBLE.value:
        WebDriverWait(conftest.driver, int(get_configuration_data('WaitForElement'))).until(
            EC.visibility_of_element_located((elem[0], elem[1])))
    elif condition.value == ExpectedConditions.ELEMENT_IS_INVISIBLE.value:
        WebDriverWait(conftest.driver, int(get_configuration_data('WaitForElement'))).until(
            EC.invisibility_of_element_located((elem[0], elem[1])))
    elif condition.value == ExpectedConditions.URL_CHANGES.value:
        WebDriverWait(conftest.driver, int(get_configuration_data('WaitForElement'))).until(EC.url_to_be(elem))
    elif condition.value == ExpectedConditions.ELEMENT_IS_CLICKABLE.value:
        WebDriverWait(conftest.driver, int(get_configuration_data('WaitForElement'))).until(
            EC.element_to_be_clickable((elem[0], elem[1])))
    elif condition.value == ExpectedConditions.TEXT_TO_BE_PRESENT_IN_ELEMENT.value:
        # Check if *args has the required additional argument (text)
        if args:
            expected_text = args[0]
            WebDriverWait(conftest.driver, int(get_configuration_data('WaitForElement'))).until(
                EC.text_to_be_present_in_element((elem[0], elem[1]), expected_text))
        else:
            raise ValueError("Expected text argument is missing for condition: TEXT_TO_BE_PRESENT_IN_ELEMENT")
    else:
        raise ValueError(f"Unsupported condition: {condition}")


# This function extracts value from the xml configuration file. It receives a string parameter - node_name and returns
# the value of that parameter
def get_configuration_data(node_name):
    root = ET.parse(
        "C:/Full Stack Automation Project/Full_Stack_Automation_Project/configuration/configuration.xml").getroot()
    return root.find(".//" + node_name).text


# This function returns the current time in seconds
def get_timestamp():
    return time.time()
