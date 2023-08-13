class Client:

    def __init__(self, name='User', user_id=555):
        self.name = name
        self.user_id = user_id

    def __str__(self):
        return f'Имя клиента: {self.name} - Уникальный id: {self.user_id}'


acc = {}
