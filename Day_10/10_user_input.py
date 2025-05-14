# Taking user input in python. 

# Taking user input: Input means your program is asking the user to type something.

#  How to take input?
# Syntax of input:
# input("Write your message here.")
# "Write your message here" The message will be shown to the user.


# Example 1: Ask for a name
Name = input(" What is your name ? ") # this will take input as string because we didn't specify.

# print("Hello " , Name , "!") #If you want to joint name using variable and it is string then use +
# Output:
# It shows: What is your name?
# You type: Jay
# It says: Hello Jay!

# Example 2: Ask for age (a number)
Age = input("Enter your age: ") # This will take your age as string.
print(type(Age)) # to check what data type age is 

# If you want to take input as integer or float you need to write int or float before input like this.
# Syntax: 
# 1.) Integer: Age = int(input("Enter your age: "))
# 2.) Float: Price = float(input("Enter the price: "))

Age = int(input("Enter your age: "))
# print(type(Age))
# print("You are", Age , "years old.")

price = float(input("Enter the price: "))
# print(type(price))

# print("The price of the iteam is: ",price)


##################################  Practice Question  ###############################

# 1. Ask the user's name
#  Ask the user their name and print a welcome message.
NAME = input("What is your name: ")
print("Welcome "+ NAME + "!")

# 2. Add two numbers
# Ask the user to enter two numbers and print the sum.
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print("The sum is: ",a+b)

# 3. Find the user's age next year
# Ask for the user's age and tell them how old they will be next year.
NextYear_AGE = int(input("Enter your age: "))
print("Next year you will", NextYear_AGE + 1, "years old.")

# 4. Simple calculator
# Ask the user for two numbers and print:
# The sum
# The difference
# The product

A = float(input("Enter the first value: "))
b = float(input("Enter the second value: "))

print("The sum: ",a+b)
print("The difference: ",a-b)
print("The Product: ",a*b)

# 5. Area of a rectangle
#  Ask for the length and width, then calculate the area.
# Formula:
# area = length * width
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

print("Area of rectangle is: ",length * width)

# 6. Greet with time of day
#  Ask the user's name and time of day (morning/afternoon/evening), then greet them.
what_yourname = input("Enter your name: ")
time = input("What is the time of the day ?")

print("Good " + time +  what_yourname +"!")

# 7. Convert temperature
# Ask the user for temperature in Celsius, and convert it to Fahrenheit.
# Formula:
# F = (C × 9/5) + 32

C = float(input("Enter temperature in celcius: "))

F = (C * 9/5) + 32

print("The temperature in Fehrenhit is: ",F)