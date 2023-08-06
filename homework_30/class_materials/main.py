import requests

data = {
    'custname': 'hello',
    'custtel': '12345678',
    'custemail': 'test@gmail.com',
    'size': 'small',
    'topping': 'bacon',
    'delivery': '11:15',
    'comments': 'faster'
}

URL = 'http://httpbin.org/post'
response = requests.post(URL, data=data)
print(response.status_code)
print(response.text)