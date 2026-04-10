import pytest
import allure


@pytest.fixture()
def new_object_id(create_post_endpoint, delete_object_endpoint):
    print('before test')
    body = {"data": {"color": "red", "size": "small"}, "name": "My object"}
    create_post_endpoint.create_new_object(body=body)
    object_id = create_post_endpoint.json()['id']
    yield object_id
    print('after test')
    delete_object_endpoint.delete_object(object_id)


@pytest.fixture(scope='session')
def hello():
    print('Start testing')
    yield
    print('Testing completed')

TEST_DATA = [{"data": {"color": "red", "size": "small"}, "name": "My object"},
                                  {"data": {"color": "blue", "size": "big"}, "name": "My object2"},
                                  {"data": {"color": "green", "size": "large"}, "name": "My object3"}]


@allure.feature('Viewing objects')
@allure.story('Get request')
@allure.title('Getting all objects')
def test_all_objects(hello, get_object_endpoint):
    get_object_endpoint.get_all_objects()
    get_object_endpoint.check_response_status_code_is_correct()


@allure.feature('Viewing objects')
@allure.story('Get request')
@allure.title('Getting one object')
def test_one_object(get_object_endpoint, new_object_id):
    get_object_endpoint.get_one_object(new_object_id)
    get_object_endpoint.check_response_status_code_is_correct()
    get_object_endpoint.check_response_id_is_correct(new_object_id)


@allure.feature('Objects managing')
@allure.story('Post request')
@allure.title('Adding new object')
@pytest.mark.medium
@pytest.mark.parametrize('body', TEST_DATA)
def test_post_an_object(create_post_endpoint, body):
    create_post_endpoint.create_new_object(body=body)
    create_post_endpoint.check_response_status_code_is_correct()


@allure.feature('Objects managing')
@allure.story('PUT request')
@allure.title('Changing object')
@pytest.mark.critical
def test_put_an_object(update_object_endpoint, new_object_id):
    body = {"data": {"color": "red", "size": "small2"},
                "name": "My object3"}
    update_object_endpoint.make_changes_in_object(new_object_id, body)
    update_object_endpoint.check_response_status_code_is_correct()
    update_object_endpoint.check_response_name_is_correct(body['name'])


@allure.feature('Objects managing')
@allure.story('PATCH request')
@allure.title('Changing object - patch')
@allure.issue('https://ya.ru/images/search?pos=0&from=tabbar&img_url=https%3A%2F%2Fimg.freepik.com%2Ffree-photo%2Fcute-kitten-sitting-staring-playful-fluffy-looking-camera-generated-by-artificial-intelligence_188544-113029.jpg%3Fsemt%3Dais_hybrid%26w%3D740&text=%D0%9A%D0%9E%D0%A2%D0%98%D0%9A&rpt=simage&lr=20575', 'st-2')
@allure.description('Changing object size and object name')
def test_patch_an_object(patch_object_endpoint, new_object_id):
    with allure.step('Prepare test data'):
        body = {"data": {"size": "small23"},
                "name": "My object45"}
    patch_object_endpoint.patch_object(new_object_id, body)
    patch_object_endpoint.check_response_status_code_is_correct()
    patch_object_endpoint.check_response_name_is_correct(body['name'])
    patch_object_endpoint.check_response_id_is_correct(new_object_id)


@allure.feature('Objects managing')
@allure.story('DELETE request')
@allure.title('Delleting object')
def test_delete_an_object(delete_object_endpoint, new_object_id):
    delete_object_endpoint.delete_object(new_object_id)
    delete_object_endpoint.check_response_status_code_is_correct()
