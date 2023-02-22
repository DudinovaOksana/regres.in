import requests
import settings


class Reqres:
    def __init__(self):
        self.base_url = settings.base_url

    def get_list_of_users(self, page, per_page):
        url = f"{self.base_url}api/users?page={page}&per_page={per_page}"
        res = requests.get(url)
        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_single_user(self):
        res = requests.get(self.base_url + 'api/users/2')
        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_single_user_not_found(self):
        res = requests.get(self.base_url + 'api/users/23')
        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def create_user(self, name, job):
        data = {
            "name": name,
            "job": job
        }
        res = requests.post(url=self.base_url + 'api/users', json=data)
        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def delete_user(self, user_id):
        res = requests.delete(f"{self.base_url}api/users/{user_id}")
        response_head = res.headers
        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def fetch_resource_list(self, page, per_page):
        data = {
            "page": page,
            "per_page": per_page
        }
        res = requests.get(self.base_url + 'api/unknown')
        response_head = res.headers
        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def fetch_single_resource(self, id):
        res = requests.get(f'{self.base_url}api/unknown/{id}')
        response_head = res.headers
        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def put_user(self, id):
        new_data = {"name": 'Vasya',
                    "job": 'Doctor'}
        res = requests.put(url=f"{self.base_url}api/users/{id}", json=new_data)
        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text
        return status, result
