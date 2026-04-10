import allure


class Endpoint:
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}

    @allure.step('Check that status code is 200')
    def check_response_status_code_is_correct(self):
        assert self.response.status_code == 200, 'Status code is incorrect'

    @allure.step('Check that name is the same name as sent')
    def check_response_name_is_correct(self, name):
        assert self.json['name'] == name, 'Name is incorrect'

    @allure.step('Check that id is correct')
    def check_response_id_is_correct(self, id):
        assert self.json['id'] == id, 'ID is incorrect'
