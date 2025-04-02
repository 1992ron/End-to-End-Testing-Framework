import allure
import pytest
import utilities.manage_pages as page_objects
from extensions.ui_actions import UiActions
from extensions.verifications import Verifications
from workflows.electron_flows import ElectronFlows


@pytest.mark.usefixtures("init_electron_driver")
class TestElectron:
    @allure.title("Test 01: Add and verify new task")
    @allure.description("This test adds a new task and verifies it is added to the list of tasks")
    def test_add_and_verify_new_task(self):
        ElectronFlows.add_new_task('Learn Java')
        Verifications.verify_object_comparison(ElectronFlows.get_number_of_tasks(), 1)
        ElectronFlows.verify_displayed_tasks(['Learn JS'])

    @allure.title("Test 02: Add and verify new tasks")
    @allure.description("This test adds a few new tasks and verifies they are added to the list of tasks")
    def test_add_and_verify_a_few_new_tasks(self):
        # Add a few tasks
        ElectronFlows.add_new_task('Learn JS')
        ElectronFlows.add_new_task('Learn Python')
        ElectronFlows.add_new_task('Learn C#')
        Verifications.verify_object_comparison(ElectronFlows.get_number_of_tasks(), 3)
        ElectronFlows.verify_displayed_tasks(['Learn JS', 'Learn Python', 'Learn C#'])

    @allure.title("Test 03: Filter the list of tasks by their status")
    @allure.description("This test filters the list of tasks by each status: 'All', 'Completed' and 'Todo'")
    def test_filter_list_of_tasks_by_status(self):
        # Add a new task
        ElectronFlows.add_new_task('Learn JS')
        # Mark the first task as completed
        UiActions.click(page_objects.electron_task_page.get_all_tasks_completed_button())
        # Create more tasks
        ElectronFlows.add_new_task('Learn Python')
        ElectronFlows.add_new_task('Learn C#')
        # Open the visibility panel
        UiActions.click(page_objects.electron_task_page.get_visibility_panel())
        # Filter the table by 'Complete' status
        ElectronFlows.filter_tasks_by_completed_status()
        # Filter the table by 'Todo' status
        ElectronFlows.filter_tasks_by_todo_status()
        # Filter the table by 'All' status
        ElectronFlows.filter_tasks_by_all_status()

    @allure.title("Test 04: Filter the list of tasks by their color")
    @allure.description("This test filter the list of tasks by their color")
    def test_filter_list_of_tasks_by_color(self):
        ElectronFlows.add_task_marked_in_red()
        ElectronFlows.add_task_marked_in_orange()
        ElectronFlows.add_task_marked_in_yellow()

        # Filter the list by red color
        UiActions.click(page_objects.electron_task_page.get_visibility_panel())
        ElectronFlows.filter_tasks_by_red_color()
        # Filter the list by orange color
        ElectronFlows.filter_tasks_by_orange_color()
        # Filter the list by yellow color
        ElectronFlows.filter_tasks_by_yellow_color()

    def teardown_method(self):
        ElectronFlows.clean_list_of_tasks()

    # pytest -v -s test_electron.py --alluredir=allure-results
    # allure serve allure-results
