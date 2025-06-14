import logging
import allure
from extensions.api_actions import ApiActions
from utilities.common_ops import get_configuration_data

url = get_configuration_data("API_Url")


class ApiFlows:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Functions for "/users" endpoint

    @staticmethod
    @allure.step("Create a new user")
    def create_user(user_name: str, username: str, email: str):
        payload = {"name": user_name, "username": username, "email": email}
        response = ApiActions.post_request("users", payload)
        if response.status_code == 201:
            user_id = response.json().get("id")
            logging.info(f"User created with ID: {user_id}")
            return True, user_id
        else:
            logging.error(f"Failed to create user: {response.status_code} - {response.text}")
            return False, None

    @staticmethod
    @allure.step("Retrieve user")
    def get_user(user_id: int):
        response = ApiActions.get_request(f"users/{user_id}")
        if response.status_code == 200:
            user_data = response.json()
            logging.info(f"Retrieved user data: {user_data}")
            return True, user_data
        else:
            logging.warning(f"User ID {user_id} not found or failed: {response.status_code}")
            return False, None

    @staticmethod
    @allure.step("Update user with ID: {user_id}")
    def update_user(user_id: int, name: str, username: str, email: str):
        payload = {"id": user_id, "name": name, "username": username, "email": email}
        response = ApiActions.put_request(f"users/{user_id}", payload)
        if response.status_code == 200:
            updated_data = response.json()
            logging.info(f"Updated user data: {updated_data}")
            return True, updated_data
        else:
            logging.error(f"Failed to update user: {response.status_code} - {response.text}")
            return False, None

    @staticmethod
    @allure.step("Delete user with ID: {user_id}")
    def delete_user(user_id: int):
        response = ApiActions.delete_request(f"users/{user_id}")
        if response.status_code == 200:
            logging.info(f"User with ID: {user_id} successfully deleted.")
            return True
        else:
            logging.error(f"Failed to delete user: {response.status_code} - {response.text}")
            return False

    # Methods for "/posts" endpoint

    @staticmethod
    @allure.step("Create a new post")
    def create_post(user_id: int, title: str, body: str):
        payload = {"userId": user_id, "title": title, "body": body}
        response = ApiActions.post_request("posts", payload)
        if response.status_code == 201:
            post_id = response.json().get("id")
            logging.info(f"Post created with ID: {post_id}")
            return True, post_id
        else:
            logging.error(f"Failed to create post: {response.status_code} - {response.text}")
            return False, None

    @staticmethod
    @allure.step("Get post by ID")
    def get_post(post_id: int):
        response = ApiActions.get_request(f"posts/{post_id}")
        if response.status_code == 200:
            post_data = response.json()
            logging.info(f"Retrieved post data: {post_data}")
            return True, post_data
        else:
            logging.error(f"Failed to retrieve post: {response.status_code} - {response.text}")
            return False, None

    @staticmethod
    @allure.step("Update post")
    def update_post(post_id: int, title: str, body: str):
        payload = {"title": title, "body": body}
        response = ApiActions.put_request(f"posts/{post_id}", payload)
        if response.status_code == 200:
            updated_post = response.json()
            logging.info(f"Updated post: {updated_post}")
            return True, updated_post
        else:
            logging.error(f"Failed to update post: {response.status_code} - {response.text}")
            return False, None

    @staticmethod
    @allure.step("Delete post by ID")
    def delete_post(post_id: int):
        response = ApiActions.delete_request(f"posts/{post_id}")
        if response.status_code in [200, 204]:  # JSONPlaceholder returns 200
            logging.info(f"Post {post_id} deleted (faked by API).")
            return True
        else:
            logging.error(f"Failed to delete post: {response.status_code} - {response.text}")
            return False

