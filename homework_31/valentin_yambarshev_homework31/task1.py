# 1) Используя платформы https://rapidapi.com/developer/dashboard и https://reqres.in/
# написать юнит тесты используя фреимворк pytest.
import requests
import fake_useragent


# def request_get(url):
#     params = {
#         'fixture': '215662'
#     }
#     headers = {
#         'X-RapidAPI-Key': '5b5448ded8mshb07a87b7639570fp17ba5fjsnbc779f5c3a70',
#         'X-RapidAPI-Host': 'api-football-v1.p.rapidapi.com'
#     }
#     response = requests.get(url, params=params, headers=headers, timeout=5)
#     assert response.status_code == 200, 'Ошибка, ожидалось 200'
#     return response.json()
#
#
# URL = 'https://api-football-v1.p.rapidapi.com/v3/fixtures/events'
# print(request_get(URL))

def request_post(url, auth_url):
    data = {
        'login': 'TimeFF84a',
        'password': 'HondaPrelude9298',
        'authenticity_token': ''
    }
    assert data['login'] == 'TimeFF84a', 'Ошибка, неверный логин'
    assert data['password'] == 'HondaPrelude9298', 'Ошибка, неверный пароль'

    user = fake_useragent.UserAgent().random
    headers = {
        'user-agent': user
    }

    session = requests.Session()
    session_request = session.get(url, headers=headers)
    response = session.post(auth_url, data=data, headers=headers)
    response_text = response.text
    return response_text


URL = 'https://github.com/login'
auth_url = 'https://github.com/session'
print(request_post(URL, auth_url))

