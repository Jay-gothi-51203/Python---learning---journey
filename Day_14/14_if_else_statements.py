# Topic : If else conditional staements.

# What is an if-else statement?
# It's a way to make decisions in your code.

# You tell Python:
# "If something is true, do this."
# "Else (if it's not true), do something else."

# if condition:
#     # code to run if condition is true
# else:
#     # code to run if condition is false

# Example: 
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

# What’s happening?
# Python checks if age >= 18
# If true, it prints "You are an adult."
# If false, it prints "You are a minor."


# ➕ elif: You can also add elif (else if):
# Syntax: 
# if condition:
    # code to run if condition is True
# elif another_condition:
      # code to run if the above condition is False and this one is True
# else:
      # code to run if all the above conditions are False


num = int(input("Enter the number: "))

if num > 0:
    print(f"{num} is positive.")

elif num < 0:
    print(f"{num} is negative.")

else:
    print(f"{num} is zero.")


######################  Practice Question  #####################

# 1.)Even or Odd Checker:Write a program that takes an integer input and prints whether it's even or odd.
num = int(input("Enter the number: "))

if num % 2 == 0:
    print("The number is even.")
else:
    print("the number is odd.22")


# 2.) Grade Calculator
# Input a student's marks (0–100) and print their grade:
# 90+ → A
# 80–89 → B
# 70–79 → C
# 60–69 → D
# <60 → F

percentage = int(input("Enter your percentage(%): "))


if percentage >= 90 and percentage <=100:
    print("congratulation!, you got 'A garde'.")

elif percentage >=80 :
    print("You got 'B garde'.")

elif percentage >=70:
    print("You got 'C garde'.")

elif percentage >=60:
    print("You got 'D garde.'")

elif percentage <60:
    print("You got 'F grade'.")

else:
    print("Enter the percentage between 0 - 100 %.")


# Age Group Classifier: Ask the user to enter their age and print which group they belong to:
# 0–12 → Child
# 13–19 → Teen
# 20–64 → Adult
# 65+ → Senior
Age = int(input("Enter your age: "))

if Age <= 12 and Age > 0:
    print("You are a child.")

elif Age <= 19:
    print("You are teenager.")

elif Age <= 64:
    print("You are an adult.")

elif Age >= 65 and Age <=100:
    print("You are a Senior.")

# Number Comparison: Take two numbers as input and print:
# First is greater
# Second is greater
# Both are equal
first_num = int(input("Enter the first number: "))

second_num = int(input("Enter the second number: "))

if first_num > second_num:
    print(f"{first_num} is greater than {second_num}.")

elif second_num > first_num: 
    print(f"{second_num} is greater than {first_num}.")

else:
    print(f"{first_num} and {second_num} are same.")

# 4.) Leap Year Checker: Ask the user to input a year and print whether it's a leap year or not.
# (Hint: A year is leap if divisible by 4 and not 100, or divisible by 400)
current_year = int(input("Enter the current year: "))

if (current_year % 4 == 0 and current_year % 100 != 0) or (current_year % 400 == 0):
    print(f"{current_year} is a leap yaer.")

else:
    print(f"{current_year} is not a leap year.")


# 6.) Simple Login System: Ask the user to input a username and password.
# If both are correct, print "Login successful"
# If either is wrong, print "Invalid credentials"

data_user1_username = "jay123"
data_user1_password = "Gothi@123"

user1_username = input("Enter your username: ")

user1_password = input("Enter your password: ")

if user1_username == data_user1_username and user1_password == data_user1_password:
    print("Login successful.")

else:
    print("Login unsuccessful.")


# 🌟 Challenge: ATM Machine Simulation:
# Objective: Build a simple ATM program that allows a user to:
# Log in using a username and PIN
# Check balance
# Deposit money
# Withdraw money
# Exit

data_pin = 12345

username = input("Enter the username: ")
pin = input("Enter the pin: ")
balance = 5000

if username == data_user1_username and pin == data_pin:
   print("Login successful.")

   print('''
     1. Check Balance
     2. Deposit
     3. Withdraw
     4. Exit ''')

user_input = int(input("Press button 1 to 4 for above services. "))

if user_input == 1:
    print(f"Your balance is: {balance}")

elif user_input == 2:
    print(f"How much money you want to deposit: ")

elif user_input == 3:
    print(f"How much money you want to withdraw: ")

elif user_input == 4:
    print(f"Exit()")

else:
    print("Press button from 1 to 4.")

############################################  Improved version  ######################################

# ATM Machine Simulation

# Stored credentials
data_user1_username = "pjay"
data_user1_pin = "12345"
balance = 5000

# Login prompt
username = input("Enter your username: ")
pin = input("Enter your PIN: ")

# Check credentials 
if username == data_user1_username and pin == data_user1_pin:
    print("Login successful.")  

    print('''
    ===== ATM Menu =====
    1. Check Balance
    2. Deposit
    3. Withdraw
    4. Exit
    ''')

    user_input = int(input("Choose an option (1–4): "))

    if user_input == 1:
        print(f"Your current balance is ₹{balance}")

    elif user_input == 2:
        deposit_amount = int(input("Enter amount to deposit: ₹"))
        if deposit_amount > 0:
            balance += deposit_amount
            print(f"₹{deposit_amount} deposited successfully. New balance: ₹{balance}")
        else:
            print("Invalid deposit amount!")

    elif user_input == 3:
        withdraw_amount = int(input("Enter amount to withdraw: ₹"))
        if 0 < withdraw_amount <= balance:
            balance -= withdraw_amount
            print(f"₹{withdraw_amount} withdrawn successfully. New balance: ₹{balance}")
        else:
            print("Insufficient balance or invalid amount!")

    elif user_input == 4:
        print("Thank you for using the ATM. Goodbye!")

    else:
        print("Invalid option. Please choose between 1 and 4.")

else:
    print("Login failed. Incorrect username or PIN.")
