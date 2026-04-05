import requests


def all_objects():
    response = requests.get('http://objapi.course.qa-practice.com/object')
    assert response.status_code == 200, 'Status code is incorrect'


def new_object():
    body = {"data": {
        "color": "red",
        "size": "small"
    },
        "name": "My object"}
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body, headers=headers)
    return response.json()['id']


def clear(post_id):
    requests.delete(f'http://objapi.course.qa-practice.com/object/{post_id}')


def one_object():
    post_id = new_object()
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{post_id}')
    print(response.json())
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['id'] == post_id, 'ID is incorrect'
    clear(post_id)


def post_an_object():
    body = {"data": {
                "color": "red",
                "size": "small"
            },
            "name": "My object"}
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body, headers=headers)
    assert response.status_code == 200, 'Status code is incorrect'


def put_an_object():
    post_id = new_object()
    print(post_id)
    body = {"data": {
                "color": "red",
                "size": "small2"
            },
            "name": "My object3"}
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f'http://objapi.course.qa-practice.com/object/{post_id}',
                            json=body, headers=headers)
    print(response.json()['id'])
    print(response.json())
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'My object3', 'Name is incorrect'
    assert response.json()['id'] == str(post_id), 'ID is incorrect' # пришлось в стр переводить, чтобы проверка прошла
    clear(post_id)


def patch_an_object():
    post_id = new_object()
    body = {"data": {
                "size": "small23"
            },
            "name": "My object45"}
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f'http://objapi.course.qa-practice.com/object/{post_id}',
                              json=body, headers=headers)
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'My object45', 'Name is incorrect'
    assert response.json()['id'] == post_id, 'ID is incorrect'
    assert response.json()['data']['size'] == 'small23', 'Size is incorrect'
    clear(post_id)


def delete_an_object():
    post_id = new_object()
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{post_id}')
    assert response.status_code == 200, 'Status code is incorrect'


all_objects()
one_object()
post_an_object()
put_an_object()
patch_an_object()
delete_an_object()
