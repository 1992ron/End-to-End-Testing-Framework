import logging
import time
import test_cases.conftest as conftest
import allure
from selenium.webdriver.common.keys import Keys
import page_objects.electron_objects.task_page as task_page
import utilities.manage_pages as page_objects
from extensions.ui_actions import UiActions
from utilities.common_ops import wait, ExpectedConditions


class ElectronFlows:

    @staticmethod
    @allure.step("Add a new task")
    def add_new_task(task_name: str):
        UiActions.update_text(page_objects.electron_task_page.get_create_task(), task_name)
        UiActions.update_text(page_objects.electron_task_page.get_create_task(), Keys.RETURN)

    @staticmethod
    @allure.step("Return the number of tasks")
    def get_number_of_tasks():
        return len(page_objects.electron_task_page.get_task_labels())

    @staticmethod
    @allure.step("Cleans the list of tasks")
    def clean_list_of_tasks():
        for task in range(ElectronFlows.get_number_of_tasks()):
            time.sleep(0.5)
            UiActions.mouse_hover_on_tooltip(page_objects.electron_task_page.get_delete_task_buttons()[0])

    @staticmethod
    @allure.step("Filter list of tasks by completed status")
    def filter_tasks_by_completed_status():
        wait(ExpectedConditions.ELEMENT_IS_CLICKABLE, task_page.filter_completed_tasks)
        UiActions.click(page_objects.electron_task_page.get_filter_completed_tasks())
        # Verify that only the completed task is displayed after filtering
        assert ElectronFlows.verify_displayed_tasks(
            ['Learn JS']), "Expected task 'Learn JS' but a different task is displayed"

    @staticmethod
    @allure.step("Filter list of tasks by todo status")
    def filter_tasks_by_todo_status():
        wait(ExpectedConditions.ELEMENT_IS_CLICKABLE, task_page.filter_todo_tasks)
        UiActions.click(page_objects.electron_task_page.get_filter_todo_tasks())
        assert ElectronFlows.verify_displayed_tasks(['Learn Python', 'Learn C#']), ("Expected tasks 'Learn Python', "
                                                                                    "but a different task is displayed")

    @staticmethod
    @allure.step("Filter list of tasks by all status")
    def filter_tasks_by_all_status():
        wait(ExpectedConditions.ELEMENT_IS_CLICKABLE, task_page.filter_all_tasks)
        UiActions.click(page_objects.electron_task_page.get_filter_all_tasks())
        assert ElectronFlows.verify_displayed_tasks(['Learn JS', 'Learn Python', 'Learn C#']), (
            "Expected tasks 'Learn Python', "
            "'Learn C#' but a different task is displayed")

    @staticmethod
    @allure.step("Marks a task in red color")
    def mark_task_in_red_color():
        # Wait for the filter button to be clickable
        wait(ExpectedConditions.ELEMENT_IS_CLICKABLE, task_page.mark_task_in_red)
        # Click on the red color
        UiActions.click(page_objects.electron_task_page.get_mark_task_in_red())
        # Close the color picker
        UiActions.click(page_objects.electron_task_page.get_color_picker())

    @staticmethod
    @allure.step("Marks a task in orange color")
    def mark_task_in_orange_color():
        # Wait for the filter button to be clickable
        wait(ExpectedConditions.ELEMENT_IS_CLICKABLE, task_page.mark_task_in_orange)
        # Click on the orange color
        UiActions.click(page_objects.electron_task_page.get_mark_task_in_orange())
        # Close the color picker
        UiActions.click(page_objects.electron_task_page.get_color_picker())

    @staticmethod
    @allure.step("Marks a task in yellow color")
    def mark_task_in_yellow_color():
        # Wait for the filter button to be clickable
        wait(ExpectedConditions.ELEMENT_IS_CLICKABLE, task_page.mark_task_in_yellow)
        # Click on the yellow color
        UiActions.click(page_objects.electron_task_page.get_mark_task_in_yellow())
        # Close the color picker
        UiActions.click(page_objects.electron_task_page.get_color_picker())

    @staticmethod
    @allure.step("Filter tasks by red color")
    def filter_tasks_by_red_color():
        wait(ExpectedConditions.ELEMENT_IS_CLICKABLE, task_page.red_filter)
        UiActions.click(page_objects.electron_task_page.get_red_filter())
        assert ElectronFlows.verify_displayed_tasks(['red task']), ("Expected only 'red task' to be displayed, "
                                                                    "but other task is displayed")
        UiActions.click(page_objects.electron_task_page.get_red_filter())

    @staticmethod
    @allure.step("Filter tasks by orange color")
    def filter_tasks_by_orange_color():
        wait(ExpectedConditions.ELEMENT_IS_CLICKABLE, task_page.orange_filter)
        UiActions.click(page_objects.electron_task_page.get_orange_filter())
        assert ElectronFlows.verify_displayed_tasks(['orange task']), ("Expected only 'orange task' to be displayed, "
                                                                       "but other task is displayed")
        UiActions.click(page_objects.electron_task_page.get_orange_filter())

    @staticmethod
    @allure.step("Filter tasks by yellow color")
    def filter_tasks_by_yellow_color():
        wait(ExpectedConditions.ELEMENT_IS_CLICKABLE, task_page.yellow_filter)
        UiActions.click(page_objects.electron_task_page.get_yellow_filter())
        assert ElectronFlows.verify_displayed_tasks(['yellow task']), ("Expected only 'yellow task' to be displayed, "
                                                                       "but other task is displayed")

    @staticmethod
    @allure.step("Verify all filtered tasks")
    def verify_displayed_tasks(expected_tasks: list) -> bool:
        # Locate only the elements containing task names (ignoring timestamps)
        displayed_tasks = [task.text for task in page_objects.electron_task_page.get_task_labels()]

        # Log for debugging
        print(f"Displayed tasks: {displayed_tasks}")
        print(f"Expected tasks: {expected_tasks}")

        return set(displayed_tasks) == set(expected_tasks)

    @staticmethod
    @allure.step("Add a new task and mark it in red")
    def add_task_marked_in_red():
        # Choose the red color from the color picker
        UiActions.click(page_objects.electron_task_page.get_color_picker())
        ElectronFlows.mark_task_in_red_color()
        # Add a new task
        ElectronFlows.add_new_task('red task')

    @staticmethod
    @allure.step("Add a new task and mark it in orange")
    def add_task_marked_in_orange():
        # Choose the red color from the color picker
        UiActions.click(page_objects.electron_task_page.get_color_picker())
        ElectronFlows.mark_task_in_orange_color()
        # Add a new task
        ElectronFlows.add_new_task('orange task')

    @staticmethod
    @allure.step("Add a new task and mark it in yellow")
    def add_task_marked_in_yellow():
        # Choose the red color from the color picker
        UiActions.click(page_objects.electron_task_page.get_color_picker())
        ElectronFlows.mark_task_in_yellow_color()
        # Add a new task
        ElectronFlows.add_new_task('yellow task')
