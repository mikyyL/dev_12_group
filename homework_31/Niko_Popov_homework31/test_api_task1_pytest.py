# Используя платформы https://rapidapi.com/developer/dashboard и https://reqres.in/
# написать юнит тесты используя фреимворк pytest.
import json
import requests
import pytest
import fake_useragent
from task1 import ResurceUser

# user = fake_useragent.UserAgent.random
# headers = {
#     'user': user
# }


def mod():
    user_status_url = ResurceUser('https://reqres.in')
    return user_status_url


def test_URL():
    url = 'https://reqres.in/api/users/2'
    assert url == 'https://reqres.in/api/users/2'
    return url


def test_check_status_client():
    user_status_url = ResurceUser('https://reqres.in')
    assert user_status_url.status_user(2).status_code == 200


def test_page_user_agent():
    user_status_url = ResurceUser('https://reqres.in')
    assert user_status_url.status_user(2).headers[
               'Content-Type'] == 'application/json; charset=utf-8'


def test_body_file_json_response():
    user_status_url = ResurceUser('https://reqres.in')
    assert user_status_url.json_file(2)['data']
    assert user_status_url.json_file(2)['support']


def test_body_json_data_response_id():
    user_status_url = ResurceUser('https://reqres.in')
    assert user_status_url.json_data(2)['id'] == 2


def test_body_json_data_response_email():
    # user_status_url = ResurceUser('https://reqres.in')
    assert mod().json_data(2)['email'] == 'janet.weaver@reqres.in'


def test_body_json_data_response_first_name():
    assert mod().json_data(2)['first_name'] == 'Janet'


def test_body_json_data_response_last_name():
    assert mod().json_data(2)['last_name'] == 'Weaver'


def test_body_json_data_response_avatar():
    assert mod().json_data(2)['avatar'] == 'https://reqres.in/img/faces/2-image.jpg'
