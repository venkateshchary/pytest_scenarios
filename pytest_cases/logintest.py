import pytest
import requests


@pytest.fixture(scope='module')
def validate():
    def make_with_variables(type_method, url, data=None, headers=None):
        if 'post' in type_method:
            r = requests.post(url, data=data)
            return r.json()
        if 'get' in type_method:
            r = requests.get(url, headers=headers)
            return r.json()
    return make_with_variables


class Testlogin(object):
    login_url = "http://127.0.0.1:8000/login/"

    def test_userlogin(self, validate):
        data = {"password": "12345", "username": "venky"}
        v = validate('post', self.login_url, data)
        assert "logged in successfully" in v['message']
        print("\n--------------:login is success")




