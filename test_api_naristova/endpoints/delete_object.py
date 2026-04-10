from test_api_naristova.endpoints.endpoint import Endpoint
import requests
import allure


class DeleteObject(Endpoint):

    @allure.step('Delete object')
    def delete_object(self, new_object_id):
        self.response = requests.delete(f'{self.url}/{new_object_id}')
        return self.response
