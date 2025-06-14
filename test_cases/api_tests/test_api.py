import allure
from workflows.api_flows import ApiFlows


class TestApi:
    # ######################################## Tests for the /user endpoint####################################
    @allure.epic("Users API")
    class TestUsersAPI:

        @allure.title("Create a new user")
        @allure.description("Verifies that a user can be created")
        def test_create_user_fake(self):
            success, user_id = ApiFlows.create_user("Alice Smith", "alice_smith", "alice@example.com")
            assert success, "Failed to create user"
            assert user_id is not None, "User ID should not be None"

        @allure.title("Get user with known ID")
        @allure.description("Gets a user with ID 1 (only certain users exist in JSONPlaceholder).")
        def test_get_user_valid_id(self):
            success, user_data = ApiFlows.get_user(1)
            assert success, "Failed to retrieve user"
            assert user_data["id"] == 1
            assert "name" in user_data

        @allure.title("Get user with invalid ID")
        @allure.description("Attempts to get a user with an invalid ID and expects failure.")
        def test_get_user_invalid_id(self):
            success, _ = ApiFlows.get_user(9999)
            assert not success, "Expected failure for non-existing user"

        @allure.title("Update user with ID 1")
        def test_update_user(self):
            success, updated_data = ApiFlows.update_user(
                user_id=1,
                name="Updated Name",
                username="updated_username",
                email="updated@example.com"
            )
            assert success, "Failed to update user"
            assert updated_data["name"] == "Updated Name"

        @allure.title("Delete user with ID 1")
        def test_delete_user(self):
            success = ApiFlows.delete_user(1)
            assert success, "Failed to delete user (note: JSONPlaceholder fakes deletes)"

    # ######################################## Tests for the /post endpoint####################################

        @allure.suite("Posts API")
        class TestPostsAPI:

            @allure.title("Create a new post")
            def test_create_post(self):
                success, post_id = ApiFlows.create_post(user_id=1, title="Test Post", body="This is a test post.")
                assert success, "Failed to create post"
                assert post_id is not None

            @allure.title("Get post with valid ID")
            def test_get_post_valid_id(self):
                success, post_data = ApiFlows.get_post(1)
                assert success, "Failed to get post"
                assert post_data["id"] == 1

            @allure.title("Get post with invalid ID")
            def test_get_post_invalid_id(self):
                success, _ = ApiFlows.get_post(9999)
                assert not success, "Expected failure when retrieving invalid post"

            @allure.title("Update post with ID 1")
            def test_update_post(self):
                success, updated_post = ApiFlows.update_post(
                    post_id=1,
                    title="Updated Title",
                    body="Updated body text."
                )
                assert success, "Failed to update post"
                assert updated_post["title"] == "Updated Title"

            @allure.title("Delete post with ID 1")
            def test_delete_post(self):
                success = ApiFlows.delete_post(1)
                assert success, "Failed to delete post (note: JSONPlaceholder fakes deletes)"
