import csv
import os

def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    return []

def save_data(filename, data):
    with open(filename, 'w', newline='') as file:
        fieldnames = data[0].keys() if data else []
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def add_expense(data, date, category, amount):
    data.append({'Date': date, 'Category': category, 'Amount': amount})

def generate_report(data, month, year):
    total_expenses = 0
    for entry in data:
        if entry['Date'].month == month and entry['Date'].year == year:
            total_expenses += float(entry['Amount'])
    
    return total_expenses

def main():
    filename = 'expenses.csv'
    data = load_data(filename)

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. Generate Monthly Report")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = input("Enter amount: ")
            add_expense(data, date, category, amount)
            save_data(filename, data)
            print("Expense added successfully!")

        elif choice == '2':
            month = int(input("Enter month (1-12): "))
            year = int(input("Enter year: "))
            total_expenses = generate_report(data, month, year)
            print(f"Total expenses for {month}-{year}: ${total_expenses:.2f}")

        elif choice == '3':
            break

if __name__ == "__main__":
    main()
