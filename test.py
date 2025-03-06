import csv
import os

class Transaction:
    def __init__(self, amount, date, category, description=None, payment_mode=None):
        self.amount = amount
        self.date = date
        self.category = category
        self.description = description
        self.payment_mode = payment_mode

    def __str__(self):
        return f"{self.date} - {self.category}: ${self.amount}, {self.payment_mode}, {self.description}"

class Expense(Transaction):
    pass

class Income(Transaction):
    pass

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.is_admin = True

class Report:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def generate_report(self):
        income = sum(t.amount for t in self.transactions if isinstance(t, Income))
        expenses = sum(t.amount for t in self.transactions if isinstance(t, Expense))
        balance = income - expenses
        print(f"Total Income: ${income}")
        print(f"Total Expenses: ${expenses}")
        print(f"Balance: ${balance}")

        if balance < 0:
            print("\nWarning: You are overspending!")
            print("Here are some suggestions to improve your finances:")
            if expenses > 1.5 * income:
                print("- Your expenses are significantly higher than your income. Consider cutting unnecessary expenses.")
            if any(t.category.lower() == 'entertainment' for t in self.transactions if isinstance(t, Expense)):
                print("- You are spending a lot on entertainment. Try reducing entertainment expenses.")
            if any(t.category.lower() == 'food' for t in self.transactions if isinstance(t, Expense)):
                print("- Food expenses are high. Cooking at home can help reduce costs.")
            print("- Track your daily expenses and prioritize essential spending only.")
        
    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description", "Payment Mode"])
            for t in self.transactions:
                writer.writerow([t.date, t.category, t.amount, t.description, t.payment_mode])

    def load_from_csv(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    date, category, amount, description, payment_mode = row
                    amount = float(amount)
                    if amount < 0:
                        self.add_transaction(Expense(amount, date, category, description, payment_mode))
                    else:
                        self.add_transaction(Income(amount, date, category, description, payment_mode))

    def load_sample_data(self):
        # Pre-adding some transactions (sample data)
        transactions = [
            Expense(50.00, "2025-03-01", "Food"),
            Expense(20.00, "2025-03-02", "Transport"),
            Expense(30.00, "2025-03-03", "Food"),
            Expense(15.00, "2025-03-04", "Entertainment"),
            Expense(25.00, "2025-03-05", "Transport"),
            Income(2000.00, "2025-03-06", "Salary"),
            Expense(45.00, "2025-03-07", "Food"),
            Expense(10.00, "2025-03-08", "Transport"),
            Expense(40.00, "2025-03-09", "Food"),
            Expense(60.00, "2025-03-10", "Entertainment")
        ]
        for transaction in transactions:
            self.add_transaction(transaction)

users = [Admin("admin", "admin123"), User("user1", "user123")]

def register():
    username = input("Enter new username: ")
    password = input("Enter new password: ")
    users.append(User(username, password))
    print(f"Account created successfully for {username}!")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    for user in users:
        if user.username == username and user.password == password:
            return user
    print("Invalid credentials. Do you want to create a new account? (yes/no)")
    choice = input().lower()
    if choice == "yes":
        register()
        return login()
    return None

def main():
    user = login()
    if not user:
        return

    report = Report()
    # Load the sample data for demo purposes
    report.load_sample_data()

    while True:
        if isinstance(user, Admin):
            action = input("(view/manage/exit): ").lower()
            if action == "view":
                report.generate_report()
            elif action == "manage":
                username = input("Enter username to manage: ")
                report.load_from_csv(f"{username}_transactions.csv")
                report.generate_report()
            elif action == "exit":
                break
        else:
            action = input("(add/report/exit): ").lower()
            if action == "add":
                amount = float(input("Amount: "))
                date = input("Date: ")
                category = input("Category: ")
                desc = input("Description: ")
                payment_mode = input("Payment Mode: ")
                transaction = Expense(amount, date, category, desc, payment_mode) if amount < 0 else Income(amount, date, category, desc, payment_mode)
                report.add_transaction(transaction)
            elif action == "report":
                report.generate_report()
                report.save_to_csv(f"{user.username}_transactions.csv")
            elif action == "exit":
                break

if __name__ == "__main__":
    main()
