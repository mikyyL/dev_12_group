import random
from Task_5_BankAcc import *

print('Реализуйте класс Client, представляющий клиента банка. Класс должен иметь атрибуты name (имя клиента)'
'и id (уникальный идентификатор клиента).'
'Реализуйте класс BankAccount, представляющий банковский счет. Класс должен иметь атрибуты account_number '
'(номер счета), '
'balance (баланс счета) и client (объект типа Client, которому принадлежит счет). Класс также должен иметь методы '
'deposit(amount) и withdraw(amount), которые позволяют пополнить или снять деньги со счета.'
'Реализуйте класс Bank, представляющий банк. Класс должен иметь атрибут accounts, который является словарем, '
'где ключами являются номера счетов, а значениями - объекты типа BankAccount. Класс также должен иметь методы '
'create_account(client, initial_balance) для создания нового счета и get_account(account_number) '
'для получения счета по его номеру.'
'Добавьте в класс Bank методы для выполнения переводов между счетами '
'(transfer(sender_account, receiver_account, amount)), а также для получения общего баланса клиента '
'(get_total_balance(client)), который включает сумму денег на всех его счетах.'
'Реализуйте обработку ошибок, например, недостаточно средств на счете при снятии денег или отсутствие счета при '
'переводе.')


class Bank:

    def __init__(self):
        self.accounts = {}

    def create_account(self, client, initial_balance):
        # account_number = len(self.accounts) + 1 # Для проверки лучше это
        account_number = random.randint(100, 999)
        account = BankAccount(account_number, initial_balance, client)
        self.accounts[account_number] = account
        return account
        # return f'Счёт пользователя: {client} создан.\n' \     # Красивый вывод, но не будет работать трансфер
        #        f'Номер счёта: {account_number}\n' \
        #        f'Изначальный баланс: {initial_balance} у.е.\n' \
        #        f'{self.accounts.keys()}'

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print('Такого счёта не существует.')

    def transfer(self, sender_account, receiver_account, amount):
        if sender_account.balance >= amount:
            sender_account.withdraw(amount)
            receiver_account.deposit(amount)
        else:
            raise ValueError('Недостаточно средств для перевода')

    def get_total_balance(self, client):
        total_balance = 0
        for account in self.accounts.values():
            if account.client == client:
                total_balance += account.balance
        return total_balance


cl = Client('Sam', 100)
cl2 = Client('Tom', 50)

b = Bank()

acc1 = b.create_account(cl, 100)
acc2 = b.create_account(cl2, 0)
acc3 = b.create_account(cl, 110)
# print(acc1)
# print(acc2)

# acc1 = b.get_account(1)
# acc2 = b.get_account(2)

print(b.get_total_balance(cl))

b.transfer(acc2, acc1, 10)
