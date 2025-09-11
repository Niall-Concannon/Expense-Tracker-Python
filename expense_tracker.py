import json
import os

# Create the dictionary - Variables
expenses = { }
category = ""
amount = 0
more = "Y"

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

while more != "N" or more != "n":

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

    # --- Get user input on more data ---
    print("Enter more? Y or N: ")

    while more != "Y" or more != "y" or more != "N" or more != "n":
        more = input()
        
        if(more == "Y" or more == "y"):
            print("Y selected")

            # Add to dictionary
            expenses[category] = amount
            break
        
        elif(more == "N" or more == "n"):
            print("N selected")

            # Add to dictionary
            expenses[category] = amount
            break

        else:
            print("Y or N not selected. Try again")

    # if statement to break if n was selected
    if more == "N" or more == "n":
        break

# --- End of main while loop

print("\nPrinting out Expense List")

# Loop to print out all dictionary items
for key, value in expenses.items():
    print("Category:", key, "Amount:", value)

# Write to file
with open("expenses.txt", "w") as fp:
    json.dump(expenses, fp)