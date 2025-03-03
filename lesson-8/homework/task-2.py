import random
from pathlib import Path


class Account:
    def __init__ (self, account_number, name, balance=0):
        self.account_number = account_number 
        self.name = name
        self.balance = balance

    def to_string(self):
        return f"{self.account_number},{self.name},{self.balance}\n"

    @staticmethod
    def from_string(line):
        account_number, name, balance = line.strip().split(',')
        return Account(account_number, name, float(balance))

class Bank:
    file = Path(r"D:\Python\python-homework\lesson-8\homework\accounts.txt")
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        account_number = "2025" + str(random.randint(1000, 9999))
        if account_number in self.accounts:
            return "Account creation failed. Try again."
        new_account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = new_account
        self.save_to_file()
        return f"Account created successfully! Your account number is {account_number}."

    def view_account(self, account_number):
        if account_number in self.accounts:
            acc = self.accounts[account_number]
            return f"Account Number: {acc.account_number}, Name: {acc.name}, Balance: ${acc.balance}"
        return "Account not found."

    def deposit(self, account_number, amount):
        if amount <= 0:
            return "Invalid deposit amount."
        if account_number in self.accounts:
            self.accounts[account_number].balance += amount
            self.save_to_file()
            return f"Deposit successful! New balance: ${self.accounts[account_number].balance}"
        return "Account not found."

    def withdraw(self, account_number, amount):
        if amount <= 0:
            return "Invalid withdrawal amount."
        if account_number in self.accounts:
            if self.accounts[account_number].balance >= amount:
                self.accounts[account_number].balance -= amount
                self.save_to_file()
                return f"Withdrawal successful! New balance: ${self.accounts[account_number].balance}"
            return "Insufficient funds."
        return "Account not found."

    def save_to_file(self):
        with open(self.file, 'w') as file:
            for acc in self.accounts.values():
                file.write(acc.to_string())

    def load_from_file(self):
        with open(self.file, 'r') as file:
                self.accounts = {}
                for line in file:
                    acc = Account.from_string(line)
                    self.accounts[acc.account_number] = acc

def menu():
    bank = Bank()
    while True:
        print("\nBANKING SYSTEM MENU")
        print("1. Create an Account")
        print("2. View Account Details")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter your name: ")
            initial_deposit = float(input("Enter initial deposit amount: "))
            print(bank.create_account(name, initial_deposit))
        elif choice == "2":
            acc_number = input("Enter your account number: ")
            print(bank.view_account(acc_number))
        elif choice == "3":
            acc_number = input("Enter your account number: ")
            amount = float(input("Enter deposit amount: "))
            print(bank.deposit(acc_number, amount))
        elif choice == "4":
            acc_number = input("Enter your account number: ")
            amount = float(input("Enter withdrawal amount: "))
            print(bank.withdraw(acc_number, amount))
        elif choice == "5":
            print("Thank you for using our bank!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
