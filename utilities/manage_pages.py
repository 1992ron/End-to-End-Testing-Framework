import test_cases.conftest as conftest
from page_objects.desktop_objects.navigation_menu_page import NavigationMenuPage
from page_objects.desktop_objects.standard_page import StandardPage
from page_objects.desktop_objects.temperature_converter_page import TemperatureConverterPage
from page_objects.electron_objects.task_page import TaskPage
from page_objects.mobile_objects.mobile_create_bug_page import CreateBugPage
from page_objects.mobile_objects.mobile_edit_bug_page import EditBugPage
from page_objects.mobile_objects.mobile_home_page import HomePage
from page_objects.mobile_objects.mobile_menu_page import MenuPage
from page_objects.mobile_objects.mobile_view_bugs_page import ViewBugsPage

# Web pages


# Mobile pages
mobile_create_bug_page = None
mobile_home_page = None
mobile_menu_page = None
mobile_view_bugs_page = None
mobile_edit_bug_page = None

# Electron pages
electron_task_page = None

# Desktop pages
standard_page = None
navigation_menu_page = None
temperature_converter_page = None


##########################################################################################################
# This class contains functions that initiate all the page objects, so they can be used across the project
##########################################################################################################

class ManagePages:

    @staticmethod
    def init_mobile_pages():
        globals()['mobile_create_bug_page'] = CreateBugPage(conftest.driver)
        globals()['mobile_home_page'] = HomePage(conftest.driver)
        globals()['mobile_menu_page'] = MenuPage(conftest.driver)
        globals()['mobile_view_bugs_page'] = ViewBugsPage(conftest.driver)
        globals()['mobile_edit_bug_page'] = EditBugPage(conftest.driver)

    @staticmethod
    def init_electron_pages():
        globals()['electron_task_page'] = TaskPage(conftest.driver)

    @staticmethod
    def init_desktop_pages():
        globals()['standard_page'] = StandardPage(conftest.driver)
        globals()['navigation_menu_page'] = NavigationMenuPage(conftest.driver)
        globals()['temperature_converter_page'] = TemperatureConverterPage(conftest.driver)
