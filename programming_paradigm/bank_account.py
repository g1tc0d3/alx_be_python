class BankAccount:
    def __init__(self, account_balance =0):
        self.account_balance = account_balance

    def deposit (self, amount):
        self.amount = input("Enter amount to deposit: ")
        self.account_balance += amount
        print (self.account_balance)

    def withdraw (self, amount):
        self.amount = input ("Enter amount to withdraw: ")
        self.account_balance -= amount
        print (self.account_balance)

        