# Используя платформы https://rapidapi.com/developer/dashboard и https://reqres.in/
# написать юнит тесты используя фреимворк pytest.
import requests
import json


class MoviesDatabase:

    def __init__(self, url, key, host):
        self.url = url
        self.key = key
        self.host = host

    def querystring(self, number):
        params = {'limit': {number}}
        return params

    def headers(self):
        headers = {
            'X-RapidAPI-Key': f'{self.key}',
            'X-RapidAPI-Host': f'{self.host}'
        }
        return headers

    def respon(self, num_querys):
        response = requests.get(url=self.url, headers=self.headers(), params=self.querystring(num_querys))
        return response

    def get_res_json(self, num_querys):
        json_data = json.loads(self.respon(num_querys).text)
        return json_data



dec = MoviesDatabase('https://moviesdatabase.p.rapidapi.com/actors/random',
                     '1b14d6fd0cmshf21c659eee42808p1c174ajsn8c234f908767',
                     'moviesdatabase.p.rapidapi.com')

print(dec.respon(2))
print(dec.get_res_json(2))
for key in dec.get_res_json(2).keys():
    print(dec.get_res_json(2)[key])
print(dec.respon(2).headers)
