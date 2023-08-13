from Task_5_Client import Client


class BankAccount:

    def __init__(self, account_number, balance, client):
        self.account_number = account_number
        self.balance = balance
        self.client = client

    client = Client()

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError('Недостаточно средств.')


# ba = BankAccount(1, 0, 'user')
# print(ba.client)
