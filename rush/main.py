import os
import sys



def clear_screen():
    """Clears the terminal screen for a clean UI look."""
    os.system('cls' if os.name == 'nt' else 'clear')

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

def display_menu():
    """Prints the actual main menu layout."""
    clear_screen()
    print("=====================================")
    print("             MAIN MENU               ")
    print("=====================================")
    print(" 1. Add Transaction")
    print(" 2. Calculate Sum")
    print(" 0. Exit Program")
    print("=====================================")
1. Add Transaction 2. View Transactions 3. Edit / Delete Transaction 4. Search & Filter 5. Financial Summary 6. Cash Runway Prediction 7. Can I Afford It? 8. Exit Enter choice: _

def main():
    while True:
        display_menu()
        choice = input("Select an option (0-2): ").strip()

        match choice:
            case "1":
                show_greeting()
            case "2":
                calculate_sum()
            case "0":
                clear_screen()
                print("Exiting program. Goodbye!\n")
                sys.exit()
            case _:
                print("\n[Invalid Selection] Please choose a valid option.")
                input("Press Enter to try again...")

if __name__ == '__main__':
    main()
