import csv
from datetime import datetime

class Transaction:
    def __init__(self, amount, date, category):
        self.amount = amount
        self.date = datetime.strptime(date, "%Y-%m-%d") if isinstance(date, str) else date
        self.category = category

    def to_dict(self, type):
        return {"Type": type, "Amount": self.amount, "Date": self.date.strftime("%Y-%m-%d"), "Category": self.category}

class Expense(Transaction):
    pass

class Income(Transaction):
    pass

class Report:
    def __init__(self):
        self.expenses = []
        self.income = []

    def add_expense(self, amount, date, category):
        self.expenses.append(Expense(amount, date, category))

    def add_income(self, amount, date, category):
        self.income.append(Income(amount, date, category))

    def total_income(self):
        return sum(income.amount for income in self.income)

    def total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

    def balance(self):
        return self.total_income() - self.total_expenses()

    def generate_report(self):
        print("Income:")
        for inc in self.income:
            print(f"{inc.date.strftime('%Y-%m-%d')} - {inc.category}: ${inc.amount}")
        
        print("\nExpenses:")
        for exp in self.expenses:
            print(f"{exp.date.strftime('%Y-%m-%d')} - {exp.category}: ${exp.amount}")
        
        print("\nSummary:")
        print(f"Total Income: ${self.total_income()}")
        print(f"Total Expenses: ${self.total_expenses()}")
        print(f"Balance: ${self.balance()}")
        
        if self.total_income() < self.total_expenses():
            print("\nWarning: You are overspending!")
            print("- You should consider cutting back on unnecessary expenses!")
            print("- Track your daily expenses and prioritize essential spending only.")
            
        elif self.total_expenses() >= 0.8 * self.total_income():
            print("\nWarning: You are spending too much on expenses!")
            print("- You have spent more than 80% of your income")
            print("- Track your daily expenses and prioritize essential spending only.")

    def save_to_csv(self, filename="transactions.csv"):
        with open(filename, mode="w", newline="") as file:
            fieldnames = ["Type", "Amount", "Date", "Category"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for inc in self.income:
                writer.writerow(inc.to_dict("income"))
            for exp in self.expenses:
                writer.writerow(exp.to_dict("expense"))

    def load_from_csv(self, filename="transactions.csv"):
        try:
            with open(filename, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["Type"] == "income":
                        self.add_income(float(row["Amount"]), row["Date"], row["Category"])
                    elif row["Type"] == "expense":
                        self.add_expense(float(row["Amount"]), row["Date"], row["Category"])
        except FileNotFoundError:
            print("No previous transactions found.")

def user_input_transaction(report):
    while True:
        print("\nTransaction details")
        type_ = input("Enter type (income/expense): ").strip().lower()
        if type_ not in ["income", "expense"]:
            print("Invalid type. Please enter 'income' or 'expense'.")
            continue
        
        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue
        
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category: ").strip()
        if not category:
            print("Category cannot be empty. Please enter a valid category.")
            continue
        
        if type_ == "income":
            report.add_income(amount, date, category)
        else:
            report.add_expense(amount, date, category)
        
        another = input("Do you want to add another transaction? (yes/no): ").strip().lower()
        if another != "yes":
            break

# Example Usage
report = Report()
user_input_transaction(report)
report.generate_report()
report.save_to_csv()
