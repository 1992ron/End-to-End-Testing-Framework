import sqlite3
import allure
import appium
import pytest
import selenium
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utilities.manage_pages import ManagePages
from selenium import webdriver
import appium.webdriver
from utilities.common_ops import get_configuration_data, get_timestamp

driver = None
action = None
db_connector = None


# This function initializes the web driver
@pytest.fixture(scope='class')
def init_web_driver(request):
    globals()['driver'] = get_web_driver()
    driver = globals()['driver']
    # Configure the WebDriver instance
    driver.implicitly_wait(int(get_configuration_data('ImplicitlyWait')))
    driver.maximize_window()
    driver.get(get_configuration_data('Url'))
    request.cls.driver = driver
    ManagePages.init_web_pages()
    yield
    driver.quit()


# This function initializes the mobile driver
@pytest.fixture(scope='class')
def init_mobile_driver(request):
    globals()['driver'] = get_mobile_driver()
    driver = globals()['driver']
    driver.implicitly_wait(int(get_configuration_data('ImplicitlyWait')))
    request.cls.driver = driver
    globals()['action'] = TouchAction(driver)
    request.cls.action = globals()['action']
    ManagePages.init_mobile_pages()
    yield
    driver.quit()


# This function initializes the electron driver
@pytest.fixture(scope='class')
def init_electron_driver(request):
    globals()['driver'] = get_electron_driver()
    driver = globals()['driver']
    driver.implicitly_wait(int(get_configuration_data('ImplicitlyWait')))
    request.cls.driver = driver
    globals()['action'] = ActionChains(driver)
    request.cls.action = globals()['action']
    ManagePages.init_electron_pages()
    yield
    driver.quit()


# This function initializes the desktop driver for windows (WinAppDriver)
@pytest.fixture(scope='class')
def init_desktop_driver(request):
    globals()['driver'] = get_desktop_driver()
    driver = globals()['driver']
    driver.implicitly_wait(int(get_configuration_data('ImplicitlyWait')))
    request.cls.driver = driver
    ManagePages.init_desktop_pages()
    yield
    driver.quit()


# This function initializes the sql connection for sqlite
@pytest.fixture(scope='class')
def init_db_connection(request):
    db_connector = sqlite3.connect(get_configuration_data("DB_Path"))
    globals()['db_connector'] = db_connector
    request.cls.db_connector = db_connector
    yield
    db_connector.close()


#  This function determines which browser will be used, the init_web_driver uses this function
def get_web_driver():
    web_driver = get_configuration_data("Browser")
    if web_driver.lower() == 'chrome':
        driver = get_chrome()
    elif web_driver.lower() == 'firefox':
        driver = get_firefox()
    elif web_driver.lower() == 'edge':
        driver = get_edge()
    else:
        driver = None
        raise Exception('Wrong input, unrecognized browser')
    return driver


#  This function determines which mobile operating system will be used, the init_mobile_driver uses this function
def get_mobile_driver():
    if get_configuration_data('Operating_System').lower() == 'android':
        driver = get_android(get_configuration_data('UDID'))
    elif get_configuration_data('Operating_System').lower() == 'ios':
        driver = get_ios(get_configuration_data('UDID'))
    else:
        driver = None
        raise Exception('Unrecognized mobile operating system')
    return driver


# This function returns the electron driver, the init_electron_driver function uses this function
def get_electron_driver():
    option = selenium.webdriver.ChromeOptions()
    option.binary_location = get_configuration_data('Electron_App')
    driver = selenium.webdriver.Chrome(chrome_options=option, executable_path=get_configuration_data('Electron_Driver'))
    return driver


# This function returns the desktop driver, the init_desktop_driver function uses this function
def get_desktop_driver():
    dc = {}
    dc['app'] = get_configuration_data('Application_Name')
    dc['platformName'] = 'Windows'
    dc['deviceName'] = 'WindowsPC'
    driver = appium.webdriver.Remote(get_configuration_data('WinAppDriver_Service'), dc)
    return driver


# This function returns the chrome driver, the get_web_driver function uses this function
def get_chrome():
    # 1) Build ChromeOptions to suppress both the normal password UI and the "unsafe password" alert
    chrome_opts = Options()
    prefs = {
        "credentials_enable_service": False,  # turn off the normal password manager UI
        "profile.password_manager_enabled": False,  # ditto
        "profile.password_manager_leak_detection": False  # ✏️ suppress the data-breach warning
    }
    chrome_opts.add_experimental_option("prefs", prefs)

    # 2) Disable the underlying feature entirely
    chrome_opts.add_argument("--disable-features=PasswordLeakDetection")
    chrome_opts.add_argument("--disable-notifications")

    # 3) Instantiate
    driver_path = ChromeDriverManager().install()
    return webdriver.Chrome(
        executable_path=driver_path,
        chrome_options=chrome_opts
    )


# This function returns the firefox driver, the get_web_driver function uses this function
def get_firefox():
    service = Service(executable_path=GeckoDriverManager.install())
    firefox_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    return firefox_driver


# This function returns the edge driver, the get_web_driver function uses this function
def get_edge():
    service = Service(EdgeChromiumDriverManager().install())
    edge_driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
    return edge_driver


# This function initialize the Android operating system, the get_mobile driver calls this function
def get_android(udid):
    dc = {}
    dc['udid'] = udid
    dc['appPackage'] = get_configuration_data('App_Package')
    dc['appActivity'] = get_configuration_data('App_Activity')
    dc['platformName'] = 'android'
    android_driver = appium.webdriver.Remote(get_configuration_data('Appium_Server'), dc)
    return android_driver


# This function initialize the iOS operating system, the get_mobile driver calls this function
def get_ios(udid):
    dc = {}
    dc['udid'] = udid
    dc['bundle_id'] = get_configuration_data('Bundle_ID')
    dc['platformName'] = 'ios'
    ios_driver = appium.webdriver.Remote(get_configuration_data('Appium_Server'), dc)
    print("hello")
    return ios_driver


# This method is to capture exceptions and errors across the project
def pytest_exception_interact(node, call, report):
    if report.failed:
        if globals()['driver'] is not None:  # if it is None --> this is an exception from API test
            image = get_configuration_data('ScreenshotsPath') + 'screen' + str(get_timestamp()) + '.png'
            globals()['driver'].get_screenshot_as_file(image)
            allure.attach.file(image, attachment_type=allure.attachment_type.PNG)
