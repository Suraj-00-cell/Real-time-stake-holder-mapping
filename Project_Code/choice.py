import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    clear_screen()
    menu = [
        "1. Get the statististical analysis of your uploaded file",
        "2. Get the Excel file - Grouped data with categorical sub group :Count and Percentage data of your uploaded file",
        "3. Get the Excel file - Grouped data :Count and Percentage data of your uploaded file",
        "4. Get the Visual (Bar and Pie chart) file (Save and View) - Grouped data with categorical sub group :Count and Percentage data of your uploaded file",
        "5. Get the Visual (Bar and Pie chart) file (Save and View) - Grouped data :Count and Percentage data of your uploaded file",
        "0. Exit"
    ]
    screen_width = os.get_terminal_size().columns
    menu_width = max(len(line) for line in menu)
    margin = (screen_width - menu_width) // 2

    print("\n" * (os.get_terminal_size().lines // 3))
    print(" " * margin + "CHOICE MENU")
    print("-" * screen_width)

    for line in menu:
        print(" " * margin + line)

    print("-" * screen_width)

def check_sales_statistics(choice):
    # Add your code to calculate and display sales statistics based on the chosen option
    # You can use if/elif statements to handle different choices

    if choice == '1':
        print("Choice 1 selected")
    elif choice == '2':
        print("Choice 2 selected")
    elif choice == '3':
        print("Choice 3 selected")
    elif choice == '4':
        print("Choice 4 selected")
    elif choice == '5':
        print("Choice 5 selected")


    # Wait for user to press Enter before returning to the menu
    input("\nPress Enter to continue...")
    show_menu()

def show_menu():
    print_menu()
    choice = int(input("Enter your choice (0-6): "))
    while choice not in [0, 1, 2, 3,4,5,6]:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (0-6): ")

    if choice == 0:
        clear_screen()
        print("Goodbye!")
    else:
        return choice
