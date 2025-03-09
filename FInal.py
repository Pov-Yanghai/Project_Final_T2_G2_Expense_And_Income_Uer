import csv
import os
import sys
from abc import ABC, abstractmethod
from datetime import datetime
import pandas as pd

# Clear screen for Window, Mac and Linux
def clear_screen():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

# Transaction class
class Transaction(ABC):
    def __init__(self, amount , date , description , currency):
        self.amount = amount
        self.date = date
        self.description = description
        self.currency = currency
    @abstractmethod
    def get_type(self):
        pass
    @abstractmethod
    def __str__(self):
        pass
# Income class
class Income(Transaction):
    # inherit from Transaction
    def get_type(self):
        # return Income type as string
        return "income"
    def __str__(self):
        # return transaction type as string
        return f"{self.date} - {self.currency}{self.amount} - {self.description}"  
# Expense class
class Expense(Transaction):
    # inherit from Transaction
    def get_type(self):
        # return Expense type as string
        return "expense"
    def __str__(self):
        # return transaction type as string
        return f"{self.date} - {self.currency}{self.amount} - {self.description}"
# Transaction report class
class Report:
    pass
# User class
class User:
    pass
# Admin class
class Admin:
    pass
# Main program
def main():
    while True:
        clear_screen()
        print("Welcome to our system")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Choose option: ")
        if choice == "1":
            username = input("Username: ").strip()
            password = input("Password: ").strip()
        elif choice == "2":
            fullname = input("Full name: ")
            username = input("Username: ").strip()
            password = input("Password: ").strip()
        elif choice == "3":
            print("Goodbye")
            break
        else:
            print("Invalid choice")
            input("Press any key to continue...")

if __name__ == "__main__":
    main()
