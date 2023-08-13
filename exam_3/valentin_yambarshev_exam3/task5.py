# Создайте систему управления банковскими счетами, которая позволяет создавать,
# управлять и выполнять операции с банковскими счетами различных клиентов.
# Реализуйте класс Client, представляющий клиента банка.
# Класс должен иметь атрибуты name (имя клиента) и id (уникальный идентификатор клиента).
# Реализуйте класс BankAccount, представляющий банковский счет.
# Класс должен иметь атрибуты account_number (номер счета),
# balance (баланс счета) и client (объект типа Client, которому принадлежит счет).
# Класс также должен иметь методы deposit(amount) и withdraw(amount),
# которые позволяют пополнить или снять деньги со счета.
# Реализуйте класс Bank, представляющий банк. Класс должен иметь атрибут accounts,
# который является словарем, где ключами являются номера счетов, а значениями - объекты типа BankAccount.
# Класс также должен иметь методы create_account(client, initial_balance)
# для создания нового счета и get_account(account_number) для получения счета по его номеру.
# Добавьте в класс Bank методы для выполнения переводов между счетами
# (transfer(sender_account, receiver_account, amount)),
# а также для получения общего баланса клиента (get_total_balance(client)),
# который включает сумму денег на всех его счетах.

class Client:

    def __init__(self, name, id):
        self.name = name
        self.id = id


class BankAccount:

    def __init__(self, account_number, client, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.client = client

    # пополняем счет
    def deposit(self, amount):
        self.balance += amount

    # снимаем со счета
    def withdrow(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Недостаточно средств на счете')


class Bank:

    def __init__(self):
        self.accounts = {}

    def create_account(self, client, initial_balance=0):
        new_account_number = len(self.accounts)  # отвечает за количество наших клиентов в банке
        new_account = BankAccount(new_account_number, client, initial_balance)
        self.accounts[new_account_number] = new_account
        return new_account

    # получаем счет по номеру аккаунта(account_number) из словаря(self.accounts)
    # и соответственно проверяем если номер имеется в словаре, то выводим его
    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]  # возвращаем значение по ключу "account_number"
        else:
            print('Такого счета не существует')

    # выполняем перевод между счетами
    def transfer(self, sender_account, receiver_account, amount):
        if sender_account.balance >= amount:
            sender_account.withdrow(amount)
            receiver_account.deposit(amount)
        else:
            print('На счете недостаточно средств')

    def get_total_balance(self, client):
        total_balance = 0
        for account in self.accounts.values():
            if account.client == client:
                total_balance += account.balance
            return total_balance



