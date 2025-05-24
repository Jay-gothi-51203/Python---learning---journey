balance = 0 # 

transactions = [] # empty list which saves transaction of user

# Function named "add_income" which calculate income.
def add_income(amt,des):
    global balance
    balance += amt #add amt to balance
    transactions.append(("Income",amt,des)) # add income to the list named "transactions"
    print(f"✅Added Money: {amt} for {des}")
    print(f"💰 New balance: ${balance:.2f}")

# Function named "add_expenses" which calculate expenses.
def add_expenses(amt,des):
    global balance

    if amt > balance:
     print("⚠️ Not enough balance to make this expense.")
    else:
     balance -= amt
     transactions.append(("Expenses",amt,des)) # add expense to the list named "transactions"
     print(f"Added Expense: {amt:.2f} for {des}")

# Function named "view_balance" which shows balance.
def view_balance():
    print(f"\n Current Balance: ₹{balance:.2f}")
    

# Function named "view_all_transaction" which shows all the transaction.
def view_all_transactions():
    if not transactions:
        print("No transactions recorded yet.")

    else:
      print(f"Total Transactions: {len(transactions)}")
      print("Transaction History:")
      for transaction in transactions:
        print(transaction)


# while loop for menu and user choice
while True:
      print("\n---- Budget Tracker Menu ----")
      print("1. Add Income")
      print("2. Add Expense")
      print("3. View Balance")
      print("4. View All Transactions")
      print("5. Exit")

      try:
       choice = int(input("Choose an option (1-5): ")) #Take input from user or take choice of user's

      except ValueError:
       print("⚠️ Please enter a valid number.")
       continue

      if choice == 1: #If user press 1 means he/she wants to add money
       amt = float(input("Enter the amount you want to add: ")) #It takes the amount which user wants to add money.
       des = input("Enter the description: ") # It takes the description from user
       add_income(amt,des) # calling a function

      elif choice == 2: #If user press 2 means he/she wants to add enpenses.
       amt = float(input("Enter the amount that you spent: ")) #It takes the amount which user wants to add expenses.
       des = input("Enter the description: ") # It takes the description from user
       add_expenses(amt,des) # calling a function 

      elif choice == 3: # If user press 3 means he/she wants to view the balance
        view_balance() # calling a function 

      elif choice == 4: # If user press 4 means he/she wants to view all the transactions.
        view_all_transactions() # calling a function 

      elif choice == 5: # If user press 5 means he/she wants to exit.
        print("👋 Exiting, Have a nice day!")
        break # it will take out user from the program.

      else: # If user give invalid input apart from 1 to 5 then it will print below line.
       print("⚠️ Invalid choice, Enter number between 1 to 5 for your service. ")