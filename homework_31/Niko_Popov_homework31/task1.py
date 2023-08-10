import requests
import json


class ResurceUser:
    def __init__(self, url):
        self.url = url

    def status_user(self, number):
        self.number = number
        response = requests.get(f'{self.url}/api/users/{self.number}')
        return response

    def json_file(self, number):
        file_json = json.loads(self.status_user(number).text)
        return file_json

    def json_data(self, number):
        d = {}
        data_json = self.json_file(number)
        for key, value in data_json.items():
            for i in value.keys():
                d[i] = value[i]
            return d  # [print(f"{i}, -> {value[f'{i}']}")]



user_status_url = ResurceUser('https://reqres.in')
# print(user_status_url.status_user(2))
# print(user_status_url.json_file(2))
# user_status_url.json_data(2)
print(user_status_url.json_data(2))
