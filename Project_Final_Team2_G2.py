import csv
import os

# Class to represent a generic Transaction (expense or income)   
class Transaction:
    def __init__(self, amount, date, category):
        # Initialize with amount, date, and category (type)
        self.amount = amount  
        self.date = date  
        self.category = category  

    def __str__(self):
        # Return string representation of the transaction (for printing)
        return f"{self.date} - {self.category}: ${self.amount}"

# Class to represent an expense, which inherits from Transaction
class Expense(Transaction):
    def __init__(self, amount, date, category):
        # Initialize expense with the same parameters as Transaction
        # vornsin complete this place

        pass  # To be implemented 

# Class to represent income, which also inherits from Transaction
class Income(Transaction):
    def __init__(self, amount, date, source):
        # Initialize income with amount, date, and source (category)
        self.amount = amount
        self.date = date
        self.source = source
        
    
       

# A class to handle the report, which tracks all expenses and income
class Report:
    def __init__(self):
        # Initialize lists to store expenses and income
        self.expenses = []  
        self.income = []  

    def add_expense(self, expense):
        # Add expense to the report
        pass  # To be implemented

    def add_income(self, income):
        # Add income to the report
        pass  # To be implemented 

    def total_income(self):
        # Calculate total income from all income transactions
        pass  # To be implemented 

    def total_expenses(self):
        # Calculate total expenses from all expense transactions
        pass  # To be implemented 

    def balance(self):
        # Calculate balance (Income - Expenses)
        pass  # To be implemented 

    def generate_report(self):
        # Print expenses, income, and summary (balance)
        pass  # To be implemented 

    def save_to_csv(self):
        # Save the transactions (expenses and income) to CSV
        pass  # To be implemented 

    def load_from_csv(self):
        # Load transactions from CSV and re-create expense/income objects
        pass  # To be implemented 

# Function to simulate adding transactions (either expense or income)
def add_transaction(report):
    # Prompt user to enter transaction details (type, amount, date, category)
    pass  # To be implemented 

# Main function to drive the process (for Week 3)
def main():
    # Initialize report object
    report = Report()

    # Load previous transactions from CSV (if any)
    report.load_from_csv()

    # Main menu for adding transactions, generating reports, and saving data
    while True:
        # Display options for the user
        pass  # To be implemented 

if __name__ == "__main__":
    main()
