# Написать как можно больше запросов на сервисах
# https://rapidapi.com/developer/dashboard и
# https://reqres.in/
#
# Скачать Postman и попробовать получить в нем ответы от api.

import requests

# URL = 'https://reqres.in/api/users?page=2'
#
# response = requests.get(URL, timeout=5)
# response_json = response.json()
# print(response.status_code)
# print(response_json)
# for i in response_json['data']:
#     print(f"{i['first_name']} {i['last_name']} - {i['email']}")
# ////////////////////////////////////////////////////////////////

# URL = 'https://wft-geo-db.p.rapidapi.com/v1/geo/adminDivisions'
#
# headers = {
#     'X-RapidAPI-Key': '5b5448ded8mshb07a87b7639570fp17ba5fjsnbc779f5c3a70',
#     'X-RapidAPI-Host': 'wft-geo-db.p.rapidapi.com'
# }
# response = requests.get(URL, headers=headers, timeout=5)
# response_json = response.json()
# print(response.status_code)
# print(response.headers['Content-Type'])
# print(response_json['links'][0]['href'])
# //////////////////////////////////////////////////////////////////////

# URL = 'https://wft-geo-db.p.rapidapi.com/v1/geo/locations/33.832213-118.387099/nearbyDivisions'
# params = {
#     'radius': '100'
# }
# headers = {
#     "X-RapidAPI-Key": "5b5448ded8mshb07a87b7639570fp17ba5fjsnbc779f5c3a70",
#     "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
# }
# response = requests.get(URL, params=params, headers=headers, timeout=5)
# response_json = response.json()
# print(response.status_code)
# print(response_json['data'][0]['name'])
# print(response_json['data'][0]['country'])
# print(response.headers)
# /////////////////////////////////////////////////////////////////

# URL = 'https://reqres.in/api/login'
# data = {
#     "email": "eve.holt@reqres.in",
#     "password": "cityslicka"
# }
# response = requests.post(URL, data=data, timeout=5)
# response_json = response.json()
# print(response.status_code)
# print(response_json)
# print(response.headers['date'])
# /////////////////////////////////////////////////////

# URL = 'https://reqres.in/api/users/2'
# data = {
#     "name": "morpheus",
#     "job": "zion resident"
# }
# response = requests.put(URL, data=data, timeout=5)
# response_json = response.json()
# response_headers = response.headers
# print(response_json)
# print(response_headers['Date'].split(' ')[4])
# ///////////////////////////////////////////////////

# URL = 'https://api-football-v1.p.rapidapi.com/v3/countries'
#
# params = {
#     'search': 'engl'
# }
#
# headers = {
#     'X-RapidAPI-Key': '5b5448ded8mshb07a87b7639570fp17ba5fjsnbc779f5c3a70',
#     'X-RapidAPI-Host': 'api-football-v1.p.rapidapi.com'
# }
# response = requests.get(URL, params=params, headers=headers, timeout=5)
# response_json = response.json()
# response_headers = response.headers
# print(response_json)
# print(response_headers)

URL = 'https://postman-rest-api-learner.glitch.me//info?id=1'
params = {'id': '1'}
response = requests.get(URL, params=params, timeout=5)
response_json = response.json()
print(response_json['message'])