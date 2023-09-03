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
        if amount > self.balance:
            raise ValueError("Not enough money on the account!")
        self.balance -= amount


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, client, initial_balance):
        account_number = len(self.accounts) + 1
        account = BankAccount(account_number, initial_balance, client)
        self.accounts[account_number] = account

    def get_account(self, account_number):
        if account_number not in self.accounts:
            raise ValueError("Account not found!")
        return self.accounts[account_number]

    def transfer(self, sender_account_number, receiver_account_number, amount):
        sender_account = self.get_account(sender_account_number)
        receiver_account = self.get_account(receiver_account_number)
        sender_account.withdraw(amount)
        receiver_account.deposit(amount)

    def get_total_balance(self, client):
        total_balance = 0
        for account in self.accounts.values():
            if account.client == client:
                total_balance += account.balance
        return total_balance


client1 = Client("John", 1)
client2 = Client("Jane", 2)

bank = Bank()
bank.create_account(client1, 1000)
bank.create_account(client2, 2000)

print(bank.get_total_balance(client1))  # 1000
print(bank.get_total_balance(client2))  # 2000

bank.transfer(1, 2, 500)

print(bank.get_total_balance(client1))  # 500
print(bank.get_total_balance(client2))  # 2500
