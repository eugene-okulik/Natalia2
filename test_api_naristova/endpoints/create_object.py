from test_api_naristova.endpoints.endpoint import Endpoint
import requests
import allure


class PostObject(Endpoint):


    @allure.step('Create new object')
    def create_new_object(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(self.url, json=body, headers=headers)
        self.json = self.response.json()
        return self.response
