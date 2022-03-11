import requests as rq
from flask import abort
import conf


class Get:
    def __init__(self, url, request):
        self.url = url
        self.request = request
        self.response = None

    def make_request(self):
        headers = dict(self.request.headers)
        headers['Content-Length'] = '0'
        params = self.request.args
        self.response = rq.get(self.url, headers=headers, params=params)

    def check_error(self):
        if self.response is None:
            raise RuntimeError("response is None")
        if self.response.status_code >= 400:
            return abort(self.response.status_code)
        return 1

    def make_full_request(self):
        self.make_request()
        self.check_error()


from . import account
from . import info
