from locust import task, HttpUser
import random


class ObjectUser(HttpUser):

    @task(1)
    def get_all_objects(self):
        self.client.get('/object')

    @task(3)
    def get_one_object(self):
        self.client.get(f'/object/{random.choice([21, 29, 11, 18])}')

    @task(4)
    def change_object(self):
        body = {"data": {"color": "red", "size": "small2"},
                "name": "My object3"}
        headers = {'Content-Type': 'application/json'}
        self.client.put(f'/object/{random.choice([21, 29, 11, 18])}', json=body, headers=headers)

    @task(2)
    def post_object(self):
        body = {"data": {"color": "red", "size": "small2"},
                "name": "My object3"}
        headers = {'Content-Type': 'application/json'}
        self.client.post('/object', json=body, headers=headers)
