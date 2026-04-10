import pytest
from test_api_naristova.endpoints.create_object import PostObject
from test_api_naristova.endpoints.update_object import UpdateObject
from test_api_naristova.endpoints.get_object import GetObject
from test_api_naristova.endpoints.patch_object import PatchObject
from test_api_naristova.endpoints.delete_object import DeleteObject


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