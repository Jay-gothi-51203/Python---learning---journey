# 🔷 What is match-case in Python?
# The match-case statement is like a switch statement in other languages. It helps you compare one value against several patterns and execute code based on which pattern matches.

# It is like saying:
# "If the value is this, do that. If it's something else, do another thing."


#  Imagine a real-life example:

# You go to a vending machine, and you press a button for a drink.
# If you press 1, you get Coke.
# If you press 2, you get Pepsi.
# If you press 3, you get Water.
# If you press anything else, the machine says "Invalid choice".

# Syntax: 

#  match variable_name:
    # case value1:
         # Code to run if variable_name == value1
    # case value2:
         # Code to run if variable_name == value2
    # case value3:
         # Code to run if variable_name == value3
    # case _: (Default case, only one)
         # Code to run if none of the above match (default)

# Example:

print(''' We have three options for you:
    Option - 1: Press 1 to get a coke.
    Option - 2: Press 2 to get a pepsi.
    Option - 3: Press 3 to get a maza.
''')
choice = int(input("Enter the number: "))

match choice:
    case 1:
        print("You chose Coke")
    case 2:
        print("You chose Pepsi")
    case 3:
        print("You chose Water")
    case _:
        print("Invalid choice")



##############################  PRACTICE QUESTION  #################################

# 1.) 1. Day of the Week
# Write a program that asks the user to enter a number from 1 to 7 and uses match-case to print the name of the day (e.g., 1 = Monday, 2 = Tuesday, etc.). If the number is not between 1 and 7, print "Invalid day".

print(''' 
Press 1 for Monday.
Press 2 for Tuesday.
Press 3 for Wednesday.
Press 4 for Thursday.
Press 5 for Friday.
Press 6 for Saturday.
Press 7 for Sunday.
''')

Day = int(input("Enter the day: "))

match Day: #match Variable_name:
    case 1: #case value-1
        print("It's a Monday.")
    case 2: #case value-2
        print("It's Tuesday.")
    case 3: #case value-3
        print("It's Wednusday.")
    case 4: #case value-4
        print("It's Thursday.")
    case 5: #case value-5
        print("It's Friday.")
    case 6: #case value-6
        print("It's Saturday.")
    case 7: #case value-7
        print("It's Sunday.")
    case _: # Default case
        print("Invalid input. Please enter the day between 1 - 7 only.")

    
###################################################################################
# Practice question - 2: 2. Calculator
# Write a program that takes two numbers and an operator (+, -, *, /) and uses match-case to perform the correct operation and print the result.
# Example:
# Inputs:
# a = 10
# b = 5
# op = "*"
# Output: 50

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

op = input("Enter the operator ( +,-,*,/ ): ")

match op:
    case "+":
        print(f"Addition  of {a} and {b} is: ", a+b)
    case "-":
        print(f"Subtraction of {a} and {b} is: ", a-b)
    case "*":
        print(f"Multiplication of {a} and {b} is: ", a*b)
    case "/":
        print(f"Division of {a} and {b} is: ", a/b)
    case _:
        print("Invalid input, Enter valid operation from: (+,-,*,/)")


###########################################################################################
# Practice question - 3. Grade System : Ask the user to enter a letter grade (A, B, C, D, F) and use match-case to print a message:
# A → "Excellent"
# B → "Good"
# C → "Average"
# D → "Below Average"
# E -> "Just pass"
# F → "Fail"
# Anything else → "Invalid grade"

print("\n Enter your grade below in capital (A TO F).")

Grade = input("\n Enter your Grade: ")

match Grade:
    case "A":
        print("Excellent, you are a genius.")
    case "B":
        print("Good")
    case "C":
        print("Average")
    case "D":
        print("Below Average")
    case "E":
        print("Just pass")
    case "F":
        print("Fail")
    case _:
        print("Invalid input, please select grade from A to F.")


##############################################################################
# 4. Traffic Light
# Ask the user to input a traffic light color (red, yellow, green) and use match-case to display what the driver should do:
# red → "Stop"
# yellow → "Slow down"
# green → "Go"
# other → "Invalid color"

print("\nEnter the color from these: (Red, Yellow, Green) below")

color = input("Enter the color: ")

match color:
    case "Red":
        print("Stop your car and turn off the ignition if you have more than 20 second.")
    case "Yellow":
        print("Turn on the ignition.")
    case "Green":
        print("Now, you can go.")
    case _:
        print("Invalid input, You can select only three colors. (Red, Yellow, Green). ")


#######################################################
# 5. Month Days Checker
# Ask the user to input a month (January, February, etc.) and use match-case to print how many days are in that month. For February, print "28 or 29 days".

print('''\n Select one month from these(Do not make spelling mistake.): (January, February, March, April, May, June, July, August, September, October, November, and December.)

''')
month = input("Enter the month: ")

match month:
    case "January"| "March" | "May" | "July" | "August" | "October" | "December" :
        print(f"{month} has 31 days.")
    
    case "April" | "June" | "September" | "November" :
        print(f"{month} has 30 days.")

    case "February":
        print(f"{month} has 28 or 29 days. In leap year 29 days and in normal year 28 days.")