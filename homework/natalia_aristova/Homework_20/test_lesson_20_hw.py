import requests
import pytest


@pytest.fixture()
def new_object_id():
    print('before test')
    body = {"data": {"color": "red", "size": "small"}, "name": "My object"}
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body, headers=headers)
    object_id = response.json()['id']
    yield object_id
    print('after test')
    requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')


@pytest.fixture(scope='session')
def hello():
    print('Start testing')
    yield
    print('Testing completed')


def test_all_objects(hello):
    response = requests.get('http://objapi.course.qa-practice.com/object')
    assert response.status_code == 200, 'Status code is incorrect'


def test_one_object(new_object_id):
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{new_object_id}')
    print(response.json())
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['id'] == new_object_id, 'ID is incorrect'


@pytest.mark.medium
@pytest.mark.parametrize('body', [{"data": {"color": "red", "size": "small"}, "name": "My object"},
                                  {"data": {"color": "blue", "size": "big"}, "name": "My object2"},
                                  {"data": {"color": "green", "size": "large"},"name": "My object3"}])
def test_post_an_object(body):
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body, headers=headers)
    assert response.status_code == 200, 'Status code is incorrect'


@pytest.mark.critical
def test_put_an_object(new_object_id):
    body = {"data": {"color": "red", "size": "small2"},
            "name": "My object3"}
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f'http://objapi.course.qa-practice.com/object/{new_object_id}',
                            json=body, headers=headers)
    print(response.json()['id'])
    print(response.json())
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'My object3', 'Name is incorrect'
    assert response.json()['id'] == str(new_object_id), 'ID is incorrect'


def test_patch_an_object(new_object_id):
    body = {"data": {"size": "small23"},
            "name": "My object45"}
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f'http://objapi.course.qa-practice.com/object/{new_object_id}',
                              json=body, headers=headers)
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'My object45', 'Name is incorrect'
    assert response.json()['id'] == new_object_id, 'ID is incorrect'
    assert response.json()['data']['size'] == 'small23', 'Size is incorrect'


def test_delete_an_object(new_object_id):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{new_object_id}')
    assert response.status_code == 200, 'Status code is incorrect'
