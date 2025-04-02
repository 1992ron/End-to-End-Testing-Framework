import requests
import allure
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

BASE_URL = "https://reqres.in/api"


class ApiActions:

    @staticmethod
    @allure.step("Sending GET request to {endpoint}")
    def get_request(endpoint, query_params=None):
        url = f"{BASE_URL}/{endpoint}"
        logging.info(f"GET Request: {url} | Params: {query_params}")
        response = requests.get(url, params=query_params)
        logging.info(f"Response: {response.status_code} | Body: {response.text}")
        return response

    @staticmethod
    @allure.step("Sending POST request to {endpoint} with payload: {payload}")
    def post_request(endpoint, payload):
        url = f"{BASE_URL}/{endpoint}"
        logging.info(f"POST Request: {url} | Payload: {payload}")
        response = requests.post(url, json=payload)
        logging.info(f"Response: {response.status_code} | Body: {response.text}")
        return response

    @staticmethod
    @allure.step("Sending PUT request to {endpoint} with payload: {payload}")
    def put_request(endpoint, payload):
        url = f"{BASE_URL}/{endpoint}"
        logging.info(f"PUT Request: {url} | Payload: {payload}")
        response = requests.put(url, json=payload)
        logging.info(f"Response: {response.status_code} | Body: {response.text}")
        return response

    @staticmethod
    @allure.step("Sending DELETE request to {endpoint}")
    def delete_request(endpoint):
        url = f"{BASE_URL}/{endpoint}"
        logging.info(f"DELETE Request: {url}")
        response = requests.delete(url)
        logging.info(f"Response: {response.status_code} | Body: {response.text}")
        return response
