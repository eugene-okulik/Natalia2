from test_api_naristova.endpoints.endpoint import Endpoint
import requests
import allure


class PatchObject(Endpoint):


    @allure.step('Changing object - patch')
    def patch_object(self, new_object_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(f'{self.url}/{new_object_id}',
                                json=body, headers=headers)

        self.json = self.response.json()
        return self.response
