# Create the dictionary
expenses = { }
category = ""
amount = 0
more = "Y"

while more != "N":
    # Get user input
    print("Enter category: ")
    category = input()

    print("Enter amount spent: ")
    amount = input()

    print("Enter more? Y or N: ")
    more = input()

    if(more == "Y" or more == "y"):
        print("Y selected")

        # Add to dictionary
        expenses[category] = amount
    
    elif(more == "N" or more == "n"):
        print("N selected")

        # Add to dictionary
        expenses[category] = amount
        break

print("\nPrinting out Expense List")

# Loop to print out all dictionary items
for key, value in expenses.items():
    print("Category:", key, "Amount:", value)