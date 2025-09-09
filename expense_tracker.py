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

    if more == "Y":
        print("Y selected")
        # Add to dictionary
        expenses[category] = amount
    
    else:
        print("N selected")
        # Add to dictionary
        expenses[category] = amount
        break

print(expenses)