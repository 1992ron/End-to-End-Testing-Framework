import allure
from workflows.api_flows import ApiFlows


class TestUpdateUser:

    @allure.title("Update user")
    @allure.description("This test updates the user details")
    def test_update_user_details(self):
        # Create a user
        user_created, user_id = ApiFlows.create_user("Dan Brown", "Writer")

        # Verify the user was created successfully
        assert user_created, "User creation failed"
        assert user_id is not None, "User ID should not be None"

        # Update the user details
        updated_successfully, updated_data = ApiFlows.update_user(user_id, "Ragnar Luthbrook", "Viking")

        # Verify that the update was successful
        assert updated_successfully, "User update failed"
        # Verify the new updated name and job
        assert updated_data.get("name") == "Ragnar Luthbrook", "User name did not update correctly"
        assert updated_data.get("job") == "Viking", "User job did not update correctly"
