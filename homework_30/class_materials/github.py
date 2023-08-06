import requests
from bs4 import BeautifulSoup
import fake_useragent

url = 'https://github.com/login'
auth_url = 'https://github.com/session'
data = {
    'login': 'mikyedit@gmail.com',
    'password': '',
    'authenticity_token': ''
}
user = fake_useragent.UserAgent().random
headers = {
    'use-agent': user
}
session = requests.Session()
session_request = session.get(url, headers=headers)
soup = BeautifulSoup(session_request.text, 'lxml')
token = soup.find('input', {'name': 'authenticity_token'})
print(token['value'])
data['authenticity_token'] = token['value']
print(data)
response = session.post(auth_url, data=data, headers=headers)
response_text = response.text
print(response.status_code)

with open('page_github.html', 'w', encoding='utf-8') as file:
    file.write(response_text)
