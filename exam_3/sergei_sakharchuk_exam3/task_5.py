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

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Недостаточно средств на счете!")


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, client, initial_balance):
        account_number = len(self.accounts) + 1
        account = BankAccount(account_number, initial_balance, client)
        self.accounts[account_number] = account

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            raise ValueError("Счет с указанным номером не существует!")

    def transfer(self, sender_account, receiver_account, amount):
        if sender_account.balance >= amount:
            sender_account.withdraw(amount)
            receiver_account.deposit(amount)
        else:
            raise ValueError("Недостаточно средств на счете отправителя!")

    def get_total_balance(self, client):
        total_balance = 0
        for account in self.accounts.values():
            if account.client == client:
                total_balance += account.balance
        return total_balance


bank = Bank()


client1 = Client("Иван", 1)
client2 = Client("Анна", 2)

bank.create_account(client1, 1000)
bank.create_account(client1, 2000)
bank.create_account(client2, 5000)

account1 = bank.get_account(1)
account2 = bank.get_account(2)

account1.deposit(500)
account1.withdraw(200)
account2.withdraw(1000)

bank.transfer(account1, account2, 300)
total_balance = bank.get_total_balance(client1)
print(f"Общий баланс клиента {client1.name}: {total_balance}")