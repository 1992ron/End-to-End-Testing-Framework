import logging
import allure
from extensions.api_actions import ApiActions
from utilities.common_ops import get_configuration_data

url = get_configuration_data("API_Url")


class ApiFlows:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    @staticmethod
    @allure.step("Create a new user")
    def create_user(user_name: str, user_job: str):
        payload = {"name": user_name, "job": user_job}
        response = ApiActions.post_request("users", payload)
        if response.status_code == 201:
            user_id = response.json().get("id")
            logging.info(f"User created with ID: {user_id}")
            return True, user_id  # Return success flag + user ID
        else:
            logging.error(f"Failed to create user: {response.status_code} - {response.text}")
            return False, None  # Return False if creation failed

    @staticmethod
    @allure.step("Retrieve user")
    def get_user(user_id: int):
        response = ApiActions.get_request(f"users/{user_id}")
        if response.status_code == 200:
            user_data = response.json().get("data")
            logging.info(f"Retrieved user data: {user_data}")
            return True, user_data  # Return True for success + user data
        else:
            logging.error(f"Failed to retrieve user: {response.status_code} - {response.text}")
            return False, None  # Return False if retrieval failed

    @staticmethod
    @allure.step("Update user with ID: {user_id} to have name: {name} and job: {job}")
    def update_user(user_id: int, name: str, job: str):
        payload = {"name": name, "job": job}
        response = ApiActions.put_request(f"users/{user_id}", payload)
        if response.status_code == 200:
            updated_data = response.json()
            logging.info(f"Updated user data: {updated_data}")
            return True, updated_data  # Return success flag + updated data
        else:
            logging.error(f"Failed to update user: {response.status_code} - {response.text}")
            return False, None  # Return False if update failed

    @staticmethod
    @allure.step("Delete user with ID: {user_id}")
    def delete_user(user_id: int):
        response = ApiActions.delete_request(f"users/{user_id}")
        if response.status_code == 204:
            logging.info(f"User with ID: {user_id} successfully deleted.")
            return True  # Return True if deletion succeeded
        else:
            logging.error(f"Failed to delete user: {response.status_code} - {response.text}")
            return False  # Return False if deletion failed
