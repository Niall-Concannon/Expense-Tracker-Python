import json
import os

# Create the dictionary - Variables
expenses = { }
category = ""
amount = 0
option = 0

# Load from file - os import needed to check if path exists
isExist = os.path.exists("expenses.txt")

if isExist == True:
    print("Previous file found. Do you want to load file? Y or N:")
    choice = input()

    if choice == "Y" or choice == "y":
        print("Loading file.")

        with open ("expenses.txt", "r") as fp:
            expenses = json.load(fp)
    else:
        print("Not loading file.")
    
else:
    print("No previous file found.")

while option != 4:

    print("1. Add expense\n2. Edit expense amount\n3. Delete expense\n4. Exit")
    option = int(input())

    if option == 1:
        print("Option 1 selected.")
        
        # --- Get category ---
        print("Enter category: ")
        
        while True:
            category = input()

            if not category.isalpha():
                print("Please enter letters: ")

            else:
                break
        
        # --- Get amount ---
        print("Enter amount spent: ")

        while True:
            amount = input()

            if not amount.isdigit():
                print("Please enter a number: ")
            
            else:
                break

        # Add to dictionary
        expenses[category] = amount

    elif option == 2:
        print("Option 2 selected.")

        print("Please enter category to change:")
        category = input()

        # Check if category exists
        if category not in expenses:
            print("Category not found exiting.")
            continue

        print("Please enter new amount:")
        amount = input()

        expenses[category] = amount

    elif option == 3:
        print("Option 3 selected.")

        print("Please enter category to delete:")
        category = input()

        # Check if category exists
        if category not in expenses:
            print("Category not found exiting.")
            continue

        print("Deleting category from dictionary")
        expenses.pop(category)

    elif option == 4:
        print("Exiting program.")

        if bool(expenses) == True:
            print("\nPrinting out Expense List")

            # Loop to print out all dictionary items
            for key, value in expenses.items():
                print("Category:", key, "Amount:", value)

            # Write to file
            with open("expenses.txt", "w") as fp:
                json.dump(expenses, fp)

    else:
        print("No option chosen. Try again.")