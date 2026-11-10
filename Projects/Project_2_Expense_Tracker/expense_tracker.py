# Project 2 - Expense Tracker : DecodeLabs

print ("-" * 40)
print ("       Personal Epense Tracker     ")
print ("-" * 40)

print("Welcome! Track Your Expenses.")
print("Enter an Expense Amount.")
print("Type 'quit' to Exist!\n")

# Initializing Total

total = 0
transaction_count = 0 
expenses = []

# Countinuous Expense Entry 

while True :

    user_input = input("Enter Expense:").strip()

    # Kill switch 
    if user_input.lower() =='quit':
        break

    # Validate Process Input 
    try:
        new_expense = int (user_input)

        if new_expense <= 0 :
            print("Please Enter a Positive Expense!\n")
            continue

        # Storing Indiviual Entry 
        expenses.append(new_expense)

        # Accumulator
        total = total + new_expense
        transaction_count += 1 

        print("Expense added successfully!")
        print(f"Current Total: ${total:.2f}\n")  # Formatting Total Amount E.g $ 10.00

    except ValueError:
        print("Invalid Input! Please enter a number")

# Display All Expenses 
print ("\n" + "-" * 40)
print ("           All Expense Enteries")
print ("-" * 40)
for index , expense in enumerate(expenses ,start=1):
    print(f"Transaction {index} : ${expense:.2f}")

# Final Output 
print ("-" * 40)
print ("        FINAL SUMMARY")
print ("-" * 40)

print (f"Total Transactions: {transaction_count}")
print (f"FINAL TOTAL : ${total:.2f}")

print ("\nThank you for using Expense Tracker!")
print ("-" * 40)



