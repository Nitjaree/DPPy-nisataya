#!/usr/bin/python3
# import os
import sys



def clear_screen():
    # """Clears the terminal screen for a clean UI look."""
    # os.system('cls' if os.name == 'nt' else 'clear')
    print("\x1b[2J\x1b[H")

def calculate_balance(transactions, opening_balance):
    balance = opening_balance    
    for transaction in transactions:        
        if transaction["type"] == "income":            
            balance += transaction["amount"]        
        else:            
            balance -= transaction["amount"]
    return balance

def view_balance():
    clear_screen()
    opening_balance = float(input("Please input opening balance : "))
    print(calculate_balance(transactions,opening_balance))
    input("\nPress Enter to return to the main menu...")

def typeis():
    clear_screen()
    print (type(transactions))
    print()
    print (type(settings))
    input("\nPress Enter to return to the main menu...")

def show_greeting():
    clear_screen()
    print("=== GREETING SECTION ===")
    print("\nHello! Welcome to the Python CLI Main Menu demo.")
    input("\nPress Enter to return to the main menu...")

def calculate_sum():
    clear_screen()
    print("=== CALCULATE SUM ===")
    try:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"\nThe result of {num1} + {num2} is: {num1 + num2}")
    except ValueError:
        print("\n[Error] Invalid input. Please enter numbers only.")
    
    input("\nPress Enter to return to the main menu...")

def under_construct():
    clear_screen()
    print("This function under construction")
    input("\nPress Enter to return to the main menu...")

def display_menu():
    """Prints the actual main menu layout."""
    clear_screen()
    print("=====================================")
    print("             MAIN MENU               ")
    print("=====================================")
    print(" 1. Add Transaction")
    print(" 2. View Transactions")
    print(" 3. Edit / Delete Transaction")
    print(" 4. Search & Filter")
    print(" 5. Financial Summary")
    print(" 6. Cash Runway Prediction")
    print(" 7. Can I Afford It?")
    print(" 0. Exit Program")
    print("=====================================")

def main():
    while True:
        display_menu()
        choice = input("Select an option (0-7): ").strip()

        match choice:
            case "1":
                show_greeting()
            case "2":
                view_balance()
            case "3":
                calculate_sum()
            case "9":
                typeis()
            case "0":
                clear_screen()
                print("Exiting program. Goodbye!\n")
                sys.exit()
            case _transactions:
                under_construct()

transactions = [    {        "id": 1,        "type": "income",        "category": "Salary",        "amount": 9000,        "recurring": True,        "description": "Monthly salary"    },    {        "id": 2,        "type": "expense",        "category": "Rent",        "amount": 6000,        "recurring": True,        "description": "Monthly rent"    },    {        "id": 3,        "type": "expense",        "category": "Food",        "amount": 4000,        "recurring": True,        "description": "Monthly food budget"    }]
settings = {    "opening_balance": 5000,    "minimum_reserve": 2000,    "next_id": 4}
if __name__ == '__main__':
    main()
