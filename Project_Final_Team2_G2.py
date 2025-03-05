import os
import csv
import datetime
import pandas as pd

# Load the real dataset (CSV)
def load_data(filename='expenses_income.csv'):
    if not os.path.exists(filename):
        print(f"File {filename} does not exist.")
        return None
    return pd.read_csv(filename)

# Add an expense to the CSV file
def add_expense(date, amount, category, description, filename='expenses_income.csv'):
    new_expense = pd.DataFrame([[date, amount, category, description]], columns=['Date', 'Amount', 'Category', 'Description'])
    new_expense.to_csv(filename, mode='a', header=False, index=False)
    print('Expense added')

# View all expenses
def view_expenses(filename='expenses_income.csv'):
    df = load_data(filename)
    if df is not None:
        print(df)

# Filter expenses by date or category
def filter_expenses(filter_by, filter_value, filename='expenses_income.csv'):
    df = load_data(filename)
    if df is not None:
        filtered_df = df[df[filter_by].str.contains(filter_value, case=False)]
        print(filtered_df)

# Delete an expense from the CSV file
def delete_expense(date, amount, category, description, filename='expenses_income.csv'):
    df = load_data(filename)
    if df is not None:
        df = df[~((df['Date'] == date) & (df['Amount'] == amount) & (df['Category'] == category) & (df['Description'] == description))]
        df.to_csv(filename, index=False)
        print('Expense deleted')

# Monthly Summary and Advice
def monthly_summary(filename='expenses_income.csv'):
    current_month = datetime.datetime.now().strftime('%Y-%m')
    df = load_data(filename)
    if df is not None:
        df['Date'] = pd.to_datetime(df['Date'])
        df['Month'] = df['Date'].dt.strftime('%Y-%m')
        
        current_month_data = df[df['Month'] == current_month]
        total_income = current_month_data[current_month_data['Amount'] > 0]['Amount'].sum()
        total_expense = current_month_data[current_month_data['Amount'] < 0]['Amount'].sum()
        category_expense = current_month_data[current_month_data['Amount'] < 0].groupby('Category')['Amount'].sum()

        print(f'Total income for {current_month}: {total_income}')
        print(f'Total expense for {current_month}: {total_expense}')
        print(f'Expenses by category: \n{category_expense}')

        # Provide advice on budget balance
        if total_expense > total_income:
            print("Warning: Your expenses exceed your income! Consider cutting back on spending.")
        else:
            print("Great job! Your expenses are within your budget.")

# Main function to interact with the user
def main():
    filename = 'expenses_income.csv'

    while True:
        print('1. Add Expense')
        print('2. View Expenses')
        print('3. Filter Expense')
        print('4. Delete Expense')
        print('5. Monthly Summary')
        print('6. Exit')
        print()
        choice = input('Select any one: ')

        if choice == '1':
            date = input('Enter date(yyyy-mm-dd): ')
            amount = float(input('Enter amount: '))
            category = input('Enter category (Income, Food, Transport, Entertainment, Utilities, Other): ')
            description = input('Enter description: ')
            add_expense(date, amount, category, description, filename)

        elif choice == '2':
            view_expenses(filename)

        elif choice == '3':
            filter_by = input('Filter by (date/category): ')
            filter_value = input(f'Enter {filter_by}: ')
            filter_expenses(filter_by, filter_value, filename)

        elif choice == '4':
            date = input('Enter date(yyyy-mm-dd): ')
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            description = input('Enter description: ')
            delete_expense(date, amount, category, description, filename)

        elif choice == '5':
            monthly_summary(filename)

        elif choice == '6':
            print('Exit from program')
            break

        else:
            print('Invalid option')

if __name__ == '__main__':
    main()
