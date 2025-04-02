import allure
import test_cases.conftest as conftest


class DBActions:

    @staticmethod
    @allure.step("Query builder")
    # Example: "SELECT product_id, product_name FROM Store WHERE category = 'Drinks'
    def query_builder(columns, table, where_name, operator, where_value):
        cols = ','.join(columns)
        query = f"SELECT {cols} FROM {table} WHERE {where_name} {operator} '{where_value}' "

        return query

    @staticmethod
    @allure.step("Get query result")
    def get_query_result(columns, table, where_name, operator, where_value):
        query = DBActions.query_builder(columns, table, where_name, operator, where_value)
        db_cursor = conftest.db_connector.cursor()
        db_cursor.execute(query)
        result = db_cursor.fetchall()
        return result  # Returns a list of tuples
