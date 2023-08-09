def requst_post():
    data = {
        'login': 'TimeFF84a',
        'password': 'HondaPrelude9298',
        'authenticity_token': ''
    }
    return data['login']
print(requst_post())