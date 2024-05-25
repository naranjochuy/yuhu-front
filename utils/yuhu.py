from django.conf import settings
from requests.exceptions import Timeout
import json
import requests


class Yuhu:

    def __init__(self):
        self.base_url = settings.BASE_URL_YUHU
        self.token = settings.JWT_YUHU
        self.headers = {'Authorization': f'Bearer {self.token}'}
        self.timeout_msg = "We're sorry, the request has exceeded the allowed timeout."

    def get_tasks(self, page):
        response = {
            "data": None,
            "error": False,
            "error_msg": "",
            "status_code": None
        }
        try:
            resp = requests.get(
                f'{self.base_url}tasks/?page={page}',
                headers=self.headers
            )
            status_code = resp.status_code
            data = json.loads(resp.text)
            response.update({"status_code": status_code})
            if status_code == 200:
                response.update({"data": data})
            else:
                error_msg = data.get("detail")
                response.update({"error_msg": error_msg, "error": True})
        except Timeout:
            response.update({
                "error": True,
                "error_msg": self.timeout_msg,
                "status_code": 408,
            })
        except Exception as e:
            response.update({
                "error": True,
                "error_msg": str(e),
                "status_code": 500,
            })
        return response

    def get_task(self, id):
        response = {
            "data": None,
            "error": False,
            "error_msg": "",
            "status_code": None
        }
        try:
            resp = requests.get(
                f'{self.base_url}tasks/{id}/',
                headers=self.headers
            )
            status_code = resp.status_code
            data = json.loads(resp.text)
            response.update({"status_code": status_code})
            if status_code == 200:
                response.update({"data": data})
            else:
                error_msg = data.get("detail")
                response.update({"error_msg": error_msg, "error": True})
        except Timeout:
            response.update({
                "error": True,
                "error_msg": self.timeout_msg,
                "status_code": 408,
            })
        except Exception as e:
            response.update({
                "error": True,
                "error_msg": str(e),
                "status_code": 500,
            })
        return response

    def create_task(self, data):
        response = {
            "data": None,
            "error": False,
            "error_msg": "",
            "status_code": None
        }
        try:
            resp = requests.post(
                f'{self.base_url}tasks/',
                headers=self.headers,
                data=data
            )
            status_code = resp.status_code
            data = json.loads(resp.text)
            response.update({"status_code": status_code})
            if status_code == 201:
                response.update({"data": data})
            else:
                error_msg = data.get("detail")
                response.update({"error_msg": error_msg, "error": True})
        except Timeout:
            response.update({
                "error": True,
                "error_msg": self.timeout_msg,
                "status_code": 408,
            })
        except Exception as e:
            response.update({
                "error": True,
                "error_msg": str(e),
                "status_code": 500,
            })
        return response

    def update_task(self, data, id):
        response = {
            "data": None,
            "error": False,
            "error_msg": "",
            "status_code": None
        }
        try:
            resp = requests.put(
                f'{self.base_url}tasks/{id}/',
                headers={'Authorization': f'Bearer {self.token}'},
                data=data
            )
            status_code = resp.status_code
            data = json.loads(resp.text)
            response.update({"status_code": status_code})
            if status_code == 200:
                response.update({"data": data})
            else:
                error_msg = data.get("detail")
                response.update({"error_msg": error_msg, "error": True})
        except Timeout:
            response.update({
                "error": True,
                "error_msg": self.timeout_msg,
                "status_code": 408,
            })
        except Exception as e:
            response.update({
                "error": True,
                "error_msg": str(e),
                "status_code": 500,
            })
        return response

    def delete_task(self, id):
        response = {
            "data": None,
            "error": False,
            "error_msg": "",
            "status_code": None
        }
        try:
            resp = requests.delete(f'{self.base_url}tasks/{id}/', headers=self.headers)
            status_code = resp.status_code
            data = json.loads(resp.text)
            response.update({"status_code": status_code})
            if not status_code == 204:
                error_msg = data.get("detail")
                response.update({"error_msg": error_msg, "error": True})
        except Timeout:
            response.update({
                "error": True,
                "error_msg": self.timeout_msg,
                "status_code": 408,
            })
        except Exception as e:
            response.update({
                "error": True,
                "error_msg": str(e),
                "status_code": 500,
            })
        return response
