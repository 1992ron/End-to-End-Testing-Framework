import allure
from workflows.api_flows import ApiFlows


class TestCreateUser:
    @allure.title("Create a new user")
    @allure.step("This test creates a new user")
    def test_create_and_delete_user(self):
        # Create a user
        user_created, user_id = ApiFlows.create_user("Dan Brown", "Writer")

        # verify the user was created successfully
        assert user_created, "User creation failed"
        assert user_id is not None, "User ID should not be None"

        # Delete the user
        user_deleted = ApiFlows.delete_user(user_id)
        assert user_deleted, "User deletion failed"



