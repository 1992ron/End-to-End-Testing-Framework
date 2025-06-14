import logging
import pytest
import allure
from extensions.db_actions import DBActions
from workflows.db_flows import DBFlows


@pytest.mark.usefixtures("init_db_connection")
class TestDatabase:

    @allure.title("Test 01: Verify products in a specific category")
    @allure.description("This test verifies products count in a specific category")
    @pytest.mark.parametrize("category, expected_count", [
        ("Fruits", 2),
        ("Fast Food", 2),
        ("Drinks", 2)
    ])
    def test_products_by_category(self, category, expected_count):
        result = DBActions.get_query_result(["product_id"], "Store", "category", "=", category)
        assert len(result) == expected_count, f"Expected {expected_count} products in {category}, but got {len(result)}"

    @allure.title("Test 02: Verify products with low quantity")
    @allure.description("This test verifies products with quantity less than a threshold")
    @pytest.mark.parametrize("threshold", [100, 200, 300])
    def test_products_below_quantity(self, threshold):
        result = DBActions.get_query_result(["product_id", "product_name", "quantity_in_stock"], "Store", "quantity_in_stock", f"<", {threshold})
        assert result, f"No products found with quantity below {threshold}"

        # Log details of the found products
        for product in result:
            product_id, product_name, quantity = product
            logging.info(
                f"Product ID: {product_id}, Name: {product_name}, Quantity: {quantity} (Below threshold: {threshold})")

    @allure.title("Test 03: Verify product unit price")
    @allure.description("This test verifies the product unit price is within a valid range")
    @pytest.mark.parametrize("min_price, max_price", [
        (1, 100),
        (10, 50),
        (5, 20)
    ])
    def test_product_price_range(self, min_price, max_price):
        query = f"SELECT product_id, product_name, unit_price FROM Store WHERE unit_price BETWEEN {min_price} AND {max_price}"
        db_cursor = self.db_connector.cursor()
        db_cursor.execute(query)
        result = db_cursor.fetchall()

        # Log the retrieved products
        if result:
            for product_id, product_name, unit_price in result:
                logging.info(f"Product Found - ID: {product_id}, Name: {product_name}, Unit Price: {unit_price}")
        else:
            logging.warning(f"No products found within the price range {min_price}-{max_price}")

        assert result, f"No products found within the price range {min_price}-{max_price}"

    @allure.title("Test 04: Insert a new product to the database")
    @allure.description("This test verifies that a newly inserted product appears in the database")
    def test_insert_product(self, init_db_connection):
        # Insert a new product and get the new product id
        new_product_id = DBFlows.insert_product("test_product", "Misc", 10, 50)
        # Verify the new product is added by check if it has an id
        assert new_product_id is not None, "Product insertion failed"
        # Delete the product after inserting
        assert DBFlows.delete_product(new_product_id)




# pytest -v -s test_db.py --alluredir=../allure-results