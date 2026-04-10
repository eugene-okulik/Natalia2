from test_api_naristova.endpoints.endpoint import Endpoint
import requests
import allure


class UpdateObject(Endpoint):

    @allure.step('Update an object')
    def make_changes_in_object(self, new_object_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(f'{self.url}/{new_object_id}', json=body, headers=headers)
        self.json = self.response.json()
        return self.response
