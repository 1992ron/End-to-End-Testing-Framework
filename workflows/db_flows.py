import logging
import allure

from extensions.db_actions import DBActions
from test_cases import conftest


class DBFlows:
    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    @staticmethod
    @allure.step("Get all products of a specific category")
    def get_products_by_category(category: str):
        columns = ["*"]  # Fetch all columns
        table = "Store"
        result = DBActions.get_query_result(columns, table, "category", category)

        if result:
            logging.info(f"Found {len(result)} products in category '{category}'.")
        else:
            logging.info(f"No products found in category '{category}'.")

        return result

    @staticmethod
    @allure.step("Get products with low stock")
    def get_low_stock_products(threshold: int):
        """Returns all products with quantity_in_stock below a certain threshold."""
        query = f"SELECT * FROM products WHERE quantity_in_stock < {threshold}"
        db_cursor = conftest.db_connector.cursor()
        db_cursor.execute(query)
        result = db_cursor.fetchall()

        if result:
            logging.info(f"Found {len(result)} products with stock below {threshold}.")
        else:
            logging.info(f"No low stock products found below {threshold}.")

        return result

    @staticmethod
    @allure.step("Check if product exists in the database")
    def product_exists(product_name: str):
        columns = ["COUNT(*)"]
        table = "Store"
        result = DBActions.get_query_result(columns, table, "product_name", product_name)

        exists = result[0][0] > 0  # Returns True if product exists
        logging.info(f"Product '{product_name}' exists: {exists}")
        return exists

    @staticmethod
    @allure.step("Count total products in the database")
    def count_products():
        query = "SELECT COUNT(*) FROM products"
        db_cursor = conftest.db_connector.cursor()
        db_cursor.execute(query)
        result = db_cursor.fetchone()

        total_count = result[0]
        logging.info(f"Total number of products in the database: {total_count}")
        return total_count

    @staticmethod
    @allure.step("Insert a new product to the table")
    def insert_product(product_name, unit_price, category, quantity_in_stock):
        """
        Inserts a new product into the Store table with a dynamic product_id.
        The product_id is determined by getting the highest existing product_id and adding 1.
        """
        db_cursor = conftest.db_connector.cursor()

        # Get the current highest product_id
        db_cursor.execute("SELECT MAX(product_id) FROM Store")
        max_product_id = db_cursor.fetchone()[0]

        # If there are no products in the table, start with ID 1
        new_product_id = (max_product_id + 1) if max_product_id else 1

        # Construct the INSERT query
        insert_query = f"""
                INSERT INTO Store (product_id, product_name, category, unit_price, quantity_in_stock) 
                VALUES ({new_product_id}, '{product_name}', '{unit_price}', {category}, {quantity_in_stock})
            """

        try:
            db_cursor.execute(insert_query)
            conftest.db_connector.commit()
            logging.info(f"Successfully inserted product: {product_name} with ID: {new_product_id}")
            return new_product_id  # Return the newly inserted product ID for verification
        except Exception as e:
            logging.error(f"Error inserting product {product_name}: {e}")
            globals()['db_connector'].rollback()
            return None

    @staticmethod
    @allure.step("Delete product by product ID")
    def delete_product(product_id):
        """Deletes a product from the Store table and verifies the deletion."""
        db_cursor = conftest.db_connector.cursor()

        # Delete query
        delete_query = f"DELETE FROM Store WHERE product_id = {product_id}"
        db_cursor.execute(delete_query)
        conftest.db_connector.commit()

        # Verify deletion
        verify_query = f"SELECT product_id FROM Store WHERE product_id = {product_id}"
        db_cursor.execute(verify_query)
        result = db_cursor.fetchall()  # Should return an empty list if deleted

        if not result:
            logging.info(f"Product with ID {product_id} was successfully deleted.")
            return True
        else:
            logging.warning(f"Deletion failed: Product with ID {product_id} still exists!")
            return False
