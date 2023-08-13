"""
Создайте систему управления банковскими счетами, которая позволяет создавать, управлять и
выполнять операции с банковскими счетами различных клиентов.
Реализуйте класс Client, представляющий клиента банка. Класс должен иметь атрибуты name (имя клиента)
и id (уникальный идентификатор клиента).
Реализуйте класс BankAccount, представляющий банковский счет. Класс должен иметь атрибуты account_number
 (номер счета), balance (баланс счета) и client (объект типа Client, которому принадлежит счет).
 Класс также должен иметь методы deposit(amount) и withdraw(amount), которые позволяют пополнить или
 снять деньги со счета.
Реализуйте класс Bank, представляющий банк. Класс должен иметь атрибут accounts, который является
словарем, где ключами являются номера счетов, а значениями - объекты типа BankAccount. Класс также
должен иметь методы create_account(client, initial_balance) для создания нового счета и get_account
(account_number) для получения счета по его номеру.
Добавьте в класс Bank методы для выполнения переводов между счетами (transfer(sender_account,
receiver_account, amount)), а также для получения общего баланса клиента (get_total_balance(client)),
 который включает сумму денег на всех его счетах.
Реализуйте обработку ошибок, например, недостаточно средств на счете при снятии денег или отсутствие
счета при переводе.

"""
class Client:
    def __init__(self, name, id):
        self.name = name
        self.id = id
class BankAccount:
    def __init__(self, account_number, balance, client):
        self.account_number = account_number
        self.balance = balance
        self.client = client

    def deposit(self, amount):
        self.balance += amount

class Bank:
#не могу решить(