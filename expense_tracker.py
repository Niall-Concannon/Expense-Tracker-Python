# Create the dictionary
expenses = { }

# Get user input
print("Enter category: ")
category = input()

print("Enter amount spent: ")
amount = input()

# Add to dictionary
expenses[category] = amount
print(expenses)