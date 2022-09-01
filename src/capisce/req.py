import base64
import requests


class Req:
    def __init__(self):
        pass

    def get(self, endpoint, headers):
        try:
            r = requests.get(endpoint, headers=headers)
            response = {
                "content_type": r.headers['Content-Type'],
                "status_code": r.status_code,
                "headers": dict(r.headers),
                "body": base64.b64encode(r.content).decode()
            }
        except requests.exceptions.ConnectionError:
            return {"error": "Could not send request"}
        return response

    def head(self, endpoint, headers):
        try:
            r = requests.head(endpoint, headers=headers)
            response = {
                "content_type": r.headers['Content-Type'],
                "status_code": r.status_code,
                "headers": dict(r.headers)
            }
        except requests.exceptions.ConnectionError:
            return {"error": "Could not send request"}
        return response

    def post(self, endpoint, headers, body):
        try:
            r = requests.post(endpoint, headers=headers, data=body)
            response = {
                "content_type": r.headers['Content-Type'],
                "status_code": r.status_code,
                "headers": dict(r.headers),
                "body": base64.b64encode(r.content).decode()
            }
        except requests.exceptions.ConnectionError:
            return {"error": "Could not send request"}
        return response

    def put(self, endpoint, headers, body):
        try:
            r = requests.put(endpoint, headers=headers, data=body)
            response = {
                "content_type": r.headers['Content-Type'],
                "status_code": r.status_code,
                "headers": dict(r.headers),
                "body": base64.b64encode(r.content).decode()
            }
        except requests.exceptions.ConnectionError:
            return {"error": "Could not send request"}
        return response

    def delete(self, endpoint, headers, body):
        try:
            r = requests.delete(endpoint, headers=headers, data=body)
            response = {
                "content_type": r.headers['Content-Type'],
                "status_code": r.status_code,
                "headers": dict(r.headers),
                "body": base64.b64encode(r.content).decode()
            }
        except requests.exceptions.ConnectionError:
            return {"error": "Could not send request"}
        return response

    def options(self, endpoint, headers):
        try:
            r = requests.options(endpoint, headers=headers)
            response = {
                "content_type": r.headers['Content-Type'],
                "status_code": r.status_code,
                "headers": dict(r.headers),
                "body": base64.b64encode(r.content).decode()
            }
        except requests.exceptions.ConnectionError:
            return {"error": "Could not send request"}
        return response

    def patch(self, endpoint, headers, body):
        try:
            r = requests.patch(endpoint, headers=headers, data=body)
            response = {
                "content_type": r.headers['Content-Type'],
                "status_code": r.status_code,
                "headers": dict(r.headers),
                "body": base64.b64encode(r.content).decode()
            }
        except requests.exceptions.ConnectionError:
            return {"error": "Could not send request"}
        return response
