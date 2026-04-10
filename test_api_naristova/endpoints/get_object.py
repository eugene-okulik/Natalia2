from test_api_naristova.endpoints.endpoint import Endpoint
import requests
import allure


class GetObject(Endpoint):


    @allure.step('Get all objects')
    def get_all_objects(self):
        self.response = requests.get(self.url)
        self.json = self.response.json()
        return self.response

    @allure.step('Get one object')
    def get_one_object(self, new_object_id):
        self.response = requests.get(f'{self.url}/{new_object_id}')
        self.json = self.response.json()
        return self.response
