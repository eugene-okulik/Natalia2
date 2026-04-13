import pytest
from test_api_naristova.endpoints.create_object import PostObject
from test_api_naristova.endpoints.update_object import UpdateObject
from test_api_naristova.endpoints.get_object import GetObject
from test_api_naristova.endpoints.patch_object import PatchObject
from test_api_naristova.endpoints.delete_object import DeleteObject


@pytest.fixture()
def new_object_id(create_post_endpoint, delete_object_endpoint):
    print('before test')
    body = {"data": {"color": "red", "size": "small"}, "name": "My object"}
    create_post_endpoint.create_new_object(body=body)
    object_id = create_post_endpoint.json['id']
    yield object_id
    print('after test')
    delete_object_endpoint.delete_object(object_id)


@pytest.fixture(scope='session')
def hello():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture()
def create_post_endpoint():
    return PostObject()


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def get_object_endpoint():
    return GetObject()


@pytest.fixture()
def patch_object_endpoint():
    return PatchObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()
