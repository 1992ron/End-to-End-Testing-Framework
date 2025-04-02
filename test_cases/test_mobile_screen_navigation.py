import allure
import pytest
from workflows.mobile_flows import MobileFlows


@pytest.mark.usefixtures('init_mobile_driver')
class TestScreenNavigation:

    @allure.title("Screen navigation")
    @allure.description("Switching between the different screens of the app")
    def test_screen_navigation(self):
        MobileFlows.switch_to_create_bug_screen()
        MobileFlows.switch_to_view_bugs_screen()
        MobileFlows.switch_to_home_screen()

